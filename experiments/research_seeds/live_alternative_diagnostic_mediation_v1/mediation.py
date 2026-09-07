from __future__ import annotations

from protocol import Diagnostic, MediationStatus, Signature

MediationOutput = Diagnostic | MediationStatus


def compare_signatures(left: Signature, right: Signature) -> Signature:
    return left[0] ^ right[0], left[1] ^ right[1]


def control_select_diagnostic() -> Diagnostic:
    return Diagnostic.Q0


def treatment_select_diagnostic(
    left: Signature,
    right: Signature,
) -> MediationOutput:
    disagreement = compare_signatures(left, right)
    if disagreement == (1, 0):
        return Diagnostic.Q0
    if disagreement == (0, 1):
        return Diagnostic.Q1
    if disagreement == (0, 0):
        return MediationStatus.NO_DISCRIMINATING_DIAGNOSTIC
    return MediationStatus.OUT_OF_FROZEN_FAMILY
