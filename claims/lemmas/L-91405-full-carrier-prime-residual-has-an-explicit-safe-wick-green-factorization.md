# L-91405 — The full-carrier prime residual has an explicit safe Wick–Green factorization

Claim ID: `L-91405`  
Status: **PROVED EXACT FULL-CARRIER PRIME-SIDE FACTORIZATION; COMPLETED BOUNDARY DOMINATION OPEN**  
Created: 2026-08-12  
Depends on: `L-91026`, `L-91307`, `L-91402`, `L-91404`  
RH status: **unproved**

## 1. The causal residual state

Fix one safe scale

\[
 a>\frac12.
\]

Let `Psi_a` be the rational spectral factor of `L-91026`, and let

\[
 \psi_a(t)
 =\mathbf1_{t\ge0}
  \sum_{r\in\{1,2,4\}}
  (A_{r,a}+B_{r,a}t)e^{-rat}
\tag{L-91405.1}
\]

be its causal inverse Fourier transform.  The coefficients are the exact
residues of `Psi_a`; they may be complex.

For a carrier `x`, put

\[
 \psi_{a,x}(v)=e^{ixv}\psi_a(v).
\tag{L-91405.2}
\]

For `tau>0`, define the cross-correlation

\[
 \boxed{
 k_{a;x,y}(\tau)
 =\int_0^\infty
  \psi_{a,x}(v+\tau)
  \overline{\psi_{a,y}(v)}\,dv.
 }
\tag{L-91405.3}

Then

\[
 k_{a;x,y}(-\tau)
 =\int_0^\infty
  \psi_{a,x}(v)
  \overline{\psi_{a,y}(v+\tau)}\,dv.
\tag{L-91405.4}

On the diagonal,

\[
 k_{a;x,x}(\tau)+k_{a;x,x}(-\tau)
 =2\mathfrak r_a(\tau)\cos(x\tau),
\tag{L-91405.5}
\]

where `mathfrak r_a=psi_a*tilde(psi_a)` is the physical residual kernel.

## 2. The critical prime measure and its safe tilts

Let

\[
 \boxed{
 d\Pi(\tau)
 =\sum_{n=p^k}
  \frac{\Lambda(n)}{\sqrt n}
  \delta_{\log n}(d\tau).
 }
\tag{L-91405.6}
\]

This measure is locally finite but has infinite total mass.  For
`r in {1,2,4}`, define its safe tilt

\[
 \boxed{
 d\Pi_{r,a}(\tau)
 =e^{-ra\tau}d\Pi(\tau).
 }
\tag{L-91405.7}
\]

Because `ra+1/2>1`, every polynomial moment of `Pi_(r,a)` is finite.
Moreover, if `sigma_r=1/2+ra` and `N_(sigma_r)` is Nakamura's positive prime
atomic measure, then

\[
 \boxed{
 d\Pi_{r,a}(\tau)
 =\tau\,d\mathsf N_{\sigma_r}(\tau).
 }
\tag{L-91405.8}

Thus all spaces below are resident safe-line prime first-chaos spaces.

## 3. Two explicit source maps

For each `r`, let

\[
 \mathcal X_{r,a}
 =L^2\left((0,\infty)_\tau\times(0,\infty)_v,
           d\Pi_{r,a}(\tau)\,dv\right).
\tag{L-91405.9}
\]

Define, for every carrier `x`,

\[
 \boxed{
 U_{r,a,x}(\tau,v)
 =e^{ix(v+\tau)}
  (A_{r,a}+B_{r,a}(v+\tau))e^{-rav},
 }
\tag{L-91405.10}
\]

and

\[
 \boxed{
 V_{r,a,x}(\tau,v)
 =e^{ixv}\psi_a(v).
 }
\tag{L-91405.11
}

Both belong to `X_(r,a)`.  Indeed, `V` has norm

\[
 \Pi_{r,a}((0,\infty))\|\psi_a\|_2^2<\infty,
\]

while `U` is controlled by the first two polynomial moments of `Pi_(r,a)` and
the exponential decay in `v`.

Let

\[
 \mathcal X_a=\bigoplus_{r\in\{1,2,4\}}\mathcal X_{r,a}
\]

and write

\[
 U_{a,x}=(U_{r,a,x})_r,
 \qquad
 V_{a,x}=(V_{r,a,x})_r.
\tag{L-91405.12}
\]

## 4. Exact cross-correlation identities

Expanding `psi_a(v+tau)` by (L-91405.1) and using the tilt
`e^(-ra tau)` in `Pi_(r,a)` gives

\[
 \boxed{
 \langle U_{a,x},V_{a,y}\rangle_{\mathcal X_a}
 =\int_0^\infty
  k_{a;x,y}(\tau)d\Pi(\tau).
 }
\tag{L-91405.13}

Similarly,

\[
 \boxed{
 \langle V_{a,x},U_{a,y}\rangle_{\mathcal X_a}
 =\int_0^\infty
  k_{a;x,y}(-\tau)d\Pi(\tau).
 }
\tag{L-91405.14}

These are fully polarized identities for arbitrary independent carriers `x`
and `y`. No scalar-diagonal reconstruction is used.

## 5. The prime explicit-formula block

For the Weil test

\[
 u\longmapsto
 \Psi_a(u-x)\overline{\Psi_a(u-y)},
\]

the prime-power contribution in the repository Fourier normalization is

\[
 \boxed{
 \mathfrak P_a(x,y)
 =-\int_0^\infty
  \left[
   k_{a;x,y}(\tau)+k_{a;x,y}(-\tau)
  \right]d\Pi(\tau).
 }
\tag{L-91405.15}

On `x=y`, (L-91405.5) reduces this exactly to

\[
 -2\sum_{n\ge2}
 \frac{\Lambda(n)}{\sqrt n}
 \mathfrak r_a(\log n)\cos(x\log n),
\]

the prime residual of `T-91005` before the common factor `a^(-4)`.

Equations (L-91405.13)--(L-91405.15) give

\[
 \boxed{
 \mathfrak P_a(x,y)
 =-\langle U_{a,x},V_{a,y}\rangle
  -\langle V_{a,x},U_{a,y}\rangle.
 }
\tag{L-91405.16}

## 6. Exact Wick–Green decomposition

Define the jump-difference vector

\[
 \boxed{
 D_{a,x}=U_{a,x}-V_{a,x}.
 }
\tag{L-91405.17}

Polarization of the elementary identity

\[
 \|U-V\|^2
 =\|U\|^2+\|V\|^2-2\Re\langle U,V\rangle
\]

gives

\[
 \boxed{
\begin{aligned}
 \mathfrak P_a(x,y)
 ={}&\langle D_{a,x},D_{a,y}\rangle_{\mathcal X_a}\\
 &-\langle U_{a,x},U_{a,y}\rangle_{\mathcal X_a}\\
 &-\langle V_{a,x},V_{a,y}\rangle_{\mathcal X_a}.
\end{aligned}}
\tag{L-91405.18}

Thus the full-carrier prime block is exactly

```text
positive jump-difference Gram
minus two explicit positive endpoint Grams.
```

All three terms live in finite positive Hilbert spaces built from safe tilted
prime measures.  This is the source-side Wick–Green factorization requested by
the Julia programme.

## 7. Completed boundary remainder

Let

\[
 \mathfrak A_a(x,y)
\]

be the complete archimedean and pole contribution of the same residual Weil
test.  The full completed residual Gram is

\[
 \mathfrak W_a(x,y)
 =\mathfrak A_a(x,y)+\mathfrak P_a(x,y).
\tag{L-91405.19}
\]

Using (L-91405.18),

\[
 \boxed{
 \mathfrak W_a(x,y)
 =\langle D_{a,x},D_{a,y}\rangle
  +\mathfrak B_a(x,y),
 }
\tag{L-91405.20
}

where the exact Green boundary kernel is

\[
 \boxed{
\begin{aligned}
 \mathfrak B_a(x,y)
 ={}&\mathfrak A_a(x,y)\\
 &-\langle U_{a,x},U_{a,y}\rangle\\
 &-\langle V_{a,x},V_{a,y}\rangle.
\end{aligned}}
\tag{L-91405.21
}

No term has been estimated or discarded.  A proof

\[
 \mathfrak B_a\succeq0
\]

would be a sufficient source-complete proof of residual Weil positivity at the
fixed scale.  More generally, a conservative coupling of `B_a` with the
jump-difference port may prove positivity through a Schur complement even if
`B_a` is not separately positive.

## 8. Delays and orientations

Carrier modulation can be supplemented by the compressed delay semigroup of
`L-91401`.  Replacing each resident input by `T_tau g` and retaining its Julia
leakage preserves every mixed-delay cross term.  Hardy reflection gives the
opposite orientation.

Therefore (L-91405.18)--(L-91405.21) lift without scalar polarization loss to
the delayed two-sided packet.  The finite bridge still requires its exact
boundary/source insertion.

## 9. Strategic consequence

The previously vague renormalization problem is now one explicit boundary
problem:

\[
 \boxed{
 \text{completed gamma/pole/theta kernel}
 \quad\text{versus}\quad
 U_a^*U_a+V_a^*V_a.
 }
\]

The positive prime production port `D_a` is already complete.  The load-bearing
joint is to show that the completed archimedean/pole source, together with the
bridge and delay leakage, absorbs the two endpoint Grams with coefficient one.

This statement is compatible with the negative-channel firewall `R-91403`:
the long-jump archimedean sector is one explicit part of `B_a`, not free
positive budget.

## 10. Exact boundary

```text
causal rational state expansion                    EXACT
safe tilted prime source spaces                    EXACT
full independent-carrier prime block               EXACT
positive jump-difference production port           EXACT
explicit endpoint counterterms                     EXACT
Wick-Green identity                                EXACT
completed Green boundary kernel                    EXPLICIT
boundary kernel / Schur complement positivity      OPEN / RH-BEARING
delayed bridge completion                          OPEN
Riemann Hypothesis                                  UNPROVED
```
