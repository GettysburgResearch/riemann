# Independent review of the coherent full remainder vector

23 October 2026. This review binds
`work/two-hour-boundary-20261023/COHERENT_FULL_REMAINDER_VECTOR.md`, SHA256
`f6058c80c4bde0f049f7f7a50740cfae4d4a158a88e1bc6c0cb8534be8f215a4`.
It also uses the unchanged reflected-completion scope note
`39850353a97e596a8e0ebabfecaf41b954cceed2026612a91ae0716eb62cb040`
and sixth-free extension
`3e4a3d902aa937d7a498ab1201a269e6891265a9b1c8a34945524c330797b507`.

Verdict: no defect found in the deduction of C1 from its specified vector
inputs. This is a source-dependent analytic review, not an independent proof
of the upstream inverse estimate or a finite-computation certificate of C1.
It concerns the full-series contour vector; primitive inversion and the
complementary inverse operator are not conclusions.

I independently checked the following interfaces and exponents.

1. The reflected numerator, Gauss orientation and fixed local vector are
   those in the previously reviewed completed kernel. The three R2 branches
   imply C4: for `C<=H`, both `HC<=H^2` and
   `H D^(5/6) C^(1/6)<=D^(5/6)H^(7/6)`; the middle and large branches are
   directly included. Rapid decay covers `C<1`. Summing dyadic labels only
   costs logarithms and replaces H by K. The profile separation is performed
   on common norm coordinates before applying the inverse estimate.
2. In the exact reciprocal identity C5, each ideal contributes `mu(a)/Na`
   and the sixth-power scale `U/(Na)^6`. The argument uses absolute values
   of these coefficients, so no Mertens premise is required. Minkowski is
   taken in the same finite label Hilbert space throughout.
3. For `A=U^(1/6)(DK)^(-1/12)>=1`, the reflected volume head sums a squared
   ideal weight to give amplitude `(DK/U)^(1/2) A^3=(DK)^(1/4)`.
   The original volume tail gives `U^(1/2) A^(-3)` with the same value.
   The reflected nonvolume head and original nonvolume tail both have
   amplitude `D^(11/24)K^(1/24)`. Thus their squared cost is exactly
   `D^(11/12)K^(1/12)`.
4. The completed original finite vector B is zero once its positive physical
   modulus annulus is below the first admissible modulus. Consequently the
   original plateau has only the finite range `A<Na<<U^(1/6)`; its `1/Na`
   sum is harmonic, not an infinite divergent plateau. The reflected plateau
   likewise has the finite head `Na<=A`. The resulting squared plateau
   remains `K^2+D^(5/6)K^(7/6)`.
5. The exact finite-minus-pole identity is used for the whole original tail,
   including subunit scales. The full residue vector S1 gives pole amplitude
   `U^(1/6)D^(1/3)A^(-1)=D^(5/12)K^(1/12)`, hence squared cost
   `D^(5/6)K^(1/6)`. This is not dropped merely because B has vanished.
6. For `K<=D`, `(DK)^(1/2)` and `D^(5/6)K^(1/6)` are bounded by
   `D^(11/12)K^(1/12)`, and `K^2<=D^(5/6)K^(7/6)`. The stronger
   `K<=D^(1/7)` hypothesis is needed for the imported residue estimate.
   Comparing the two surviving terms with `D^(5/6+h/6)` gives precisely
   `k<2h-1` and `k<h/7`, in addition to the source ranges and fixed epsilon
   slack stated in C7.

The new argument uses the same completion plateau that blocked a previous
uncompleted reflected estimate. Its improvement comes from balancing the
coherent reflected vector against the original vector before the global
reciprocal split, not from deleting that plateau. This distinction is correctly
preserved. The earlier reflected-envelope review was my independent source
audit; this review independently checks the new balancing deduction, while
retaining that audited input rather than claiming to prove it a second time.

No assertion about the primitive vector, full inverse norm, a new fixed
zero-free boundary, or RH is licensed by this review alone.
