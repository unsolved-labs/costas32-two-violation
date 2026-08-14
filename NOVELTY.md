# Scoped novelty and baseline audit

Audit cutoff: 2026-08-11.

## Frozen comparison point

The comparison point is the order-32 approximate solution reported by:

David Vulakh and Raphael Finkel, "Parallel m-dimensional relative ant colony optimization (mDRACO) for the Costas-array problem," *Soft Computing* 26 (2022), 5765-5772. DOI: 10.1007/s00500-022-06969-1.

The paper states that the smallest unresolved Costas order is 32 and reports that, after more than 10,000 CPU-days, mDRACO found an order-32 permutation with 17 Costas-array-property violations. The Appendix prints that permutation. Its unique parse as a permutation of 1..32 is frozen in `baseline_mdraco_17.txt`.

Primary source:
https://doi.org/10.1007/s00500-022-06969-1

Public implementation:
https://github.com/dvulakh/mDRACO

The public implementation's Costas graph code counts a newly introduced displacement as a violation when the same displacement has already occurred in the partial permutation. For a completed permutation this equals

`sum_v max(0, multiplicity(v)-1)`

over displacement vectors `v`.

## 2026 status check

Gulec and Abolghasemi, "Universal Costas Matrices: Towards a General Framework for Costas Array Construction," arXiv:2602.03407 (2026), continues to treat discovery of new Costas arrays as an active construction problem and develops reconstruction machinery intended to support future AI-assisted search.

Primary source:
https://arxiv.org/abs/2602.03407

Searches through the audit cutoff did not identify a primary publication reporting an order-32 approximate permutation with fewer than 17 violations, nor an exact order-32 Costas array. Because absence claims over the literature cannot be mechanically exhaustive, the public release is phrased conservatively as a strict improvement against the explicitly frozen published mDRACO baseline, not as an unconditional claim about every unpublished computation.

## Released advance

The released permutation has exactly two violations under the same objective. Both independent integer verifiers in this repository reproduce the scores `2` and `17` from the two frozen permutations.

## Excluded claims

The release does not claim:

- existence of an order-32 Costas array;
- global optimality of two violations;
- exhaustive exclusion of one-violation or zero-violation permutations;
- priority over unpublished private computations;
- any hardware, radar, communications, or cryptographic performance improvement.
