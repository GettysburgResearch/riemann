# L-93282 - A negative phase-locked Hermite carrier forces a finite safe-line covariance

Claim ID: `L-93282`  
Status: **PROPOSED COMPLETE EXACT INVERSE THEOREM - INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-93280`, `L-93281`; the first-Hermite explicit formula of PR #379 and its phase-locked multiplication from PR #520  
RH status: **not assumed**

## 1. Exact covariance variable

Put

\[
\mathfrak C_{q,m}(t)
=\int_0^\infty B_{q,m}(r)\mathcal G_C(r,t)\,dr.
\tag{L-93282.1}
\]

By `L-93281`,

\[
\mathfrak C_{q,m}(t)
=S_{q,m}(t)-S_{q,m}^{\rm cont}(t).
\tag{L-93282.2}
\]

The filtered Guinand-Weil formula has the form

\[
\mathcal M_m(q,t)
=\mathcal A_m(q,t)
-c_q\Re S_{q,m}(t),
\qquad c_q>0,
\tag{L-93282.3}
\]

where `A_m` is the explicit pole plus gamma contribution. Define the exact
centered reserve

\[
\mathcal R_m(q,t)
=\mathcal A_m(q,t)
-c_q\Re S_{q,m}^{\rm cont}(t).
\tag{L-93282.4}
\]

Then

\[
\boxed{
\mathcal M_m(q,t)
=\mathcal R_m(q,t)-c_q\Re\mathfrak C_{q,m}(t).
}
\tag{L-93282.5}
\]

Every term is an absolutely convergent explicit integral or a finite-energy
safe-line pairing.

## 2. Inverse theorem

If

\[
\mathcal M_m(q,t)<0,
\]
then

\[
\boxed{
\Re\mathfrak C_{q,m}(t)
>\frac{\mathcal R_m(q,t)}{c_q}.
}
\tag{L-93282.6}
\]

Cauchy-Schwarz and `L-93280` yield

\[
\boxed{
\frac{\mathcal R_m(q,t)}{c_q}
<\|B_{q,m}\|_2\,\|\mathcal G_C(\cdot,t)\|_2
\ll\|B_{q,m}\|_2\log^2(2+|t|).
}
\tag{L-93282.7}
\]

Thus every negative carrier is a finite, normalized covariance witness on the
safe line. The old statement that a raw scale-field norm must be small is
replaced by the exact signed scalar (L-93282.1).

## 3. Why this still does not close by absolute values

The norm of the synthesis vector has the exact Plancherel representation

\[
\boxed{
\|B_{q,m}\|_2^2
=\frac1{2\pi}\int_{\mathbb R}
\left|
\frac{P(\xi+i/2)^{2m}\widehat h_q(\xi+i/2)}
{\widehat W_C(1-i\xi)}
\right|^2d\xi.
}
\tag{L-93282.8}
\]

Near the critical saddle, `P(xi+i/2)` has a simple zero while `W_C(1-i xi)`
has a double zero. For fixed or sublinear `m`, the Gaussian still contributes
the boundary factor `e^(q/4)`. The maximum-modulus firewall of `R-94054`
therefore remains binding: an absolute safe-line norm cannot be exponentially
smaller than every retained terminal depth.

The remaining producer is genuinely signed:

\[
\boxed{
\mathrm{SCID}_{\rm PL}:
\quad
c_q\Re\mathfrak C_{q,m}(t)\le\mathcal R_m(q,t)
\quad(q>0,t\in\mathbb R,m\ge1).
}
\tag{L-93282.9}
\]

Proving `SCID_PL` gives the filtered First-Hermite inequalities and RH. It is
not proved here and is not replaced by the unconditional norm bound.
