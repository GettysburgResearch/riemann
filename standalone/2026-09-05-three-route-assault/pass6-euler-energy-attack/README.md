# Pass 6: a direct signed Euler-factor attack

Status: proposed component proofs and exact finite checks; independent review required. **RH is not proved.**

This continuation attacks primewise multiplicative contraction rather than extending a tail estimate. It records the failure of that specific proposed final step using the genuine Mobius signs, quantifies it at all large prime cutoffs, and retains the horizon-correct arithmetic identity.

Read `PROOF.md`, then `REVIEW_AND_SOURCES.md`. The parent is PR #793 at `c4fedfcebf5226915969610281c650f452844fd8`. No preceding packet or its manifest is changed.

For a in (1/2,1), let P_X(s)=product_(p<=X,p!=67)(1-p^-s). Its physical energy is

    K_X(a)=(1/(2pi)) integral_R |P_X(a+it)|^2/(a^2+t^2)dt.

The proved logarithmic asymptotic is

    log K_X(a) ~ 2 X^(1-a)/[(1-a)log X],

while the diagonal tends to the finite constant

    zeta(2a)/[2a zeta(4a)(1+67^(-2a))].

This uses ACTUAL Mobius signs, not a changed source. The product has a growing spike near t=pi/log X. It does not follow that the full Mertens source has such a spike: almost all the approximant's normalized energy escapes past the horizon where its coefficients agree with the full arithmetic source.

The one-step contraction already fails for the three primes 2,3,5. At a=1, the scaled shift correlation is -11/1800 and the resulting energy exceeds its diagonal update by 11/900. The proof gives the strict sign for every a>0.

The exact stopped prime-insertion formula retains the signed correlation AND the lost boundary interval. A bound for the assembled stopped ledger would imply the required causal Mobius estimate; no such bound is supplied. This identity is not advertised as an advance in the RH-equivalent estimate itself.

A further check shows that polynomial prime cutoffs can automatically pass the Laguerre subexponential upper test even while retaining squarefree products as large as exp((1+o(1))N^2). The positive squarefree control still leaves its entire 3^N signal in the omitted set. Large included integers do not imply full source coverage.

## Reproduction

Python 3.10+; standard library only:

    python verify.py --check RESULTS.json --manifest
    python -O verify.py --check RESULTS.json --manifest
    python verify.py --self-test
    python -O verify.py --self-test

The suite reconstructs 489 exact finite controls and runs twelve unit/rejection tests. The large-X asymptotic is not inferred from a prime scan. No large prime sums or actual-zeta numerical computations are included.

This packet is a research result about an unsuccessful contraction mechanism. It is not a proof or disproof of RH, and makes no claim to external priority.
