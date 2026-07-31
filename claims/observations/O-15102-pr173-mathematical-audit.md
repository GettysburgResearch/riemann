# O-15102 — Mathematical audit of PR #173

Claim ID: `O-15102`  
Status: **AUDIT; MIXED VERDICT**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Scope: theorem-level review of `claude/agentic-polymath-riemann-jjj23a`; no large computation rerun  
Related counterexample candidates: none

## 1. Claims that survive

### A. The target normalization has a factor `1/4`

For

\[
 h(x)=\frac\pi2x^2(2\pi x^2-3)e^{-\pi x^2},
 \qquad
 k(u)=u^{1/2}\sum_{n\ge1}h(nu),
\]

the Mellin transform is

\[
 \int_0^\infty h(v)v^{s-1}\,dv
 =\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2).
\]

Therefore

\[
 \boxed{
 \widehat k(z)=\frac14\Xi(z).}
\]

The correction to `L-15101.7` is valid. It is harmless for zeros but must be retained in absolute error budgets. One may instead replace the source by `4h` and the radical target by `4k` to recover transform exactly `Xi`.

### B. The CvS entries are Fourier coefficients

For the integer-node finite Fourier theorem, the target vector consists of Fourier coefficients of a compactly supported finite Fourier sum. After centering the support interval, the coefficient adapter contributes the factor `(-1)^j`. The finite transform is the windowed cardinal function

\[
 2e^{-iz/2}\sin(z/2)
 \sum_{j=-N}^{N}\frac{p_j}{z-2\pi j},
\]

not the unwindowed exponential sum. The three-node adjudication in `O-16001` is correct.

### C. Gap parity gives a valid lower bound

For

\[
 R(s)=\sum_i\frac{p_i}{\lambda_i-s},
\]

the endpoint pole signs show that the number of zeros in a node gap has odd parity when adjacent residues have the same sign and even parity when they have opposite signs. Hence every same-sign gap contains at least one real root.

The one-signed interlacing corollary is also correct.

### D. A canonical Loewner completion exists in the simple-real-root case

The matrix of divided differences of `-P'/P` is a canonical special completion. Its exact inertia and parity are proved, with the missing global-congruence step repaired, in `L-15111`.

### E. The precision warning is justified

Polynomial root and inertia decisions in this problem can be catastrophically ill-conditioned. Ordinary `float64` roots have no evidentiary status. Exact algebraic or directed interval gates are required.

## 2. Claims requiring correction

### A. The classical-kernel scaling displayed in `L-16001(e)` is internally off by four

PR #173 defines

\[
 \Phi_{\rm cl}(u)=2K(2u).
\]

But `hat K(z)=Xi(z)/4` implies directly

\[
 \begin{aligned}
 2\int_0^\infty\Phi_{\rm cl}(u)\cos(zu)\,du
 &=4\int_0^\infty K(2u)\cos(zu)\,du\\
 &=2\int_0^\infty K(t)\cos(zt/2)\,dt\\
 &=\frac14\Xi(z/2).
 \end{aligned}
\]

Thus the simultaneously displayed assertion

\[
 \Xi(z/2)=2\int_0^\infty\Phi_{\rm cl}(u)\cos(zu)\,du
\]

is false for that definition. Either the right side needs a factor `4`, or the kernel called classical must be multiplied by `4`. Imports from the de Bruijn--Newman literature should remain blocked until one source convention is fixed consistently.

### B. Squarefreeness is not automatic

Nonzero target coordinates imply `P(lambda_i)!=0`; they do not imply that `P` is squarefree. Any real-root/inertia theorem must retain squarefreeness or use a confluent formulation.

### C. The proof that each nonreal pair forces one negative eigenvalue was incomplete

An indefinite pair summand can be altered by addition of other summands. The exact count follows only after assembling the full real Cauchy factorization `Q=UJU^T` and proving `U` has full column rank. `L-15111` supplies that proof and obtains inertia `(r+c,c,1)`.

### D. Gap parity is not an exact root-distribution law

`L-16003(iv)` and the language “the failure mode is exactly Lehmer's phenomenon” overstate the theorem. The exact target

\[
 \lambda=(-1,0,1),
 \qquad
 p=(-1,3,-1)
\]

has no same-sign adjacent pair, but its polynomial is

\[
 P(s)=s^2-3,
\]

with two real roots. This also refutes the converse requested by Issue #174. See `R-15103`.

### E. Real-rootedness does not decide the one-scalar Finsler gate

`L-15108` concerns existence of an arbitrary positive special metric. The target-pinned family in `L-15107` is the much smaller source line

