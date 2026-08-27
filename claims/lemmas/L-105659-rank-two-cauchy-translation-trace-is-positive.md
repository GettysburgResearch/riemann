# L-105659 — The Cauchy translation trace inequality holds for every two-factor packet

Claim ID: `L-105659`  
Status: **EXACT SYMBOLIC-RATIONAL THEOREM; INDEPENDENT REPLAY REQUESTED**  
Created: 2026-08-27  
Depends on: `T-105655`; `X-105659`  
RH status: **not assumed**

Let

\[
\lambda_1=A+i\alpha_1,
\qquad
\lambda_2=B+i\alpha_2,
\qquad
A,B,H>0,
\]

and put

\[
D=\alpha_2-\alpha_1.
\]

For

\[
G_s(i,j)
=
\frac1{\overline{\lambda_i}+\lambda_j+s},
\]

define

\[
\mathcal O_H
=
\operatorname{tr}
(G_0^{-1}G_{2H}G_{4H}^{-1}G_{2H}),
\]

\[
\mathcal T_H
=
\operatorname{tr}(G_0^{-1}G_H).
\]

Then

\[
\boxed{
\mathcal O_H-\mathcal T_H>0.
}
\tag{L-105659.1}

Thus `CTI105655` is true for every packet of rank two, including arbitrary
horizontal separation and the confluent limit.

## 1. Exact algebraic reduction

The difference in (L-105659.1) is invariant under a common horizontal
translation and symmetric in `A,B`.  Clear its positive Cauchy determinant
denominator, replace

\[
U=D^2,
\qquad
P=A+B,
\qquad
R=AB,
\]

and symmetrize in the two depths.  The resulting numerator and denominator are
polynomials in

\[
P,R,U,H
\]

whose coefficients are all nonnegative.  The numerator is nonzero for
`A,B,H>0`; the only boundary degeneracies occur after a depth or `H` is allowed
to vanish.

The exact expansion, symmetry conversion, denominator sign, and coefficient
ledger are generated and checked by

```text
experiments/X-105659-rank-two-cauchy-trace/verify.py.
```

No floating-point simplification enters the proof.

## 2. Scope of the result

The theorem is substantially stronger than the rank-one result of `L-105654`:
the two model factors may collide horizontally or have unrelated depths, and
the complete nonorthogonal Cauchy interaction is retained.

It does not establish arbitrary-rank `CTI105655`.  In particular, positivity of
every one- and two-factor principal packet does not bootstrap abstractly to an
all-packet matrix or trace theorem.  The repository's packet-size firewalls
remain binding.

## 3. Consequence

At packet rank at most two,

\[
\boxed{
\mathfrak P_{0,H}
\le
\mathfrak R_H,
}
\]

so the degree-zero reverse-oriented phase overlap is completely paid by the
literal current reserve.  Arbitrary-rank Xi packets, cofinal endpoint passage,
pointwise localization, and RH remain open.
