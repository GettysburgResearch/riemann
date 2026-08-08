# L-26802 — Exact annular physical-to-carry split isometry

Claim ID: `L-26802`  
Title: The compact opposite-parity physical window is exactly a weighted carry split on one oversupport row  
Status: **PROPOSED COMPLETE EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-source-specific`  
Created: 2026-08-08  
Dependencies: PR #268 `L-26201/L-26202`; PR #269 `L-26901/L-26903`; PR #241 `L-9518`  
Scope: exact source map and norm identity; no lower-scale recurrence or RH conclusion

## 1. The compact source window

Retain

\[
 \omega_2(n)
 =\mu(n)-\frac32\mathbf1_{2\mid n}\mu(n/2)
 +\frac12\mathbf1_{4\mid n}\mu(n/4),
\]

and put

\[
 L=\log2,
 \qquad
 h_\omega(t)
 =e^{-t/2}
 \left[
 \mathbf1_{[0,L)}(t)-\frac12\mathbf1_{[L,2L)}(t)
 \right].
 \tag{L-26802.1}
\]

The window is real, compactly supported, and belongs to \(L^1\cap L^2\).
For integers \(m,r\ge1\), define

\[
 g_m(r)
 =\mathbf1_{m\le r<2m}
 -\frac12\mathbf1_{2m\le r<4m}.
 \tag{L-26802.2}
\]

Because

\[
 \mathbf1*\omega_2
 =\varepsilon-\frac32\delta_2+\frac12\delta_4,
\]

one has the exact floor identity

\[
 \boxed{
 g_m(r)
 =\sum_{k\le r/m}\omega_2(k)
   \left\lfloor\frac r{mk}\right\rfloor .
 }
 \tag{L-26802.3}
\]

Thus \(g_m\) is not a model wavelet. It is the literal compact output of the
complete opposite-parity arithmetic source.

## 2. Physical step signal

Let \(x=(x_m)\) be any finitely supported real or complex sequence and put

\[
 \alpha_x
 =\sum_m\frac{x_m}{\sqrt m}\,\delta_{\log m},
 \qquad
 Q_x=h_\omega*\alpha_x.
 \tag{L-26802.4}
\]

Define the integer potential

\[
 F_x(r)=\sum_m x_m g_m(r).
 \tag{L-26802.5}
\]

For almost every

\[
 \log r\le t<\log(r+1),
\]

equation (L-26802.1) gives

\[
 h_\omega(t-\log m)
 =\sqrt m\,e^{-t/2}g_m(r).
\]

Therefore

\[
 \boxed{
 Q_x(t)=e^{-t/2}F_x(r)
 \qquad
 (\log r\le t<\log(r+1)).
 }
 \tag{L-26802.6}
\]

In particular,

\[
 \boxed{
 \|Q_x\|_{L^2(\mathbb R)}^2
 =\sum_{r\ge1}\frac{|F_x(r)|^2}{r(r+1)}.
 }
 \tag{L-26802.7}
\]

This is an exact physical norm, not a Riemann-sum approximation.

## 3. The carry split is the additive defect of the same potential

For a row \(n\), define

\[
 (\mathcal S_nF)(j)
 =F(n)-F(j)-F(n-j),
 \qquad 0\le j\le n.
 \tag{L-26802.8}
\]

PR #269 proves

\[
 Z_{n,m}(j)
 =g_m(n)-g_m(j)-g_m(n-j).
\]

Consequently,

\[
 \boxed{
 (\mathcal S_nF_x)(j)
 =\sum_m x_m Z_{n,m}(j).
 }
 \tag{L-26802.9}
\]

Thus the physical source and the carry feature are not merely analogous
positive Grams. They are the same finite source before and after one explicit
additive-split operator.

## 4. Exact generalized-prime specialization

Let

\[
 a_\omega(2^\nu u)=2\nu+2^{-\nu}
 \qquad(u\ {\rm odd})
\]

be the positive inverse coefficient and define

\[
 \Lambda_\omega=\omega_2*(a_\omega\log).
\]

For the complete choice

\[
 x_m=a_\omega(m)\log m,
 \tag{L-26802.10}
\]

equations (L-26802.3) and finite convolution give

\[
 \boxed{
 F_x(r)
 =\sum_{q\le r}\Lambda_\omega(q)
  \left\lfloor\frac rq\right\rfloor .
 }
 \tag{L-26802.11}
\]

Hence

\[
 \boxed{
 (\mathcal S_nF_x)(j)
 =\sum_{q\le n}\Lambda_\omega(q)\chi_{n,q}(j),
 }
 \tag{L-26802.12}
\]

the exact generalized-prime Kummer profile of PR #269.

Equations (L-26802.6) and (L-26802.12) are the requested source-specific
physical-to-carry intertwiner.

## 5. Annular support and exact weighted isometry

Assume now that

\[
 x_m=0\qquad\text{unless}\qquad M\le m<2M.
 \tag{L-26802.13}
\]

Then

\[
 \operatorname{supp}F_x\subset [M,8M).
 \tag{L-26802.14}
\]

Choose the oversupport row

\[
 N=16M-1.
 \tag{L-26802.15}
\]

For \(1\le j<8M\),

\[
 F_x(N)=F_x(N-j)=0,
\]

and therefore

\[
 (\mathcal S_NF_x)(j)=-F_x(j).
\]

Combining this with (L-26802.7) gives the exact identity

\[
 \boxed{
 \|Q_x\|_2^2
 =
 \sum_{j=1}^{8M-1}
 \frac{|(\mathcal S_NF_x)(j)|^2}{j(j+1)}.
 }
 \tag{L-26802.16}
\]

This is a literal congruence between:

```text
physical space:
    the compact log-prime normal signal Q_x;

