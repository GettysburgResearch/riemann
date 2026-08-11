# Final-strike report: from finite signature moments to a global Fredholm hierarchy

**Date:** 2026-08-11  
**Status:** new proposed-complete reductions and one exact no-go; RH unproved.

## Executive verdict

The complete-kernel route has already shown that, once a hypothetical off-line pair is captured, a corrected-kernel floor tending to zero is equivalent to RH. The Xi-cardinal branch removes the conditioning/capture escape. Therefore another finite linear channel, window, Schur correction, or row reserve cannot by itself be the final step.

The new move is nonlinear and global:

```text
Weil form
-> fixed Gaussian trace-class compression A_sigma
-> full Fredholm determinant det(I+t A_sigma)
-> all exterior powers / all shifted moment Hankel matrices.
```

This gives an exact theorem:

```text
RH
<=> A_sigma >= 0
<=> det(I+tA_sigma)>0 for all t>0
<=> every exterior coefficient is nonnegative
<=> every shifted moment Hankel matrix is PSD.
```

Unlike the finite bandwidth-one moment architecture, all trace moments now have absolutely convergent unconditional prime-cluster expansions. A hypothetical off-line pair necessarily creates a negative exterior coefficient at some finite degree, and trace-norm convergence pushes that witness to a finite prime cutoff and finite Galerkin matrix.

No negative coefficient has been found, and the required all-order positivity has not been proved. RH remains open.

## 1. Why this leaves Claude's method class

Claude's theorem uses a finite Gabor compression, the first trace, the Frobenius square, and the signature/rank structure. Its own method analysis says that routine higher moments are available only where the dimension cap makes them ineffective; the bandwidth-one information class cannot approach 100 percent.

Gaussian confinement changes the regime. It does not let the support grow with height. Instead it damps a prime shift by

```text
exp[-sigma (log n)^2/2],
```

so every operator moment and every prime word converges absolutely. The price is that one must prove an infinite hierarchy of signs rather than one asymptotic two-moment inequality.

## 2. Main new operator theorem

For sigma>0 define

```text
w_sigma(u)=exp(-sigma u^2),
R=(1-d^2/du^2)^(-1),
J_sigma=M_(w_sigma) R.
```

Pull Weil's Hermitian form back through J_sigma. The zero-side evaluation vectors decay quadratically with the ordinate; the local zero count makes the resulting self-adjoint operator A_sigma trace class.

The exact Gaussian overlap identity

```text
int exp(-sigma u^2) exp(-sigma(u-y)^2) du
 =sqrt(pi/(2sigma)) exp(-sigma y^2/2)
```

makes the complete prime-power operator series trace-norm convergent with a super-polynomial cutoff error.

The exact Xi-cardinal difference for an off-line pair belongs to the range of J_sigma because its source decays faster than every Gaussian. It gives Weil value -2m and is orthogonal, in the Weil form, to the cardinal sources of all other pairs. Hence the negative index of A_sigma is exactly the number of distinct off-line reflected pairs.

## 3. Finite-witness theorem

Let -eta be any negative eigenvalue and R=||A_sigma||_1/eta. The Fredholm determinant is

```text
D(t)=sum_k e_k t^k,
e_k=tr(wedge^k A_sigma),
|e_k|<=||A_sigma||_1^k/k!.
```

Since D(1/eta)=0, not all initial coefficients can be nonnegative past degree about 2eR. More precisely, some

```text
e_k<0,
k <= ceil(2e||A_sigma||_1/eta)-1.
```

The Gaussian prime cutoff converges in trace norm, exterior coefficients are trace-norm continuous, and finite-rank Galerkin projections converge in trace norm. Therefore false RH has a finite directed certificate:

```text
finite k
+ finite prime cutoff P
+ finite matrix dimension M
+ strict e_k<0.
```

This is a serious falsification architecture even though it does not establish positivity.

## 4. Exact phase-bank firewall

The powered inner Q4 bank is unitary only in the boundary critical-line norm. In any reproducing-kernel Hilbert space controlling evaluation at an off-line point z,

```text
||M_F|| >= |F(z)|.
```

For the powered reflected channel this lower bound is exponential in the power k. For a root-of-unity bank the direct-sum multiplier norm is bounded below by the square root of the average reflected power, also exponential.

Therefore the claimed exponential off-line amplification is paid somewhere: in the strip/form metric or, equivalently, in weighted causal coefficient mass. A polynomial derivative gauge and unit critical-line L2 energy do not imply a subexponential complete arithmetic block.

This does not disprove the phase-bank criterion. It proves that its remaining subexponential complete arithmetic block estimate is the conclusion-producing RH-strength theorem, not bookkeeping.

## 5. The remaining target

There are now two equivalent exact forms.

### Fredholm / Lee-Yang

```text
det(I+t A_sigma)>0 for every t>0.
```

### Stieltjes moments

```text
H_d=(tr A_sigma^(i+j+1))_(0<=i,j<=d) >= 0
for every d.
```

Every entry has an absolutely convergent prime-cluster expansion. The highest-value next attack is to find a source-order factorization of the quadratic form

```text
sum_(i,j) c_i c_j tr A_sigma^(i+j+1)
 =tr[A_sigma |p(A_sigma)|^2]
```

as an explicit prime-side sum of squares before absolute values. Any such factorization, uniform in the polynomial p, proves RH.

## 6. Hostile review order

1. Fourier signs in the centered Weil pairing and the definition of the evaluation vectors.
2. Uniform O((1+t^2)^(-1)) evaluation decay after Gaussian multiplication and order-two smoothing.
3. Trace-norm convergence of the zero-side hyperbolic series.
4. Exact Gaussian trace-norm overlap bound for prime shifts.
5. Extension of the explicit formula from compact tests to the Gaussian-confined range.
6. Exact inclusion of the Xi-cardinal source in Range(J_sigma).
7. Negative-index equality, including infinitely many off-line pairs.
8. Converse direction of the shifted-Hankel criterion.
9. Exterior-degree tail bound and trace-norm continuity of exterior coefficients.
10. Finite Galerkin realization and outward-directed primitive evaluation.

## 7. Verification

The retained finite regression returns

```text
PASS_FREDHOLM_PONTRYAGIN_FINAL_STRIKE
```

and checks:

- positive spectrum -> positive exterior coefficients and Hankel matrices;
- a negative eigenvalue -> positive-axis determinant root, negative exterior coefficient, and negative shifted-Hankel minor;
- the quantitative finite-degree exponential-tail bound;
- exterior-power amplification of one negative direction;
- the exact Gaussian overlap identity;
- boundary unitarity versus exponential reflected phase-bank multiplier norm;
- noncommutative word expansion of trace moments;
- trace-norm stability of exterior coefficients;
- rapidly decreasing Gaussian-weighted von Mangoldt tails.

The replay is finite diagnostic algebra. It does not prove any zeta positivity statement.
