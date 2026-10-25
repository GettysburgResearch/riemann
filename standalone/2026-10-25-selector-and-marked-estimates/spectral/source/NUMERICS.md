# Full-source numerical experiments and their limits

**EMPIRICAL, ordinary arbitrary precision; not interval-certified.**
No finite experiment proves a new zero-free half-plane. The matrix contains
the full semilocal prime-power sum and the complete analytic archimedean
tail. No zeta zero, fitted root, or imported quasi-RH bound is an input.

## Reproduction

Requires `mpmath==1.3.0` in the tested environment. The exact algebra checker
uses only the Python standard library.

```sh
python -I -S -B verify.py
python -I -S -B -O verify.py
python -B experiment.py --a 1.3 --modes 16 --dps 120 --order 192 --output /tmp/N16.json
python -B experiment.py --a 1.3 --modes 16 --dps 150 --order 256 --output /tmp/N16-replay.json
python -B validate_numerics.py
```

`results/` retains seven experiment reports: four mode cutoffs at a=1.3,
a higher-precision/quadrature replay, a larger-window experiment, and a
prime-deletion negative control. Each reports all normalized coefficients,
all prime powers, all shifts, parity minima, log coefficients and comparison
values. There are THREE shift choices per report: the explicit safe shift,
a shift below the numerical finite minimum by 10^(-12) times its magnitude,
and a fixed 10^(-6) gap. The near-bottom choice is not certified below the
continuum minimum. These 21 cases are not independent theorem validations.

The experiment rejects unresolved minima near the working precision. This
is a guard, not an interval proof. A finite positive matrix is not a lower
certificate for the full operator.

## Matrix derivation

Put D=2a and e_n(x)=exp(2pi i n x/D)/sqrt(D) on [-a,a]. Define

    A(t)=exp(-t/2)/(1-exp(-2t)),    k_n=2pi n/D,
    S_n=integral_0^D A(t)sin(k_n t)dt
           +sum_(p^j<=exp D) (log p)/sqrt(p^j) sin(k_n log(p^j)).

For m!=n the paired correlation of e_m,e_n is

    (-1)^(m-n) [sin(k_m t)-sin(k_n t)]/[pi(n-m)].

For m=n it is 2(1-t/D)cos(k_n t). These are obtained by integrating
the actual overlapping support intervals, not by periodic wrap-around.
The pole matrix before the centered-basis sign is

    P_mn=32D sinh(D/4)^2 (D^2-16pi^2 mn)
                 /[(D^2+16pi^2 m^2)(D^2+16pi^2 n^2)].

Thus the off diagonal is

    (-1)^(m-n)[P_mn-(S_m-S_n)/(pi(n-m))].

The diagonal is P_nn minus log(4pi)+gamma, minus

    integral_0^D A(t)[2(1-t/D)cos(k_n t)-2exp(-t/2)]dt,

plus the exact tail 2atanh(exp(-D)), minus the complete prime-power
paired-correlation sum. The singular integrand is evaluated with `expm1`
and sin-squared identities to avoid catastrophic cancellation at zero.
Gauss--Legendre nodes and weights are refined at working precision, rather
than inherited as double-precision quadrature weights.

Parity blocks have entries E_00=Q_00, E_0j=sqrt(2)Q_0j,
E_ij=Q_ij+Q_i,-j for i,j>0, and O_ij=Q_ij-Q_i,-j.
The normalized Fourier transform is evaluated from the exact sinc expansion,
not from sampled FFT peaks.

## What the finite comparisons actually show

At a=1.3 the full source includes the nine prime powers
2,3,4,5,7,8,9,11,13. For the near-finite-bottom resolvent, at z=10:

| Full matrix dimension | Numerical even minimum | Error before gauge | Error after Gaussian gauge |
|---:|---:|---:|---:|
| 33 | 1.6199e-35 | 0.0119093 | 0.000555264 |
| 49 | 4.32284e-44 | 0.00153465 | 0.000118215 |
| 65 | 1.20885e-50 | 0.00756236 | 3.02513e-05 |
| 97 | 2.31538e-58 | 0.0116337 | 6.41661e-07 |

The gauge is precisely exp((V-V_X)z^2/2); it matches the quadratic
coefficient to Xi and leaves ALL zeros unchanged. This is a disclosed fitted
normalization, so the second coefficient is not independent evidence.
The higher coefficients and other comparison values are reported without
being fitted. In particular, these are function errors, not zero-location
errors or a verified zero height.

The raw comparison is NOT monotone across these cutoffs. At the larger
window a=1.8, N=24, the compensated z=10 error is about 0.000780, worse
than the a=1.3,N=24 value. Thus the runs do not establish convergence as
the interval expands. Increasing only the matrix dimension at a fixed
interval cannot supply the required cofinal arithmetic result.

Removing the prime terms gives numerical even and odd minima about
-0.863 and -2.001 and a very different normalized transform. This control
shows the calculation is using the arithmetic source, not that adding
primes proves global positivity.

## Executed validation

- Ordinary and optimized `verify.py` outputs agree byte-for-byte. Seven
  groups of exact rational algebra are checked, including a counterexample
  to generic positive-matrix reasoning and the theta differential factors.
- Four deliberately incorrect optimized runs reject at their intended
  division, rank-one, prime-power, and theta-normalization checks.
- The N=16 experiment at 120 digits/192 nodes was rerun under Python `-O`;
  the entire report agrees byte-for-byte.
- Its 150-digit/256-node replay gives identical stored 60-digit normalized
  coefficients. This is agreement between numerical implementations of
  the same formula, not a rounding certificate.
- Independently integrating the 25 actual overlap pairs of the N=2 matrix
  with adaptive quadrature agrees with the closed divided-difference
  assembly to about 7.25e-71. The complete archimedean tail is analytic in
  both calculations. The Taylor recurrence also agrees with differentiation.
- An early exploratory combined run hit the process timeout. The retained
  N=48 report was subsequently completed in a separate execution; no
  partial output is accepted. Exploratory fixed-gap failures motivated
  reporting all three shift rules rather than silently selecting a good one.

The cross-check scripts and proofs have the same author. No separate agent,
human referee, proof assistant, interval backend, repository-wide CI, or
complete-source independent implementation is claimed.
