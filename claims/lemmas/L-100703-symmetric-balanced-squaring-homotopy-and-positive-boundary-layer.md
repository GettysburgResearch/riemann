# L-100703 — Symmetric balanced squaring homotopy and a corrected positive boundary layer

Claim ID: `L-100703`  
Status: **PROVED EXACT HOMOTOPY + FIXED-ORDER POSITIVITY LAYER WITH INACTIVE TAIL**  
Created: 2026-08-20  
Depends on: `L-100701`; corrected `L-100180`  
RH status: **not assumed**

Let `mathcal L` be the prime-label multiset containing one copy of every prime and a second independent copy of `67`.  For a label `ell` over the prime `p_ell`, put

\[
r_\ell=p_\ell^{-1/2},
\qquad
E_\ell=I-r_\ell U_{p_\ell},
\]

\[
Q_\ell=I-r_\ell^2U_{p_\ell^2},
\qquad
R_\ell=r_\ell U_{p_\ell}-r_\ell^2U_{p_\ell^2}.
\]

Then `E_ell=Q_ell-R_ell`.  For `0<=t<=1`, define

\[
\boxed{
H_{\ell,t}=Q_\ell-tR_\ell
=I-tr_\ell U_{p_\ell}-(1-t)r_\ell^2U_{p_\ell^2}.
}
\tag{L-100703.1}
\]

For a finite label set `Lambda`, put

\[
H_{\Lambda,t}=\prod_{\ell\in\Lambda}H_{\ell,t}.
\]

## 1. Exact finite homotopy

Finite differentiation gives

\[
{d\over dt}H_{\Lambda,t}
=-\sum_{\ell\in\Lambda}
R_\ell\prod_{h\in\Lambda\setminus\{\ell\}}H_{h,t}.
\]

Hence

\[
\boxed{
\prod_{\ell\in\Lambda}E_\ell
=
\prod_{\ell\in\Lambda}Q_\ell
-
\int_0^1
\sum_{\ell\in\Lambda}R_\ell
\prod_{h\ne\ell}H_{h,t}\,dt.
}
\tag{L-100703.2}
\]

The two labelled copies of `67` are separate factors throughout.  The previous notation `prod_p` plus an ad hoc extra budget term obscured this source typing.

## 2. Correct object acted upon

For fixed `m>=3`, define the positive unsieved critical carrier

\[
\mathcal K_m(X)
=4^mX^{m/2}
\kappa_{m,m-1}(X^{-1/2}).
\tag{L-100703.3}
\]

Then the native final centered-Bernstein remainder is

\[
R_{m,m-1}(X)
=
\left(\prod_{\ell\in\mathcal L}E_\ell\right)\mathcal K_m(X)
\tag{L-100703.4}
\]

in the absolutely convergent source sense.  Define the interpolating physical state by

\[
R_{m,t}(X)
=
\left(\prod_{\ell\in\mathcal L}H_{\ell,t}\right)\mathcal K_m(X).
\tag{L-100703.5}
\]

Thus `R_(m,1)=R_(m,m-1)` and `R_(m,0)` is its fully squared completion.  The former expression `(H_tR_(m,m-1))(X)` applied a second Euler family to an already native source and is withdrawn.

## 3. Corrected owner budget

The critical removal cost of an active ordinary label is at most `1/p`; a squared label costs at most `1/p^2`.  Because `mathcal K_m` is noncompact, ordinary labels with `p>X` contribute an inactive tail.  For fixed `m`,

\[
\Sigma_{m,t}(X)
\le
 t\sum_{\substack{\ell\in\mathcal L\\p_\ell\le X}}{1\over p_\ell}
 +(1-t)\sum_{\ell\in\mathcal L}{1\over p_\ell^2}
 +t\,R_m^{\rm inact}(X),
\tag{L-100703.6}
\]

where

\[
R_m^{\rm inact}(X)
\ll_m
\sqrt X\sum_{p>X}p^{-3/2}
\ll_m {1\over\log(2X)}.
\tag{L-100703.7}
\]

Put

\[
H_X^*=\sum_{\substack{\ell\in\mathcal L\\p_\ell\le X}}{1\over p_\ell},
\qquad
P_2^*=\sum_{\ell\in\mathcal L}{1\over p_\ell^2}
< {95\over196}+{1\over4489},
\]

and choose

\[
t_{m,X}
=
\min\left(1,
{1\over4(H_X^*+R_m^{\rm inact}(X))}
\right).
\tag{L-100703.8}
\]

For `0<=t<=t_(m,X)`,

\[
\Sigma_{m,t}(X)
< {1\over4}+{95\over196}+{1\over4489}<1.
\]

Adjacent-level pairing therefore proves

\[
\boxed{
R_{m,t}(X)>0
\qquad
(0\le t\le t_{m,X}).
}
\tag{L-100703.9}
\]

Since `H_X^*=log log X+O(1)`, the positive layer still has width comparable to `1/log log X` for each fixed `m`.

## 4. Exact boundary

The original critical state is `t=1`.  The remaining arithmetic is the balanced interval

\[
t_{m,X}<t\le1,
\]

with the completed-minus-transition cancellation retained.  This theorem does not prove positivity there and does not produce a fixed one-signed Landau density.
