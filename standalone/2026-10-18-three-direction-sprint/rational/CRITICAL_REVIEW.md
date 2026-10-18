# Independent component review of the critical arithmetic track

Reviewer: rational rough-core subagent, 2026-10-18. This is an independent
agent review and fresh-process replay, not a human referee report. It does
not integrate the proposed objects or change the repository's RH status.

Reviewed snapshots, SHA-256:

* `../critical/PROOF.md`:
  `b680acd936e78677b7c8390a7bb1c5171ea6f282f432f32b107682f35f42eeea`.
* `../critical/UNIFORM_PRIMES.md`:
  `64f286f355cd4e52834cc5649a987d3ac1cc3cb925d05317bce1977148bc50dd`.

Result: no analytic gap found in Theorems A--D, F--G at their expressly
stated sector scope. The complete unweighted critical energy estimate is
still open. I independently rederived the main coefficient identities,
uniform error costs, sign formulas and the growing-prime optimization.

The checks that matter for these conclusions are as follows.

1. For `a(p^j)=-(p-1)/p^j`, the Euler factors for the mean of
   `a(rd)a(sd)` and its coprime-ray correction agree coefficient by
   coefficient. The correction prime factors are absolutely summable
   against `n^-theta` for every fixed theta>1/2. Uniformity over arbitrary
   r,s requires the displayed `(rs)^epsilon`; bounded prime-support size
   permits the stated absolute uniform constant. Abel summation yields
   the uniform harmonic error, including `x<1`, where the explicit
   logarithm must be paid rather than silently set to zero.
2. The complete primitive-ratio ray formula retains every common factor
   d and all Gaussian tails. Its horizon shift contributes `-log(rs)/2`.
   This produces the PLUS `ell'_P(1/2)/2` in the uniform sector expansion.
   The support correction differentiates to the displayed positive
   `alpha_p`; no common-prime factor has been removed.
3. For fixed finite prime support the Fourier Euler factors
   `lambda_p(t)=1-2c_p Re(z/(1-z))` are strictly positive, including
   p=2. Both exponent directions at a prime are mutually exclusive by
   coprimality. The infinite prime-power sums converge absolutely before
   Fourier inversion and before differentiating; this is a different
   completion from a physical cutoff or a small-coordinate cutoff.
4. The lower bound for `log ell^(P)` uses a positive Fourier window near
   `pi/log P`. The discarded small-prime contribution is only
   `O(sqrt(P)/log(P)^2)`, smaller than the main scale. The fixed-prime
   harmonic error is not used with growing P without the new uniform
   resource. In that resource every local prime-power geometric series
   is included in `Xi_theta(P)`.
5. With `theta=1-2/log P`, the absolute resource has logarithm at most
   `(4e+o(1))sqrt(P)/log P`; its secondary local-factor error is
   `O(P^(1/4))` uniformly. Thus `P=kappa(log T)^2`,
   `kappa<1/(4e^2)`, makes the absolute remainder tend to zero. Relative
   bounds for `ell'_P` and the support correction follow from pointwise
   positive Fourier factors. They leave a positive main bracket and
   the displayed `2sqrt(kappa)log T/log log T` growth rate. This remains
   compatible with subpower growth of the full energy.

Two initial clarity requests were corrected before the above proof hash:
the fixed-prime sector formula explicitly specifies the Gaussian kernel,
and the numerical prime-ray tail fixtures specify their actual shift
`c=1/2`.

Fresh-process replay receipts are `CRITICAL_DIRECTED_REPLAY.json` and
`CRITICAL_UNIVERSE_REPLAY.json` in this directory. The first reran the
directed Gaussian checker at 192 bits with reduced-ratio cutoff 16384;
all three complete small-coordinate sign gates and nine prime-ray
fixtures passed. The second reran the prime-universe checker at 192 bits,
mesh 512 and largest prime cutoff 1000000; its independent complete-pair
versus Fourier checks and all whole-integral bounds passed. These are
fresh executions of the author's checkers, not an independently written
numerical implementation. The analytic review above is independent of
those replays. No finite receipt proves the open full-energy estimate.

## Additional compact-tent audit

I also independently derived the compact kernel identities used by
`../critical/certify_tent_energy.py`. Write `h=log 2` and
`psi(u)=(1-|u|/h)_+`. Its Mellin factor is

    2[cosh(h(s-1/2))-1]/[h(s-1/2)^2].

The value at the removable center is h, and all actual zeros lie on
`Re(s)=1/2`. Since `zeta(rho+1)` is nonzero at every nontrivial zeta
zero rho, every offcritical zero is retained by this detector.

For `b_n=a(n)/sqrt(n)`, the complete amplitude has slope jump at
`X=k/2` equal to

    [b_k-2*1_(2|k)b_(k/2)+1_(4|k)b_(k/4)]/h.

It vanishes for `X<1/2`, and only modes `n<=2T` contribute through T.
The cell integration formula is the exact integral of a squared affine
function of `log X`. For a prime ray p<q with `delta=log(q/p)<h`, the
two tents overlap on `[delta-h,h]` with exactly the three affine pieces
`[delta-h,0]`, `[0,delta]`, `[delta,h]`, truncated at
`log(T/(dp))`. The source coefficient is exactly
`a(pd)a(qd)/(d sqrt(pq))`, including shared primes. The source and common-
factor tails vanish beyond the stated compact endpoints. I found no
analytic, normalization or endpoint error in these identities. This
checks the mechanism; the author's final directed receipts require their
own separately recorded replay and code hash.
