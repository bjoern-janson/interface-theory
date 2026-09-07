import unittest

from protocol import Diagnostic, Repair, Topology
from viability import initial_action_supports_zero_error, viable_initial_actions


class ViabilityTests(unittest.TestCase):
    def test_ga_requires_q_a_initially(self):
        self.assertEqual(viable_initial_actions(Topology.A), frozenset({Diagnostic.QA}))

    def test_gb_requires_q_b_initially(self):
        self.assertEqual(viable_initial_actions(Topology.B), frozenset({Diagnostic.QB}))

    def test_wrong_probe_has_no_bounded_zero_error_continuation(self):
        self.assertFalse(initial_action_supports_zero_error(Topology.A, Diagnostic.QB))
        self.assertFalse(initial_action_supports_zero_error(Topology.B, Diagnostic.QA))

    def test_repairs_and_stop_cannot_guarantee_both_faults_initially(self):
        for topology in (Topology.A, Topology.B):
            self.assertFalse(initial_action_supports_zero_error(topology, Repair.R0))
            self.assertFalse(initial_action_supports_zero_error(topology, Repair.R1))
            self.assertFalse(initial_action_supports_zero_error(topology, "stop"))

    def test_viable_initial_action_sets_are_nonempty_and_disjoint(self):
        a = viable_initial_actions(Topology.A)
        b = viable_initial_actions(Topology.B)
        self.assertTrue(a)
        self.assertTrue(b)
        self.assertTrue(a.isdisjoint(b))


if __name__ == "__main__":
    unittest.main()
