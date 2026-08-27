# L-105435 — A three-height microscope is equivalent to the complete Xi critical sign

Claim ID: `L-105435`  
Status: **PROVED EXACT EQUIVALENCE CONDITIONAL ON THE CRITICAL-POINT REALITY STRATUM**  
Created: 2026-08-24  
Depends on: `L-105220`, `L-105432--L-105434`  
RH status: **not assumed**

## 1. The scalar three-height field

Fix one Xi derivative

\[
F=\Xi^{(r)},
\qquad
m(z)={F(z)\over F'(z)}.
\]

For real `a` and `h>0`, define

\[
\boxed{
\mathcal P_r(a,h)
=-{3\over2}\operatorname{Im}m(a+ih)
+{6\over5}\operatorname{Im}m(a+2ih)
-{3\over10}\operatorname{Im}m(a+3ih).
}
\tag{L-105435.1}

The coefficients are the value-only multipole coefficients of `L-105220`.

## 2. Exact positive localizer

Put

\[
\boxed{
\Omega_{a,h}(x)
={36h^5\over
((x-a)^2+h^2)
((x-a)^2+4h^2)
((x-a)^2+9h^2)}.
}
\tag{L-105435.2}

Then

\[
\Omega_{a,h}(x)>0
\]

and

\[
\boxed{
\Omega_{a,h}(x)
={3h/2\over(x-a)^2+h^2}
-{12h/5\over(x-a)^2+4h^2}
+{9h/10\over(x-a)^2+9h^2}.
}
\tag{L-105435.3}

It is the approximate identity

\[
\Omega_{a,h}(x)
={1\over h}\Omega_{0,1}\!\left({x-a\over h}\right),
\qquad
\int_{\mathbb R}\Omega_{a,h}(x)\,dx={3\pi\over5}.
\tag{L-105435.4}

At its center,

\[
\boxed{
\Omega_{a,h}(a)={1\over h}.}
\tag{L-105435.5}

With the Fourier convention `hat f(xi)=integral exp(-ix xi)f(x)dx`,

\[
\boxed{
\widehat\Omega_{0,h}(\xi)
=\pi\left[
{3\over2}e^{-h|\xi|}
-{6\over5}e^{-2h|\xi|}
+{3\over10}e^{-3h|\xi|}
\right]
={3\pi\over10}t(t^2-4t+5)>0,
}
\tag{L-105435.6}

where `t=e^(-h|xi|)`. Thus the microscope kernel is both pointwise positive
and positive definite.

## 3. Recovery of one residue

Let `c` be a simple noncommon real critical point and

\[
\rho_c={F(c)\over F''(c)}.
\]

Locally,

\[
m(c+ijh)={\rho_c\over ijh}+O(1)
=-i{\rho_c\over jh}+O(1).
\]

Substitution in (L-105435.1) gives

\[
\begin{aligned}
h\mathcal P_r(c,h)
&=\rho_c\left(
{3\over2}-{3\over5}+{1\over10}
\right)+o(1)\\
&=\rho_c+o(1).
\end{aligned}
\]

Therefore

\[
\boxed{
\lim_{h\downarrow0}h\mathcal P_r(c,h)=\rho_c.}
\tag{L-105435.7}

Every individual residue is a literal fine-scale limit of one scalar
three-height phase field.

## 4. The signed-measure form under the critical sign

Assume every critical point is real and every residue is nonpositive. By
`L-105432--L-105433`, `m` has its complete symmetric critical-pole expansion,
with the even central atom included exactly once and with no affine endpoint
term after parity regularization. Applying (L-105435.3) term by term gives

\[
\boxed{
\mathcal P_r(a,h)
=
\sum_{F'(c)=0}\rho_c\Omega_{a,h}(c)
\le0.
}
\tag{L-105435.8}

The paired series is locally uniform and the sixth-order decay makes the
localized sum absolutely convergent.

## 5. Exact equivalence

On the simple real-critical stratum, the following are equivalent:

1. `rho_c<=0` at every critical point;
2. `mathcal P_r(a,h)<=0` for every real `a` and every `h>0`;
3. `F/F'` is Pick;
4. `F` is real-rooted.

Indeed, `1 -> 2` is (L-105435.8), `2 -> 1` follows from (L-105435.7), and the
remaining equivalences are `L-105432--L-105434`.

Thus the complete critical Vandermonde hierarchy may be replaced by the scalar
two-parameter inequality

\[
\boxed{
\mathcal P_r(a,h)\le0
\qquad(a\in\mathbb R,\ h>0).
}
\tag{L-105435.9}

## 6. Oriented shifted-zero interpretation

Since

\[
\left.\partial_\alpha
\arg {F'-\alpha F\over F'+\alpha F}
\right|_{0}
=-2\operatorname{Im}{F\over F'},
\]

`mathcal P_r` is one fixed three-height combination of infinitesimal oriented
shifted-zero phase velocities. It uses no determinant and no separately
selected critical point.

## 7. Scope

The theorem does not prove the scalar inequality. Its value is to convert an
all-critical-point sign condition into one smooth field with a physical scale
parameter. The multiple/common-zero case requires the corresponding confluent
fine-scale limit.
