# T-24504 — Lagarias, the prime ramp, and signed carry transport form an equivalence triangle

Claim ID: `T-24504`  
Status: `PROPOSED — complete synthesis from stated dependencies`  
Scope: full Riemann Hypothesis equivalences  
Issue: #245

Define the full prime-power ramp

\[
S_X=\sum_{q=p^a\le X}
\frac{\Lambda(q)}{\sqrt q}\log\frac Xq,
\tag{T-24504.1}
\]

and the ordinary-prime ramp

\[
P_X=\sum_{p\le X}
\frac{\log p}{\sqrt p}\log\frac Xp.
\tag{T-24504.2}
\]

Let `b_X^(0)` be the parabolic seed of `L-24502`, and let

\[
r_p^{(0)}=v_p(b_X^{(0)})-p^{-1/2}\log(X/p).
\tag{T-24504.3}
\]

The following statements are equivalent.

## A. Riemann Hypothesis

Every nontrivial zero of `zeta(s)` has real part `1/2`.

## B. Critical prime-ramp lower bound

For every `epsilon>0`,

\[
\boxed{
P_X\ge4\sqrt X-O_\epsilon(X^\epsilon).
}
\tag{T-24504.4}
\]

Equivalently, the same estimate holds with `S_X` in place of `P_X`.

## C. Finite signed carry certificate

For every `epsilon>0` and every sufficiently large `X`, there is a finite real
linear combination of the constant `b`-blocks of `L-24520` such that the
corrected vector `b_X^*` satisfies

\[
v_p(b_X^*)\le p^{-1/2}\log(X/p)
\qquad(p\le X),
\tag{T-24504.5}
\]

and

\[
\boxed{
J_{\mathbb P,X}(b_X^*)
\ge J_{\mathbb P,X}(b_X^{(0)})-O_\epsilon(X^\epsilon).
}
\tag{T-24504.6}
\]

No sign condition is imposed on the corrected `b`-coordinates.

## D. Lagarias harmonic divisor inequality

For every integer `n>=1`,

\[
\boxed{
\sigma(n)
\le H_n+e^{H_n}\log H_n,
}
\tag{T-24504.7}
\]

with equality only at `n=1`.

## Proof

### A equivalent to D

This is `T-24502`, imported from Lagarias's elementary reformulation with its
Robin dependency boundary made explicit.

### A equivalent to B

The square-screw/prime-ramp transfer already present in the repository gives

\[
\mathrm{RH}
\iff
S_X\ge4\sqrt X-X^{o(1)}.
\]

`L-24517` proves unconditionally that

\[
S_X-P_X=O(\log^2X),
\]

so the ordinary-prime and full prime-power versions are equivalent at every
`X^epsilon` scale.

### C implies B

For every corrected vector satisfying (T-24504.5), exact von Mangoldt duality
on the ordinary primes gives

\[
P_X
\ge J_{\mathbb P,X}(b_X^*).
\]

By `L-24517`,

\[
J_{\mathbb P,X}(b_X^{(0)})
\ge4\sqrt X-O(\log^2X).
\]

Combining this with (T-24504.6) proves (T-24504.4).

### B implies C

Assume B. By `L-24520`, constant `b`-blocks between prime endpoints span the
whole ordinary-prime residual space. In particular, transport the positive
part of `r^(0)` to zero, using endpoint `1` for any remaining mass. The exact
objective loss of an optimal such correction is no larger than

\[
\left[J_{\mathbb P,X}(b_X^{(0)})-P_X\right]_+.
\tag{T-24504.8}
\]

By B and the parabolic seed estimate, the quantity in (T-24504.8) is
`O_epsilon(X^epsilon)`. The resulting vector is feasible and satisfies
(T-24504.6). Hence C holds.

This completes the equivalence.

## Interpretation

The theorem provides a precise connection between the paper imported in
`T-24502` and the elementary carry program:

```text
Lagarias harmonic divisor inequality
<=> critical prime ramp
<=> finite signed carry-block certificate
<=> RH.
```

The harmonic wrapper, the prime Riesz mean, and the carry LP are not independent
proofs. They are exact coordinate systems for the same global scalar
obstruction.

## Review boundary

The nontrivial imported dependencies are Lagarias/Robin for `A<=>D` and the
repository's square-screw/Landau transfer for `A<=>B`. The finite bridge
`B<=>C` is supplied by `L-24517/L-24520`.
