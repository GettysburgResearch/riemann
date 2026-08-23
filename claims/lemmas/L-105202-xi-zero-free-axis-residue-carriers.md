# L-105202 — The Xi Poisson boundary carriers have asymptotic coherence one on the zero-free real axis

Claim ID: `L-105202`  
Status: **PROVED EXACT BOUNDARY DICTIONARY + FIXED-ORDER ASYMPTOTIC**  
Created: 2026-08-23  
Depends on: `L-105200`; the standard definition and functional equation of xi  
RH status: **not assumed**

Use

\[
\Xi(z)=\xi\!\left(\frac12+iz\right),
\qquad
F_k(z)=\Xi^{(k)}(z).
\]

Fix an integer `k>=1`. For `T>1/2`, put

\[
\sigma=T+\frac12
\]

and, whenever the denominators are nonzero, define

\[
U_k(T)=\frac{\xi^{(k+1)}(\sigma)}{\xi^{(k)}(\sigma)},
\tag{L-105202.1}
\]

\[
S_k(T)=\frac{\xi^{(k-1)}(\sigma)}{\xi^{(k)}(\sigma)},
\tag{L-105202.2}
\]

\[
R_k(T)=
\frac{\xi^{(k-1)}(\sigma)^2}
{\xi^{(k)}(\sigma)\xi^{(k+1)}(\sigma)}.
\tag{L-105202.3}
\]

Let

\[
\boxed{
\mathscr D_T f
=T^3f''(T)-3T^2f'(T)+3Tf(T).
}
\tag{L-105202.4}
\]

## 1. Exact functional-equation dictionary

The functional equation gives

\[
\xi^{(j)}\!\left(\frac12-T\right)
=(-1)^j\xi^{(j)}\!\left(\frac12+T\right).
\]

Since differentiation in `z` contributes a factor `i`,

\[
F_j(iT)=(-i)^j\xi^{(j)}(\sigma).
\tag{L-105202.5}
\]

Consequently

\[
\frac{F_{k+1}}{F_k}(iT)=-iU_k(T),
\tag{L-105202.6}
\]

\[
\frac{F_{k-1}}{F_k}(iT)=iS_k(T),
\tag{L-105202.7}
\]

and

\[
\frac{F_{k-1}^2}{F_kF_{k+1}}(iT)=-iR_k(T).
\tag{L-105202.8}
\]

Differentiate these identities along the imaginary axis and insert them into
the boundary functional of `L-105200`. One obtains the exact formulas

\[
\boxed{
\mathfrak B_{0,T}\!\left[\frac{F_{k+1}}{F_k}\right]
=\frac18\mathscr D_TU_k,
}
\tag{L-105202.9}
\]

\[
\boxed{
-\mathfrak B_{0,T}\!\left[\frac{F_{k-1}}{F_k}\right]
=\frac18\mathscr D_TS_k,
}
\tag{L-105202.10}
\]

and

\[
\boxed{
\mathfrak B_{0,T}\!\left[
\frac{F_{k-1}^2}{F_kF_{k+1}}
\right]
=\frac18\mathscr D_TR_k.
}
\tag{L-105202.11}
\]

Thus the natural localized count, first-moment carrier and uncorrected
second-moment carrier all live on the zero-free real axis `sigma=T+1/2`.

## 2. Fixed-order derivative asymptotics

Put

\[
\Lambda(T)=\frac{\xi'(\sigma)}{\xi(\sigma)}.
\]

Stirling's formula and absolute convergence of the zeta Euler product on the
right half-plane give

\[
\boxed{
\Lambda(T)
=\frac12\log\frac{T}{2\pi}+O(T^{-1}),
}
\tag{L-105202.12}
\]

\[
T\Lambda'(T)=\frac12+O(T^{-1}),
\qquad
T^j\Lambda^{(j)}(T)=O_j(1)\quad(j>=2).
\tag{L-105202.13}
\]

For each fixed derivative order, the complete Bell-polynomial formula for
`xi^(j)/xi` implies

\[
\frac{\xi^{(j)}(\sigma)}{\xi(\sigma)}
=\Lambda(T)^j
\left(1+O_j\!\left(\frac1{T\Lambda(T)^2}\right)\right),
\tag{L-105202.14}
\]

and the same estimate may be differentiated twice. In particular,

\[
U_k(T)=\Lambda(T)
\left(1+O_k\!\left(\frac1{T\Lambda(T)^2}\right)\right),
\tag{L-105202.15}
\]

\[
S_k(T)=\Lambda(T)^{-1}
\left(1+O_k\!\left(\frac1{T\Lambda(T)^2}\right)\right),
\tag{L-105202.16}
\]

and

\[
R_k(T)=\Lambda(T)^{-3}
\left(1+O_k\!\left(\frac1{T\Lambda(T)^2}\right)\right).
\tag{L-105202.17}
\]

These formulas also prove that all denominators above are nonzero for
sufficiently large `T`.

## 3. Boundary main terms

Applying `mathscr D_T` and using (L-105202.13),

\[
\boxed{
\mathscr D_TU_k
=3T\Lambda(T)
\left(1+O_k(\Lambda(T)^{-1})\right),
}
\tag{L-105202.18}
\]

\[
\boxed{
\mathscr D_TS_k
=\frac{3T}{\Lambda(T)}
\left(1+O_k(\Lambda(T)^{-1})\right),
}
\tag{L-105202.19}
\]

and

\[
\boxed{
\mathscr D_TR_k
=\frac{3T}{\Lambda(T)^3}
\left(1+O_k(\Lambda(T)^{-1})\right).
}
\tag{L-105202.20}
\]

Hence the three zero-free-axis boundary carriers are eventually positive and
have the scales

\[
\boxed{
\mathcal N_k^{\rm bdry}(T)
:=\frac18\mathscr D_TU_k
=\frac{3T\Lambda(T)}8(1+o(1)),
}
\tag{L-105202.21}
\]

\[
\boxed{
\mathcal M_{1,k}^{\rm bdry}(T)
:=\frac18\mathscr D_TS_k
=\frac{3T}{8\Lambda(T)}(1+o(1)),
}
\tag{L-105202.22}
\]

\[
\boxed{
\mathcal M_{2,k}^{\rm bdry}(T)
:=\frac18\mathscr D_TR_k
=\frac{3T}{8\Lambda(T)^3}(1+o(1)).
}
\tag{L-105202.23}
\]

Their normalized coherence is asymptotically one:

\[
\boxed{
\frac{
(\mathcal M_{1,k}^{\rm bdry}(T))^2
}{
\mathcal N_k^{\rm bdry}(T)
\mathcal M_{2,k}^{\rm bdry}(T)
}
=1+O_k(\Lambda(T)^{-1}).
}
\tag{L-105202.24}
\]

The constant in `mathcal N_k^bdry` is the natural one: the localizer has

\[
\int_{-\infty}^{\infty}
\left(\frac{T^2}{x^2+T^2}\right)^3dx
=\frac{3\pi T}{8},
\]

while the leading zero density is `Lambda(T)/pi`.

## 4. Meaning and boundary

Equation (L-105202.24) proves that the zero-free-axis main terms already have
the precise size and ratio required by residue coherence. Therefore no missing
constant in the gamma factor blocks the Xi reverse–Rolle programme.

To identify these carriers with the real-critical moments, one must still:

1. pass the finite localizer identities through canonical-product exhaustion;
2. construct and control the entire Bézout interpolant replacing `A_p`;
3. bound the nonreal-critical correction;
4. compare the resulting localized count with the real critical-point count.

Those are arithmetic/entire interpolation problems, not main-term evaluation.
No RH conclusion is claimed here.
