# Final consolidation — weighted shell-tail stability

**Agent:** `gpt56-pro`  
**Date:** 2026-08-08  
**Repository:** `gfreund123/riemann`  
**Branch:** `research/gpt56-pro-275-final-wsts-consolidation`  
**Frozen base:** PR #240 at `58c70a81dce76cd84ea50a60c15c227537f240c1`  
**Status:** **REVIEW-READY CONSOLIDATION; ONE RH-EQUIVALENT THEOREM UNPROVEN**  
**RH:** **UNPROVEN**

## 1. Executive conclusion

The elementary carry programme is now consolidated to one exact finite scalar:

\[
\mathcal B_X
=
\max_{2\le z\le X}
\left[
\sum_{z\le p\le X}
(\log p)
\left(
r_X(p)-\mathbf1_{p\le\lfloor X/2\rfloor}
 r_{\lfloor X/2\rfloor}(p)
\right)
\right]_+.
\]

The final theorem is

\[
\forall\varepsilon>0,
\qquad
\mathcal B_X=O_\varepsilon(X^\varepsilon).
\tag{WSTS}
\]

The consolidation proves, subject to review of the stated exact dependencies,

\[
\boxed{
\mathrm{WSTS}\Longleftrightarrow\mathrm{RH}.}
\]

The new reverse implication is quantitative:

\[
\boxed{
\mathrm{RH}\Longrightarrow
\mathcal B_X=O(\log^4X).}
\]

This settles the status question.  The surrounding geometry really is close to
complete, but the last prime-sampling assertion is not a routine transfer.  It
is exactly as strong as RH.

No accepted proof of RH is present in the live graph.

## 2. Why this consolidation was necessary

After PR #265, many branches appeared to be one short estimate away from
completion:

```text
endpoint-scale blocker control;
prime-tail queue;
prime-tail charge;
fifth-scale digital–Green recurrence;
factor-five physical transition contraction;
finite arithmetic Green deformation;
annular dual frame;
boundary-jet domination;
parity–Green coercivity.
```

Each branch made genuine exact advances.  The resulting collection could give
the impression that several independent routes now jointly cover the final
step.

They do not.  Their open conclusions all estimate, transport, or repackage the
same logarithmic prime discrepancy.  Equivalences and finite geometric
constructions cannot be concatenated into an inequality unless one branch
actually proves its cofinal quantitative theorem.

The present packet chooses the most economical scalar and removes every other
open theorem from the load-bearing proof spine.

## 3. The common exact foundation

### 3.1 Average-binomial carries

For

\[
\beta_{nq}
={\lfloor n/q\rfloor(q-1-(n\bmod q))\over n+1},
\]

Kummer and Legendre give

\[
G_n
={1\over n+1}\sum_{j=0}^n\log\binom nj
=
\sum_{q=p^a\le n}\Lambda(q)\beta_{nq}.
\]

Thus every nonnegative feasible carry vector gives a positive lower certificate
for the complete prime-power ramp.

### 3.2 Sharp parabolic seed

The parabolic seed

\[
b_X(m)
=2\sqrt m
\left[
\log(X/m)-2(1-\sqrt{m/X})
\right]
\]

has objective

\[
J_X(b_X)
\ge4\sqrt X-6\log X+O(1).
\]

PR #265 proves that the seed is already nonnegative in the original carry-row
coordinates.  Its endpoint increments are also nonnegative.  Positivity of the
physical finite object is therefore not the final obstruction.

### 3.3 Continuum tail order

For the continuum response defect `E`, PR #265 proves

\[
\int_\theta^1E(u)du\le0.
\]

PR #240 strengthens this.  With

\[
J(\theta)={1\over\sqrt\theta}
\int_\theta^1E(u)du,
\]

one has

\[
J'(\theta)
={2\over\theta^{3/2}}
[N\theta+1-(S_N+1)\sqrt\theta]
\ge0
\]

inside every reciprocal cell.  Therefore every fixed-ratio shell

\[
E_c(\theta)
=E(\theta)-c^{-1/2}E(\theta/c)\mathbf1_{\theta\le c}
\]

has nonpositive upper tails.  Below half scale there is a quantitative moat

