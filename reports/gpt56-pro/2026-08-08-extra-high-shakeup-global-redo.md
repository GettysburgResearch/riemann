# Extra-high shake-up redo: what survives after attacking the live graph from first principles

Author: `gpt56-pro`  
Date: 2026-08-08  
Status: **research report; RH unproved**

## 1. Reason for the redo

The previous pass stopped too quickly after the MCF refutation. This redo refreshed the live repository through the post-#314/#315 graph and deliberately attacked several structurally different routes rather than shrinking another carry subproblem.

The outcome is not an unconditional proof of RH. It does produce two exact new arithmetic source theorems, one important large-scale mutation, and a clearer separation between genuinely different research directions.

## 2. Live-state conclusions

The newest branches reinforce one central lesson.

```text
pointwise/ambient positivity                    repeatedly fails;
absolute endpoint atomization                   can cost a power;
correct signed recombination                     is essential;
root/fixed-ratio Möbius mode                     survives Pascal cycles;
finite smooth/Green/endpoint geometry            is not the final arithmetic theorem.
```

In particular:

- PR #314 refutes eventual MCF exactly;
- PRs #305/#308/#310/#311/#315 refute the proposed polylogarithmic absolute boundary atomization while retaining much smaller coherent carry metrics;
- PR #316 closes fresh analytic-depth boundary injection, but not propagation of the old boundary bank;
- PR #326 identifies the carry root mode exactly and derives Jordan/totient source gauges, while leaving their conclusion-producing estimate open.

## 3. New exact result A — two hinge rows already see every off-line zero

PR #295 decomposes the critical target positively into square-root hinges

\[
h_T(q)=q^{-1/2}-T^{-1/2}.
\]

Large finite reconnaissance suggested the exact triangular carry inverse of each hinge might be positive. Rather than extrapolate that sign, this pass computed the first two inverse rows exactly.

For row two,

\[
K_2=-\mu+2\delta_2*\mu-\delta_3*\mu.
\]

For row three,

\[
K_3=\frac{-2\mu-2\delta_2*\mu+10\delta_3*\mu-6\delta_4*\mu}{6}.
\]

Their finite Dirichlet numerators are

\[
E_2(s)=-2+4\,2^{-s}-2\,3^{-s},
\]

\[
E_3(s)=-2-2\,2^{-s}+10\,3^{-s}-6\,4^{-s}.
\]

If both vanished, writing `x=2^-s` and `y=3^-s` gives

\[
y=2x-1,
\qquad
-6(x-1)(x-2)=0.
\]

Neither root is compatible with `Re(s)>0`. Thus the two rows have no common right-half-plane zero.

The Mellin transform in the endpoint `T` is a nonzero elementary factor times

\[
E_j(z+1/2)/\zeta(z+1/2)
\]

plus an elementary column-one correction. Therefore every hypothetical off-line zeta zero creates a pole in at least one of the two fixed row transforms.

Consequently:

```text
eventual positivity of hinge row 2
+
eventual positivity of hinge row 3
-> RH.
```

This explains why the striking finite hinge positivity cannot be treated as a routine convexity lemma. Two fixed coordinates already contain the full reciprocal-zeta obstruction.

The complete proof is `L-32701`.

## 4. New exact result B — a zero-safe quadratic Jordan parity source

The all-order Selberg work on PR #326 suggests studying Jordan sources directly. For

\[
J_2=\mu*\operatorname{id}_2,
\]

cancel its unique main pole by the forced dyadic factor

\[
c_2=(\varepsilon-8\delta_2)*J_2.
\]

Exactly,

\[
\sum c_2(n)n^{-s}=\eta(s-2)/\zeta(s).
\]

More strikingly,

\[
(\mathbf1*c_2)(n)=(-1)^{n-1}n^2,
\]

so the complete floor potential is

\[
H(N)=(-1)^{N-1}\frac{N(N+1)}2.
\]

The pointwise carry charge of a split `n=j+k` is therefore explicit:

```text
odd parent:       +(n+1)*(even child) > 0;
even parent,
 even/even:       -j*k < 0;
even parent,
 odd/odd:         -[n(n+1)+j(j+1)+k(k+1)]/2 < 0.
```

Thus every split of every odd parent is favorable and every split of every even parent is unfavorable. No Mersenne exception, quotient cell, Möbius value, or hidden source sign remains.

