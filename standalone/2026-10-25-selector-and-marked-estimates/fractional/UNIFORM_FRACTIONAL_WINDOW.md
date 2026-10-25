# A proved fractional window and the prime stratum it cannot bypass

Status: proved source-dependent moment estimate for a polynomially shrinking
coefficient window; the fixed-parameter fractional mean remains open.
Scope: the exact sixth-power-free physical Eisenstein family of PR #1021,
with its fixed finite character data, original collision zeros, common
punctures, common profiles, and norm twists. No zero-free boundary moves.
Date: 25 October 2026.

Exact sources: PR #1021 mathematical commit
`742e952be4ef7843de86ea12678c0bdd3d3579c3`, especially
`arithmetic/DIRECT_NATIVE_APPLICATION.md` and
`arithmetic/COEFFICIENT_CONTINUATION.md`;
Xu--Sang, [arXiv:2610.17675v2](https://arxiv.org/html/2610.17675v2),
equation (2.3), Theorem 2.2, Corollary 2.3, and Theorem 1.2.
The arbitrary-coefficient input (2.3) is stated for **sixth-power-free**
rows and columns, so no powerful-row summation loss is needed here.

Smallest remaining gap: control outside the power-thin window in Theorem 1,
or a new complete prime/same-prime-count estimate. The bounds below do not
prove the positive-measure hypothesis of PR #1021.

## 1. Keep the actual coefficient and the actual norm

Use the same Hilbert vector as the native application:

\[
 V_z(u)=D^{-1/2}\sum_{\mathfrak n}
       \mu^2(\mathfrak n)z^{\omega(\mathfrak n)}
       \psi_u(\mathfrak n)(N\mathfrak n)^{it}
       W(N\mathfrak n/D),\qquad
 \mathcal M_z=\sum_u w(u)|V_z(u)|^2.
 \tag{1}
\]

Rows have norm comparable to `U` and are sixth-power-free. The bounded
nonnegative row weight is fixed. The multiplicative character presentation
retains every natural zero, and its extra column puncture is common to the
row sum. All sums below use the same presentation. The norm of a column
multiplier of modulus at most one cannot increase an arbitrary-coefficient
sieve bound.

Put

\[
 S_6(U,D)=U+D+U^{5/6}D^{1/3}+U^{1/3}D^{5/6}.
 \tag{2}
\]

The source's full sixth-power-free sieve gives, for every common coefficient
vector `a_n` on the squarefree columns of this annulus,

\[
 \sum_u w(u)\left|\sum_n a_n\psi_u(n)\right|^2
       \ll_\varepsilon(UD)^\varepsilon S_6(U,D)\sum_n|a_n|^2.
 \tag{3}
\]

Fixed ray multipliers and the common puncture belong to `a_n`. There is no
row-dependent choice of the column vector in (3).

The ordinary endpoint adapter of PR #1021, under its pinned ordinary
moment input, gives

\[
 \mathcal M_1(U,D)
  \ll (UD)^\varepsilon U(1+|t|)^A p_J(W)^2
 \tag{4}
\]

in every prescribed bounded-power length range. Its principal-row and
growing-conductor qualifications remain in force. We do not re-certify
the imported analytic framework by citing (4).

## 2. An elementary coefficient-energy estimate

For one fixed number field and `D>=3`,

\[
 \sum_{Nn\le cD}\omega(n)^2
       \ll_{F,c}D(1+\log\log D)^2.
 \tag{5}
\]

To see this, expand `omega(n)^2` as the sum of the single-prime indicators
and twice the distinct-prime-pair indicators. Ordinary ideal counting
`#\{Nn<=X\}<<_F X` bounds the number divisible by `p` or `pq` by
`O(D/Np)` or `O(D/(Np Nq))`. At most `[F:Q]` prime ideals lie above a
rational prime, and prime ideals of residue degree at least two have a
convergent reciprocal norm sum. The elementary rational-prime harmonic
upper bound therefore gives `sum_(Np<=cD)1/Np<<1+loglogD`.
This proves (5), including the bounded range by adjusting the constant.

For `0<=z<=1`, put `eta=1-z`. The exact factorization of `1-z^k` gives

\[
 0\le1-z^k=(1-z)(1+z+\cdots+z^{k-1})\le k\eta.
 \tag{6}
\]

Consequently the normalized squared coefficient energy of `V_z-V_1`
is at most

\[
 D^{-1}\sum_n\mu^2(n)|z^{\omega(n)}-1|^2
                         |W(Nn/D)|^2
 \ll \eta^2(1+\log\log D)^2p_0(W)^2.
 \tag{7}
\]

This bound is uniform in `z` on the whole interval `[0,1]`. Omitting
columns or retaining extra natural zeros only decreases its right-side
coefficient calculation.

## 3. The actual uniform fractional-window theorem

**Theorem 1.** Under the source inputs (3)--(4), for `0<=z<=1`,

\[
 \boxed{
 \mathcal M_z(U,D)^{1/2}
 \le \mathcal M_1(U,D)^{1/2}
 +C_\varepsilon(UD)^\varepsilon(1-z)(1+\log\log D)
                    S_6(U,D)^{1/2}p_0(W).}
 \tag{8}
\]

Here the harmless small loss has been renamed after taking a square root.

**Proof.** Apply (3) to the exact coefficient difference in (7). Then
apply the Hilbert-space triangle inequality to `V_z=V_1+(V_z-V_1)`.
No differentiation of a one-point analytic bound is involved. QED.

In particular, if `Q(U,D)>=U`, and

\[
 0\le1-z\le\left(Q(U,D)/S_6(U,D)\right)^{1/2},
 \tag{9}
\]

then, after absorbing logarithms into the requested arbitrarily small
loss and taking a seminorm controlling `p_0`,

\[
 \mathcal M_z(U,D)
 \ll (UD)^\varepsilon (1+|t|)^{A'}p_{J'}(W)^2 Q(U,D).
 \tag{10}
\]

Thus this pass does establish a uniform bound for genuinely noninteger
parameters. Its interval, however, depends on the physical lengths and
shrinks by a fixed power. That distinction is decisive.

### The complete native target and its exact window widths

Set `D=U^r`, `1<=r<=3/2`, and

\[
 T(r)=\max\{1,\tfrac16+\tfrac45r\},\qquad
 s(r)=\tfrac13+\tfrac56r.
\]

Throughout this range, `S_6(U,U^r)` is within fixed factors of `U^{s(r)}`,
and the desired native envelope is within fixed factors of `U^{T(r)}`.
Theorem 1 therefore proves that envelope uniformly whenever

\[
 1-U^{-\kappa(r)}\le z\le1,
 \qquad
 \kappa(r)=\frac{s(r)-T(r)}2
 =\begin{cases}
 \frac{5r}{12}-\frac13,&1\le r\le25/24,\\[2mm]
 \frac1{12}+\frac r{60},&25/24\le r\le3/2.
 \end{cases}
 \tag{11}
\]

| Rectangle | Window exponent `kappa(r)` |
|---|---:|
| `D=U` | `1/12` |
| `D=U^(25/24)` | `29/288` |
| `D=U^(3/2)` | `13/120` |

The uniform width `U^(-13/120)` works throughout the displayed range,
with the same source qualifications. For a small robust enlargement of
the range, use (9) directly with the full four-term `S_6`; no corner
exponent outside its proved range is silently reused.

For a complex disk `|z-1|<=eta`, the coefficient difference is bounded by
`eta k(1+eta)^(k-1)`. Since the squarefree degree is
`r_D=O(logD/loglogD)`, the same result holds with an additional
`exp(eta r_D)` factor in (8). On the power-thin windows (11) this factor
is bounded and tends to one. Thus the result is not restricted to
approaching the endpoint from a single real direction.

### Why this does not continue to the Mobius point

PR #1021's shrinking-window extrapolation cost is at most

\[
 (8/\eta)^{2r_D}.
 \tag{12}
\]

For the proved width `eta=U^{-kappa(r)}`, its logarithm is of order
`(logD)(logU)/loglogD`, rather than `o(logD)`. The bound (12) is therefore
not a subpower loss. It cannot close the native consumer.

The desired width `1/loglogD` is much larger. Inequality (8) at that
width recovers the arbitrary-coefficient exponent, not the row-volume
endpoint. The new theorem makes the size of the unresolved stability
gain explicit; it does not supply that gain.

## 4. The exact ordinary-to-fractional convolution

There is another natural attempt to enlarge the interval. For
`z=1-eta`, `0<eta<1`, the ratio of the squarefree Euler series is

\[
 \frac{F_{1-\eta}(s)}{F_1(s)}
 =\prod_p\frac{1+(1-\eta)\psi(p)(Np)^{-s}}
                {1+\psi(p)(Np)^{-s}}.
 \tag{13}
\]

The common character can be left outside the coefficient convolution.
The resulting multiplicative coefficients satisfy exactly

\[
 b_\eta(1)=1,\qquad b_\eta(p^j)=\eta(-1)^j\quad(j\ge1),
 \qquad |b_\eta(n)|=\eta^{\omega(n)}.
 \tag{14}
\]

Thus the deformation is a signed convolution of the ordinary squarefree
source. It is not a harmless small absolutely summable Euler correction.
Minkowski with the uniform ordinary endpoint would pay

\[
 \sum_{Nn\le cD}\frac{|b_\eta(n)|}{\sqrt{Nn}}.
 \tag{15}
\]

The prime terms alone make (15) at least
`c_F eta sqrt(D)/logD` on a fixed interior prime-norm annulus, by the
fixed-field prime ideal theorem. In particular the proposed
`eta=1/loglogD` window does not make this absolute-convolution method
subpower. At `eta=1`, (13) is the inverse of the ordinary squarefree
Euler series: its exact convolution cancels every nonunit coefficient.
Dropping those signs loses precisely the structure one hopes to exploit.

This calculation is a failure of the separate absolute bound, not a
lower bound on the actual character mean.

## 5. The phase average already contains a hard prime estimate

Write `V_z=sum_(k=0)^(r_D) z^k v_k`, with `v_k` the actual row vector
on columns having exactly `k` distinct prime factors. Parseval and
Cauchy give

\[
 \mathcal E_\omega(U,D):=\sum_k\|v_k\|^2
 =\frac1{2\pi}\int_0^{2\pi}\mathcal M_{e^{i\theta}}(U,D)d\theta,
 \qquad
 \mathcal M_{-1}\le(r_D+1)\mathcal E_\omega.
 \tag{16}
\]

This provides one positive target rather than many parameterwise targets.
At the arbitrarily-small-exponent-loss level it is another form of the
earlier compact coefficient-continuation problem, not an analytic gain.

In particular, `v_1` is exactly the normalized prime-ideal polynomial.
Hence any proposed bound for `E_omega` must first bound its positive
prime contribution. Specialize to the canonical symbol `nu=1`,
`sign=+1`, no extra moving puncture, the source's fixed excluded set `S`,
a fixed profile, and `t=0`, `D=U=Q`. Xu--Sang's Theorem 1.2 gives,
for the restriction `v_1^sf` to its stated squarefree row subfamily,

\[
 \|v_1^{\rm sf}\|^2\ll Q^{\kappa_6-1+\varepsilon},
 \qquad
 \kappa_6-1=\frac{31-10\sqrt6}{6}
              =1.084183762\ldots.
 \tag{17}
\]

The native target at this point is `Q^(1+epsilon)`. Thus the currently
supplied prime theorem does not already establish even this one stratum.
The source's theorem statement is for squarefree rows; it must not be
silently relabeled a theorem for the full sixth-power-free moment.
Conversely, a full native phase-average theorem would imply the same
strong prime bound on that squarefree subfamily by positivity.

The current zero-density/absolute-value calculation has, at the native
corner `r=25/24` and zero class `sigma=3/4`, exponent

\[
 R(3/4)+(2(3/4)-1)(25/24)
 =\frac7{12}+\frac{25}{48}
 =\frac{53}{48},
\]

versus target exponent one. The deficit is `5/48`. This is the same
specific arithmetic loss already identified in PR #1021, now visible
inside the first positive stratum of the phase-average formulation.

## 6. Decision from this pass

The actual new estimate is (8)--(11), including the full physical-row
and common-mask scope. It proves continuity of the desired moment on
an explicit power-thin window and shows the exact extent of that method.

The next required arithmetic gain is not interpolation or continuity:
it is cancellation in the signed convolution (13), or a stronger
prime/same-omega mean that beats (17) and its native-corner analogue.
Norm-twist approximations and narrow-prime-band decompositions are
examined separately in `NORM_TWIST_AND_BAND_TRANSFER.md`.
