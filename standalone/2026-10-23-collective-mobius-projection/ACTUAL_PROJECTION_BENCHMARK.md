# An exact benchmark for the whole primitive projection

23 October 2026. This is a consumer of the proposed, separately reviewed
analytic lemmas; the accompanying finite rational replay checks algebra,
not those analytic imports.

The component hashes are:

- PRIMITIVE_LABEL_CONTINUATION.md:
  a10b7626fc5a7ab7315f8327c53b2fcbe1381a2f04816a04aa697309803976ee.
- SIXTH_FREE_LABEL_EXTENSION.md:
  3e4a3d902aa937d7a498ab1201a269e6891265a9b1c8a34945524c330797b507.

Use all the fixed ray, smoothing, puncture, literal primitive exclusion,
and exact adjoint-orientation hypotheses of P14. Let

\[
 U=D^{6/7},\qquad K=D^{1/32}.
\]

The inherited inverse norm estimate has nonvolume term

\[
 U^{1/6}D^{5/6}=D^{41/42}.
\]

P14 bounds the projection onto the span of all good sixth-power-free
labels of norm at most \(K\) by the sum of three terms:

| Term | Exact exponent of \(D\) |
|---|---:|
| \(KU\) | \(199/224\) |
| \(D^{11/12}K^{13/12}\) | \(365/384\) |
| \(U^{1/3}D^{2/3}\) | \(20/21\) |

The last exponent is the largest. The primitive pole vector range
\(K\le D^{1/7}\) and the Gram range \(K\le U^{1/2-\delta}\) both hold
with fixed slack; for example \(\delta=1/4\) is allowed. Consequently

\[
 \left\|\operatorname{proj}_{\operatorname{span}\{v_R:NR\le D^{1/32}\}}
               A_U\alpha\right\|^2
 \ll D^{20/21+\epsilon}.                                      \tag{B1}
\]

This is a saving \(D^{1/42}\), up to the usual arbitrary epsilon,
against the earlier full inverse upper bound at this scale. All
sixth-power-free labels are retained in this projection, including
their natural zeros. This is a growing space, not a statement about
just the principal vector.

Here \(A_U\alpha\) is matrix multiplication, not an adjoint applied to
the column vector. The adjoint identity used in its proof is
\(\langle A_U\alpha,v_R\rangle=\langle\alpha,A_U^*v_R\rangle\).

The complementary projection is not estimated by B1. In particular
one cannot subtract B1 from an upper bound for the full norm to infer
a smaller upper bound for the complement. No zero-free-boundary
improvement or proof of RH follows from B1 alone.

The next useful target is a matching estimate on
\((I-\operatorname{proj}_{\{v_R\}})A_U\alpha\), or a signed source
return in which this complementary term cancels. Such a target must
retain the common Poisson kernel and the actual Möbius coefficient.
