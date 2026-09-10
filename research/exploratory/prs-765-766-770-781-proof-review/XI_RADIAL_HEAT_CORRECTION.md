# 3. Primary Target F — first nonuniversal Xi heat correction

Use the literal source notation from #765:

\[
E=e^\xi,\qquad
\varepsilon=(\pi E)^{-1/2},\qquad
h=E^{-1},
\]

and

\[
R_\xi(u)=\frac{H_\xi(\varepsilon u)}{H_\xi(0)}.
\]

For \(|d|\le1\), the source proof gives

\[
R_\xi(u)
=
\exp[-2\pi E(\cosh d-1)]\,
B_\xi(d),\qquad d=\varepsilon u,
\tag{F.1}
\]

where

\[
B_\xi(d)=
\frac{\theta_*(Ee^d)\theta_*(Ee^{-d})}
     {\theta_*(E)^2},
\qquad
\theta_*(X)=1-\frac{3}{2\pi X}+r(X),
\]

and \(0\le r(X)\le(512/31)e^{-3\pi X}\).

The global source bound is \(0<R_\xi(u)\le9e^{-u^2}\).

## 3.1 Source expansion

### Theorem F1

For every fixed \(m\ge0\) and \(T\ge0\),

\[
R_\xi(u)
=
e^{-u^2}
\left[
1+h\,r_1(u)+h^2r_2(u)
\right]
+O_{m,T}(h^3)
\tag{F.2}
\]

in the weighted norm

\[
\int_\mathbb R(1+|u|^m)e^{T|u|}
|\cdot|\,du,
\]

where

\[
\boxed{r_1(u)=-\frac{u^4}{12\pi}}
\tag{F.3}
\]

and

\[
\boxed{
r_2(u)=
\frac{u^8}{288\pi^2}
-\frac{u^6}{360\pi^2}
-\frac{3u^2}{2\pi^2}.
}
\tag{F.4}
\]

The last term in (F.4) is the first contribution from the
\(-3/(2\pi X)\) theta coefficient. It first appears at order \(E^{-2}\).

### Proof

Taylor expansion gives

\[
2\pi E(\cosh(\varepsilon u)-1)
=
u^2+\frac{h\,u^4}{12\pi}
+\frac{h^2u^6}{360\pi^2}
+O(h^3u^8).
\]

Therefore

\[
e^{-2\pi E(\cosh(\varepsilon u)-1)}
=
e^{-u^2}
\left[
1-\frac{hu^4}{12\pi}
+h^2\left(
\frac{u^8}{288\pi^2}
-\frac{u^6}{360\pi^2}
\right)
\right]
+O(h^3e^{-u^2/2}P(u)).
\tag{F.5}
\]

Put \(a=3/(2\pi)\). Ignoring the exponentially small \(r(X)\), which
is smaller than every power of \(h\),

\[
B_\xi(d)
=
\frac{1-2ah\cosh d+a^2h^2}
     {(1-ah)^2}.
\]

Since \(d^2=hu^2/\pi\),

\[
B_\xi(d)
=
1-\frac{3h^2u^2}{2\pi^2}
+O(h^3P(u)).
\tag{F.6}
\]

Multiplying (F.5) and (F.6) gives (F.2)–(F.4). To make the expansion
global, split at \(|u|=h^{-1/12}\). Taylor remainders are polynomially
dominated in the central region; the global \(9e^{-u^2}\) bound makes
the complementary region smaller than every power of \(h\), including
the part where \(|\varepsilon u|>1\). ∎

## 3.2 Comparison kernels

Two comparisons separate the mechanisms.

1. **Pure Gaussian**

   \[
   R_\xi^{\mathrm G}(u)=e^{-u^2}.
   \]

   It has neither \(r_1\) nor \(r_2\).

2. **Cosh-only synthetic source**

   \[
   R_\xi^{\mathrm C}(u)
   =
   e^{-2\pi E(\cosh(\varepsilon u)-1)}.
   \]

   It has the same \(r_1\) and the first two terms of \(r_2\), but not
   the theta-arithmetic term \(-3u^2/(2\pi^2)\).

Thus the \(E^{-1}\) correction distinguishes Xi from a Gaussian source,
while the \(E^{-2}\) quadratic term distinguishes the literal theta
coefficient from a source with the same cosh geometry.

## 3.3 Normalized continuum current

For fixed compact \(\kappa\), let

\[
p_\kappa(u)=
\frac{2}{\sqrt\pi}e^{-\kappa^2/4}
u^2\sinhc(\kappa u)e^{-u^2}.
\]

The committed moment formulas give

\[
\mathbb E_\kappa U^2
=
\frac32+\frac{\kappa^2}{4},
\]

\[
M_4(\kappa):=\mathbb E_\kappa U^4
=
\frac{15}{4}
+\frac{5\kappa^2}{4}
+\frac{\kappa^4}{16}.
\]

After continuum current normalization, Theorem F1 yields

\[
p_{\kappa,\xi}(u)
=
p_\kappa(u)
\left[
1-\frac{h}{12\pi}
\bigl(u^4-M_4(\kappa)\bigr)
\right]
+O(h^2).
\tag{F.7}
\]

The first coefficient-specific theta contribution is

\[
-\frac{3h^2}{2\pi^2}
\left(
u^2-\frac32-\frac{\kappa^2}{4}
\right)p_\kappa(u).
\tag{F.8}
\]

The density correction changes sign: it is positive below the fourth
moment scale and negative above it. It is therefore not pointwise
one-signed.

