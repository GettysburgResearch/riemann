# Oscillating overlap variables: a larger proved fourth-moment range

Status: a proposed rigorous deduction from classical squarefree character large sieves. This note proves an improved bound for specified overlap pieces of the actual inverse Möbius polynomial. It does not prove the full fourth moment, the full higher-moment hierarchy, or a new zero-free half-plane.

Source being continued: GettysburgResearch/riemann PR #913, head 6498d6cc2eded03159c7332b25fd224ad07f89c1, especially GENERAL_MOMENT_ATTACK.md and REFINED_ALL_ROW_SIEVE.md. No existing source file is edited by this working note.

The main gain is already present at the fourth moment. When \(H=D^{1+\theta}\), \(0<\theta\le1/10\), the exact part of \(A_u(D)^2\) with
\[
N\gcd(n_1,n_2)\ge D^{(5-\theta)/7}
\]
has squared row norm \(\ll D^{2+\epsilon}H\). The previous classical cutoff in PR #913 was \(D^{(3-\theta)/4}\). The decrease in the cutoff exponent is \((1-3\theta)/28>0\).

The improvement comes from retaining the cubic phase of the common gcd. It does not require cancellation in the Möbius signs of the residual factors.

## 1. Data, zero extensions, and classical inputs

Work over \(K=\mathbb Q(\sqrt{-3})\), with fixed prime exclusions \(S\) containing the primes above 2 and 3 and the ramification of the fixed finite-order character \(\nu\). Ideal indices use the chosen primary generators of the source. The sextic residue symbols are
\[
\chi_n(u)=(u/n)_6,
\]
extended by zero when \((n,u)>1\). For each fixed smooth \(W_i\), supported in \([\alpha_i,\beta_i]\subset(0,\infty)\), put
\[
A_u(D_i;W_i)=
\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W_i(Nn/D_i).
\tag{1.1}
\]
Every row sum includes every nonzero Eisenstein element \(u\) of norm at most \(H\). Throughout, \(D_i,H\ge1\), the number of factors is fixed, and constants may depend on \(K,S,\nu,k\), the tests, and the displayed positive loss. Write \(D_*=2+\max_iD_i\).

The following squarefree-row inputs are classical. If \(z_n\) is supported on squarefree ideals prime to \(S\), \(Nn\le L\), and is independent of the varying squarefree row \(a\), then for \(j=1,2,4,5\),
\[
\sum_{\substack{Na\le M\\a\ {\rm squarefree}\\(a,S)=1}}
\left|\sum_nz_n\chi_n(a)^j\right|^2
\ll_\epsilon(ML)^\epsilon
\left[M+L+(ML)^{2/3}\right]\sum_n|z_n|^2.
\tag{1.2}
\]
For \(j=3\), the quadratic sieve gives the stronger factor
\[
\sum_{\substack{Na\le M\\a\ {\rm squarefree}\\(a,S)=1}}
\left|\sum_nz_n\chi_n(a)^3\right|^2
\ll_\epsilon(ML)^\epsilon(M+L)\sum_n|z_n|^2.
\tag{1.3}
\]
Empty row ranges are omitted. Bounded scales can be absorbed into constants.

