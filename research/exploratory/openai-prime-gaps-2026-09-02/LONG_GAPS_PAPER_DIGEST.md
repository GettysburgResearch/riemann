# Paper digest: Improved Long Gaps Between Primes

```text
Status: PAPER-LINKED FORMAL SOURCE / REVIEW_PENDING
Scope: global asymptotic lower bound for maximal consecutive-prime gaps
Paper source: OpenAI, Improved Long Gaps Between Primes
Formal source: openai/LongGapsBetweenPrimes
Riemann Hypothesis: unproved; this theorem does not imply RH
```

## 1. Exact theorem

Let \(G(X)\) be the largest gap between consecutive primes not exceeding
\(X\). The paper and formal repository state that there is an absolute
constant \(c>0\) such that, for all sufficiently large \(X\),

\[
G(X)
\ge
c\,
\frac{\log X\,(\log_2 X)^2\,\log_4 X}
     {(\log_3 X)^2},
\]

where \(\log_j\) denotes the \(j\)-fold iterated natural logarithm.

The Lean endpoint is

```lean
LongGapsBetweenPrimes.long_gap_theorem
```

and the source-facing intermediate theorem is

```lean
LongGapsBetweenPrimes.short_translates
```

corresponding to Proposition 1.2. The repository metadata also identifies
`long_prime_gaps` as an indexed-prime Comparator form of Theorem 1.1.

## 2. Scale of the improvement

The Ford-Green-Konyagin-Maynard-Tao long-gap theorem gives the explicit scale

\[
G(X)
\gg
\frac{\log X\,\log_2 X\,\log_4 X}{\log_3 X}.
\]

The new scale is larger by

\[
\frac{\log_2 X}{\log_3 X}\longrightarrow\infty.
\]

This is therefore an unbounded-factor asymptotic improvement, not a change of
the hidden constant.

Relative to the classical Erdos-Rankin baseline

\[
R(X)=
\frac{\log X\,\log_2 X\,\log_4 X}{(\log_3 X)^2},
\]

the new theorem supplies the explicit multiplier \(\log_2 X\).

The theorem remains a lower bound along an infinite sequence of exceptionally
large prime-free intervals. It is not an assertion about typical gaps or an
upper bound for every gap.

## 3. Exact short-translates engine

The formal Proposition 1.2 has the following content. There is
\(0<\delta<1/2\) such that, for all sufficiently large \(x\), whenever

```text
x < H <= x (log x)^2,
S is a subset of [1,H],
|S| <= delta x,
b is a residue below the primorial P(x),
```

there is an integer

```text
1 <= t <= exp(x)
```

for which every number

\[
b+P(x)t+s,\qquad s\in S,
\]

is composite.

This is a powerful deterministic output from a probabilistic/sieve argument:
an arbitrary sparse set of offsets is simultaneously killed by one short
translate of a primorial progression.

The theorem is reusable independently of the final Erdos-Rankin cover. It is
the main object to extract into a generic sieve library.

## 4. Signed divisor coefficients

The proof begins with a squarefree primorial-like modulus \(P\) and the
normalization

\[
B=\sum_{\substack{d\mid P\\d>1}}
\frac1{\varphi(d)\log d}.
\]

It defines

\[
a(1)=1,
\qquad
a(d)=-\frac1{B\log d}\quad(d>1),
\]

so that the exact weighted cancellation

\[
\sum_{d\mid P}\frac{a(d)}{\varphi(d)}=0
\]

holds.

This is the structural center of the random-sieve calculation. It makes the
chosen divisor packet mean zero while retaining positive diagonal mass.
Partial divisor subsums containing \(1\) become nonnegative because omitted
coefficients are negative.

The formal source proves these identities exactly before any asymptotic
estimate.

## 5. Local residue factors and negative covariance

For a prime \(p\), a selected root \(a\pmod p\), and a residue \(t\pmod p\),
the local factor is normalized to have:

```text
mean zero;
square mean p/(p-1);
negative covariance for two distinct roots.
```

Concretely, the distinct-root covariance is

