# L-105211 — Seven-gap pressure and global defect averaging

Claim ID: `L-105211`  
Status: **EXACT DEDUCTION CONDITIONAL ON PINNED FINITE CERTIFICATE**  
External finite premise: `ainta/zeta-simple-zeros@040c5e8`

Let \(k\) be the normalized Montgomery–Taylor overlap kernel and
\(w(x)=k(x)^2\). The pinned Arb certificate proves, for all
\(g_1,\ldots,g_6\ge0\),
\[
\frac1{3000}\sum_{i=1}^6 g_i
+
\sum_{s=1}^6\frac{2}{7-s}
\sum_{i=1}^{7-s}
w(g_i+\cdots+g_{i+s-1})
\ge \frac{19}{5000}.
\tag{1}
\]

For \(m\) ordered points \(y_1<\cdots<y_m\), put
\[
E_m=2\sum_{1\le i<j\le m}w(y_j-y_i).
\]
Summing (1) over all consecutive seven-point windows gives
\[
\boxed{
E_m+\frac1{500}(y_m-y_1)
\ge \frac{19}{5000}(m-6).
}
\tag{2}
\]

The coefficient \(1/500\), not \(1/3000\), is forced because an interior gap
appears in six consecutive seven-point windows.

For a consecutive block of \(269\) simple critical-line zeros, convex
pinching and the spectral defect from L-105210 give
\[
\Delta(G_B)+\frac1{500}\operatorname{span}(B)
\ge \frac{4997}{5000}-o(1).
\]
Averaging over all \(269\) offsets yields
\[
\boxed{
\Delta(M)
\ge
\frac{4997}{1\,345\,000}S
-
\frac{268}{134\,500}N
-o(N),
}
\tag{3}
\]
where \(S=N_0^s(T,2T)\) and \(N=N(T,2T)\).

Equation (3) is the exact global input to T-105210.
