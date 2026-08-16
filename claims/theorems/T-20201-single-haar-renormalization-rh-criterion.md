# T-20201 — A single Haar renormalization defect is an RH criterion

Claim ID: `T-20201`  
Title: Eventual one-sidedness of one fixed three-tap screw defect is equivalent to the Riemann Hypothesis  
Status: `PROPOSED — COMPLETE ARGUMENT FROM THE IMPORTED SCREW/LAPLACE IDENTITY; PENDING INDEPENDENT REVIEW`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: `L-19801`'s normalization of the Nakamura–Suzuki zeta screw function and its Fourier–Laplace identity; Landau's one-sign theorem for Laplace transforms; standard discreteness and functional-equation symmetry of the zeros of `xi`  
Scope: a global scalar criterion, not a finite computation  
Related counterexample candidates: none

## 1. Setup

Use the screw function normalization already fixed in `L-19801`:

\[
\Psi(t)=-g_\zeta(t),
\]

with the locally uniform zero expansion

\[
 g_\zeta(t)=\sum_\gamma m_\gamma
 \frac{e^{-i\gamma t}-1}{\gamma^2}
\tag{1}
\]

and the Fourier–Laplace identity

\[
\boxed{
 \int_0^\infty \Psi(t)e^{izt}\,dt
 =-\frac1{z^2}\frac{\xi'}{\xi}
 \left(\frac12-iz\right),
 \qquad \operatorname{Im}z>\frac12.}
\tag{2}
\]

Here

\[
 \gamma=\frac{\rho-1/2}{i}
\]

runs over nontrivial zeros with multiplicity. Define the dyadic Haar defect

\[
\boxed{
 \mathcal D(t)=4\Psi(t)-\Psi(2t).}
\tag{3}
\]

## 2. RH gives a literal spectral square

Assume RH. Pairing the real zero coordinates `+gamma` and `-gamma` in (1) gives

\[
 \Psi(t)=2\sum_{\gamma>0}m_\gamma
 \frac{1-\cos(\gamma t)}{\gamma^2}.
\tag{4}
\]

Therefore

\[
\begin{aligned}
 \mathcal D(t)
 &=\sum_{\gamma>0}m_\gamma
   \frac{|1-e^{-i\gamma t}|^4}{\gamma^2}\\
 &=4\sum_{\gamma>0}m_\gamma
   \frac{(1-\cos(\gamma t))^2}{\gamma^2}
 \ge0.
\end{aligned}
\tag{5}
\]

Equivalently, with the fixed Haar step

\[
 h_t=\mathbf1_{[0,t]}-\mathbf1_{[t,2t]},
\]

one has

\[
 \widehat h_t(\gamma)
 =\frac{(1-e^{-i\gamma t})^2}{i\gamma},
\]

so (5) is the spectral norm square associated with one fixed three-tap vector

\[
 (1,-2,1).
\]

In the finite-node screw matrix convention,

\[
 \sum_{j,k=0}^2 a_ja_k g_\zeta((j-k)t)
 =2\mathcal D(t),
 \qquad a=(1,-2,1).
\tag{6}
\]

Thus this is not a varying packet hierarchy: the same Haar shape is used at every scale.

## 3. Laplace transform and pole-cancellation descent

Substituting `u=2t` in (2) gives, initially for `Im z>1`,

\[
\boxed{
 \int_0^\infty \mathcal D(t)e^{izt}\,dt
 =\frac2{z^2}\left[
 F\left(\frac12-\frac{iz}{2}\right)
 -2F\left(\frac12-iz\right)
 \right],}
\tag{7}
\]

where

\[
 F=\frac{\xi'}{\xi}.
\]

The load-bearing fact is that holomorphy of the bracket in the complete upper half-plane forces RH.

Suppose the bracket in (7) is holomorphic for `Im z>0`. If

\[
 \rho=\frac12+\delta+i\tau,
 \qquad \delta>0,
\]

is a zero of multiplicity `m`, put

\[
 z_0=i(\rho-1/2).
\]

Then `Im z_0=delta>0`, and the second logarithmic derivative term in (7) has a pole at `z_0`. Cancellation is possible only if

\[
 \rho_1=\frac12+\frac{\rho-1/2}{2}
\tag{8}
\]

is also a zero. A residue calculation gives the same multiplicity: near `z_0`,

\[
 F\left(\frac12-\frac{iz}{2}\right)
 -2F\left(\frac12-iz\right)
 =\frac{2i(m_1-m)}{z-z_0}+O(1).
\]

Hence `m_1=m`. Iterating produces distinct zeros

\[
 \rho_k=\frac12+2^{-k}(\rho-1/2)
\]

converging to the finite point `1/2`, contradicting discreteness of the zero set of the nonzero entire function `xi`. Therefore no zero has real part greater than `1/2`; the functional equation gives RH.

This is the **pole-descent mechanism**. It replaces an unbounded matrix-capture argument by rigidity under one dyadic rescaling.

## 4. From one-sidedness to holomorphy

The exact prime/Lerch formula in `L-19801` gives the unconditional derivative estimate

\[
 |\Psi'(t)|\le C(1+t)e^{t/2}
\tag{9}
\]

between prime-power knots, with the corresponding variation bound across closed intervals. Hence

\[
 |\mathcal D'(t)|
 \le4|\Psi'(t)|+2|\Psi'(2t)|
 \le C'(1+t)e^t.
\tag{10}
\]

Assume that for every `epsilon>0`,

\[
 \mathcal D(t)\ge-C_\epsilon(1+t)^{B_\epsilon}e^{\epsilon t}
\tag{11}
\]

eventually. Add a positive polynomial multiple of `e^(epsilon t)` and a compactly supported continuous correction to obtain an everywhere nonnegative function `H_epsilon`. Its Laplace transform equals the meromorphic right side of (7) plus a function holomorphic in `Im z>epsilon`.

Landau's one-sign theorem says that, unless `H_epsilon` is eventually zero, its abscissa of convergence is a singularity on the positive imaginary axis. The right side has no such singularity because `xi` has no real zero. Thus the abscissa is at most `epsilon`; if the function is eventually zero, the same conclusion is immediate. Subtracting the correction shows that the bracket in (7) is holomorphic for `Im z>epsilon`.

Since (11) holds for every positive `epsilon`, the bracket is holomorphic throughout `Im z>0`. Section 3 then proves RH.

## 5. Integer sampling

Set

\[
 t_n=\log n,
 \qquad n\ge2.
\tag{12}
\]

For `t_n<=t<=t_(n+1)`,

\[
 t_{n+1}-t_n=\log(1+1/n)\le1/n
\]

and `e^t` is comparable to `n`. Equation (10) therefore gives the critical interpolation bound

\[
 |\mathcal D(t)-\mathcal D(t_n)|
 \le C(1+t).
\tag{13}
\]

The exponential growth of the derivative is exactly canceled by the logarithmic integer mesh.

Consequently:

\[
\boxed{
 \mathrm{RH}
 \iff
 \mathcal D(\log n)\ge0
 \text{ for every sufficiently large integer }n.}
\tag{14}
\]

More generally,

\[
\boxed{
 \mathrm{RH}
 \iff
 \bigl(-\mathcal D(\log n)\bigr)_+=n^{o(1)}.}
\tag{15}
\]

For the reverse implication in (15), the sample condition and (13) imply (11) for every `epsilon>0`. Under RH, (5) gives nonnegativity at every real scale.

Thus false RH forces the negative Haar defect to exceed every subpower envelope on every integer tail.

## 6. General integer dilations

For an integer `r>=2`, define

\[
 \mathcal D_r(t)=r^2\Psi(t)-\Psi(rt).
\tag{16}
\]

Under RH,

\[
 \mathcal D_r(t)
 =2\sum_{\gamma>0}m_\gamma
 \frac{r^2(1-\cos\gamma t)-(1-\cos r\gamma t)}{\gamma^2}
 \ge0
\tag{17}
\]

because `|sin(rx)|<=r|sin x|`. Its transform is

\[
 \int_0^\infty\mathcal D_r(t)e^{izt}dt
 =\frac r{z^2}\left[
 F\left(\frac12-\frac{iz}{r}\right)
 -rF\left(\frac12-iz\right)
 \right].
\tag{18}
\]

The same pole descent maps

\[
 \rho\mapsto\frac12+\frac{\rho-1/2}{r}.
\]

The defects satisfy the exact cocycle

\[
\boxed{
 \mathcal D_{rs}(t)=r^2\mathcal D_s(t)+\mathcal D_r(st).}
\tag{19}
\]

The dyadic case `r=2` is the minimal fixed Haar filter and the preferred route.

## 7. What this theorem changes

The repository already has complete countable dyadic FIR and finite-element search hierarchies. This theorem is substantially smaller:

- one scalar at each integer scale;
- one fixed coefficient vector `(1,-2,1)`;
- one finite prime-power sum through `n^2`;
- no growing packet dimension;
- no principal-angle, matrix-capture, or cofinal Schur-complement hypothesis.

It does not prove the eventual sign. It identifies a new global arithmetic target whose failure is forced by any off-line zero through a rigid dyadic pole cascade.

## 8. Proof boundary

- Equations (3)–(8), (16)–(19) are exact after accepting the screw normalization and Laplace identity.
- The Landau step uses the standard one-sign theorem, exactly as in `L-19801`.
- The integer transfer uses only the unconditional derivative budget already derived there.
- The theorem does **not** establish `D(log n)>=0` cofinally.
- The theorem is new and remains `PROPOSED`; it cannot retroactively promote `T-19801` or any operator branch.
