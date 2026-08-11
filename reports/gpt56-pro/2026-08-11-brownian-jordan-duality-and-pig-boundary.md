# Brownian–Jordan duality for the PIG boundary

Date: 2026-08-11  
Branch: `research/gpt56-pro/90410-pig-fourier-rademacher`  
Status: **new exact finite theorems; deterministic PIG and RH remain unproved**

## 1. Why this continuation was needed

PR #383 reduced the compact-Q4 Positive Innovation Gate to one mean coordinate and a square-root-sized additive major arc. PR #386 then gave an equivalent singular cosine/Goldbach normal form. Those coordinates identify the correct positive mass but do not explain why the old complete-period Jordan/Farey energies were easy while the fixed endpoint remains hard.

The present continuation supplies that missing dictionary.

## 2. Fixed endpoint: one mean plus one Brownian bridge

For any prefix source `c`, the symmetric row

```text
Q_N(j)=C(N)-C(j)-C(N-j)-kappa
```

has exactly one mean coordinate. After removing it, every source atom is a centered nested interval. Reflection pairs `m` and `N+1-m`, so the entire nonconstant row depends only on

```text
d_N(m)=c(N+1-m)-c(m).
```

The covariance kernel is exactly

```text
K_BB(u,v)=min(u,v)-uv.
```

Thus

```text
fixed PIG row
 = one symmetric mean
   + Brownian-bridge H^{-1} energy of reflection differences.
```

This is `L-90416`. It is the radial/reflection version of the inverse-circle-Laplacian theorem `L-90411` and the cosine antiderivative theorem on PR #386.

For the actual compact source, the tail process is a symmetric short-interval prime discrepancy. The largest sampled Brownian eigenvalue is of order `N`; therefore generic `ell^2` still loses exactly one factor of `N`. The new normal form does not hide that loss.

## 3. Complete residue averaging: exact Jordan-2 squares

If both parent and split residues are averaged over one complete common period, the centered carry variables satisfy

```text
Cov(X_d,X_e)=((d,e)^2-1)/(4de).
```

Hence every finite coefficient packet has exact energy

```text
1/4 sum_(q>=2) J_2(q)
    |sum_(q|d) a_d/d|^2.
```

This is `L-90417`. It gives exact coprime orthogonality and an elementary spectral bound

```text
periodized energy
 <= (1/4)(1+log D)^2 sum_d |a_d|^2.
```

Equivalently, the periodized deterministic packet is bounded by only a squared-logarithmic factor times its diagonal/Rademacher benchmark.

This is the precise common structure behind:

```text
complete-period carry energies;
Jordan-totient Bohr squares;
corrected Farey full-period positivity;
randomized Euler diagonal control.
```

## 4. Why this does not prove PIG

The actual PIG block freezes the parent endpoint. Complete-residue coprime orthogonality then fails badly.

Exact witness:

```text
N=100, d=49, e=47, (d,e)=1,
fixed covariance = 8/125,
periodized covariance = 0.
```

A second witness has

```text
Cov_100(40,45)=76/625,
periodized value=1/300.
```

This is `R-90416`.

Therefore the missing theorem is not another GCD-sum estimate. It is a source-specific control of the incomplete-period boundary which survives when the complete Jordan square is removed.

That is exactly where the repository's first Farey/Mertens cell and balanced Type-II firewall live.

## 5. New Rosetta stone

For one arithmetic source `f` and `c=1*f`, the same carry field has two exact quadratic coordinates:

```text
fixed endpoint / prefix coordinate:
    reflection Brownian bridge in c(N+1-m)-c(m);

complete residue / divisor coordinate:
    positive Jordan-2 square in sum_(q|d) f(d)/d.
```

The difference between them is the local arithmetic boundary. This connects the Q4/PIG, analytic-totient/Farey, carry/Pascal, and randomized-Euler lines without identifying their hard theorems falsely.

## 6. Preferred next theorem

A genuinely conclusion-producing continuation should prove, for the actual compact-Q4 source and the actual logarithmic block measure, a boundary transference estimate of the schematic form

```text
fixed-endpoint Brownian energy
 <= N^o(1) * periodized Jordan/diagonal energy
    + polynomial mean/collar forcing.
```

The theorem may not be source-independent: `R-90416` and the exact Mertens cell exclude that possibility.

An equivalent formulation is to control the reflection-difference tails

```text
[C(N)-C(N-R)]-C(R)
```

in the Brownian Green norm after the complete Möbius/four-adic siblings are recombined.

If such a source-specific transference holds with `N^o(1)` loss, then `L-90410` and `L-90417` give subpower innovation energy. After the separate PR #371 global-adapter repairs, this would be sufficient for pole exclusion.

## 7. Exact replay

```bash
python3 experiments/X-90416-brownian-jordan-carry-duality/verify.py \
  --json /tmp/verification.json
cmp /tmp/verification.json \
  experiments/X-90416-brownian-jordan-carry-duality/results/verification.json
```

Retained verdict:

```text
PASS_X_90416_BROWNIAN_JORDAN_CARRY_DUALITY
```

The finite checker verifies:

```text
529 complete-residue covariance identities;
260 Jordan-2 quadratic factorizations;
760 reflection Brownian-bridge row identities;
2 exact fixed-endpoint transfer counterexamples.
```

## 8. Honest boundary

```text
fixed-endpoint Brownian normal form          PROPOSED COMPLETE EXACT
complete-residue Jordan-2 factorization      PROPOSED COMPLETE EXACT
periodized deterministic/diagonal bound      PROPOSED COMPLETE EXACT
fixed-endpoint = periodized transfer          REFUTED GENERICALLY
source-specific boundary transference         OPEN / RH-BEARING
repaired global PIG-to-pole adapter            OPEN / PR #371
PIG and RH                                     UNPROVED
```
