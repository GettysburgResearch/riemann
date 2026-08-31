# Exact four-jet factorization at the safe-axis endpoint

Status: EXACT ALGEBRA plus high-precision reconnaissance. The transcendental
signs are not yet interval-certified, so this note does not claim a local
four-node positivity theorem.

Put \(a=1/2\), \(f_r=F^{(r)}(a)\), and
\(H(x,y)=(F(x)+F(y))/(x+y)\). In the signed unnormalized derivative basis,
\[
 G_{ij}=\left.(-1)^{i+j}\partial_x^i\partial_y^jH(x,y)\right|_{x=y=a},
 \qquad C_{ij}=(i+j)!,\qquad0\le i,j\le3.                 \tag{J4.1}
\]
Leibniz gives the exact formula
\[
 G_{ij}=\sum_{r=0}^i {i\choose r}(-1)^r f_r(i-r+j)!
       +\sum_{r=0}^j {j\choose r}(-1)^r f_r(i+j-r)!.       \tag{J4.2}
\]
This is the confluent limit of the ordinary \((H,C)\) packet. Only
\(f_0,\ldots,f_3\) occur at the point.

The leading determinants factor as
\[
\begin{aligned}
 D_1={}&2f_0,\\
 D_2={}&(2f_0-f_1)(2f_0+f_1),\\
 D_3={}&2(4f_0-2f_1-f_2)
 (4f_0^2+2f_0f_1+f_0f_2-2f_1^2),\\
 D_4={}&A_-A_+,
\end{aligned}                                             \tag{J4.3}
\]
where
\[
\begin{aligned}
 A_-={}&48f_0^2-48f_0f_1-24f_0f_2-4f_0f_3
       +12f_1^2+12f_1f_2+2f_1f_3-3f_2^2,\\
 A_+={}&48f_0^2+48f_0f_1+24f_0f_2+4f_0f_3
       -36f_1^2-12f_1f_2+2f_1f_3-3f_2^2.
\end{aligned}                                             \tag{J4.4}
\]
The last factorization is the odd/even reflection split of the persymmetric
four-jet matrix. It is exact and does not use a sampled determinant.

Equivalently, in the orthonormal repeated-node Malmquist basis, put
\(d=2f_0\),
\[
 b_1=2af_1,\quad b_2=2af_1+2a^2f_2,\quad
 b_3=2af_1+4a^2f_2+\frac43a^3f_3.
\]
Then the matrix is symmetric Toeplitz with diagonal \(d\) and successive
off-diagonals \(b_1,b_2,b_3\). Its determinant factors as
\[
 [(d-b_3)(d-b_1)-(b_1-b_2)^2]\,
 [(d+b_3)(d+b_1)-(b_1+b_2)^2].                            \tag{J4.5}
\]

For reproducible numerical reconnaissance, use the regular expansion
\[
\begin{aligned}
 \log\xi(1+z)={}&\mathrm{const}+\log(1+z)
 +\log[z\zeta(1+z)]-\tfrac z2\log\pi\\
 &+\log\Gamma(\tfrac12+\tfrac z2),\\
 z\zeta(1+z)={}&1+\sum_{n\ge0}\frac{(-1)^n\gamma_n}{n!}z^{n+1}.
\end{aligned}                                             \tag{J4.6}
\]
This avoids nested differentiation across the pole at one. At 100 decimal
digits it gives
\[
\begin{array}{c|r}
0& .023095708966121033814310247906495291621932127152051\\
1& .046154317295804602757107990379077303530267962324145\\
2&-.00022231646290421184552533647782915694792837849797304\\
3&-.00044176332757013710996062784218360906787698957764460\\
4& .000017162240538302585659226253915178831737759583956662\\
5& .000033772370032651951392805876857134852110316717076949\\
6&-.0000032934176277874359200371386647199569286002545487343\\
7&-.0000063950952791918340238232397689185950088592240174724.
\end{array}
\]
The last four values are recorded for a future interval-in-\(a\) proof; they
do not enter (J4.1)--(J4.5).

Substitution gives the orthonormal generalized eigenvalues
\[
 1.0365420536068911\,10^{-11},\quad
 1.6828257842189672\,10^{-7},\quad
 3.7014494667541057\,10^{-4},\quad
 1.8439535848934902\,10^{-1}.
\]
The odd and even factors in (J4.5) are approximately
\(3.83670803159143\,10^{-15}\) and
\(3.10305263756176\,10^{-8}\). The limiting value agrees with the independent
\(2^{-32}\) near-confluent scout. The separated packet
\((1/2,9/16,3/4,1)\) has smallest generalized eigenvalue about
\(9.1195730967\,10^{-11}\), confirming that confluence at the endpoint is the
harder registered chamber.

These numerical signs are stable under independent 100/200-digit evaluation
but are not outward-rounded analytic intervals. Because the smallest exact
factor is only about \(3.8\,10^{-15}\), ordinary double precision is
inadequate. A local theorem requires rigorous enclosures for the Stieltjes
constants and the higher derivatives on a declared interval. Continuity alone
would give a neighborhood after the endpoint signs were rigorously certified;
this note does not use that circularly. No four-node continuum positivity or
RH claim follows.

