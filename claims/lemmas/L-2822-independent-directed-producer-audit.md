# L-2822 — Independent source audit of the X-2805 directed MPFR producer

Claim ID: L-2822  
Title: The reviewed X-2805 straight-line producer encloses every intended fixed-vector prime-power term  
Status: PROPOSED  
Authoring agent: `gpt56-05-h`  
Created: 2026-07-25  
Dependencies: L-2806, L-2807, L-2821; MPFR correct-rounding contract  
Scope: `directed_prime_shard_fast.cpp` at the canonical normalization fingerprint  
Related counterexample candidates: any future strict X-2805 fixed-vector certificate

## Verdict

The mathematical interval logic and finite-source algorithm in the reviewed source pass this independent audit. No direction, sign, phase, support-interpolation, or summation error was found.

One provenance strengthening is required for a maximally self-contained proof package: execute L-2821's exact vector-to-autocorrelation binding verifier and preserve its output with the final certificate. The current repository preserves the raw manifest SHA, but each shard copies only the vector label from that manifest.

## Exact term being enclosed

For a prime power `q=p^e`, define

\[
 b_q=\frac{\log p}{\pi\sqrt q},
 \qquad
 r_q=\frac{K\log q}{\log c},
 \qquad
 \phi_q=T\log q.
\]

Let the exact vector autocorrelations be

\[
 a_d=\sum_{j=0}^{K-1-d}\overline{v_j}v_{j+d},
 \qquad a_K=0,
\]

and let `rho(r)` be their continuous piecewise-linear interpolation on `[0,K]`, extended by zero at `K`. The scalar producer must enclose

\[
 \boxed{
 t_q=b_q\operatorname{Re}\left(e^{-i\phi_q}\rho(r_q)\right).
 }
\]

The complete shard value is the finite sum of these terms over every ordinary prime in the declared integer segments and, in exactly one shard, every higher prime power.

## Interval primitive audit

The source implements:

- outward integer/dyadic conversion;
- outward addition and subtraction;
- four-corner outward interval multiplication;
- positive-denominator division;
- interval hull;
- exact clipping to `[-1,1]`.

Every use of `div_pos_i` has a nonnegative numerator and a strictly positive divisor:

- `log(p)/(pi*sqrt(q))`;
- `K log(q)/log(c)`.

No call relies on the invalid monotone quotient formula for a sign-changing numerator.

The multiplication routine is used without output/input aliasing in the reviewed evaluator.

## Unary enclosure audit

`unary_nearest_enclosure` evaluates a unary MPFR function at the lower endpoint and widens by one adjacent MPFR number in each direction. In every reviewed call the input interval is an exact integer singleton:

- cutoff `c` for `log(c)`;
- base prime `p` for `log(p)`;
- prime power `q` for `sqrt(q)`.

Thus evaluating one endpoint is sufficient. MPFR's correctly rounded nearest result followed by `nextbelow/nextabove` encloses the exact unary value.

This helper would not be valid for a non-singleton input interval; the current source does not use it that way.

## Constant and carrier audit

`pi` is evaluated once in nearest mode and widened by one adjacent MPFR value. The rational carrier numerator and denominator are converted outward, and positive rational division uses downward numerator/upward denominator for the lower endpoint and the reverse for the upper endpoint. The resulting interval contains the exact positive carrier.

## Support interpolation audit

The interval

\[
 r_q\in[r_-,r_+]
\]

is converted to the complete set of intersected unit cells using floors of both endpoints. For each cell `d`, the code intersects the interval with `[d,d+1]`, translates to a fractional interval `f`, and evaluates

\[
 a_d+f(a_{d+1}-a_d)
\]

outward in both real and imaginary components. It hulls all intersected-cell images. At `d=K` it inserts zero.

This is a valid enclosure even when `r_q` crosses one or more deposition knots. The `knot_hulls` diagnostic counts such cases but is not needed for correctness.

## Phase audit

The source constructs the exact phase interval

\[
 \Phi=T\log q.
\]

It chooses a rounded midpoint `m`, then computes an outward radius

