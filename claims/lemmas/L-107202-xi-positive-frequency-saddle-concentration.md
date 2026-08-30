# L-107202 — The positive-frequency Xi derivative measure has its natural Gaussian saddle

Claim ID: `L-107202`  
Status: **PROVED ANALYTICALLY FROM THE EXPLICIT STANDARD XI KERNEL; INDEPENDENT CONSTANT REVIEW REQUESTED**  
Created: 2026-08-30  
Depends on: `L-107102`; the literal Xi-kernel bounds in PR #765 at
`a30276a5be049749ebb2147f30f000dd5659298b`  
RH status: **not assumed**

Use the standard full-line normalization

\[
\Xi(t)=\int_{\mathbb R}\Phi_\Xi(u)e^{itu}\,du,
\qquad
\Phi_\Xi(-u)=\Phi_\Xi(u)>0.
\]

The source-locked first-theta-orbit estimate from PR #765 gives absolute
constants \(0<c_1<c_2<\infty\) such that, for \(u\ge0\),

\[
c_1 e^{9u/2-\pi e^{2u}}
\le
\Phi_\Xi(u)
\le
c_2 e^{9u/2-\pi e^{2u}}.
\tag{L-107202.1}
\]

It also gives a superexponentially small relative error as \(u\to\infty\).
Only the two-sided bound is required for concentration.

For an integer \(m\ge1\), define the probability measure

\[
d\nu_m(u)
=
\frac{u^m\Phi_\Xi(u)\,du}
     {\int_0^\infty u^m\Phi_\Xi(u)\,du},
\qquad u>0.
\tag{L-107202.2}
\]

Put

\[
S_m(u)=m\log u+\frac92u-\pi e^{2u}.
\tag{L-107202.3}
\]

## 1. Unique saddle and exact width identity

The derivative

\[
S_m'(u)=\frac m u+\frac92-2\pi e^{2u}
\]

is strictly decreasing after its unique positive zero \(w_m\), and
\(S_m''<0\) everywhere.  Thus \(w_m\) is the unique saddle and satisfies

\[
\boxed{
2\pi e^{2w_m}=\frac m{w_m}+\frac92.
}
\tag{L-107202.4}
\]

For all sufficiently large \(m\),

\[
\boxed{
\frac13\log m<w_m<\frac12\log m.
}
\tag{L-107202.5}
\]

Indeed, at \(u=(\log m)/3\), the term \(m/u\) dominates
\(2\pi m^{2/3}\); at \(u=(\log m)/2\), the term \(2\pi m\) dominates
\(m/u+9/2\).

Define

\[
a_m=(-S_m''(w_m))^{-1/2}.
\tag{L-107202.6}
\]

Using (L-107202.4),

\[
\boxed{
a_m^{-2}
=
\frac m{w_m^2}
+\frac{2m}{w_m}
+9.
}
\tag{L-107202.7}
\]

Hence, for all sufficiently large \(m\),

\[
\boxed{
\frac{w_m}{4m}
\le a_m^2\le
\frac{w_m}{2m}.
}
\tag{L-107202.8}
\]

In particular,

\[
w_m
=
\frac12\log\frac m{\log m}+O(1),
\qquad
a_m\asymp\sqrt{\frac{\log m}{m}}.
\tag{L-107202.9}
\]

The displayed saddle asymptotic follows by taking logarithms in
(L-107202.4) and using (L-107202.5).

## 2. Uniform Gaussian concentration

There are absolute constants \(C,c>0\) such that, for all sufficiently large
\(m\) and every \(A\ge1\),

\[
\boxed{
\nu_m\{|u-w_m|>A a_m\}
\le
C e^{-cA^2}.
}
\tag{L-107202.10}
\]

More generally, for every fixed \(H\ge0\) and \(j=0,1,2\),

\[
\boxed{
\int_{|u-w_m|>Aa_m}
\left(1+\frac{u^2}{w_m^2}\right)
|u-w_m|^j e^{H|u-w_m|}\,d\nu_m(u)
\le C_{H,j}e^{-cA^2}.
}
\tag{L-107202.11}
\]

### Proof

On \(|u-w_m|\le1\), equation (L-107202.4) and
\(e^{2u}\ge e^{-2}e^{2w_m}\) give

\[
-S_m''(u)
=
\frac m{u^2}+4\pi e^{2u}
\ge c_0\frac m{w_m}.
\]

Taylor's theorem therefore gives

\[
S_m(u)-S_m(w_m)
\le
-c_1\frac m{w_m}(u-w_m)^2
\le
-c_2\frac{(u-w_m)^2}{a_m^2}.
\tag{L-107202.12}
\]

At \(u=w_m\pm1\), the drop is \(\gg m/w_m\).  Strict concavity then
continues the estimate outside this unit neighbourhood with a linear tail
whose initial slope is \(\gg m/w_m\).  Near zero, the factor \(u^m\)
gives a still stronger bound.

The upper estimate in (L-107202.1) bounds the numerator by a constant
multiple of the integral of \(e^{S_m}\).  The lower estimate, integrated on
\(|u-w_m|\le a_m\), bounds the normalization from below by a constant
multiple of \(a_m e^{S_m(w_m)}\).  Rescaling
\(u-w_m=a_m x\) in the local region and using the linear exterior tails
proves (L-107202.10).  Polynomial and fixed exponential weights are absorbed
by decreasing \(c\), proving (L-107202.11).

No unbalanced \(u<0\) region occurs because (L-107202.2) is the positive
frequency measure.  Evenness supplies the reflected half of \(\Xi\).

## 3. Derivative companions

For \(m\ge0\),

\[
\Xi^{(m)}(z)
=
2M_m
\int_0^\infty
\cos\!\left(uz+\frac{m\pi}{2}\right)d\nu_m(u),
\qquad
M_m=\int_0^\infty u^m\Phi_\Xi(u)\,du.
\tag{L-107202.13}
\]

Up to an irrelevant sign, the phase is one of the cosine/sine phases in
`L-107102`.

Choose an absolute \(A_*\) sufficiently large that the weighted tail in
(L-107202.11) lies below the margins in `L-107102`, and put

\[
\delta_m=A_*a_m.
\tag{L-107202.14}
\]

Then the truncated measure lies in
\([w_m-\delta_m,w_m+\delta_m]\), its relative width is \(o(1)\), and the
discarded tail is admissible.

Consequently there are absolute \(c_*,m_0>0\) such that, for \(m\ge m_0\),

\[
\boxed{
\Xi^{(m)}
\text{ has only simple real zeros in }
|\Re z|\le c_*\sqrt{\frac m{\log m}},
\quad
|\Im z|\le\frac12.
}
\tag{L-107202.15}
\]

The same region has a strict Laguerre reserve for the normalized derivative
companion.  This proves the analytic input named `XISADDLE107110`.

## Scope and normalization

The theorem concerns derivative order growing with the observed height.  It
does not transport the resulting real-rooted packet down to fixed order.
The scalar factor-of-two correction to the historical Xi kernel cancels in
\(\nu_m\) and changes none of the normalized conclusions.
