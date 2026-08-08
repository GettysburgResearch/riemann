# R-21703 — The published cardinal Robin fiber is wrong and reflected tail domination is impossible

Claim ID: `R-21703`  
Title: Centered symmetrization forces an even `cosh+2z sinh` fiber, while the proposed `cosh+sinh/ell` fiber and finite reflected-tail domination cannot hold  
Status: **EXACT LOAD-BEARING SCOPE CORRECTION**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Frozen target: PR #296 at `4a68887f9f713aea7f63444030379fb864766a2d`  
Dependencies: PR #296 `L-21706/L-21707/T-21705`; elementary Mellin layer cake  
Scope: finite Brownian/Nörlund cardinal representation and the proposed `RCM` closure

## 1. Centered symmetrization must be even

Let `Y>0`, put

\[
m(s)=\mathbb E[Y^s],
\]

and define

\[
X(s)=m(s)+m(1-s).
\]

For

\[
s=\frac12+z,
\]

one has identically

\[
\boxed{
X\left(\frac12+z\right)
=X\left(\frac12-z\right).
}
\tag{R-21703.1}

Therefore every exact centered cardinal fiber must be an even entire function of `z`.

PR #296 `L-21707` uses the displayed fiber

\[
\widetilde\Phi_\ell(z)
=\cosh\frac{\ell z}{2}
+\frac1\ell\sinh\frac{\ell z}{2}.
\tag{R-21703.2}

For every finite nonzero `ell`,

\[
\widetilde\Phi_\ell(-z)
\ne\widetilde\Phi_\ell(z).
\]

Indeed its linear Taylor coefficient is `1/2`. It therefore cannot be the centered contribution of a symmetrized Mellin moment. The Robin determinant and positive/negative length classification derived from (R-21703.2) are not valid.

## 2. Correct derivation from the tail identity

Let

\[
Z=Y^2,
\qquad
T(u)=\mathbb P(Z>u).
\]

For `0<Re(s)<1`, the Mellin layer cake gives

\[
m(s)=\frac{s}{2}
\int_0^\infty u^{s/2-1}T(u)\,du.
\tag{R-21703.3}

Put `u=e^ell`, so `du=e^ell d ell`. At `s=1/2+z`, adding the reflected term gives

\[
\begin{aligned}
X\left(\frac12+z\right)
={}&\frac12\int_{-\infty}^{\infty}
 e^{\ell/4}T(e^\ell)\\
&\quad\times
\left[
\cosh\frac{\ell z}{2}
+2z\sinh\frac{\ell z}{2}
\right]d\ell.
\end{aligned}
\tag{R-21703.4}

The same formula applies to a positive tail defect, with `T` replaced by that defect. The correct centered fiber is therefore

\[
\boxed{
\Phi_\ell(z)
=\cosh\frac{\ell z}{2}
+2z\sinh\frac{\ell z}{2}.
}
\tag{R-21703.5}

It is even in `z`, and

\[
\Phi_{-\ell}(z)
=\cosh\frac{\ell z}{2}
-2z\sinh\frac{\ell z}{2}.
\tag{R-21703.6}

Positive and negative lengths are now genuinely different.

## 3. Reflected-tail domination is impossible at every finite N

PR #296 `T-21705` proposes, for the finite Nörlund tail, a pointwise inequality of the form

\[
W_N(a)\ge W_N(-a)
\qquad(a\ge0),
\tag{R-21703.7}

where

\[
W_N(a)
=e^{a/2}\overline T_N(\pi e^{2a})
\]

under the normalization of that branch.

For every finite `N`, the Nörlund law is a finite positive mixture of finite gamma sums. Hence it has a finite positive exponential moment: for some `theta_N>0`,

\[
\mathbb E[e^{\theta_N Z}]<\infty.
\]

Markov's inequality gives

\[
\overline T_N(u)
\le C_Ne^{-\theta_Nu}.
\tag{R-21703.8}

Consequently

\[
W_N(a)
\le C_Ne^{a/2}
\exp[-\theta_N\pi e^{2a}].
\tag{R-21703.9}

On the other hand, since the random variable is strictly positive,

\[
\overline T_N(\pi e^{-2a})\longrightarrow1,
\]

and therefore

\[
W_N(-a)
=e^{-a/2}[1+o(1)].
\tag{R-21703.10}

It follows that

\[
\boxed{
\frac{W_N(a)}{W_N(-a)}\longrightarrow0
\qquad(a\to\infty).
}
\tag{R-21703.11}

Thus (R-21703.7) is false for every finite `N`. No asymptotic sequence of Nörlund approximants can satisfy the proposed pointwise reflected-tail domination theorem.

## 4. What survives

The exact finite gamma algebra, logarithmic Nörlund convergence, and positive tail-defect identities on PR #296 are unaffected.

The correct spectral statement is:

```text
positive length ell    -> one nonnegative self-adjoint Robin fiber;
negative length ell    -> one Robin fiber with a real off-line pair;
finite N tail          -> necessarily contains negative-length mass;
pointwise RCM           -> impossible.
```

A completion must use cancellation or a global canonical-system structure across lengths. It cannot delete the negative-length sector by a pointwise tail inequality.

## 5. Exact disposition

```text
finite Brownian/gamma algebra               RETAINED
Nörlund convergence to xi                   RETAINED
published fiber cosh+sinh/ell                FALSE
correct fiber cosh+2z sinh                   PROVED
positive/negative Robin classification       REQUIRES CORRECTED FIBER
finite reflected-tail domination RCM         FALSE
BLNRZ / RH                                   UNPROVEN
```