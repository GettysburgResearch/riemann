# T-99810 — Two exact owner-square integrators for the canonical scalar spine

Claim ID: `T-99810`  
Status: **UNCONDITIONAL INTEGRATOR / ARITHMETIC PACKING STILL OPEN**  
Created: 2026-08-20  
Frozen base: PR #659 at `83c17b32a99ac9e1aa5aec3168535550eb286636`  
Imported native source: PR #660 at `ca3c055307e6804ae904cb9105594dd3f2408ba3`  
RH status: **unproved**

Use PR #659's notation

\[
 c_{L,y}(n)=\frac{\beta_{67}(n)}{\sqrt n}
 (\mathcal F_LT)(y/n),
 \qquad
 \tau_L=\frac1{\log(L+e)},
\]

and the inverse coefficients

\[
 b_{L,k}=\binom{M_L+k-1}{k}.
\]

## I. Exact Hardy-tail gate

Put

\[
 S_{L,y}(t)=\sum_{n\ge t}c_{L,y}(n).
\]

By `L-99810`,

\[
 Q_L(y)
 =|f_L(y)|^2
 +2\tau_L\int_1^\infty
 t^{2\tau_L-1}|S_{L,y}(t)|^2dt.
\tag{T-99810.1}
\]

Therefore `GPMOC99800` is exactly the following tail-Carleson statement:

\[
\boxed{
\sum_{k=0}^{L+1}b_{L,k}
\int_{2^{L-k}}^{2^{L+1-k}}
\left(
 |f_L(y)|^2
 +2\tau_L\int_1^\infty
 t^{2\tau_L-1}|S_{L,y}(t)|^2dt
\right)^{1/2}\frac{dy}{y}
=2^{o(L)}.
}
\tag{HTOC99810}
\]

This is an equivalent positive normal form, not an additional hypothesis
hidden behind phase notation.

## II. Divisor-GCD alternative

Define

\[
 \mathcal G_L(y)=
 \sum_{d\ge1}J_{2\tau_L}(d)
 \left|\sum_{d\mid n}c_{L,y}(n)\right|^2.
\tag{T-99810.2}
\]

By `L-99811`, `|f_L(y)|^2<=mathcal G_L(y)`. Hence the independently sufficient
condition

\[
\boxed{
\sum_{k=0}^{L+1}b_{L,k}
\int_{2^{L-k}}^{2^{L+1-k}}
\sqrt{\mathcal G_L(y)}\frac{dy}{y}
=2^{o(L)}
}
\tag{DGOC99810}
\]

implies subpower negative mass for the compact zero-safe packet. The exact
Mellin--Landau consumer of PR #659 then gives RH.

## III. Native first-owner Hardy gate

Let

\[
 F=s_kI+\sum_i\lambda_i\Delta_i^{\rm fut}
\]

be the coefficient-exact native first-owner decomposition. By `L-99812`,

\[
 Q_{\tau_L}(Ff)
 \le s_kQ_{\tau_L}(f)
 +\sum_i\lambda_iQ_{\tau_L}(\Delta_i^{\rm fut}f).
\tag{T-99810.3}
\]

Thus one may prove `HTOC99810` by estimating the right side of
(T-99810.3) in the exact endpoint blocks. This route uses the actual native
Euler coefficients and the actual physical Hardy target. It does not use the
refuted alpha-child source or an uncontrolled labelled collapse.

## IV. Exact status

The packet proves:

```text
Poisson phase packet = exact truncated-tail square       PROVED
multiplicative evaluation = exact divisor-GCD square     PROVED
native first-owner Hardy convexity                       PROVED
diagonal/source-blind closure                            REFUTED
HTOC99810 / GPMOC99800 arithmetic tail packing           OPEN
DGOC99810 divisor-owner packing                          OPEN
Riemann Hypothesis                                       UNPROVED
```

The only unresolved content is the signed squarefree-core packing inside one
of the two displayed positive squares. No remaining normalization, source
coefficient, phase-evaluation, inverse-filter, or Landau interface is hidden.