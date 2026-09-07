import unittest

from protocol import (
    BUDGET, DIAGNOSTIC_COST, NULL_PAIR, POSITIVE_MODELS, POSITIVE_PAIRS,
    REPAIR_COST, Diagnostic, marginal_view,
)


class ProtocolTests(unittest.TestCase):
    def test_square_signatures_are_exact(self):
        self.assertEqual(
            {m.key: marginal_view(m) for m in POSITIVE_MODELS},
            {"M00": (0, 0), "M01": (0, 1), "M10": (1, 0), "M11": (1, 1)},
        )

    def test_positive_family_is_exactly_the_four_square_edges(self):
        edges = {frozenset((a.key, b.key)) for a, b in POSITIVE_PAIRS}
        self.assertEqual(edges, {
            frozenset(("M00", "M10")), frozenset(("M01", "M11")),
            frozenset(("M00", "M01")), frozenset(("M10", "M11")),
        })
        self.assertNotIn(frozenset(("M00", "M11")), edges)
        self.assertNotIn(frozenset(("M01", "M10")), edges)

    def test_each_positive_edge_differs_on_exactly_one_coordinate(self):
        for left, right in POSITIVE_PAIRS:
            self.assertEqual(sum(a != b for a, b in zip(left.signature, right.signature)), 1)

    def test_each_endpoint_occurs_in_one_q0_and_one_q1_edge(self):
        incidence = {m.key: set() for m in POSITIVE_MODELS}
        for left, right in POSITIVE_PAIRS:
            diffs = [i for i in (0, 1) if left.signature[i] != right.signature[i]]
            diagnostic = Diagnostic.Q0 if diffs == [0] else Diagnostic.Q1
            incidence[left.key].add(diagnostic)
            incidence[right.key].add(diagnostic)
        for value in incidence.values():
            self.assertEqual(value, {Diagnostic.Q0, Diagnostic.Q1})

    def test_repairs_and_budget_are_exact(self):
        self.assertEqual(len({m.repair for m in POSITIVE_MODELS}), 4)
        self.assertEqual((BUDGET, DIAGNOSTIC_COST, REPAIR_COST), (2, 1, 1))

    def test_null_pair_has_same_signature_but_distinct_repairs(self):
        left, right = NULL_PAIR
        self.assertEqual(left.signature, right.signature)
        self.assertEqual(left.signature, (0, 0))
        self.assertNotEqual(left.repair, right.repair)


if __name__ == "__main__":
    unittest.main()
