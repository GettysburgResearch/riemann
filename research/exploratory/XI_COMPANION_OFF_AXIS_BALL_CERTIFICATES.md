# Actual Xi off-axis companion zero and alignment certificates

Status: PROPOSED SOURCE-BOUND BALL CERTIFICATES; independent exact-SHA review required.
Scope: nine explicit local disks, at three exact frozen Riemann--Siegel scales.
No RH assumption is used for the local statements. No zero census or physical
band-capture theorem is claimed.
Authoring base: ac7fa9af27c3fbcb3314f3ed58c8eed35b318052.
Five new files; all frozen source proofs and the preceding source audit are unchanged.

## 1. Exact objects and finite result

Keep the unrescaled normalization in GC1 and NA1:
\[
 f(z)=\Xi(z)=\xi_{\rm R}(1/2+iz),\qquad
 \xi_{\rm R}(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
 \tag{OA1}
\]
This is the actual entire Xi function, not a polynomial surrogate.
For each of the three anchors a=32,64,128, set
\[
 \omega(a)=\tfrac12\Re\psi(1/4+ia/2)-\tfrac12\log\pi,\qquad
 \lambda_a=1/\omega(a)>0.
 \tag{OA2}
\]
Differentiate the exact phase displayed in frozen L-106610 to obtain OA2;
the two digamma terms are conjugates on the real axis. These are the exact
constant freezing scales of L-106620.1, not 2/log(a/(2pi)) and not lambda(z).
Certified positivity is checked directly at all three anchors. We do NOT
identify these selected anchors with a pre-existing prescribed physical
partition, and do not assert that a historical sufficiently-high threshold
equals 32. The native constant-scale algebra itself is exact here.

Write, for k=0,5,
\[
 R_k=f^{(k)}-i\lambda_a f^{(k+1)},\quad
 C_k=f^{(k)}+i\lambda_a f^{(k+1)},\quad
 \Theta_k=R_k/C_k,\quad
 W=f f^{(6)}-f'f^{(5)}.
 \tag{OA3}
\]
For each anchor there are three declared disks D(c,2^-120).
The exact centers c=(n_x+i n_y)/2^180 are the literal integer pairs in the
producer's DISKS and in the source-sealed fixture. The following decimals
are only a readable index, not the inputs to certification.

| anchor | approximate Re c | approximate Im c | strict raw modulus corridor at the zero |
|---|---:|---:|---|
| 32 | 27.4289614778 | 0.6774809311 | 672/1000 < abs(Theta0) < 673/1000 |
| 32 | 31.7434932793 | 0.6454503127 | 439/1000 < abs(Theta0) < 440/1000 |
| 32 | 35.8419702457 | 0.5640976006 | 722/1000 < abs(Theta0) < 723/1000 |
| 64 | 61.1348212673 | 0.5154279252 | 250/1000 < abs(Theta0) < 251/1000 |
| 64 | 63.8396914505 | 0.5317259135 | 692/1000 < abs(Theta0) < 693/1000 |
| 64 | 69.3518795950 | 0.4836367415 | 451/1000 < abs(Theta0) < 452/1000 |
| 128 | 124.9655159851 | 0.4631965367 | 265/1000 < abs(Theta0) < 266/1000 |
| 128 | 129.1375992667 | 0.4772246167 | 493/1000 < abs(Theta0) < 494/1000 |
| 128 | 133.3226736722 | 0.4573589801 | 438/1000 < abs(Theta0) < 439/1000 |

**Finite certified result.** Subject to the explicitly pinned ball-library
enclosure contract in Section 4, each disk contains exactly one R5 zero,
counted with complex multiplicity. It is therefore simple. Each disk lies
strictly in C+ and in (a-6,a+6)+i(0,1). The three disks for any one anchor
are disjoint. On the full closed rectangle enclosing each disk, C5, R0,
C0, f6 and W are nonzero, and the listed strict modulus corridor holds.
Thus each zero is a genuine simple zero of Theta5, not a canceled raw zero,
and is not a zero or pole of Theta0. In particular every listed raw modulus
is strictly greater than 1/4.

The fixture also encloses f^(j), j=0,...,8, at the exact center and uniformly
on its rectangle, and encloses Theta0, Theta0', Theta0'' and W there.
The latter derivative enclosures are ordinary analytic derivatives at
fixed lambda_a, not derivatives with lambda varying with z.

Equivalently, every listed b is an unconditional genuine simple pole of
the literal native meromorphic quotient U5=R0*C5/(C0*R5). The fixture encloses
its nonzero residue R0(b)*C5(b)/(C0(b)*R5'(b)); R5' also excludes zero on
the whole rectangle. This is not a contradiction to conditional innerness:
a ratio of two inner functions can have poles in the upper half-plane.

The center search was exploratory Newton iteration, using ball midpoints.
It is NOT a proof step. Acceptance does not call Newton, mpmath, a floating
finite difference, a decimal root tolerance, or a presumed zero list.
Only the frozen exact rational centers are used.

## 2. Complete local proof and cancellation safety

Let F=R5, c a declared center and r=2^-120. For z in the disk,
analytic Taylor expansion with integral remainder gives
\[
 |F(z)-F(c)-F'(c)(z-c)|\le \tfrac12 M_2 |z-c|^2,
 \quad M_2\ge\sup_{|w-c|\le r}|F''(w)|.
 \tag{OA4}
\]
For example, integrate F'' along the line segment from c to z twice;
the disk is convex, so the same supremum bounds the remainder.
The producer encloses F(c), F'(c), and
F''=f^(7)-i lambda_a f^(8) on the containing rectangle
[x-r,x+r]+i[y-r,y+r]. Let A be an upper bound on abs(F(c)),
D a positive lower bound on abs(F'(c)), and M the upper bound on
abs(F'') from that rectangle. It checks with exact rational arithmetic
\[
 A+\tfrac12Mr^2 < Dr.
 \tag{OA5}
\]
In fact it checks the stronger slack (left)*2^50 < right in every disk.
On the circle, F differs from F'(c)(z-c) by strictly less than the
modulus of that linear function. Rouche's theorem gives exactly one
zero counted with multiplicity inside and no boundary zero. This proves
existence and simplicity without any real-zero or RH premise.

All functions used here are analytic on a neighborhood of the rectangles.
For s=1/2+iz in these rectangles, abs(Im s)>20, so s is neither 0 nor 1,
Gamma(s/2) has no pole, and zeta(s) has no pole. There is no reliance on
removable product cancellation to make a singular ball evaluation finite.
The same is true of the functional-equation route s -> 1-s.

The positivity of each computed modulus lower bound for C5 prevents
internal cancellation of R5. Independently f6 excludes zero and, at the
R5 zero b, C5(b)=2i lambda_a f6(b) != 0. R0 and C0 separately exclude zero
on the whole rectangle. Hence Theta0 is analytic and nonzero there.
The direct W check is redundant but useful:
\[
 R_0C_5-C_0R_5=2i\lambda_a W.
 \tag{OA6}
\]
At b this also certifies W(b)!=0, consistent with GC's cancellation-safe
common-zero criterion. No global assertion about the zero set of W or
the exceptional parameter set E follows from nine nonzero local samples.

For real lambda, conjugation gives C5(bar z)=overline(R5(z)).
Thus the conjugate disks in C- contain the corresponding simple C5 zeros.
Because f is even and real entire, R5(-bar z)=-overline(R5(z));
there are also reflected simple R5 zeros in C+ at -bar b.
These are consequences of symmetry, not independently enumerated data.
In particular a C+ zero in the table must not be called a C5 zero.

## 3. What the alignment data imply, conditionally

Assume, separately for a chosen lambda_a, GH's existing two-component
inner premise: Theta0 and Theta5 are inner in C+. Write
Theta0=G U and Theta5=G B after removing their maximal common inner factor.
GH excludes singular factors, but the following local argument only needs
the inner factorization and the displayed nonzero guards.

At each listed b, Theta0(b)!=0. Consequently G(b)!=0 and the simple
Theta5 zero survives as a simple zero of B. Moreover
\[
 |U(b)|=|\Theta_0(b)|/|G(b)|\ge|\Theta_0(b)|.
 \tag{OA7}
\]
There is no need to prove lambda_a outside GC's global exceptional set:
other common zeros, if any, do not erase this node. Conversely, a local
surviving node does not prove that G is constant.

For the boundary-dx Hardy norm and normalized kernel
e_b(z)=sqrt(Im b/pi)/(z-bar b), reproducing kernels give
P_(UH2)=M_U M_U^* and
\[
 \|P_{UH^2}e_b\|=|U(b)|,\qquad e_b\in K_B.
 \tag{OA8}
\]
Therefore the GLOBAL operator norm of P_(UH2) P_(KB) is strictly greater
than 722/1000, 692/1000, and 493/1000, respectively, for the three anchors.
These are finite, conditional, one-vector lower bounds; the other listed
nodes and jets can be used by a future finite Gram computation.

Do not reverse OA7. The raw upper corridor does not give an upper bound
on the reduced numerator U without controlling G. None of this estimates
a Fourier-band compression, a retained high-T outer metric, a physical
trace, or a Hilbert--Schmidt norm. CP already proves that even coprime pure
infinite-height pairs can have finite corrected physical capture.
We neither bypass that obstruction nor turn this finite collection into
a cofinal source theorem. There is no RH conclusion, parameter stability
theorem, exhaustive off-axis census, or novelty claim about Rouche's
theorem, interval arithmetic, or the classical Xi function.

## 4. Arithmetic and primitive replay contract

The certificate uses python-flint 0.9.0, FLINT 3.6.0, CPython 3.12.10,
Windows AMD64, at 256-bit precision, with series cap exactly 9.
The manifest pins all 44 installed native .pyd/.dll files by an aggregate
SHA256 of their canonical path-to-SHA256 map. No binary is checked into
this five-file packet. A different runtime identity is rejected rather
than silently treated as the same replay. This is a reproducibility pin,
not a security attestation of the interpreter, operating system, hardware,
or every Python dependency.

All constants entering the certificate are integers or exact rational
fmpq values; pi, logarithm and digamma are enclosed ball operations.
The [official python-flint general concepts](https://python-flint.readthedocs.io/en/latest/general.html)
specify rigorous interval outputs and conservative comparison predicates.
We rely on that implementation contract; this packet does not formally
verify FLINT or independently reimplement its special-function bounds.
The runtime's own 227 tests and 3092 doctests passed before this work;
that fact is a diagnostic, not a substitute for the enclosure contract.

Evaluate OA1 on the formal series s=1/2+i(z+X). The coefficient of X^j
is f^(j)(z)/j!, so multiplication by j! yields the requested derivative.
For a rectangular constant coefficient z, the interval-series operations
enclose that derivative for every center z in the rectangle. No omitted
higher series coefficient is used to estimate the remainder: F'' is
separately enclosed uniformly on the entire rectangle.
The [series API](https://python-flint.readthedocs.io/en/latest/acb_series.html)
and [FLINT 3.6.0 series documentation](https://github.com/flintlib/flint/blob/v3.6.0/doc/source/acb_poly.rst)
describe the operations used.

Every point and rectangular jet is also evaluated using xi_R(1-s).
The reflected variable includes the minus sign in its series coefficient,
so derivatives remain derivatives with respect to z. All corresponding
complex balls must overlap. These two algebraically equivalent routes
exercise different arguments but share FLINT; they are not independent
implementations of transcendental arithmetic.

Ball lower and upper endpoints are extracted as outward-rounded exact
dyadic rationals. No decimal rendering participates in acceptance.
The final Rouche inequalities are recomputed in Python Fraction
arithmetic, independently of interval comparison. The proof uses the
rectangle enclosure, not a sample grid or a small residual alone.
The lambda ball is also an enclosure of the exact fixed number; dependency
overestimation only weakens the tested inequalities.

The producer authenticates six complete frozen notes by both Git object
identity and LF-normalized SHA256. It executes no ancestor producer.
The manifest, proof, producer and test have local artifact seals; the
fixture has a canonical payload seal. Acceptance reconstructs every
primitive ball evaluation and every derived field from fixed code inputs;
resealing an edited fixture does not make it acceptable.

Input limits are explicit: 3,000,000 bytes, 100,000 JSON nodes, depth 24,
4096-bit rational components, and exactly nine declared disks. Public
arithmetic precision is confined to 192--512 bits and the Xi evaluation
domain to 20<Re z<150 and 0<Im z<1. These caps are implementation boundaries,
not unbounded mathematical claims. Booleans are not accepted as integers,
floats/NaN/Infinity and duplicate JSON keys are rejected, and ordinary
guards remain enabled under Python -O.

The smallest result-invalidating burden is the uniform ball enclosure of
the eighth derivative or a sign/orientation error in OA3--OA5.
The smallest next scientific burden is not finding another tiny residual:
it is a certified region census, or a source-correct finite/band operator
calculation using these surviving nodes and the reduced numerator metric.
