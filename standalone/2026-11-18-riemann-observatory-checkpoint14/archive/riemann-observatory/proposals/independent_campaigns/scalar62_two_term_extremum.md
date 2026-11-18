# Complete coalescence maximizes the two-term scalar taper in every degree

Let \(Q(z)=\prod_{j=1}^{m}(1-q_jz)\) with arbitrary unit factors, and use the reciprocal taper with \(M=2\) and power \(m\). Put \(a=2^{-m}\) and \(B=\binom{2m}{m}\). The squared coefficient norm \(E\) of the residual satisfies
\[
 E\le B-1+a^2m^2B-2am\binom{2m}{m-1},
\]
with equality precisely when all factors coincide. The proof below supplies the degrees \(m\ge5\). The degrees \(m=1,2\) are in [the scalar window report](unit_circle_scalar_window_round3.md), the cubic case is in [the coalescence report](scalar_window_coalescence_maximum_round3.md), and the quartic case is [THM-E-W311](../../theorems/semantic_finite_cases_round3.jsonl).

## Expansion

Let \(e_k\) be the elementary symmetric functions, \(b_k=\binom mk\), and \(e_0=b_0=1\). Since \(A=1+ae_1z\),
\[
 E=\sum_{k=0}^m|e_k|^2-1+a^2|e_1|^2\sum_{k=0}^m|e_k|^2
        -2a\sum_{k=1}^m\Re(e_1e_{k-1}\overline{e_k}).
\]
The displayed maximum is the value at all \(q_j=1\), by Vandermonde's identity. Set
\[
 D_k=b_k^2-|e_k|^2,\quad D=\sum_{k=0}^mD_k,\quad
 C_k=mb_{k-1}b_k-\Re(e_1e_{k-1}\overline{e_k}),\quad C=\sum_{k=1}^m C_k.
\]
The term with \(a^2\) is individually maximized at coalescence since \(|e_k|\le b_k\). Therefore \(E_{\rm coal}-E\ge D-2a C\).

## Comparing cross terms with same-size subset differences

Write \(q_S=\prod_{j\in S}q_j\) and \(\rho(u)=1-\Re u\) for unit \(u\). Let \(d=\mathbb E_{I\ne J}\rho(q_I\overline q_J)\) for a uniform ordered pair, so \(d\) measures the mean pair difference. For independent uniform \(k\)-subsets \(U,T\), one has \(\mathbb E\rho(q_U\overline q_T)=D_k/b_k^2\).

Choose independent uniform \(I,S,T\), with \(I\) a single index and \(S,T\) of sizes \(k-1,k\). Then \(C_k/(mb_{k-1}b_k)=\mathbb E\rho(q_I q_S \overline q_T)\). When \(I\notin S\), the set \(S\cup\{I\}\) is uniform of size \(k\). When \(I\in S\), choose \(J\) uniformly from the complement of \(S\). The set \(U=S\cup\{J\}\) is again uniform of size \(k\), independently of \(T\), and \((I,J)\) is uniform over distinct ordered pairs by permutation symmetry. Use \(\rho(uv)\le 2\rho(u)+2\rho(v)\), which follows from \(\rho(u)=|1-u|^2/2\). The second case is bounded in expectation by \(2D_k/b_k^2+2d\). It has probability \(p_k=(k-1)/m\), giving
\[
 C_k\le mb_{k-1}b_k\big[(1+p_k)D_k/b_k^2+2p_kd\big]. \tag{1}
\]

For \(1\le k<m\), one also has
\[
 d\le\left(1+\frac1{\max(k,m-k)}\right)D_k/b_k^2. \tag{2}
\]
To see this, start with a uniform \((k-1)\)-subset \(H\) and extend it by two distinct indices \(I,J\) sampled uniformly from its complement of size \(L=m-k+1\). The product difference has expectation \(d\), since the factors of \(q_H\) cancel. Sampling the indices with replacement instead multiplies this expectation by \((L-1)/L\). The resulting expectation is \(\mathbb E\operatorname{Var}(q_U\mid H)\), where \(U\) is a uniform extension of \(H\) and the complex variance means \(\mathbb E|X-\mathbb EX|^2\). Total variance bounds this quantity above by \(\operatorname{Var}(q_U)=D_k/b_k^2\). This gives the factor \(1+1/(m-k)\). Complementing the \(k\)-subsets gives the factor \(1+1/k\), since \(e_{m-k}=e_m\overline{e_k}\) and hence \(D_{m-k}=D_k\).

## Summation

The complement identity gives \(C_{m+1-k}=C_k\). Sum (1) over \(1\le k\le (m+1)/2\) with weights \(2\) for reflected pairs and \(1\) for a central singleton. Here \(b_{k-1}/b_k=k/(m-k+1)\le1\) and \(p_k\le1/2\). The \(D_k\) terms total at most \(3mD\). The \(d\) terms total at most \(mBd\), by \(2p_k\le1\), reflection of the binomial products, and \(\sum_{k=1}^m b_{k-1}b_k=\binom{2m}{m-1}\le B\).

For \(m\ge6\), summing (2) over interior \(k\) gives \(d\le (3/2)D/(B-2)\). Since \(B\ge8\), it follows that \(mBd\le2mD\), hence \(C\le5mD\). For \(m\ge6\), \(10m<2^m\) by its value at \(6\) and induction. This yields \(E_{\rm coal}-E\ge(1-10m/2^m)D\).

For \(m=5\), the coefficients in the weighted form of (1) are \(2,6,7\) on \(D_1,D_2,D_3\). The coefficients on \(d\) sum to \(600\). Equation (2) yields \(d\le(4/3)D/250\). Thus \(C\le(51/5)D<16D\), and the energy gap is again bounded below by a positive multiple of \(D\).

