# L-34403 — Positive Q=4-to-compact two-parameter Jordan interpolation and scalar Schur no-go

Claim ID: `L-34403`  
Title: The Q=4 Euler--Blaschke source admits a coefficientwise-positive two-parameter Jordan interpolation to the compact one-step source, but the naive scalar scale-ratio log-Hessian is necessarily indefinite and cannot supply the innovation Schur bound  
Status: **PROPOSED COMPLETE EXACT DIRICHLET/ROW THEOREM + EXACT NO-GO — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #342 `L-34003`; PR #345 `L-34402`; PR #339 `L-33802`  
Scope: exact source interpolation, positive Jordan coefficients, row jets, and scalar-Hessian scope; no innovation-square bound or RH claim

## 1. Linear source interpolation

Put

\[
 x=4^{-s},
 \qquad
 B_4(s)=\frac{1-4^{1-s}}{(1-4^{-s})\zeta(s)},
 \qquad A_4=B_4^{-1}.
\]

For a real parameter

\[
0\le\sigma\le1
\]

define

\[
\boxed{
 B_\sigma(s)=(1-\sigma x)B_4(s),
 \qquad
 A_\sigma(s)=\frac{A_4(s)}{1-\sigma x}.
}
\tag{L-34403.1}
\]

Then

\[
 B_0=B_4,
 \qquad
 B_1=(1-4^{-s})B_4
     =\frac{1-4^{1-s}}{\zeta(s)}
     =B_\circ,
\tag{L-34403.2}
\]

so this is an exact interpolation from the Q=4 Euler--Blaschke source to the compact one-step source of PR #342.

At coefficient level,

\[
\boxed{
 b_\sigma=(\varepsilon-\sigma\delta_4)*b_4.
}
\tag{L-34403.3}
\]

In particular `sigma=1` gives `b_circ`.

## 2. Positive two-parameter Jordan family

For `tau>=0` put

\[
 a=4^\tau\ge1
\]

and define

\[
\boxed{
 J_{\tau,\sigma}(s)
 =\frac{A_\sigma(s-\tau)}{A_\sigma(s)}.
}
\tag{L-34403.4}
\]

Using `x=4^-s`,

\[
\boxed{
 J_{\tau,\sigma}(s)
 =J_{4,\tau}(s)
  \frac{1-\sigma x}{1-\sigma a x},
}
\tag{L-34403.5}
\]

where `J_(4,tau)` is the coefficientwise-positive Q=4 Jordan deformation of PR #339.

The extra local factor has the exact expansion

\[
\boxed{
 \frac{1-\sigma x}{1-\sigma a x}
 =1+\sum_{r\ge1}
   \sigma^r a^{r-1}(a-1)x^r.
}
\tag{L-34403.6}
\]

Every displayed coefficient is nonnegative for `tau>=0` and `sigma>=0`. Since the product of Dirichlet series with nonnegative coefficients again has nonnegative coefficients,

\[
\boxed{
 J_{\tau,\sigma}(n)\ge0
 \qquad(n\ge1,\ tau\ge0,\ 0\le\sigma\le1).
}
\tag{L-34403.7}
\]

Thus the positive Jordan family requested abstractly in PR #345 exists explicitly all the way from the Q=4 source to the compact source.

## 3. First two tau jets

Let

