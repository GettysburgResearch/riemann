# Final saturation review packet

Agent: `gpt56-pro-global-01`  
Date: 2026-08-07  
Frozen starting head: `61c6f1129eb2848ce30750ec51c257945a7351c7`  
Status: **full proof proposal assembled; SAT remains open and is exactly RH-equivalent; no RH resolution is claimed**

## Executive verdict

The prime-annihilator programme now has a complete, noncancelling chain down to
one scalar inequality.  Every preceding analytic, entire-function, probability,
and line-zero factorization step has been separated from the final statement.

The sole missing assertion is

\[
\boxed{
\operatorname{Var}_{1/2}(\log Y)
\le
2\sum_{\xi(1/2+i\gamma)=0}
 \frac{m_\gamma}{\gamma^2},}
\tag{SAT}
\]

where

\[
Y=\sqrt{2/\pi}
 \left(\max b-\min b\right)
\]

is the normalized range of a standard Brownian bridge and the variance is under
the half-size-biased law.

The centered Hadamard product gives the opposite inequality and the exact defect

\[
\boxed{
\begin{aligned}
D_{\rm off}
={}&\operatorname{Var}_{1/2}(\log Y)
 -2\sum_{\gamma\in\Gamma_L}\frac{m_\gamma}{\gamma^2}\\
={}&4\sum_{(\delta,\gamma)\in\Gamma_O}
 m_{\delta,\gamma}
 \frac{\gamma^2-\delta^2}
      {(\gamma^2+\delta^2)^2}
\ge0.
\end{aligned}}
\tag{1}
\]

Every summand is strictly positive.  Consequently

\[
\boxed{\mathrm{SAT}\iff D_{\rm off}=0\iff\mathrm{RH}.}
\tag{2}
\]

No independent proof of SAT was obtained.  This report records the complete
proposal for review and proves a new exact convex-order/martingale budget for all
known line-zero factors.

---

## A. Exact chain of claims

### A1. Brownian Mellin law

Biane--Pitman--Yor prove

\[
\mathbb E[Y^s]=2\xi(s)
\qquad(s\in\mathbb C).
\tag{3}
\]

Under the half-size bias

\[
\frac{d\mathbb P_{1/2}}{d\mathbb P}
 =\frac{Y^{1/2}}{\mathbb E[Y^{1/2}]},
\]

put `Z=log Y`. Then

\[
\mathbb E_{1/2}[e^{itZ}]
 =\frac{\xi(1/2+it)}{\xi(1/2)}
 =:\Xi(t).
\tag{4}
\]

The functional equation makes `Z` symmetric, and

\[
\operatorname{Var}_{1/2}(Z)
 =\frac{\xi''(1/2)}{\xi(1/2)}.
\tag{5}
\]

### A2. Centered canonical product

Let

\[
X(w)=\xi(1/2+w).
\]

Group the zeros of `X` into critical-line pairs

\[
w=\pm i\gamma
\]

and off-line quartets

\[
w=\pm\delta\pm i\gamma.
\]

The symmetric order-one canonical product gives

\[
\begin{aligned}
\Xi(t)
={}&\prod_{\gamma\in\Gamma_L}
 \left(1-\frac{t^2}{\gamma^2}\right)^{m_\gamma}\\
&\times
\prod_{(\delta,\gamma)\in\Gamma_O}
 \left(1-\frac{t^2}{(\gamma-i\delta)^2}\right)^{m_{\delta,\gamma}}
 \left(1-\frac{t^2}{(\gamma+i\delta)^2}\right)^{m_{\delta,\gamma}}.
\end{aligned}
\tag{6}
\]

Twice differentiating the logarithm at zero gives (1).  Since every nontrivial
ordinate exceeds `14` and `0<delta<1/2`, every quartet term is strictly positive.

### A3. Uniform/cosine-bell line factors

For each actual critical-line ordinate define

\[
U_\gamma(t)=\frac{\sin(\pi t/\gamma)}{\pi t/\gamma}
\tag{7}
\]

and

\[
C_\gamma(t)=
 \frac{\sin(\pi t/\gamma)}
 {\left(\pi t/\gamma\right)(1-t^2/\gamma^2)}.
\tag{8}
\]

These are characteristic functions of, respectively,

- the centered uniform law on `[-pi/gamma,pi/gamma]`;
- the cosine-bell density proportional to `1+cos(gamma x)` on that interval.