## 3.4 Monotonicity law

Let \(Q_t(r,du)\) be the Bessel-3/radial heat kernel. In output radius
\(u>0\), the order-\(h\) correction operator is

\[
A_t\varphi(r)
=
-\frac1{12\pi t^2}
\operatorname{Cov}_{Q_t(r,\cdot)}
\bigl(\varphi(U),U^4\bigr).
\tag{F.9}
\]

For every bounded increasing \(\varphi\),

\[
\boxed{A_t\varphi(r)\le0.}
\tag{F.10}
\]

This follows from the elementary covariance identity using two
independent copies:

\[
2\operatorname{Cov}(\varphi(U),U^4)
=
\mathbb E[
(\varphi(U)-\varphi(V))(U^4-V^4)
]\ge0.
\]

The inequality is strict for a nonconstant increasing \(\varphi\).
The first Xi source correction therefore moves mass inward in
first-order stochastic order.

## 3.5 Exact total positivity of the continuum source family

For an arbitrary positive radial source factor \(R\), define the
continuum kernel, up to its row normalization, by

\[
\widetilde q_t(r,u)
\propto
u^2 R(u/\sqrt t)\,
\sinhc(2ru/t),
\qquad r,u>0.
\tag{F.11}
\]

### Theorem F2

The kernel \(\widetilde q_t\) is strictly totally positive of every
finite order on \((0,\infty)^2\).

### Proof

Positive row and column factors do not change signs of minors. It is
therefore enough to treat

\[
S(r,u)=\sinhc(2ru/t)
=
\sum_{n=0}^\infty
\frac{(2/t)^{2n}r^{2n}u^{2n}}{(2n+1)!}.
\tag{F.12}
\]

For strictly increasing positive \(r_i,u_j\), Cauchy–Binet expands an
\(N\times N\) minor into a sum over
\(0\le n_1<\cdots<n_N\) of

\[
\left(\prod_\ell\frac{(2/t)^{2n_\ell}}{(2n_\ell+1)!}\right)
\det[r_i^{2n_\ell}]
\det[u_j^{2n_\ell}].
\]

Every generalized Vandermonde determinant is positive. At least one
term is positive, so the minor is positive. ∎

This is an exact source-universality theorem. Xi, the Gaussian source,
the cosh-only source, and every positive synthetic radial source share
this continuum total positivity. Consequently this particular
total-positivity property cannot distinguish Xi or imply critical-line
purity.

## 3.6 No semigroup cocycle

A first-order correction to a semigroup would have to satisfy

\[
A_{s+t}=A_sQ_t+Q_sA_t.
\tag{F.13}
\]

It does not. Let \(\varphi(u)=u^2\). The radial moments are

\[
Q_tU^2=r^2+\frac{3t}{2},
\]

\[
Q_tU^4=r^4+5tr^2+\frac{15t^2}{4},
\]

\[
Q_tU^6=r^6+\frac{21t}{2}r^4
+\frac{105t^2}{4}r^2+\frac{105t^3}{8}.
\]

Hence

\[
A_t\varphi(r)
=
-\frac1{12\pi}
\left(
\frac{4r^4}{t}+15r^2+\frac{15t}{2}
\right).
\tag{F.14}
\]

At \(r=0\) and \(s=t=1\),

\[
\boxed{
(A_1Q_1+Q_1A_1-A_2)\varphi(0)
=
-\frac{25}{8\pi}\ne0.
}
\tag{F.15}
\]

The first Xi source correction is therefore not a semigroup cocycle.

## 3.7 The larger rounding correction: a no-go theorem

The actual repository kernel uses odd integer order

\[
K_\xi(r)=1+2\left\lfloor\frac r\delta\right\rfloor,
\qquad
\delta=\frac{\varepsilon}{\xi}.
\]

Its current factor is

\[
F_K(\delta u)
=
\frac12\int_{-1}^1(1+t\delta u)^{K-1}\,dt.
\]

Suppose

\[
K\delta=\kappa+\omega\delta+O(\delta^2).
\]

Then, uniformly after multiplication by fixed Gaussian/exponential
weights,

\[
F_K(\delta u)
=
\sinhc(\kappa u)
+\delta\,G_{\kappa,\omega}(u)
+O(\delta^2),
\tag{F.16}
\]

where

\[
\boxed{
G_{\kappa,\omega}(u)
=
(\omega-1)u\,\sinhc'(\kappa u)
-\frac{\kappa u^2}{2}\,\sinhc''(\kappa u).
}
\tag{F.17}
\]

For the exact floor rule at time \(t\), with target
\(\kappa=2r/\sqrt t\),

\[
\omega
=
1-2\left\{\frac{\kappa}{2\delta}\right\}.
\tag{F.18}
\]

The fractional part need not converge, so the normalized
\(O(\delta)\) correction need not have a unique limit. Moreover,

\[
\frac{\delta}{h}
=
\frac{e^{\xi/2}}{\sqrt\pi\,\xi}
\longrightarrow\infty.
\tag{F.19}
\]

Therefore the \(E^{-1}\) Xi source term is not the first correction of
the literal rounded family. It is hidden behind a larger,
source-independent, potentially oscillatory order-discretization term.

A genuine arithmetic correction theorem for the literal \(P_{\xi,t}\)
must first do one of the following:

1. replace the floor rule by a declared continuous-order interpolation;
2. subtract the exact \(F_K\) correction;
3. select and record a rounding subsequence through \(\omega\).

Without one of these, an \(E^{-1}\) semigroup expansion is false as a
uniform statement.

---
