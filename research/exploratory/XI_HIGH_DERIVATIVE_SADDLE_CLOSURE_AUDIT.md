# Independent audit: actual Xi high-derivative saddle closure

Status: exact-source review passed; the stated native analytic endpoint
theorem is accepted. Reverse-Rolle descent, XICURV107110, critical-line
proportions and RH remain open.

Reviewed source: 1b5547c3fcd1ba116106953f44a2ee4ceb81b525.
Programme copy: 48b3b3ecc62711edc417e62753a26b21aa6ad1d4.
Review date: 2026-08-31.

The root read the complete proof, producer, fixture, tests and manifest,
reconstructed the analytic estimates and reran the frozen checks. A separate
exact-SHA reviewer independently checked the argument, source bindings,
bounded arithmetic and additional formal-series controls. No mathematical
or machine repair to this frozen packet was required.

## Frozen identities

The five reviewed files have the following Git blobs:

- XI_HIGH_DERIVATIVE_SADDLE_CLOSURE.md:
  6ad6f85b53a18295f84306393118cbaf4d829627.
- xi_high_derivative_saddle_closure.py:
  de84ea884427709a1427cbc55b78cfe7c91c422a.
- xi_high_derivative_saddle_closure.json:
  a4fd3a1eba0353bbdd30bd40320d8c59a1f675b5.
- xi_high_derivative_saddle_closure.sources.json:
  6173a27246e686e2c81a80db0db6fee4980c2134.
- tests/test_xi_high_derivative_saddle_closure.py:
  cab8d1b08944b686ea0188eae139bad7172d97e1.

All seven repository source bindings authenticate by frozen commit, Git blob
and LF-normalized hash. The programme copy is byte-identical at the Git blob
level. The earlier claims are retained unchanged: this separate proof repairs
the interface rather than silently rewriting a frozen claim identity.

## Analytic review

1. The half-line cosine kernel is four times phi0; the full-line Fourier
   kernel is twice phi0. Both derivative parities and the scalar relation
   F_k=(-1)^k Xi^(k)/Z_k are correct. A positive scalar does not change the
   probability measure, but no frequency rescaling is made.
2. With b=9/2, the unique real saddle solves k/a+b=2*pi*exp(2a).
   Writing S=k/a gives precision Lambda=S/a+2S+9 and
   a=(log k-log log k-log pi+o(1))/2. The theta amplitude is bounded
   globally and tends to its asserted leading constant at the saddle.
3. The exact logarithmic ratio is a sum of two nonpositive losses.
   The three displacement ranges yield the global
   exp[-S min(s^2,abs(s))/16] upper bound, including the origin-side tail.
   The local second-derivative bound supplies the normalization reserve;
   log-concavity of the complete theta sum is not assumed.
4. The weighted moment estimate is uniform for H<=B sqrt(S), at fixed
   B and moment order. The near/far split and the explicit rational
   majorants M1=25758000 and M2=168980256 are valid. These deliberately
   coarse constants are sufficient and are not advertised as sharp.
5. The complex F, F-prime and F-second bounds retain the exponential
   height weight. The enlarged height is Hstar=max(H,1/(4a)).
   The disk and complement reference lower bound 1/10 is valid after
   normalization by exp(a abs(Im z)). Rouché and conjugation give one
   simple real zero in every selected full disk and none elsewhere in
   the rectangle. Disks meeting vertical boundaries do not determine
   an exact endpoint count.
6. The errors tend uniformly to zero whenever
   T_k+H_k=o(sqrt(k/log k)). The displayed Laguerre reserve follows from
   the F/F-prime/F-second errors, with the quadratic dependent term
   alpha^2 retained. Fixed strip height H=1/2 is permitted.
7. The central limit proof uses an integrable two-part bound for the
   unnormalized density. Weighted uniform integrability justifies the
   tail limit. At delta=C sigma and H sigma -> h>=0 the weighted tail
   tends to 4 exp(h^2/2) normal_upper_tail(C-h), which is positive for
   finite C,h. In particular the fixed four-sigma tail is eventually
   below 1/256, but is not exponentially small in k.
8. Growing windows A/sqrt(S) give the separate decaying-tail estimate
   under the stated height restriction. Neither that estimate nor the
   fixed-window result is substituted for the other.

The original full-disk tail condition at height H is insufficient if
H<1/(4u0). The finite two-atom R=511 control demonstrates the problem
analytically, without sampling hyperbolic functions. The corrected interface
requires the weighted tail at Hstar and holomorphy on a neighborhood of the
rectangle and full disks. A single finite exponential moment does not by
itself assert entire continuation. The corrected real and complex reserves
are adequate for the endpoint theorem.

## Prior art and attribution

Scaled cosine universality for high derivatives is established prior art,
not a newly discovered phenomenon. The root checked the primary accepted
manuscript of
[Gunns--Hughes, Theorem 3.1 and its proof, pages 10--11](https://eprints.whiterose.ac.uk/134951/1/ManyDerivsXi_Resubmitted.pdf).
It supplies the compact-domain comparison and the explicit saddle context.
The packet also cites the
[Ki 2006 publisher record](https://www.sciencedirect.com/science/article/pii/S0022314X05002489);
the author's and separate reviewer's abstract check is not misreported as
a successful root retrieval of that publisher page.

The growing-domain assertion and repaired constants are supported here by
the native proof, not by an inference that the cited literature contains
no stronger theorem. No external priority claim has been established.

## Reproduction and machine boundary

The root reran all 33 tests normally and with Python -O, both complete
producer checks, Ruff lint and format checks, and whitespace checks.
All passed. The producer also passed after import into the programme.
The separate frozen reviewer reported the same successful checks and seven
source authentications. Its additional 66 formal-coordinate/order controls,
including 96-bit boundary coordinates and orders 2 through 12, agreed with
an independently derived logarithmic-derivative formula; the largest
reported coefficient used 1058 bits, below the 4096-bit arithmetic cap.

The author additionally reported a clean fresh detached CRLF replay, both
producer modes, all 33 tests in both modes, and the 48 adjacent actual-kernel
and physical-band tests in both modes. These are separately attributed
checks, not extra tests silently counted in the root's 33.

The machine artifact proves only its finite exact algebra, source and
budget controls. Formal saddle coordinates are not claimed to be actual
transcendental saddles. No floating Xi evaluation, quadrature, sampled
zero location, or numerical proof of an asymptotic limit is used. The
analytic theorem has been mathematically reviewed, not formally verified.

## Acceptance boundary

Accept the repaired high-derivative endpoint and the stated weighted
concentration, Gaussian limit and localization results. Keep the source
fixture's historical subject-to-review label unchanged; this audit records
the later acceptance decision.

The exact reverse-Rolle ledger still has the unpaid sum of nonnegative
defects. A real/simple high derivative does not bound that sum. Nothing in
this packet controls descent to order zero, the full native Pick charge,
the infinite-inner exhaustion, a percentage of Xi zeros, RH, or GRH.

