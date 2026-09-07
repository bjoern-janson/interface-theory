from __future__ import annotations

from enum import Enum
from typing import TypeAlias


class Topology(str, Enum):
    A = "A"
    B = "B"


class Diagnostic(str, Enum):
    QA = "q_A"
    QB = "q_B"


class Repair(str, Enum):
    R0 = "r_0"
    R1 = "r_1"


Action: TypeAlias = Diagnostic | Repair | str
FAULTS = (0, 1)
TOPOLOGY_BIT = {Topology.A: 0, Topology.B: 1}
ACTIONS: tuple[Action, ...] = (
    Diagnostic.QA, Diagnostic.QB, Repair.R0, Repair.R1, "stop"
)
BUDGET = 2
DIAGNOSTIC_COST = 1
REPAIR_COST = 1


def probe(topology: Topology, diagnostic: Diagnostic, fault: int) -> int | None:
    if fault not in FAULTS:
        raise ValueError("fault must be 0 or 1")
    if topology is Topology.A:
        return fault if diagnostic is Diagnostic.QA else None
    return fault if diagnostic is Diagnostic.QB else None


def valid_repair(fault: int, repair: Repair) -> bool:
    if fault not in FAULTS:
        raise ValueError("fault must be 0 or 1")
    return (fault == 0 and repair is Repair.R0) or (
        fault == 1 and repair is Repair.R1
    )
