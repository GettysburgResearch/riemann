# Proof extract

The source-faithfulness gate is closed by
\[
P_v=B_v\oplus\bigoplus_w r_{v,w}SP_w
=C_v(t)\oplus\bigoplus_wt_{v,w}SP_w.
\]
Every coefficient, activation and owner is literal, and the root observation is
the exact annular scalar.

For any even `L=O(log log log X)`, the critical `1/p` layer sums satisfy
\[
E_j(X)=\frac{z^j}{j!}(1+o(1)),\qquad z\sim\log\log X.
\]
Since `z/L->infinity`, the odd last layer dominates:
\[
\sum_{j<L}(-1)^jE_j<-\frac23E_{L-1}.
\]
The bounded base remainder contributes
\[
o(\sqrt X E_{L-1}),
\]
so the literal current is eventually negative.

Therefore neither the cutoff-239 local recursion nor the adaptive
small-prime-depth repair supplies the needed sign. The remaining theorem is the
critical product-boundary NCBI67/CPSL67 inequality.
