# R-93300 — Magnitude-only dispersion and hidden RH inputs cannot close the cubic route

Claim ID: `R-93300`  
Status: **EXACT METHOD FIREWALL / SCOPE CORRECTION**  
Created: 2026-08-16  
Frozen predecessor: PR #498 at `6cc0da2fa5711017e260ebdcea4ba8c22e453288`  
RH status: **unproved**

## 1. Binding predecessor firewall

`R-93254` remains binding.  A large number of prime blocks in one half-plane,
a safe same-prime diagonal, or a rank-one positive cross certificate is an
inverse theorem.  None is an upper bound for the complete prime sum.

The present packet strengthens that warning for the explicit cubic kernel.

Let

\[
 K(x)=\frac{x(1-x)(2x-1)}3,
\]

and put

\[
 F(x)=K(x)-4K(4x)\mathbf1_{0\le x\le1/4},
 \qquad 0\le x\le1.
\]

Then `L-93302` proves

\[
 \int_0^1F(x)\,dx=0,
 \qquad
 \int_0^1F(x)\log x\,dx=0.
\]

These two cancellations remove the constant-density and first logarithmic
density modes.  They do not give cancellation for arbitrary coefficients.

Indeed, for every sufficiently large integer \(N\), take

\[
 b_n=\operatorname{sgn}F(n/N)
\]

at the nonzero mesh points.  Then

\[
 \sum_{n\le N}b_nF(n/N)
 =\sum_{n\le N}|F(n/N)|
 \asymp N.
\]

The coefficient magnitudes, support, block count and diagonal norm are all
compatible with complete coherence.  Therefore no argument using only

```text
support size;
coefficient absolute values;
one-block L2 norms;
a generic large-sieve inequality;
or common-half-plane cardinality
```

can yield the required \(O(\sqrt N\,\mathrm{polylog}\,N)\) bound.

A successful proof must use the actual arithmetic covariance between the
truncated Möbius coefficient and the prime coefficient in `L-93303`, or an
equally source-specific mechanism.

## 2. Exact RH-strength inputs

The hostile reconstruction in `L-93300` proves that each of the following
statements is conclusion-producing:

\[
 |\mathcal A_\circ(N)|
 \ll \sqrt N(\log N)^B;
\]

\[
 \mathscr V_\circ(N)\ll(\log N)^B;
\]

\[
 |\mathfrak C_{\ne p}^{\mathrm{maj},0}(N)|
 \ll(\log N)^B;
\]

and the balanced cubic dispersion estimate `BCD` of `T-93305`.

Consequently none may be imported as an unconditional estimate, even under
different terminology such as

```text
square-root prime-block cancellation;
critical-line carrier decorrelation;
uniform major-arc covariance;
or a generic Type-II dispersion bound.
```

The estimates may be proved; they may not be assumed.

## 3. Standard large-sieve scope

The additive expansion of `L-93302` is exact:

\[
 \sum_{n\le N}a_nF(n/N)
 =
 \sum_{h\ne0}\widehat F_{\mathbb T}(h)
 \sum_{n\le N}a_ne(hn/N).
\]

The generic additive large sieve controls suitable averages of the inner
Fourier sums.  At one fixed endpoint and for one fixed arithmetic sequence it
does not provide the square-root cancellation required here.  In particular,
the low frequencies remain capable of complete coherence.

Likewise, the Mellin representation of `T-93305` has a double zero at the
zero carrier \(t=0\), but its weight is nonzero on bounded nonzero carriers.
A short-carrier mean-value theorem alone does not control one exceptional
arithmetic carrier.

## 4. First-Hermite scope

`L-93304` gives an exact heat-wavelet decomposition of the cubic scale-four
kernel.  It is a genuine bridge to the First-Hermite carrier family.  It does
not import the still-open one-carrier exclusion from the First-Hermite route.
Any descendant which replaces that exclusion by the block-count conclusion of
`L-93241` violates both `R-93254` and this firewall.

## 5. Boundary

```text
centered cubic identities                         retained
double Mellin moment                              exact
small-prime and unbalanced ranges                 closed unconditionally
balanced arithmetic covariance                    open / RH-bearing
generic magnitude-only closure                    refuted
First-Hermite block-count closure                 refuted
Riemann Hypothesis                                unproved
```
