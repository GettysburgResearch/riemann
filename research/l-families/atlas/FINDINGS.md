# Cross-family findings

Status: exact finite statements are separated below from discovery evidence and
open nominations. Nothing in this note proves RH or GRH.

## 1. Exact invariant: unitary local top coefficient

At each included unramified prime, the reciprocal local factor is put in its
unitary variable. In the Phase-0 rows:

```text
GL(1):  1-chi(p)T,                  |top coefficient|=1;
GL(2):  1-(a_p/sqrt(p))T+T^2,       top coefficient=1.
```

Every checked row satisfies this control exactly. It is a normalization
invariant, not a new theorem about zeros. It is valuable operationally because
it catches an unshifted GL(2) factor before different degrees or weights are
pooled.

The superficially stronger statement `|a_p/p^(w/2)|=1` is false. For each of
the three elliptic-curve rows, already at `p=2`, `a_p=-2`, so the normalized
prime coefficient has square `a_p^2/p=2`, not `1`. Zeta and the quadratic
character modulo 5 do have exact second and fourth moment `1` on the declared
window. Thus a GL(1) unit-amplitude pattern is not a degree-free detector law.

For reference, the exact GL(2) finite means through `p<=43` are:

| LMFDB row | imported rank | `M2` | display decimal | `M4` | display decimal |
|---|---:|---:|---:|---:|---:|
| `11.a2` | 0 | `9536727364483/14030349555495` | `0.679721` | `13680377587284913295751529/15142362203798364929591925` | `0.903451` |
| `37.a1` | 1 | `2284882048044/2371850295815` | `0.963333` | `821205796921744526847416/432744140442900231270325` | `1.897671` |
| `389.a1` | 2 | `144147769429982797/91579329321690210` | `1.574021` | `2016668514750617670001638172310929/599055254215042018487340800703150` | `3.366415` |

The decimals are display-only conversions of the exact fractions. The apparent
rank ordering is not evidence of a rank law: conductor, curve, and sample size
all change, and there is only one selected object per rank.

## 2. Exact finite result: the classical reciprocal filter has no common sign

Let `mu_L^cl(n)` be the reciprocal coefficients in the classical Euler
variable and use inclusive endpoints in

\[
W_L^{\rm cl}(X)=(I-\sqrt2S_2)(I-S_2)^2
\sum_{n\le X}\mu_L^{\rm cl}(n),
\qquad S_2M(X)=M(\lfloor X/2\rfloor).
\]

The filter expansion and its double root at `S_2=1` and root at
`S_2=1/sqrt(2)` are checked exactly in `Q(sqrt(2))`. Every reciprocal
coefficient through 256 is generated from the declared local factors, including
the bad factors at 11 and 37. The exact rows are:

| object | `X=32` | `X=64` | `X=128` | `X=256` |
|---|---:|---:|---:|---:|
| zeta | `-4-2sqrt(2)` (-) | `6+4sqrt(2)` (+) | `-4-6sqrt(2)` (-) | `2+4sqrt(2)` (+) |
| quadratic `chi_5` | `-1+sqrt(2)` (+) | `1+sqrt(2)` (+) | `3-sqrt(2)` (+) | `-7-3sqrt(2)` (-) |
| `11.a2`, rank metadata 0 | `-2+2sqrt(2)` (+) | `-1+2sqrt(2)` (+) | `-31+sqrt(2)` (-) | `7+31sqrt(2)` (+) |
| `37.a1`, rank metadata 1 | `14-19sqrt(2)` (-) | `63-14sqrt(2)` (+) | `122-63sqrt(2)` (+) | `259-122sqrt(2)` (+) |
| `389.a1`, rank metadata 2 | `34-24sqrt(2)` (+) | `92-34sqrt(2)` (+) | `301-92sqrt(2)` (+) | `579-301sqrt(2)` (+) |

Thus even this source-faithful common algebra does not produce a common finite
sign across the five objects. This is useful falsification, not a limiting law:
there are only four endpoints and one selected curve at each imported rank.
Moreover the GL(2) rows deliberately use integral classical coefficients. For
motivic weight one their unitary counterparts satisfy
`mu_unitary(n)=mu_classical(n)/sqrt(n)`, whereas the weight-zero GL(1) map is
trivial. Raw magnitudes in the table are therefore not cross-degree moments.

