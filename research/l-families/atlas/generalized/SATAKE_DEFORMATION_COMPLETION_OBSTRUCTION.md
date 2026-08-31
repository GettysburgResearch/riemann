# A fixed-parameter completion obstruction for a Satake deformation

Status: proposed reviewable mathematics; exact finite controls, not yet integrated.
Programme: #764 generalized L-objects; independent prime-deformation axis.
Identity: `GLO764.SATAKE_FIXED_PARAMETER_NONMEROMORPHY_V1`.
Scope: every fixed real `0 < |epsilon| <= 1`; failure of meromorphic continuation
at `s=1` for an all-prime rank-three Euler product built from actual Delta data.
No novelty claim, RH implication, new automorphic object, or natural-boundary claim.

The parent coefficient-power/finite-graded notes are unchanged. Their frozen
context is `e2f469142cd55086e74751293877ab533001e786`; none of their mathematical
results is a premise here. This is a different diagnostic: many good local
properties survive a deformation, while a global completion gate fails.

## 1. Inputs and exact theorem

Let `Delta(q) = q product_(n>=1) (1-q^n)^24 = sum tau(n) q^n`, the normalized
weight-12 level-one cusp form. We import precisely these arithmetic facts:

- **D1 (unitarity).** Deligne's Theorem (8.2), printed p.302, gives the absolute
  values `p^(11/2)` of the two roots of `X^2-tau(p)X+p^11`. Thus choose
  `theta_p in [0,pi]` with `tau(p)=2 p^(11/2) cos(theta_p)`.
- **D2 (actual-Delta Sato--Tate).** Barnet-Lamb--Geraghty--Harris--Taylor,
  Corollary C, printed p.32, gives semicircle equidistribution of
  `tau(p)/(2p^(11/2))`. Equivalently, for every continuous `f` on `[0,pi]`,
  `pi(x)^(-1) sum_(p<=x) f(theta_p)` tends to
  `(2/pi) integral_0^pi f(theta) sin(theta)^2 dtheta`.

D2 is explicitly a theorem about Delta, so this application does not require
an additional unproved non-CM assertion. There are no bad finite primes at level
one. No numerical tau table, effective Sato--Tate rate, PNT estimate, GRH, or
uniformity in epsilon is imported. Primary references and locators are in §8.

Set `phi_p=2 theta_p` and choose the conjugacy class

\[
 A_p=\operatorname{diag}(e^{i\phi_p},1,e^{-i\phi_p}),\qquad
 T_\epsilon(A)=A\exp\!\left(\frac\epsilon2(A^3-A^{-3})\right).
\]

For real epsilon its eigenvalues are `1, exp(i psi), exp(-i psi)`, where
`psi=phi+epsilon sin(3phi)`. Define initially for `Re s>1`

\[
 L_\epsilon(s)=\prod_p\det(I-T_\epsilon(A_p)p^{-s})^{-1}.
\]

**Theorem.** For every fixed real `0<|epsilon|<=1`, this product is a nonzero
holomorphic function on `Re s>1` but has no meromorphic continuation to any
neighborhood of `s=1`. More precisely, with

\[
 a(\epsilon)=1-\frac1{2\pi}\int_0^{2\pi}
                 \cos(\epsilon\sin(3\phi))\,d\phi,
\]

\[
 \frac{\epsilon^2}{4}-\frac{\epsilon^4}{64}
 \leq a(\epsilon)\leq\frac{\epsilon^2}{4},\qquad
 \lim_{\sigma\downarrow1}
 \frac{\log L_\epsilon(\sigma)}{\log(1/(\sigma-1))}=a(\epsilon)\in(0,1).
\]

For every nonzero meromorphic multiplier germ `M` at `1`, the product
`M(s)L_epsilon(s)` also has no meromorphic continuation there. This includes
finite ordinary gamma quotients, rational factors, and exponential conductor
factors. The assertion is pointwise for **each** epsilon, not merely an
obstruction to a jointly differentiable family of completions.

## 2. What survives locally

