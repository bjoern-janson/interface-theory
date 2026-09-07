import inspect
import unittest

import mediation
from mediation import (
    compare_signatures,
    control_select_diagnostic,
    treatment_select_diagnostic,
)
from protocol import Diagnostic, MediationStatus


class MediationTests(unittest.TestCase):
    def test_xor_comparison_is_permutation_symmetric(self):
        self.assertEqual(compare_signatures((0, 0), (1, 0)), (1, 0))
        self.assertEqual(compare_signatures((1, 0), (0, 0)), (1, 0))
        self.assertEqual(compare_signatures((0, 1), (0, 0)), (0, 1))

    def test_treatment_selects_unique_disagreement_coordinate(self):
        self.assertEqual(treatment_select_diagnostic((0, 0), (1, 0)), Diagnostic.Q0)
        self.assertEqual(treatment_select_diagnostic((0, 0), (0, 1)), Diagnostic.Q1)

    def test_treatment_abstains_on_no_disagreement(self):
        self.assertEqual(
            treatment_select_diagnostic((0, 0), (0, 0)),
            MediationStatus.NO_DISCRIMINATING_DIAGNOSTIC,
        )

    def test_treatment_rejects_double_disagreement_as_out_of_family(self):
        self.assertEqual(
            treatment_select_diagnostic((0, 0), (1, 1)),
            MediationStatus.OUT_OF_FROZEN_FAMILY,
        )

    def test_control_selector_is_pair_blind(self):
        self.assertEqual(list(inspect.signature(control_select_diagnostic).parameters), [])
        self.assertEqual(control_select_diagnostic(), Diagnostic.Q0)

    def test_treatment_selector_accepts_only_two_marginal_signatures(self):
        self.assertEqual(
            list(inspect.signature(treatment_select_diagnostic).parameters),
            ["left", "right"],
        )

    def test_mediation_module_has_no_latent_registry_imports(self):
        forbidden = {
            "LatentModel",
            "POSITIVE_MODELS",
            "POSITIVE_PAIRS",
            "NULL_PAIR",
            "M00",
            "M01",
            "M10",
            "M11",
        }
        self.assertTrue(forbidden.isdisjoint(mediation.__dict__))


if __name__ == "__main__":
    unittest.main()
