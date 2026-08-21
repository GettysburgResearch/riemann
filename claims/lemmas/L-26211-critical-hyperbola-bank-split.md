# L-26211 — Critical hyperbola bank and strict lower-scale remainder

Claim ID: `L-26211`  
Title: Dirichlet hyperbola splitting decomposes the fixed digital output into a critical opposite-parity prefix bank and one source-complete remainder whose every monomial lies at a strict lower logarithmic scale  
Status: **PROPOSED COMPLETE — exact finite convolution, support, and pole-mode algebra pending independent review**  
Date: 2026-08-08  
Depends on: `L-26210`; PR #236 `R-23008`; PR #269 `L-26901/L-26903`  
Scope: exact two-sided bank decomposition and its critical scaling; no norm contraction for the lower-scale remainder and no RH conclusion

## 1. Prefix operators

Retain

\[
c_2(n)=1-v_2(n),
\]

\[
\omega_2(n)
=
\mu(n)-\frac32\mathbf1_{2\mid n}\mu(n/2)
+rac12\mathbf1_{4\mid n}\mu(n/4),
\]

and

\[
c_2*\omega_2
=
\varepsilon-\frac52\delta_2+\delta_4.
\tag{L-26211.1}
\]

For a real number \(Y>1\), define the normalized strict prefix operators

\[
\mathcal C_Y
=
\sum_{1\le n<Y}
\frac{c_2(n)}{\sqrt n}\tau_n,
\qquad
\mathcal O_Y
=
\sum_{1\le d<Y}
\frac{\omega_2(d)}{\sqrt d}\tau_d,
\tag{L-26211.2}
\]

where \((\tau_n f)(t)=f(t-\log n)\).

Put

\[
\mathcal H
=I-\frac5{2\sqrt2}\tau_2+rac12\tau_4.
\tag{L-26211.3}
\]

## 2. Exact two-sided hyperbola identity

Fix an integer \(N\ge3\). Every factor pair \(dn<N^2\) satisfies at least one of

\[
d<N,
\qquad
n<N.
\]

Inclusion--exclusion in the product variable therefore gives

\[
\boxed{
\begin{aligned}
\mathcal H
={}&
\sum_{d<N}
\frac{\omega_2(d)}{\sqrt d}
\tau_d\mathcal C_{N^2/d}\\
&+
\sum_{n<N}
\frac{c_2(n)}{\sqrt n}
\tau_n\mathcal O_{N^2/n}
-
\mathcal O_N\mathcal C_N.
\end{aligned}}
\tag{L-26211.4}
\]

The left side is the complete convolution because its coefficients are supported on \(1,2,4<N^2\). The first two sums include every pair \(dn<N^2\), and the last term removes the pairs counted twice.

Since translations and convolution commute,

\[
\mathcal O_N\mathcal C_N
=
\sum_{n<N}
\frac{c_2(n)}{\sqrt n}
\tau_n\mathcal O_N.
\]

Hence (L-26211.4) has the more useful form

\[
\boxed{
\mathcal H
=
\mathcal S_N+\mathcal L_N,
}
\tag{L-26211.5}
\]

where

\[
\boxed{
\mathcal S_N
=
\sum_{d<N}
\frac{\omega_2(d)}{\sqrt d}
\tau_d\mathcal C_{N^2/d},
}
\tag{L-26211.6}
\]

and

\[
\boxed{
\mathcal L_N
=
\sum_{n<N}
\frac{c_2(n)}{\sqrt n}
\tau_n
\left(
\mathcal O_{N^2/n}-\mathcal O_N
\right).
}
\tag{L-26211.7}
\]

This is an exact finite identity for every \(N\ge3\).

## 3. Strict lower-scale support of the remainder

Expanding (L-26211.7), every monomial of \(\mathcal L_N\) has the form

\[
\frac{c_2(n)\omega_2(d)}{\sqrt{nd}}\tau_{nd}
\]

with

\[
1\le n<N,
\qquad
N\le d<N^2/n.
\tag{L-26211.8}
\]

Consequently

\[
\boxed{
N\le nd<N^2.
}
\tag{L-26211.9}
\]

Thus, on a causal physical block ending at time \(J\), every remainder column is evaluated at time at most

\[
J-\log N.
\tag{L-26211.10}
\]