\[
H_c(\theta)
\le-{1\over5}\sqrt\theta\log(1/c).
\]

### 3.4 Finite floor decomposition

PR #240 proves uniformly

\[
r_X(q)
=X^{-1/2}E(q/X)
+O\left(q^{-3/2}[1+\log(X/q)]\right).
\]

At two endpoints this becomes

\[
s_{X,Y}(q)
=X^{-1/2}E_{Y/X}(q/X)
+\epsilon_{X,Y}(q),
\]

where the logarithmically weighted floor error is absolutely summable.

### 3.5 Exact prime sampling remainder

Writing

\[
R(t)=\vartheta(t)-t,
\]

Stieltjes summation gives

\[
\begin{aligned}
X^{-1/2}
\sum_{z\le p\le X}(\log p)E_c(p/X)
={}&
\sqrt X H_c(z/X)\\
&+X^{-1/2}
\int_{[z,X]}E_c(t/X)dR(t).
\end{aligned}
\]

The first term is nonpositive.  The second is the complete arithmetic sampling
remainder.  There is no additional operator, endpoint face, or unrecorded
packet.

### 3.6 Exact weighted transport

If every logarithmically weighted upper tail of a prime residual is nonpositive,
PR #240 constructs an exact zero-objective-cost transport from every positive
atom into later negative slack.  For a general residual, the least one-boundary
charge is exactly the maximum positive weighted upper tail.

Therefore `mathcal B_X` is not merely an estimate suggested by the continuum.
It is the exact loss of the finite proof-producing transport.

## 4. The consolidated forward proof

Assume `WSTS`.

Let

\[
X_0=X,
\qquad
X_{j+1}=\lfloor X_j/2\rfloor.
\]

For every dyadic shell:

1. the continuum component has nonpositive weighted upper tails;
2. the finite discrepancy is charged by `mathcal B_(X_j)`;
3. exact incidence blocks make the shell feasible;
4. the objective loses at most that charge;
5. the endpoint shell sources telescope.

For any fixed `eta>0`, apply `WSTS` with exponent `eta/2`:

\[
\sum_j\mathcal B_{X_j}
\ll_\eta
\sum_jX_j^{\eta/2}
\ll_\eta X^{\eta/2}.
\]

The corrected parabolic object therefore has ordinary-prime objective

\[
P_X
\ge4\sqrt X-O_\eta(X^\eta).
\]

Proper prime powers differ by only `O(log^2 X)`.  Hence the complete prime-power
ramp obeys the same estimate.

At `X=N^2`, the square-screw formula has exact archimedean main term `4N`.  The
prime-ramp lower bound gives a subpolynomial upper envelope for the screw on the
square mesh.  The derivative budget fills the gaps, and Landau continuation
excludes every off-line pole.  Functional-equation symmetry gives RH.

Thus

\[
\mathrm{WSTS}\Longrightarrow\mathrm{RH}.
\]

## 5. New reverse proof

Assume RH.  The classical Chebyshev estimate is

\[
R(t)=O(\sqrt t\log^2(2t)).
\]

`L-27501` proves the unconditional profile estimates

\[
|E_c(u)|
\ll u^{-1/2}[1+\log(1/u)],
\]

and

\[
|E_c'(u)|
\ll u^{-3/2}[1+\log(1/u)],
\]

uniformly for the finite dyadic ratio

\[
c={\lfloor X/2\rfloor\over X}\in[1/3,1/2].
\]

Stieltjes integration by parts gives

\[
\begin{aligned}
\mathcal E_{X,Y}(z)
={}&-X^{-1/2}E_c(z/X)R(z^-)\\
&-X^{-3/2}\int_z^XR(t)E_c'(t/X)dt.
\end{aligned}
\]

The boundary term is `O(log^3 X)`.  The integral is bounded by

\[
\int_z^X
{\log^2(2t)[1+\log(X/t)]\over t}dt
=O(\log^4X)
\]

uniformly in `z`.  The floor error is smaller.  Therefore

\[
\mathcal B_X=O(\log^4X).
\]

Hence RH implies `WSTS`.

This is the first exact reverse implication in the carry-shell language and
shows that no hidden strengthening has been inserted into the final theorem.

## 6. What the live side branches contribute

