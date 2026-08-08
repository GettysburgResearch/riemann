# L-26804 — Critical Euler-filtered annular split frame

Claim ID: `L-26804`  
Title: Every finite dyadic translation filter preserves the exact annular physical/carry isometry; the critical Euler filter cancels the pole and double half-pole modes  
Status: **PROPOSED COMPLETE EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-source-specific`  
Created: 2026-08-08  
Dependencies: `L-26802`, `R-26802`; PR #263 `L-26201/L-26205/L-26206`; PR #241 `L-9518`  
Scope: safe compact geometry for arbitrary source coefficients; no source-change estimate, recurrence, or RH conclusion

## 1. Polynomial translation filter

Let

\[
 p(z)=\sum_{j=0}^{d}c_jz^j
\]

be a fixed real polynomial, let \(L=\log2\), and let

\[
 (\tau_Lf)(t)=f(t-L).
\]

Starting from the compact normalized window \(h_\omega\) of `L-26802`, define

\[
 \boxed{H_p=p(\tau_L)h_\omega.}
 \tag{L-26804.1}
\]

Its Laplace multiplier is

\[
 P(s)=p(2^{-s}).
 \tag{L-26804.2}
\]

For any finite coefficient vector \(x\), put

\[
 Q_{p,x}=H_p*
 \sum_m\frac{x_m}{\sqrt m}\delta_{\log m}.
 \tag{L-26804.3}
\]

Since translation commutes with convolution,

\[
 Q_{p,x}=p(\tau_L)Q_x.
 \tag{L-26804.4}
\]

## 2. Exact integer potential after filtering

Let \(F_x\) be the potential of `L-26802`. For almost every
\(\log r\le t<\log(r+1)\),

\[
 Q_x(t-jL)
 =2^{j/2}e^{-t/2}
 F_x\!\left(\left\lfloor\frac r{2^j}\right\rfloor\right).
 \tag{L-26804.5}
\]

Therefore

\[
 \boxed{Q_{p,x}(t)=e^{-t/2}F_{p,x}(r),}
 \tag{L-26804.6}
\]

where

\[
 \boxed{
 F_{p,x}(r)
 =\sum_{j=0}^{d}c_j2^{j/2}
 F_x\!\left(\left\lfloor\frac r{2^j}\right\rfloor\right).
 }
 \tag{L-26804.7}
\]

Consequently,

\[
 \boxed{
 \|Q_{p,x}\|_2^2
 =\sum_{r\ge1}\frac{|F_{p,x}(r)|^2}{r(r+1)}.
 }
 \tag{L-26804.8}
\]

Every finite translation-filtered physical source remains an exact weighted
integer potential.

## 3. Filtered annular isometry

Assume \(x_m=0\) unless \(M\le m<2M\). Since

\[
 \operatorname{supp}F_x\subset[M,8M),
\]

one has

\[
 \operatorname{supp}F_{p,x}\subset[M,2^{d+3}M).
 \tag{L-26804.9}
\]

Set

\[
 U=2^{d+3}M,
 \qquad
 N=2U-1=2^{d+4}M-1.
 \tag{L-26804.10}
\]

For \(1\le r<U\),

\[
 F_{p,x}(N)=F_{p,x}(N-r)=0.
\]

Hence

\[
 \boxed{
 \|Q_{p,x}\|_2^2
 =\sum_{r=1}^{U-1}
 \frac{|(\mathcal S_NF_{p,x})(r)|^2}{r(r+1)}.
 }
 \tag{L-26804.11}
\]

This is exact for every fixed translation polynomial and every annular source
coefficient sequence.

## 4. The critical Euler filter

Take

\[
 \boxed{
 p_{\rm crit}(z)
 =(1-z)(1-2z)(1-\sqrt2z)^2.
 }
 \tag{L-26804.12}
\]

Its coefficients are

\[
 \boxed{
 p_{\rm crit}(z)
 =1-(3+2\sqrt2)z
 +(4+6\sqrt2)z^2
 -(6+4\sqrt2)z^3
 +4z^4.
 }
 \tag{L-26804.13}
\]

The multiplier \(p_{\rm crit}(2^{-s})\) has:

- a zero at \(s=0\);
- a zero at \(s=1\);
- a double zero at \(s=1/2\).

Thus the filtered compact window cancels the constant, pole, and double
half-pole modes used in the critical Euler-fiber programme.

The degree is four, so a coefficient annulus \([M,2M)\) has filtered output
support in \([M,128M)\), and

\[
 \boxed{N_{\rm crit}=256M-1.}
 \tag{L-26804.14}
\]

Equation (L-26804.11) becomes

\[
 \boxed{
 \|Q_{{\rm crit},x}\|_2^2
 =\sum_{r=1}^{128M-1}
 \frac{|(\mathcal S_{256M-1}F_{{\rm crit},x})(r)|^2}{r(r+1)}.
 }
 \tag{L-26804.15}
\]

## 5. RH-sensitive specialization and parity companion

The RH-sensitive choice is

\[
 \boxed{x_m=\Lambda_\omega(m).}
 \tag{L-26804.16}
\]

By `R-26802`, its transform retains every reciprocal-zeta logarithmic-
derivative pole. The split vector is a finite dyadic combination of the
RH-sensitive carry feature

\[
 W_n(j)=\sum_q(\omega_2*\Lambda_\omega)(q)\chi_{n,q}(j).
\]

The companion filter \(p_{\rm crit}(-z)\) satisfies the same exact annular
identity. PR #263 proves the frame reserve

\[
 |p_{\rm crit}(z)|^2+|p_{\rm crit}(-z)|^2
 \ge\frac{45}{4}
\]

on the declared critical annulus and gives a finite positive Bézout
reconstruction.

Thus both safe physical channels have explicit carry split maps, and the
original reciprocal-zeta source is reconstructed by finitely many dyadic
delays.

The alternative choice \(x=a_\omega\log\) yields PR #269's carry profile
\(P_n\), but `R-26802` proves that its physical primitive is pole blind. It may
not replace (L-26804.16).

## 6. What this closes

The exact finite-source level now contains:

1. critically safe compact windows;
2. explicit physical-to-carry maps for the RH-sensitive source;
3. the parity companion and finite synthesis;
4. exact support and oversupport constants.

The former generic source-map existence problem is closed.

## 7. What remains open

The established strict carry reserve is for

\[
 P_n=\sum_q\Lambda_\omega(q)\chi_{n,q},
\]

not automatically for the RH-sensitive feature \(W_n\). The exact relation is

\[
 a_\omega*W=P.
\]

A proof must either:

- transfer the reserve through this source change with a strict quantitative
  bound; or
- prove a direct reflected reserve for \(W\).

It must then show that every proper-divisor and digital lower-block charge is
strictly below the current reserve.

## 8. Firewalls

Reject any use of this lemma that:

- drops the factor \(2^{j/2}\) in (L-26804.7);
- uses \(128M-1\) instead of \(256M-1\);
- treats one parity channel as a frame by itself;
- claims that mode cancellation proves contraction;
- substitutes a one-frequency integral for the physical block;
- uses \(a_\omega\log\) as the RH-sensitive physical coefficient;
- silently replaces \(W\) by \(P\);
- ignores the proper-divisor defect of `L-26803`.

## 9. Proof boundary

Closed exactly:

1. polynomial-filtered cell potential;
2. filtered weighted physical/carry isometry;
3. critical pole and half-pole cancellations;
4. exact support and oversupport constants;
5. compatibility with the RH-sensitive source, parity companion, and finite
   synthesis.

Open:

1. the RH-sensitive source-change/direct reserve theorem;
2. the reflected current-versus-lower-scale reserve inequality;
3. complete boundary charge accounting;
4. the corrected annular recurrence;
5. RH.
