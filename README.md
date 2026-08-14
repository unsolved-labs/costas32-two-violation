# Order-32 Costas two-violation construction

This repository is the canonical artifact for Unsolved Labs release R018.

## Frozen claim

Under the Costas-array violation objective used by Vulakh and Finkel's mDRACO implementation—one violation for each repeated displacement occurrence beyond the first—the order-32 permutation

```text
1 2 29 21 28 18 19 22 31 27 15 10 26 12 32 30 24 6 14 7 17 16 13 4 8 20 25 9 23 3 5 11
```

has exactly **2 violations**.

The published mDRACO order-32 approximate solution has **17 violations** under the same objective. The released permutation is therefore a strict `17 -> 2` improvement against that frozen published baseline.

The two repeated displacement vectors are:

- `(1, 1)`, from `(1,1)->(2,2)` and `(6,18)->(7,19)`;
- `(5, 17)`, from `(1,1)->(6,18)` and `(2,2)->(7,19)`.

## What is not claimed

This repository does **not** contain an order-32 Costas array. It does not prove that 2 is the global minimum possible number of violations, and it does not settle whether a Costas array of order 32 exists.

## Frozen baseline

D. Vulakh and R. Finkel, *Parallel m-dimensional relative ant colony optimization (mDRACO) for the Costas-array problem*, Soft Computing 26 (2022), 5765–5772, DOI `10.1007/s00500-022-06969-1`.

The paper reports that after more than 10,000 CPU-days, mDRACO found an order-32 permutation with 17 Costas-array-property violations. The exact baseline permutation transcribed from the paper is frozen in `baseline_mdraco_17.txt`.

The public mDRACO implementation defines the incremental Costas cost by counting a new displacement as a violation when that same displacement has already occurred; this is exactly the duplicate-excess objective implemented by `verify.py`.

## Reproduce

Requires Python 3.10+ and no third-party packages.

```bash
python verify.py
```

Expected terminal line:

```text
PASS: candidate=2 baseline=17 strict_improvement=15
```

The verifier independently checks:

1. both files are permutations of `1..32`;
2. every positive-horizontal displacement vector between pairs of points;
3. duplicate excess `sum(max(0,multiplicity-1))`;
4. the exact two duplicate candidate vectors and their endpoints;
5. the frozen baseline score of 17;
6. the strict improvement from 17 to 2.

CI executes the same verifier from a clean checkout.

## Files

- `candidate.txt` — released 2-violation permutation.
- `baseline_mdraco_17.txt` — frozen published 17-violation baseline.
- `verify.py` — self-contained exact verifier.
- `result.json` — machine-readable frozen claim and expected output.
- `NOVELTY.md` — scoped novelty/baseline audit.
- `.github/workflows/verify.yml` — clean-checkout replay.

## Trust boundary

The public claim depends only on integer parsing, permutation checks, integer subtraction, counting equal integer pairs, and comparison with the frozen expected values. No stochastic search, floating point arithmetic, model-generated prose, external solver, or network access is required for verification.

## Review status

Independent specialist review is pending.
