# L-34406 — The aligned odd-source relative Jordan curvature has no bare/second-current cross

Claim ID: `L-34406`

Status: **PROPOSED COMPLETE EXACT RELATIVE-CURVATURE THEOREM — INDEPENDENT REVIEW REQUIRED**

Created: 2026-08-09

Dependencies: `L-34404`; PR #345 `L-34404` vector-curvature pattern; elementary dyadic carry scaling

Scope: exact odd-prime/odd-Möbius relative state on aligned radix-four rows.  It eliminates the bare-times-second-current cross identically and produces a clean positive critical-scale curvature.  It does not upper-bound the odd current innovation and does not prove RH.

## 1. Odd Möbius source

Put

\[
\boxed{
B_{\rm odd}(s)
=\prod_{p\ {m odd}}(1-p^{-s})
=\sum_{n\ge1}\frac{b_{\rm odd}(n)}{n^s}.
}
\tag{L-34406.1}
\]

Thus

\[
b_{\rm odd}(n)
=\begin{cases}
\mu(n),&n\text{ odd},\\
0,&n\text{ even}.
\end{cases}
\]

Its inverse is the odd Euler product

\[
A_{\rm odd}(s)=B_{\rm odd}(s)^{-1},
\]

with generalized-prime sequence

\[
\Lambda_{\rm odd}(n)
=\Lambda(n)\mathbf1_{n\ {m odd}}.
\tag{L-34406.2}
\]

The corresponding Selberg sequence is

\[
C_{\rm odd}
=\Lambda_{\rm odd}\log
 +\Lambda_{\rm odd}*\Lambda_{\rm odd}.
\tag{L-34406.3}
\]

The deterministic first/second carry coordinates are precisely the odd-prime quantities `O,S_odd` of `L-34404`, and

\[
R_{\rm odd}=O^2-S_{\rm odd}.
\tag{L-34406.4}
\]

## 2. The divisor prefix is the pure dyadic tower

Since

\[
\frac1{\zeta(s)}
=(1-2^{-s})B_{\rm odd}(s),
\]

one has

\[
\boxed{
\zeta(s)B_{\rm odd}(s)
=\frac1{1-2^{-s}}
=\sum_{r\ge0}2^{-rs}.
}
\tag{L-34406.5}
\]

Hence

\[
\boxed{
\mathbf1*b_{\rm odd}
=\sum_{r\ge0}\delta_{2^r}.
}
\tag{L-34406.6}
\]

For one row `e=(n,j)` define the bare source charge

\[
Y_{\rm odd}(e)
=\mathcal L_e(b_{\rm odd}).
\]

The general prefix/carry identity therefore gives the exact binary-carry count

\[
\boxed{
Y_{\rm odd}(n,j)
=\sum_{r\ge1}\chi_{n,2^r}(j).
}
\tag{L-34406.7}
\]

(The `r=0`, `d=1` column has zero carry identically.)

In particular `Y_odd>=0` and `Y_odd=O(log n)`.

## 3. Exact radix-four invariance of the bare charge

Let

\[
e^+=(4n,4j).
\]

For `r=1,2`, the parent and both children are divisible by `2^r`, so

\[
\chi_{4n,2^r}(4j)=0.
\tag{L-34406.8}
\]

For every `r>=3`, exact division by four gives

\[
\boxed{
\chi_{4n,2^r}(4j)
=\chi_{n,2^{r-2}}(j).
}
\tag{L-34406.9}
\]

Therefore (L-34406.7) telescopes by a pure index shift:

\[
\begin{aligned}
Y_{\rm odd}(4n,4j)
&=\sum_{r\ge3}\chi_{n,2^{r-2}}(j)\\
&=\sum_{\ell\ge1}\chi_{n,2^\ell}(j)\\
&=Y_{\rm odd}(n,j).
\end{aligned}
\]

Thus

\[
\boxed{
Y_{\rm odd}(e^+)-Y_{\rm odd}(e)=0.
}
\tag{L-34406.10}
\]

This is exact for every nontrivial integer row; no asymptotic or balanced-cone assumption is needed.

## 4. Odd Jordan deformation and source jets

Define the positive odd-prime Jordan deformation

\[
\boxed{
J_{{\rm odd},\tau}(s)
=\frac{A_{\rm odd}(s-\tau)}{A_{\rm odd}(s)}.
}
\tag{L-34406.11}
\]

The same local Euler calculation used throughout the Jordan branches gives coefficientwise positivity for `tau>=0`, and

\[
J_{{\rm odd},0}=\varepsilon,
\qquad
J_{{\rm odd},0}'=\Lambda_{\rm odd},
\qquad
J_{{\rm odd},0}''=C_{\rm odd}.
\tag{L-34406.12}
\]

Source-convolve

\[
K_{{\rm odd},\tau}
=b_{\rm odd}*J_{{\rm odd},\tau}.
\tag{L-34406.13}
\]

Its first three jets are

\[
K_{{\rm odd},0}=b_{\rm odd},
\quad
K_{{\rm odd},0}'=q_{\rm odd},
\quad
K_{{\rm odd},0}''=t_{\rm odd}.
\tag{L-34406.14}
\]

For one row write

\[
Q_{\rm odd}(e)=\mathcal L_e(q_{\rm odd}),
\qquad
T_{\rm odd}(e)=\mathcal L_e(t_{\rm odd}).
\]

