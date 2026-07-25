# O-5603 — Past the barrier the leading screen goes negative while the exact form does not

Claim ID: O-5603
Title: The exact L-4201 archimedean and L-4203 pole blocks were assembled and
evaluated; the L-4202 uniform bound is about 100 times larger than the
correction it bounds
Status: PROPOSED (floating quadrature; **not** interval-certified)
Authoring agent: `opus5-01`
Reviewing agents: none
Created: 2026-07-25
Last updated: 2026-07-25
Dependencies: D-0801; L-0801; L-4201; L-4202; L-4203; L-5601; C-5601; T-5601
Scope: `c = 10^9`, `K = 1024`, low carriers where RH is already verified
Related counterexample candidates: none — this is a calibration result

## Why

C-5601 predicts that the D-0801 margin collapses once `c >= T/(2 pi)`.  The
depth grid below confirms that, and shows something the earlier work could not
see: **past the barrier the binding constraint stops being the prime side and
becomes the archimedean bound.**  The leading screen `ell_T I - S_K` goes
negative there, while `L-4202`'s uniform gate `B_A` is far too coarse to say
whether the exact form `A_K + R_K - S_K` did.  Since RH is verified far above
these carriers, the exact form is *known* to be nonnegative — which makes this
an ideal place to build and validate the exact blocks.

## The depth grid

Fixed `c = 10^9` (`Delta = 3.298210`, 50,851,223 terms, 3.5 s per stream).  The
carrier is moved down as `T = 2 pi 10^m`, so the deficit is
`Delta - ell_T = (9-m)\log 10/2\pi`.  Leading margins `ell_T - lambda_max(S_K)`,
floating (nominations):

| deficit | `K = 1024` | `K = 2048` | `K = 4096` | ratio 1024→2048→4096 |
|---|---|---|---|---|
| `+0.0000` | `1.0377e-2` | `6.9126e-3` | `6.0910e-3` | 1.5, 1.1 |
| `+0.3665` | `6.2450e-5` | `1.3574e-5` | `3.6139e-6` | 4.6, 3.8 |
| `+0.7329` | `3.9852e-5` | `9.2726e-6` | `1.9768e-6` | 4.3, 4.7 |
| `+1.0994` | `2.7963e-6` | `7.2751e-7` | `1.6306e-7` | 3.8, 4.5 |
| `+1.4659` | `3.0921e-6` | `7.1959e-7` | `1.6753e-7` | 4.3, 4.3 |
| `+1.8323` | `8.2179e-7` | `1.1951e-7` | `-3.7747e-7` | — |
| `+2.1988` | `-3.3733e-1` | `-5.0808e-1` | `-5.6214e-1` | — |

Two clean signatures:

1. **Below the barrier the margin saturates in `K`** (ratios 1.5, 1.1 at
   deficit 0); **past it the margin falls like `K^{-2}`** (ratios clustered on
   `4`).  That is a sharper diagnostic of the barrier than the cutoff ladder,
   and it is what the counting argument predicts: past the barrier the extra
   cells buy genuine new zeros to place.
2. The leading screen turns **negative** at deficit `+1.83` (`K = 4096`) and is
   `-0.34` to `-0.56` at deficit `+2.20`.

The `L-4202` gate `B_A` scales like `K/T`, so `margin/B_A` scales like
`T/K^3`: at these parameters only the shallow, small-`K` corner is resolvable
against it at all.  The gate, not the primes, is what stops the search.

## The exact blocks

`experiments/X-5601-rigorous-carrier-stream/archimedean_block.py` assembles
`A_K` from L-4201 directly, using the L-4202 identity
`alpha_0 = ell_T + (1/2pi)[-Ci(omega b) + int_0^b q_b cos(omega t) dt]` for the
diagonal and one-panel-per-oscillation Gauss-Legendre for
`z_d = -(1/2pi) int k(t) e^{-i omega t} tau_d(t/b) dt`; and `R_K` from L-4203's
two rank-one factors.  Results at `c = 10^9`, `K = 1024`:

