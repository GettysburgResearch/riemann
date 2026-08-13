# L-91415 — The fractional Lorenz cutoff cancels, leaving one strict-prefix determinant

Status: **PROVED EXACT REDUCTION**. RH remains unproved.

Let `c` be the even cutoff atom of the leftmost score-Lorenz submeasure `U`. All even score mass at `e<c` is used, a fraction of the mass at `c` may be used, and no mass above `c` is used.

In the finite-prefix gap of `L-91412`, the cutoff atom is multiplied by `q(c)-q(c)=0`. Since `c` has positive parity, the odd prefix also contains no atom at `c`. Therefore
\[
\boxed{
G_{pre}=
\sum_{\substack{d<c\\ d\mid P_{61}}}
\mu(d)K_S(d)[q(d)-q(c)].
}
\]

Put
\[
S_{<c}=\sum_{d<c}\mu(d)K_S(d),
\qquad
R_{<c}^{(j)}=\sum_{d<c}\mu(d)K_R^{(j)}(d).
\]
Then
\[
\boxed{
G_{pre}=
\frac{R_{<c}^{(j)}K_S(c)-S_{<c}K_R^{(j)}(c)}{K_S(c)}.
}
\]

Hence the complete Lorenz row gate follows from the strict-prefix determinant
\[
\boxed{
\Pi_{j,c}(p,y)=
R_{<c}^{(j)}K_S(c)-S_{<c}K_R^{(j)}(c)\ge0.
}

This gate uses only divisors `d<c<2000`; the fractional cutoff amount and every source above `c` disappear from the hard row calculation. Sources above `c` contribute only the nonnegative tail reserve from `L-91412`.
