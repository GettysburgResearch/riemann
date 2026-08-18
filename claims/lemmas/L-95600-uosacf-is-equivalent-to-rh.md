# L-95600 — One-sided subpower annular Q4 is equivalent to the Riemann Hypothesis

Claim ID: `L-95600`  
Status: **PROPOSED COMPLETE EQUIVALENCE — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Frozen base: PR #595 at `e66a91166b80cbf0a520e3a78ea96582d263d563`  
Scientific status: **RH remains unproved**

Let \(\mathcal A(X)\) be the exact ten-band annular Q4 observation of PR #580,
and let \(\mathcal S_H(X)\) be the separated small-gcd coprime form with
\(H=(\log 2X)^B\). PR #595 proves

\[
\mathcal A(X)^2
=
\mathcal D_A(X)+\mathcal S_H(X)+E_H(X),
\]

with

\[
\mathcal D_A(X)=O(\log^2 X),
\qquad
E_H(X)=O_B(\log^{B+2}(2X)).
\]

It defines `UOSACF` by requiring, for every \(\varepsilon>0\),

\[
\mathcal S_H(X)\le C_\varepsilon X^\varepsilon
\]

for all sufficiently large \(X\), and proves `UOSACF -> RH`.

## Converse under RH

Let

\[
M(x)=\sum_{n\le x}\mu(n),
\qquad
M_o(x)=\sum_{\substack{n\le x\\n\ {\rm odd}}}\mu(n).
\]

The exact dyadic identity is

\[
M(x)=M_o(x)-M_o(x/2),
\]

hence

\[
\boxed{
M_o(x)=\sum_{j\ge0}M(x/2^j).
}
\tag{L-95600.1}
\]

Under RH, for every \(\eta>0\),

\[
M(x)=O_\eta(x^{1/2+\eta}),
\]

and therefore the same estimate holds for \(M_o\).

Write the exact ten-band weight as

\[
G_X(t)
=
\frac{(\log t)J_0(t/X)+(\log2)J_1(t/X)}{\sqrt t}.
\]

On each activation band, the deposited exact cubic formulas imply uniformly

\[
|G_X(t)|\ll \frac{\log(2X)}{\sqrt X},
\qquad
|G_X'(t)|\ll \frac{\log(2X)}{X^{3/2}}.
\tag{L-95600.2}
\]

Partial summation on each of the ten bands, retaining every real endpoint,
gives

\[
\boxed{
\mathcal A(X)=O_\eta(X^\eta\log(2X)).
}
\tag{L-95600.3}
\]

Given \(\varepsilon>0\), choose \(\eta<\varepsilon/4\). Then

\[
\mathcal S_H(X)
\le
\mathcal A(X)^2
+
O_B(\log^{B+2}(2X))
\le
C_\varepsilon X^\varepsilon.
\]

Thus RH implies UOSACF.

## Equivalence

\[
\boxed{
\mathrm{RH}
\Longleftrightarrow
\mathrm{UOSACF}
\Longleftrightarrow
\mathcal A(X)=X^{o(1)}.
}
\tag{L-95600.4}
\]

The annular Q4 condition is therefore an exact RH criterion, not a weaker
standard Type-II estimate.


---
