# Audited parabolic Vaughan continuation and two-field AND-gate

Date: 2026-08-21  
Branch base: PR #691 head `be9a4168fa0df971a2fc63176f07ce3beee6c3d4`  
Scientific status: **RH unproved**

## Binding audit corrections

The hostile reconstruction of the first PR #696 continuation found and
corrected five defects.

1. The gcd coordinates require `mu^2(gab)=1`; the earlier display admitted
   spurious nonsquarefree gcd terms.
2. A same-occurrence Cauchy certificate requires
   `collar_-^2 <= A B`, not `A+B`.
3. The right-survival telescoping sign was reversed. For a fixed least owner,
   greatest-owner mass beyond every fixed power is asymptotically full, not
   suppressed.
4. The auxiliary `512` amplitude bound used a false endpoint estimate. The
   safe uncentered bound has leading constant `192` times the endpoint factors.
   After exact carrier subtraction, however, the endpoint kernel is uniformly
   bounded by `256`, with no `sqrt(X)` factor.
5. At the adaptive cutoff `Z=sqrt(T)`, two unsquared labels already exceed the
   threshold. The earlier depth-three boundary was off by one.

These dispositions are frozen in `R-102001`.

## Exact results retained and sharpened

### Positive cubic compactifier

`L-102000` remains exact: the critical cubic has a nonnegative compact
exponential B-spline compactification with a Mellin multiplier that preserves
every open-strip reciprocal-zeta pole. Its half-order moment is positive, so
it is not interchangeable with the signed zero-moment Vaughan kernel.

### Large-divisor Hankel and exact parabolic geometry

`L-102001` proves

\[
\mathcal B_U(X)
=\sum_{d,e>U}\frac{\mu(d)\mu(e)}{\sqrt{de}}
\mathcal L_K(X/de).
\]

For `U=floor(X^(1/3))`, every active ordered pair satisfies exactly

\[
\max(d,e)<\min(d,e)^2.
\]

The corrected gcd coordinates are

\[
\mathcal B_U(X)
=\sum_{\substack{g,a,b\ge1\\\mu^2(gab)=1\\ga,gb>U}}
\frac{\mu(a)\mu(b)}{g\sqrt{ab}}
\mathcal L_K(X/(g^2ab)).
\]

### Two wings collapse to one Möbius owner

`L-102008` defines the positive ordered balanced-divisor multiplicity

\[
N_V(m)=\sum_{a\mid m}\mathbf1_{a>V}\mathbf1_{m/a>V}
\]

and proves

\[
\mathcal B_U(X)
=\sum_{\substack{g,m\ge1\\\mu^2(gm)=1}}
\frac{\mu(m)}{g\sqrt m}N_{U/g}(m)
\mathcal L_K(X/(g^2m)).
\]

If `m=pc` with `p=P^+(m)`, then

\[
\mu(m)N_V(m)
=-2\mu(c)
\sum_{a\mid c}\mathbf1_{a>V}\mathbf1_{c/a>V/p}.
\]

Thus the balanced terminal contains one sign-free square core, one unique
largest prime, one remaining cofactor Möbius sign, and one positive oriented
divisor multiplicity.

### Exact ratio-four two-field factorization

`L-102009` constructs a positive ratio-four two-box spline `A` and the two
kernels

\[
A_-=(D-1/2)A,
\qquad
A_+=(D+3/2)A,
\]

with

\[
K_1=A_-*_M A_+.
\]

At the source level, if

\[
b_U(n)=\mu(n)\mathbf1_{n>U},
\]

then

\[
a_U=b_U*\mathbf1,
\qquad
a_U*a_U*\mu=b_U*a_U.
\]

The balanced Vaughan packet therefore factors exactly as

\[
\mathcal B_U(X)
=\int_U^{X/U}F_{U,-}(Y)F_{U,+}(X/Y)\frac{dY}{Y}.
\]

This gives the genuine same-occurrence product certificate

\[
(\mathcal B_U(X))_-^2
\le\mathcal E_{U,-}(X)\mathcal E_{U,+}(X).
\]

`T-102001` proves that subpower logarithmic block bounds for both field
energies jointly imply `BVD100310` and hence RH. Both estimates remain open.

## Exact replay

```bash
python3 experiments/X-102000-audited-factorizations/verify.py \
  --output experiments/X-102000-audited-factorizations/results/verification.json
```

Retained verdict:

```text
PASS_X_102000_AUDITED_FACTORIZATIONS
```

The replay performs 90,918 exact finite checks:

```text
source factorizations             2,592
largest-prime recurrences         7,104
joint-survival identities            15
depth-threshold checks           80,190
centered-kernel checks            1,017
```

It records all conclusion-facing estimates and RH as unproved.

## Current implication matrix

```text
large Möbius tail b_U
  --A_- ratio-four observation-->  LMTE102001

positive divisor completion a_U=b_U*1
  --A_+ ratio-four observation-->  DCTE102001

LMTE102001 AND DCTE102001
  -> balanced Vaughan negative mass
  -> zero-moment compact detector
  -> RH.
```

This is a literal two-statement conjunction rather than a pair of aliases: the
source factors and kernel factors are distinct, and their multiplicative
convolution is exactly the original obstruction.

```text
LMTE102001                         OPEN / RH-BEARING
DCTE102001                         OPEN / RH-BEARING
SOW102008                          OPEN / RH-EQUIVALENT
Riemann Hypothesis                 UNPROVED
```
