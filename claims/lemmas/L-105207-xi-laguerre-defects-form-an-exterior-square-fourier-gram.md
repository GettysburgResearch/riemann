# L-105207 — Xi Laguerre defects form an all-order exterior-square Fourier Gram kernel

Claim ID: `L-105207`  
Status: **PROVED UNCONDITIONALLY**  
Created: 2026-08-23  
Audited: 2026-08-23  
Depends on: the classical positive Fourier kernel of Xi  
RH status: **not assumed**

This theorem acts at every fixed low derivative order.  No high-derivative
limit, zero-density theorem, or RH input is used.

## 1. The complete Laguerre-defect ladder

Write the classical Fourier representation in two-sided form

\[
\Xi(t)=\int_{\mathbb R}\varphi(u)e^{itu}\,du,
\qquad
\varphi(u)=\Phi(|u|)>0.
\tag{L-105207.1}
\]

Put

\[
F_m(t)=\Xi^{(m)}(t)
=\int_{\mathbb R}(iu)^m\varphi(u)e^{itu}\,du
\tag{L-105207.2}
\]

and define the real Laguerre defect

\[
\boxed{
\Lambda_m(t)
=F_{m+1}(t)^2-F_m(t)F_{m+2}(t).
}
\tag{L-105207.3}
\]

Its sign is exactly the real Hermite--Biehler phase-velocity sign of
`L-104512`.

## 2. Exterior-square Gram representation

Let

\[
\mathcal H=L^2(\mathbb R,\varphi(u)du)
\]

with inner product linear in the first argument, and, for an integer `a>=0`
and real `t`, define

\[
v_{a,t}(u)=u^a e^{-itu}.
\]

In the exterior square `wedge^2 H`, put

\[
\omega_{a,t}
=(-1)^a v_{a,t}\wedge v_{a+1,t}.
\tag{L-105207.4}
\]

A direct two-by-two determinant calculation gives

\[
\boxed{
\langle\omega_{a,t},\omega_{b,s}\rangle
=\Lambda_{a+b}(s-t).
}
\tag{L-105207.5}
\]

Indeed,

\[
\langle v_{a,t},v_{b,s}\rangle
=i^{-(a+b)}F_{a+b}(s-t),
\]

and the exterior-product determinant is

\[
(-1)^{a+b}
\left[F_{a+b+1}^2-F_{a+b}F_{a+b+2}\right],
\]

with the prefactors in (L-105207.4) cancelling the displayed sign.

Consequently, for every finite collection `(a_j,t_j)`,

\[
\boxed{
\left[
\Lambda_{a_i+a_j}(t_j-t_i)
\right]_{i,j}
\succeq0.
}
\tag{L-105207.6}
\]

This is an all-order, all-translation positive-semidefinite kernel on

\[
\mathbb Z_{\ge0}\times\mathbb R.
\]

It is the second compound of the positive Xi Fourier Gram.

## 3. Pointwise Schur consequences

Every two-by-two principal minor of (L-105207.6) gives

\[
\boxed{
|\Lambda_{a+b}(t-s)|^2
\le
\Lambda_{2a}(0)\Lambda_{2b}(0).
}
\tag{L-105207.7}

More generally, for arbitrary compactly supported test functions `g_a`,

\[
\boxed{
\sum_{a,b}
\int_{\mathbb R}\int_{\mathbb R}
 g_a(t)\overline{g_b(s)}
 \Lambda_{a+b}(s-t)\,dt\,ds
\ge0.
}
\tag{L-105207.8}

Taking all `g_a` to be scalar multiples of one function proves that every
autocorrelation-windowed Hankel matrix

\[
\left[
\int (\psi*\widetilde\psi)(x)
\Lambda_{a+b}(x)\,dx
\right]_{a,b}
\]

is positive semidefinite.  In particular, the triangular/Fejer window gives

\[
\boxed{
\left[
\int_{-T}^{T}(T-|x|)\Lambda_{a+b}(x)\,dx
\right]_{a,b}
\succeq0
\qquad(T>0).
}
\tag{L-105207.9}

Thus every derivative order participates in one unconditional averaged
Laguerre/Pick hierarchy.

## 4. Fourier-side moment hierarchy

With the convention

\[
\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-it\xi}\,dt,
\]

direct convolution gives

\[
\boxed{
\widehat\Lambda_m(\xi)
=
\pi(-1)^m
\int_{\mathbb R}
(2u-\xi)^2
[u(\xi-u)]^m
\varphi(u)\varphi(\xi-u)\,du.
}
\tag{L-105207.10}
\]

For fixed `xi`, define the real coordinate

\[
X_\xi(u)=-u(\xi-u)
\]

and the positive measure

\[
d\mu_\xi(u)
=
\pi(2u-\xi)^2
\varphi(u)\varphi(\xi-u)\,du.
\]

Then

\[
\widehat\Lambda_m(\xi)
=\int X_\xi(u)^m\,d\mu_\xi(u).
\]

Hence every Fourier-side Hankel matrix

\[
\boxed{
\left[
\widehat\Lambda_{a+b}(\xi)
\right]_{a,b=0}^{N}
\succeq0.
}
\tag{L-105207.11}

The diagonal terms satisfy

\[
\widehat\Lambda_{2a}(\xi)\ge0,
\]

and the first nontrivial Schur inequality is

\[
\boxed{
|\widehat\Lambda_{2a+1}(\xi)|^2
\le
\widehat\Lambda_{2a}(\xi)
\widehat\Lambda_{2a+2}(\xi).
}
\tag{L-105207.12}

This controls every odd derivative defect by its two adjacent even defects
before physical localization.

## 5. Explicit unconditional central sign region

Let

\[
M_j=\int_0^\infty u^j\Phi(u)\,du.
\]

For an even derivative index `m=2a`, parity gives

\[
\Lambda_m(0)=4M_mM_{m+2}>0.
\tag{L-105207.13}
\]

Since `Lambda_m` is positive definite as a function of `t`, its normalized
spectral measure has second moment

\[
\boxed{
\Delta_m
=-{\Lambda_m''(0)\over\Lambda_m(0)}
={M_{m+4}\over M_{m+2}}
-{M_{m+2}\over M_m}
>0.
}
\tag{L-105207.14}

Using `cos x >= 1-x^2/2` in the Bochner representation,

\[
\boxed{
\Lambda_m(t)
\ge
\Lambda_m(0)
\left(1-{\Delta_m t^2\over2}\right).
}
\tag{L-105207.15}

Therefore

\[
\boxed{
|t|<\sqrt{2/\Delta_m}
\quad\Longrightarrow\quad
\Lambda_m(t)>0.
}
\tag{L-105207.16}

At a zero of `F_(m+1)`, a wrong extremum would have `Lambda_m<0`.
Consequently every even Xi derivative has an explicit unconditional central
interval containing no wrong extremum.

## 6. Scope

The theorem proves complete source-level and averaged positivity at **all low
orders**.  It does not prove

\[
\Lambda_m(t)\ge0
\]

at every individual height.  Translating a positive Fourier average to one
fixed ordinate introduces the oscillatory phase which is precisely the
Levinson localization problem.  Thus (L-105207.6) is genuine unconditional
low-order structure, while the final height-local sign remains open.
