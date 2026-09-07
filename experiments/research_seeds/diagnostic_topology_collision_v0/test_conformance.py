import unittest

from conformance import Condition, EpisodeSpec, episode_specs, run_episode, validate_contract
from protocol import Diagnostic, Topology
from representation import make_history


class ConformanceComponentTests(unittest.TestCase):
    def test_episode_family_is_exact(self):
        specs = episode_specs()
        self.assertEqual(len(specs), 8)
        self.assertEqual(
            {(s.topology, s.fault, s.nuisance) for s in specs},
            {
                (topology, fault, nuisance)
                for topology in (Topology.A, Topology.B)
                for fault in (0, 1)
                for nuisance in (0, 1)
            },
        )

    def test_g1_representative_episode_repairs(self):
        spec = EpisodeSpec(Topology.B, fault=1, nuisance=0)
        history = make_history(spec.topology, spec.nuisance)
        result = run_episode(Condition.G1, spec, history)
        self.assertIs(result.diagnostic, Diagnostic.QB)
        self.assertEqual(result.observation, 1)
        self.assertTrue(result.repair_success)
        self.assertEqual(result.budget_remaining, 0)

    def test_g0_representative_wrong_probe_fails_bounded_continuation(self):
        spec = EpisodeSpec(Topology.B, fault=0, nuisance=0)
        history = make_history(spec.topology, spec.nuisance)
        result = run_episode(Condition.G0, spec, history)
        self.assertIs(result.diagnostic, Diagnostic.QA)
        self.assertIsNone(result.observation)
        self.assertFalse(result.repair_success)
        self.assertEqual(result.failure, "NO_BOUNDED_ZERO_ERROR_CONTINUATION")
        self.assertEqual(result.budget_remaining, 1)

    def test_static_validator_checks_refrozen_structure(self):
        contract = validate_contract()
        self.assertEqual(contract["positive_episode_count_per_condition"], 8)
        self.assertTrue(contract["viable_policy_initial_action_collision_verified"])
        self.assertTrue(contract["representation_capacity_matched"])
        self.assertTrue(contract["controller_identity_matched"])
        self.assertTrue(contract["primitive_actions_matched"])
        self.assertTrue(contract["budget_matched"])
        self.assertTrue(contract["controller_selectability_structure_verified"])


if __name__ == "__main__":
    unittest.main()
