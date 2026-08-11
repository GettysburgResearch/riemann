# L-91016 — The dyadic Cauchy all-pass has one hyperbolic singular pair and an exact Lyapunov depth projector

Claim ID: `L-91016`  
Status: **PROPOSED COMPLETE EXACT SCATTERING/SIGNATURE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91013` (the three-state `SO(3)` Cauchy all-pass completion)  
RH status: **unproved**

## 1. Fixed-axis Cayley transfer

Let

\[
 \mathbf n=(\sqrt{5/8},0,\sqrt{3/8})^T
\]

and let `K` be the real skew matrix `Kv=n cross v`.  Put

\[
 \mathcal R(v)=(I+vK)(I-vK)^{-1}.
 \tag{L-91016.1}
\]

For real `v`, this is the rotation through angle `2 arctan(v)` about the fixed
axis `n`.  Its first column is

\[
 \boxed{
 \mathcal R(v)e_1
 =\frac1{4(1+v^2)}
 \begin{pmatrix}
 4+v^2\\
 2\sqrt6\,v\\
 \sqrt{15}\,v^2
 \end{pmatrix}.
 }
 \tag{L-91016.2}
\]

Consequently, with

\[
 h_a(u)=\frac{a^2}{a^2+u^2},
 \qquad
 h_{2a}(u)=\frac{4a^2}{4a^2+u^2},
\]

and the two detail channels of `L-91013`,

\[
 \begin{pmatrix}h_a(u)\\g_{1,a}(u)\\g_{2,a}(u)\end{pmatrix}
 =h_{2a}(u)\mathcal R(u/a)e_1.
 \tag{L-91016.3}
\]

## 2. Constant diagonalisation

The matrix `K` is normal, with eigenvalues `0,+i,-i`.  A constant unitary
matrix `U`, independent of `v`, gives

\[
 \boxed{
 U^*\mathcal R(v)U
 =\operatorname{diag}
 \left(1,b(v),b(v)^{-1}\right),
 \qquad
 b(v)=\frac{1+iv}{1-iv}.
 }
 \tag{L-91016.4}
\]

Thus the real three-state bank is the spin-one/adjoint representation of one
scalar first-order all-pass factor.

## 3. Complex zero coordinate

For a centred zero coordinate

\[
 z=d+ir,
 \qquad d\ge0,
\]

put

\[
 v=-iz/a.
\]

Then

\[
 \boxed{
 b(v)=\frac{a+z}{a-z}.
 }
 \tag{L-91016.5}
\]

On the critical line `d=0`, `|b|=1` and `R(v)` is unitary.  For a right-side
off-line coordinate `d>0`, define

\[
 \beta_a(d,r)
 =\left|\frac{a+d+ir}{a-d-ir}\right|
 =\sqrt{\frac{(a+d)^2+r^2}{(a-d)^2+r^2}}>1.
 \tag{L-91016.6}
\]

The singular values are exactly

\[
 \boxed{\beta_a(d,r),\ 1,\ \beta_a(d,r)^{-1}.}
 \tag{L-91016.7}
\]

Hence

\[
 \mathcal R(v)^*\mathcal R(v)-I
\]

has one positive, one negative and one zero eigenvalue.  Every off-line pair is
one hyperbolic scattering block of signature `(1,1)`; every critical-line atom
is lossless.

Although Hermitian unitarity fails off the line, complex orthogonality remains
exact:

\[
 \boxed{
 \mathcal R(v)^T\mathcal R(v)=I,
 \qquad \det\mathcal R(v)=1.
 }
 \tag{L-91016.8}
\]

## 4. Exact trace excess

The nonunitarity trace is

\[
\begin{aligned}
 \operatorname{tr}(\mathcal R^*\mathcal R)-3
 &=\beta_a^2+\beta_a^{-2}-2\\
 &=\boxed{
 \frac{16a^2d^2}
 {[(a-d)^2+r^2][(a+d)^2+r^2]}.
 }
\end{aligned}
 \tag{L-91016.9}
\]

It is strictly positive precisely off the critical line.  At the matching
ordinate `r=0`, the expanding gain is

\[
 \beta_a(d,0)=\frac{a+d}{|a-d|},
 \tag{L-91016.10}
\]

and blows up as the radial scale approaches the zero depth.

## 5. Lyapunov depth projector

Define the positive logarithmic singular gain

\[
 \ell_a(d,r)=\log\beta_a(d,r)
 =\frac12\log
 \frac{r^2+(a+d)^2}{r^2+(a-d)^2}.
 \tag{L-91016.11}
\]

The standard logarithmic integral gives the exact identity

\[
 \boxed{
 \int_{\mathbb R}\ell_a(d,r)\,dr
 =2\pi\min(a,d).
 }
 \tag{L-91016.12}
\]

Therefore, distributionally in `a`,

\[
 \boxed{
 \frac1{2\pi}\frac{d}{da}
 \int_{\mathbb R}\ell_a(d,r)\,dr
 =\mathbf1_{\{a<d\}},
 }
 \tag{L-91016.13}
\]

and

\[
 \boxed{
 -\frac1{2\pi}\frac{d^2}{da^2}
 \int_{\mathbb R}\ell_a(d,r)\,dr
 =\delta(a-d).
 }
 \tag{L-91016.14}
\]

Thus the all-pass Lyapunov exponent is an exact cumulative projector onto
horizontal zero depth.  This is the multiplicative/scattering counterpart of
the radial-curvature depth projector on PR #394.

## 6. Finite-packet consequence

For a finite reflected zero packet `Z`, sum `ell_a` over one representative of
each right-side pair, with multiplicity.  Then

\[
 \frac1{2\pi}\partial_a
 \int_{\mathbb R}\sum_{\rho\in Z_+}m_\rho
 \ell_a(\Re\rho-1/2,\Im\rho-x)\,dx
\]

is exactly the number of right-side packet zeros deeper than `a`.  In
particular, the complete three-state transfer is unitary for every carrier and
scale if and only if the packet lies on the critical line.

## 7. Multiscale composition

All matrices `R(v)` are functions of the same fixed generator `K` and hence
commute.  Their scalar eigenchannels multiply:

\[
 \prod_j\mathcal R(-iz/a_j)
 =U\,\operatorname{diag}
 \left(1,\prod_j\frac{a_j+z}{a_j-z},
          \prod_j\frac{a_j-z}{a_j+z}\right)U^*.
 \tag{L-91016.15}
\]

The positive logarithmic gains therefore add exactly across scales.  No hidden
state dimension grows in the internal scattering channel; only the emitted
detail ports accumulate.

## 8. Boundary

Closed here:

```text
three-state bank = fixed-axis Cayley rotation;
constant diagonalisation to one scalar all-pass pair;
one off-line pair = one expanding/contracting singular pair;
exact trace excess;
exact Lyapunov depth projector;
commuting all-generation cascade.
```

Open:

```text
prime-side control of the emitted detail ports;
critical-boundary source/scattering intertwining;
vanishing of every hyperbolic block;
RH.
```