### PR #265 — positive endpoint-scale frame

Durable:

```text
parabolic seed is a nonnegative carry-row object;
endpoint differences are positive atoms;
finite scale greedy is feasible;
blocker charge has q^(-3/2) diagonal weight;
continuum endpoint kernel and zeta symbol are exact.
```

Open:

```text
ESBT/ESGS.
```

These are candidate proofs of a sharp positive producer, not dependencies of the
WSTS chain.

### PRs #271/#274 — positive deformation and prime queue

Durable:

```text
positivity-preserving ordinary-prime correction exists;
its LP optimum is exactly the actual prime ramp;
consecutive-prime queue is the least oversupport charge;
proper powers can be neutralized;
fixed-ratio tails are eventually nonpositive.
```

Open:

```text
shrinking-ratio PTQ/PTC.
```

The zero-tax theorem closes geometry while exposing that the optimum is still
the RH-bearing scalar.

### PR #244 — fifth-scale digital recurrence

Durable:

```text
frozen-corridor self-similarity;
first off-diagonal descent below X/5;
base-five phase identities;
logarithmic simultaneous-blocker sparsity.
```

Open:

```text
DGB(5), the cross-residue boundary ledger.
```

### PR #269 — factor-five reflected carry source

Durable:

```text
compact pointwise opposite-parity wavelet;
negative Kummer rows confined to 2m<=n<5m;
strict carry-feature Schur reserve;
positive generalized-prime wavelet synthesis.
```

Open:

```text
physical independent-frequency normal-to-carry transference.
```

### PR #270 — affine continuum Green deformation

Durable:

```text
exact signed Green equality state;
all-integer decoder;
affine oversupport lift;
continuum zero-affine-charge coupling.
```

Open:

```text
FAGD finite arithmetic deformation.
```

### Other mechanisms

The annular frame, boundary-jet, parity–Green, Euler-fiber, and bottom-charge
routes isolate other exact images of the same scalar.  Their final inequality is
also unproved.

## 7. Why this packet is review ready

The package has one main theorem and no alternative closure hidden in the proof.
A reviewer can reject it by finding any of:

```text
an incorrect continuum cell derivative;
a missing reciprocal knot atom;
a wrong finite-to-continuum scale;
a nonsummable floor error;
a wrong Stieltjes endpoint orientation;
a nonzero objective cost in the weighted transport;
a failed dyadic telescope;
a square-screw normalization or Landau sign error;
an incorrect RH Chebyshev bound application.
```

Acceptance verifies the equivalence `WSTS <=> RH`.  It does not verify `WSTS`
unconditionally.

## 8. Exact regression

`X-27501-wsts-consolidation` uses exact rational/integer arithmetic and checks:

```text
normalized-tail derivative identity                  1 formal identity
prime-tail queue = maximum positive suffix           19,530 cases
weighted Abel upper-tail identity                     3,905 cases
least Skorokhod boundary charge                      19,530 cases
dyadic shell telescope                                8,128 cases
Stieltjes orientation                                 1 exact piecewise test
zero-cost weighted transfer                              30 cases
logarithmic cubic/quartic budget                      exact coefficients
finite dyadic ratio                                   4,998 cases
```

Retained result digest:

```text
bed2adcc56608f1fcd42227c6603eaa7ed7bb00b0afd3a39de78d64c0486d03c
```

The checker explicitly states that it proves neither `WSTS` nor RH.

## 9. Final honest status

```text
positive finite carry geometry                   COMPLETE PROPOSED
continuum fixed-ratio shell order                COMPLETE PROPOSED
finite floor decomposition                      COMPLETE PROPOSED
weighted prime-tail transport                   COMPLETE PROPOSED
RH => WSTS with O(log^4 X)                      COMPLETE PROPOSED
WSTS => prime ramp => RH                        COMPLETE PROPOSED
WSTS <=> RH                                     COMPLETE PROPOSED EQUIVALENCE
unconditional WSTS                             UNPROVEN
Riemann Hypothesis                             UNPROVEN
```

The project is finished as a **consolidated reduction**.  It is not finished as
a proof of RH until one unconditional argument establishes `WSTS` or an
explicitly mapped equivalent theorem.