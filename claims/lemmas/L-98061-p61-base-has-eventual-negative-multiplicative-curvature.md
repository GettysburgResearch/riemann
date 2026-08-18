# L-98061 — The complete `P_61` base has eventual negative multiplicative curvature

Claim ID: `L-98061`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC THEOREM**  
Created: 2026-08-18  
Depends on: `L-98040`; the fixed-colour Euler-ramp expansion in PR #587  
RH status: **not assumed**

Let `b(Y)=F_61(Y)` be the repaired annular `5:3` base and

\[
h(Y)={b(Y)\over\sqrt Y}.
\]

The complete fixed-colour expansion has

\[
\boxed{
b(Y)=a_*\sqrt Y+c_*+O_{P_{61}}(Y^{-3/2}),
\qquad
h(Y)=a_*+{c_*\over\sqrt Y}+O_{P_{61}}(Y^{-2}),
}
\tag{L-98061.1}
\]

where

\[
a_*=12\prod_{r\le61\atop r\ {m prime}}\left(1-{1\over r}\right)>0
\tag{L-98061.2}
\]

and

\[
\boxed{
c_*
=\log4
\left(6\zeta(1/2)-{15\over2}+{9\over\sqrt2}\right)
\prod_{r\le61\atop r\ {m prime}}
\left(1-{1\over\sqrt r}\right)<0.
}
\tag{L-98061.3}
\]

The sign in (L-98061.3) is unconditional.  The alternating eta series is
positive at `1/2`, while

\[
\eta(1/2)=(1-\sqrt2)\zeta(1/2),
\]

so `zeta(1/2)<0`.  Also

\[
-{15\over2}+{9\over\sqrt2}<0,
\]

and every finite Euler factor in (L-98061.3) is positive.

For fixed primes `p,q`, define the multiplicative determinant

\[
\mathcal K_{p,q}[h](Y)
=h(Y)h(Y/(pq))-h(Y/p)h(Y/q).
\tag{L-98061.4}
\]

Substitution of (L-98061.1) gives

\[
\boxed{
\mathcal K_{p,q}[h](Y)
={a_*c_*\over\sqrt Y}
 (\sqrt p-1)(\sqrt q-1)
+O_{p,q,P_{61}}(Y^{-2}).
}
\tag{L-98061.5}
\]

The quadratic `c_*^2/Y` terms cancel exactly.  Since `a_*>0`, `c_*<0`, and
`p,q>1`, there is an effective `Y_0(p,q)` such that

\[
\boxed{
\mathcal K_{p,q}[h](Y)<0
\qquad(Y\ge Y_0(p,q)).
}
\tag{L-98061.6}
\]

Thus the native annular base is eventually multiplicatively log-concave, not
multiplicatively TP2.

## Consequence for future-prime ratios

Under the positivity hypotheses of `L-98060`, adjoining a fixed future prime
`q` therefore eventually **increases** the earlier `p` profile ratio:

\[
Q_p[\mathcal E_qh](Y)>Q_p[h](Y).
\tag{L-98061.7}
\]

This gives a second, asymptotic obstruction to a source-blind projective
contraction.  The obstruction is small—of order `Y^{-1/2}` for fixed `p,q`—but
its sign is the adverse one.

The theorem does not say that the accumulated ratio reaches `p`, and it does
not refute `GPC67`.  It says that a valid proof cannot assert that every future
prime damps the ratio by total positivity.  It must budget the complete signed
curvature debt or use an equivalent source correlation.

```text
P61 constant term c_*                  IDENTIFIED / NEGATIVE
base multiplicative TP2                FALSE EVENTUALLY
single future-prime ratio damping      FALSE EVENTUALLY
complete accumulated Bellman bound     OPEN
GPC67 / RH                             UNPROVEN
```