# L-32201 — Prime-radix residue Fourier modes are reciprocal Dirichlet-L cores

Claim ID: `L-32201`  
Title: The unit-residue state modulo a prime diagonalizes into the Riesz means of `1/L(s,chi)`; radix two is the only prime radix with no nonprincipal character channel  
Status: **PROPOSED COMPLETE EXACT ANALYTIC/ALGEBRAIC LEMMA**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: elementary Dirichlet characters and Mellin integration  
Scope: source decomposition and a proof-search firewall; no RH conclusion

## 1. Character-resolved Möbius Riesz means

Let `p` be prime and let `chi` be a Dirichlet character modulo `p`, extended by zero on multiples of `p`. Define

\[
\mathcal R_\chi(X)
=\sum_{n\le X}
\frac{\mu(n)\chi(n)}{\sqrt n}\log\frac Xn.
\tag{L-32201.1}
\]

For `Re(z)>1/2`, termwise integration gives

\[
\boxed{
\int_1^\infty \mathcal R_\chi(X)X^{-z-1}\,dX
=\frac{1}{z^2L(z+1/2,\chi)}.
}
\tag{L-32201.2}
\]

Indeed complete multiplicativity of `chi` gives

\[
(\mu\chi)*\chi=\varepsilon,
\]

so the Dirichlet series of `mu chi` is `1/L(s,chi)` in the half-plane of absolute convergence.

For the principal character `chi_0 mod p`,

\[
L(s,\chi_0)=\zeta(s)(1-p^{-s}),
\]

and therefore

\[
\boxed{
\sum_n\frac{\mu(n)\chi_0(n)}{n^s}
=\frac{1}{\zeta(s)(1-p^{-s})}.
}
\tag{L-32201.3}
\]

For every nonprincipal `chi`, (L-32201.2) carries the zero set of the corresponding primitive/imprimitive Dirichlet `L`-function.

## 2. Residue-class Fourier transform

For every unit residue `r in (Z/pZ)^*`, define

\[
\mathcal R_r(X)
=\sum_{\substack{n\le X\\n\equiv r\pmod p}}
\frac{\mu(n)}{\sqrt n}\log\frac Xn.
\tag{L-32201.4}
\]

Character orthogonality gives the exact finite Fourier transform

\[
\boxed{
\mathcal R_\chi(X)
=\sum_{r\in(\mathbb Z/p\mathbb Z)^*}\chi(r)\mathcal R_r(X),
}
\tag{L-32201.5}
\]

and the inverse

\[
\boxed{
\mathcal R_r(X)
=\frac{1}{p-1}
\sum_\chi \overline{\chi(r)}\mathcal R_\chi(X).
}
\tag{L-32201.6}
\]

Thus a complete finite residue-state theorem is automatically a theorem about all character channels, not only the principal zeta channel.

## 3. Exact specialization to radix five

The group `(Z/5Z)^*` is cyclic of order four. Taking `2` as a generator, the four characters are

\[
\chi_j(2^a)=i^{ja},\qquad j=0,1,2,3.
\tag{L-32201.7}
\]

Hence the four nonzero residue coordinates of a five-adic source are exactly equivalent to

```text
principal channel        1/[zeta(s)(1-5^-s)];
quadratic channel         1/L(s,chi_2);
complex channel           1/L(s,chi_1);
conjugate complex channel 1/L(s,chi_3).
```

The residue-zero coordinate is the strict lower-scale `5`-divisible channel. The remaining four-state quotient is therefore not a source-free rational gadget: three of its Fourier modes contain nonprincipal Dirichlet-L zeros.

## 4. Consequence for a finite residue contraction

Suppose a norm `D_X` on the complete unit-residue state is uniformly equivalent, in the fixed four-dimensional residue coordinate, to the coordinate norm, and suppose one proves

\[
D_X\le \rho D_{X/5}+O(\log^A X),\qquad \rho<1.
\tag{L-32201.8}
\]

Then fixed-dimensional norm equivalence and iteration give

\[
\mathcal R_r(X)=X^{o(1)}
\]

for every unit residue `r`, hence by (L-32201.5)

\[
\mathcal R_\chi(X)=X^{o(1)}
\]

for every character modulo five. Equation (L-32201.2) would then exclude every zero of every `L(s,chi)` to the right of `Re(s)=1/2`; functional-equation symmetry gives the corresponding GRH statement for all four mod-five characters.

Therefore a finite five-state certificate of the strength proposed on PR #322 is potentially a simultaneous RH/GRH theorem. That is not a contradiction, but it is a mandatory scope fact: the nonprincipal residue modes cannot be declared harmless finite boundary states without proving their contraction.

## 5. Radix two is character-free

For `p=2`, the unit group has one element and hence only the principal character. There is no nonprincipal character channel.

Thus among prime radices,

\[
\boxed{
p=2\text{ is the unique radix for which the unit-residue Fourier decomposition introduces no additional Dirichlet-}L\text{ source.}
}
\tag{L-32201.9}
\]

Finite two-adic Euler factors may create artificial boundary poles, but they do not introduce an independent nonprincipal `L`-function. This is the structural reason to prefer a source-complete dyadic recurrence over a source-blind five-adic automaton.

## 6. Proof boundary

Closed exactly:

1. the `1/L(s,chi)` coefficient identity;
2. the character-residue Fourier transform;
3. the complete mod-five character decomposition;
4. the implication from a norm-equivalent subpower residue bound to GRH for all mod-five characters;
5. uniqueness of radix two as the prime character-free residue split.

Not proved:

1. any five-adic residue contraction;
2. any dyadic coupled-boundary recurrence;
3. RH or GRH.
