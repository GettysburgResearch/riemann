# L-105443 — Base-height flow is an adjacent-derivative ratio curvature

Claim ID: `L-105443`  
Status: **PROVED EXACT DIFFERENTIAL IDENTITY**  
Created: 2026-08-24  
Depends on: `L-105442`  
RH status: **not assumed**

## 1. Adjacent-rung ratio

For

\[
F_r=\Xi^{(r)},
\qquad
m_r={F_r\over F_{r+1}},
\]

put

\[
\boxed{
\mathcal R_r(z)
={F_r(z)F_{r+2}(z)\over F_{r+1}(z)^2}
={m_r(z)\over m_{r+1}(z)}.
}
\tag{L-105443.1}

Direct differentiation gives

\[
\boxed{m_r'(z)=1-\mathcal R_r(z).}
\tag{L-105443.2}

Thus the nonlinear adjacent-derivative ratio is exactly the defect from the
identity map in the reciprocal field.

## 2. Base and scale derivatives

Use the shifted minimal field

\[
\mathcal Q_{r,b}(a,h)
=-{4\over3}\Im m_r(z_1)
+{2\over3}\Im m_r(z_2),
\]

where

\[
z_1=a+i(b+h),
\qquad
z_2=a+i(b+2h).
\]

Cauchy--Riemann gives

\[
{d\over dy}\Im m_r(a+iy)=\Re m_r'(a+iy).
\]

Using (L-105443.2), one obtains the exact base-height identity

\[
\boxed{
\partial_b\mathcal Q_{r,b}(a,h)
={2\over3}
\left[
2\Re\mathcal R_r(z_1)
-
\Re\mathcal R_r(z_2)
-1
\right].
}
\tag{L-105443.3}

The exact physical-scale derivative is

\[
\boxed{
\partial_h\mathcal Q_{r,b}(a,h)
={4\over3}
\left[
\Re\mathcal R_r(z_1)
-
\Re\mathcal R_r(z_2)
\right].
}
\tag{L-105443.4}

No zero-location or sign hypothesis is used wherever the sampled ratios are
holomorphic.

## 3. First-contact interpretation

The zero-height variational principle starts with

\[
\mathcal Q_{r,b}\le0
\]

for every `b>=1/2` and seeks descent to `b=0`.

Suppose a finite contact occurs at

\[
\mathcal Q_{r,b_*}(a_*,h_*)=0
\]

while the field is nonpositive for all slightly larger bases. If the field
becomes positive immediately below `b_*`, then necessarily

\[
\boxed{
\partial_b\mathcal Q_{r,b_*}(a_*,h_*)\le0.
}
\tag{L-105443.5}

Therefore every such contact obeys the adjacent-rung inequality

\[
\boxed{
2\Re\mathcal R_r(z_1)
-
\Re\mathcal R_r(z_2)
\le1.
}
\tag{L-105443.6}

Conversely, the strict reverse inequality at every finite zero contact would
exclude that contact mechanism.

This is a typed contact condition, not a globally valid inequality. Direct
numerical and polynomial fixtures show that no source-free global monotonicity
of `Re mathcal R_r` should be expected.

## 4. Simple-zero calibration

Let `z_0=a_0+i beta` be a simple zero of `F_r`, and approach it from the base

\[
b=\beta-\delta.
\]

Locally,

\[
m_r(z)=z-z_0+O((z-z_0)^2),
\]

so

\[
\mathcal R_r(z)=O(z-z_0).
\]

Equation (L-105443.3) then gives

\[
\boxed{
\partial_b\mathcal Q_{r,b}(a_0,h)
=-{2\over3}+o(1),
}
\tag{L-105443.7}

matching the local detector

\[
\mathcal Q_{r,b}(a_0,h)
={2\over3}(\beta-b)+o(|\beta-b|).
\]

Thus an off-line zero crosses the microscope boundary with one universal
transverse speed.

## 5. Contact-curvature target

The exact identity suggests one possible source-facing theorem:

```text
ACCR105443 — adjacent-ratio contact rigidity

At every finite first contact of the Xi minimal microscope,

  2 Re R_r(a+i(b+h)) - Re R_r(a+i(b+2h)) > 1.
```

Such a theorem would rule out finite sign contact. It would not by itself rule
out a pole obstruction or a contact escaping to `h=0` or `|a|=infinity`; those
interfaces must be handled separately.

The oriented-ratio and one-sided-Hardy programmes already produce the
adjacent-rung reciprocal fields entering `mathcal R_r`. Equation
(L-105443.3) is the exact consumer interface for any future phase-gap estimate.

## 6. Scope

`ACCR105443` is not proved and is not asserted globally. The lemma contributes
only the exact differential dictionary and the universal simple-zero crossing
calibration.
