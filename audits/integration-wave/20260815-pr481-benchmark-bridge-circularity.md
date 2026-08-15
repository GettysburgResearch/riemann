# Exact audit: the imported `J_Lambda - 4 sqrt(X)` bridge is RH-bearing

**Review target:** PR #481 at `005ae49723898d8661d407a0433a6d69cb6d6efc`  
**Disposition:** **UNPROVEN / GAP as a pre-RH input**  
**Mathematical type:** **RH-BEARING ONE-SIDED CRITERION**

## 1. The submitted bridge

The live factor-67 score files use

\[
J_\Lambda(X)-4\sqrt X<4\log X
\tag{1}
\]

as a frozen elementary benchmark comparison. The PR #481 locks do not identify a path/blob theorem proving (1).

The issue is not merely missing provenance. Any eventual bound of this shape already implies RH.

## 2. Exact Mellin transform

Put

\[
J_\Lambda(X)=
\sum_{n\le X}
\frac{\Lambda(n)}{\sqrt n}\log\frac Xn.
\]

For `Re z>1/2`, finite Fubini gives

\[
\begin{aligned}
\int_1^\infty J_\Lambda(X)X^{-z-1}dX
&=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
  \int_n^\infty\log(X/n)X^{-z-1}dX\\
&=\frac1{z^2}
  \sum_{n\ge2}\frac{\Lambda(n)}{n^{z+1/2}}\\
&=\boxed{\frac{-\zeta'/\zeta(z+1/2)}{z^2}}.
\end{aligned}
\tag{2}
\]

Also

\[
\int_1^\infty4\sqrt X\,X^{-z-1}dX
=\frac4{z-1/2}.
\tag{3}
\]

Therefore, for

\[
D(X)=J_\Lambda(X)-4\sqrt X,
\]

one has

\[
\boxed{
\widehat D(z)=
\frac{-\zeta'/\zeta(z+1/2)}{z^2}
-\frac4{z-1/2}.
}
\tag{4}
\]

## 3. Pole audit

Near `z=1/2`,

\[
-\frac{\zeta'}\zeta(z+1/2)
=\frac1{z-1/2}+O(1),
\]

and `z^-2=4+O(z-1/2)`. Thus the real pole at `z=1/2` cancels in (4).

If

\[
\rho=\frac12+\delta+i\gamma,
\qquad\delta>0,
\]

is a nontrivial zero of multiplicity `m_rho`, then (4) has a genuine nonreal pole at

\[
z=\delta+i\gamma
\]

with nonzero residue

\[
-\frac{m_\rho}{(\delta+i\gamma)^2}.
\]

There is no singularity on the open positive real axis:

- zeta has no real zero for real `s>1/2`;
- the pole at `s=1` has been canceled by (3);
- the factor `z^-2` has its pole only at zero.

## 4. Landau contradiction

Assume that for some constant `C`,

\[
D(X)\le C\log X
\tag{5}
\]

for all sufficiently large `X`. Altering a compact interval only adds an entire Mellin term. Hence define

\[
g(X)=C\log X-D(X)\ge0
\]

for all `X>=1` after such a compact alteration.

The Mellin transform of `C log X` is `C/z^2`, so every off-line pole of (4) remains a nonreal pole of `g`'s transform. Let `sigma_c` be the finite abscissa of convergence of that nonnegative Mellin/Laplace transform.

If `sigma_c<delta`, the defining integral is holomorphic at `delta+i gamma`, contradicting the pole there.

If `sigma_c>=delta>0`, Landau's theorem for a nonnegative function forces a singularity at the real point `sigma_c`. The real-pole audit above shows that no such positive-real singularity exists.

Both alternatives are impossible. Thus no zero can satisfy `Re rho>1/2`. The functional equation then gives RH.

Therefore

\[
\boxed{
J_\Lambda(X)-4\sqrt X\le C\log X
\text{ eventually}
\Longrightarrow RH.
}
\tag{6}
\]

In particular, the submitted bound (1) is itself conclusion-producing.

## 5. Consequence for PR #481

The following uses are invalid unless the bridge receives an independent proof that would itself prove RH:

```text
L-91728  one-shot native root cost
L-91735  translation from continuum shortfall to native deficit
L-91736  O(log X) distinguished-root composition
T-91724  corrected factor-67 resolution proposal
T-91725  PR #478 audit supplement composition
```

The elementary fallback

\[
(1-\tau_K)J_\Lambda(X)<4290\log X
\]

controls only the incremental cost of the scalar thinning. It does not bound the baseline native gap between `J_Lambda` and the score of the unthinned continuum root packet.

A noncircular successor must compute

\[
\langle Y_4,r_X\rangle
\]

directly from the explicit fully corrected root slack vector, including the terminal, finite-base, and common-port packets, without passing through (1).

## 6. Verdict

```text
statement (1) as a mathematical assertion      NOT REFUTED
statement (1) as an unconditional input        UNPROVEN / CIRCULAR
one-sided O(log X) bridge                      RH-BEARING CRITERION
incremental thinning cost                      RETAINED
required repair                                DIRECT Y4 ROOT-SLACK AUDIT
Riemann Hypothesis                             UNPROVEN
```
