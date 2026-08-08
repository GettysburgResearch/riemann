# L-26212 — Annular normalization exactly absorbs the critical digital-bank loss

Claim ID: `L-26212`  
Title: The \(O(M)\) squared observability cost forced by critical-line modes is exactly canceled by the \(M^{-1}\) normalization in the annular physical-to-carry isometry  
Status: **PROPOSED COMPLETE SCALE-ADAPTER LEMMA PENDING INDEPENDENT REVIEW**  
Date: 2026-08-08  
Depends on: `L-26210`; PR #268 `L-26802/L-26804`; PR #269 factor-five carry feature space  
Scope: exact normalization and conditional frame composition; no upper estimate for the bank observations and no RH conclusion

## 1. Annular physical/carry normalization

Let \(x=(x_m)\) be supported on

\[
M\le m<2M.
\]

For the compact opposite-parity window, PR #268 `L-26802` constructs the physical signal \(Q_x\) and one carry split vector \(V_x\) on row \(16M-1\). Its normalized lower-half carry norm satisfies

\[
\boxed{
\frac M8\,\|Q_x\|_2^2
\le
\|V_x\|_{\rm car}^2
\le
8M\,\|Q_x\|_2^2.
}
\tag{L-26212.1}

For the degree-four critical parity filters, `L-26804` gives the same exact weighted isometry on row \(256M-1\); replacing the unfiltered carry norm by the direct sum of the two parity-channel norms changes only one absolute finite constant.  Denote a valid common constant by \(C_{\rm ann}\).

Thus, in either form,

\[
\boxed{
\|Q_x\|_2^2
\le
\frac{C_{\rm ann}}M
\|V_x\|_{\rm car}^2.
}
\tag{L-26212.2]

## 2. Hilbert-valued critical bank

The proof of `L-26210` is Hilbert valued.  Let \(R=M\), let \(V_x\) play the role of the target vector, and let \(V_{x,d}\) be the complete carry vector exported by the strict digital prefix \(C_{<M/d}\) and the declared scale-\(d\) source translation.  Then

\[
\boxed{
\|V_x\|_{\rm car}^2
\le
C_{\rm bank}M
\sum_{d<M}\pi_M(d)
\|V_{x,d}\|_{\rm car}^2,
}
\tag{L-26212.3]

where

\[
C_{\rm bank}
=\frac{25}{\kappa_*^2},
\qquad
\kappa_*=(\sqrt2-1)(1-2^{-3/2}),
\]

and

\[
\pi_M(d)
=
\frac{|\omega_2(d)|d^{-1/2}}
{\sum_{r<M}|\omega_2(r)|r^{-1/2}}.
\]

The factor \(M\) is the sharp critical order.  It may not be replaced by a polylogarithm on a source class containing genuine critical-line modes.

## 3. Exact cancellation of scales

Combining (L-26212.2) and (L-26212.3) gives

\[
\boxed{
\|Q_x\|_2^2
\le
C_{\rm ann}C_{\rm bank}
\sum_{d<M}\pi_M(d)
\|V_{x,d}\|_{\rm car}^2.
}
\tag{L-26212.4]

The critical factor \(M\) has disappeared exactly.  It is paid by the conversion from an unweighted row feature to the critically normalized physical annulus.

This explains why the critical-order correction of PR #236 does not destroy the annular programme: the physical/carry isometry carries precisely the reciprocal scale.

## 4. RH-sensitive specialization

Take

\[
x_m=\Lambda_\omega(m)\mathbf1_{[M,2M)}(m).
\]

Then \(Q_x\) is the RH-sensitive annular physical source of PR #268 `L-26802`, and \(V_x\) is its exact carry split \(W_n\).  The strict prefixes in (L-26212.3) are source-bound digital observations of this same feature; they are not the pole-blind generalized-prime profile \(P_n\) unless the complete source-change ledger proves that identification.

The exact relation

\[
c_2*(\omega_2*\Lambda_\omega)
=
\left(\varepsilon-\frac52\delta_2+\delta_4\right)*\Lambda_\omega
\tag{L-26212.5]

shows that the complete bank output is a finite three-scale combination of the generalized-prime feature.  `L-26211` further splits the bank into a current critical component and a strict lower-scale remainder.

## 5. Consequence for the live full proposal

The remaining annular theorem no longer needs to overcome a polynomial conditioning loss.  It must prove only that the weighted bank observations in (L-26212.4) are the sum of:

1. the factor-five transition form on quotient cells \(2,3,4\);
2. the nonnegative proper-divisor half-scale defect of PR #268 `L-26803`;
3. the explicit digital and endpoint collars;
4. strict lower-scale source outputs whose total charge is below the carry reserve.

The exact physical-to-carry map and the critical normalization are already closed at their declared scopes.

## 6. Firewalls

Reject any use of this lemma that:

- applies the bank to the pole-blind coefficient \(a_\omega\log\) instead of the RH-sensitive source without an exact source map;
- drops the factor \(M\) in the carry/physical normalization;
- uses the critical bank with \(R\) unrelated to the annular scale;
- replaces the weighted observation average by one arbitrary prefix;
- takes total variation of the lower-scale hyperbola remainder;
- suppresses a critical-line mode by claiming a subcritical bank rate.

## 7. Proof boundary

Closed, subject to review:

- the exact cancellation of the critical \(O(M)\) bank cost against annular normalization;
- the resulting physical-to-bank scale-free inequality;
- compatibility with the RH-sensitive annular source and the finite three-scale output.

Open:

- a source-complete upper estimate for the bank observations;
- the strict transition-versus-lower-scale reserve;
- RH.
