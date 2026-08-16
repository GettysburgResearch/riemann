# Review specification

Frozen target:

```text
PR #498
6cc0da2fa5711017e260ebdcea4ba8c22e453288
```

## Required reconstruction

1. Derive the centered endpoint cells with reflected predecessor `N-j-1`.
2. Verify the Bernoulli weight has mean zero and squared norm `1/180`.
3. Reconstruct the cubic Riesz identity and the factor `N/180` in Cauchy.
4. Derive the Mellin multiplier and verify every open-strip zero survives.
5. Prove the `O(1)` integer-to-real interpolation.
6. Reindex the contracted source into the scale-four wavelet `F` and retain the separate four-adic gauge.
7. Verify the complete prime-tower geometric formula and the `p<=sqrt(N)` bound.
8. Verify both zero Mellin moments, the first nonzero logarithmic moment, and all four exact grid formulas.
9. Reconstruct the exact Vaughan identity with signs `+,+,-,+`.
10. Verify the grouped coefficient `a_U(m)=sum_(d|m,d>U) mu(d)`.
11. Check all Type-I estimates and the `m l <= N^(3/4)` Type-II estimate without Möbius cancellation.
12. Verify the First-Hermite Fourier transform and Calderón formula.
13. Confirm that BCD remains open and no RH-strength input is hidden in the preceding steps.
14. Run the exact replay, mutation checks, and SHA-256 ledgers.

## Immediate falsifiers

Reject at the first failure of:

- the scale-four coefficient `4`;
- the separate power-of-four gauge;
- either Mellin moment;
- any residue-class grid identity;
- the strict divisor threshold `d>U`;
- the Vaughan minus sign;
- the low-product support split;
- the Mellin or additive transform normalization;
- the stated absence of CPBD, a Mertens square-root bound, or First-Hermite one-carrier positivity as an input.

## Computation scope

The replay is lightweight and exact-rational. It does not test prime cancellation, compute zeta zeros, rerun large endpoint campaigns, or certify BCD/RH.