In either case, equality implies \(D_1=0\), hence \(|q_1+\cdots+q_m|=m\) and all factors coincide. A common rotation preserves the energy.

## Fixed window lengths at sufficiently high degree

For arbitrary \(M\ge2\), write \(h_j(q)=[z^j]Q^{-1}\), \(w_j=(1-j/M)^m\), and
\[
 c_j=w_j\binom{m+j-1}{j}\quad(0\le j<M),\qquad
 H=\sum_{j=0}^{M-1}c_j,\qquad L=m+M-1.
\]
For \(m\ge2\) a sufficient condition for the same strict coalescence maximum is
\[
 4L^2(H^2-1)<1. \tag{3}
\]

Indeed the \(n\)-th coefficient of \(QA\) is \(\sum_{j=0}^{M-1}(-1)^{n-j} w_j e_{n-j}h_j\), using \(e_\ell=0\) outside \(0\le\ell\le m\). The squared contribution from \(j=0\) over \(n\ge1\) has deficit \(D\) as above. Every other diagonal contribution has nonnegative deficit, as does a cross term with \(j+k\) even. For a cross term with \(j+k\) odd, normalize the two polynomials \(e_{n-j}h_j\) and \(e_{n-k}h_k\) by their values at coalescence. Each normalization is an average of monomials represented by an elementary subset and a weak composition sampled independently and uniformly. When both terms are present, independently choose these monomials and order the \(n\) factors in each by a uniform random permutation. Write the two ordered sequences of indices as \((I_\ell)\) and \((J_\ell)\). At any coordinate, conditional on the indices differing, the pair \((I_\ell,J_\ell)\) is uniform by simultaneous relabeling symmetry. The mean of \(\rho(q_{I_\ell}\overline q_{J_\ell})\) is at most \(d\). For unit \(u_\ell\), telescoping the product and then using Cauchy–Schwarz gives \(\rho(\prod_{\ell=1}^n u_\ell)\le n\sum_{\ell=1}^n\rho(u_\ell)\). It follows that the normalized cross-term deficit is at most \(n^2d\).

For each ordered pair \(j,k\), use \(n\le L\) and \(\sum_n b_{n-j}b_{n-k}\le B\) by Cauchy–Schwarz, with \(b_\ell=0\) outside \(0\le\ell\le m\). Its total adverse deficit is bounded by \(L^2dBc_jc_k\). Summing over all ordered pairs with \(j+k\) odd gives a bound of \(L^2dB(H^2-1)\), using \(c_0=1\) and \(c_j\ge0\). Equation (2) gives \(d\le2D/(B-2)\). As \(B\ge6\), we have \(dB\le4D\). The energy gap is therefore at least \(D[1-4L^2(H^2-1)]\), which is strictly positive when (3) holds and the factors do not all coincide.

For every fixed integer \(M\ge2\), the sum \(H-1\) is bounded by \(O_M(m^{M-1}(1-1/M)^m)\). Hence (3) eventually holds as \(m\to\infty\). The maximum value in this region is the squared coefficient norm computed at \(q_j=1\).

## Exact local stability check

For \(m\ge2\), set \(q_i=e^{itx_i}\) with real \(x_i\) and \(\sum_i x_i=0\). For \(k+j=n\), let
\[
 u_{k,j}=(-1)^k\binom mk\binom{j+m-1}{j}(M-j)^m,\qquad
 v_{k,j}=k(m-k)(m+1)+j(j+m)(m-1).
\]
Use \(0\le k\le m\) and \(0\le j<M\) in both sums below. Then the exact quadratic coefficient of the energy gap is
\[
 E_{\rm coal}-E(t)=
 \frac{t^2\sum_i x_i^2}{M^{2m}m(m^2-1)}
 \sum_{n=1}^{m+M-1}
 \left(\sum_{k+j=n}u_{k,j}\right)
 \left(\sum_{k+j=n}u_{k,j}v_{k,j}\right)+O(t^4).
\]
Indeed the first moments of the dot products of \(x\) with a uniform \(k\)-subset and a uniform weak \(j\)-composition vanish. The subset moment is \(k(m-k)\sum_i x_i^2/[m(m-1)]\) by its single and double inclusion probabilities. For the composition \(\alpha\), the generating function \((1-z)^{-m}\) and the geometric series for one or two marked indices give
\(\mathbb E\alpha_1=j/m\),
\(\mathbb E\alpha_1(\alpha_1-1)=2j(j-1)/[m(m+1)]\), and
\(\mathbb E\alpha_1\alpha_2=j(j-1)/[m(m+1)]\).
Thus its dot-product moment is \(j(j+m)\sum_i x_i^2/[m(m+1)]\). Independence adds the moments in the product \(e_k h_j\). Taking coefficient squares gives the formula, whose odd powers vanish by conjugation symmetry.

The integer sum in this formula is strictly positive on the 700 parameter pairs listed in [the exact result](../../experiments/results/scalar62_local_curvature.json), which includes \(m\) up to \(128\) and \(M\) up to \(256\). The integer calculation in [the script](../../experiments/code/scalar62_local_curvature.py) establishes local stability for those pairs only. A negative value at any pair would disprove the global conjecture by a perturbation in any nonzero mean-zero direction. Strictly positive curvature does not exclude a higher maximum at a separated configuration.

## Remaining case

The two-term argument absorbs a cross term into same-size subset deficits despite the sign changes in the raw Laurent expansion. The larger-window argument estimates each adverse cross term separately and therefore requires the higher weights to be small. It leaves the regime outside (3) with \(M\ge3\) unresolved in general degree. Extending the comparison into that regime would require sharper estimates or cancellations among the cross terms.