For orders 3 and 6, the primary input is Blomer–Goldmakher–Louvel, *L-functions with n-th order twists*, Theorem 1.3, [arXiv:1112.1650v1](https://arxiv.org/html/1112.1650v1). Order 3 applies to \(j=2,4\); order 6 to \(j=1,5\), with conjugation if needed. For the quadratic input, the exact specialization is recorded in the October 5 imported manuscript, Lemma with label lem:quadratic, citing Goldmakher–Louvel. Fixed reciprocity and ray-class corrections require only finitely many partitions. At each good squarefree column prime, these nontrivial character powers retain that prime in the conductor and retain the local zero.

The refined order-six all-row theorem proved in PR #913 is
\[
\sum_{0<Nu\le H}\left|\sum_nz_n\chi_n(u)^j\right|^2
\ll_\epsilon(HL)^\epsilon
\left[H+H^{1/6}L+(HL)^{2/3}\right]\sum_n|z_n|^2,
\qquad j=1,5.
\tag{1.4}
\]
Its exact dependency is REFINED_ALL_ROW_SIEVE.md, Theorem 3.4. It uses only the classical inputs described there. This note proves the corresponding order-three and order-two all-row bounds needed for the overlap argument.

An arbitrary fixed column mask can always be absorbed into \(z_n\) in (1.2)–(1.4). This is a uniform assertion about arbitrary coefficients, so the implied constants do not acquire a dependence on the masked ideal.

## 2. An all-row cubic sieve with the cube-copy scale

### Theorem 2.1

For \(j=2,4\), and the squarefree column coefficients above,
\[
\boxed{
\sum_{0<Nu\le H}
\left|\sum_nz_n\chi_n(u)^j\right|^2
\ll_\epsilon(HL)^\epsilon
\left[H+H^{1/3}L+(HL)^{2/3}\right]\sum_n|z_n|^2.
}
\tag{2.1}
\]
The characters have their literal nonunit zeros.

### Proof

It suffices to prove the case \(j=2\), since the other is its conjugate. Choose generators multiplicatively for all ideals, including the fixed bad primes. The field has class number one. Every nonzero element has the unique representation
\[
u=\varepsilon v^3 a b^2,
\tag{2.2}
\]
where \(\varepsilon\) is one of the six units, \(v\) is arbitrary, and \(a,b\) are squarefree and pairwise coprime. The ideal \(v\) is allowed to share primes with \(a\) or \(b\). This follows by writing each prime valuation uniquely as \(3e+r\), \(r=0,1,2\).

At every column \(n\), including columns not coprime to \(u\), the exact identity is
\[
\chi_n(u)^2
=\chi_n(\varepsilon)^2
{\bf1}_{(n,v)=1}\chi_n(a)^2\chi_n(b)^4.
\tag{2.3}
\]
In particular, a cube factor is a coprimality mask, not an everywhere-one replacement.

First fix the squarefree bad-prime parts of \(a,b\). There are finitely many possibilities depending only on \(S\). Absorb their character factors into the column coefficients and divide them out of the squarefree row variables. Their norms change the row constraint by fixed factors only. Fix the unit as well. No decomposition or omission is needed for the bad-prime part of \(v\): the entire ideal \(v\) will be frozen, and its full mask in (2.3) is retained.

Put the remaining norms into dyads
\[
Nv\asymp V,\qquad Na\asymp A,\qquad Nb\asymp B,
\]
with \(V,A,B\ge1\). Write
\[
P=V^3AB^2,\qquad F=VAB,\qquad M=\max(A,B).
\tag{2.4}
\]
For a nonempty block, \(P\ll_S H\). The number of choices for \(v\) and the smaller squarefree component is \(O_S(F/M)\), by the elementary ideal count \(\#\{Nn\le X\}\ll_K X\).

For every such frozen choice, use the larger squarefree component as the row of (1.2). The remaining fixed character factors and \({\bf1}_{(n,v)=1}\) form a coefficient multiplier of modulus at most one. The restriction that \(a\) and \(b\) are coprime may be dropped from the positive outer row sum; it is not removed from an inner signed expression. If \(a\) is the varying component, the power is 2; if \(b\), the power is 4. Both use the same cubic input. Therefore the contribution of this block is at most
\[
\ll_\epsilon(HL)^\epsilon
\left[F+\frac{FL}{M}
+ \frac{F L^{2/3}}{M^{1/3}}\right]\sum_n|z_n|^2.
\tag{2.5}
\]

All needed inequalities are literal monomial inequalities:
\[
F\le P,\qquad
\frac{(F/M)^3}{P}
=\frac{A^2B}{M^3}\le1,\qquad
\frac{(F/M^{1/3})^3}{P^2}
=\frac{A}{M V^3B}\le1.
\tag{2.6}
\]
Consequently
\[
F\ll H,\qquad F/M\ll H^{1/3},\qquad
F/M^{1/3}\ll H^{2/3}.
\]
Inserting these into (2.5) gives the bracket in (2.1). There are \(O_S((1+\log H)^3)\) nonempty blocks and finitely many unit and bad-prime labels. Start with a smaller positive loss in (1.2), and absorb their sum into \((HL)^\epsilon\). This proves (2.1). \(\square\)

### Remark on necessity of the cube scale

The \(H^{1/3}L\) term is consistent with the literal rows \(u=v^3\). On these rows a cubic character contributes \({\bf1}_{(n,v)=1}\). Thus a proof cannot discard the replication from cubes. The theorem makes no claim to improve the squarefree-row cross term \((HL)^{2/3}\).

## 3. The other orders of an overlap character

If a prime occurs in exactly \(m\) factors of an ordinary polynomial product, its row character is \(\chi_c(u)^m\). Its nontrivial order is
\[
r=r(m)=\frac6{\gcd(m,6)}.
\tag{3.1}
\]

For \(m\equiv3\pmod6\), the all-row quadratic bound is
\[
\sum_{0<Nu\le H}\left|\sum_nz_n\chi_n(u)^m\right|^2
\ll_\epsilon(HL)^\epsilon[H+H^{1/2}L]\sum_n|z_n|^2.
\tag{3.2}
\]
Indeed write \(u=\varepsilon v^2a\), with arbitrary \(v\) and squarefree \(a\), allowing common primes. The exact character identity retains \({\bf1}_{(n,v)=1}\). Freeze \(v\), the unit, and the finite bad-prime part of \(a\), then apply (1.3) with row length \(O_S(H/Nv^2)\). The row-length terms sum to
\[
H\sum_v(Nv)^{-2}\ll H,
\]
and the column terms sum to
\[
L\#\{Nv\ll H^{1/2}\}\ll LH^{1/2}.
\]
The epsilon factors and bounded small scales are harmless. Every nonunit zero is present in the fixed mask or in the squarefree character.

For \(6\mid m\), the exact identity is
\[
\chi_n(u)^m={\bf1}_{(n,u)=1}.
\]
The universally valid elementary estimate is
\[
\sum_{0<Nu\le H}
\left|\sum_nz_n{\bf1}_{(n,u)=1}\right|^2
\ll HL\sum_n|z_n|^2.
\tag{3.3}
\]
It follows from Cauchy–Schwarz, the \(O(L)\) number of columns, and the \(O(H)\) number of element rows. No oscillatory order-one sieve is asserted.

It is convenient to collect (1.4), (2.1), (3.2), and (3.3) into
\[
K_r(H,L)=
\begin{cases}
H+H^{1/r}L+(HL)^{2/3},&r=3,6,\\
H+H^{1/2}L,&r=2,\\
HL,&r=1.
\end{cases}
\tag{3.4}
\]
In every case the all-row square norm is \(\ll(HL)^\epsilon K_r(H,L)\sum|z_n|^2\).

## 4. Master theorem for a designated incidence ideal

Expand \(\prod_{i=1}^k A_u(D_i;W_i)\). For each original squarefree tuple \((n_1,\ldots,n_k)\) and nonempty subset \(I\subseteq[k]\), let \(q_I\) be the product of primes occurring in precisely the factors indexed by \(I\). Thus
\[
n_i=\prod_{I\ni i}q_I
\]
is the unique incidence decomposition. Fix \(I\), put \(m=|I|\ge2\), and let \(F_{I,\ge C}(u)\) be the exact portion of this expanded polynomial with \(Nq_I\ge C\), where \(C\ge1\). Put
\[
\mathcal P=\prod_{i=1}^k D_i.
\]

### Theorem 4.1

For \(r=r(m)\in\{3,6\}\),
\[
\boxed{
\|F_{I,\ge C}\|_{\ell^2(0<Nu\le H)}^2
\ll_\epsilon(D_*H)^\epsilon\mathcal P^2
\left[
H C^{1-2m}
+H^{1/r}C^{2-2m}
+H^{2/3}C^{5/3-2m}
\right].
}
\tag{4.1}
\]
For \(r=2\),
\[
\boxed{
\|F_{I,\ge C}\|_2^2
\ll_\epsilon(D_*H)^\epsilon\mathcal P^2
\left[H C^{1-2m}+H^{1/2}C^{2-2m}\right].
}
\tag{4.2}
\]
For \(r=1\),
\[
\boxed{
\|F_{I,\ge C}\|_2^2
\ll_\epsilon(D_*H)^\epsilon H\mathcal P^2C^{2-2m}.
}
\tag{4.3}
\]

The same bounds hold if \(q_I\) is replaced by the ordinary gcd of the factors indexed by \(I\), with the corresponding exact decomposition and no restriction on which outside factors contain a prime.

### Proof, including exact eligibility and moving masks

Restrict to a dyad \(L\le Nq_I<2L\). Write \(c=q_I\) and
\[
n_i=ca_i\quad(i\in I),
\]
and freeze every \(a_i\), \(i\in I\), and every \(n_j\), \(j\notin I\).

Here are exact necessary and sufficient eligibility conditions. Each frozen ideal is squarefree and prime to \(S\). The varying ideal \(c\) is squarefree, prime to \(S\), and coprime to all the frozen ideals. Finally, every prime dividing all \(a_i\), \(i\in I\), must divide at least one frozen \(n_j\), \(j\notin I\). When \(I=[k]\), the last condition says \(\gcd(a_1,\ldots,a_k)=1\).

To verify sufficiency, a prime of \(c\) occurs precisely in the factors of \(I\), while the last condition excludes any additional exact-\(I\) prime in the residual tuple. Necessity follows from the definition of \(q_I\). Thus the representation is exact, with no multiple counting. These conditions do not depend on the row.

For the ordinary gcd of a subset, instead impose \(\gcd(a_i:i\in I)=1\) and require \(c\) to be coprime only to the \(a_i\). An outside factor may share a prime with \(c\). The proof below is unchanged, since all outside factors are frozen.

The support of the tests gives
\[
Na_i\le \beta_i D_i/L\quad(i\in I),\qquad
Nn_j\le\beta_jD_j\quad(j\notin I).
\]
Every nonempty dyad has \(D_i/L\ge1/\beta_i\) for \(i\in I\). Therefore the elementary ideal count, including these bounded scales below 1, gives
\[
\#\{\hbox{frozen tuples}\}
\ll_{k,\mathbf W}\mathcal P L^{-m}.
\tag{4.4}
\]
In particular, a claimed cutoff with \(C>\min_{i\in I}\beta_iD_i\) concerns an empty polynomial piece.

For one frozen tuple, its contribution is
\[
\eta(u)\sum_c z_c\,\chi_c(u)^m,
\tag{4.5}
\]
where the residual row multiplier \(\eta(u)\), including every residual character, has modulus bounded by a constant depending only on the fixed tests. The coefficient \(z_c\) is
\[
\mu_K(c)^m\nu(c)^m\,{\bf1}_{L\le Nc<2L}
\prod_{i\in I}W_i(Nc\,Na_i/D_i),
\tag{4.6}
\]
times the exact row-independent coprimality and eligibility masks just described. It is supported on squarefree columns \(Nc<2L\), and
\[
\sum_c|z_c|^2\ll_{k,\mathbf W}L.
\tag{4.7}
\]
The weights of the outside factors may be put in \(\eta\). The identity in (4.5) uses multiplicativity only between coprime factors inside each original \(n_i\). Consequently it is valid also at rows where one or several character factors vanish.

Apply the appropriate all-row bound in (3.4), then the contraction by \(\eta\), and then Minkowski over the frozen tuples. For \(r=3,6\), this gives
\[
\begin{split}
\|F_{I,L}\|_2
&\ll_\epsilon(D_*H)^\epsilon\mathcal P L^{-m}
\left(HL+H^{1/r}L^2+H^{2/3}L^{5/3}\right)^{1/2}\\
&\ll_\epsilon(D_*H)^\epsilon\mathcal P
\left[
\sqrt H\,L^{1/2-m}
+H^{1/(2r)}L^{1-m}
+H^{1/3}L^{5/6-m}
\right].
\end{split}
\tag{4.8}
\]
The analogous quadratic estimate omits the third term. The order-one estimate is
\[
\|F_{I,L}\|_2\ll\sqrt H\,\mathcal P L^{1-m}.
\tag{4.9}
\]
All displayed exponents of \(L\) are negative because \(m\ge2\). Summing the norms over \(L=2^\ell C\), \(\ell\ge0\), is therefore a convergent geometric sum, dominated by its first scale. Squaring proves (4.1)–(4.3), after adjusting the positive loss. \(\square\)

### Diagonal-scale criterion

For \(r=3,6\), a sufficient condition for
\(\|F_{I,\ge C}\|_2^2\ll(D_*H)^\epsilon H\mathcal P\) is
\[
C\ge
\max\left\{
1,\
\mathcal P^{1/(2m-1)},\
\left(\frac{\mathcal P}{H^{1-1/r}}\right)^{1/(2m-2)},\
\left(\frac{\mathcal P^3}{H}\right)^{1/(6m-5)}
\right\}.
\tag{4.10}
\]
For \(r=2\), omit the final term and replace \(1-1/r\) by \(1/2\). For \(r=1\), it suffices that
\[
C\ge\max\{1,\mathcal P^{1/(2m-2)}\}.
\tag{4.11}
\]
These inequalities describe a nonempty asymptotic range only when compatible with the support upper bound in the proof.

For \(D_i=D\), \(H=D^h\), the exponent in (4.10) is
\[
\gamma_{k,m,r}(h)=
\max\left\{
0,\
\frac{k}{2m-1},\
\frac{k-h(1-1/r)}{2m-2},\
\frac{3k-h}{6m-5}
\right\}.
\tag{4.12}
\]
The common-gcd specialization is \(m=k\).

## 5. The strict fourth-moment improvement

At \(k=m=2\), the character carried by the common gcd is cubic. Theorem 4.1 reads
\[
\boxed{
\|T_{\ge C}\|_2^2
\ll_\epsilon(DH)^\epsilon D^4
\left[
H C^{-3}+H^{1/3}C^{-2}+H^{2/3}C^{-7/3}
\right],
}
\tag{5.1}
\]
where \(T_{\ge C}\) is the exact part of \(A_u(D)^2\) with \(N\gcd(n_1,n_2)\ge C\).

One may see the coefficient explicitly by writing \(n_1=ca\), \(n_2=cb\), with \(a,b,c\) pairwise coprime:
\[
\begin{split}
T_{\ge C}(u)
={}&\sum_{\substack{Nc\ge C\\(c,S)=1}}
\mu_K(c)^2\nu(c)^2\chi_c(u)^2\\
&\ \times
\sum_{\substack{a,b\ {\rm squarefree}\\(a,b)=1\\(ab,cS)=1}}
\mu_K(a)\mu_K(b)\nu(ab)\chi_{ab}(u)
W(Nc\,Na/D)W(Nc\,Nb/D).
\end{split}
\tag{5.2}
\]
Formula (5.1) follows by freezing \(a,b\), keeping the entire dependence on \(c\) inside the cubic sum, and applying Theorem 2.1. In particular, the cubic phase has not been replaced by a bounded exterior multiplier.

The sufficient cutoff for diagonal fourth-moment energy is
\[
C\ge
\max\left\{
1,\ D^{2/3},\ DH^{-1/3},\ (D^6/H)^{1/7}
\right\}.
\tag{5.3}
\]
For \(H=D^h\), \(1<h\le11/10\), the last exponent dominates the other two:
\[
\frac{6-h}{7}\ge\frac23
\quad\hbox{because }h\le\frac43,
\]
and
\[
\frac{6-h}{7}\ge1-\frac h3
\quad\hbox{because }h\ge\frac34.
\]
Hence
\[
\boxed{
C\ge D^{(6-h)/7}
=D^{(5-\theta)/7}
\quad\Longrightarrow\quad
\|T_{\ge C}\|_2^2\ll_\epsilon D^{2+\epsilon}H,
\qquad h=1+\theta,\ 0<\theta\le1/10.
}
\tag{5.4}
\]
The fixed relation \(H=D^h\) converts \((DH)^\epsilon\) into any prescribed \(D^\epsilon\) by starting with a smaller loss.

The PR #913 squarefree-core estimate requires
\[
C\ge DH^{-1/4}=D^{(4-h)/4}.
\]
Our decrease in the cutoff exponent is exactly
\[
\frac{4-h}{4}-\frac{6-h}{7}
=\frac{4-3h}{28}
=\frac{1-3\theta}{28}>0.
\tag{5.5}
\]
At the limiting scale \(h\downarrow1\), the two exponents are \(3/4\) and \(5/7\), respectively.

This is a strictly larger controlled piece of the polynomial. The complement with smaller gcd remains. No inequality here estimates that complement at diagonal fourth-moment scale.

### Rectangular fourth moment

For \(A_u(X;W_1)A_u(Y;W_2)\), put \(P=XY\). The same proof gives
\[
\|T_{\ge C}(X,Y)\|_2^2
\ll_\epsilon((2+X+Y)H)^\epsilon P^2
\left[H C^{-3}+H^{1/3}C^{-2}+H^{2/3}C^{-7/3}\right].
\tag{5.6}
\]
Thus the target \(HP\) holds whenever
\[
C\ge
\max\left\{
1,\ P^{1/3},\ P^{1/2}H^{-1/3},\
P^{3/7}H^{-1/7}
\right\}.
\tag{5.7}
\]
The support also requires \(C\le\min(\beta_1X,\beta_2Y)\). In the region
\[
P^{3/8}\le H<P^{2/3},
\]
the last term of (5.7) dominates the other two and is strictly smaller than the previous rectangular core cutoff \(P^{1/2}H^{-1/4}\). This proves an explicit anisotropic improvement whenever that range is compatible with the smaller factor scale.

## 6. What the general residue-class theorem does and does not improve

The designated-overlap theorem is a uniform way to preserve the exact character order. It should be combined with, rather than substituted for, the stronger pre-existing core estimate when that estimate wins.

The designated-incidence counterpart of PR #913's common-gcd bound follows directly from the norm weights. For completeness, fix all shared ideals \(q_J\), \(|J|\ge2\), and put
\[
R(\mathbf q)=\prod_{|J|\ge2}(Nq_J)^{|J|},
\qquad P(\mathbf q)=\frac{D^k}{R(\mathbf q)}.
\]
The residual singleton variables have effective scales
\(X_i=D/\prod_{J\ni i,\ |J|\ge2}Nq_J\).
Only \(X_i\ge1/\beta_i\) can occur. Regroup their product into a squarefree column. The number of factor tuples is \(O_{\mathbf W}(\prod_iX_i)\); the fixed-order ideal divisor bound gives coefficient squared mass
\(\ll_\epsilon D^\epsilon P(\mathbf q)\).
The exact exclusion by every shared ideal remains inside that coefficient.

The refined sextic sieve therefore bounds the residual norm by
\[
\ll_\epsilon D^\epsilon\left[
\sqrt H\,P(\mathbf q)^{1/2}
+H^{1/12}P(\mathbf q)
+H^{1/3}P(\mathbf q)^{5/6}
\right].
\tag{6.0a}
\]
Apply Minkowski and sum over the shared ideals with \(Nq_I\ge C\).
For the first term, each ideal \(q_J\) has weight
\((Nq_J)^{-|J|/2}\): the \(|J|=2\) sums cost logarithms up to \(O(D)\), and all \(|J|\ge3\) sums converge. Ignoring the distinguished tail in this first term is harmless. For the second term, every weight has exponent \(|J|>1\), and the distinguished tail is
\[
\sum_{Nc\ge C}(Nc)^{-m}\ll C^{1-m}.
\]
For the third term, every exponent is \(5|J|/6>1\), and the distinguished tail is
\[
\sum_{Nc\ge C}(Nc)^{-5m/6}\ll C^{1-5m/6}.
\]
The pairwise-coprimality and support restrictions may be removed in these positive exterior majorants. Thus, for every designated incidence ideal, the resulting bound is
\[
\|F_{I,\ge C}\|_2^2
\ll_\epsilon (DH)^\epsilon
\left[
HD^k+
H^{1/6}D^{2k}C^{2-2m}
+H^{2/3}D^{5k/3}C^{2-5m/3}
\right].
\tag{6.0b}
\]
In particular, its sufficient core cutoff is
\[
\gamma^{\rm core}_{k,m}(h)=
\max\left\{
0,\
\frac{k-5h/6}{2m-2},\
\frac{2k-h}{5m-6}
\right\}.
\tag{6.1}
\]
Formula (6.1) is therefore the natural comparison for (4.12).

For \(m\ge3\) and \(r=3,6\), the new oscillating-variable bound does not improve this scalar cutoff. Its second cutoff is at least the second one in (6.1), and
\[
\frac{3k-h}{6m-5}-\frac{2k-h}{5m-6}
=
\frac{k(3m-8)+h(m+1)}{(6m-5)(5m-6)}>0.
\tag{6.2}
\]
For \(r=2\), \(m\ge9\), the first oscillating-variable cutoff bounds the last core cutoff because
\[
\frac{k}{2m-1}-\frac{2k-h}{5m-6}
=
\frac{k(m-4)+h(2m-1)}{(2m-1)(5m-6)}\ge0.
\tag{6.3}
\]
For the remaining quadratic case \(m=3\), the second oscillating cutoff bounds the last core cutoff whenever \(h\le2k\):
\[
\frac{k-h/2}{4}-\frac{2k-h}{9}
=\frac{2k-h}{72}\ge0.
\tag{6.4}
\]
This includes the intended \(1<h\le11/10\). The principal case \(6\mid m\) also gives no improvement to (6.1).

For \(m=2\), the new cutoff can improve the core cutoff. On equal scales \(D_i=D\) and the intended \(1<h\le11/10\), a nonempty new range from the unlocalized master theorem occurs at \(k=2\). For \(k\ge3\), the third condition in (4.12) already exceeds 1, so the resulting cutoff is beyond the factor support asymptotically. This prevents a false claim that the new common-gcd trick alone advances every balanced moment.

Rectangular scales and additional fixed overlap restrictions can make the theorem useful inside higher moments as well: the counting argument depends on the remaining factor scales and on the actual number of frozen tuples. Such localized applications require their constraints to be stated explicitly; they are not a full higher-moment result.

### Corollary 6.1. A larger controlled portion at every moment of order \(4\ell\)

Let \(k=2\ell\), \(\ell\ge2\), and expand \(A_u(D)^k\). Fix constants \(0<\eta_0<\eta_1\). Let \(E_{k,\ge C}(u)\) be the exact portion whose designated incidence ideals satisfy
\[
Nq_{\{1,2\}}\ge C,\qquad
\eta_0D\le Nq_{\{3,4\}}<\eta_1D,\quad\ldots,\quad
\eta_0D\le Nq_{\{k-1,k\}}<\eta_1D.
\tag{6.5}
\]
All other incidence ideals and all allowed cross-overlaps retain their exact conditions. Then
\[
\boxed{
\|E_{k,\ge C}\|_2^2
\ll_{\epsilon,k,\mathbf W,\eta_0,\eta_1}
(DH)^\epsilon D^{k+2}
\left[
H C^{-3}+H^{1/3}C^{-2}+H^{2/3}C^{-7/3}
\right].
}
\tag{6.6}
\]
In particular, for \(H=D^{1+\theta}\), \(0<\theta\le1/10\), the cutoff
\[
C\ge D^{(5-\theta)/7}
\]
gives \(\|E_{k,\ge C}\|_2^2\ll_\epsilon HD^{k+\epsilon}\).

To prove this, each outside original pair \((n_{2j-1},n_{2j})\), \(2\le j\le\ell\), has an ordinary gcd of norm at least \(\eta_0D\). Its two residual ideals therefore have bounded norm depending only on \(\eta_0\) and the fixed supports. The number of possible outside pairs is \(O(D)\), and the number of outside tuples is \(O(D^{\ell-1})\).

Freeze an outside tuple. On a dyad \(Nq_{\{1,2\}}\asymp L\), write \(n_1=ca_1,n_2=ca_2\), \(c=q_{\{1,2\}}\), and freeze \(a_1,a_2\). There are \(O((D/L)^2)\) choices. Impose the exact eligibility conditions of Theorem 4.1 and the remaining conditions (6.5) as row-independent coefficient restrictions. In particular, \(c\) is coprime to every outside original factor. Each outside designated-pair condition is then determined by the frozen tuple and residual factors; alternatively its full indicator can simply remain in the arbitrary \(c\)-coefficient. The varying character is exactly \(\chi_c(u)^2\), the coefficient squared mass is \(O(L)\), and the frozen row multiplier is bounded.

Apply Theorem 2.1 and Minkowski over \(O(D^{\ell-1}(D/L)^2)\) frozen labels. This is the proof of (5.1) with the norm multiplied by \(D^{\ell-1}\), and hence its energy multiplied by \(D^{k-2}\). The dyadic tail sum is unchanged. This proves (6.6).

For the same localized class, the preceding core method gives the cutoff \(DH^{-1/4}\): in its second norm term each outside pair dyad contributes
\(\sum_{Nc\asymp D}(Nc)^{-2}\ll D^{-1}\), and in its third term it contributes
\(\sum_{Nc\asymp D}(Nc)^{-5/3}\ll D^{-2/3}\).
The resulting two energy errors are
\[
H^{1/6}D^{k+2}C^{-2},
\qquad
H^{2/3}D^{k+4/3}C^{-4/3}.
\tag{6.7}
\]
Relative to \(HD^k\), their sufficient cutoffs are \(DH^{-5/12}\) and \(DH^{-1/4}\). Thus (6.6) strictly enlarges that matched range by the same exponent difference (5.5).

Nonempty support is required: the constants \(\eta_0,\eta_1\) and the factor tests must permit the large outside pair ideals, and \(C\) must fit inside the first two factor supports. For configurations with no additional shared ideals, the singleton product is of order \(D^2/(Nq_{\{1,2\}})^2\). Those between the new and old cutoffs are outside the earlier criterion \(P\le H^{1/2}\). This identifies the enlarged portion without claiming control of every tuple contributing to the \(4\ell\)-th moment.

## 7. An optional Möbius-specific improvement, with a separate imported premise

This section uses a stronger and separately identified input: the September 30 manuscript's all-row inverse second moment, label eq:raw-moment, together with its scale-uniform form eq:inverse-scale-supremum and the moving-exclusion adapter. It is not being presented as a consequence of the classical sieves above.

The required input is the following uniform statement for every fixed \(c_0>0\), every fixed finite-order twist and either sextic orientation, with \(H\ge X^{1+c_0}\):
\[
\sum_{0<Nu\le H}
\left|
\sum_{\substack{(n,SQ)=1}}
\mu_K(n)\xi(n)\chi_n(u)^{\pm1}V(Nn/X)
\right|^2
\ll_{\epsilon,c_0,V}(XH\,NQ)^\epsilon HX.
\tag{7.1}
\]
Here \(Q\) is a moving exclusion ideal of polynomial size in the ambient scale, the constants are uniform for tests in a bounded smooth family, and the same row bound \(H\) is retained at every smaller scale. Section 7 is conditional on precisely this input.

The original raw moment has \(Q=1\). The previously reviewed moving-mask adapter in the generalized-inverse-moments packet supplies (7.1) from that source input: reciprocal local factors have absolutely summable norm costs \(\prod_{p\mid Q}(1-(Np)^{-1/2})^{-1}\ll_\epsilon(NQ)^\epsilon\), and every resulting smaller-scale moment has the same \(H\). Fixed bad primes are kept fixed.

If \(m\equiv1,5\pmod6\), then
\[
\mu_K(c)^m=\mu_K(c),\qquad
\chi_c(u)^m=\chi_c(u)^{\pm1}.
\]
After freezing the residual tuple in Section 4, the varying coefficient has exactly the Möbius sign, a fixed finite-order twist \(\nu^m\), the moving exclusion, and a uniformly smooth weight at scale \(L\).

For this application use a smooth dyadic partition supported in a fixed compact subinterval of \((0,\infty)\), rather than a sharp dyad. Its weight is of the form
\[
V_{\mathbf a,L}(t)=
\rho(t)\prod_{i\in I}W_i(t\,LNa_i/D_i).
\tag{7.2}
\]
On every nonempty block the parameters \(LNa_i/D_i\) are bounded above by fixed constants; all derivatives of (7.2) are consequently bounded uniformly. The frozen exclusion ideal has norm at most a fixed power of \(D_*\). A dyadic partition of a tail cutoff can be made smooth with uniformly bounded seminorms if the cutoff itself is smooth; a sharp cutoff instead requires a standard interval-maximal version of (7.1). Thus the assertion below is stated for smooth gcd tails, unless that maximal version is supplied.

Assume \(H=D^h\), \(h>1\) fixed, all \(D_i=D\), and take \(0<c_0<h-1\). Then \(H\ge L^{1+c_0}\) for all contributing \(L\ll_{\mathbf W}D\), after adjusting bounded endpoints. Applying (7.1), then the identical tuple count and Minkowski argument, gives
\[
\|F_{I,\ge C}^{\rm smooth}\|_2^2
\ll_\epsilon H D^{2k+\epsilon}C^{1-2m}.
\tag{7.3}
\]
Here the smooth tail is any fixed smooth weight in \(Nq_I/C\) which vanishes below a positive constant and equals one above another fixed constant, with the original compact factor supports still present.

The diagonal target follows when
\[
C\ge D^{k/(2m-1)}.
\tag{7.4}
\]
There are parameter ranges where this improves (6.1). A sufficient condition for strict improvement over its second term, together with a nonempty cutoff, is
\[
\frac{5h(2m-1)}6<k<2m-1.
\tag{7.5}
\]
The third term must also be checked in each comparison; when it is larger, the new bound may still help.

For example, \(m=5\), \(k=8\), \(1<h<16/15\), gives cutoff \(D^{8/9}\), while the core cutoff is
\[
\max\left\{D^{1-5h/48},D^{(16-h)/19}\right\}
=D^{1-5h/48}.
\tag{7.6}
\]
At these parameters \(1-5h/48>8/9\). The range is compatible with the support if the five overlapping factors have room at that scale; it concerns that designated-overlap piece only. It depends on the imported inverse moment and does not follow merely from the classical large sieves.

This signed argument has not improved the genuinely balanced, nearly coprime residual core. On that core the Möbius factor is multiplied by a balanced divisor convolution; replacing its coefficients by arbitrary ones loses precisely the input needed to obtain a full fourth or higher moment.

## 8. Remaining target

The principal proved addition is (5.1), with the strict cutoff improvement (5.4), and its rectangular form (5.6)–(5.7). All row classes, local zeros, exact gcd eligibility conditions, bounded scales, and norm summations were retained.

The remaining full fourth-moment problem is a mean square for the actual balanced Möbius coefficient with \(N\gcd(n_1,n_2)<D^{(5-\theta)/7}\), including the nearly coprime range. The unbounded hierarchy still has the RH-level strength already identified in PR #912. Neither the new cubic overlap estimate nor the optional signed overlap estimate supplies that missing balanced-core cancellation.