No current-block or smaller-delay monomial is hidden in \(\mathcal L_N\). The strict destination is obtained by exact source recombination before a norm.

This is the lower-scale property absent from the one-sided bank inequality of `L-26210`.

## 4. Critical suppression of the prefix bank at a zero mode

Let

\[
\rho=\beta+i\gamma
\]

be a nontrivial zeta zero. The full digital series \(C_2(s)\) vanishes at \(ho\). PR #236 `R-23008` gives, for every \(Y\ge3\),

\[
\left|
\sum_{n<Y}rac{c_2(n)}{n^\rho}
\right|
\le
C_\rho(1+\log Y)Y^{-\beta}.
\tag{L-26211.11}
\]

Evaluating the first bank in (L-26211.6) at the exponential mode corresponding to \(ho\), the factor \(d^{-\rho}\) from translation cancels the \(d^\beta\) from \(Y=N^2/d\). Therefore

\[
\begin{aligned}
|\mathcal S_N(\rho)|
&\le
C_\rho N^{-2\beta}
\sum_{d<N}|\omega_2(d)|
\left(1+\log\frac{N^2}{d}\right)\\
&\le
C_\rho' N^{1-2\beta}(1+\log N),
\end{aligned}
\tag{L-26211.12}
\]

because \(|\omega_2(d)|\le5/2\).

Hence

\[
\boxed{
\mathcal S_N(\rho)
=O_\rho\left(N^{1-2\beta}\log N\right).
}
\tag{L-26211.13}
\]

At a critical-line zero this is only polylogarithmic, which is compatible with the line spectrum. At every off-line zero with \(\beta>1/2\),

\[
\boxed{
\mathcal S_N(\rho)\longrightarrow0.
}
\tag{L-26211.14}
\]

Thus a hypothetical off-line pole is forced asymptotically into the strict lower-scale remainder \(\mathcal L_N\). This is an exact routing theorem, not yet a contraction estimate.

## 5. Critical-order interpretation

The synthesis side of \(\mathcal S_N\) contains fewer than \(N\) opposite-parity coefficients, while every digital prefix has length at least \(N\). The resulting squared observation scale is \(N^2\), equal to the critical \(R\)-order of `L-26210` with \(R=N^2\).

Therefore (L-26211.5) is simultaneously:

- compatible with genuine critical-line modes;
- suppressive on every fixed off-line mode in its current-scale bank;
- strict in logarithmic scale on its complete remainder.

This is the correct shape of a pole-exclusion recurrence.

## 6. The remaining source-specific estimate

The exact identity does not bound \(\mathcal L_N\) by its delayed target energy. Its coefficients must not be charged in total variation: doing so loses the Möbius and digital cancellation and produces a supercritical factor.

A complete proof must use the PR #269 factor-five source structure to prove a coupled estimate of the form

\[
\boxed{
\|\mathcal L_N f\|_{\mathrm{phys},J}^2
+
\|\mathcal S_N f\|_{\mathrm{phys},J}^2
\le
N^{2+o(1)}D_N(J)
+
\theta_N\,\mathcal E(J-\log N),
}
\tag{L-26211.15}

with a source-complete tempered channel \(D_N\) and a net charge satisfying the critical reserve required by the pole-exclusion consumer.

The physical norm must be the independent-frequency normal block of PR #241, and every \(\omega_2\) cross term, quotient cell \(2,3,4\), collar, and finite boundary row must remain in the ledger.

Equation (L-26211.15) is not proved here.

## 7. Review mutations

Any production use of the hyperbola split must fail if:

1. strict inequalities in the prefixes are changed inconsistently;
2. a factor pair \(dn<N^2\) is omitted or counted twice;
3. a remainder monomial with \(nd<N\) survives;
4. the signed \(\omega_2\) synthesis is replaced by total variation before the physical Gram;
5. the critical-line scaling is claimed better than \(N^2\);
6. the dyadic or \(2/3\) Mertens projection disappears.

## 8. Proof boundary

Closed exactly, subject to review:

- the two-sided hyperbola bank identity;
- the strict lower-scale support of its remainder;
- the critical \(N^2\) current-scale observation count;
- the \(N^{1-2\beta}\log N\) suppression of every off-line zero in the current-scale bank.

Open:

- the source-specific physical estimate for the remainder;
- the net reserve after collars and finite transition rows;
- RH.