\[
 \beta\mapsto\beta-c\lambda.
\]

The exact four-node example in `R-15103` has a simple real-rooted target polynomial and a canonical PSD completion, but its scalar family for `Q=0` is infeasible. Therefore PR #173's census, even if fully rigorous for the intended target, would decide only arbitrary completion unless the actual Bézoutian thresholds are also checked.

### F. The leading-minor warning needs a precise predicate

Nonnegative leading principal minors are insufficient for PSD. However, for a symmetric matrix, strict positivity of every proper leading principal minor together with exact determinant zero **does** certify corank-one PSD. See `L-15112`. The claim that a singular matrix necessarily requires all principal minors is too broad.

## 3. The census does not evaluate the target it defines

The claim files define the exact coefficient as

\[
 p_j=(-1)^jF(2\pi j),
\]

where

\[
 F(z)=\int_{|t|\le1/(2\alpha)}\Phi(t)e^{i\alpha zt}\,dt
\]

or, for the smooth production cutoff, the analogous transform of `chi(t)Phi(t)`.

But `experiments/X-16002-cvs-sampled-target-census/exact_count.py` actually sets

```text
p_j = (-1)^j Xi(2*pi*alpha*j)
```

and never evaluates `F`. These are different objects. For the actual centered projection on `[-ell,ell]`,

\[
 p_n
 =\frac{(-1)^n}{\sqrt{2\ell}}
   \int_{-\ell}^{\ell}K(t)e^{-i\pi nt/\ell}\,dt,
\]

not the full transform sample

\[
 \frac{(-1)^n}{\sqrt{2\ell}}\widehat K(\pi n/\ell).
\]

Their difference is precisely the discarded localization tail. At the claimed threshold `alpha about 1.0644`, PR #173 itself describes this tail as a fixed nonnegligible fraction, so it cannot simultaneously be ignored in the census.

The sampled-`Xi` calculation is a useful **periodized/full-sample surrogate census**. It is not a production-target census and does not refute the cofinal repaired-target sequence.

## 4. The census is empirical, not certified for exact transcendental coefficients

The computation evaluates `Xi` with `mpmath`, rounds each value to a decimal rational, and then performs exact Sturm arithmetic on the rounded polynomial.

That proves the root count of the rational surrogate. Repeating the rounding at several decimal precisions is strong numerical evidence but is not an inclusion proof for the exact `Xi` values. A proof-grade result needs one of:

1. directed rectangles for every primitive followed by interval-safe inertia;
2. a coefficient error bound smaller than an exact root/inertia stability moat;
3. exact algebraic data.

The descriptions `CERTIFIED-COMPUTATIONAL`, “every decision exact,” and “first production-level pass” should therefore be downgraded. The large census need not be recomputed before the target and proof boundary are corrected.

## 5. Issue #175's density/localization route fails

Three steps in the issue are invalid.

1. Local-uniform limits do not preserve a common exponential-type bound without a uniform global growth estimate. Polynomial partial sums, all of type zero, converge locally uniformly to `e^z`.
2. Every finite CvS transform already has the uncancelled sine-lattice zeros `2*pi*m`, `|m|>N`. Its asymptotic zero density is therefore fixed by the support interval independently of the `2N` numerator roots.
3. The quotient roots need not remain in the diagonal node hull: `p=(-1,3,-1)` at nodes `(-1,0,1)` gives roots `+-sqrt(3)`.

Thus Levinson density does not conflict with a fixed local zero-free region, and the rank-one perturbation supplies no required localization. The satisfiability question remains open, but this proposed structural obstruction does not approach it.

## 6. What is worth retaining for the next attack

The most useful surviving interface is the canonical Loewner matrix, used correctly:

- it computes the exact number of nonreal pairs by inertia without root isolation;
- it automatically supplies parity for symmetric simple-root targets;
- it can be evaluated directly from `P,P',P''` at the nodes;
- it supplies a clean stability target for converting the sampled-`Xi` surrogate into the actual windowed target.

The next proof-grade computation should therefore not repeat the large root census. It should:

1. generate directed coefficients of the **actual windowed/smooth-cutoff target**;
2. assemble the canonical Loewner matrix with interval arithmetic;
3. certify its inertia or unresolved radius;
4. separately test the actual arithmetic scalar thresholds of `L-15109`.

These two outputs must not be conflated: canonical inertia decides arbitrary completion; threshold separation decides the one-scalar Weil completion.

## Current computational status

No additional workflow result or issue-#175 verdict is present on PR #173's head. The branch contains the reported nine commits and no GitHub Actions run associated with that head.