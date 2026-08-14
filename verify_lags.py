#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name):
    p = [int(x) for x in (ROOT / name).read_text().split()]
    assert len(p) == 32 and sorted(p) == list(range(1, 33))
    return p


def lag_score(p):
    score = 0
    collisions = []
    for d in range(1, 32):
        row = [p[i + d] - p[i] for i in range(32 - d)]
        score += len(row) - len(set(row))
        seen = {}
        for i, delta in enumerate(row):
            if delta in seen:
                collisions.append((d, delta, seen[delta] + 1, i + 1))
            else:
                seen[delta] = i
    return score, collisions

c = load("candidate.txt")
b = load("baseline_mdraco_17.txt")
cs, cc = lag_score(c)
bs, _ = lag_score(b)
assert cs == 2, cs
assert bs == 17, bs
assert cc == [(1, 1, 1, 6), (5, 17, 1, 2)], cc
print(f"PASS-LAGS: candidate={cs} baseline={bs} strict_improvement={bs-cs}")