\[
 \Lambda_\sigma=-\frac{A_\sigma'}{A_\sigma},
 \qquad
 C_\sigma=\Lambda_\sigma\log+\Lambda_\sigma*\Lambda_\sigma.
\]

Coefficientwise differentiation of (L-34403.4) at `tau=0` gives

\[
\boxed{
 J_{0,\sigma}=\varepsilon,
 \qquad
 \partial_\tau J_{\tau,\sigma}|_{0}=\Lambda_\sigma,
 \qquad
 \partial_\tau^2J_{\tau,\sigma}|_{0}=C_\sigma.
}
\tag{L-34403.8}
\]

From (L-34403.1), with `L=log 4`,

\[
\boxed{
 \Lambda_\sigma
 =\Lambda_4
  +L\frac{\sigma x}{1-\sigma x}
 =\Lambda_4
  +L\sum_{r\ge1}\sigma^r\delta_{4^r}.
}
\tag{L-34403.9}
\]

At `sigma=1` this is exactly the generalized-prime sequence of the compact inverse `A_circ`.

In particular,

\[
\boxed{
 \partial_\sigma\Lambda_\sigma|_{\sigma=0}
 =L\delta_4.
}
\tag{L-34403.10}
\]

## 4. Source-convolved Jordan family and compact current

Define

\[
\boxed{
 K_{\tau,\sigma}=b_\sigma*J_{\tau,\sigma}.
}
\tag{L-34403.11}
\]

Its Dirichlet multiplier is `B_sigma J_(tau,sigma)`. At `tau=0`,

\[
K_{0,\sigma}=b_\sigma.
\]

Differentiating in `tau` gives the source current

\[
\boxed{
 \partial_\tau K_{\tau,\sigma}|_0
 =b_\sigma*\Lambda_\sigma
 =B_\sigma'
 =:q_\sigma.
}
\tag{L-34403.12}
\]

Using (L-34403.1),

\[
\boxed{
 q_\sigma
 =(\varepsilon-\sigma\delta_4)*q_4
  +\sigma L\delta_4*b_4.
}
\tag{L-34403.13}
\]

Therefore

\[
q_0=q_4,
\qquad
q_1=q_\circ,
\tag{L-34403.14}
\]

and

\[
\boxed{
 \partial_\sigma q_\sigma|_0
 =-\delta_4*q_4+L\delta_4*b_4
 =q_\circ-q_4.
}
\tag{L-34403.15}
\]

PR #345 correctly distinguishes the actual aligned innovation

\[
 i_\circ=(\varepsilon-\delta_4)q_4
 =q_\circ-L\delta_4*b_4.
\tag{L-34403.16}
\]

Thus the source parameter reaches the own compact current exactly, while the actual Q=4 scale innovation differs by the already-declared delayed bare gauge.

## 5. Positive row partition

For a nontrivial carry row `e=(n,j)`, define

\[
\boxed{
 F_e(\tau,\sigma)
 =1+\mathcal L_e(J_{\tau,\sigma}).
}
\tag{L-34403.17}
\]

Every carry coefficient is zero or one, and (L-34403.7) gives

\[
\boxed{F_e(\tau,\sigma)>0}
\tag{L-34403.18}
\]

for the declared real parameter range.

At `tau=0`,

\[
F_e(0,\sigma)=1
\tag{L-34403.19}
\]

for every `sigma`. Its first two `tau` jets are

\[
\boxed{
 \partial_\tau F_e(0,\sigma)=P_\sigma(e),
 \qquad
 \partial_\tau^2F_e(0,\sigma)=S_\sigma(e).
}
\tag{L-34403.20}
\]

Consequently

\[
\boxed{
 -\partial_\tau^2\log F_e(0,\sigma)
 =P_\sigma(e)^2-S_\sigma(e).
}
\tag{L-34403.21}
\]

At `sigma=0` this is the Q=4 Selberg--Kummer reserve.

## 6. Radix-four scale-ratio extension

Let `e^+=(4n,4j)` and extend PR #345's scale ratio by

\[
\boxed{
 H_e(\tau,\sigma)
 ={F_{e^+}(\tau,\sigma)\over F_e(4\tau,\sigma)}.
}
\tag{L-34403.22}
\]

Then

\[
H_e(0,\sigma)=1.
\tag{L-34403.23}
\]

At `(tau,sigma)=(0,0)`, PR #345's identities are recovered:

\[
\boxed{
 \partial_\tau\log H_e(0,0)
 =P_4(e^+)-4P_4(e)=E_e,
}
\tag{L-34403.24}
\]

and

\[
\boxed{
 -\partial_\tau^2\log H_e(0,0)
 =R_4(e^+)-16R_4(e)
 =\Delta_4R(e).
}
\tag{L-34403.25}
\]

So the positive interpolation genuinely extends the exact relative Jordan curvature.

## 7. Exact scalar Schur no-go

The natural hope would be to use the two variables `(tau,sigma)` in the positive scalar partition `H_e` and obtain the compact-current estimate from a positive matrix

\[
-\operatorname{Hess}\log H_e(0,0)\succeq0.
\]

That hope is impossible for this scalar interpolation.

Because `F_e(0,sigma)=1` identically,

\[
\boxed{
 \partial_\sigma\log H_e(0,0)=0,
 \qquad
 \partial_\sigma^2\log H_e(0,0)=0.
}
\tag{L-34403.26}
\]

On the other hand, (L-34403.10) gives

\[
 \partial_\tau\partial_\sigma\log F_e(0,0)
 =L\chi_{n,4}(j).
\tag{L-34403.27}
\]

For the aligned row `e^+=(4n,4j)`,

\[
 \chi_{4n,4}(4j)=0,
\]

whereas the denominator of (L-34403.22) contributes the factor four. Hence

\[
\boxed{
 \partial_\tau\partial_\sigma\log H_e(0,0)
 =-4L\chi_{n,4}(j).
}
\tag{L-34403.28}
\]

Whenever `chi_(n,4)(j)=1`, the negative log-Hessian has the form

\[
\boxed{
 -\operatorname{Hess}\log H_e(0,0)
 =
 \begin{pmatrix}
 \Delta_4R(e)&4L\\
 4L&0
 \end{pmatrix},
}
\tag{L-34403.29}
\]

whose determinant is

\[
\boxed{-16L^2<0.}
\tag{L-34403.30}
\]

Thus it is indefinite, independently of the size of the positive radix-four moat.

This is a structural no-go, not a numerical failure.

## 8. Consequence for the closing Schur mechanism

The positive scalar source interpolation exists, but it cannot be the two-variable partition postulated abstractly in PR #345 Section 4. Its source coordinate is flat at `tau=0`, so it has no source-source Fisher diagonal capable of paying a nonzero mixed score.

A successful Schur/Cramér--Rao closure must therefore retain an additional source-convolved physical/Hermitian coordinate, for example the `K_(tau,sigma)` leg of (L-34403.11), the matching parity current/bare jet of PR #329/#346, or an equivalent vector-valued Gram. This agrees with the independent-frequency/source-complete orientation already required by the repository firewalls.

The theorem removes one vague production task:

```text
construct a positive Q4-to-compact two-parameter Jordan family
```

is **closed exactly**.

The remaining task is narrower:

```text
construct/use the source-convolved vector/Hermitian Fisher matrix;
prove its relative radix-four Schur complement controls the compact innovation.
```

No scalar positive-partition shortcut remains available.

## 9. Proof boundary

Closed exactly here:

1. linear Q=4-to-compact source interpolation;
2. coefficientwise-positive two-parameter Jordan family;
3. complete first two Jordan jets;
4. exact interpolation of the source-convolved current from `q4` to `q_circ`;
5. positive row partition and extension of the exact radix-four log-curvature;
6. exact mixed source derivative;
7. exact indefiniteness of the naive scalar Schur Hessian.

Still open:

1. vector/source-convolved Hermitian Schur matrix at the critical increment scale;
2. compact innovation domination;
3. coefficient-one global recurrence;
4. RH.