No zeta-specific weighted-`L2` abscissa theorem is transferred. The next valid
family question is a unitary, source-locked moment such as Target C, with local
densities and bad primes explicit.

## 3. Exact refutation: purity does not force the toy signed coefficient probe

For every monic squarefree cubic `D` over `F_5[T]`, the exact computation gives

\[
L_D(u)=1+A_Du+5u^2,
\qquad A_D^2\le16<20.
\]

Consequently both reciprocal roots have modulus `sqrt(5)`. Direct Moebius sums
and the formal reciprocal recurrence also agree through degree three for every
member. Nevertheless, with

\[
B_D(n)=\sum_{\deg f=n}\mu(f)\chi_D(f),
\qquad H_D(n)=5^{-n/2}B_D(n),
\qquad C_D=H_D(1)H_D(2),
\]

the 100-member family has

```text
C_D < 0: 40 members
C_D = 0: 20 members
C_D > 0: 40 members
family mean numerator B_D(1)B_D(2): exactly 0
```

This refutes the naive universalization “Frobenius purity determines a
memberwise signed reciprocal-coefficient correlation.” It simultaneously
exhibits the family/member gap: perfect family cancellation coexists with both
memberwise signs.

This does **not** refute canonical `XD`, `HCNC`, or physical occupancy. `C_D` is
an explicitly labeled toy lag-one probe. A genuine port must derive its degree
kernel from the same reciprocal-L source and preserve the relevant carrier.

## 4. Exact covariance: central zeros are rank-one atoms with a convention sign

Write the centered completed function as

\[
\Lambda(z)=z^rG(z),\qquad
F_\Lambda(z)=\frac r z+F_G(z),\qquad u_i=x_i^{-1}.
\]

The two detector conventions must remain separate:

\[
\frac{F(x)-F(y)}{x-y}:\qquad M_{\rm raw}=B-r uu^{\mathsf T},
\]

\[
\frac{F(x)+F(y)}{x+y}:\qquad M_{\rm raw}=B+r uu^{\mathsf T}.
\]

Thus the legitimate central atom is negative semidefinite for the Loewner
difference and positive semidefinite for the Pick sum/Hankel kernel. Calling
both simply “the Pick matrix” erases a load-bearing sign.

If the root number is `epsilon`, parity authorizes only

\[
r_{\rm forced}=\frac{1-\varepsilon}{2},
\qquad e=r-r_{\rm forced}.
\]

The exact parity/full residual satisfies

\[
M^{\rm parity}-M^{\rm full}=\sigma e uu^{\mathsf T},
\qquad
\|M^{\rm parity}-M^{\rm full}\|_F^2
=e^2\left(\sum_i x_i^{-2}\right)^2,
\]

where the squared scalar is convention-independent. At nodes `(1,2)`, the
factor is `(5/4)^2=25/16`. The imported rank-stress rows therefore give:

| curve | root number | order `r` | forced | excess `e` | squared residual |
|---|---:|---:|---:|---:|---:|
| `11.a2` | `+1` | 0 | 0 | 0 | 0 |
| `37.a1` | `-1` | 1 | 1 | 0 | 0 |
| `389.a1` | `+1` | 2 | 0 | 2 | `25/4` |

The arithmetic metadata is discovery-only; the algebra conditional on those
integers is exact.

## 5. Exact hostile control: deflation is not positivity

The synthetic quartic background remains indefinite after the full central
atom is removed. In the declared three-node control, the deflated Loewner
background has determinant `-36`, and the deflated Pick-sum background has two
negative directions despite determinant `+36`. Therefore central deflation is
bookkeeping that removes legitimate rank contamination; it is not a positivity
theorem for the remaining L-function geometry.

## 6. What appears genuinely transferable

The experiments suggest a narrow hierarchy:

1. **Transferable exactly:** Euler reciprocal algebra, unitary local scaling,
   central-order factorization, rank-one atoms, and the parity/full norm identity.
2. **Family-dependent:** local coefficient moments, monodromy averages, rank
   distributions, and low-zero statistics.
3. **Not implied by purity alone in this pilot:** a common memberwise sign for
   the particular toy coefficient `H_D(1)H_D(2)`. A genuine source-derived
   kernel could still have deterministic positivity and must be checked on its
   own Frobenius-character image.

That hierarchy is more useful than another broad plot: it tells a later proof
attempt precisely which steps are algebra and which require arithmetic geometry,
twist moments, or an individualization theorem.
