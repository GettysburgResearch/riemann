# R-91008 — The scalar causal Cauchy mother has an interior-zero jump defect

Claim ID: `R-91008`  
Status: **EXACT REFUTATION OF `L-91032` AS WRITTEN — DIRECTED INTERVAL CERTIFICATE**  
Created: 2026-08-12  
Refutes: `L-91032-one-fixed-safe-scale-is-a-form-core-for-the-zeta-screw-kernel.md` at branch head `f1a5f2b22bb10d2de5ff3af26a04cc0de16759f8`  
Consequential status: `T-91007` is **UNPROVEN / DEPENDS ON A FALSE FORM-CORE LEMMA**  
RH status: **unproved**

## 1. The causal impulse can be written exactly

At scale one, put

\[
 \alpha=\frac{163-5\sqrt{561}}{28},
 \qquad
 \beta=\frac{163+5\sqrt{561}}{28},
\]

and use the right-half-plane Laplace representative of the causal factor,

\[
 P(s)
 =
 \sqrt{378}\,
 \frac{s(s+\sqrt\alpha)(s+\sqrt\beta)}
 {(s+1)^2(s+2)^2(s+4)^2}.
 \tag{R-91008.1}
\]

This differs from the Fourier boundary value of `L-91031` only by the fixed
unimodular convention needed to pass from `u` to `s=-iu`.

Define

\[
\begin{aligned}
 A&=\frac{70\sqrt{33}-61\sqrt{42}}9>0,\\
 B&=\frac{5(\sqrt{33}-\sqrt{42})}3<0,\\
 C&=3(5\sqrt{33}-4\sqrt{42})>0,\\
 D&=\frac{20(\sqrt{33}-\sqrt{42})}3<0.
\end{aligned}
\tag{R-91008.2}
\]

Exact partial fractions give

\[
 \boxed{
 P(s)=
 -\frac{A}{s+1}
 +\frac{B}{(s+1)^2}
 +\frac{C}{(s+2)^2}
 +\frac{A}{s+4}
 +\frac{D}{(s+4)^2}.
 }
 \tag{R-91008.3}
\]

Therefore its causal impulse is

\[
 \boxed{
 \psi(t)=
 -Ae^{-t}+Bte^{-t}+Cte^{-2t}
 +Ae^{-4t}+Dte^{-4t},
 \qquad t\ge0.
 }
 \tag{R-91008.4}
\]

It is continuous, real analytic on `(0,infinity)`, exponentially decaying and
satisfies `psi(0)=psi'(0)=0`.

Scale covariance gives

\[
 \psi_a(t)=a\,\psi(at)
 \tag{R-91008.5}
\]

up to the same irrelevant global phase.

## 2. There is a genuine positive-time zero

Outward interval evaluation gives

\[
 \psi(31/20)
 \in
 (0.0087229042372578,\,
  0.0087229042372674)
 \tag{R-91008.6}
\]

and

\[
 \psi(8/5)
 \in
 (-0.012743812577641,\,
  -0.012743812577631).
 \tag{R-91008.7}
\]

Hence there is a zero

\[
 \boxed{
 \tau_0\in(31/20,8/5).
 }
 \tag{R-91008.8}
\]

The retained high-precision localization is

\[
 \tau_0=
 1.569866480336558256315360159785539\ldots .
 \tag{R-91008.9}
\]

At scale `a`, the corresponding zero is `tau_0/a`.

## 3. An exact hidden jump vector

Fix

\[
 a>\frac12,
 \qquad
 1<\eta<2a,
\]

and write the causal carrier family in the physical convention of `L-91032` as

\[
 f_{a,x}^{+}(t)
 =
 -i\frac{d}{dt}
 \left(e^{ixt}\psi_a(t)\right).
 \tag{R-91008.10}
\]

In

\[
 \mathcal H_{\eta,+}
 =
 L^2((0,\infty),e^{\eta t}dt)
\]

define

