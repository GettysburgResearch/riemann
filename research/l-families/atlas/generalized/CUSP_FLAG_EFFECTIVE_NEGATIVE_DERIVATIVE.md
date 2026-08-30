# An effective negative derivative of the actual weight-24 cusp quotient

Status: PROPOSED SOURCE-BOUND ANALYTIC CERTIFICATE; independent exact-SHA
review required. This is a separate five-file packet; no parent is edited.

Scope: the fixed uncompleted weight-24 functions F and L below, derivatives
in w=s+23, and one explicit transcendental evaluation point. No numerical
derivative sampling, completed-Q claim, second-derivative claim, minimal-order
claim, uniform-in-weight conclusion, RH/GRH consequence, or novelty claim.

Exact sources: repaired positive-spectrum parent
282ce03941444d0e02daba5fde260ccb54a3f909; weight-24 source
b62dfc6348661992bca659c99de226a1b6b22e14 and review
8e9f05211954e0a7aae5e63c9367f1d520d3671d. Four load-bearing/context objects
are bound by Git blob and LF-SHA256 in the manifest. The coefficient fixture
is authenticated before its q rows and full frequency maps are used.

## 1. Explicit theorem and unchanged source

Retain q=exp(2*pi*i*z), E4=1+240 sum sigma_3(n)q^n,
E6=1-504 sum sigma_5(n)q^n, and

    Delta=(E4^3-E6^2)/1728=q product_(n>=1)(1-q^n)^24,
    g=Delta E4^3-696 Delta^2,   b=Delta^2,
    c_n=[q^n]g,                b_n=[q^n]b.                 (ED1)

These are the actual canonical q-echelon basis of S24, not fitted arrays.
In particular c1=1,c2=0,c3=195660,b1=0,b2=1,b3=-48. Define

    B(w)=sum_(n>=1) c_n^2 n^-w,
    C(w)=sum_(n>=3) c_n b_n n^-w,
    U(w)=sum_(n>=3) b_n^2 (n/2)^-w,
    F(w)=B(w)-2^w C(w)^2/(1+U(w)),
    L(w)=zeta(2w-46) F(w).                                (ED2)

This is exactly PS1 and RQ9 in w coordinates. The original completed
quotient remains Q(s)=A_24(s)L(s+23); it is not substituted for F or L.

Put

    rho_*=9/2, x_*=log(9/2), a_*=-88203653222400,
    m=8192, w_*=96+8192/log(9/2),
    R_f=(-1)^m f^(m)(w_*)/[x_*^m exp(-w_*x_*)].            (ED3)

The derivative is taken first, then evaluated at w_*; it is not a derivative
of a sampled sequence. The denominator in ED3 is strictly positive.

**Theorem.** Both actual derivatives are strictly negative, with certified
normalized upper bounds

    R_F <= -88203307492526 < 0,
    R_L <= -88203140778512 < 0.                            (ED4)

Since m is even, these are negative 8192nd derivatives themselves. The
proof below establishes absolute convergence, every omitted-frequency
bound, and the rational inequalities used in the certificate. The producer
does not evaluate a transcendental derivative or claim its exact value.

## 2. Explicit global coefficient majorants

Write |H| for coefficientwise absolute values. For n>=1, reversing divisors
and applying the integral bound to zeta gives

    sigma_3(n)<=n^3(1+integral_1^infinity x^-3 dx)=3n^3/2,
    sigma_5(n)<=n^5(1+integral_1^infinity x^-5 dx)=5n^5/4.

The coefficients of (1-q)^-4 and (1-q)^-6 are at least n^3/6 and n^5/120.
Since 2160<=2^12 and 75600<=2^17, including the constant terms,

    |E4| <= 2^12(1-q)^-4,   |E6| <= 2^17(1-q)^-6.

Coefficientwise convolution and ED1 give

    |Delta| <= (2^36+2^34)/1728 (1-q)^-12
             <= 2^26(1-q)^-12,
    |b| <= 2^52(1-q)^-24,
    |g| <= (2^62+696*2^52)(1-q)^-24
         <= 2^63(1-q)^-24.                               (ED5)

For n>=1,

    binom(n+23,23)/n^23
      =product_(j=1..23)(1+j/n)/23! <=24<=2^32.

Thus the deliberately coarse but explicit bounds, valid for EVERY n, are

    |b_n|<=2^84 n^23,   |c_n|<=2^95 n^23.                 (ED6)

The inequalities are not extrapolated from finite q samples.

## 3. Certified absolute mass at w0=96