The corresponding Riesz scalar has Mellin transform

\[
\frac{\eta(z-3/2)}{z^2\zeta(z+1/2)},
\]

and the numerator cannot cancel a nontrivial zeta-zero pole.

This creates a genuinely new combinatorial target:

```text
construct an exact nonnegative carry flow
whose explicit odd-parent reserve dominates its even-parent debt.
```

No such global flow theorem is claimed here. The exact source theorem is `L-32702`.

## 5. Large-scale mutation of the actual binary/ternary producer

The actual critical half-binary/half-ternary producer, not an Abel-smoothed surrogate, was reconstructed to large endpoints with compensated arithmetic.

It develops negative rows after the previously explored range. Representative values include

```text
X=25,000,000   minimum about -5.98e-4;
X=50,000,000   minimum about -1.93e-2;
X=100,000,000  minimum about -5.68e-2.
```

At `X=100,000,000` there were 53 negative rows in the retained reconstruction.

The weighted negative debt nevertheless remained only about `2.27` in that run.

This is not yet an exact refutation: the full source uses floating square roots and logarithms and has not been converted to a directed interval proof object. It is recorded as discovery only in `O-32701`.

Strategically, however, it says that reviewers should not spend time trying to prove GFEP/pointwise producer positivity before this mutation is resolved. The weaker BTF/Cycle-Debt route remains compatible with the data.

## 6. Orthogonal routes checked in the shake-up

### Brownian/GGC

The exact Brownian/gamma representation remains valuable, but generic infinite divisibility of the centered log law cannot be the missing theorem: an infinitely divisible characteristic function has no real zeros, whereas the centered xi characteristic function has the known critical-line zeros. The repository's prior Thorin audit also correctly isolates the central positive-measure continuation as RH-bearing.

### Brownian Nörlund / Robin

The finite Nörlund approximants remain an interesting independent architecture. The live correction on PR #318 shows that positive superposition of individually real-rooted Robin fibers is not closed, so a new source-specific stability theorem is still required.

### Growing Fejer / r-adic screw filters

The endpoint Fejer family pushes the first adverse prime region to the sharp `O(N^-2)` scale, but its complete low-lag autocorrelation ledger remains order one and alternating. Allowing the degree to grow does not by itself create a PNT-sized positive reserve: the leading prime and archimedean terms still cancel at the critical normalization.

### Current external literature

A current arXiv sweep found no published closure that bypasses the repository's remaining theorem:

- Verjovsky, arXiv:2607.25002, gives local Möbius-moment criteria equivalent to RH;
- Gaber, arXiv:2607.26114, gives Euler-ell-totient criteria whose error term still carries zeta-zero poles;
- Connes, arXiv:2602.04022, proves finite extremal approximating values lie on the critical line and explicitly identifies convergence from finite to infinite Euler products as the prospective next step;
- Freedman, arXiv:2606.29555, explicitly leaves the quotient-to-original Weyl lift and final RH/de Branges bridge outside the current certificate.

These are useful cross-checks, not imported proof steps.

## 7. What I would review now

The exact reusable mathematics from this pass is narrow and reviewable:

1. `L-32701` — the two-row hinge Möbius firewall;
2. `L-32702` — the quadratic Jordan parity carry source;
3. `X-32701` — exact finite replay of both source identities;
4. `O-32701` — discovery-only producer mutation, kept separate from theorem status.

The branch should **not** be reviewed as a claimed proof of RH.

## 8. Research judgment after the shake-up

The dominant carry routes have now been pushed far enough that any purported elementary positivity closure should be assumed RH-bearing until its exact dual source is computed.

The genuinely distinct surviving directions are:

```text
A. signed Cycle-Debt / balanced transport,
   now with evidence that pointwise positivity is stronger than needed;

B. quadratic Jordan parity flow,
   whose source sign is deterministic rather than Möbius;

C. Brownian/Nörlund finite half-plane stability,
   genuinely outside the prime/carry loop;

D. Connes/Weil spectral convergence,
   where finite approximants are already on the line but the cofinal convergence theorem remains open.
```

No unconditional proof of RH emerged. The correct response is not to disguise one of these remaining statements as routine. The two exact source theorems above materially change what the next ambitious attack should target.