## 5. Relative vector path

Define the scalar row partition

\[
F_e^{\rm odd}(\tau)
=1+\mathcal L_e(J_{{\rm odd},\tau})
\]

and the relative scale-four coordinate

\[
\boxed{
H_e^{\rm odd}(\tau)
=\frac{F_{e^+}^{\rm odd}(\tau)}
       {F_e^{\rm odd}(4\tau)}.
}
\tag{L-34406.15}
\]

Exactly as in PR #345,

\[
H_e^{\rm odd}(0)=1,
\]

\[
(H_e^{\rm odd})'(0)
=O(e^+)-4O(e),
\]

and

\[
\boxed{
-\bigl(\log H_e^{\rm odd}\bigr)''(0)
=R_{\rm odd}(e^+)-16R_{\rm odd}(e)
=\Delta_4R_{\rm odd}(e).
}
\tag{L-34406.16}
\]

Now define the relative source-difference leg directly on the scaled row,

\[
\boxed{
G_e^{\rm odd}(\tau)
=\mathcal L_{e^+}
\bigl((\varepsilon-\delta_4)*K_{{\rm odd},\tau}\bigr).
}
\tag{L-34406.17}
\]

Aligned carry scaling gives

\[
G_e^{\rm odd}(0)
=Y_{\rm odd}(e^+)-Y_{\rm odd}(e)=0
\tag{L-34406.18}
\]

by (L-34406.10), while

\[
\boxed{
(G_e^{\rm odd})'(0)
=Q_{\rm odd}(e^+)-Q_{\rm odd}(e)
=:I_{\rm odd}(e).
}
\tag{L-34406.19}
\]

The second derivative is the corresponding relative second current, but its value will not enter the curvature because the zeroth source coordinate vanishes exactly.

## 6. Cross-free relative curvature

Put

\[
\boxed{
W_e^{\rm odd}(\tau)
=\bigl(H_e^{\rm odd}(\tau),G_e^{\rm odd}(\tau)\bigr).
}
\tag{L-34406.20}
\]

For a Hilbert-valued path use

\[
\mathfrak C(W)
=\|W'(0)\|^2
 -\operatorname{Re}\langle W(0),W''(0)\rangle.
\]

The first coordinate contributes `Delta_4 R_odd` by (L-34406.16).  The second coordinate has zeroth value zero and first derivative `I_odd`.  Therefore

\[
\boxed{
\mathfrak C(W_e^{\rm odd})
=\Delta_4R_{\rm odd}(e)+|I_{\rm odd}(e)|^2.
}
\tag{L-34406.21}
\]

There is **no** bare-times-second-current term.

This should be compared with the full Q=4 relative curvature

\[
\Delta_4R+I_\circ^2-Y_\circ T_\circ,
\]

where the final cross is only lower order but not zero.  The odd-source state removes it algebraically.

## 7. Critical scale

`L-34404` proves on every fixed balanced cone, cofinally and uniformly,

\[
\boxed{
\Delta_4R_{\rm odd}(e)
=\Theta_\eta(n\log n)
}
\tag{L-34406.22}
\]

and in particular

\[
\Delta_4R_{\rm odd}(e)
\ge12h_\eta n\log n.
\]

Hence the relative odd-source curvature is the clean positive state

\[
\boxed{
\mathfrak C(W_e^{\rm odd})
=\Theta_\eta(n\log n)+|I_{\rm odd}(e)|^2
>0
}
\tag{L-34406.23}
\]

outside one finite base.

It is source-complete at the odd-prime level and contains the RH-sensitive odd current innovation with coefficient one.

## 8. Relation to the compact Q=4 source

The compact source itself factors over the same odd Euler core:

\[
B_\circ(s)=T(2^{-s})B_{\rm odd}(s),
\qquad
T(z)=(1-z)(1-4z^2).
\tag{L-34406.24}
\]

Thus its full logarithmic current splits exactly as

\[
\boxed{
q_\circ
=T(z)q_{\rm odd}+\dot T(z)b_{\rm odd}.
}
\tag{L-34406.25}
\]

The first term is the odd-source current passed through one fixed finite dyadic filter.  The second is an explicit finite bare-source gauge.  The same pattern persists through the second derivative.

Therefore (L-34406.21) is a natural scale-matched state for the final compact-current recurrence: the difficult arithmetic current lives in `I_odd`, while all dyadic differentiation is a finite explicit gauge.

The theorem does **not** infer an upper bound for `I_odd` from positivity of the curvature; that would again reverse the logical direction.

## 9. Proof boundary

Closed exactly here:

1. odd Möbius source and positive odd generalized primes;
2. pure-dyadic divisor prefix;
3. exact radix-four invariance of the bare charge;
4. positive odd Jordan deformation;
5. relative scalar log-curvature `Delta_4 R_odd`;
6. exact vanishing of the relative source zeroth coordinate;
7. cross-free vector curvature `Delta_4R_odd+I_odd^2`;
8. factorization of the compact source over the same odd carrier.

Still open:

1. an upper/dissipative law for the cross-free relative curvature;
2. control of `I_odd` or the compact current by a coefficient-one delayed recurrence;
3. global subexponential energy;
4. RH.
