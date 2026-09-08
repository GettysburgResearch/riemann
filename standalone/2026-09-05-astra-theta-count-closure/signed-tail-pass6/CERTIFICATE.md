# Exact arithmetic contract for the ten-dimensional source certificate

This is a FINITE source computation, not an all-rank theorem. It uses no zero
values, zero verification, float special functions, or imported numerical jets.
The code is independent of the interval implementations in PRs #792/#793.

## Arithmetic and elementary functions

Every interval is [lo/2^640,hi/2^640], lo and hi integers. Addition and
negation are exact; multiplication and division round both endpoints
outwards using integer floor/ceiling. Division through zero refuses. Square
roots use integer square roots of endpoint times 2^640. Exact fractions
are converted outwards. No `assert` is an acceptance gate.

For positive x, range-reduce x=2^k y with 1<=y<=2, and use

    log y=2 sum_(j>=0) t^(2j+1)/(2j+1), t=(y-1)/(y+1).

After n terms the positive tail is at most
2*3^(-2n-1)*9/[8(2n+1)]. n=floor(640/3)+12. log2 is computed by the
same formula, not inserted as a decimal. For exp(x), reduce |x| by repeated
halving to <=1/8, sum its Taylor series through the same n, and use the
positive tail bound (8/7)*8^(-n-1)/(n+1)!. Repeated squaring and reciprocal
for negative x preserve enclosure. General interval log/exp use monotonicity.
Pi is 16 atan(1/5)-4 atan(1/239), each arctangent enclosed by its alternating
series and next-term bound. Bernoulli numbers through B_96 are reconstructed
by their exact rational recurrence.

## Fixed safe germs

For p=1,2,4,8,16, put s0=(1+sqrt(1+4p))/2. Its rigorous real enclosure is
used everywhere. On the complex circle |z|=1/4, Re(s0+z)>1 and
|s0+z+j|<=6+j. Compute degree-four Taylor jets in z for

    log(s0+z)+log(s0-1+z) -(s0+z)log(pi)/2
                    +logGamma((s0+z)/2)+log zeta(s0+z).

Constant terms may be omitted only when they cannot affect a derivative.
The zero-free Euler half-plane justifies the local logarithm of zeta.

### Zeta remainder

The Euler--Maclaurin formula with N=256 and M=48 is

    sum_(n<N)n^(-s)+N^(1-s)/(s-1)+N^(-s)/2
      +sum_(k=1)^M B_(2k)/(2k)! (s)_(2k-1)N^(-s-2k+1)+R(s).

The periodic-Bernoulli integral gives on the stated disk

    |R(s)| <= E_zeta
      = |B_96| (6)_96/[96! *96*256^96] < 10^-120.

The integral denominator is Re(s)+95>96, and the N exponent is less
than -96. Cauchy's coefficient bound therefore widens coefficient j by
4^j E_zeta, for j=0,...,4. These are explicit bounds on the remainder
analytic function, not derivatives of an uncontrolled pointwise error.

To avoid artificial interval blow-up, the code generates (s)_j/j!
before applying its scalar correction B_(j+1)/[(j+1)N^j]. It does not
round a very tiny factor and then multiply a huge unnormalized rising
factorial. Subsequent series logarithm uses the enclosed nonzero constant.

### Gamma remainder

Shift w=(s0+z)/2 by 128 and use

    logGamma(w+128)
       =(w+128-1/2)log(w+128)-(w+128)+log(2pi)/2
        +sum_(k=1)^47 B_(2k)/[2k(2k-1)(w+128)^(2k-1)]+R_G.

Subtract the 128 exact logarithms log(w+j), j=0,...,127. On the s-disk,
Re(w+128)>128 and |Im(w+128)|<=1/8. DLMF 5.11(ii)'s complex remainder
bound is at most the first omitted term times sec(arg(w+128)/2)^96.
This secant factor is <2: |arg|<=1/1024, cos(arg/2)>=1-2^-23 and
(1-2^-23)^96>=1-96*2^-23>1/2. Thus

    |R_G| <= E_Gamma
       =2|B_96|/[96*95*128^95] < 10^-120.

Widen coefficient j by 4^j E_Gamma. The constant log(2pi)/2 may be
omitted because all retained outputs are nonconstant derivatives.
A prepublication audit widened the initially tighter Gamma error by this
factor two, and all final certificate/replay files were regenerated.

## Return to the invariant variable and form matrix

Write u=p+v and s=s0+delta(v). The exact relation is

    v=(2s0-1)delta+delta^2.

Its degree-four inverse is computed recursively, with delta(0)=0. Compose
the log-xi jet with delta and differentiate once; this gives h_0,...,h_3
in the convention h(p+v)=sum h_j v^j. The entry formulas (21)--(22) in
PROOF.md give the actual raw form Q on all ten prescribed basis functions.

Interval LDL is performed without pivot reordering. At step i,

    d_i=Q_ii-sum_(j<i)L_ij^2 d_j;
    L_ki=(Q_ki-sum_(j<i)L_kj L_ij d_j)/d_i.

The algorithm refuses unless the lower endpoint of EVERY d_i is positive.
Induction in interval arithmetic encloses the exact LDL factorization of
the same source matrix. Sylvester congruence then proves its positivity.
The certificate's 60-place decimal intervals are rational OUTWARD
conversions of the internal dyadic enclosures, not display-only floats.
The final raw pivot is about 4.58e-48. No lower eigenvalue or numerical
conditioning guarantee in the original Hilbert norm is inferred from it.

## Reproduction and evidence boundaries

    python interval_source.py --check certificate.json
    python -O interval_source.py --check certificate.json
    python interval_source.py --full > full_source_payload.json

The full payload contains all jets, all 100 entries, and internal pivot
endpoints. Its hash is reconstructed from canonical JSON and stored in the
compact certificate. A hash or stored positive flag is never accepted
without recomputing the source. `verify.py` also checks finite arithmetic
and algebra controls and intended refusal paths.

Classical source references, checked for the specified identities:
- https://dlmf.nist.gov/25.2 (Euler--Maclaurin zeta expansion)
- https://dlmf.nist.gov/25.11 (integral remainder)
- https://dlmf.nist.gov/5.11 (Stirling expansion and complex remainder)
- https://dlmf.nist.gov/5.4 (digamma special values)
- https://dlmf.nist.gov/5.5 (Gamma recurrence)

An independent 160-digit mpmath differentiation reproduced all twenty jet
enclosures. It is NON_DIRECTED_HIGH_PRECISION and is not a proof dependency.
No independent referee, alternate interval implementation, Lean kernel,
repository-wide test run, or new zero verification is claimed.
