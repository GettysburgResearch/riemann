# Independent review of the fixed-shift and signed-correlation component

Status: independent mathematical reconstruction by the primary agent, with
executed replay of the author's frozen checker. This is an AI review of a
standalone proposed result; it is not external referee or integrated acceptance.

## Frozen files reviewed

| File | SHA-256 |
|---|---|
| PROOF.md | `54527c0c30700c324835f5e8f6928db64357e161193eaca0880fce10254948cc` |
| ARITHMETIC.md | `786cb7a8c53986cb4d0cbd53695789de563ecbafd2e3e342fa2fbbf3e20fedbb` |
| verify.py | `3b7bf46af20ec72482567aec9d930591b2d082bcf1fca10da8ffc6288451ee9b` |
| replay.py | `25f50da48936bcb936a3d89103e06f13a73cab5e0035691f2b243a2296c91aaa` |
| SOURCES.md | `d467396946a6c918044d246474b1872c91c189f5c94ccbf402952cdc27683846` |
| VALIDATION.md | `a40f5c770ef9bee8d9b7e65b93ef0fd8f5440e6e4e3975101b4f9db2b1bc8365` |

All nine payload hashes in the author's handoff inventory were also checked
against the actual local bytes after replay. No file had changed.

## Reconstruction of the analytic bridge

I rederived both Dirichlet convolutions from their literal ideal sums. On
the normalized function f(X)/sqrt(X), a dilation by the ideal norm n has
coefficient n^(-h-1/2), and its finite-horizon norm uses the smaller interval
(0,T/n). This proves the two Minkowski bounds with exactly Z(h+1/2) and
Z(h+1/2)/Z(2h+1), including p=infinity. Absolute summability requires h>1/2;
there is no hidden interpolation in p or T and no critical-energy bound in
this argument.

I completed the square in the one-sided continuum integral and independently
obtained its erfc formula. Its normalized tail is O(X^(1/2-h)); therefore the
whole correction is in every critical Lp for h>1/2. On writing b=h-1/2 and
v=c-1/2, Mellin Plancherel gives the Gaussian weight
exp(2v^2-2t^2)/(b^2+t^2). Integrating this weight yields the stated continuum
norm, and taking the real part of 1/(b-it) gives the cross term b times that
norm squared. These checks fix the normalization and the direction of the
one-sided integral.

The single-shift sufficiency argument also reconstructs. The subpower energy
premise gives locally uniform Mellin convergence on Re s>1/2 by a dyadic
Cauchy estimate. At a zero rho there, the explicit rational subtraction is
regular unless rho=1-h, a case excluded by Z(1-h)!=0. Holomorphy of the
quotient then forces a zero at rho+h with at least the same multiplicity.
Repeating at this new zero eventually crosses Re s=1. A shifted numerator
pole cannot avoid the contradiction. No rightmost-zero or simplicity premise
is needed. The necessity direction explicitly assumes field RH before the
contour is moved; its reciprocal estimate is used only on a fixed zero-free
half-plane. The argument does not prove that reciprocal estimate
unconditionally.

For finite S, the removed Euler factors have their extra zeros on Re s=0.
They cause no exception to the right-half-plane argument. The legal universal
centered choice h=3/2 uses Z(-1/2)!=0, justified by the fixed-field functional
equation and the Euler half-plane. The ordinary h=1 choice correctly uses
zeta(0)=-1/2 and k_1=2.

## Reconstruction of the arithmetic statements

I independently derived a(p^j)=-(p-1)/p^j from the complete convolution and
completed the square in the product of the two normalized Gaussians. This
gives the exact ratio factor exp(-log(n/m)^2/8), factor 1/sqrt(nm), and normal
CDF argument log T-(log n+log m)/2-2v. At every finite horizon the positive
Gaussian majorant is integrable, which licenses the initial infinite double
expansion and its subseries. It does not license a subsequent infinite
large-horizon exchange without a separate majorant.

The squared local Euler factor and its value at s=1 give
G_p(1)=(p-1)(p+2)/(p^2+p+1). The absolute Dirichlet convergence for Re s>1/2
follows from the stated O(p^(-sigma-1)+p^(-2sigma)) local error. Convolution
with 1 then gives the claimed O(x^theta) error and the logarithmic harmonic
mean. At a prime dividing a fixed ray ratio, summing the full shared-prime
geometric tail gives beta(p^j)=-(p^2-1)/(p^j(p+2)); omitting those shared
primes would give a different constant.

For the fixed-offset result I read Tao's original primary preprint
[arXiv:1509.05422v4](https://arxiv.org/pdf/1509.05422), especially Theorem 1.3,
Corollary 1.5 and the subsequent Liouville nonpretentiousness discussion.
The published version uses Theorem 3 and Corollary 5. The prime values of a
differ from Liouville by 1/p, so the pretentiousness sums differ by at most
sum_p p^(-2), uniformly in the character and allowed real twist. This is
enough for the exact imported theorem. The argument pays each fixed offset,
with no claimed uniformity for a growing offset range. I did not reprove
Tao's entropy-decrement theorem.

For the infinite divisibility sector, the Gaussian ratio weight is summable
even after replacing |beta(r)| by 1. The normalized smoothed harmonic sum is
bounded uniformly in r because increasing r decreases the CDF argument.
This gives a valid dominated-convergence proof of the complete sector's
asymptotic. It avoids summing the uncontrolled O_r(1) constants. The full
primitive-ratio double series has a different behavior: comparable distinct
primes give a block of absolute size at least a constant times R/log^2 R.
I checked this divergence and the resulting prohibition on the double limit
exchange. A negative divisibility sector is consistent with the nonnegative
complete energy, and imposes a positive compensating contribution elsewhere.

## Executed checks and independent computation

I executed `critical/replay.py`. Its ordinary and optimized reports agreed
byte for byte, reproducing report SHA-256
`8a314267209f9fe2b62dd6035ef2ff2dbb7ebad92bdf257fceda6dfa0e30628c`.
The three separately executed optimized corruptions were rejected at their
specified gates: wrong beta(2), omitted prime powers and a changed Gaussian
ratio denominator. The count 2,573 includes repeated primitive guards; it
does not count independent analytic results.

I also wrote a separate computation of the infinite constant. It uses
convex midpoint/trapezoid rational quadrature for logarithms, a positive
Taylor expansion with its full geometric tail for exponentials, and 4,096
ray ratios on a 100-bit dyadic grid. It imports no part of the author's sign
checker and uses no transcendental library value. The whole omitted ray
tail is added with both signs. Its exact rational enclosure proves

    -9/5 < L_div < -17/10.

The displayed enclosure is approximately
(-1.7715054494689935,-1.7430583147069783). The decimal display is not used
for acceptance. Ordinary and optimized runs were byte-identical. This
independent program verifies the constant only; the preceding analytic
argument proves that the constant describes the infinite sector's limit.

The independent program and report are separate payload files, with their
own source review and manifest identities. This stronger enclosure does not
rewrite the author's frozen weaker certificate.

## Disposition and exact remaining gap

No substantive mathematical correction was required in the reviewed files.
The bounded bridge, fixed-offset imported-theorem deduction, local Euler
asymptotics, and infinite divisibility-sector sign are supported at their
stated scopes. The unknown assertion remains the subpower ONE-SIDED upper
bound for the complete nondivisibility contribution, or equivalently the
complete critical energy. None of the checks estimates that contribution,
proves uniform growing-shift cancellation, or supplies an RH proof.
