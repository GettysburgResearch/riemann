# L-105438 — The minimal two-height microscope detects every Xi critical residue

Claim ID: `L-105438`  
Status: **PROVED EXACT MINIMAL LOCALIZER THEOREM**  
Created: 2026-08-24  
Depends on: `L-105432--L-105434`  
RH status: **not assumed**

## 1. Definition

For

\[
F=\Xi^{(r)},
\qquad
m_r(z)={F(z)\over F'(z)},
\]

define

\[
\boxed{
\mathcal Q_r(a,h)
=-{4\over3}\operatorname{Im}m_r(a+ih)
+{2\over3}\operatorname{Im}m_r(a+2ih),
}
\tag{L-105438.1}

for real `a` and `h>0` whenever the two sampled denominators are nonzero.

## 2. Exact positive kernel

Put

\[
\boxed{
K_{a,h}(x)
={4h^3\over
((x-a)^2+h^2)((x-a)^2+4h^2)}.
}
\tag{L-105438.2}

Then

\[
\boxed{
K_{a,h}(x)
={4h/3\over(x-a)^2+h^2}
-{4h/3\over(x-a)^2+4h^2}>0.
}
\tag{L-105438.3}

It satisfies

\[
K_{a,h}(x)
={1\over h}K_{0,1}\!\left({x-a\over h}\right),
\qquad
\int_{\mathbb R}K_{a,h}(x)\,dx={2\pi\over3},
\tag{L-105438.4}

and

\[
\boxed{K_{a,h}(a)=1/h.}
\tag{L-105438.5}

Its Fourier multiplier is

\[
\boxed{
\widehat K_{0,h}(\xi)
={2\pi\over3}t(2-t)>0,
\qquad t=e^{-h|\xi|}.
}
\tag{L-105438.6}

Thus the minimal microscope kernel is both pointwise positive and positive
definite.

## 3. Exact residue recovery

At a simple noncommon real critical point,

\[
m_r(c+ijh)=-i{\rho_c\over jh}+O(1).
\]

Therefore

\[
\begin{aligned}
h\mathcal Q_r(c,h)
&=\rho_c\left({4\over3}-{1\over3}\right)+o(1)\\
&=\rho_c+o(1).
\end{aligned}
\]

Hence

\[
\boxed{
\lim_{h\downarrow0}h\mathcal Q_r(c,h)=\rho_c.}
\tag{L-105438.7}

## 4. Exact measure form under the critical sign

If all critical points are real and all residues are nonpositive, the Pick
representation of `L-105432--L-105433` gives

\[
\boxed{
\mathcal Q_r(a,h)
=
\sum_{F'(c)=0}\rho_cK_{a,h}(c)
\le0.
}
\tag{L-105438.8}

The affine Herglotz term cancels automatically because

\[
-{4\over3}h+{2\over3}(2h)=0.
\tag{L-105438.9}

Thus this localizer does not require the Xi-specific proof that the affine
coefficient vanishes.

## 5. Minimality

Consider a source-independent combination of one or two heights,

\[
\mathcal L(a,h)=\sum_{j=1}^Jc_j\Im m(a+jh),
\qquad J\le2.
\]

To cancel every affine term `az`, one needs

\[
\sum_jjc_j=0.
\tag{L-105438.10}

To recover a pole residue with the normalization

\[
h\mathcal L(c,h)\longrightarrow\rho_c,
\]

one needs

\[
-\sum_j{c_j\over j}=1.
\tag{L-105438.11}

No nonzero one-height coefficient satisfies both equations. For heights `h`
and `2h`, the unique solution is

\[
\boxed{c_1=-4/3,\qquad c_2=2/3.}
\tag{L-105438.12}

Therefore `mathcal Q_r` is the unique minimal affine-free normalized residue
microscope on the first two integer heights.

## 6. Boundary Taylor cancellation

At a regular real point, `m` has real Taylor coefficients and

\[
\Im m(a+iy)
=ym'(a)-{y^3\over6}m'''(a)+O(y^5).
\]

The linear term cancels, giving

\[
\boxed{
\mathcal Q_r(a,h)
=-{2\over3}h^3m_r'''(a)+O(h^5).
}
\tag{L-105438.13
}

For a Pick ratio, `m'''(a)>=0`, consistently giving the desired sign.

## 7. Equivalence

Require that both sampled ratios be holomorphic for every `a,h>0`. This
excludes every nonreal zero of `F'`. On that stratum,

\[
\boxed{
\mathcal Q_r(a,h)\le0\text{ for all }a,h
\Longleftrightarrow
\rho_c\le0\text{ for all }c
\Longleftrightarrow
F\text{ is real-rooted}.}
\tag{L-105438.14}

The reverse direction uses (L-105438.7); the forward direction uses
(L-105438.8) and `L-105432`.

## 8. Scope

The theorem does not prove two-height negativity for Xi. It replaces the
three-height frontier by a unique minimal scalar field with a simpler kernel
and scale evolution.
