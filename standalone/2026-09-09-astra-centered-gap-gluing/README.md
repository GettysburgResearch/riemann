# Centered divisor gaps: exact two-reservoir gluing and sharp logarithmic loss

**Proposed complete component proofs, for independent review. RH and the native
signed coherent-work estimate remain unproved.** This packet does not propose a
full RH solution. It settles a narrower open question in the current graph work.

The #825/#826 gap estimates and #828/#829 box spectra left open an absolute
centered gap on arbitrary divisor-closed supports. CGG26 constructs literal
squarefree supports with centered inverse gap of order log log of their largest
prime. They are two prime boxes joined at integer 1; every allowed edge is kept.
The individual boxes have constant centered gaps, while their union develops
exactly one slow positive direction. The contrast between their two harmonic
means identifies that direction quantitatively.

## Statements

For disjoint nonempty prime alphabets A,B let S=B(A) union B(B), where B(A)
contains every squarefree product of A. Keep the metric sum |f(n)|^2/n and the
complete prime-power form sum log(p)/(jp^k)|f(jp^k)-f(j)|^2. Write Z_A,Z_B for
the harmonic masses, G_A,G_B for their explicit root Green capacities, and g
for the smaller individual gap. Then

```
H_A/G_A + G_A (Z_B-1)/(Z_A+Z_B-1) <= C(S)
 <= 1/g + (Z_B G_A+Z_A G_B)/(Z_A+Z_B),
Var_S(f) <= E_S(f)/g + Z_A Z_B/(Z_A+Z_B)|mean_A f-mean_B f|^2.
```

Here C(S) is CENTERED, not anchored; H_A is the explicit second root spectral
moment. Every direction orthogonal to the constant and the displayed contrast
has gap at least g. The second positive eigenvalue is at least g.

Take A=all primes <=y, and B=the subsequent primes until its harmonic mass first
reaches Z_A. If P(y) is that terminal prime, the new all-scale theorem is

```
C(S_y) = 3/(2pi^2) log log P(y)+O(1),
lambda_1(S_y) ~ 2pi^2/[3log log P(y)],
lambda_2(S_y) >= (3/2)log2.
```

A fixed mass ratio r generalizes the leading constant to
3r/[(1+r)pi^2]. Together with #825's source-qualified upper theorem, the worst
CENTERED inverse gap among divisor-closed supports has exact order log log P
at every sufficiently large prime budget P. No optimal universal leading
constant or conclusion for ordinary intervals 1,...,N is asserted.

Read [PROOF.md](PROOF.md), [REVIEW_AND_SOURCES.md](REVIEW_AND_SOURCES.md), then
[VALIDATION.md](VALIDATION.md). The box root-capacity asymptotic is reconstructed
and credited to #828/#829; gluing and the centered sharpness are the new step.

## Replay

```
python -I -S -B check.py --check verification.json
python -I -S -B -O check.py --check verification.json
python -I -S -B test_check.py --part all
python -I -S -B -O test_check.py --part all
```

`--emit` is a producer, not acceptance. Six actual-log-prime certificates are
Rayleigh lower witnesses plus theorem-based upper bounds, NOT computed optimal
gaps. The large second boxes are handled by an exact product-mass/zero-profile
compression, not enumerated. Small separate full-graph panels use FORMAL rational
rates for exact algebra. Finite checks do not establish the analytic asymptotics.
