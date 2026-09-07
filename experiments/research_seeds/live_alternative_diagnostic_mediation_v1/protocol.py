from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import TypeAlias

Signature: TypeAlias = tuple[int, int]


class Diagnostic(str, Enum):
    Q0 = "q0"
    Q1 = "q1"


class MediationStatus(str, Enum):
    NO_DISCRIMINATING_DIAGNOSTIC = "NO_DISCRIMINATING_DIAGNOSTIC"
    OUT_OF_FROZEN_FAMILY = "OUT_OF_FROZEN_FAMILY"


@dataclass(frozen=True)
class LatentModel:
    key: str
    signature: Signature
    repair: str


M00 = LatentModel("M00", (0, 0), "r00")
M01 = LatentModel("M01", (0, 1), "r01")
M10 = LatentModel("M10", (1, 0), "r10")
M11 = LatentModel("M11", (1, 1), "r11")
POSITIVE_MODELS = (M00, M01, M10, M11)
POSITIVE_PAIRS = ((M00, M10), (M01, M11), (M00, M01), (M10, M11))
N0 = LatentModel("N0", (0, 0), "rN0")
N1 = LatentModel("N1", (0, 0), "rN1")
NULL_PAIR = (N0, N1)
DIAGNOSTICS = (Diagnostic.Q0, Diagnostic.Q1)
BUDGET = 2
DIAGNOSTIC_COST = 1
REPAIR_COST = 1


def marginal_view(model: LatentModel) -> Signature:
    return model.signature


def world_observation(model: LatentModel, diagnostic: Diagnostic) -> int:
    return model.signature[0 if diagnostic is Diagnostic.Q0 else 1]
