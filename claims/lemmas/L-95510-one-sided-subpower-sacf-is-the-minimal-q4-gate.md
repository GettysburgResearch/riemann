# L-95510 — One-sided subpower SACF is sufficient and is the minimal quadratic gate

Claim ID: `L-95510`  
Status: **PROVED EXACT REDUCTION**  
Created: 2026-08-18  
Frozen base: PR #580 at `812e7fcbaff2dd1c2c53c885def7b6c0d0e68a05`  
RH status: **not assumed**

Retain the annular Q4 observation and its diagonal/cross decomposition

\[
 \mathcal A(X)^2=\mathcal D_A(X)+\mathcal X_A(X),
 \qquad
 \mathcal D_A(X)=O(\log^2X).
\tag{L-95510.1}
\]

For `H=(log(2X))^B`, PR #580 proves

\[
 \mathcal X_A(X)=\mathcal S_H(X)+E_H(X),
 \qquad
 E_H(X)=O_B(\log^{B+2}(2X)),
\tag{L-95510.2}
\]

where `mathcal S_H` is the separated, small-gcd, coprime Type-II form.

## 1. Automatic lower bound

Since `mathcal A(X)^2>=0`,

\[
 \mathcal X_A(X)\ge-\mathcal D_A(X).
\]

Therefore

\[
 \boxed{
 \mathcal S_H(X)
 \ge-\mathcal D_A(X)-E_H(X)
 =-O_B(\log^{B+2}(2X)).
 }
\tag{L-95510.3}
\]

The difficult direction is only an **upper** bound.  Negative separated
correlation is automatically harmless.

Consequently, up to changing a logarithmic exponent,

\[
 \mathcal S_H(X)\le O(\log^A X)
 \quad\Longleftrightarrow\quad
 |\mathcal S_H(X)|\le O(\log^{A'}X).
\tag{L-95510.4}
\]

Thus the absolute-value formulation of `SACF` is formally stronger in its
statement but has no additional conclusion-producing content.

## 2. Subpower rather than polylogarithmic growth

Define **Upper One-Sided SACF** (`UOSACF`) by: for one fixed sufficiently large
`B` and every `epsilon>0`,

\[
 \boxed{
 \mathcal S_{(\log 2X)^B}(X)
 \le C_\epsilon X^\epsilon
 }
\tag{L-95510.5}
\]

for all sufficiently large `X`.

Then (L-95510.1)--(L-95510.2) give, for every `epsilon>0`,

\[
 0\le\mathcal A(X)^2
 \le O(\log^2X)+C_\epsilon X^\epsilon
   +O_B(\log^{B+2}X)
 =O_\epsilon(X^\epsilon).
\]

Hence

\[
 \boxed{\mathcal A(X)=X^{o(1)}.}
\tag{L-95510.6}
\]

The stable inverse of PR #580 has total coefficient mass `64/21`, so the
original preconditioned Q4 observation also satisfies `mathcal C_e(X)=X^{o(1)}`.
Its Mellin integral therefore converges and is holomorphic in every half-plane
`Re s>delta>0`.  The frozen pole audit then excludes an off-critical zeta zero.

Thus

\[
 \boxed{
 \mathrm{UOSACF}\Longrightarrow\mathrm{RH}.
 }
\tag{L-95510.7}
\]

This is strictly weaker than the published requirement of an absolute
polylogarithmic estimate.  It remains RH-bearing and is not proved here.
