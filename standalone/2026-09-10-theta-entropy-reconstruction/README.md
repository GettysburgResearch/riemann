# Whole-theta reconstruction: all orders, but not in the pair-Ising class

**Proposed component proofs. The pair realization and RH remain unproved.**
Continuation of PR #842 from `8f1f457b0b92e76a0a75bd3d8a8921c205fa75b0`.

The direct extension tested here has a complete all-order answer after enlarging
the model class. A prescribed sequence of finite, zero-field spin systems with
nonnegative even MANY-SPIN couplings and a common positive field weight converges
to the unmodified theta probability law, in every moment and uniformly on every
complex compact of its generating function. The construction uses no zero data.

For an even confining polynomial P of degree 2d, take N=L^(2d+1) spins and the
observable X=S/L^(2d), where S is their total spin. Give configurations exponent

    H=N sum_(r=1)^d (S/N)^(2r)/[2r(2r-1)]-P(S/L^(2d)).

At an explicit large-L threshold all coefficients of even spin-subset products
are nonnegative. Binomial entropy cancels to the required order, and the full
law converges to normalized exp(-P). The proof includes both extreme spin
levels and the entire physical tail. Rational even potentials

    P_j(t)=t^2+Q_j(t)^2

are then constructed from the literal theta density, with a global Gaussian
envelope. A diagonal choice reaches the whole normalized theta law. This is
not a finite moment fit and not a claim of an efficient graph-size bound.

**Why this is not an RH proof:** positive even many-spin interactions do not
have the pair-Ising Lee--Yang guarantee. The exact four-spin interaction
exp(J sigma_1 sigma_2 sigma_3 sigma_4), J>0, already has nonimaginary field zeros.
A connected four-spin law with positive pair AND four-body couplings has the
same defect. More strongly, the SAME entropy construction converges for
P=x^2/2+10^-6 x^6 to a smooth density with sixth cumulant in
(-0.000740,-0.000696), whereas every pair-ferromagnetic weighted magnetization
has nonnegative sixth cumulant. The exact rational certificate pays the entire
Gaussian integral. Neither counterexample is the actual theta law.

The remaining sufficient theorem is a theta-specific PAIR replacement preserving
each full restricted magnetization partition sum up to a multiplicative factor
exp(+-epsilon_j), epsilon_j->0. The paper gives its complete conditional RH
consumer and does not prove that replacement. Arbitrary hidden-spin gadgets,
conditional pair attraction, and positivity of higher-body coefficients do not
supply it automatically.

Read [PROOF.md](PROOF.md), then [REVIEW.md](REVIEW.md), [SOURCES.json](SOURCES.json)
and [VALIDATION.md](VALIDATION.md). Classical Curie--Weiss entropy cancellation,
Bernstein approximation, Lee--Yang and Hurwitz are credited; no external novelty
or independent acceptance is claimed. Prior research is unchanged.

```
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

The finite checker does not construct a large theta spin graph or prove the
infinite limit. It reconstructs exact entropy/spin algebra and a distinct
continuous counterlaw. All-order many-spin reconstruction is a paper theorem
submitted for review, not a machine-certified RH result.
