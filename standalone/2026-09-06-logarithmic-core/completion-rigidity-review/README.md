# Review submission: exact completion rigidity and a shorter contour

Status: proposed component proofs; independent mathematical and code review pending.
**No full proposed proof of RH is claimed. The count/sign estimate OPEN in PROOF.md, Section 7 is unproved.**

Parent: PR #803 at `ed074bcabfd2c1ca3336e457b8fdd09a25bcd2a7`.
This packet is add-only. No earlier mathematical source or review is changed.

## What is established here

1. For every finite real polynomial p retaining the Mobius prefix below Y>=ceil(2m), with p(1)=0, its complete critical-line signed functional satisfies exactly

   `I_m(p)=D(m)-1/4+(45m/128)(p'(1)-1)^2`.

   Its real tail Hessian has rank one. All p with p'(1)=1 give the same value. Convexity does not establish the sign of their common minimum. This completely resolves the proposed signed-completion optimization, not the native arithmetic sign.

2. If p is supported below A Y and has coefficient energy at most B(1+log Y), the entire absolute contour tail above Y^nu is

   `O((1+log Y)^2 Y^(1-3nu/2+epsilon))`, for fixed `2/3<nu<=1` and `0<epsilon<3nu/2-1`.

   The constant is uniform over all such p and m. Taking nu=3/4 leaves a vanishing `O_epsilon(log^2(Y)Y^(-1/8+epsilon))` error. This reduces the parent's frequency interval from Y to Y^(3/4). Classical analytic constants are not numerically certified.

3. Every two normalized completions in that fixed support/energy class also have truncated SIGNED integrals differing by only that vanishing error. Tail optimization cannot create an order-one improvement of the native sign.

4. An exact primitive arithmetic check at m=2 gives `-17/500<I_2<-33/1000`, while `D(2)=1/4+I_2>0`. This rejects the stronger proposed assertion that the signed integral itself is nonnegative. It is not a counterexample to RH or to the needed weaker bound.

## End-to-end boundary

For the fixed polynomial p_(2k^2), let Z_k be the signed contour up to `(2k^2)^(3/4)` with phase k^(4it). The proof supplies `D(k^2)=1/4+Z_k+o(1)`. A fixed power saving in the count of `Z_k<-1` would imply RH by the fully stated negative-part/spectral-supremum argument in Section 7. That count saving is not proved. The pinned earlier source/curvature lemmas remain review dependencies.

No new positive range, all-window sign, zero-free region, numerical contour evaluation, or external novelty is claimed. The classical convolution identity is credited rather than renamed a new inverse method.

## Read and replay

Read PROOF.md, then REVIEW.md and SOURCES.json. VALIDATION.md records what was actually run.

```
python -I -S -B verify.py --check result.json
python -I -S -B -O verify.py --check result.json
```

The checker authenticates this eight-file packet and the two frozen parent manuscripts, but executes no parent code. Its 534 bounded fixtures in 16 groups cover finite convolution, independent Mobius factorization, full Laurent principal parts, polarized residues, cutoff exponents, and an actual rational-logarithmic sign. They do not prove the infinite contour argument or OPEN. Separate parent-suite replays and actual corruption refusals are recorded in VALIDATION.md; their counts are not added to 534.
