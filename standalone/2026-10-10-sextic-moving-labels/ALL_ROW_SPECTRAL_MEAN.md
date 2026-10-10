# The canonical Gauss spectral mean at every nonzero arithmetic row

Status: proposed source-conditional analytic theorem. This extends the canonical spectral mean of PR #922 from squarefree primary rows to every nonzero Eisenstein element row, with the same strict threshold Re(u)>5/8 and the same auxiliary-divisor loss. It uses the imported completed mean square and the established refined all-row sextic upper sieve. It does not use an angular reciprocal bound or any zero-free conclusion.

Scope: a fixed finite family of ray characters, every nonzero element row including units, fixed bad-prime factors and sixth-power copies, a moving squarefree auxiliary d, and a strict interior vertical strip. The theorem concerns the canonical Gauss Dirichlet family. It does not identify that family with an inverse-Mobius moment or extend the squarefree-row reflected identity for the function Y in PR #922 to arbitrary rows.

Exact sources:

* PR #922, commit `f71a9bc6ac3ce59a3c19d7e842a3fa082ecfbe32`, `standalone/2026-10-10-signed-covariance-descent/SPECTRAL_ROW_MEAN.md`: definitions, cube-completion normalization, and squarefree-row Mellin argument.
* PR #913, commit `6498d6cc2eded03159c7332b25fd224ad07f89c1`, `standalone/2026-10-10-sextic-moment-descent/REFINED_ALL_ROW_SIEVE.md`, Theorem 3.4: arbitrary nonzero element rows, squarefree columns, and literal nonunit zeros.
* OpenAI/math commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, October 5 `build/paper2.tex`, equations `eq:T`, `eq:completed-twist`, `eq:R` and Proposition `prop:R`. The resident copy is `standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex` at PR #923 commit `1a1152008706f7e24fa1efe4990588f8f99c5d8d`. The proposition explicitly sums every nonzero element row. Its proof writes k=u_0 s v^2 without assuming (s,v)=1 and retains the literal character zeros. This input is inherited, not independently established here.

## 1. Exact family and statement

Work over K=Q(sqrt(-3)) with the inherited primary generators, fixed bad set S, and sextic symbol chi_n(k) extended by zero at nonunits. Let xi be a character of the prescribed fixed ray group. Put

\[
 a_\xi(n)=\overline{\alpha(n)}\gamma_2(n)\xi(n),
 \qquad \alpha(n)=n/|n|.
\tag{1.1}
\]

For any nonzero element k and any squarefree primary d outside S, define initially for Re(u)>1

\[
 G_{k,d}(u)=\sum_{(n,S)=1}^{*}
 \frac{a_\xi(n)\chi_n(k)\chi_n(d)^4}{(Nn)^u}.
\tag{1.2}
\]

Only n is squarefree in this definition. There is no squarefree restriction on k, and no assumption (k,d)=1. The symbol itself retains the exact n-coprimality masks at k and d.

Write

\[
 c_k(b)=\overline{\alpha(b)}^{\,3}\xi(b)^3\chi_b(k)^3.
\]

The cube Euler product and exact completion are

\[
 \mathcal L_{k,d}(z)=
 \prod_{p\nmid Sd}\left(1-c_k(p)(Np)^{-z}\right)^{-1},
 \qquad
 \mathcal T_{k,d}(u)=G_{k,d}(u)\mathcal L_{k,d}(3u-\tfrac12).
\tag{1.3}
\]

If p divides k, c_k(p)=0, so its displayed factor is one. Equivalently that prime can be omitted. At a prime of d, chi_b(d)^12 is the nonunit-zero mask, which is why the product omits d. No imprimitive character has been replaced by its primitive character without its zeros.

### Theorem 1.1

The functions G and T in (1.2)--(1.3) continue holomorphically to Re(u)>1/2. For every closed real strip

\[
 \frac58<a_0\le a=\Re u\le a_1<1
\tag{1.4}
\]

and every epsilon>0, there exists a finite M such that, uniformly for H>=2, F=Nd>=1 and every subset K_H of the nonzero element rows satisfying 0<Nk<=cH for a fixed c,

\[
\boxed{
 \sum_{k\in K_H}|G_{k,d}(a+i t)|^2
 \ll_{a_0,a_1,\epsilon,S,\xi,c}
 H^{1+\epsilon}F^{1-a+\epsilon}(2+|t|)^M.
}
\tag{1.5}
\]

The same estimate holds with T in place of G. It is uniform over the chosen fixed finite ray family and over the subset K_H. Thus it covers sharp row balls, annuli, prescribed residue subsets, and sixth-power rows without a separate exceptional contribution. No endpoint assertion at a=5/8 is made.