\[
 \boxed{
 h_0(t)=
 e^{-\eta t}
 \mathbf 1_{(\tau_0/a,\infty)}(t).
 }
 \tag{R-91008.11}
\]

Then `h_0` is nonzero and belongs to `H_(eta,+)`.  For every real carrier `x`,

\[
\begin{aligned}
 \langle h_0,f_{a,x}^{+}\rangle_{\mathcal H_{\eta,+}}
 &=
 \int_{\tau_0/a}^{\infty}
 \overline{f_{a,x}^{+}(t)}\,dt\\
 &=
 i\left[
  e^{-ixt}\overline{\psi_a(t)}
 \right]_{\tau_0/a}^{\infty}\\
 &=0.
\end{aligned}
\tag{R-91008.12}
\]

The upper endpoint vanishes by exponential decay and the lower endpoint
vanishes because `psi_a(tau_0/a)=0`.

But `h_0` is not a scalar multiple of the integral representer
`e^(-eta t)`.  Thus the orthogonal complement of the scalar causal family has
dimension at least two:

\[
 \boxed{
 \dim
 \left(
 \overline{\operatorname{span}}\{f_{a,x}^{+}:x\in\mathbb R\}
 \right)^\perp
 \ge2.
 }
 \tag{R-91008.13}
\]

This directly contradicts `(L-91032.7)`.

## 4. The distributional proof failed at the zero set

`L-91032` argued from

\[
 H'\,\overline{\psi_a}=0
\]

that `H` is constant because `psi_a` is nonzero almost everywhere.  That
implication is false for distributions.  If `H` has a jump at a zero of
`psi_a`, then `H'` contains a Dirac mass supported at that zero, and

\[
 \psi_a\,\delta_{\tau_0/a}=0.
\]

The vector `(R-91008.11)` is exactly this missing distributional solution.

The correct hypothesis for the scalar argument would be that the physical
mother is nowhere zero on the open half-line.  That cannot hold for the present
real causal mother: it has zero total integral and is not identically zero, so
its sign must change.

## 5. The one bridge cannot repair the missing dimensions

The reflected anti-causal family has the corresponding reflected jump defect.
Before adding a bridge, the direct sum of the two half-line scalar families has
orthogonal codimension at least four in the full weighted space.  Passing to the
global mean-zero hyperplane removes at most one dimension, and adjoining the
single bridge of `L-91032` removes at most one further dimension.  Therefore the
family claimed in `(L-91032.12)` still has codimension at least two.

Consequently:

\[
 \boxed{
 L\text{-}91032\text{ is false as stated.}
 }
\]

The proof of `T-91007` uses `L-91032` as its density step, so the claimed
fixed-scale equivalence is not established.

This does **not** show that the finite fixed-scale Gram is positive or negative
for actual zeta data.  It shows that its proposed implication to the full screw
form is invalid.

## 6. Repair direction

The obstruction is a common-zero obstruction.  It is removed by replacing one
scalar causal mother by an energy-preserving direct integral of its positive
delays.  No nonzero distribution can then place all its jump mass
simultaneously on the zero set of every delayed copy.  This repair is carried
out in `L-91034`.

## 7. Verification

The retained regression checks:

```text
exact Laplace partial fraction identity;
outward sign intervals at 31/20 and 8/5;
root localization;
quadrature of the hidden-jump orthogonality for five carriers;
scale covariance and delayed-copy diagnostics.
```

It returns

```text
PASS_CORRECTED_FOCK_HARDY_COMPLETION
```

The interval signs and the endpoint calculation prove the refutation.  The
quadrature is only a replay.

## 8. Exact boundary

```text
scalar causal half-line form core                 FALSE
one-bridge global fixed-scale form core           FALSE
T-91007 fixed-scale equivalence proof              BLOCKED
interior impulse zero and jump defect              EXACT
delay-fibre repair                                 PROPOSED COMPLETE in L-91034
unconditional delayed cross-Gram positivity        OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVED
```