Exact Eisenstein convolutions construct all coefficients through q^64.
The tests independently reconstruct Delta by its logarithmic derivative.
The first 24 q rows and both complete frequency prefixes agree with the
frozen weight-24 coefficient fixture.

For n>=65, monotonicity gives

    sum_(n>=65) n^-50 <= integral_64^infinity x^-50 dx
                       =64^-49/49.

Consequently ED6 bounds the omitted coefficient sums at w0=96 by

| Sum | Omitted n>=65 upper bound |
|---|---|
| B-1 | 2^190 * 64^-49/49 = 2^-104/49 |
| C_abs=sum abs(c_n b_n)n^-96 | 2^179 * 64^-49/49 = 2^-115/49 |
| U_abs=sum b_n^2(n/2)^-96 | 2^264 * 64^-49/49 = 2^-30/49 |

For every finite prefix summand and each displayed tail bound, the producer
rounds UP to a multiple of 2^-160 by integer ceiling. Exact rational
comparisons establish

    B(96)-1 < 2^-100,
    C_abs(96) < 2^-110,
    U_abs(96) < 2^-30 < 1.                               (ED7)

The U prefix starts at n=3: its leading denominator pivot b2=1 is already
the 2^-w factored out in ED2. It must not be included in U.

The geometric inverse is now numerically justified, not merely formal.
For Re(w)>=96 all absolute word sums are dominated by

    M_F <= B(96)+2^96 C_abs(96)^2/(1-U_abs(96))
         < 1+2^-100+2^-124/(1-2^-30) < 2.                 (ED8)

Here M_F is an upper bound for sum_rho |a_rho(F)|rho^-96 after grouping
equal frequencies: the sum of absolute ungrouped word masses also obeys it.
The common endpoint factor 2^w in ED2 is retained. Furthermore

    zeta(146)<=1+integral_1^infinity x^-146 dx=146/145<2,
    M_L < 4.                                             (ED9)

This controls ALL omitted inverse words and ALL omitted zeta factors.
Normal absolute convergence holds on Re(w)>=96. Every fixed derivative
is justified at each w>96 by domination with
(log rho)^h rho^-(w-96), which is bounded on rho>=1.

## 4. Complete prefix, not a selected set of words

An inverse-depth h correction has frequency and coefficient

    rho=(nm/2) product_(j=1..h)(ell_j/2),
    (-1)^(h+1)c_n b_n c_m b_m product_j b_(ell_j)^2,
    n,m,ell_j>=3.                                        (ED10)

For rho<=12, the lower bound (9/2)(3/2)^h forces h<=2; the next depth
starts at 243/16>12. Each endpoint is <=8, and each internal index is <=5.
These bounds follow by setting the other indices to their minimum three.
They apply even when some actual coefficients vanish. The integer B prefix
needs n<=12. Zeta multiplication needs d<=floor(sqrt(12))=3.

The producer enumerates every ordered word in those finite boxes, filters
only by the exact rational frequency, and then groups equal frequencies.
There are 27 retained correction words. Both resulting functions have
17 nonzero atoms through 12, with the same support:

    1,3,4,9/2,5,6,27/4,7,15/2,8,9,10,81/8,21/2,11,45/4,12.

The entire maps, not only the first negative atom, equal the frozen parent
maps. The unique word at 9/2 is n=m=3,h=0, giving a_* in ED3. Multiplication
by zeta leaves it unchanged. The coefficient at four changes from
145929492496384 in F to 216298236674048 in L; it is not discarded.
The fixture records every grouped coefficient and the word-coverage counts.

## 5. Rational logarithm and kernel certificates

For rational v in [1,12], put u=(v-1)/(v+1). Integrating the geometric
series for 2/(1-u^2) gives, with J=64,

    L_J=2 sum_(j=0..J-1) u^(2j+1)/(2j+1),
    L_J <= log v <= L_J+
             2u^(2J+1)/[(2J+1)(1-u^2)].                 (ED11)

All quantities on the right are rational. Round L_J DOWN and its upper
bound UP to multiples of 2^-40. In particular the resulting upper bound
for log 2 is strictly below 7/10. No ordinary floating-point value of a
logarithm or exponential is used.

Let psi(t)=t exp(1-t). Direct integration gives, for t>0,

    log psi(t)=log t+1-t
       <= -(t-1)^2/[2 max(1,t)].                         (ED12)

For t<=1 integrate (1-u)/u over [t,1] and use 1/u>=1.
For t>=1 integrate (u-1)/u over [1,t] and use 1/u>=1/t.