The source-conditional status concerns the imported analytic completed bound. The extension from squarefree rows in PR #922 to all rows is the new deduction proved below.

## 2. The two all-row smooth-block estimates

Fix a compact interval I contained in (0,infinity), and W in C_c^infinity(I). The literal completed block is

\[
\begin{split}
 T_W(X;k,d)=X^{-1/2}
 \sum_{(n,S)=1}^{*}
 \sum_{\substack{b\equiv1\ (3)\\(b,Sd)=1}}
 &a_\xi(n)\chi_n(k)\chi_n(d)^4\,c_k(b)\sqrt{Nb}\\
 &\qquad\times W\!\left(\frac{Nn(Nb)^3}{X}\right).
\end{split}
\tag{2.1}
\]

There is no condition (n,b)=1. The b-row character is retained even at primes dividing k. Equation (2.1) is exactly the source T with V_*(y)=sqrt(y)W(y) and auxiliary f=d.

Proposition R supplies, for X>=1,

\[
 \sum_{k\in K_H}|T_W(X;k,d)|^2
 \ll (2HFX)^\epsilon\|W\|_{C^J(I)}^2
 \left(H+\frac{H^2F}{X}\right).
\tag{2.2}
\]

Indeed apply that all-row proposition with reference parameter max(2cH,F,X,2), increasing a fixed constant if necessary, and C_0=1. Restricting its positive row energy to K_H preserves its upper bound. This application does not rely on a squarefree-row extension inferred from a character relabeling.

The alternative estimate is

\[
\boxed{
 \sum_{k\in K_H}|T_W(X;k,d)|^2
 \ll (2HX)^\epsilon\|W\|_\infty^2
 \left(H+H^{1/6}X+(HX)^{2/3}\right).
}
\tag{2.3}
\]

To prove it, write L_b=X/(Nb)^3 and define

\[
 S_W(L_b;k,d)=L_b^{-1/2}
 \sum_{(n,S)=1}^{*}a_\xi(n)\chi_n(k)\chi_n(d)^4 W(Nn/L_b).
\tag{2.4}
\]

If the support upper endpoint is C, nonempty terms have L_b>=1/C and Nb<=(CX)^(1/3). The squared mass of the column coefficients in (2.4) is O_I(||W||_infinity^2), by ideal counting and |a_xi(n)chi_n(d)^4|<=1. This remains true for the bounded nonempty scales 1/C<=L_b<1, by replacing the sieve cutoff by a fixed constant. The d mask is a fixed contraction in these column coefficients.

Theorem 3.4 of the refined all-row sieve therefore gives

\[
 \sum_{k\in K_H}|S_W(L_b;k,d)|^2
 \ll (2HX)^\epsilon\|W\|_\infty^2
 \left(H+H^{1/6}L_b+(HL_b)^{2/3}\right).
\tag{2.5}
\]

The exact block (2.1) equals the sum of c_k(b)S_W(L_b;k,d)/(Nb). Apply weighted Cauchy using |c_k(b)|<=1 and

\[
 \sum_{Nb\le(CX)^{1/3}}\frac1{Nb}\ll_I\log(2X).
\]

Summing (2.5) with weight 1/Nb bounds its three terms respectively by

\[
 H\log(2X),\qquad
 H^{1/6}X\sum_b(Nb)^{-4},\qquad
 (HX)^{2/3}\sum_b(Nb)^{-3}.
\]

The latter two ideal sums converge. Absorb the logarithms into the requested small X-power. This proves (2.3), including all sixth-power copies. Its H^(1/6)X term is deliberately retained.

## 3. Holomorphic reconstruction on Re(u)>1/2

Choose a fixed smooth dyadic partition of unity on [1,infinity), with a separately fixed initial cutoff if required. Each test is supported in a fixed compact interval inside (0,infinity). For X=2^j put W_u(y)=y^(-u)W_0(y), with the analogous initial cutoff. On every bounded real u-strip,

\[
 \|W_u\|_{C^J}\ll(2+|\Im u|)^J.
\tag{3.1}
\]

For Re(u)>1, absolute convergence gives the identity

\[
 \mathcal T_{k,d}(u)
 =\sum_{X=2^j,\ j\ge0}X^{1/2-u}T_{W_u}(X;k,d).
\tag{3.2}
\]

Term by term, this multiplies sqrt(Nb) by (Nn(Nb)^3)^(-u), so the cube exponent is exactly 3u-1/2, as in (1.3).

