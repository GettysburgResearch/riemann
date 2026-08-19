# L-99272 — Complete scalar Mellin–Landau audit and dependency firewall

Claim ID: `L-99272`  
Status: **PROVED SELF-CONTAINED ANALYTIC THEOREM**  
Created: 2026-08-20  
Depends on: elementary Dirichlet series, the zeta functional equation  
RH status: **not assumed**

This lemma reconstructs the analytic consumer used by `L-99270` without
importing the SHARP row kernel, compact Hall, random-key tree, Volterra frame,
or any score/capacity theorem.

## 1. Scalar transform from primitive arithmetic

The direct coefficient identity

\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67)
\]

gives, for `Re(z)>1`,

\[
\sum_{n\ge1}\beta(n)n^{-z}
=(1-67^{-z})/\zeta(z).
\]

Also, for `Re(s)>1/2`,

\[
\int_1^\infty(4\sqrt x-3)x^{-s-1}\,dx
=\frac{s+3/2}{s(s-1/2)}.
\]

Absolute Fubini therefore proves (L-99270.2) directly.  No row identity is an
antecedent.

## 2. Positive-real-axis audit

Let `z=s+1/2` with real `s>0`.

- If `z>1`, the Euler product gives `zeta(z)>0`.
- If `1/2<z<1`, the alternating series
  \[
  \eta(z)=\sum_{n\ge1}(-1)^{n-1}n^{-z}
  =\sum_{m\ge1}\bigl((2m-1)^{-z}-(2m)^{-z}\bigr)>0
  \]
  and `eta(z)=(1-2^(1-z))zeta(z)` give `zeta(z)<0`.
- At `z=1`, zeta has residue one.  Hence the zero of `1/zeta(z)` cancels the
  displayed factor `(s-1/2)^(-1)`.

The remaining factors are nonzero for real `s>0`.  Thus the continuation in
(L-99270.2), and its product with `K_A(s)`, is analytic at every positive real
`s`.

## 3. Specialized Landau theorem

Let `f:[1,infinity)->[0,infinity)` be locally integrable, not almost everywhere
zero, and suppose

\[
F_f(s)=\int_1^\infty f(x)x^{-s-1}\,dx
\]

has a finite abscissa of convergence `sigma_c`.  Then `s=sigma_c` is a
singularity.

### Proof

Assume instead that `F_f` is holomorphic on a disc
`|s-sigma_c|<r`.  Put `s_1=sigma_c+r/4`.  For every `n>=0`, differentiation
under the integral is valid and

\[
(-1)^nF_f^{(n)}(s_1)
=\int_1^\infty f(x)(\log x)^n x^{-s_1-1}\,dx\ge0.
\]

The disc about `sigma_c` gives the Taylor series at `s_1` radius at least
`3r/4`.  For real `0<=u<3r/4`, its nonnegative-coefficient form is

\[
F_f(s_1-u)
=\sum_{n\ge0}\frac{(-1)^nF_f^{(n)}(s_1)}{n!}u^n.
\]

Tonelli identifies the sum with

\[
\int_1^\infty f(x)x^{-s_1-1}e^{u\log x}\,dx
=\int_1^\infty f(x)x^{-(s_1-u)-1}\,dx.
\]

Taking `u=r/2` proves convergence at
`sigma_c-r/4`, contradicting the definition of `sigma_c`.  This proves the
theorem.

## 4. Correct abscissa logic

The primitive scalar satisfies `h(x)=O(sqrt(x) log(2x))`, so every positive
surrogate used in `L-99270` has a finite abscissa no larger than `1/2`.
If its explicit continuation is analytic at all positive real points, Landau
forces its abscissa to be at most zero.  Its defining Mellin integral is then
holomorphic throughout `Re(s)>0`.

This is the precise step compressed in earlier packets.  Analyticity on the
positive real axis alone is not asserted to imply half-plane holomorphy; the
nonnegative-density Landau theorem and the finite-abscissa bound are both used.

## 5. Off-line pole and functional equation

If `zeta(rho)=0` and `Re(rho)>1/2`, put `s_0=rho-1/2`.  Then

\[
|67^{-\rho}|<1,
\qquad 1-67^{-\rho}\ne0,
\]

and `rho+1`, `s_0`, and `s_0-1/2` are nonzero.  A zero of multiplicity `m`
therefore gives a pole of the same multiplicity at `s_0`.  No holomorphic
negative-mass correction, compact initial correction, or zero-free smoothing
factor can remove it.

Landau excludes every zero to the right of the critical line.  The functional
equation for the completed zeta function reflects a nontrivial zero `rho` to
`1-rho`, so zeros to the left are excluded as well.

## 6. Dependency firewall

The conclusion-facing chain is exactly

```text
primitive beta coefficient
 -> scalar h
 -> one producer from L-99270
 -> explicit scalar Mellin transform
 -> specialized Landau theorem
 -> functional equation
 -> RH.
```

The following are useful cross-checks but **not dependencies**:

```text
PR #642 SHARP row kernel;
compact Hall/profile monotonicity;
Radon-Nikodym child thinning;
random-key common-parent tree;
PR #648 calibration coboundary;
fixed-row large-j noncancellation;
Volterra boundary modes;
score, capacity, thinning, terminal, or prime-square estimates.
```
