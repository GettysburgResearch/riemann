# L-97102 — The scalar reciprocal-Julia channel is an alternating divisor martingale with logarithmic energy

Claim ID: `L-97102`  
Status: **PROVED EXACT ENERGY THEOREM**  
Created: 2026-08-17  
Depends on: `L-97101`  
RH status: **not assumed**

For `n>1`, define
\[
P_n(d)=
\frac{\Lambda_\diamond(d)g_\diamond(n/d)}
     {g_\diamond(n)\log n},
\qquad d\mid n,\ d>1.
\]
By (L-97101.5), this is a probability distribution. Put
\[
f_\diamond(n)=\frac{b_\diamond(n)}{g_\diamond(n)}\in[-1,1].
\]
Equation (L-97101.6) gives
\[
\boxed{f_\diamond(n)=-\sum_dP_n(d)f_\diamond(n/d).}
\tag{L-97102.1}
\]
Thus for the descending divisor chain `N_(t+1)=N_t/d`,
\[
\boxed{(-1)^t f_\diamond(N_t)\text{ is a bounded martingale}.}
\tag{L-97102.2}
\]
This is the exact probabilistic form of cumulative rough parity.

The only nonzero dyadic fibres over an odd squarefree `m` contribute
\[
\begin{array}{c|c}
e&b_\diamond(2^em)^2/[g_\diamond(2^em)2^em m]\\ \hline
0&1/m\\
1&5/(4m)\\
2&4/(17m)\\
3&1/(196m).
\end{array}
\]
Therefore
\[
\boxed{
\sum_{n\le X}\frac{b_\diamond(n)^2}{g_\diamond(n)n}
\le
\frac{4149}{1666}(1+\log X).
}
\tag{L-97102.3}
\]
Also
\[
\sum_{e\ge0}\frac{2e+2^{-e}}{2^e}=\frac{16}{3},
\]
so
\[
\boxed{
\sum_{n\le X}\frac{g_\diamond(n)}n
\le\frac{16}{3}(1+\log X).
}
\tag{L-97102.4}
\]

The signed channel and the positive trace both live at logarithmic energy. Absolute scalarization is therefore not forced by scale. Nevertheless, (L-97102.3) alone does not imply the one-sided prefix bound below; a valid completion must preserve the martingale covariance through its boundary extraction.
