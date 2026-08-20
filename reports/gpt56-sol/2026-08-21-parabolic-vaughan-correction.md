# Audited parabolic Vaughan and ratio-four half-divisor frontier

Date: 2026-08-21  
Branch base: PR #691 head `be9a4168fa0df971a2fc63176f07ce3beee6c3d4`  
Scientific status: **RH unproved**

## Binding audit corrections

The first continuation contained five defects, now frozen in `R-102001`:

1. the gcd reparameterization omitted the squarefree condition `mu^2(gab)=1`;
2. a same-occurrence certificate displayed `A+B` where the Cauchy gate requires `AB`;
3. the right-survival telescoping sign was reversed;
4. the auxiliary endpoint bound `Delta_p Psi<=128 sqrt(X)` was false;
5. the automatic unsquared threshold for `Z=sqrt(T)` occurs at depth two, not depth three.

For a fixed least owner, greatest-owner mass beyond every fixed power tends to
the full least-owner mass. Joint survival prevents the divergent marginal norm
of `R-100616`; it does not suppress wide owner intervals.

## Exact results retained

### Positive cubic compactifier

`L-102000` constructs a nonnegative compact exponential B-spline from the
critical cubic. Its support and Mellin noncancellation are exact. Its
half-order moment is strictly positive, so `R-102000` forbids importing the
zero-moment Type-I theorem from a different kernel.

### Large-divisor and single-wing coordinates

`L-102001` proves

\[
\mathcal B_U(X)=
\sum_{d,e>U}\frac{\mu(d)\mu(e)}{\sqrt{de}}
\mathcal L_K(X/de).
\]

For `U=floor(X^(1/3))`, every active ordered outer pair is exactly parabolic.
The audited gcd form keeps the coupled cutoff and `mu^2(gab)=1`.

`L-102008` collapses the two apparent Möbius wings to one sign:

\[
\mathcal B_U(X)
=\sum_{\mu^2(gm)=1}
\frac{\mu(m)}{g\sqrt m}N_{U/g}(m)
\mathcal L_K(X/(g^2m)),
\]

where `N_V(m)>=0` is the balanced-divisor multiplicity. Unique largest-prime
ownership leaves one cofactor sign times a positive oriented divisor count.

### Centered collar correction

After subtracting the exact `192 sqrt(X)` carrier, the endpoint kernel is
uniformly bounded:

\[
\|\Delta_{p_i}\Delta_{p_j}(\Psi-192\sqrt{\cdot})\|_\infty\le256.
\]

The centered collar is supported exactly on subset products

\[
m_S>X/(p_ip_j).
\]

Unsigned Rankin still fails, and after squaring at `Z=sqrt(X/(p_ip_j))` the
automatic unsquared tail starts at depth two. These facts localize but do not
sign the collar.

## Ratio-four factorization

`L-102009` constructs a positive two-box spline `A` supported on `[1,4]` with

\[
\widehat A(s)=
\frac{(1-2^{-s})(1-\sqrt2\,2^{-s})}{s(s-1/2)}.
\]

Put

\[
A_-=(D-1/2)A,
\qquad
A_+=(D+3/2)A.
\]

Then the signed ratio-16 Vaughan kernel factors exactly:

\[
K_1=A_-*_M A_+.
\]

With `b_U=mu 1_(n>U)` and `a_U=b_U*1`, the balanced source is

\[
a_U*a_U*\mu=b_U*a_U.
\]

Hence the balanced remainder is the same-occurrence Mellin convolution of a
large Möbius-tail field and a divisor-completed-tail field. This gives the
literal two-field Cauchy gate of `T-102001`.

## Positive half-divisor square root

`L-102010` introduces the nonnegative multiplicative function

\[
\eta(p^k)=\binom{2k}{k}/4^k,
\qquad \eta*\eta=\mathbf1.
\]

For

\[
h_U=(\mu\mathbf1_{>U})*\eta,
\]

one has

\[
a_U*a_U*\mu=h_U*h_U.
\]

Thus the two source fields become identical. The exact Hardy relation between
`A_+` and `A_-` has sharp `L2` norm three, giving

\[
|\mathcal B_U(X)|
\le3\int_U^{4X/U}|H_{U,-}(Y)|^2\frac{dY}{Y}.
\]

The conclusion-facing gate is now one explicit energy:

\[
\mathrm{HHFE102010}(L):
\quad
\int_{2^L}^{2^{L+1}}
\int_{U_X}^{4X/U_X}|H_{U_X,-}(Y)|^2
\frac{dY}{Y}\frac{dX}{X}=2^{o(L)}.
\]

`HHFE102010` implies the balanced Vaughan estimate and therefore RH. It is not
proved unconditionally.

## Replays

```text
PASS_X_102000_AUDITED_FACTORIZATIONS
PASS_X_102010_RATIOFOUR_HALF_DIVISOR_FACTORIZATION
```

The retained exact checks cover source convolution, gcd/single-wing collapse,
unique-largest-prime recurrence, corrected survival telescoping, depth
thresholds, the centered kernel bound, `eta*eta=1`, the symmetric half-completed
source, the ratio-four piecewise kernel identities, and the sharp Hardy norm.
They explicitly record `rh_established=false`.

## Exact boundary

```text
positive cubic B-spline compactifier             PROVED EXACT
B-spline Type-I inheritance                      REFUTED
large-divisor Hankel identity                    PROVED EXACT
parabolic outer-pair geometry                    PROVED EXACT
gcd core sign removal                            PROVED EXACT
two wings -> one Möbius owner                     PROVED EXACT
joint survival suppression of wide owners        REFUTED
centered endpoint kernel bound 256                PROVED EXACT
large-product threshold localization             PROVED EXACT
unsigned Rankin closure                          REFUTED
ratio-four kernel/source factorization            PROVED EXACT
positive half-divisor square root                 PROVED EXACT
two fields -> one Hardy-related field             PROVED EXACT
HHFE102010                                        OPEN / RH-BEARING
Riemann Hypothesis                                UNPROVED
```
