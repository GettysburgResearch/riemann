# BHH26: the actual branching orbit is eventually critical-line confined

**PROPOSED COMPLETE COMPONENT THEOREM; independent mathematical review required.
RH and the remaining bounded-but-growing confinement problem are OPEN.**

This continuation starts from PR #857 at
`3f1984867d23b588d09c88a892882411724b174b`. It adds a new directory without
editing the prescribed Gamma(5/2) orbit, earlier source, or research status.

## The theorem

For EVERY fixed depth n in the actual shared-uniform branching recursion,
there is a finite T_n such that every zero of H_n in
`0<=Re s<=1, |Im s|>=T_n` is simple and on Re s=1/2. There are infinitely
many such zeros. The identical assertion holds for the parent's entire E_n.

The proof identifies every finite Laplace singularity and keeps its lower
logarithmic terms. The leading coefficients obey

```
b_(n+1,j)=b_(n,j)^2-2b_(n,j-1)^2,
P_n(v)=sum b_(n,j)^2 v^j.
```

Their growth forces every root of P_n into |v|<=1/4, away from v=2^-s
on the critical strip. A complete rotated-ray Mellin remainder gives

```
M_n(s)=c_n^2 Gamma(beta_n+s/2)/Gamma(beta_n)
        * (pi/15)^(s/2) P_n(2^-s) [1+e_n(s)],
beta_n=3*2^n+2,
e_n, e_n' = O_n(log(2+|Im s|)^(2^(n+1))/|Im s|).
```

The derivative bound is on the closed critical strip, using a wider strip
for Cauchy. This eventually recovers strict modulus-ratio monotonicity,
despite its certified failure at depth one and height23. The fixed-depth count is

```
N_n(T)=T/(2pi) log(pi*T/(30*4^n))-T/(2pi)+O_n(1).
```

These are paper proofs, not extrapolations from finite algebra. No numerical
T_n is certified and NO uniform joint height/depth threshold is proved.
In particular this is not an RH proof: off-central zeros can still persist
in |Im s|<T_n as n grows. Section7 states the exact missing conclusion.

## Reading and execution

Read [PROOF.md](PROOF.md), especially Sections2--5; then
[SOURCES.json](SOURCES.json) and [VALIDATION.md](VALIDATION.md).

```
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

The exact standard-library checker authenticates every packet file and
reconstructs bounded coefficient, local-pole and Gaussian-rational identities.
It does not evaluate a high-height zero, zeta, a contour integral, or the
unevaluated asymptotic constants. `--write` is producer-only, not acceptance.

## Review questions

1. Does the differential-dilation identity retain the shared-uniform factor2?
2. Does the local Laurent-log induction control both banks and derivatives,
   without treating branch singularities as meromorphic poles?
3. Does the rotated contour bound pay all n+1 singular neighborhoods, zero,
   compact complements and the full infinite ray?
4. Is the gamma reflection cancellation and one-power relative saving valid?
5. Are the polynomial phase bound, simplicity and fixed-depth count correct?
6. Are the two limit orders kept distinct in every claimed RH implication?

Classical beta-gamma algebra, Enestrom--Kakeya, gamma identities, contour
rotation and Hurwitz are credited. No external priority, independent acceptance,
Lean verification or full repository build is claimed.
