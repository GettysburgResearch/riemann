# L-106000 — Euler-completed Dirichlet-family lift of the native common mother

Claim ID: `L-106000`  
Programme aliases: `LFAM1.EULER_COMPLETED_COMMON_MOTHER`, `STRESS.DIRICHLET_FAMILY_LIFT`  
Status: **PROVED EXACT SOURCE AND MELLIN IDENTITY**  
Created: 2026-08-24  
Base: PR #719 at `20e6bc5d961f00818fac86c9252e2535c5d9821a`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

This theorem gives a literal family lift of the fixed common-mother detector. Its
principal character is exactly the original native zeta channel after one
explicit ramified Euler completion. The family is fixed before any hypothetical
zero is introduced.

## 1. Fixed source and character twist

Let `ell` be an odd prime with

\[
\ell\ne 67.
\]

For a Dirichlet character `chi (mod ell)`, extended by zero on multiples of
`ell`, put

\[
b_\chi(n)=\mu(n)\chi(n).
\tag{L-106000.1}
\]

Let `Phi_*` be the compact common mother inherited from PR #715/#719, and use
the normalized dilation

\[
(S_a f)(X)=f(X/a).
\tag{L-106000.2}
\]

Define the untampered character field

\[
F_\chi(X)
=
\sum_{n\ge1}{\mu(n)\chi(n)\over\sqrt n}
\Phi_*(X/n).
\tag{L-106000.3}
\]

Compact support makes the sum finite at every `X`.

The literal twist of the marked-67 native source is obtained by

\[
F_{\chi,67}
=
\left(I-\chi(67)67^{-1/2}S_{67}\right)F_\chi.
\tag{L-106000.4}
\]

The factor `chi(67)` is source typing, not a detector chosen after a zero: it
is exactly what results from twisting the fixed marked-prime coefficient.

Finally introduce the ramified local completion

\[
\boxed{
\mathcal F_{\chi,\ell}
=
\left(I-\ell^{-1/2}S_\ell\right)F_{\chi,67}.
}
\tag{L-106000.5}
\]

The same `ell` and the same completion operator are used for every character in
the family.

## 2. Exact Mellin transform

Write

\[
s=z+\frac12.
\]

With

\[
\widehat\Phi_*(z)
=
\int_0^\infty \Phi_*(X)X^{-z}{dX\over X},
\]

initial absolute convergence gives

\[
\widehat F_\chi(z)
=
{\widehat\Phi_*(z)\over L(s,\chi)}.
\tag{L-106000.6}
\]

Since `S_a` has Mellin multiplier `a^{-z}`, (L-106000.5) yields

\[
\boxed{
\widehat{\mathcal F}_{\chi,\ell}(z)
=
\widehat\Phi_*(z)\,
{(1-\ell^{-s})(1-\chi(67)67^{-s})
 \over L(s,\chi)}.
}
\tag{L-106000.7}
\]

All continuation statements are taken only after the initially convergent
identity is established.

For the principal character `chi_0 (mod ell)`,

\[
L(s,\chi_0)=\zeta(s)(1-\ell^{-s}),
\qquad
\chi_0(67)=1,
\]

and hence

\[
\boxed{
\widehat{\mathcal F}_{\chi_0,\ell}(z)
=
\widehat\Phi_*(z)\,
{1-67^{-s}\over\zeta(s)}.
}
\tag{L-106000.8}
\]

The principal completed family member is therefore exactly the native marked-67
common-mother detector, not a finite-Euler approximation to it.

## 3. Coefficientwise principal restoration

Let

\[
b_{\ell}(n)=\mu(n)\mathbf1_{\ell\nmid n}.
\]

Applying `I-ell^{-1/2}S_ell` at the scalar level corresponds to the source

\[
c_\ell(n)
=
b_\ell(n)
-
\mathbf1_{\ell\mid n}b_\ell(n/\ell).
\tag{L-106000.9}
\]

A direct squarefree case split gives

\[
\boxed{c_\ell(n)=\mu(n)\qquad(n\ge1).}
\tag{L-106000.10}
\]

Indeed:

- if `ell` does not divide `n`, both sides equal `mu(n)`;
- if `ell || n`, then
  `c_ell(n)=-mu(n/ell)=mu(n)`;
- if `ell^2 | n`, both sides vanish.

The marked-67 filter then gives exactly

\[
\mu-\delta_{67}*\mu.
\tag{L-106000.11}
\]

Thus (L-106000.8) is also a literal coefficient theorem.

## 4. Functoriality through the source algebra

For arithmetic functions `f,g`, character twisting satisfies

\[
\boxed{
((f*g)\chi)=(f\chi)*(g\chi),
}
\tag{L-106000.12}
\]

because `chi(ab)=chi(a)chi(b)`, including the zero values at ramified
arguments.

Consequently every coefficientwise identity in the inherited common-mother,
half-divisor, Wick, owner and stopped-Vaughan algebra has an exact character
lift when every source factor is twisted consistently.

The ramified completion in (L-106000.5) is applied only after the full linear
carrier recombination. It is not inserted separately into positive squares,
absolute values or owner marginals.

## 5. Pole retention

If `Re(s)>0`, then

\[
|\ell^{-s}|<1,
\qquad
|\chi(67)67^{-s}|<1.
\]

Therefore neither finite factor in the numerator of (L-106000.7) vanishes in
the open right half-plane. Any zero of `L(s,chi)` there remains an uncancelled
reciprocal-`L` pole of the completed family detector, with its multiplicity.

In particular, the principal member retains every hypothetical off-line zeta
zero exactly as the original common mother does.

## 6. Scope

This theorem proves:

```text
one fixed family chosen before a hypothetical zero;
exact principal recovery of the native common mother;
exact character lift of the source algebra;
exact reciprocal-L Mellin transform;
open-half-plane finite-factor noncancellation.
```

It does not estimate any family moment, isolate the principal member at
subpower cost, prove `BQSP102870`, or prove RH.