Functional calculus makes `T_epsilon` conjugation-equivariant. On unitary
representatives of the specified inverse-pair-plus-one class,
`G=(A^3-A^(-3))/2` is skew-Hermitian and traceless;
it commutes with `A`. Hence `T_epsilon(A)` is unitary and has determinant one for
real epsilon. Direct substitution gives
`T_epsilon(A^(-1))=T_epsilon(A)^(-1)` and, after transposing,
`T_epsilon(A^(-T))=T_epsilon(A)^(-T)`. These are inverse and contragredient
compatibility, not tensor or twist functoriality. The determinant-one assertion
is not made for arbitrary determinant-one matrices: `diag(2,3,1/6)` is an exact
countercontrol, with nonzero `trace(G)`.

Write `c=cos(psi)`, `t=1+2c`. The local denominator is

\[
 (1-X)(1-2cX+X^2)=1-tX+tX^2-X^3.
\]

It has degree three and reciprocal unitary parameters. For real `0<X<1` it is
positive, since `1-2cX+X^2=(1-X)^2+2(1-c)X>0`. The inverse local series has
coefficients `h_r` with `|h_r|<=binomial(r+2,2)`: it is the complete homogeneous
symmetric polynomial in three unit-modulus parameters. Consequently its
multiplicative global coefficients have absolute Dirichlet series bounded by
`zeta(sigma)^3` for `sigma>1`.

Also `|trace(T_epsilon(A_p)^k)|<=3`, so

\[
 \log L_\epsilon(s)=\sum_p\sum_{k\geq1}
       \frac{\operatorname{tr}(T_\epsilon(A_p)^k)}{k p^{ks}}
\]

converges absolutely, locally uniformly on `Re s>1`. Its exponential equals
the Euler product and never vanishes there. Positive real local factors show
that this logarithm is the ordinary real logarithm when `s=sigma>1`.

At epsilon zero the local data are those of normalized `Sym^2 Delta`.
The nonzero-epsilon proof does not require continuation at epsilon zero.
These properties do not supply an arithmetic realization, integrality,
ramified local theory, an archimedean factor, or a functional equation.

## 3. Exact Sato--Tate mean: why frequency three works

The substitution `phi=2theta` pushes the Sato--Tate measure to

\[
 d\nu(\phi)=\frac{1-\cos\phi}{2\pi}\,d\phi
       \quad(0\leq\phi\leq2\pi).
\]

Denote uniform circle average by `E`. For `j=1,2`, shifting phi by `2pi/3`
multiplies `exp(ij phi+i epsilon sin(3phi))` by a nontrivial cube root of unity.
Its integral is unchanged by the shift, hence its mean is zero. This is an
exact identity for every real epsilon, not a truncated Taylor calculation.
Using `2 cos(phi) cos(psi)=cos(epsilon sin(3phi))+
cos(2phi+epsilon sin(3phi))` now gives

\[
 \int(1+2\cos(\phi+\epsilon\sin3\phi))\,d\nu
       =1-E\cos(\epsilon\sin3\phi)=a(\epsilon).
\]

The last average is often denoted `J_0(epsilon)`; no Bessel-function result is
needed. Since the trace is a fixed continuous function of phi, D2 gives

\[
 \sum_{p\leq x}(\operatorname{tr}T_\epsilon(A_p)-a(\epsilon))=o(\pi(x))
\]

for each fixed epsilon. There is no interchange of an epsilon derivative with
this limiting statement.

For completeness, for every real x,
`x^2/2-x^4/24 <= 1-cos(x) <= x^2/2`. Indeed,
`1-cos(x)=integral_0^|x| (|x|-u) cos(u) du`; using `cos(u)<=1` proves the
upper bound, hence `cos(u)>=1-u^2/2`, which inserted into the same integral
proves the lower bound. The exact circle means
`E sin(3phi)^2=1/2` and `E sin(3phi)^4=3/8` yield the theorem's bounds.
For `0<|epsilon|<=1` the lower bound is at least `15 epsilon^2/64>0`, and
the upper bound is at most `1/4<1`. Also `a(0)=0` and `a(-epsilon)=a(epsilon)`.

## 4. Qualitative equidistribution suffices: full Abel argument

**Lemma.** Suppose bounded real numbers `b_p` satisfy
`B(x)=sum_(p<=x)b_p=o(pi(x))`. Then, as real `sigma` decreases to one,

