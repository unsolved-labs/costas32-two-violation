#!/usr/bin/env python3
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name):
    vals = [int(x) for x in (ROOT / name).read_text().split()]
    if len(vals) != 32 or set(vals) != set(range(1, 33)):
        raise SystemExit(f"FAIL: {name} is not a permutation of 1..32")
    return vals


def analyze(p):
    counts = Counter()
    segments = defaultdict(list)
    for i in range(32):
        for j in range(i + 1, 32):
            v = (j - i, p[j] - p[i])
            counts[v] += 1
            segments[v].append((i + 1, p[i], j + 1, p[j]))
    duplicates = {v: segments[v] for v, m in counts.items() if m > 1}
    score = sum(m - 1 for m in counts.values() if m > 1)
    return score, duplicates

candidate = load("candidate.txt")
baseline = load("baseline_mdraco_17.txt")
cs, cd = analyze(candidate)
bs, _ = analyze(baseline)
expected = {
    (1, 1): [(1, 1, 2, 2), (6, 18, 7, 19)],
    (5, 17): [(1, 1, 6, 18), (2, 2, 7, 19)],
}
if cs != 2:
    raise SystemExit(f"FAIL: candidate score {cs}, expected 2")
if cd != expected:
    raise SystemExit(f"FAIL: candidate duplicate structure {cd!r}")
if bs != 17:
    raise SystemExit(f"FAIL: baseline score {bs}, expected 17")
if not cs < bs:
    raise SystemExit("FAIL: candidate is not a strict improvement")
print(f"PASS: candidate={cs} baseline={bs} strict_improvement={bs-cs}")