For rho in the prefix other than 1 and rho_*, use ED11 to enclose
t=log(rho)/x_* in [a,b]. The certified intervals avoid one. Set

    delta=1-b if b<1, or a-1 if a>1,
    d_rho=delta^2/[2 max(1,b)],
    K_rho=floor(8192*d_rho/(7/10)).

Then ED12 and log2<7/10 imply

    psi(log(rho)/x_*)^8192 <= 2^-K_rho.                   (ED13)

The pivotal exponents are K_4=35, K_5=26, and K_12=1506.
All other prefix exponents are recorded. Since psi is decreasing above
one and log(12)/x_*>1, EVERY rho>12 obeys the same bound 2^-1506.
Thus no unenumerated frequency has been assigned an uncertified gap.

## 6. The signed derivative and complete remainder payment

Termwise differentiation of the normally convergent series, followed by
evaluation at w_* in ED3, yields the exact identity

    R_f=sum_rho a_rho(f)(rho_*/rho)^96
                     psi(log(rho)/x_*)^8192.              (ED14)

The rho=1 term vanishes because m>=1; the rho_* term equals a_*.
For every other rho<=12 use ED13. The entire omitted part satisfies

    abs(tail contribution) <= rho_*^96 M_f 2^-1506,       (ED15)

using M_F<2,M_L<4 from ED8--ED9. This is an absolute tail estimate, not
a sign assumption about omitted coefficients.

The producer takes an integer ceiling separately for each of the 15
remaining prefix contributions and ED15. Their sums are exactly

    E_F=345729874,   E_L=512443888,                        (ED16)

both strictly less than |a_*|/2. Therefore R_f<=a_*+E_f, which is ED4.
The certificate is intentionally conservative; no optimal derivative order
or exact normalized derivative value is claimed.

## 7. Source, replay, and acceptance boundaries

This closes the numerical absolute-mass/explicit-order issue left open
by PS9--PS12 for the actual weight-24 source, at the fixed uncompleted
normalizations ED2. It does not replace the parent's all-weight analytic
proof, estimate an actual period, establish negative curvature, change
the canonical flag, alter a completion, or say anything about RH/GRH.

The classical Eisenstein expansions and discriminant relation are in
[Zagier, Elliptic Modular Forms and Their Applications, section2.2
Proposition5 and section2.4 equation(23)](https://people.mpim-bonn.mpg.de/zagier/files-restricted/doi/10.1007/978-3-540-74119-0/fulltext.pdf).
These were directly consulted using the PDF source-reading workflow.
Remote bytes are not authenticated; the frozen local normalization
contracts are. The Laplace atom-extraction mechanism is the parent's
classical elementary argument, not a newly claimed abstract principle.

The arithmetic class is MIXED: CERTIFIED_INTEGER_COVERAGE and EXACT_RATIONAL.
Analytic logarithms are NOT declared rational: rational lower/upper bounds
are proved by ED11, with outward integer/dyadic rounding. All comparisons
in ED7, ED13, ED16 are exact. Finite arithmetic verifies these inequalities;
the global tail, normal convergence, and termwise derivative arguments are
the written proof, not assertions inferred from finite sampling.

Public caps: q order64, cutoff12, inverse depth2, support64, derivative
order8192, logarithm terms64, 40-bit log and160-bit mass dyadic grids,
32-bit primitive rationals, 8192-bit checked internal rationals, source/JSON
bytes<=1048576, and at most1000000 charged work units. Budget charges cover
the declared expansions, not every interpreter instruction or arbitrary
hostile-object computation. These helpers are used on the reconstructed
native source; standalone coefficient-array controls do not authenticate
an unrelated infinite series.

The full typed JSON report is rebuilt from authenticated primitives.
Unknown/missing fields, resealed coefficient changes, bool/int confusion,
floats/nonfinite/duplicate JSON, excessive shapes/bytes and source/artifact
drift fail closed. Result-bearing checks do not use assert and survive -O.

    python -B research/l-families/atlas/generalized/cusp_flag_effective_negative_derivative.py --check
    python -B -O research/l-families/atlas/generalized/cusp_flag_effective_negative_derivative.py --check
    python -B -m unittest discover -s tests -p test_cusp_flag_effective_negative_derivative.py
    python -B -O -m unittest discover -s tests -p test_cusp_flag_effective_negative_derivative.py

Ruff lint/format and the full authoring-base-to-head whitespace check are
additional replay gates. Freeze the exact source SHA for independent review;
author replay alone is not acceptance.
