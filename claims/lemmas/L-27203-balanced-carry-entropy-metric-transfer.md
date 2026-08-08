# L-27203 — Balanced carry entropy is the unweighted carry metric up to polylogarithmic loss

Claim ID: `L-27203`  
Title: Every nonnegative balanced carry packing has `O(log^2 X)` square-root mass, and its binomial entropy differs from its total unweighted carry load by only `O(log^2 X)`  
Status: **PROPOSED COMPLETE ANALYTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: atomized carry identity `L-23808`; elementary Dirichlet hyperbola and Stirling bounds  
Scope: every finite nonnegative balanced carry flow; no RH input

## 1. Finite flow and slack

Fix `0<eta<=1/2` and `X>=2`. Let

\[
d_{n,j}\ge0,
\qquad
2\le n\le X,
\qquad
\eta n\le j\le(1-\eta)n,
\tag{L-27203.1}
\]

and define its integer carry loads

\[
v(q)=\sum_{n=q}^{X}\sum_jd_{n,j}\chi_{n,j}(q),
\qquad
\chi_{n,j}(q)=
\left\lfloor\frac nq\right\rfloor-
\left\lfloor\frac jq\right\rfloor-
\left\lfloor\frac{n-j}{q}\right\rfloor.
\tag{L-27203.2}
\]

Assume

\[
0\le v(q)\le w_X(q),
\qquad
w_X(q)=q^{-1/2}\log(X/q).
\tag{L-27203.3}
\]

Put

\[
\Sigma_X=\sum_{q=2}^{X}[w_X(q)-v(q)]\ge0.
\tag{L-27203.4}
\]

## 2. Square-root mass bound

For a balanced split and every integer

\[
\max(j,n-j)<q\le n,
\]

one has

\[
\chi_{n,j}(q)=1.
\]

Hence there is a constant `c_eta>0` such that

\[
\boxed{
H_{n,j}:=
\sum_{q=2}^{n}\frac{\chi_{n,j}(q)}{\sqrt q}
\ge c_\eta\sqrt n.}
\tag{L-27203.5}
\]

Indeed, the interval `((1-eta)n,n]` already contributes, and its finitely many
small-`n` exceptions can be absorbed into `c_eta`.

Multiply (L-27203.3) by `q^(-1/2)`, sum in `q`, and use Tonelli:

\[
\begin{aligned}
c_\eta\sum_{n,j}d_{n,j}\sqrt n
&\le
\sum_{q=2}^{X}\frac{v(q)}{\sqrt q}\\
&\le
\sum_{q=2}^{X}\frac{\log(X/q)}q
=O(\log^2X).
\end{aligned}
\]

Therefore

\[
\boxed{
\sum_{n,j}d_{n,j}\sqrt n
=O_\eta(\log^2X).}
\tag{L-27203.6}
\]

This bound uses only nonnegativity, balance, and feasibility.

## 3. Unweighted carry count

Define

\[
\kappa(n,j)=\sum_{q=2}^{n}\chi_{n,j}(q).
\tag{L-27203.7}
\]

Let

\[
D(m)=\sum_{q=1}^{m}\left\lfloor\frac mq\right\rfloor.
\]

The `q=1` carry vanishes, so exactly

\[
\boxed{
\kappa(n,j)=D(n)-D(j)-D(n-j).}
\tag{L-27203.8}
\]

The elementary Dirichlet-hyperbola estimate

\[
D(m)=m\log m+(2\gamma-1)m+O(\sqrt m)
\tag{L-27203.9}
\]

is uniform for `m>=1`. Therefore, with

\[
h(t)=-t\log t-(1-t)\log(1-t),
\]

\[
\boxed{
\kappa(n,j)=n h(j/n)+O(\sqrt n).}
\tag{L-27203.10}
\]

Uniform Stirling bounds give

\[
\boxed{
\log\binom nj=n h(j/n)+O(\log(n+1)).}
\tag{L-27203.11}
\]

Combining (L-27203.10)--(L-27203.11),

\[
\boxed{
\left|
\log\binom nj-\kappa(n,j)
\right|
\le C\sqrt n}
\tag{L-27203.12}
\]

for one absolute constant `C` and every `1<=j<n`.

## 4. Packet-level metric comparison

By (L-27203.6) and (L-27203.12),

\[
\boxed{
\left|
\sum_{n,j}d_{n,j}\log\binom nj
-
\sum_{n,j}d_{n,j}\kappa(n,j)
\right|
=O_\eta(\log^2X).}
\tag{L-27203.13}
\]

But Tonelli and (L-27203.2) give exactly

\[
\sum_{n,j}d_{n,j}\kappa(n,j)
=
\sum_{q=2}^{X}v(q)
=
\sum_{q=2}^{X}w_X(q)-\Sigma_X.
\tag{L-27203.14}
\]

Elementary integral comparison yields

\[
\sum_{q=2}^{X}q^{-1/2}\log(X/q)
=4\sqrt X+O(\log X).
\tag{L-27203.15}
\]

Consequently

\[
\boxed{
\sum_{n,j}d_{n,j}\log\binom nj
=
4\sqrt X-
\Sigma_X+O_\eta(\log^2X).}
\tag{L-27203.16}
\]

This is the sharp metric transfer missing from the old capacity argument.

## 5. Prime-power consequence

Legendre's formula gives the exact atomized identity

\[
\log\binom nj
=
\sum_{q=p^a\le n}\Lambda(q)\chi_{n,j}(q).
\tag{L-27203.17}
\]

Since `v(q)<=w_X(q)` and `Lambda(q)>=0`,

\[
\sum_{q=p^a\le X}\frac{\Lambda(q)}{\sqrt q}\log(X/q)
\ge
\sum_{n,j}d_{n,j}\log\binom nj.
\tag{L-27203.18}
\]

Therefore

\[
\boxed{
\sum_{q=p^a\le X}\frac{\Lambda(q)}{\sqrt q}\log(X/q)
\ge
4\sqrt X-
\Sigma_X-O_\eta(\log^2X).}
\tag{L-27203.19}
\]

Exact MFT has `Sigma_X=0`. A near-saturating flow needs only
`Sigma_X=X^{o(1)}`.

## 6. Conceptual consequence

The sharp constant four is not extracted from an upper capacity bound. It is
the unweighted target mass. Balance makes binomial entropy and unweighted carry
count differ by only a square-root error per row, while feasibility forces the
total square-root row mass to be polylogarithmic.

This unifies:

- exact MFT;
- finite Gamma-carry minorants;
- Greedy Slack/DCRS;
- signed fragmentation flows with small total slack.

## 7. Proof boundary

Closed here:

- square-root mass control;
- direct entropy/carry comparison;
- correct sharp-prime-ramp implication.

Open:

- construction of a balanced nonnegative flow with `Sigma_X=X^{o(1)}`;
- MFT;
- RH.
