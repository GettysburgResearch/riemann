# Square-width capture of the full residual

Status: PROPOSED COMPLETE COMPONENT PROOFS; independent review required.
**RH and the arbitrary-rank arithmetic lower bound remain unproved.**
Base: PR #790 at 513d8f206bb597747afcb7a7410cdf768519d548.
All additions are confined to quadratic-capture-pass8/.

## The main result

Keep u_j(t)=exp(-t)[t^(j-2)/(j-2)!-t^(j-1)/(j-1)!] and the ORIGINAL
L2 metric. Let Pi_(m,d) project onto span{u_m,...,u_(m+d)}. Put r=m-2.
If d/r^2->c as r tends to infinity, the new proposed theorem is

    Pi_(m,d) -> multiplication by 1_[1/(2c),infinity)

STRONGLY. The conventions are zero projection at c=0 and identity at
c=infinity. The finite tests all have integral zero; that constraint is
retained in the proof, and its disappearing rank-one complement is proved
rather than assumed harmless.

A first-order energy bound strengthens the old escape estimate:

    int_0^T |f(t)|^2 dt <= 2T(d+1+r)/r^2 ||f||^2.

An exact independent calibration in the one-dimension-larger space
W_(r,n)=t^r exp(-t) Polynomials_(<=n) is

    ||P_W exp(-t)||^2/||exp(-t)||^2=(n+r)!^2/[n!(n+2r)!].

Its limit is exp(-1/c), checking the factor 2 and proving sharpness of the
quadratic threshold. This is a theorem about projections, not an experiment.

## Consequence for the actual xi source

For the parent's trace-class Gamma_0(s,t)=S(s+t),

    ||Pi Gamma_0 Pi-P_a Gamma_0 P_a||_1 ->0,
    P_a Gamma_0 P_a is a shifted copy of Gamma_(2a), a=1/(2c).

Thus at the concrete square-width schedule d=(m-2)^2 the actual finite
matrices retain Gamma_1, including EVERY hypothetical negative direction.
They do not drift to zero. Their negative traces converge to Tr(Gamma_1)_-.
If RH fails, all sufficiently large matrices detect it. No zero locations
are used to select the spaces, and no spacing or finite-verification input
is used. The inherited heat-Hankel inertia theorem is an explicit dependency.

Every finite raw matrix uses only h=X'/X and derivatives at the one safe
invariant point u=1. PROOF.md gives both the exact factorial metric and
Q_jk=s_(j+k-2)-2s_(j+k-1)+s_(j+k). The correct normalized compression is
G^-1/2 Q G^-1/2, not a Euclidean interpretation of raw entries.

## A signed prime-tail theorem in the nonescaping regime

ENDPOINT_DEFECT.md uses the actual square-width projections f_r of
f(t)=exp(-t)1_[1/2,infinity). Although f_r->f in L2 and every fixed prime
summand converges, the complete prime sum has the exact defect

    lim_r P(f_r)=P(f)-2pi/e,
    lim_X lim_r P_>X(f_r)=-2pi/e.

The order of limits is essential. Every finite f_r has zero integral;
the limit has integral exp(-1/2), and the endpoint reappears. An explicit
finite error is

    |P_>X(f_r)+2pi/e|
      <=64(log X+3)/sqrt X+(50+16sqrt X log X)||f_r-f||.

The projection error squared is e^-2(e/2-theta_r), with theta_r an
explicit rational Gram solve. It is not an uncomputed zeta error. The
fixed finite-packet version has the exact rank-one matrix defect -2pi b b^t.
No arbitrary simultaneous-cutoff limit or unbounded packet-size uniformity
is asserted. This supplies genuine signed arithmetic cancellation on a
bounded-norm nonescaping sequence, but not the remaining full matrix sign.

## Why this is not an RH proof

The earlier growing-rank tail estimates require width at most linear in m,
or smaller. That is entirely within the subquadratic regime. In that regime
compression of ANY trace-class operator tends to zero, even if it is
indefinite. The new theorem identifies the nonescaping regime, but does not
supply arithmetic positivity there.

The actual attempted completion is recorded in PROOF.md Section 8. The
missing assertion is a source-side bound Q>=-eta_r G, eta_r->0, on the
square-width schedule, or equivalently vanishing limiting negative trace.
The endpoint term in the limiting explicit formula must be restored:
zero integral on finite tests is NOT preserved by strong L2 convergence.
An exact positive-heat five-atom countercontrol has all-gap three-sparse
positivity but keeps one negative direction. It tests both proposed shortcuts.

## Replay and source status

Run `python verify.py --check result.json` and the same under `python -O`.
Run `python test_rejections.py` for saved-result and source corruptions.
Then run `sha256sum -c SHA256SUMS`.

See VALIDATION.md for actual run counts. The checker uses exact Fraction
and Gaussian-rational arithmetic only. It does not evaluate any actual xi
matrix, enumerate primes/zeros, certify special functions, or machine-prove
the analytic convergence theorem. Independent proof/code review is pending.
No external novelty claim; classical Laguerre/spectral theory is credited.
