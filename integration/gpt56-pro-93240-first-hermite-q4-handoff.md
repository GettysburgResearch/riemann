# Handoff — First-Hermite and Q4 prime-block coherence packet

Status: **PROPOSED; INDEPENDENT REVIEW REQUIRED; RH UNPROVED**  
Base: `main` at `9c7538559d7f56c2914b39aed5a1fb3fbf7ce131`

## Load-bearing files

```text
claims/lemmas/L-93240-prime-block-coherence-principle.md
claims/lemmas/L-93241-first-hermite-distinct-prime-resonance-sharpening.md
claims/lemmas/L-93242-q4-endpoint-prime-block-coherence.md
claims/theorems/T-93243-q4-pure-distinct-prime-gram-criterion.md
experiments/X-93240-prime-block-coherence/verify.py
reports/gpt56-pro/2026-08-15-first-hermite-q4-prime-block-coherence.md
```

## Frozen dependencies

```text
First-Hermite PR #390:
ea20af8867c3119c23efc27738d343aac2f79362

First-Hermite PR #392:
d2387cd21eb891a8801fd122bc8d0ddd7c1c0fc4

Q4 PR #474:
56eeaccb2b041fdf68b6e718bad85032ecbdc66a
```

## New results

1. A finite Hilbert-space prime-block coherence lemma with exact diagonal/cross identity, \(E/D\) positive-block lower bound, \(E/(4D)\) half-carrier lower bound, and rank-one positive cross certificate.
2. First-Hermite complete same-prime-tower diagonal
   \[
   D_{q,a}(t)\le V(q)+1152\ll q+1,
   \]
   upgrading PR #392's forced distinct-prime count from \(\gg(\log T)^2/q^2\) to \(\gg(\log T)^2/(q+1)\).
3. Exact prime-base decomposition of the complete actual Q4 endpoint row with
   \[
   D_N\le576N^2\log^2N.
   \]
4. Conditional on `T-93010`, RH is equivalent to a polylogarithmic bound for one pure distinct-prime Q4 Gram correlation.

## Preferred review order

```text
1. L-93240 finite Hilbert lemma
2. L-93241 Hermite factor and tower constant
3. L-93242 complete Q4 source decomposition and 576 bound
4. T-93243 conditional composition with T-93010
5. X-93240 replay and mutation tests
```

## Replay

```bash
cd experiments/X-93240-prime-block-coherence
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected:

```text
PASS_X_93240_PRIME_BLOCK_COHERENCE
```

## Smallest failure points

- `L-93241`: failure of the uniform block diagonal bound would invalidate the factor-\(q\) sharpening.
- `L-93242`: failure of the coefficientwise source split or the \(576N^2\log^2N\) diagonal bound would invalidate the pure-cross reduction.
- `T-93243`: the RH equivalence remains conditional on independent acceptance of frozen `T-93010`.

## Open gates

```text
heat:
one-carrier deterministic exclusion of the aligned prime blocks

Q4:
polylogarithmic control of the pure distinct-prime row Gram correlation

RH:
unproved
```
