import unittest

from protocol import Diagnostic, Topology
from representation import RawHistory, g0, g1, make_history, select_diagnostic


class RepresentationTests(unittest.TestCase):
    def test_same_history_can_feed_both_encoders(self):
        history = make_history(Topology.A, 1)
        self.assertEqual(history, RawHistory(topology_bit=0, nuisance=1))
        self.assertEqual(g0(history), 1)
        self.assertEqual(g1(history), 0)

    def test_g0_collapses_topology_for_matched_nuisance(self):
        for nuisance in (0, 1):
            self.assertEqual(
                g0(make_history(Topology.A, nuisance)),
                g0(make_history(Topology.B, nuisance)),
            )

    def test_g1_preserves_topology_for_both_nuisance_values(self):
        for nuisance in (0, 1):
            self.assertEqual(g1(make_history(Topology.A, nuisance)), 0)
            self.assertEqual(g1(make_history(Topology.B, nuisance)), 1)

    def test_both_encoders_are_binary(self):
        for topology in (Topology.A, Topology.B):
            for nuisance in (0, 1):
                history = make_history(topology, nuisance)
                self.assertIn(g0(history), (0, 1))
                self.assertIn(g1(history), (0, 1))

    def test_controller_is_fixed(self):
        self.assertIs(select_diagnostic(0), Diagnostic.QA)
        self.assertIs(select_diagnostic(1), Diagnostic.QB)


if __name__ == "__main__":
    unittest.main()
