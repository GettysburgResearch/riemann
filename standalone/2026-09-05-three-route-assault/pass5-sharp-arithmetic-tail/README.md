# Fifth continuation: a sharp arithmetic-tail completion, not RH

**PROPOSED COMPLETE COMPONENT PROOFS. Independent mathematical review is required. RH and the signed-energy upper bound remain unproved.**

Parent: PR #793 at `6ebbe5efe6430584736649b87495af2be073f693`.
All preceding folders, including the independently authored `pass4/` and imported `pass4-signed-energy-attempt/`, are preserved. All three research routes remain active. This continuation concentrates on the growing-degree tail left open in the Mobius route.

## What is proved

For `a_n=sum b_k k^(-3/2)L_n(2log k)`, any `|b_k|<=1`, and the SAME integer cutoff `X_N=1728^N` for every degree `0<=n<=N`,

```
||(a_n-a_n^(X_N))_(0<=n<=N)||_2 < (10/3)(11/12)^N.
```

This includes the actual `mu_67` source. It is an unconditional full arithmetic-tail estimate, not fixed-degree convergence or a numerical scan. It proves that the finite signed-energy records at this specified cutoff have the same subexponential endpoint as the infinite source. Their signed upper bound is still open; the raw finite-sum envelope is exponential here.

The natural follow-up is sharp as well. Among cutoffs `X_N=exp(cN)`, the exact universal threshold for a vanishing vector-tail norm on the q-free squarefree support is

```
7.17798836313058 < c_* < 7.17798836313060.
```

At `c=c_*` the error has order `N^(-1/2)`; above it the error decreases exponentially; below it an explicit positive squarefree control gives exponentially growing error. The decimal bracket is certified by exact rational logarithm series. It is not inferred from a plotted saddle.

For fixed `c>8/3`, put

```
p=c-1-sqrt(c(c-2)), beta=(1-p)/(1+p),
Psi(c)=-log p-c(1-3p)/(2(1+p)).
```

The exact squarefree-support tail norm is asymptotic to

```
2 delta_67 / [(1-3p)sqrt(2 pi beta(1-p^2))]
   * N^(-1/2) exp(N Psi(c)).
```

The proof derives the continuous saddle directly and transfers it to the actual squarefree support with the elementary error `|W_67(x)-delta_67 x|<=4sqrt(x)`. No PNT, zero data, or Mobius cancellation hypothesis is used.

A separate central limit theorem locates the RELATIVE exponential-signal transition of the same positive control:

```
log X=(8/3)n+z sqrt((32/9)n)
retained coefficient / [2 delta_67 (-3)^n] -> Phi(z).
```

Thus `8/3` (fraction of the 3^n signal captured) and `c_*` (absolute tail tends to zero) are different thresholds. The signed continuous comparison is not falsely called a probability measure: its negative mass is bounded by `(e/3)^n` before the characteristic-function limit is used.

## Exact remaining RH theorem

Writing `E_N^(X)` for the actual mu_67 finite energy, the remaining statement is

```
for every epsilon>0, E_N^(1728^N) <= C_epsilon exp(epsilon N), all N>=1.
```

The tail theorem makes this an accurately covered finite formulation; it does not prove the displayed bound. The same-diagonal positive counterfeit still has root growth 3 after this cutoff. Diagonal comparison without literal Mobius signs remains invalid.

The exponential size of the cutoff is stated explicitly. No growing-N evaluation through these integers was executed or represented as computationally practical.

## Read and replay

Read `PROOF.md`, then `SOURCES_AND_REVIEW.md`. The former contains AT-1 through AT-5 and the exact failed final inference. Standard ingredients are attributed and no external priority claim is made.

```
python verify.py --check RESULTS.json --manifest
python -O verify.py --check RESULTS.json --manifest
python verify.py --self-test
python -O verify.py --self-test
```

The 498 bounded exact controls include the critical-constant interval certificate, independent integrated-kernel reconstructions, cumulants, the squarefree count identity, and small finite extremizer tests. Fourteen unit/rejection tests pass in each mode. The finite tests do not machine-prove Cauchy continuation, saddle asymptotics, the normal limit, the full arithmetic-tail theorem, or RH.

Optional `python regression.py` uses mpmath at 90 digits. It checks only continuous-kernel asymptotics at degrees 50, 200, and 800. `REGRESSION.json` labels those results NON_DIRECTED_HIGH_PRECISION and excludes them from proof dependencies.

Publication status for THIS continuation is recorded in the external handoff receipt, not inferred from the existence of this folder. The parent checkpoint and the author's previous signed-energy archive import were verified remotely before this work. No claim of a new remote commit is made without a successful write and readback.
