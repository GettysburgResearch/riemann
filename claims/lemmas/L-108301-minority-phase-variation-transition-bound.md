# L-108301 — Minority fifth-companion phase controls the direct reverse–Rolle loss

Claim ID: `L-108301`  
Status: **PROVED EXACT FINITE-WINDOW THEOREM**  
Created: 2026-08-31  
Depends on: `L-108300`; the direct residue-transition criterion  
RH status: **not assumed**

Let

\[
c_1<\cdots<c_M
\]

be consecutive simple real zeros of \(f^{(5)}\) in a regular interval, with
\(f(c_j)\ne0\), and put

\[
\rho_j={f(c_j)\over f^{(6)}(c_j)}.
\]

Let \(U_+\) and \(U_-\) be the numbers of positive and negative residues, and
let

\[
V_5=\#\{1\le j<M:\rho_j\rho_{j+1}<0\}.
\]

## 1. Direct interval production

The signs of \(f^{(6)}(c_j)\) alternate at consecutive simple zeros of
\(f^{(5)}\). Hence

\[
\rho_j\rho_{j+1}>0
\quad\Longrightarrow\quad
f(c_j)f(c_{j+1})<0.
\]

Every same-sign residue edge therefore contains a real zero of \(f\). With
the endpoint, common-zero, multiplicity and exhaustion loss denoted by
\(\mathcal E_{\rm reg}\),

\[
\boxed{
N_{\mathbb R}(f;I)
\ge M-1-V_5-\mathcal E_{\rm reg}.
}
\tag{L-108301.1}
\]

## 2. Minority-sign bound

For every two-colour path, each vertex of the minority colour is incident to
at most two colour-changing edges. Therefore

\[
\boxed{
V_5\le2\min(U_+,U_-).
}
\tag{L-108301.2}
\]

By `L-108300`,

\[
U_\sigma
=
\lim_{\varepsilon\downarrow0}
\mathscr U_{\sigma,\varepsilon}(f;I)
\qquad(\sigma=\pm1),
\]

so

\[
\boxed{
N_{\mathbb R}(f;I)
\ge
M-1
-
2\min_{\sigma=\pm1}
\lim_{\varepsilon\downarrow0}
\mathscr U_{\sigma,\varepsilon}(f;I)
-
\mathcal E_{\rm reg}.
}
\tag{L-108301.3}
\]

This is strictly more economical than paying all five adjacent-rung Cauchy
layers: it uses one endpoint Wronskian and automatically chooses the minority
residue orientation.

## 3. Exact percentage thresholds

Suppose, on \(I_T=(T,2T)\),

\[
M(T)\ge(p_5-o(1))N(T,2T).
\]

Then more than \(90\%\) follows from

\[
\boxed{
\limsup_{T\to\infty}
{2\min_\sigma U_\sigma(T)+\mathcal E_{\rm reg}(T)
 \over N(T,2T)}
<
p_5-\frac9{10}.
}
\tag{L-108301.4}
\]

Three useful exact specializations are

\[
p_5={9863\over10000}
\quad\Longrightarrow\quad
\min_\sigma U_\sigma+\frac12\mathcal E_{\rm reg}
<
{863\over20000}N,
\tag{L-108301.5}
\]

\[
p_5={997\over1000}
\quad\Longrightarrow\quad
\min_\sigma U_\sigma+\frac12\mathcal E_{\rm reg}
<
{97\over2000}N,
\tag{L-108301.6}
\]

and

\[
p_5={49\over50}
\quad\Longrightarrow\quad
\min_\sigma U_\sigma+\frac12\mathcal E_{\rm reg}
<
{1\over25}N.
\tag{L-108301.7}
\]

The first two values are inherited programme inputs and are not re-proved
here; the implication is exact for any supplied \(p_5\).

## Scope

The theorem closes the combinatorial and phase-coordinate passage. The
Xi-specific minority phase-variation estimate remains open.
