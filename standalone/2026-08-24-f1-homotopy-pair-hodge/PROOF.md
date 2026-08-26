# Homotopy-coherent F1 Hodge trace and degree-two pair geometry

The finite F1 source and Hodge package is exact, but a cofinal estimate is
sensitive to the order of operations.  Removing the first chaos and then
squaring the Wick remainder is power-lossy.  Its Dirichlet source has the real
singularity

\[
D_{\ge2}(z)
=
C_{67}\log\frac1{z-1}+O(1),
\]

and the filtered-disk slope has nonzero half-order moment.  Thus the isolated
Hodge energy is asymptotic to a positive constant times \(X/\log^2X\).

The correct primitive vector is formed from the full tangent path and integrated
before squaring.  If

\[
v_\tau=(A_\tau/\sqrt{24},\sqrt2(G_\tau-A_\tau)),
\]

then

\[
\int\|v_\tau\|^2
=
\left\|\int v_\tau\right\|^2
+
\int\left\|v_\tau-\int v_\sigma d\sigma\right\|^2d\tau.
\]

The first term is the coherent native-minus-completion energy; the second is
the nonnegative debt created by premature homotopy squaring.

For the unordered pair current, attach \(v_{ij}\) to the codimension-two
stratum \(x_ix_j\) of the prime box.  With \(S=\sum v_{ij}\) and
\(r_i=\sum_jv_{ij}\),

\[
2\sum_{\text{disjoint pairs}}\langle v_{ij},v_{k\ell}\rangle
=
\|S\|^2+\sum\|v_{ij}\|^2-\sum\|r_i\|^2.
\]

The diagonal is already subpower.  Therefore the physical trace is bounded by
the positive four-distinct-label Hodge intersection plus the shared-owner star
energy.  Their conjunction implies the coherent trace theorem and hence RH.

Neither arithmetic estimate is proved here.  RH remains unproved.
