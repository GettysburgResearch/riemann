# L-90401 — Every finite no-alias multirate Gabor compression collapses to one scalar profile

Claim ID: `L-90401`  
Status: **PROPOSED COMPLETE EXACT HARMONIC-ANALYSIS THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: Anthropic zeta-23 Poisson/Gabor identity and scalar Montgomery–Taylor variational theorem; PR #358 `L-90301`  
Scope: exact completed-frame identity and its two-trace consequence; it does not evaluate new prime sums and does not prove RH

## 1. Setup

Fix a support length `L>0`. For `j=1,...,m`, let

\[
\phi_j\in C_c^2(\mathbb R),
\qquad
\operatorname{supp}\phi_j\subseteq[-L/2,L/2].
\]

Let the `j`-th modulation lattice have arbitrary offset `a_j`, spacing `h_j>0`, and dual period

\[
P_j:=\frac{2\pi}{h_j}.
\]

Use the Fourier convention

\[
\widehat\phi(z)=\int_{\mathbb R}\phi(u)e^{izu}\,du.
\]

Define the completed frame kernel

\[
K_\infty(\tau,\tau')
 :=\sum_{j=1}^m\sum_{k\in\mathbb Z}
 \widehat\phi_j(\tau-a_j-kh_j)
 \overline{\widehat\phi_j(\tau'-a_j-kh_j)}.
\tag{L-90401.1}
\]

The **no-alias hypothesis** is

\[
\boxed{P_j\ge L\quad(1\le j\le m).}
\tag{L-90401.2}
\]

The critical lattice of the imported zeta-23 proof is the endpoint `P_j=L`. Larger `P_j` means a denser modulation lattice. The periods may be distinct, irrationally related, and the offsets arbitrary.

Put

\[
\boxed{
 v(u):=\frac1L\sum_{j=1}^m P_j|\phi_j(u)|^2.
}
\tag{L-90401.3}
\]

Then `v>=0` and `supp v` lies in the same interval.

## 2. Exact multirate collapse

### Theorem

Under (L-90401.2), for all real `tau,tau'`,

\[
\boxed{
K_\infty(\tau,\tau')
 =L\widehat v(\tau-\tau').
}
\tag{L-90401.4}
\]

In particular,

\[
\boxed{
K_\infty(\tau,\tau)
 =L\int_{\mathbb R}v(u)\,du,
}
\tag{L-90401.5}
\]

independently of `tau`, every offset, and every relation among the lattice spacings.

### Proof

Fix `j` and abbreviate `a=a_j`, `h=h_j`, `P=P_j`, `phi=phi_j`. Expanding the two transforms gives

\[
\begin{aligned}
&\sum_{k\in\mathbb Z}
 \widehat\phi(\tau-a-kh)
 \overline{\widehat\phi(\tau'-a-kh)}\\
&=\iint \phi(u)\overline{\phi(w)}
 e^{i\tau u-i\tau'w}e^{-ia(u-w)}
 \sum_{k\in\mathbb Z}e^{-ikh(u-w)}\,du\,dw.
\end{aligned}
\tag{L-90401.6}
\]

The Dirac-comb identity is

\[
\sum_{k\in\mathbb Z}e^{-ikhx}
 =P\sum_{r\in\mathbb Z}\delta(x-rP).
\tag{L-90401.7}
\]

Because `u,w` lie in an interval of length `L` and `P>=L`, the constraint `u-w=rP` has positive-measure solutions only for `r=0`; at `P=L`, the nonzero translates can meet only on boundary sets of measure zero. Hence (L-90401.6) equals

\[
P\int |\phi(u)|^2e^{i(\tau-\tau')u}\,du
=P\widehat{|\phi|^2}(\tau-\tau').
\tag{L-90401.8}
\]

Summing in `j` and using (L-90401.3) proves (L-90401.4). The same proof may be written with ordinary Poisson summation; the compact support kills every nonzero dual mode.

## 3. First and second traces see only `v`

Index a finite Weil Gram matrix by all atoms `(j,k)` whose centres lie in a height window. Completing each lattice away from the two ends gives the kernel (L-90401.4). Therefore the leading first trace depends on the whole multirate family only through

\[
K_\infty(\tau,\tau)=L\int v,
\]

and the Frobenius square depends only through

\[
|K_\infty(\tau,\tau')|^2
 =L^2|\widehat v(\tau-\tau')|^2.
\tag{L-90401.9}
\]

Every cross-lattice and cross-window term is already inside the single scalar profile `v`. Standard fixed-width taper and end-effect estimates from the imported proof apply lattice by lattice; a finite family changes constants, not the limiting functional.

On the zero side, evaluation of all atoms at one zero is still one vector. Thus:

- one distinct on-line zero contributes one positive rank-one atom;
- one off-line functional-equation pair contributes a pullback of one hyperbolic plane;
- adding lattices does not create extra zero-side rank per zero.

So the rank–trace–inertia assembly is unchanged.

## 4. Variational consequence

Let

\[
\lambda=\frac{L}{\log(T/2\pi)}\in(0,1].
\]

After scaling the support to `[-1/2,1/2]`, the limiting two-trace ratio is exactly the imported scalar functional

\[
\boxed{
 c_\lambda(v)
 =\frac{\lambda(\int v)^2}
 {\int v^2+
  \lambda^2\iint |s-t|v(s)v(t)\,ds\,dt}.
}
\tag{L-90401.10}
\]

The upstream Euler–Lagrange calculation gives

\[
 c_\lambda(v)\le c_\lambda^*
 :=\frac{\sqrt2\tan(\lambda/\sqrt2)}
 {1+(\lambda/\sqrt2)\tan(\lambda/\sqrt2)},
\tag{L-90401.11}
\]

with equality at the positive profile

\[
 v^*_{\lambda}(s)=\cos(\sqrt2\lambda s).
\]

Thus at `lambda=1` no finite no-alias multirate family can improve the imported constants

\[
2-\frac1{c_1^*}=0.6725007\ldots,
\qquad
\frac{3-1/c_1^*}{2}=0.8362503\ldots
\]

inside the same first-trace/Frobenius-square rank–inertia architecture.

## 5. Strict extension of `L-90301`

PR #358 `L-90301` treated several windows on one common critical lattice. The present theorem also covers:

- arbitrary lattice offsets;
- different oversampling rates;
- irrationally related or incommensurable lattices;
- arbitrary finite mixtures of the above;
- vector-valued windows split across distinct no-alias rates.

All collapse to one nonnegative scalar profile.

## 6. Exact frontier left open

To escape (L-90401.11), a proposal must use at least one of:

1. an **aliased** lattice `P_j<L`, so translated support overlaps survive Poisson summation;
2. frequency-dependent/nonstationary atoms for which there is no stationary completed kernel;
3. several inequivalent quadratic statistics retained separately rather than one Frobenius sum;
4. genuinely new arithmetic moments or bandwidth beyond one;
5. a full configuration certificate not representable by this two-trace compression.

`L-90402` identifies the exact additional variables in the aliased case. `L-90403` shows that fixed or subpolynomial prime-resonant alias banks cannot change the leading constant through their exact resonant diagonal alone.

## 7. Proof boundary

Closed exactly here:

1. arbitrary-offset, arbitrary-rate completed Poisson identity under `P_j>=L`;
2. collapse of all completed first and second trace data to one scalar `v`;
3. extension of the Montgomery–Taylor scalar ceiling to every finite no-alias multirate family.

Not proved here:

1. finite-window analytic error terms beyond those already present upstream;
2. any useful aliased prime-side asymptotic;
3. any improvement of the zeta-23 constants;
4. RH.
