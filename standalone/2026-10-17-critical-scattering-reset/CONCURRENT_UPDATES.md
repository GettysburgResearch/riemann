# Concurrent work: #960, #961, and a common geometric weight

Source cutoff: the repository scan following the first publication of #962
on 17 October 2026. Two other research PRs appeared during this pass. They are
included here as separate proposed sources; neither is promoted to accepted
mathematics or used silently as a premise of the original component proofs.

* [#960](https://github.com/GettysburgResearch/riemann/pull/960), created
  19:39 UTC, head `c127f4f22d08585b699ccd59faa4eedd9bb001ae`.
* [#961](https://github.com/GettysburgResearch/riemann/pull/961), created
  19:47 UTC, head `7bd275b44261fff93bb565a9342c44b7c66526f6`.

The new notes were read at those exact heads. Their main interfaces were
checked by separate agents; this remains an AI compatibility review, not a
fresh certification of every imported theorem or their finite test suites.

## 1. #960 adds short-range and endpoint-maximal cancellation

[THEOREMS.md](https://github.com/GettysburgResearch/riemann/blob/c127f4f22d08585b699ccd59faa4eedd9bb001ae/standalone/2026-10-17-growing-shift-maximal/THEOREMS.md)
and its SOURCES.md use the same four rational-integer coefficient families,
with fixed ordinary Dirichlet character and excluded primes. The deep input
is the established [Matomaki--Radziwill--Tao v3](https://arxiv.org/pdf/1503.05121v3),
Theorem 1.7 and equation (1.12), whose displayed interface was checked in the
primary PDF by the source analyst. It is not an application of a fixed-shift
ordinary-Chowla theorem at growing coefficients.

Writing

\[
r(H,X)=\frac{\log\log(3H)}{\log(2H)}
       +(\log(2X))^{-1/700},
\]

the proposed conclusion includes

\[
\sum_{h\le H}\max_{Y\le X}|C_h(Y)|
\ll_{S,\xi}\sqrt A\,HX\,r(H,X)^{1/4}
\]

against any second sequence with square mass at most `AX`. It gives
`o(HX)` for every growing `H<=X`, uniformly in the algebraic completion degree
and powerful profiles. The short-interval frequency supremum remains outside
the integral. The dense/sparse dilation split and heavy/light square-mass
partition are essential to the claimed uniformity and endpoint maximum.

This complements our Fourier appendix:

| Feature | #960 | This packet's Fourier result |
|---|---|---|
| `H=X^theta`, `0<theta<1`, or slower growing H | Nontrivial average, including endpoint maximum | Global Parseval bound need not beat the trivial average |
| H comparable to X, fixed endpoint | Fixed displayed logarithmic saving | Arbitrary logarithmic saving |
| Arbitrary L2 second sequence | Explicitly included | The strongest stated filter bound uses two completion families |
| Smooth signed filters | Can be bounded through absolute correlations | Direct width/modulation-uniform bound |
| Conditional additive Fourier power | Not its main interface | Exact forward and inverse transfer at every exponent greater than 1/2 |

Neither result covers general Dedekind ideal coefficients by pretending they
are a one-bounded rational multiplicative function. Neither proves the full
critical covariance. For a Gaussian shell with `H=D^theta`, #960 still has
the power-scale factor `D^theta`, multiplied by its logarithmic saving.

## 2. #961 corrects the endpoint diagnosis and localizes the next signed task

[THETA_ESCAPE.md](https://github.com/GettysburgResearch/riemann/blob/7bd275b44261fff93bb565a9342c44b7c66526f6/standalone/2026-10-17-review-imports-theta-escape/THETA_ESCAPE.md)
has three limiting growth exponents equal to `1/4`: theta, the good Poisson
class and the principal z remainder. Improving only the first, with the
others unchanged, would not move the final boundary.

Its restricted reflected estimate gains `tau/4` on the original physical
rows whose powerful part has norm at least `Z^tau`. Its proposed retuning
lowers the other two tied errors and isolates OPEN-L, a signed bound on the
remaining physical rows. Conditional on that still-open bound and its named
analytic inputs, it obtains

\[
\Re s>2747/3000=11/12-1/1000.
\]

This is not an unconditional new boundary. More specifically, the cutoff is
on the powerful part of the physical theta row `m`. It is not a cutoff on the
Poisson frequency or on the new `a_z` coefficient lift in our principal
projection. No commutation between these projections is proved. Our physical
factor `X^(1/2-z)` must also remain in any attempted comparison.

The useful revised priority is to retain the actual low-powerful signed
pairing while investigating a principal or spectral projection. OPEN-L may
provide a nearer quantitative milestone, but it does not supply OPEN-PR,
Hardy membership or a bound for the model-space defect.

## 3. An exact connection to the geometric reciprocal source

[GEOMETRIC_ROUTE.md](https://github.com/GettysburgResearch/riemann/blob/7bd275b44261fff93bb565a9342c44b7c66526f6/standalone/2026-10-17-review-imports-theta-escape/GEOMETRIC_ROUTE.md)
uses the BV/Hecke class-and-scaling period. Its first Möbius convolution removes
zeta completely. Its second restores a reciprocal detector and unfolds to

\[
G_2(t)=c_Fm\sum_{\mathfrak n}\mu_F(\mathfrak n)
J_m(Qt^mN\mathfrak n),\qquad
\int_0^\infty J_m(u)u^s\frac{du}{u}=\Gamma(s)^m.
\]

Here `Q,c_F>0` are fixed field constants and `[F:Q]=2m`. With `X=t^(-m)`, its
critical OPEN-G is a square-root estimate for the weight `W(v)=J_m(Qv)`.

**Corollary of the critical convolution theorem.** In the common field setting
where our `a_z` is defined, for each fixed real `z>1/3`, the all-epsilon bound

\[
\sum_{\mathfrak n}\mu_F(\mathfrak n)J_m(QN\mathfrak n/X)
\ll_\varepsilon X^{1/2+\varepsilon}
\]

holds if and only if the same bound holds with `a_z` in place of `mu_F`,
using the **same** `J_m` weight and fixed field data.

Proof. For every `B>0`, gamma-product Mellin inversion on `Re s=B`, whose
vertical integral converges absolutely, gives
`|J_m(u)|<=C_B u^(-B)`. The local bound on `a_z` and the critical h/k masses
in PRINCIPAL_TWO_VARIABLE_FACTOR.md therefore justify its full convolution
and shorter-scale envelope proof with this weight; `B=2` suffices. The
normalized envelope tends to zero at small scales, so finite-scale terms
cause no problem. Apply the forward and reverse convolution inequalities.

To compare unrestricted `mu_F` with exterior `mu_F^S`, use the finite Euler
kernels. Their critical absolute masses are, respectively,

\[
\prod_{\mathfrak p\in S}(1-(N\mathfrak p)^{-1/2})^{-1},
\qquad
\prod_{\mathfrak p\in S}(1+(N\mathfrak p)^{-1/2}).
\]

Both are finite. They transfer the same envelope in both directions, then
our h/k kernels transfer it to `a_z`. This proves the corollary. It is an
application of the already proved convolution theorem, checked by the audit
analyst and main author; no new numerical assertion is involved.

The corollary connects the geometric realization to the free-z coefficients.
It does not claim automatic comparability of the different Gaussian and
product-Gamma smoothing kernels, or a bound for either signed source. The
geometric positive-period estimate does not survive Möbius inversion as a
positive reciprocal estimate.

## 4. Additional primary papers checked

[Frei--Sofos--Widmer v2](https://arxiv.org/html/2610.18491v2) was checked at the
introduction and small-splitting-prime theorem. The authors explicitly state
their results conditionally on QRH because they have not verified the upstream
arguments. Their prime threshold retains both the log-discriminant and
log-log-discriminant factors. These applications do not provide the missing
critical prime-discrepancy estimate in our detector.

[Bhargava--Vemulapalli v1](https://arxiv.org/html/2610.20600v1), Proposition 9
and the following CM estimate, were checked in the primary HTML. The complete
class/scaling period contains zeta itself. Its CM discriminant-aspect estimate
is not a fixed-field physical-scale bound for our signed source. No full
reconstruction of either paper is claimed.

The source map is now current through these concurrent inputs. All previously
stated open gates remain open. The added comparison changes neither the
component proof files nor the archived finite computations.
