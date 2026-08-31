# Independent review of the frozen pair-geometry proofs

Freeze: 8522f5a8854c29c755314bf4d86b2bc42464da71.

| Reviewed proof | Verified Git blob |
| --- | --- |
| NATIVE_THRESHOLD_LAW_AND_CONVEXIFICATION.md | a4f189a6f12cd189be7b711a4d0ac5f36bbc613d |
| NATIVE_PAIR_MOMENT_LOWER_ENVELOPE.md | a8b3d8448aef58f7c0c1b2105302e03e973d91d1 |

The reviewer read both complete drafts, then both complete frozen texts,
verified these blob identities, and checked that neither working proof
differs from the freeze. The final threshold-law text includes the
explicit Reynolds predecessor pin5e312c7dc81926e637d2d7343f90eba4708587c0.
No scientific process, numerical panel, test suite or optimizer was run
by this reviewer. These are proof-only results.

No mathematical blocker was found.

For the threshold-law theorem, a monotone profile determines its unique
CDF law including the initial/final endpoint atoms. The completed graph
gives a continuous monotone path in the stated path category. The
Tonelli calculations yield A=1-E T, B=(1-E T^2)/2 and
C=A-E|T-S|/2 with independent copies from the same law; they do not
allow those probabilistic quantities to be independently prescribed.

The variance-bound equality classification is exact. Equality in
|T-S| >= (T-S)^2 forces every pair of distinct support points to have
distance one, leaving precisely a point law or support contained in
{0,1}. The nearest Reynolds moment calculation correctly forces all
the displayed scalar inequalities to equality at
epsilon=(sqrt(10)-3)/2. A constant profile cannot have the required
deviations; the remaining threshold location is unique. This is the
maximum-moment norm result, not a nearest physical Hilbert path.

The averaging defect is the integral of pointwise profile variance.
For a genuine two-prime source, bilinear curvature has exactly the
three coefficient directions1,u,v. Direct differentiation independently
confirms the literal readouts
B_(p,q)=A/2, B_(p,pq)=-B/4, B_(q,pq)=(C-1)/8.
They prove that the full all-record correction is Delta times the
nonzero C direction, with its original factor2 and endpoint constant.
The proof retains all physical weights/aliases after observation,
limits the complete-source statement to two primes, and does not
claim an energy decrease or legal equivariant source projection.

For the lower-envelope theorem, the feasible(A,B) range and its
constant/threshold interpolation are correct. The no-clip affine
solution has slope12(B-A/2). The lower ramp has
L=3(A-B)/A and C=4A^2/(3L); its two boundaries are exactly L=1
and L=2A. Reflection gives the stated upper-only formula and
transition curves. In the both-clipped case,
L^2=12(2A-A^2-2B) gives C=A-L/6. All shared boundaries, A=0,1,
B=A/2 and the terminal threshold B=A-A^2/2 are consistently handled.

The global minimality argument is stronger than comparison within
a guessed parametric family. Pointwise projection onto[0,1],
combined with the two exact moment constraints, proves
C(g)-C(f_*) >= integral(g-f_*)^2 for every boxed measurable competitor.
The nonnegative slope then makes the unique boxed minimizer admissible
as a monotone profile. At the terminal B boundary, the signed
rearrangement integral forces the unique threshold. The proof properly
separates this occupation-moment objective and u-time stability from
the original physical energy and higher-arity compatibility.

The classical CDF, variance, interval-projection and rearrangement
methods are credited as elementary/prior inputs. The new explicit
source and fixed-moment consequences are not promoted to an all-prime,
retained-gamma, RH or full physical-optimization result.

Independence disclosure: the reviewer did not author either reviewed
pair theorem. The reviewer authored the cited earlier support-reduction
principle and the separate S3/general-curvature quotient note. The
present review independently checks the new threshold-law formulas,
all-record two-prime correction, four-regime specialization and their
scope, rather than claiming those inherited inputs were authored by
someone else.

