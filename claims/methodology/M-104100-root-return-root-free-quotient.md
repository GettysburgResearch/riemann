# M-104100: typed root-return / root-free quotient of the implication matrix

Claim ID: `M-104100`  
Status: **PROVED EXACT METHODOLOGY / CLASSIFICATION**  
Created: 2026-08-21  
Base: PR #704, `66f755df4321a03874e0da3f61b033300173e364`  
RH status: **unproved**

## 1. Why a quotient is needed

The live repository contains many exact positive forms: Hardy tails,
Cauchy--Poisson squares, divisor-GCD squares, owner energies, phase Grams and
compact wavelet energies.  Several have the schematic form

```text
positive square = critical root square + nonnegative excess.
```

Changing coordinates among such forms can expose useful arithmetic, but it does
not by itself control the critical root.  The implication ledger must therefore
separate four types:

```text
D  fixed conclusion-facing detector;
Q  root-containing positive square;
RR strict source-owned return of the root from Q;
RF root-free packing of the excess and return remainder.
```

Only the hyperedge

```text
D + Q + RR + RF -> subpower negative mass -> RH
```

is counted as conclusion progress.

## 2. Relation to the current matrix genealogy

PR #697 proves a two-channel nonnegative Perron criterion.  PR #704 proves
matched transfer and adaptive-completion residual identities.  `L-104101` is
the one-dimensional Schur-complement quotient of those mechanisms:

```text
x <= theta(x+e)+r, theta<1
=>
(1-theta)x <= theta e+r.
```

The quotient is not advertised as an independent detector.  Its purpose is to
make the minimal arithmetic division of labour explicit.

## 3. Root-return side

Candidate inputs belong here only if they produce a strict coefficient below
one before the sign of the detector is observed.  Examples include a
source-prescribed owner return, compensated Hasse transport, or a Perron row
whose self-coefficient is strictly subcritical.

The required moat may shrink:

```text
(1-theta_L)^(-1)=2^o(L)
```

is sufficient.  A fixed numerical gap is unnecessary.

## 4. Root-free packing side

Candidate inputs belong here only after the detector root has been removed
algebraically.  The packing target is

```text
integral_(2^L)^(2^(L+1))
  [sqrt(E_L(X))+sqrt(R_L(X))] dX/X
=2^o(L).
```

A positive form that still contains the full root is not root-free and cannot
be counted as this second input.

## 5. Firewalls

The following promotions are forbidden:

```text
supercritical positivity -> critical sign;
PSD Gram -> signed linear sign;
excess estimate -> root estimate;
pairwise positivity -> all-prime cone;
theta=1 -> strict return;
endpoint-dependent completed observable -> fixed Mellin detector.
```

The first four have exact finite countermodels in `R-104100`.  The last is
handled by the fixed-detector residual formulation inherited from PR #704.