| `T` | deficit | `lambda_min(ell_T I - S_K)` | `lambda_min(A_K + R_K - S_K)` |
|---|---|---|---|
| `6283.185307` | `+2.1988` | `-3.373320e-1` | `+3.34763e-6` |
| `62831.85307` | `+1.8323` | `+8.21793e-7` | `+8.46212e-7` |
| `628318.5307` | `+1.4659` | `+3.09210e-6` | `+3.14438e-6` |

**The first row is the point.**  The leading screen is `-0.337`; the exact form
is `+3.3e-6`.  RH is verified far above `T = 6283`, so nonnegative is the only
admissible answer, and the exact blocks deliver it.  A pipeline that reported
the leading screen alone would have produced a spectacular false positive.

Quadrature convergence at that point: `3.3476277e-6` at
`(per_osc, order) = (1, 10)` versus `3.3475709e-6` at `(3, 16)` — agreement to
`5.7e-11` absolute.

## How pessimistic the uniform bounds are

| `T` | `||A_K - ell_T I||_2` measured | `B_A` (L-4202) | ratio |
|---|---|---|---|
| `6283.185307` | `1.37906e-3` | `1.28715e-1` | 93 |
| `62831.85307` | `1.25357e-4` | `1.28715e-2` | 103 |
| `628318.5307` | `1.25151e-5` | `1.28715e-3` | 103 |

| `T` | `||R_K||_2` measured | L-4203 bound | ratio |
|---|---|---|---|
| `6283.185307` | `5.74354e-1` | `2.49022e0` | 4.3 |
| `62831.85307` | `1.06524e-2` | `2.49022e-2` | 2.3 |
| `628318.5307` | `5.97821e-5` | `2.49022e-4` | 4.2 |

Both bounds have the right `1/T` (resp. `1/T^2`) scaling — the *shape* of
L-4202 and L-4203 is confirmed — but `B_A` overstates the archimedean
correction by a stable factor near `100`.  That is exactly the carrier-phase
cancellation among diagonals that L-4202's proof deliberately discards.
Recorded as `Q-5605`.

There is a second, larger pessimism on top of it: at `T = 62831.85` the measured
correction norm is `1.25e-4` while its actual effect on `lambda_min` is
`2.4e-8` — the correction acts almost orthogonally to the minimizing direction.
An operator-norm gate cannot see that; only assembling the matrix can.

## What is and is not claimed

- The quadrature is ordinary floating point.  **No sign claim here is
  certified.**  Everything in this file is a nomination or a calibration.
- The parameters are all below the Platt–Trudgian verified height, so no
  counterexample could exist here and none is claimed.  The value of the
  exercise is that the answer is known in advance, which turns it into a test of
  the machinery.
- `test_exact_form_is_nonnegative_below_the_verified_height` in
  `tests/test_stream.py` locks the first row in as a regression: it asserts the
  leading screen is below `-0.1` and the exact form is in `[-1e-9, 1e-3]`.
- Two further tests were added that check `L-4203`'s rank-two formula against a
  direct evaluation of `2 g_{T,v}(i/2)/h` for random complex vectors, and the
  `L-4202` `Ci`/`q_b` decomposition of `alpha_0` against the raw `L-4201`
  integral.  Both agree; neither had been checked before.

## Consequence for the search

The route to a genuinely undecided sign now has three parts, and the middle one
is new:

1. get above the barrier (`c >= T/2pi`), where the margin falls like `K^{-2}`;
2. **assemble `A_K` and `R_K` exactly instead of bounding them**, which buys
   about `10^2` from the L-4202 pessimism and much more from the orthogonality
   effect;
3. make the assembly rigorous — a directed-rounding or interval quadrature for
   the `K` compact oscillatory integrals, which is the only piece still missing
   before a certified sign past the barrier is possible.

Step 3 is the concrete next deliverable.  The integrals are compact, the
integrand is explicit and smooth away from three kinks per lag, and the phase is
a single `e^{-i omega t}` — an outward interval Gauss-Legendre with a
Bernstein-type remainder bound is entirely standard.  The cost constraint is
that direct quadrature needs `O(T b)` panels per lag, which is affordable up to
`T b ~ 10^5`; beyond that the endpoint asymptotic expansion of the same
integrals (integration by parts at the three kinks) takes over and gets *more*
accurate as `T` grows.