They obey

\[
U_\gamma(t)
 =\left(1-\frac{t^2}{\gamma^2}\right)C_\gamma(t).
\tag{9}
\]

The multiplicity-weighted infinite convolutions `mu_U,mu_C` exist in `L2` and
satisfy

\[
\mathrm{RH}
\iff
\mu_\Xi*\mu_C=\mu_U.
\tag{10}
\]

Variance equality in (10) is exactly SAT.  Conversely, the sign-definite defect
(1) shows that variance equality already forces the full convolution identity
and RH.

### A4. Corrected prime annihilator

The centered infinite-notch limit is two-sided.  Its exact prime functional must
contain both

\[
G(x-\log n)
\quad\text{and}\quad
G(x+\log n).
\]

After the complete archimedean subtraction, the corrected Guinand--Weil residual
`R_infty` has only nontrivial-zero terms.  Its notch product kills every
critical-line zero and no point with nonzero real part.  Subject to independent
normalization review,

\[
R_\infty\equiv0
\iff\mathrm{RH}.
\tag{11}
\]

This is a prime-side realization of the same off-line canonical factor.  The
short scalar proof through SAT does not require (11).

### A5. Gamma-convolution and perpetuity forms

Biane--Pitman--Yor also give

\[
\Sigma_2=\frac2{\pi^2}
 \sum_{n\ge1}\frac{\Gamma(2)_n}{n^2}
\overset d=\frac2\pi Y^2.
\tag{12}
\]

Thus SAT is equivalently

\[
\operatorname{Var}^{\Sigma}_{1/4}
 (\log\Sigma_2)
\le
8\sum_{\gamma\in\Gamma_L}\frac{m_\gamma}{\gamma^2}.
\tag{13}
\]

The ordinary size-biased variable satisfies the explicit BPY perpetuity

\[
\Sigma_2^*\overset d=
\Sigma_2+H\Sigma_2^*,
\tag{14}
\]

with independent variables and density

\[
\mathbb P(H\in dh)=(h^{-1/2}-1)dh,
\qquad0<h<1.
\tag{15}
\]

Equations (12)--(15) supply a concrete stochastic operator for a proposed proof.
They do not by themselves imply SAT.

---

## B. New theorem: the complete line-zero martingale budget

Let

\[
a=\pi/\gamma.
\]

For `0<=r<=a`, the uniform and cosine-bell tails satisfy

\[
\mathbb P(|U_\gamma|>r)=1-r/a,
\tag{16}
\]

\[
\mathbb P(|C_\gamma|>r)
 =1-r/a-\pi^{-1}\sin(\pi r/a).
\tag{17}
\]

Therefore

\[
|C_\gamma|\preceq_{\rm st}|U_\gamma|.
\tag{18}
\]

Because both laws are symmetric and centered, this implies

\[
\boxed{C_\gamma\preceq_{\rm cx}U_\gamma.}
\tag{19}
\]

Their exact variance gap is

\[
\boxed{
\operatorname{Var}(U_\gamma)
-
\operatorname{Var}(C_\gamma)
=2/\gamma^2.}
\tag{20}
\]

Convex order is preserved by independent convolution and square-integrable
limits.  Hence, for the complete line-zero sums,

\[
\boxed{C\preceq_{\rm cx}U,}
\tag{21}
\]

\[
\boxed{
\operatorname{Var}(U)-\operatorname{Var}(C)
=2\sum_\gamma m_\gamma/\gamma^2.}
\tag{22}
\]

By factorwise Strassen couplings, there is a canonical global martingale
reservoir

\[
\boxed{\mathbb E[U\mid C]=C.}
\tag{23}
\]

The Brownian completion theorem needed for SAT is

\[
\boxed{Z+C\preceq_{\rm cx}U,}
\tag{24}
\]

or equivalently a coupling satisfying

\[
\boxed{\mathbb E[U\mid Z+C]=Z+C.}
\tag{25}
\]

Testing `x^2` in (24) gives SAT.  Conversely, the positive quartet defect forces
variance equality, so (24), (25), SAT, and RH are equivalent.

A one-parameter equivalent formulation is the stop-loss family

\[
\boxed{
\mathbb E[(Z+C-r)_+]
\le
\mathbb E[(U-r)_+]
\quad(r\in\mathbb R).}
\tag{26}
\]

This is the most concrete final review target produced in this pass.