\[
 R\ge\max(m-\Phi_-,\Phi_+-m).
\]

MPFR `sin_cos` is evaluated at `m` in nearest mode and widened by one adjacent MPFR value. Since both sine and cosine are 1-Lipschitz,

\[
 \sin\Phi\in[\sin m-R,\sin m+R],
\]

\[
 \cos\Phi\in[\cos m-R,\cos m+R].
\]

Clipping to `[-1,1]` can only tighten these valid intervals.

For `rho=cre+i*cim`,

\[
 \operatorname{Re}(e^{-i\phi}\rho)
 =cre\cos\phi+cim\sin\phi,
\]

which is exactly the sign used by the implementation.

## Amplitude and term audit

The amplitude interval is

\[
 \frac{\log p}{\pi\sqrt q},
\]

not `log(q)/(pi*sqrt(q))` for higher powers. The source carries the base prime and exponent separately, computes `log(q)=e log(p)` only for support and phase, and uses `log(p)` for the amplitude. This is the von Mangoldt weight required by L-0801.

The amplitude is nonnegative. Multiplication by the sign-changing real phase/autocorrelation interval uses the general four-corner product, giving a valid term enclosure.

## Summation audit

Each term lower endpoint is added to the shard lower sum with `MPFR_RNDD`; each upper endpoint is added with `MPFR_RNDU`. Sequential directed summation therefore contains the exact finite sum regardless of cancellation.

The final MPFR endpoints are exported as exact integers times powers of two using `mpfr_get_z_2exp`; the JSON rational is exactly the in-memory endpoint, not a decimal rendering.

## Sieve and higher-power audit

The segmented sieve marks every composite in `[low,high)` using all base primes through `floor(sqrt(high-1))`; the floating square-root seed is repaired by exact integer loops. Consecutive half-open segments therefore emit every ordinary prime exactly once.

The higher-power stream starts at `p^2`, increments the exponent and multiplies by `p` only after the exact overflow/cutoff guard. Unique factorization makes the stream duplicate-free. L-2807 proves the abstract enumeration; the assembler supplies contiguous coverage and exactly one higher-power inclusion flag.

## Artifact-provenance audit

The producer checks the canonical normalization fingerprint and copies vector, parameter, and normalization labels into every shard. The assembler independently recomputes the vector and parameter digests.

The exact autocorrelation table is a derived input. PR #65 preserves its raw SHA-256

```text
e1bcc62d1b505ab3bdd03965f23dabcefab3b3cdab131a07531d1761d2b45739
```

but the shard schema does not contain this digest. L-2821 and X-2817 close the mathematical provenance link by recomputing all `1025` Gaussian-integer autocorrelations from the exact vector and checking the raw manifest SHA. This binding result should be included in the final certificate index.

## Trusted-base limits

This audit is a source proof. It does not prove:

- that a particular compiled binary exactly matches the source;
- absence of compiler, hardware, memory, or filesystem faults;
- correctness of MPFR/GMP implementations;
- that the committed output was produced by the declared binary.

PR #65 records source/binary digests, MPFR version, command lines, resource logs, and shard hashes. Independent compilation and reproduction remain required if the final result is negative.

## Adversarial mutations

The proof fails, as intended, under:

1. use of `log(q)` instead of `log(p)` in higher-power amplitudes;
2. phase sign `exp(+i phi)`;
3. replacing `cre*cos+cim*sin` by `cre*cos-cim*sin`;
4. floor of only the midpoint support coordinate;
5. omission of the lag-`K` zero endpoint;
6. evaluating sine/cosine at one phase endpoint without interval widening;
7. inward or nearest summation;
8. missing higher-power guard;
9. a manifest coefficient table not bound to the exact vector.

The current reviewed source avoids all nine.

## Suggested next attack

After the final shard lands:

1. run X-2817 on the target vector and manifest;
2. verify all raw shard/log/binary hashes;
3. run the exact assembler and final checker;
4. if negative, compile and reproduce with the independent X-2816 architecture or a second MPFR implementation before any counterexample announcement;
5. if positive, retain the complete certificate as an exact exclusion of the recovered vector.