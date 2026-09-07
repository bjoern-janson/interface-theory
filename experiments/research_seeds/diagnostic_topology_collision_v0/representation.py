from __future__ import annotations

from dataclasses import dataclass

from protocol import Diagnostic, TOPOLOGY_BIT, Topology


@dataclass(frozen=True)
class RawHistory:
    topology_bit: int
    nuisance: int


def make_history(topology: Topology, nuisance: int) -> RawHistory:
    if nuisance not in (0, 1):
        raise ValueError("nuisance must be 0 or 1")
    return RawHistory(TOPOLOGY_BIT[topology], nuisance)


def g0(history: RawHistory) -> int:
    return history.nuisance


def g1(history: RawHistory) -> int:
    return history.topology_bit


def select_diagnostic(retained_bit: int) -> Diagnostic:
    if retained_bit == 0:
        return Diagnostic.QA
    if retained_bit == 1:
        return Diagnostic.QB
    raise ValueError("retained bit must be 0 or 1")