---

## C. Why the attempted shortcuts fail

### C1. Characteristic-function positivity

For `1/2<a<1`,

\[
\phi(t)=a+(1-a)\cos(bt)
\]

is an even entire characteristic function, strictly positive on the real axis,
but with nonreal zeros.  Multiplying it by a sinc power produces a compactly
supported smooth law whose transform has infinitely many real zeros and
additional nonreal zeros.

Therefore

```text
probability law + symmetry + entire transform + many real zeros
```

does not imply SAT.

### C2. Reciprocal size-bias symmetry

Any symmetric log-density can be untilted to a positive variable whose
half-size-biased logarithm has that density.  The BPY reciprocal symmetry is not
alone restrictive enough to force real zeros.

### C3. Additive GGC structure

`Sigma_2` is an additive generalized gamma convolution.  SAT concerns the
Fourier transform of its logarithm under a fractional size bias.  There is no
general implication from additive GGC structure to `PF_infinity`, total
positivity of the log law, or real-rootedness of the Mellin transform.

### C4. Factorwise convex order

The proved comparison is `C <=cx U`; the target is `Z+C <=cx U`.  Adding an
independent nondegenerate `Z` increases spread.  No convolution closure turns
the first comparison into the second.

### C5. Finite verified height

A hypothetical quartet at ordinate `T` contributes

\[
4m/T^2+O(T^{-4})>0.
\]

Thus a finite zero table makes the defect extremely small but cannot make it
exactly zero.

### C6. Log-concavity or `TP_2`

SAT is a full real-zero or `TP_infinity` conclusion.  Low-order total positivity
and strict log-concavity do not supply the missing all-orders property.

---

## D. Exact proof ledger for the reviewing agent

| Unit | Statement | Current status |
|---|---|---|
| P1 | BPY Brownian Mellin identity | imported theorem |
| P2 | Half-tilted log-range has CF `Xi` and variance `xi''/xi` | exact consequence |
| P3 | Symmetric centered Hadamard product | standard entire-function algebra |
| P4 | Positive off-line quartet defect (1) | exact, proposed pending review |
| P5 | Uniform/cosine-bell transforms and infinite convolution | exact |
| P6 | Factorwise and infinite convex order `C <=cx U` | exact new theorem |
| P7 | Corrected two-sided completed prime residual | proposed normalization review |
| P8 | Brownian completion `Z+C <=cx U`, equivalently SAT | **open** |
| P9 | P4 + P8 imply RH | immediate |

The short proposed RH proof is therefore

\[
\boxed{
\text{BPY}
\to
\text{positive quartet defect}
\quad+\quad
\text{independent proof of SAT}
\to
\mathrm{RH}.}
\tag{27}
\]

There is no additional finite-to-global step after SAT.

---

## E. Circularity rejection list

A reviewer should reject any purported proof of SAT that imports any of the
following under another name:

1. `Xi` belongs to the Laguerre--Polya class;
2. the xi kernel is `PF_infinity` or totally positive of all orders;
3. the complete central Hausdorff hierarchy is nonnegative;
4. the xi scattering ratio is inner or its Hankel defect vanishes;
5. the centered reciprocal xi function has a positive Thorin/GGC
   representation;
6. the off-line canonical factor is constant;
7. the corrected annihilator residual is zero;
8. finite verified-height near saturation is exact equality.

Items 1--7 are already RH-equivalent.  Item 8 loses the global quantifier.

---

## F. Requested independent attacks

1. **Brownian path coupling.** Construct (25) from an excursion decomposition of
the bridge range.
2. **Gamma perpetuity transport.** Derive the stop-loss inequalities (26) from
(14)--(15) under the quarter-size bias.
3. **Direct stop-loss computation.** Use the explicit theta density of `Z` and
the convergent uniform/cosine convolutions to prove (26).
4. **Arithmetic endpoint.** Prove the corrected two-sided completed prime
identity directly; by the positive defect it implies SAT.
5. **Adversarial audit.** Recheck every factor of two, multiplicity convention,
and canonical-product sign in (1).

## Final status

The contribution does not prove SAT.  It proves that SAT is exactly the last
step, gives a complete reviewable RH chain, proves a new exact martingale budget
for every critical-line factor, and excludes the main generic-probability
shortcuts.

Any valid proof of (24), (25), (26), or SAT completes the proposed RH proof
immediately.