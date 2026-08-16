# T-93305 — Balanced Cubic Dispersion is the explicit remaining arithmetic closure candidate

Claim ID: `T-93305`  
Status: **SELF-CONTAINED CANDIDATE CLOSURE THEOREM / OPEN ARITHMETIC PRODUCER**  
Created: 2026-08-16  
Depends on: `L-93300`--`L-93304`, `R-93300`  
RH status: **unproved**

## 1. The producer

For integer \(N\ge64\), put

\[
 U=\lfloor N^{1/3}\rfloor,
 \qquad
 a_U(m)=\sum_{\substack{d\mid m\\d>U}}\mu(d),
\]

and let \(F\) be the explicit scale-four cubic wavelet of `L-93301`.

Define

\[
 \boxed{
 \operatorname{BCD}(N)
 =
 \sum_{\substack{
 N^{1/3}<m,\ell\le N^{2/3}\\
 N^{3/4}<m\ell\le N
 }}
 a_U(m)\Lambda(\ell)F(m\ell/N).
 }
 \tag{T-93305.1}
\]

The proposed **Balanced Cubic Dispersion theorem** is:

> There exist absolute constants \(B,C\) such that
> \[
> \boxed{
> |\operatorname{BCD}(N)|
> \le C\sqrt N(\log(2N))^B
> \qquad(N\ge64).
> }
> \tag{T-93305.2}
> \]

No form of (T-93305.2) is assumed in the preceding lemmas.

## 2. Why this is not a renaming of CPBD

`L-93303` proves unconditionally

\[
 \mathcal A_\circ(N)
 =
 \operatorname{BCD}(N)
 +O\!\left(\sqrt N(\log(2N))^3\right).
 \tag{T-93305.3}
\]

Thus the new producer contains none of the following objects:

```text
endpoint rows or endpoint means;
prime-block cardinality;
same-prime towers;
higher prime powers as an independent gate;
small prime bases;
Type-I convolutions;
products below N^(3/4);
the four-adic gauge;
or an unspecified PIG adapter.
```

Its coefficients, ranges and kernel are fixed in (T-93305.1).  A proof must use
the arithmetic covariance of the truncated Möbius divisor sum with the
von Mangoldt coefficient in one balanced near-hyperbola region.

## 3. Equivalent exact attack coordinates

### A. Additive bilinear dispersion

Let

\[
 \mathcal D_h(N)
 =
 \sum_{\substack{m>U,\ \ell>U\\m\ell\le N}}
 a_U(m)\Lambda(\ell)e(hm\ell/N).
\]

The full Type-II term is exactly

\[
 \sum_{h\ne0}\widehat F_{\mathbb T}(h)\mathcal D_h(N),
 \qquad
 |\widehat F_{\mathbb T}(h)|\ll h^{-2},
 \tag{T-93305.4}
\]

and the omitted low-product part is already
\(O(\sqrt N\log^3N)\).

A successful additive proof must exploit the actual \(a_U\)- and
\(\Lambda\)-correlations.  A generic large-sieve average is insufficient by
`R-93300`.

### B. Mellin band-pass dispersion

With the finite Dirichlet polynomials

\[
 A_U(s)=\sum_{U<m\le N/U}\frac{a_U(m)}{m^s},
 \qquad
 L_U(s)=\sum_{U<\ell\le N/U}\frac{\Lambda(\ell)}{\ell^s},
\]

the full Type-II term has the exact Mellin representation

\[
 \frac1{2\pi}
 \int_{\mathbb R}
 \widehat F(c+it)N^{c+it}A_U(c+it)L_U(c+it)\,dt.
 \tag{T-93305.5}
\]

At \(c=1\),

\[
 \widehat F(1+it)=O(t^2)\quad(t\to0),
 \qquad
 \widehat F(1+it)=O(t^{-2})\quad(|t|\to\infty).
\]

The zero carrier and remote carriers are therefore suppressed.  The bounded
nonzero carrier range remains load bearing.

### C. First-Hermite heat frame

`L-93304` rewrites the same wavelet as a continuous superposition of
First-Hermite heat derivatives.  A carrier-based proof may establish
(T-93305.2) by a source-specific estimate for that integral.  It may not
replace such an estimate by block count or half-plane alignment.

## 4. BCD implies RH

By (T-93305.3), BCD gives

\[
 |\mathcal A_\circ(N)|
 \ll\sqrt N(\log(2N))^{\max(B,3)}.
\]

`L-93300` supplies the exact integer-to-real interpolation and Mellin pole
audit.  Every zero with real part greater than \(1/2\) would survive as a pole,
contradicting the resulting holomorphy.  Functional-equation symmetry gives
RH.

## 5. RH implies BCD

Under RH, the von Koch estimate gives

\[
 \mathcal A_\circ(N)
 \ll\sqrt N\log^2(2N).
\]

Equation (T-93305.3) then gives BCD with a fixed logarithmic exponent.
Therefore

\[
 \boxed{
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 \operatorname{BCD}(N)
 \ll\sqrt N(\log N)^B
 \text{ for some fixed }B.
 }
 \tag{T-93305.6}
\]

This equivalence is a status statement, not a proof of BCD.

## 6. No hidden RH-strength estimate

The proof of the reduction uses only:

```text
finite source identities;
the two explicit cubic Mellin moments;
Euler--Maclaurin for a fixed piecewise polynomial;
the exact Vaughan identity;
|mu|<=1, |a_U|<=tau;
Lambda(n)<=log n;
and elementary divisor sums.
```

It does not use:

```text
a Mertens square-root bound;
a prime number theorem with fixed power saving;
a critical-line mean-value estimate strong enough to imply RH;
CPBD under another name;
or the First-Hermite one-carrier exclusion.
```

The exact open estimate is displayed as (T-93305.2).

## 7. Immediate falsifiers

Reject a proposed proof of BCD if it:

1. bounds the balanced form using only coefficient magnitudes;
2. moves a Mellin contour through \(-\zeta'/\zeta\) while assuming no
   off-line residues;
3. invokes a fixed-power prime number theorem error;
4. treats the double zero at \(s=1\) as cancellation against the prime
   discrepancy;
5. substitutes the block-count inverse theorem for a covariance estimate;
6. uses an average-carrier estimate as a pointwise-carrier theorem;
7. drops the truncated Möbius coefficient \(a_U(m)\);
8. omits the range \(N^{3/4}<m\ell\le N\).

## 8. Boundary

```text
PR #498 analytic spine                         independently reconstructed
large-prime shell                              exact
two Mellin moments and grid cancellation       exact
all Type-I and low-product ranges              square-root safe
First-Hermite heat-wavelet bridge              exact
balanced cubic dispersion                      open / RH-equivalent
accepted proof of RH                           no
Riemann Hypothesis                             unproved
```
