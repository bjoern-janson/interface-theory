import unittest

from protocol import (
    ACTIONS, BUDGET, DIAGNOSTIC_COST, FAULTS, REPAIR_COST, TOPOLOGY_BIT,
    Diagnostic, Repair, Topology, probe, valid_repair,
)


class ProtocolTests(unittest.TestCase):
    def test_frozen_resources_and_actions(self):
        self.assertEqual((BUDGET, DIAGNOSTIC_COST, REPAIR_COST), (2, 1, 1))
        self.assertEqual(FAULTS, (0, 1))
        self.assertEqual(TOPOLOGY_BIT, {Topology.A: 0, Topology.B: 1})
        self.assertEqual(
            ACTIONS,
            (Diagnostic.QA, Diagnostic.QB, Repair.R0, Repair.R1, "stop"),
        )

    def test_ga_topology(self):
        self.assertEqual(probe(Topology.A, Diagnostic.QA, 0), 0)
        self.assertEqual(probe(Topology.A, Diagnostic.QA, 1), 1)
        self.assertIsNone(probe(Topology.A, Diagnostic.QB, 0))
        self.assertIsNone(probe(Topology.A, Diagnostic.QB, 1))

    def test_gb_topology(self):
        self.assertEqual(probe(Topology.B, Diagnostic.QB, 0), 0)
        self.assertEqual(probe(Topology.B, Diagnostic.QB, 1), 1)
        self.assertIsNone(probe(Topology.B, Diagnostic.QA, 0))
        self.assertIsNone(probe(Topology.B, Diagnostic.QA, 1))

    def test_fault_specific_repairs(self):
        self.assertTrue(valid_repair(0, Repair.R0))
        self.assertTrue(valid_repair(1, Repair.R1))
        self.assertFalse(valid_repair(0, Repair.R1))
        self.assertFalse(valid_repair(1, Repair.R0))


if __name__ == "__main__":
    unittest.main()
