# R-28101 — Fixed-order Abel producer positivity fails

Claim ID: `R-28101`  
Title: The binary–ternary producer has exact negative third-, fourth-, and fifth-prefix kernels at finite endpoints  
Status: **EXACT REFUTATION OF FIXED-ORDER ABEL POSITIVITY AS A CLOSING MECHANISM**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Targets: PR #279 `L-27801/T-27801`; fixed-order continuations of the same argument  
Dependencies: PR #247 `L-23810/L-23811`; integer Möbius inversion; exact descending binary–ternary recurrence  
Scope: refutes the stated third-prefix theorem and the immediate fixed fourth/fifth-prefix repairs; it does not refute positivity of the actual critical producer or RH

## 1. The frozen producer

For an endpoint `X`, a target `w(2),...,w(X)`, and

\[
 U_w(m)=\sum_{k\le X/m}\mu(k)w(mk),
 \qquad
 R_w(m)=U_w(m)-U_w(m+1),
\]

the frozen half-binary/half-ternary producer is defined by descending recursion

\[
\begin{aligned}
 A_w(n)=R_w(n)+\frac12\sum_{m>n}A_w(m)
 \bigl[&\mathbf1_{\lceil m/3\rceil=n}
       +\mathbf1_{m-\lceil m/3\rceil=n}\\
      &+\mathbf1_{\lfloor m/2\rfloor=n}
       +\mathbf1_{m-\lfloor m/2\rfloor=n}\bigr].
\end{aligned}
\tag{R-28101.1}
\]

This is the exact recurrence used in PRs #247, #277, and #279.  No floating point or asymptotic approximation occurs below.

For an Abel order `r>=1` and a terminal column `Q`, put

\[
 w_{Q,r}(q)
 =\binom{Q-q+r-1}{r-1}\mathbf1_{2\le q\le Q}.
\tag{R-28101.2}
\]

The `r=3` case is precisely PR #279's third cumulative kernel
`S_X(n,Q)` when `X=Q`.

## 2. Exact third-prefix counterexample

Take

\[
 X=Q=520,
 \qquad r=3.
\]

Exact integer Möbius inversion followed by the Fraction recurrence (R-28101.1) gives

\[
\boxed{
 A_{w_{520,3}}(15)=-\frac{91}{256}<0.
}
\tag{R-28101.3}
\]

Therefore the all-scale statement

\[
 S_X(n,Q)\ge0
\]

in `TACP-I` is false.  The finite scan through `X=80` on PR #279 was valid at its declared scope but did not reveal the first later obstruction.

Consequently:

```text
PR #279 TACP-I third-prefix positivity       FALSE
TACP-I + collar as the proposed proof         NOT AVAILABLE
actual critical-source producer positivity    OPEN
RH                                             UNPROVED
```

## 3. The immediate fourth- and fifth-prefix repairs also fail

The same exact recurrence gives:

\[
\boxed{
 A_{w_{4500,4}}(19)
 =-\frac{11921994153}{4096}<0,
}
\tag{R-28101.4}
\]

and

\[
\boxed{
 A_{w_{23500,5}}(15)
 =-\frac{164644438459306823}{131072}<0.
}
\tag{R-28101.5}
\]

Thus replacing “third Abel” by one fixed higher Abel order does not repair the argument.  The obstruction merely moves outward.

These examples do not prove that every fixed order eventually fails, but they reject the three concrete fixed orders currently suggested by the finite trend.

## 4. Why the failures are structurally useful

The critical source

\[
 q^{-1/2}\log(X/q)
\]

has nonnegative interior differences of every order.  Therefore the failures in (R-28101.3)--(R-28101.5) belong to the producer/kernel side, not to a loss of source smoothness.

The correct next mechanism must preserve the complete source while exploiting an additional feature not present in fixed Abel smoothing.  The continuation on this branch uses the exact decomposition

\[
\mathcal T_X=\mathcal T+\mathcal E,
\]

where `mathcal T` is the positive continuum central cascade and `mathcal E` is a one-lattice-step commutator.  Every noncontinuum word contains `mathcal E`, which gains one full Mellin power and places the error in a strictly contractive half-plane.  This is a genuinely different mechanism from fixed prefix positivity.

## 5. Exact replay

`experiments/X-28101-fixed-abel-counterexamples/verify.py` uses only:

- Python integers;
- `fractions.Fraction`;
- a linear Möbius sieve;
- the exact recurrence (R-28101.1).

It verifies all three boxed values and rejects any mutation of the split multiplicities or target order.

## 6. Scope boundary

Refuted:

- PR #279's proposed all-scale third-prefix kernel positivity;
- the direct fixed fourth-prefix repair;
- the direct fixed fifth-prefix repair.

Not refuted:

- actual critical producer positivity by another source-specific method;
- cycle-optimized carry repair;
- the central commutator cascade;
- the Riemann Hypothesis.
