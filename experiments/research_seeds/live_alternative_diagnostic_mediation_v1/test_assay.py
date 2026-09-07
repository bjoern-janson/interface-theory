import unittest
from assay import Condition, EpisodeResult, ProtocolViolation, aggregate_results, positive_episode_specs, run_episode, validate_contract
from protocol import M00, M01, M10, M11, NULL_PAIR, Diagnostic, MediationStatus


class AssayTests(unittest.TestCase):
    def test_c0_succeeds_when_fixed_q0_discriminates(self):
        result = run_episode(Condition.C0, (M00,M10), M10)
        self.assertEqual((result.diagnostic,result.observation,result.resolved_model,result.repair,result.budget_remaining), ("q0",1,"M10","r10",0))
        self.assertTrue(result.discriminating)
        self.assertTrue(result.repair_success)

    def test_c0_has_no_bounded_zero_error_continuation_after_nondiscriminating_q0(self):
        result = run_episode(Condition.C0, (M00,M01), M01)
        self.assertEqual(result.diagnostic, "q0")
        self.assertEqual(result.observation, 0)
        self.assertIsNone(result.resolved_model)
        self.assertIsNone(result.repair)
        self.assertEqual(result.budget_remaining, 1)
        self.assertFalse(result.discriminating)
        self.assertFalse(result.repair_success)
        self.assertEqual(result.failure, "NO_BOUNDED_ZERO_ERROR_CONTINUATION")

    def test_c1_relation_selects_q1_then_world_evidence_resolves(self):
        result = run_episode(Condition.C1, (M00,M01), M01)
        self.assertEqual((result.diagnostic,result.observation,result.resolved_model,result.repair,result.budget_remaining), ("q1",1,"M01","r01",0))
        self.assertTrue(result.repair_success)

    def test_c1_is_pair_order_invariant(self):
        forward = run_episode(Condition.C1, (M00,M01), M01)
        reverse = run_episode(Condition.C1, (M01,M00), M01)
        self.assertEqual((forward.diagnostic,forward.resolved_model,forward.repair_success), (reverse.diagnostic,reverse.resolved_model,reverse.repair_success))

    def test_null_abstains_before_world_action(self):
        left, right = NULL_PAIR
        result = run_episode(Condition.C1, (left,right), left)
        self.assertEqual(result.diagnostic, MediationStatus.NO_DISCRIMINATING_DIAGNOSTIC.value)
        self.assertIsNone(result.observation)
        self.assertEqual(result.budget_remaining, 2)

    def test_square_diagonal_is_protocol_violation_not_episode_outcome(self):
        with self.assertRaises(ProtocolViolation):
            run_episode(Condition.C1, (M00,M11), M00)

    def test_true_world_must_belong_to_live_pair(self):
        with self.assertRaises(ProtocolViolation):
            run_episode(Condition.C1, (M00,M01), M10)

    def test_positive_episode_specs_only_enumerate_count(self):
        self.assertEqual(len(positive_episode_specs()), 8)

    def test_aggregation_uses_only_supplied_synthetic_results(self):
        fake = [
            EpisodeResult("C0",("A","B"),"A","q0",0,"A","rA",0,True,True,None),
            EpisodeResult("C0",("C","D"),"C","q0",0,None,None,1,False,False,"NO_BOUNDED_ZERO_ERROR_CONTINUATION"),
        ]
        aggregate = aggregate_results(fake)
        self.assertEqual(aggregate, {"episode_count":2,"discriminating_count":1,"repair_success_count":1,"P_disc":0.5,"P_repair":0.5})

    def test_static_contract_fields_are_exact(self):
        record = validate_contract()
        expected_true = {
            "endpoint_nonidentifiability_verified",
            "no_universal_diagnostic_verified",
            "pair_order_invariance_verified",
            "marginal_information_matched",
            "joint_comparison_only_in_C1",
            "read_only_mediator_verified",
            "mediator_ephemeral_verified",
            "shared_menu_verified",
            "budget_matched",
            "resolver_identity_matched",
        }
        for field in expected_true:
            self.assertIs(record[field], True, field)
        self.assertEqual(record["positive_pair_count"], 4)
        self.assertEqual(record["positive_episode_count_per_condition"], 8)
        self.assertEqual(record["null_disagreement_vector"], [0,0])
        self.assertEqual(record["null_mediator_output"], "NO_DISCRIMINATING_DIAGNOSTIC")


if __name__ == "__main__":
    unittest.main()