\[
-\frac{p}{(p-1)^2}.
\]

Products of these factors over prime divisors form a tensor-product basis for
the sieve variables. The negative off-diagonal covariance is essential: it
prevents a naive sum of positive errors and allows the simultaneous-root
second moment to close.

This exact local algebra is potentially reusable in other finite-prime
selection and residue-cover problems.

## 6. Random-sieve and second-moment mechanism

The formal proof builds truncated divisor tuples, weighted residue sums, and a
Gram matrix. Its main analytic tasks are:

1. estimate the diagonal coefficient moment;
2. control divisor tails;
3. control collisions between distinct linear forms;
4. bound row sums of the residual Gram operator;
5. use a second moment to show that one residue choice works simultaneously
   for every offset in the sparse set.

The source uses only weak Mertens/Euler-product estimates sufficient for the
argument. It does not import a strong prime number theorem as one opaque
black box.

The fixed choice

\[
\kappa=\frac18
\]

sets a divisor cutoff of size roughly \(D=e^{x/8}\), while the averaging
range has length about \(e^x\). A characteristic interval-error term behaves
like

\[
\frac{D^6}{e^x}=e^{-x/4},
\]

which is safely negligible. This parameter choice is conservative enough for
a formal proof; it is a natural target for a parameterized optimization.

## 7. Erdos-Rankin covering stage

After Proposition 1.2, the proof constructs a complete residue cover of a
long interval.

The formal implementation uses three prime ranges.

### Small primes

Primes up to a cutoff comparable to

\[
W=(\log x)^4
\]

are assigned simple residues, eliminating integers with small prime factors.

### Intermediate primes

A smoothness cutoff of the shape

\[
Z=
\exp\!\left(
\frac{\log x\,\log_3 x}{C\log_2 x}
\right)
\]

is introduced, with a sufficiently large fixed constant \(C\). Residues for
primes between \(W\) and \(Z\) are chosen greedily to remove most survivors.

### Larger primes

Primes above \(Z\), together with the short-translates theorem, cover the
remaining sparse set. The exceptional survivors are either primes or
\(Z\)-smooth integers; a Rankin/Euler-product estimate makes their number
small enough for Proposition 1.2.

The outcome is a full residue cover of an interval of length

\[
y
\asymp
x(\log x)^2\frac{\log_3 x}{(\log_2 x)^2}.
\]

## 8. From a residue cover to a consecutive-prime gap

Chinese remaindering produces an integer \(m\) such that every one of

\[
m+1,\ldots,m+y
\]

is composite.

The proof then selects the nearest prime below and the first prime above the
block, verifies that they are consecutive, and obtains a gap of length at
least \(y\). A Bertrand-type bound controls the location of the upper prime by
a quantity of the shape

\[
e^{8x}.
\]

Finally, setting \(x\) proportional to \(\log X\) gives the announced
iterated-log scale.

## 9. Formalization and source-lock boundary

The proof code imported by Riemann is pinned at

```text
8f5fa88c88b4750028c05b66b081d56a92418054.
```

The later upstream commit

```text
03a1190d0bc5502d9f54eeb60ad3e45e22b0df0b
```

adds the public paper and abridged-chain-of-thought links to `README.md` and
adds the paper URL to `formalization.yaml`. It is an unsigned documentation
commit whose parent is the imported proof commit. It changes no Lean source;
the main Lean file remains the same blob.

The upstream metadata reports:

```text
scope: Full formalization of main results
sorry_count: 0
axioms: propext, Classical.choice, Quot.sound
review: self-assessed
Lean: v4.33.0
```

This is strong formal evidence, but Riemann still requires an independent
clean build, Comparator/Nanoda replay, theorem-statement comparison, and
semantic proof review before promotion.

The paper CDN could not be rendered or downloaded in this import environment.
Accordingly, the paper title, URL, theorem numbering, and alignment are
source-locked through the upstream metadata, but no PDF byte hash, page count,
or screenshot audit is claimed.

## 10. Relevance to the Riemann repository

### Prime-gap formal infrastructure

