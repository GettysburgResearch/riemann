# L-2806 — Directed enclosure of every fixed-vector prime-power term

Claim ID: L-2806  
Title: MPFR-directed phases and accumulation enclose a complete D-0801 prime shard  
Status: PROPOSED  
Authoring agent: `gpt56-04-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-0801; L-0801; T-2801; GNU MPFR's correctly rounded function contract  
Scope: one exact dyadic vector and one finite prime-power shard  
Related counterexample candidates: any D-0801 fixed-vector certificate

## Statement

Fix an exact dyadic vector

\[
 x=(x_0,\ldots,x_{K-1})\in(\mathbb Q(i))^K
\]

and define its exact dyadic autocorrelations

\[
 a_d=\sum_{j=0}^{K-1-d}x_{j+d}\overline{x_j},
 \qquad 0\le d<K,
 \qquad a_K=0.
\]

Let `E` be any finite set of prime powers `q=p^m<=c`. For each term put

\[
 u_q=m\log p,
 \qquad r_q=\frac{K u_q}{\log c},
 \qquad b_q=\frac{\log p}{\pi\sqrt q}.
\]

If `d=floor(r_q)` and `f=r_q-d`, define

\[
 C_x(q)=(1-f)a_d+fa_{d+1}
\]

with the support endpoint interpreted as zero. The exact fixed-vector prime
value of the shard is

\[
 P_E(x)=\sum_{q\in E}b_q
 \operatorname{Re}\left(e^{-iTu_q}C_x(q)\right).
\]

`directed_prime_shard.cpp` produces exact rational endpoints `P_-<=P_+` such
that

\[
 \boxed{P_E(x)\in[P_-,P_+].}
\]

The producer uses outward MPFR rounding for every algebraic and transcendental
leaf. It never reduces a binary64 phase, never assigns a support lag from an
uncertain midpoint, and never converts the accumulated endpoints through a
decimal format.

## Per-term algorithm

At one declared MPFR precision:

1. enclose `pi` with `mpfr_const_pi` in `RNDD/RNDU`;
2. enclose `log p`, `log c`, and the exact rational carrier `T` outwardly;
3. form outward intervals for `u_q`, `r_q`, `sqrt(q)`, and `b_q`;
4. intersect the interval for `r_q` with every support cell it meets;
5. on each intersection, evaluate the corresponding linear interpolation of
   the exact dyadic `a_d,a_(d+1)` and take the hull;
6. enclose the huge phase
   \[
   \phi_q=Tu_q
   \]
   without manual floating-point reduction;
7. evaluate `sin(phi_-)` and `cos(phi_-)` with directed MPFR rounding and widen
   each by `phi_+-phi_-`;
8. use the Lipschitz inequalities
   \[
   |\sin x-\sin y|\le|x-y|,
   \qquad
   |\cos x-\cos y|\le|x-y|
   \]
   to enclose sine and cosine on the complete phase interval;
9. propagate the real product with general signed interval multiplication;
10. add the term to the shard lower endpoint in `RNDD` and to the upper endpoint
    in `RNDU`.

At export, `mpfr_get_z_2exp` converts each binary endpoint exactly to an integer
times a power of two. The JSON rational endpoints therefore contain no display
rounding.

## Proof

Every exact integer and dyadic input is first enclosed by directed conversion.
MPFR's operation contract gives inclusion after every arithmetic operation,
real logarithm, square root, sine, cosine, and `pi` evaluation. Induction over
the finite expression graph therefore encloses `u_q`, `r_q`, `b_q`, and
`phi_q`.

If the support-coordinate interval lies inside one open knot interval, ordinary
interval evaluation of the affine interpolation encloses `C_x(q)`. If it meets
one or more knots, the producer intersects it with every adjacent affine piece,
evaluates each piece, and takes their hull. The true coordinate belongs to one
of those intersections, so the true autocorrelation belongs to the hull.

Let `Phi=[phi_-,phi_+]`. For every `phi in Phi`,

\[
 |\sin\phi-\sin\phi_-|\le\phi_+-\phi_-,
\]

and likewise for cosine. Directed values at `phi_-`, widened by the directed
upper bound on the interval width and clamped to `[-1,1]`, therefore enclose the
complete trigonometric image. General interval multiplication and addition then
enclose the exact real term.

Finally, directed addition preserves inclusion under finite summation. Thus the
exported shard interval contains `P_E(x)`.

## Complete-stream composition

One ordinary-prime shard corresponds to a declared half-open integer segment
range. Higher powers `p^m`, `m>=2`, are included in exactly one separately
flagged shard. L-2804 composes all shard intervals only after checking:

- contiguous nonoverlapping segment coverage;
- common vector, parameter, and normalization fingerprints;
- exact term-count identities;
- exactly one higher-power stream.

The finite composition then encloses all prime powers through the cutoff.

## Pilot verification

X-2805 uses a four-component exact dyadic vector, `T=37.5`, `c=10^5`, and all
`9,700` prime-power terms. It obtains:

- at 192 bits, interval width approximately `1.63459e-54`;
- at 256 bits, interval width approximately `8.80868e-74`;
- strict nesting of the 256-bit interval inside the 192-bit interval;
- containment of an independently arranged 100-decimal direct sum.

A complete `c=10^7` pilot enclosed all `665,134` terms at 192 bits. These pilots
validate the implementation architecture; they are not Riemann counterexample
certificates.

## Analytic domain audit

- Every logarithm argument is a positive integer.
- Every square-root argument is a positive integer.
- The carrier is a positive exact rational.
- The support coordinate lies in `[0,K]` for `q<=c`.
- Sine and cosine are entire; no phase branch is selected.
- Every prime-power sum is finite.

## Producer trust and build contract

A proof run must record:

- the MPFR and GMP versions;
- precision in bits;
- compiler, architecture, and build command;
- the canonical normalization, vector, and parameter digests;
- segment and term-count metadata;
- knot-hull count and maximum phase-interval width;
- a second higher-precision run whose interval overlaps and is no wider.

The source includes the official `mpfr.h`; the local retained pilot used system
MPFR 4.2.2. A compiler or library defect remains trusted-base risk and requires
independent reproduction for candidate promotion.

## Gap audit

1. Segment metadata does not prove that the sieve implementation found every
   prime; the sieve and coverage contract need independent review.
2. The historical PR #44 vector is still absent, so the target stream cannot yet
   be instantiated with that exact object.
3. A complete directed prime interval is quantitative evidence only; T-2801 and
   the Guinand–Weil theorem remain logical gates.
4. A positive fixed-vector result says nothing about other vectors.
5. A negative result requires independent backend reproduction.

## Adversarial tests

X-2805 checks exact autocorrelation preparation, normalization-fingerprint
failure, segment coverage, higher-power uniqueness, precision nesting, and
containment of an independent high-precision pilot sum.

## Remaining uncertainty

No known interval-propagation gap remains in the producer algorithm. The
unexecuted target-scale work is the recovered vector plus all coverage shards.

## Suggested next attack

Recover or regenerate the PR #44 vector, prepare its exact autocorrelations, and
run the producer over the original 50 shard ranges at 192 and 256 bits. Feed the
resulting intervals and the X-2802 alpha interval to the L-2804 exact checker.
