# L-91413 — The finite Euler scale gap makes every cutoff determinant positive for sufficiently large `p`

Status: **PROVED ASYMPTOTIC TAIL REDUCTION — AN EFFECTIVE THRESHOLD IS NOT YET EXTRACTED**. RH remains unproved.

For fixed `2<=j<=66`, Euler summation in the exact Green formula gives
\[
Q_Y(j)=a_j\sqrt Y+\lambda_j\log Y+b_j+O_j(Y^{-1/2}\log Y),
\]
where
\[
a_j=\frac8{j(j-1)},
\]
and
\[
\lambda_j=
\frac2{j(j-1)}\zeta(1/2)
-\frac2{j(j-1)}\sum_{m<j}m^{-1/2}
+\frac{j+2}{j\sqrt j}-\frac1{\sqrt{j+1}}<0.
\]

For `P=P_61`, define
\[
A_P=\prod_{q\mid P}(1-q^{-1}),
\qquad
B_P=\prod_{q\mid P}(1-q^{-1/2}),
\qquad
\vartheta_P=B_P/A_P.
\]
Exactly,
\[
\vartheta_P=\prod_{q\mid P}(1+q^{-1/2})^{-1}<1.
\]

Once the parent endpoint `x=py` activates the complete finite Euler block, the signed parent score and row have the uniform expansions
\[
S_{sig}=5A_P\sqrt x-3B_P+O(x^{-1/2}),
\]
\[
R_{sig}^{(j)}=a_jA_P\sqrt x+\lambda_jB_P\log x+O_j(1).
\]
The child subtraction is `O(x^{-1/2})` uniformly for `1<=y<=67`.

For any fixed outer cutoff atom `1<=c<2000`,
\[
\frac{K_R^{(j)}(c)}{K_S(c)}
=
\frac{a_j}{5}
+rac{\lambda_j\sqrt c\log x}{5\sqrt x}
+O_j(x^{-1/2}),
\]
while
\[
\frac{R_{sig}^{(j)}}{S_{sig}}
=
\frac{a_j}{5}
+rac{\lambda_j\vartheta_P\log x}{5\sqrt x}
+O_j(x^{-1/2}).
\]
Therefore
\[
\boxed{
\frac{R_{sig}^{(j)}}{S_{sig}}
-
\frac{K_R^{(j)}(c)}{K_S(c)}
=
\frac{(-\lambda_j)(\sqrt c-\vartheta_P)\log x}{5\sqrt x}
+O_j(x^{-1/2}).
}
\]
The leading coefficient is strictly positive because `lambda_j<0` and `sqrt(c)>=1>vartheta_P`.

The row range, child range, and cutoff set are finite/compact. Hence there exists one finite `X_*` such that every cutoff determinant of `L-91411` is positive whenever `py>=X_*`.

The remaining directed task is therefore compact: extract explicit remainders and check only `67<=p<X_*/y`.