carry space:
    the lower-half weighted split defect on row 16M-1.
```

No unidentified operator, compactness limit, or generic norm comparison remains
on one annular source fiber.

The unweighted normalized carry row is also quantitatively comparable. If

\[
 \|u\|_{N,\mathrm{low}}^2
 =\frac1{N+1}\sum_{j=1}^{8M-1}|u(j)|^2,
\]

then

\[
 \boxed{
 \frac{M}{8}\|Q_x\|_2^2
 \le
 \|\mathcal S_NF_x\|_{N,\mathrm{low}}^2
 \le
 8M\|Q_x\|_2^2.
 }
 \tag{L-26802.17}
\]

For proof-facing work, the weighted identity (L-26802.16) is preferable because
it has no scale loss.

## 6. Four-color annular decomposition

The output of an annulus \([M,2M)\) lies in \([M,8M)\). Annuli whose base
scales differ by a factor \(16\) therefore have disjoint physical support.

Consequently, the dyadic annuli split into four color classes

\[
 M=2^{4r+c},
 \qquad c\in\{0,1,2,3\},
\]

such that the physical signals in each fixed color are orthogonal. The full
physical energy is bounded by four times the sum of the four color energies.

Thus a block recurrence may be proved color by color without discarding any
source coefficient or reflected cross term within an annulus.

## 7. What this closes

The former F5PBT/SIFD formulation asked for an unspecified finite operator
between the physical normal block and the carry transition Gram.

On the compact source window \(h_\omega\), equations (L-26802.9) and
(L-26802.16) construct that operator explicitly:

\[
 \boxed{
 \text{annular physical normal Gram}
 =
 \text{weighted lower-half carry split Gram}.
 }
\]

The physical-to-carry source-map problem is therefore closed on each complete
annular fiber.

## 8. What remains open

This lemma does not prove:

1. that the reflected Selberg source energy is bounded by the annular
   generalized-prime Gram;
2. that all proper-divisor and digital boundary terms carry total charge below
   the strict reserve;
3. a lower-scale recurrence for the inverse-zeta source;
4. Bottom-Charge Positivity;
5. RH.

Those obligations are isolated in `T-26802`. The critical square-root
normalization is fully included in (L-26802.4)--(L-26802.7); replacing it by an
unnormalized step norm is an automatic rejection.
