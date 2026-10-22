# L-26802 — Exact annular physical-to-carry split isometry

Claim ID: `L-26802`  
Title: The compact opposite-parity physical window is exactly a weighted carry split on one oversupport row  
Status: **PROPOSED COMPLETE EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-source-specific`  
Created: 2026-08-08  
Dependencies: PR #268 `L-26201/L-26202`; PR #269 `L-26901/L-26903`; PR #241 `L-9518`; `R-26802`  
Scope: exact geometry for arbitrary source coefficients; no source-change estimate, recurrence, or RH conclusion

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

Thus \(g_m\) is the literal compact output of the complete opposite-parity
arithmetic source.

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

For almost every \(t\) with \(\log r\le t<\log(r+1)\),

\[
 \boxed{
 Q_x(t)=e^{-t/2}F_x(r).
 }
 \tag{L-26802.6}
\]

Consequently,

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
 Z_{n,m}(j)=g_m(n)-g_m(j)-g_m(n-j).
\]

Therefore

\[
 \boxed{
 (\mathcal S_nF_x)(j)
 =\sum_m x_m Z_{n,m}(j).
 }
 \tag{L-26802.9}
\]

The physical source and the carry feature are the same finite coefficient
family before and after one explicit additive-split operator.

## 4. Two distinct source specializations

Let

\[
 a_\omega(2^\nu u)=2\nu+2^{-\nu}
 \qquad(u\text{ odd}),
\]

and

\[
 \Lambda_\omega=\omega_2*(a_\omega\log).
\]

### 4.1 RH-sensitive physical source

The correct RH-sensitive specialization is

\[
 \boxed{x_m=\Lambda_\omega(m).}
 \tag{L-26802.10}
\]

Its physical transform contains

\[
 -\frac{A_\omega'}{A_\omega}(s)
 =-\frac{\zeta'}{\zeta}(s)+\frac{E'}E(s),
 \qquad
 E(s)=(1-2^{-s})(1-2^{-s-1}),
\]

so every hypothetical off-line zeta zero remains a pole.

Equations (L-26802.3) and finite convolution give

\[
 \boxed{
 F_\Lambda(r)
 =\sum_{q\le r}(\omega_2*\Lambda_\omega)(q)
  \left\lfloor\frac rq\right\rfloor,
 }
 \tag{L-26802.11}
\]

and hence

\[
 \boxed{
 (\mathcal S_nF_\Lambda)(j)
 =\sum_{q\le n}(\omega_2*\Lambda_\omega)(q)\chi_{n,q}(j).
 }
 \tag{L-26802.12}
\]

Denote this RH-sensitive carry feature by \(W_n\).

### 4.2 Positive-inverse carry source

For

\[
 x_m=a_\omega(m)\log m,
 \tag{L-26802.13}
\]

one instead obtains

\[
 \boxed{
 (\mathcal S_nF_x)(j)
 =\sum_{q\le n}\Lambda_\omega(q)\chi_{n,q}(j)
 =:P_n(j),
 }
 \tag{L-26802.14}
\]

the generalized-prime Kummer profile controlled on PR #269.

However, `R-26802` proves that the corresponding physical primitive is
holomorphic at every zeta zero: the reciprocal-zeta pole cancels. Thus
\(x=a_\omega\log\) is useful in carry space but is not the RH-sensitive
physical source.

The exact relation between the two carry coefficient sequences is

\[
 \boxed{
 a_\omega*(\omega_2*\Lambda_\omega)=\Lambda_\omega.
 }
 \tag{L-26802.15}
\]

Transferring the strict reserve from \(P_n\) to \(W_n\), or proving a direct
reserve for \(W_n\), is a separate arithmetic theorem.

## 5. Annular support and exact weighted isometry

Assume

\[
 x_m=0\qquad\text{unless}\qquad M\le m<2M.
 \tag{L-26802.16}
\]

Then

\[
 \operatorname{supp}F_x\subset[M,8M).
 \tag{L-26802.17}
\]

Choose

\[
 N=16M-1.
 \tag{L-26802.18}
\]

For \(1\le j<8M\), one has

\[
 F_x(N)=F_x(N-j)=0,
\]

so

\[
 (\mathcal S_NF_x)(j)=-F_x(j).
\]

Combining with (L-26802.7) gives

\[
 \boxed{
 \|Q_x\|_2^2
 =
 \sum_{j=1}^{8M-1}
 \frac{|(\mathcal S_NF_x)(j)|^2}{j(j+1)}.
 }
 \tag{L-26802.19}
\]

This is an exact congruence for every annular coefficient sequence \(x\), in
particular for the RH-sensitive sequence \(x=\Lambda_\omega\).

The unweighted normalized lower-half row obeys

\[
 \boxed{
 \frac{M}{8}\|Q_x\|_2^2
 \le
 \|\mathcal S_NF_x\|_{N,\mathrm{low}}^2
 \le
 8M\|Q_x\|_2^2.
 }
 \tag{L-26802.20}
\]

The weighted identity (L-26802.19) is the proof-facing form because it has no
scale loss.

## 6. Four-color annular decomposition

The output of \([M,2M)\) lies in \([M,8M)\). Annuli whose base scales differ
by a factor \(16\) have disjoint physical support. Thus four color classes
suffice for the unfiltered window.

The degree-four critical filters of `L-26804` enlarge this to eight colors.

## 7. What this closes

The exact annular geometry and the physical-to-carry map for the RH-sensitive
feature \(W_n\) are closed:

\[
 \boxed{
 \text{annular RH-sensitive physical Gram}
 =
 \text{weighted carry Gram of }W_n.
 }
\]

No unidentified operator remains.

## 8. What remains open

This lemma does not prove:

1. a strict reserve for the RH-sensitive feature \(W_n\);
2. transfer of PR #269's reserve from \(P_n\) through
   \(a_\omega*W=P\);
3. that all proper-divisor and digital boundary charges lie below the current
   reserve;
4. a lower-scale recurrence;
5. Bottom-Charge Positivity;
6. RH.

The source distinction in Section 4 is mandatory. Silently replacing \(W\) by
\(P\) is an automatic rejection.
