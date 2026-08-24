# T-105410 — Second-order Xi centering sharply enlarges the unconditional capacity prefix

Claim ID: `T-105410`  
Status: **MAJOR UNCONDITIONAL HIGH-DERIVATIVE ADVANCE; LOW-ORDER DESCENT OPEN**  
Created: 2026-08-24  
Depends on: `T-105390`, `L-105410--L-105412`  
RH status: **unproved**

## 1. Sharp model reserve

At fixed matrix order `k`, the trigonometric tail after `J` critical pairs has

\[
\lambda_{\min}
(\mathsf R_{k,p,J}^{(a)})
\asymp_{k,a}
J^{-(4k+2a-3)}.
\tag{T-105410.1}
\]

The worst block is the shifted block:

\[
\boxed{q_k=4k-1.}
\tag{T-105410.2}
\]

This replaces the earlier sufficient exponent `d_k=3k(k-1)+4`.

## 2. Second-order source and prefix errors

Put

\[
\mathcal R_r=r\omega_r.
\]

At fixed order, `L-105410` gives normalized source-entry error `O_k(mathcal R_r^-1)`. For the first `J` actual critical pairs it gives

\[
|\Delta_0^{\rm prefix}|
\ll {J\over\mathcal R_r},
\qquad
|\Delta_n^{\rm prefix}|
\ll_n {1\over\mathcal R_r}
\quad(n\ge1).
\tag{T-105410.3}
\]

Conjugating by the natural diagonal `D_J` of `L-105411`, every source and prefix error is `o(1)` relative to the model tail whenever

\[
\boxed{
{J^{4k-1}\over\mathcal R_r}
\longrightarrow0.
}
\tag{T-105410.4}
\]

No common isotropic `J^(-d_k)` moment bound is used.

## 3. Enlarged growing-prefix theorem

Let `J_r` satisfy

\[
J_r\longrightarrow\infty,
\qquad
J_r=o(\sqrt{\mathcal R_r}),
\qquad
{J_r^{4k-1}\over\mathcal R_r}
\longrightarrow0.
\tag{T-105410.5}
\]

Then, for both parities and all sufficiently high `r`,

1. every critical point in the first `J_r` positive cells is real and simple;
2. every corresponding residue is negative;
3. there is no additional critical point in the controlled strip; and
4. for `a=0,1`,

\[
\boxed{
\widehat{\mathsf A}_{k,r}^{(a)}
-
\widehat{\mathsf C}_{k,r,J_r}^{(a)}
\succ0.
}
\tag{T-105410.6}
\]

Undoing the positive scaling congruence gives the physical source-capacity inequality.

Since `omega_r` is comparable to `log r`, one may take

\[
\boxed{
J_r=\lfloor r^\gamma\rfloor,
\qquad
0<\gamma<{1\over4k-1}.
}
\tag{T-105410.7}
\]

The first examples are

```text
k=1: gamma < 1/3;
k=2: gamma < 1/7;
k=3: gamma < 1/11.
```

The previous sufficient exponents were `1/10`, `1/22`, and `1/46`.

## 4. Finite-height terminal consequence

A physical Xi window of height `T` contains `J` high-derivative critical cells with

\[
J\asymp\omega_rT.
\]

Therefore, at every fixed packet order `k`, the complete sharp residue and boundary-capacity gates are unconditionally valid in that high-derivative window once

\[
\boxed{
{(\omega_rT)^{4k-1}\over r\omega_r}
\longrightarrow0.
}
\tag{T-105410.8}
\]

For example, any choice

\[
r(T)\ge T^{\,4k-1+\varepsilon}
\]

with a sufficiently large logarithmic factor is admissible. This supplies a much earlier fixed-packet terminal derivative for the reverse-Rolle programme. It does not descend that terminal positivity to derivative order zero.

## 5. Complete-tail endpoint collapse

Assume additionally the complete high-derivative critical hierarchy `CRVH105330` and only the scalar ordinary pivot `ZCAP105412`. Then `L-105412` proves

\[
\widehat\nu_r\Longrightarrow\nu_p
\]

for the complete critical measures, and every fixed-order complete boundary negative part tends to zero. Thus the earlier remote-tail gate is retyped as

```text
local trigonometric cells
+ complete sharp residue sign
+ one zeroth endpoint-mass pivot
-> all fixed remote moments and vanishing terminal negative part.
```

The scalar pivot and complete sharp sign remain open.

## 6. What has been removed

The following are no longer needed for the unconditional growing-prefix theorem:

```text
the moving complex saddle;
the crude d_k=3k(k-1)+4 conditioning exponent;
one common remote-moment rate at all moment orders;
atom-by-atom matching outside the controlled prefix.
```

## 7. Exact frontier

```text
second-order centered real-saddle approximation       PROVED / REVIEW REQUIRED
universal beta-tail scaling                           PROVED EXACT
sharp tail eigenvalue exponent 4k+2a-3               PROVED EXACT
growing prefix gamma<1/(4k-1)                        PROVED / REVIEW REQUIRED
fixed-height high-derivative packet endpoint          PROVED / REVIEW REQUIRED
complete remote moments from CRVH + zeroth pivot      PROVED CONDITIONAL
CRVH105330 complete critical sign                     OPEN / SHARP
ZCAP105412 scalar endpoint mass                       OPEN / BOUNDARY SCALAR
low-order reverse-Rolle descent                       OPEN
Riemann Hypothesis                                    UNPROVEN
```