For fixed H,F, (2.2) and Minkowski make (3.2) normally convergent in the finite-dimensional row Hilbert space on compact subsets of Re(u)>1/2. Choose the preliminary loss in (2.2) smaller than twice the distance of the compact set from 1/2. Its dyadic tail is then a convergent geometric series. Each smooth block is a finite entire function of u, so the limit is holomorphic and agrees with the original completed series on Re(u)>1.

For Re(u)>1/2, both the product L_{k,d}(3u-1/2) and its reciprocal converge absolutely, uniformly in k,d and the vertical variable on strict interior strips. Their factors are bounded by the ordinary products formed with (Np)^(-1-delta), and the product is nonzero. Multiplication by the reciprocal gives the holomorphic continuation of G. No zero-free theorem is used here; the cube argument remains inside an absolute Euler half-plane.

## 4. The sixth-power cost does not change the spectral threshold

Ignore preliminary arbitrarily small powers for this calculation; they will be absorbed using the strict strip margins. Combining (2.2) and (2.3), set

\[
 \mathcal B(H,F,X)=
 \min\left(H+H^{1/6}X+(HX)^{2/3},\ H+H^2F/X\right).
\]

The elementary minimum inequality gives

\[
 \mathcal B(H,F,X)
 \le H+\min(H^{1/6}X,H^2F/X)
       +\min((HX)^{2/3},H^2F/X).
\tag{4.1}
\]

After taking square roots and applying Minkowski in (3.2), the base H term contributes O(H^(1/2)), since sum_X X^(1/2-a) converges when a>1/2.

For the first minimum, the crossover is

\[
 X_1=H^{11/12}F^{1/2}.
\tag{4.2}
\]

Below X_1 the dyadic norm summand is H^(1/12)X^(1-a); above it the summand is H F^(1/2)X^(-a). Since 1/2<a<1, both geometric sums are bounded by

\[
\boxed{H^{1-11a/12}F^{(1-a)/2}.}
\tag{4.3}
\]

This is at most H^(1/2)F^((1-a)/2) as soon as a>=6/11. In particular it is strictly below the required row exponent throughout a>5/8. At a=5/8, the H exponent in (4.3) is 41/96, already below 1/2.

The second minimum has the same crossover as in PR #922:

\[
 X_2=H^{4/5}F^{3/5}.
\tag{4.4}
\]

Below X_2 its dyadic summand is H^(1/3)X^(5/6-a), and above it the summand is H F^(1/2)X^(-a). For a<5/6, the two geometric sums give

\[
 H^{1-4a/5}F^{1/2-3a/5}.
\tag{4.5}
\]

For a>5/6 the lower sum is O(H^(1/3)); at a=5/6 there is only a logarithm. Uniformly on strips crossing 5/6, a sufficient bound is the sum of (4.5) and H^(1/3), multiplied by log(2HF). This avoids a constant singular at that interior value.

For a>5/8,

\[
 1-\frac45a<\frac12,
 \qquad
 \frac12-\frac35a\le\frac{1-a}{2}.
\tag{4.6}
\]

Hence (4.5), the H^(1/3) term and the base term all obey the required H^(1/2)F^((1-a)/2) envelope. The first minimum imposes only a>6/11; the second still imposes a>5/8. Since 6/11<5/8, restoring sixth-power rows causes no loss in the final spectral threshold.

Retain the small H,F,X powers from the block bounds throughout this calculation. Their values at X_1,X_2 are bounded by arbitrarily small powers of H,F, and their tails are summable after shrinking the strict margins in (1.4). The logarithms and smooth norms are handled in the same way. We obtain

\[
 \|\mathcal T_{k,d}(a+i t)\|_{\ell^2(K_H)}
 \ll H^{1/2+\epsilon}F^{(1-a)/2+\epsilon}(2+|t|)^M.
\]

Square and rename epsilon,M. The uniformly bounded reciprocal in Section 3 gives the same estimate for G. This proves Theorem 1.1.

## 5. Meaning and remaining boundary

This removes the squarefree-row restriction in the spectral input itself. The new estimate can be used whenever an exact arithmetic adapter produces this literal canonical family at all rows, with the same auxiliary d and cube mask.

It does not extend the actual all-cusp series identity Y_k(s,v) from PR #922 merely by replacing its row summation sign. That identity used the squarefree row's particular local reflection data. Arbitrary local row exponents must be treated in the exact identity before an all-row estimate for Y can be asserted.

Nor does a better spectral threshold alone improve the physical covariance envelope: PR #922, FULL_CUSP_DESCENT.md, Section 5 proves that limitation for its specified contour-and-Minkowski mechanism even if its threshold were lowered to 1/2. The present gain is full-row scope at the existing threshold, not a new zeta boundary, an inverse-Mobius moment, or the signed large-conductor cancellation needed for 17/24.