\[
 \sum_p b_p p^{-\sigma}=o\!\left(\log\frac1{\sigma-1}\right).
\]

**Proof.** Put `P(sigma)=sum_p p^(-sigma)`. Partial summation, with initial
value zero at `2^-`, gives

\[
 \sum_p b_p p^{-\sigma}
      =\sigma\int_{2^-}^{\infty}B(x)x^{-\sigma-1}\,dx.
\]

The terminal term vanishes since `B(x)=O(pi(x))=O(x)` and `sigma>1`.
For any `delta>0`, choose `X_delta` so that `|B(x)|<=delta pi(x)` for
`x>=X_delta`. The initial integral is `O_(X_delta)(1)`, uniformly for
`1<sigma<=3/2`; the tail is at most
`delta sigma integral_(2^-)^infinity pi(x)x^(-sigma-1) dx=delta P(sigma)`.

No PNT is needed to evaluate P. Integral comparison of the decreasing function
`x^(-sigma)` gives `zeta(sigma)=1/(sigma-1)+O(1)`. Its absolutely convergent
Euler logarithm gives `log zeta(sigma)=P(sigma)+O(1)`, because, for `sigma>=1`,

\[
 \sum_p\sum_{k\geq2}\frac{p^{-k\sigma}}k
 \leq\sum_p\frac{p^{-2\sigma}}{1-p^{-\sigma}}
 \leq2\sum_{n\geq2}n^{-2}<\infty.
\]

Thus `P(sigma)=log(1/(sigma-1))+O(1)` tends to infinity. Divide the preceding
Abel bound by P, take the limsup, and then let delta tend to zero. This proves
the lemma with no rate assumption. QED.

Apply the lemma with `b_p=trace(T_epsilon(A_p))-a(epsilon)`. The `k>=2`
part of `log L_epsilon` is bounded in absolute value by
`6 sum_(n>=2)n^(-2)`, uniformly for real epsilon and `sigma>=1`.
The `k=1` term is `a(epsilon)P(sigma)+o(P(sigma))`. This proves the displayed
logarithmic limit. It does **not** prove a nonzero constant-times asymptotic,
an algebraic branch-germ description, or any epsilon-uniform boundary limit.

## 5. Integer-order contradiction and limits of the conclusion

Suppose a meromorphic germ F at one agrees with `L_epsilon` on its intersection
with `Re s>1`. It is not identically zero. Laurent factorization gives
`F(s)=(s-1)^m h(s)` with integer m and h holomorphic, `h(1)!=0`. On the real
right-hand interval,

\[
 \log L_\epsilon(\sigma)=\log|F(\sigma)|
       =m\log(\sigma-1)+O(1).
\]

The logarithmic limit must therefore be `-m`, an integer, contradicting
`0<a(epsilon)<1`. If a nonzero meromorphic germ M made `M L_epsilon`
meromorphic, division by M would make `L_epsilon` meromorphic as well, the
same contradiction. Zeros and poles of M at one do not evade division.
Identically zero multipliers and nonmeromorphic fractional powers are excluded.

This is a meromorphic-completion failure at one, not a theorem that all
locally unitary deformations fail. It says nothing about other epsilons,
possible continuation elsewhere, zero distributions, natural boundaries,
or RH. It makes no first-order functional-equation obstruction claim: the
mean has zero linear term and a positive quadratic term. A worthwhile next
question would impose preservation of the prime trace mean before testing
other completion constraints; this packet does not solve that question.

## 6. Exact bounded replay and held-out controls

`satake_deformation_completion_obstruction.py` uses only Python's standard
library and exact `Fraction` arithmetic. The default fixture checks all formal
degrees `0..12`; the public bounded range is `2..24`. It verifies:

- cube-root cancellation for phase modes 1 and 2 against frequency 3;
  formal Laurent constant terms through the declared order; wrong-frequency
  and divisible-mode negative controls;
- rational mean coefficients against the independent closed formula
  `a_(2j)=(-1)^(j+1)/(4^j (j!)^2)`, odd coefficients zero;
  exact even sine moments and the two rational Taylor-bound polynomials;
