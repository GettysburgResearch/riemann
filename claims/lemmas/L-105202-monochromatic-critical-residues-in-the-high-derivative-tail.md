# L-105202 — Critical residues are asymptotically monochromatic throughout the natural high-derivative tail

Claim ID: `L-105202`  
Status: **PROPOSED COMPLETE UNCONDITIONAL ANALYTIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: `L-105200--L-105201`; PR #720 `L-104522--L-104523`  
RH status: **not assumed**

## 1. Residues in the common natural box

Fix `C,H>1`. Put

\[
T_M=C\sqrt{M\over\log M}
\]

and let `m>=M`. At every simple real zero `c` of `Xi^(m+1)` satisfying

\[
|c|\le T_M-1,
\]

define

\[
\rho_{m,c}
={\Xi^{(m)}(c)\over\Xi^{(m+2)}(c)}.
\tag{L-105202.1}
\]

Then, uniformly over all such `m,c`,

\[
\boxed{
\rho_{m,c}
=-{1\over w_m^2}\left(1+o_{M\to\infty}(1)\right).
}
\tag{L-105202.2}
\]

In particular, every residue in the box is negative for sufficiently large
`M`. Thus every critical point there is a Rolle-generating extremum, and no
wrong extremum occurs in the high derivative tail.

## 2. Exact Gaussian-model residue

Let

\[
g_m(z)=e^{-s_m^2z^2/2}\chi_m(w_mz),
\]

where `chi_m=cos` for even `m` and `chi_m=sin` for odd `m`. At a real critical
point `x` of `g_m`, write

\[
q={\chi_m'(w_mx)\over\chi_m(w_mx)}.
\]

The critical equation is

\[
-s_m^2x+w_mq=0.
\]

Since `chi_m''=-chi_m`, logarithmic differentiation gives

\[
{g_m''(x)\over g_m(x)}
=-s_m^2-w_m^2(1+q^2)
=-\left(w_m^2+s_m^2+s_m^4x^2\right).
\]

Therefore the model residue is exactly

\[
\boxed{
{g_m(x)\over g_m''(x)}
=-{1\over w_m^2+s_m^2+s_m^4x^2}.
}
\tag{L-105202.3}
\]

On the natural box, `|x|<=T_M` and `s_mT_M=O_C(1)`. Hence

\[
{s_m^2+s_m^4x^2\over w_m^2}=o(1)
\]

uniformly for `m>=M`, so (L-105202.3) is `-w_m^(-2)(1+o(1))`.

## 3. Passage from the model to Xi

The derivative version `L-105200.10` gives `C^2` convergence to the Gaussian
trigonometric model after normalization, uniformly on a slightly larger
rectangle. The cellwise Rouché proof in `L-105201` also localizes every zero of
`Xi^(m+1)` within `o(1/w_m)` of one model critical point.

At those points, the model value is bounded away from zero after division by
the Gaussian factor, and its second derivative has magnitude
`w_m^2(1+o(1))` times the value. Substituting the localized point into the
`C^2` approximation therefore transfers (L-105202.3) to the actual ratio
(L-105202.1), proving (L-105202.2).

## 4. First and second moments

Let

\[
\mathcal C_{m,M}
=\{c\in[-T_M+1,T_M-1]:\Xi^{(m+1)}(c)=0\},
\]

and put

\[
R_{m,M}=|\mathcal C_{m,M}|,
\]

\[
\mathcal M_{1,m}(M)
=-\sum_{c\in\mathcal C_{m,M}}\rho_{m,c},
\qquad
\mathcal M_{2,m}(M)
=\sum_{c\in\mathcal C_{m,M}}\rho_{m,c}^2.
\]

Uniform monochromaticity gives

\[
\boxed{
\mathcal M_{1,m}(M)
={R_{m,M}\over w_m^2}(1+o(1)),
}
\tag{L-105202.4}
\]

and

\[
\boxed{
\mathcal M_{2,m}(M)
={R_{m,M}\over w_m^4}(1+o(1)),
}
\tag{L-105202.5}
\]

uniformly for `m>=M`.

The residue coherence of `L-104522` consequently satisfies

\[
\boxed{
\mathfrak C_{m,M}
={\mathcal M_{1,m}(M)^2
 \over R_{m,M}\mathcal M_{2,m}(M)}
=1-o(1).
}
\tag{L-105202.6}
\]

Equivalently, the squared coefficient of variation of the negative residue
carrier tends to zero.

## 5. Unconditional high-tail RCMV

For every fixed `delta<1/2`, sufficiently large `M` gives, simultaneously for
all `m>=M`,

\[
\boxed{
\mathcal M_{1,m}(M)^2
>\left({1\over2}+\delta\right)
R_{m,M}\mathcal M_{2,m}(M).
}
\tag{L-105202.7}
\]

Thus the Xi-specific residue mean-value condition `RCMV104530` is true with a
margin approaching the optimal value throughout the complete natural-scale
high derivative tail. The open difficulty is not the existence of residue
coherence in the Xi Fourier model; it is persistence of enough coherence
through the finitely many low derivative levels required at a given height.

## 6. Scope

The sums exclude an `O(w_m)`-independent number of boundary cells by shrinking
the real interval by one. This has no effect on the displayed asymptotics.
The theorem does not assert residue coherence for a fixed `m` as the height
tends to infinity, and therefore does not prove RH.