This theorem is the strongest immediate candidate for extracting a reviewed
prime-gap library:

```text
ConsecutivePrimes
primorial and residue-cover APIs
short-translates theorem
full-cover-to-gap bridge
iterated-log asymptotic comparison.
```

Its Lean generation matches Riemann's current 4.33 generation, unlike the
bounded-gap-186 package.

### Stress test for gap-cell RH architectures

The earlier RH bridge in this packet decomposes the prime source into
logarithmic gap cells. The new theorem creates larger explicit empty cells
than previously known by an unbounded factor. Any proposed local energy,
sampling, or Poincare bound must survive these cells with the correct
scale-dependent constants.

This is valuable even negatively: it rules out any RH architecture that
quietly assumes uniform local prime density, uniformly short gap cells, or a
scale-independent sampling lower bound.

### Explicit-formula normalization

A prime-free interval creates a strong localized negative discrepancy in
\(\theta\) and \(\psi\). The formal cover therefore supplies adversarial
source packets for testing the repository's Mellin, Weil, and
coefficient-extraction normalizations.

It does not identify which zeta zeros produce that discrepancy. Many zero
configurations can generate compatible local oscillation.

### Beta/Mobius and divisor-wavelet programs

The signed divisor normalization and tensor residue factors resemble the
repository's primitive-pair and divisor-wavelet decompositions. The exact
mean-zero coefficient packet may offer a cleaner model for:

- source-preserving divisor truncation;
- collision Gram estimates;
- separating diagonal mass from signed off-diagonal cancellation;
- certifying residue-selection operators.

The similarity is methodological, not an implication from long gaps to the
open Mobius estimates.

## 11. Why this does not approach RH by itself

RH is equivalent to global square-root-scale control of a signed prime
discrepancy or to an equivalent zero/positivity statement. The long-gap
theorem proves existence of unusually large local holes.

It discards:

- the signs and phases at all other scales;
- logarithmic prime-power weights outside the chosen block;
- the Mellin-frequency decomposition;
- information distinguishing critical-line from off-line zeros;
- any uniform upper bound on prime gaps.

Indeed, RH is ordinarily used in the opposite direction: sufficiently strong
control of \(\psi(x)-x\) gives upper bounds on how long a prime-free interval
can be. A larger lower bound for exceptional gaps cannot be reversed into RH.

The honest RH relevance is as a source of exact adversarial cells and formal
sieve infrastructure.

## 12. Highest-value improvements

### Formal review

1. clean build at the exact proof commit;
2. Comparator, lean4export, Nanoda, and axiom receipts;
3. line-by-line comparison of Proposition 1.2 and Theorem 1.1 with Lean;
4. verify every interval endpoint, strict inequality, and notion of
   consecutive primes;
5. extract the theorem into modules without changing statements.

### Effective theorem

1. expose an explicit positive constant \(c\);
2. expose a computable threshold \(X_0\);
3. generate finite residue-cover witnesses at test scales;
4. preserve a constant ledger through every asymptotic conversion.

### Analytic strengthening

1. parameterize \(\kappa\) rather than fixing \(1/8\);
2. optimize the small-prime and smoothness cutoffs;
3. strengthen ShortTranslates to larger sparse sets or longer offset ranges;
4. replace the second-moment existence step by higher-moment,
   dependent-rounding, or entropy methods;
5. sharpen the smooth-survivor count and greedy cover;
6. determine which change can improve the iterated-log order rather than only
   the hidden constant.

A genuine next-order improvement must enlarge the coverable interval or
reduce the survivor density at a structural level. Optimizing `8`, `16`, or
`128` alone changes only the implicit constant.

## 13. Verdict

Subject to independent proof review, this is a dramatic prime-gap result: a
full formalization of an unbounded-factor improvement over the previous
explicit long-gap scale.

Its strongest contribution to Riemann is not evidence for RH. It is:

```text
a theorem-sized short-translates engine;
a fully formal Erdos-Rankin cover;
a severe stress test for local prime-source architectures;
and a reusable exact model of signed sieve cancellation.
```
