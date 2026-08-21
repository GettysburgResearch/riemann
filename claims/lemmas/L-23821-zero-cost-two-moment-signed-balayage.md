# L-23821 — Zero-cost two-moment signed balayage

Claim ID: `L-23821`  
Title: An arbitrary high-rank signed residual in one logarithmic cell can be transported to its two endpoints with exactly zero prime objective cost  
Status: **PROPOSED EXACT FINITE THEOREM — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #238  
Dependencies: PR #248 `L-24517/L-24520`; exact finite transport algebra  
Scope: ordinary-prime residuals after the polylogarithmic proper-prime-power reduction

## 1. Cell residual and its two moments

Let

\[
p_0<p_1<\cdots<p_m
\tag{L-23821.1}
\]

be the ordinary primes in one finite cell and put

\[
x_i=\log p_i.
\tag{L-23821.2}
\]

Let

\[
r=\sum_{i=0}^{m}r_i\delta_{p_i}
\tag{L-23821.3}
\]

be an arbitrary real signed residual. No sign, rank, or source-factorization
hypothesis is imposed.

Define its total and logarithmic moments

\[
M=\sum_{i=0}^{m}r_i,
\qquad
L=\sum_{i=0}^{m}x_i r_i.
\tag{L-23821.4}
\]

Assume first `m>=1` and put

\[
D=x_m-x_0>0.
\tag{L-23821.5}
\]

Define endpoint charges

\[
\boxed{
 A=\frac{x_mM-L}{D},
 \qquad
 B=\frac{L-x_0M}{D}.}
\tag{L-23821.6}
\]

Then

\[
A+B=M,
\qquad
x_0A+x_mB=L.
\tag{L-23821.7}
\]

Thus

\[
\mathcal B_Ir=A\delta_{p_0}+B\delta_{p_m}
\tag{L-23821.8}
\]

is the unique measure on the two cell endpoints having the same two moments as
`r`.

## 2. Exact prime-incidence transport

PR #248 `L-24520` gives a constant carry block

\[
\mathcal T(a,b;t)
\tag{L-23821.9}
\]

whose residual change is

\[
+t\delta_a-t\delta_b
\tag{L-23821.10}
\]

and whose exact prime-objective loss is

\[
t\log(b/a).
\tag{L-23821.11}
\]

For every interior index `1<=i<=m-1`, put

\[
\alpha_i=r_i\frac{x_m-x_i}{D},
\qquad
\beta_i=r_i\frac{x_i-x_0}{D}.
\tag{L-23821.12}
\]

Apply the two signed transports

\[
\mathcal T(p_0,p_i;\alpha_i),
\qquad
\mathcal T(p_i,p_m;-\beta_i).
\tag{L-23821.13}
\]

Their combined residual change is

\[
\alpha_i\delta_{p_0}
-(\alpha_i+\beta_i)\delta_{p_i}
+\beta_i\delta_{p_m}.
\tag{L-23821.14}
\]

Since

\[
\alpha_i+\beta_i=r_i,
\tag{L-23821.15}
\]

the entire interior mass at `p_i` is removed.

Summing over the interior indices leaves exactly (L-23821.8), including the
original endpoint masses.

## 3. The transport cost is identically zero

The objective loss for the `i`th pair is

\[
\begin{aligned}
&\alpha_i(x_i-x_0)
-\beta_i(x_m-x_i)\\
&\quad=
 r_i\frac{(x_m-x_i)(x_i-x_0)}D
-r_i\frac{(x_i-x_0)(x_m-x_i)}D\\
&\quad=0.
\end{aligned}
\tag{L-23821.16}
\]

Therefore the complete cell transport satisfies

\[
\boxed{
\text{prime-objective loss}(r\longrightarrow\mathcal B_Ir)=0.}
\tag{L-23821.17}
\]

The result is exact for signed residuals. It does not use positivity of the
transport amounts.

## 4. Interpretation

The operator

\[
r\longmapsto\mathcal B_Ir
\tag{L-23821.18}
\]

is a discrete logarithmic balayage. It preserves precisely the two scalar
functionals relevant to incidence transport:

```text
total residual mass;
logarithmic prime-objective moment.
```

It annihilates every cell residual with both moments zero by an exact
zero-objective correction.

This is materially different from the withdrawn two-contact theorem:

- it does **not** claim that the arithmetic source has only two coordinates;
- it does **not** count terminal faces;
- it permits an arbitrarily high-rank same-sign Möbius cube;
- it is applied after the complete signed residual has been formed;
- its two endpoint charges are aggregate moments, not free source variables.

## 5. High-rank mutation

For the PR #239 same-sign rank-`K` cube, place all products falling in one
logarithmic cell into (L-23821.3). The cube may have `2^K` distinct points and
rank `K`. Equations (L-23821.6)--(L-23821.17) still reduce its complete signed
residual to two aggregate endpoint charges at exactly zero objective cost.

The cube can therefore invalidate a source-rank argument without invalidating
this transport identity.

## 6. Degenerate cells and full partition

A one-point cell is left unchanged. A two-point cell already equals its
balayage. Applying the construction independently to a disjoint partition of
the ordinary-prime coordinates gives a global signed transport whose total
objective cost remains zero.

Proper prime powers may first be removed at `O(log^2 X)` cost using PR #248
`L-24517`.

## 7. Proof boundary

Closed exactly:

- two-moment endpoint charges;
- an explicit signed incidence transport realizing them;
- exact zero objective cost;
- robustness to arbitrary arithmetic rank and sign pattern.

Open:

- a source-specific lower-scale barrier for the aggregate endpoint charges;
- the scalar prime-ramp estimate;
- RH.
