# T-20701 — Square-support D-0001 arithmetic criterion

Claim ID: `T-20701`  
Title: The scalar `N=0` square-support D-0001 block already carries the complete square-screw RH criterion  
Status: `PROPOSED CROSS-BRANCH EQUIVALENCE`  
Authoring agent: `gpt56-03-r`  
Created: 2026-08-01  
Dependencies: exact identity `L-20704`; square-screw criterion `T-19801/L-19802`; the D-0001 admissibility and normalization audit  
Scope: integer square supports `c=M^2`

## 1. Scalar D-0001 sequence

Let

\[
 a_M=e_0^{\mathsf T}A_{0,M^2}e_0.
\tag{T-20701.1}
\]

The same scalar is the constant principal coordinate of every larger packet
`A_(N,M^2)`. By `L-20704`,

\[
\boxed{
 \mathcal S(M)=\log M\,a_M.
}
\tag{T-20701.2}
\]

## 2. Equivalent scalar criteria

Subject to the independent review of `T-19801/L-19802`,

\[
\boxed{
\mathrm{RH}
\Longleftrightarrow
a_M\ge0\text{ for every sufficiently large integer }M.
}
\tag{T-20701.3}
\]

The exact rightmost-zero exponent is

\[
\boxed{
\Theta_\zeta
=\limsup_{M\to\infty}
{\log\left(1+\log M\,(-a_M)_+\right)\over2\log M}.
}
\tag{T-20701.4}
\]

In particular,

\[
\boxed{
(-a_M)_+=M^{o(1)}
\Longrightarrow\mathrm{RH}.
}
\tag{T-20701.5}
\]

The much stronger estimate `a_M>=-epsilon_M` with `epsilon_M->0` also implies
RH.

## 3. Consequence for a growing matrix schedule

Choose the explicit unbounded schedule

\[
\boxed{
(N_M,c_M)=(M,M^2),
\qquad M=2,3,4,\ldots .
}
\tag{T-20701.6}
\]

Suppose a directed block proof gives

\[
A_{WW,M}\succ0
\tag{T-20701.7}
\]

and

\[
S_{R,M}
=A_{RR,M}-A_{RW,M}A_{WW,M}^{-1}A_{WR,M}
\succeq-\varepsilon_MG_{R,M}.
\tag{T-20701.8}
\]

Let `G_triangle,M` be the exact square-completion metric and suppose

\[
G_{\triangle,M}\preceq\Lambda_M I,
\qquad
\delta_M\ge0
\tag{T-20701.9}
\]

is the complete assembly radius. Then

\[
A_{M,M^2}
\succeq
-(\Lambda_M\varepsilon_M+\delta_M)I.
\tag{T-20701.10}
\]

Evaluating on `e_0` and using (T-20701.2) gives

\[
\boxed{
\mathcal S(M)
\ge
-\log M\,(\Lambda_M\varepsilon_M+\delta_M).
}
\tag{T-20701.11}
\]

Therefore the user-requested rate

\[
\boxed{
\Lambda_M\varepsilon_M+\delta_M\longrightarrow0
}
\tag{T-20701.12}
\]

would imply (T-20701.5), hence RH.

## 4. Why this is a useful reduction

The conclusion does not say that the matrix program is circular. A directed
matrix factorization could still be a new proof of RH. It says exactly what the
factorization must accomplish arithmetically: before controlling any growing
Schur geometry, it must prove the square-screw prime inequality already present
in the constant principal coordinate.

In particular, none of the following can by itself establish (T-20701.12):

- a better Cauchy-frame condition number;
- a different first-frame graph;
- separate absolute bounds for the prime and pole matrices;
- positivity of a finite support average without a pointwise selection theorem;
- a prime-number-theorem error estimate too weak to prove (T-20701.5).

## 5. Converse under RH

Under RH, the Guinand--Weil criterion makes every admissible D-0001 test matrix
positive semidefinite. Hence

\[
A_{N,M^2}\succeq0
\tag{T-20701.13}
\]

for every `N,M`, subject to the D-0001 admissibility and normalization audit.
Thus the square-support full-matrix positivity statement is equivalent to RH,
while the vanishing-negative-floor version is a quantitatively weakened but
still RH-resolving form.

## 6. Proof boundary

- The embedding (T-20701.2) is exact.
- The RH equivalence is inherited from the proposed square-screw theorem and
  must not be promoted independently of its review.
- This theorem does not provide the lower bounds (T-20701.7)--(T-20701.8).
- It identifies those bounds as the arithmetic theorem itself, already in rank
  zero, rather than a remaining conditioning or bookkeeping lemma.
