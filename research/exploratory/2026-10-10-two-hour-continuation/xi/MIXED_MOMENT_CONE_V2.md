# A count-free real head gives an anisotropic cone of mixed moment signs

Status: proposed source-qualified complete analytic corollary, with exact
rational controls. No new native higher jet is computed for this theorem.
Scope: complete mixed shifted moments, preserving all unknown conjugate
blocks and multiplicities. Actual Xi inherits a finite rectangle of strict
signs from the previous count-free census through 5419. The rectangle is
finite; no all-order Hausdorff assertion or RH conclusion follows.
Exact sources: [SHIFTED_COMPLETE_MOMENTS_V2.md](SHIFTED_COMPLETE_MOMENTS_V2.md),
the complete even product and strip, and the frozen previous-wave
`xi/outer-ray/SIXTEENTH_MOMENT_CENSUS_RECOVERY.md` with receipt SHA256
`964f49cc79a61b354cd77fe1f077637e54bb46f39a5643e1455e87f60fabc4d6`.
What was actually run: exact Fraction guards and prior direct source hashes.
The checker does not compute the billions of individual coefficients or
rerun the primitive signs; complete rectangle coverage is the proof below.
Smallest remaining gap: extend real-head control cofinally, or prove the
complete mixed sign family from the exact actual theta source.

## MC1. Complete mixed moment normalization

Let t>A>=0 and put L=1/(t^2-A^2). For every positive-half-plane source root
define lambda_rho=(rho^2+t^2)^(-1). The complete moments are

\[
 a_n=\sum m_\rho\lambda_\rho^{n+1},\qquad
 b_n=a_n/L^n,\qquad
 B_{n,j}=\sum_{\ell=0}^j(-1)^\ell{j\choose\ell}b_{n+\ell}
       =\sum m_\rho\lambda_\rho(\lambda_\rho/L)^n
                      (1-\lambda_\rho/L)^j.
\tag{MC1}
\]

Here n,j are nonnegative integers. All series converge absolutely for each
fixed n,j, and full conjugate grouping makes B_n,j real. These are complete
source moments, not moments of only the finite real head.

Assume every source zero with abs(Re rho)<=R is real, R>0. Multiplicities
there may be arbitrary; simplicity is unnecessary. Every such real term
in (MC1) is strictly positive, because 0<lambda/L<1.

## MC2. The exact unknown-block phase

For an unknown root rho=x+iy, x>R and 0<=y<=A, write

\[
 D=\rho^2+t^2,\qquad Q=\rho^2+A^2,\qquad
 c=t^2-A^2>0,\qquad D=Q+c.
\]

Re Q>=x^2>0 and Re D>x^2. If theta_D=arg D and theta_Q=arg Q,
then 0<=theta_D<=theta_Q<pi/2, and

\[
 \theta_D\le\frac{2A}{x},\qquad
 \tan(\theta_Q-\theta_D)
   =\frac{2xyc}{(\operatorname{Re}Q)(\operatorname{Re}D)+(2xy)^2}
   \le\frac{2Ac}{x^3}.
\tag{MC2}
\]

The denominator is at least x^4. Since atan v<=v for v>=0, the same last
bound holds for theta_Q-theta_D. The identity
`1-lambda/L=Q/D` gives the mixed term's phase

\[
 -(n+1)\theta_D+j(\theta_Q-\theta_D).
\tag{MC3}
\]

Both quantities being subtracted are nonnegative. Therefore its absolute
value is at most their maximum, not their sum. In particular it is strictly
less than pi/2 whenever

\[
 (n+1)\frac{2A}{R}<\frac\pi2,\qquad
 j\frac{2A(t^2-A^2)}{R^3}<\frac\pi2.
\tag{MC4}
\]

Negative-y roots are conjugates and have the opposite phase. Every unknown
source occurrence consequently has strictly positive real contribution.
The full sum in (MC1) is strictly positive if the source has any zero.
There is no omitted exponential term, dropped complex block or finite-tail
replacement. The two different bounds explain the anisotropic geometry:
the power index n costs order R, while the difference index j costs order
R^3/t^2 at a fixed shift.

## MC3. An actual-Xi finite rectangle from the count-free head

Use the independently established count-free real head R=5419, A=1/2,
and t=512. Its 4968 positive zeros ensure a nonempty real head. For every

\[
 0\le n\le8000,\qquad 0\le j\le900000,
\tag{MC5}
\]

the exact extreme bounds are

\[
 \frac{8001}{5419}<\frac32<\frac\pi2,\qquad
 \frac{235929375000}{159131975059}<\frac32<\frac\pi2.
\tag{MC6}
\]

The rational checker verifies these inequalities and the exact inherited
receipt/direct-source identities. Monotonicity in n,j covers the entire
rectangle, so B_n,j>0 for every index in (MC5). No individual coefficient
enumeration or new native endpoint run is claimed by this exact checker.
The separate 528 native mixed tests through n+j<=31 are compatible controls,
not the source of the larger analytic rectangle.

The full Hausdorff characterization requires every n,j without an upper
bound. This finite rectangle does not provide that hypothesis. Its real-head
premise is the previously proved finite count-free census, not an assumed
unbounded critical-line census or a historical zero count. Thus the argument
does not close the missing cofinal step.