- epsilon zero and signed rational epsilon pairs; held-out `+/-7/11` in tests;
- rational SO(3) matrices, generator skewness/tracelessness/commutation,
  conjugation and inverse compatibility; a generic SL(3) determinant warning;
- local denominator, positive rational evaluations, inverse-series recurrence
  versus a separate quadratic-factor convolution, and coefficient majorants.

These are synthetic angle/formal controls, **not sampled Delta primes**, and
not a finite verification of Sato--Tate, convergence, or the infinite theorem.
The all-order shift proof, analytic estimates, and germ argument are native
written mathematics; D1 and D2 remain imported arithmetic theorems.

Arithmetic class: `MIXED`, consisting of `EXACT_RATIONAL` and
`CERTIFIED_INTEGER_COVERAGE`; no floating-point rounding occurs. Public scalar
inputs reject bool, float, and strings. Rational inputs have a 128-bit cap;
series order, frequency, phase, and file sizes have explicit preflight bounds.
The declared conservative work majorant must be **strictly below** the selected
work cap. This is a bounded replay contract, not a performance theorem.

The checker authenticates the frozen context blob against Git and its LF SHA256,
checks the current context bytes, pins the external-source declarations, records
LF hashes of note/producer/tests/manifest, regenerates the complete fixed corpus,
and compares typed canonical JSON exactly. Duplicate keys, NaN/Infinity,
oversized files, changed data, changed artifact hashes, bool/int substitutions,
or a mismatched payload digest fail. Validation does not depend on `assert`.
External PDFs are identified but are **not** downloaded or machine-proved by
the offline checker. A declared primary-source URL is not a proof certificate.

Replay from the repository root:

```text
python -B research/l-families/atlas/generalized/satake_deformation_completion_obstruction.py --check
python -B -O research/l-families/atlas/generalized/satake_deformation_completion_obstruction.py --check
python -B -m unittest discover -s tests -p test_satake_deformation_completion_obstruction.py
python -B -O -m unittest discover -s tests -p test_satake_deformation_completion_obstruction.py
```

`--write` regenerates only the declared fixture, after source authentication.
The checked-in fixture is not a numerical or independently formalized proof.
Preparation replay: the default checker passed with and without Python `-O`;
all 20 unit tests passed in both modes, including maximum order 24, fixture and
source tampering, and simulated CRLF checkout replay. Ruff format/check passed.
These are author-run results; exact-frozen-SHA independent review is a separate
step and is not claimed by this record.
The smallest mathematical failure that would invalidate the application is a
wrong pushed Sato--Tate mean or a failure of the stated fixed-epsilon Abel
passage; both are proved explicitly above and require independent review.

## 7. Relationship to the programme

At epsilon zero the standard symmetric-square local object supplies a control.
Every nonzero epsilon in the stated interval preserves the named local
properties but fails a necessary global meromorphy gate. Thus arbitrary
conjugation-equivariant unitary prime-local functional calculus is too broad a
definition of generalized completable L-objects. This is a diagnostic exclusion
of one explicit family, not a classification of the remaining moduli space.
The calculation does not certify a new programme as novel or unexplored.

## 8. Primary sources and import boundary

1. Pierre Deligne, *La conjecture de Weil : I*, Publ. Math. IHES 43 (1974),
   273--307, Theorem (8.2), printed p.302 (PDF page 31),
   [primary PDF](https://www.numdam.org/article/PMIHES_1974__43__273_0.pdf),
   DOI `10.1007/BF02684373`. Imported only for D1, not as a source of this
   deformation or its obstruction.
2. Tom Barnet-Lamb, David Geraghty, Michael Harris, Richard Taylor,
   *A Family of Calabi--Yau Varieties and Potential Automorphy II*, Publ. RIMS
   47 (2011), 29--98, Corollary C, printed p.32 (PDF page 4),
   [publisher page](https://ems.press/journals/prims/articles/4468),
   [primary PDF](https://ems.press/content/serial-article-files/41128?nt=1),
   DOI `10.2977/PRIMS/31`. Imported only for the actual-Delta qualitative
   distribution D2. Its deep proof is not reproduced here.

No external result is claimed as new. The packet's contribution is the explicit
deformation, its bounded exact control record, and the written application of
the elementary noninteger-log-order test under these imported hypotheses.
