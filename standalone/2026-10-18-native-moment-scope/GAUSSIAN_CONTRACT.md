# Directed primitive Gaussian replay

Status: finite directed enclosures of a specified native source. No finite
value or moment is used as evidence for the infinite critical estimate.

## Exact source

The field is F=Q(w), w^2+w+1=0, with S the prime ideals above 2 and 3.
All nonzero integral ideals are indexed separately, including conjugate
ideals of equal rational norm. For EVERY ideal b outside S with Nb<=64,
the observable is the actual masked principal Gaussian

    A_(b^6)(D)=sum_n mu_F(n) 1_((n,b)=1) W_(4,1)(Nn/D),
    W_(4,1)(y)=y^(-4) exp[-(log y)^2/4]/sqrt(4 pi).

Thus tau=1 agrees with the Gaussian normalization of #976; c=4 is fixed
before evaluation. The generalized tau in PROOF.md is not required here.
All b, including their repeated-prime powers, are included. Signatures
only combine rows proven identical at this principal source; their exact
ideal multiplicities remain in every reported moment.

The finite production grid and precision are recorded in GAUSSIAN.json.
It is a finite list of real scales, not all real D and not a zero scan.

## Primitive coefficient generation

`ideals.py` enumerates lattice ideals by complete column HNF. Independently,
`norm_mobius_coefficients` uses rational Euler factors. The latter supplies
all norm coefficients up to the explicitly recorded N cutoff:

* split p=1 mod 3: the complete factor is (1-X)^2;
* inert p=2 mod 3: the complete factor is 1-X^2;
* ramified p=3: the complete factor is 1-X;
* S exclusions remove the factors at 2 and 3 entirely.

Masking one prime ideal above a split p changes (1-X)^2 to (1-X), while
masking both changes it to 1. An inert prime has ideal norm p^2, not p.
An exponent in b does not cause the same prime ideal to be removed twice.
These rules are checked against every individual HNF ideal in the finite
caps in CHECKS.json and EXTENDED_CHECKS.json. No floating arithmetic enters
the integer source production. Each full coefficient array has its own
portable little-endian signed-int32 SHA-256 in the numerical report.

The principal producer reuses one complete primitive array and applies the
exact Euler-deletion recurrence from PROOF.md §2. Removing a prime ideal
of norm q divides the norm series by (1-X^q): at multiples of q, in ascending
order, set `out[n] = in[n] + out[n/q]`. Two split conjugates require two
separate factors. This avoids rebuilding and factoring every integer for
every mask. The fast arrays are checked against the independent local-factor
algorithm for all 66 distinct mask signatures through Nb<=512, over every
norm <=8192. It is the proved source identity used as an algorithm.

## A complete upper-tail majorant

The Eisenstein ring is norm-Euclidean: rounding the two coordinates of a
quotient leaves errors at most 1/2, whose norm is at most 3/4<1. Thus every
ideal is principal and has exactly six unit generators. For x>=1,

    N(a+bw)=(a-b/2)^2+3b^2/4 <=x

allows at most (4 sqrt(x)/sqrt(3)+1)(2 sqrt(x)+1) lattice points. Dividing
by six, omitting zero, and bounding each constant by its multiple of
sqrt(x) gives

    I_F(x) <= (2/sqrt(3)+1/2)x < 2x.                     (G1)

This intentionally coarse bound counts all ideals, so it also bounds the
S-excluded and masked sources. Since |mu_F(n)|<=1, it bounds the absolute
omitted tail for every b in the report, without a sign or cancellation
assumption.

For general fixed c,tau let Y>=1 and R=Y/D. Suppose W_(c,tau) is decreasing
on [R,infinity), i.e. c+log(R)/(2tau)>=0. Stieltjes partial summation and
(G1) give

    sum_(Nn>Y) |mu_F(n) 1_((n,b)=1) W_(c,tau)(Nn/D)|
       <= 2 Y W_(c,tau)(Y/D)
          + D exp[tau(1-c)^2]
             erfc((log(Y/D)-2tau(1-c))/(2sqrt(tau))).    (G2)

The nonnegative boundary term is retained. Specifically, from
sum_(Nn>Y) W = -I_F(Y)W(Y/D) + integral_Y^infinity I_F(t)(-dW(t/D)),
discarding the negative boundary and using I_F(t)<=2t yields
2 Y W(Y/D)+2 integral_Y^infinity W(t/D)dt. Completing the square in log(t/D)
evaluates the integral and proves (G2). This covers infinitely many ideal
columns beyond Y. No lower tail is truncated: all norms 1<=n<=Y occur in
the integer coefficient arrays.

The producer evaluates the right side of (G2) by Arb ball arithmetic and
adds a symmetric radius at least its upper endpoint to each signed finite
sum. Positivity, finite values and the decreasing-profile premise are
strict acceptance gates. All normalizing constants, logarithms, exponentials,
pi, square roots and erfc values are directed operations. The library's
arithmetic contract, rather than ordinary high precision, is the numerical
assumption. No hand-specified approximate pi or float input is used.

## Acceptance and limits

`gaussian.py` reproduces GAUSSIAN.json. `replay_gaussian.py` reconstructs the
source and recomputes at higher precision with a longer cutoff, then requires
the deposited full-source enclosures to contain the new full-source
enclosures. It separately compares low-scale values to sums over individual
HNF ideals. `test_exact.py` executes corrupted exact models in subprocesses.
The source, coverage, tail proof and directed numerical contract are each
necessary; agreement between two decimal reports alone is insufficient.

This is a full primitive replay of the DECLARED principal-sector finite
experiment. It does not compute nonprincipal Hecke characters, every physical
CT row, or the full family moment in Theorem A. It does not prove an all-scale
bound, a critical exponent, field RH or ordinary RH. The analytic theorems
remain written deductions awaiting independent mathematical review.
