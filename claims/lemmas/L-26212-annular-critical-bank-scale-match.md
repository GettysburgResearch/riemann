# L-26212 — Conditional annular matching of the critical digital-bank scale

Claim ID: `L-26212`  
Title: The \(O(M)\) squared observability cost forced by critical-line modes matches the \(M^{-1}\) annular physical-to-carry normalization once all bank observations are embedded in one common source metric  
Status: **PROPOSED CONDITIONAL SCALE-ADAPTER — COMMON SOURCE-IMAGE EMBEDDING REMAINS OPEN**  
Date: 2026-08-08  
Depends on: `L-26210`; PR #268 `L-26802/L-26804`; PR #269 factor-five carry feature space  
Scope: exact scalar cancellation after one declared intertwining hypothesis; no physical bank embedding, observation upper estimate, or RH conclusion

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
\]

For the degree-four critical parity filters, `L-26804` gives an exact weighted isometry on row \(256M-1\). The two parity channels and their finite delays may be placed in a fixed finite direct sum. Denote a valid annular comparison constant by \(C_{\rm ann}\).

For the **unbanked annular source**, this gives

\[
\boxed{
\|Q_x\|_2^2
\le
\frac{C_{\rm ann}}M
\|V_x\|_{\rm car}^2.
}
\tag{L-26212.2}
\]

## 2. Hilbert-valued critical bank

The proof of `L-26210` is Hilbert valued. Abstractly, if \(V\) is one vector in a Hilbert space and \(V_d\) are the complete strict-prefix observations appearing in its digital bank, then with \(R=M\),

\[
\boxed{
\|V\|^2
\le
C_{\rm bank}M
\sum_{d<M}\pi_M(d)
\|V_d\|^2,
}
\tag{L-26212.3}
\]

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

The factor \(M\) is the sharp critical order. It may not be replaced by a polylogarithm on a source class containing genuine critical-line modes.

## 3. The conditional scale cancellation

To combine (L-26212.2) and (L-26212.3), one needs an exact common-metric source map. Namely, the banked production object must provide vectors \(V_{x,d}\) in one declared annular carry Hilbert space such that:

1. \(V_x\) is the carry image of the RH-sensitive annular physical signal \(Q_x\);
2. \(V_{x,d}\) is the carry image of the strict-prefix physical observation indexed by \(d\);
3. the translation, source scaling, row index, weight \(1/[j(j+1)]\), parity delays, and oversupport collars are all included in the map;
4. the bank identity of `L-26210` holds in that common Hilbert space.

Call this the **common annular bank embedding**.

If that embedding is supplied, then (L-26212.3) applies with \(V=V_x\), and (L-26212.2) gives

\[
\boxed{
\|Q_x\|_2^2
\le
C_{\rm ann}C_{\rm bank}
\sum_{d<M}\pi_M(d)
\|V_{x,d}\|_{m car}^2.
}
\tag{L-26212.4}

Under the embedding, the critical factor \(M\) is paid exactly by the annular normalization \(M^{-1}\).

Without the embedding, writing (L-26212.4) is invalid: a multiplicative prefix changes source support, annular scale, physical row, and endpoint collar. Those observations cannot simply be declared to live in the metric of \(V_x\).

## 4. RH-sensitive specialization

The intended coefficient is

\[
x_m=\Lambda_\omega(m)\mathbf1_{[M,2M)}(m).
\]

Then \(Q_x\) is the RH-sensitive annular physical source of PR #268 `L-26802`, and \(V_x\) is its exact carry split \(W_n\).

The strict prefixes must remain source-bound observations of \(W_n\). They are not the pole-blind generalized-prime feature \(P_n\) unless an exact source-change ledger proves that identification.

The full source relation

\[
c_2*(\omega_2*\Lambda_\omega)
=
\left(\varepsilon-\frac52\delta_2+\delta_4\right)*\Lambda_\omega
\tag{L-26212.5}
\]

shows why a finite generalized-prime output is available after the complete digital convolution. `L-26211` gives an exact current/lower-scale hyperbola split. Neither identity alone constructs the common annular bank embedding.

## 5. Consequence for the live full proposal

The scalar exponents are compatible: the unavoidable critical bank cost is of precisely the order which annular normalization can absorb.

The remaining production theorem must still prove simultaneously:

1. the common annular bank embedding;
2. the factor-five transition ledger on quotient cells \(2,3,4\);
3. the nonnegative proper-divisor half-scale defect of PR #268 `L-26803`;
4. the explicit digital, commutator, endpoint, and oversupport collars;
5. a net transition-versus-lower-scale reserve.

Thus this lemma removes a potential **rate obstruction** but does not remove the source-image theorem.

## 6. Firewalls

Reject any use of this lemma that:

- applies the bank to the pole-blind coefficient \(a_\omega\log\) instead of the RH-sensitive source without an exact source map;
- drops the factor \(M\) in the carry/physical normalization;
- uses the critical bank with \(R\) unrelated to the annular scale;
- places prefix observations from different source supports or row indices in one norm without an explicit intertwiner;
- replaces the weighted observation average by one arbitrary prefix;
- takes total variation of the lower-scale hyperbola remainder;
- suppresses a critical-line mode by claiming a subcritical bank rate.

## 7. Proof boundary

Closed, subject to review:

- the compatibility of the critical \(O(M)\) bank exponent with the annular \(M^{-1}\) normalization;
- the exact scalar cancellation after a declared common source embedding;
- the identification of the data that embedding must preserve.

Open:

- the common annular bank embedding itself;
- a source-complete upper estimate for the bank observations;
- the strict transition-versus-lower-scale reserve;
- RH.
