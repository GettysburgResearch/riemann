# Genus-two third-order primitive inventory

Status: **REDUCED exactly to eight level-2 genus-one trace channels** for
every odd prime power.

Scope: let \(q\) be an odd prime power. A primitive conductor \(r\) is a
squarefree product of exactly \(\ell\) monic linear primes and \(k\) monic
irreducible-quadratic primes over \(\mathbf F_q\). This packet treats all
twelve types with

\[
 \ell+2k\in\{4,6,8\}.
\]

It proves exact formulas for the conductor sums of \(s_1^3\), \(s_1s_2\),
\(s_3\), and every marked deletion correlation required by the frozen
54-signature \(B4\) ledger. The formulas are not polynomials in \(q\) alone:
they retain eight explicitly named trace moments on the fully split and
linear-times-quadratic cubic strata. The exact coefficient polynomials are
frozen in genus2_third_order_primitive_inventory.json and replayed by
genus2_third_order_primitive_inventory.py.

Exact dependencies: GENUS2_B3_PRIMITIVE_TRACE_AVERAGE.md supplies the lower
sign inventories and their normalization; GENUS1_CUBIC_FAMILY_LAWS.md
supplies only the full level-one cubic moments through degree eight; and
genus2_second_moment_reduction.json supplies the exact \(B4\)
conductor/deletion support. All three dependency packets are content-hash
and canonical-payload locked by the producer.

## 1. Definitions

Put

\[
 I={q(q-1)\over2},\qquad n={q-1\over2}.
\]

For \(N\) signs in \(\{+1,-1\}\) with total \(S\), let \(E_j(N,S)\) be their
\(j\)-th elementary symmetric sum. Newton's identities give

\[
 jE_j(N,S)=\sum_{i=1}^j(-1)^{i-1}E_{j-i}(N,S)p_i,\qquad
 p_i=\begin{cases}S,&i\text{ odd},\\N,&i\text{ even}.
 \end{cases}                                                     \tag{1}
\]

Let \(\chi_m\) be the quadratic character of \(\mathbf F_{q^m}\), extended
by zero, and define

\[
 s_m(r)=\sum_{z\in\mathbf F_{q^m}}\chi_m(r(z)).                    \tag{2}
\]

For a monic squarefree cubic \(f\), put

\[
 a_f=-\sum_{x\in\mathbf F_q}\chi(f(x)).                            \tag{3}
\]

Write \(\mathcal C_{111}\), \(\mathcal C_{12}\), and \(\mathcal C_3\) for
the monic squarefree cubics with respectively three linear factors, one
linear and one irreducible-quadratic factor, and one irreducible-cubic
factor. For \(\nu\in\{111,12,3\}\), define

\[
 M_{\nu,2j}(q)=\sum_{f\in\mathcal C_\nu(q)}a_f^{2j}.                \tag{4}
\]

The eight residuals retained by this packet are

\[
 M_{111,2},M_{111,4},M_{111,6},M_{111,8},
 \quad
 M_{12,2},M_{12,4},M_{12,6},M_{12,8}.                              \tag{5}
\]

## 2. The affine-fibre sign inventory

Let \(f\) have \(m_1\) rational roots and \(m_2\)
irreducible-quadratic factors. Thus

\[
 (m_1,m_2)=(3,0),(1,1),(0,0)
\]

on the three strata above. Put \(\eta_q=\chi(-1)\). The local signs attached
to the \(q\) monic linear conductor primes have nonzero population
\(q-m_1\) and total

\[
 -\eta_q a_f.                                                            \tag{6}
\]

The signs attached to the \(I\) monic irreducible-quadratic conductor primes
have nonzero population \(I-m_2\) and total

\[
 {q+m_1-a_f^2\over2}.                                                    \tag{7}
\]

Consequently define

\[
 G_{\ell,k}^{(m_1,m_2)}(a)
 =E_\ell(q-m_1,-\eta_q a)
  E_k\!\left(I-m_2,{q+m_1-a^2\over2}\right).                    \tag{8}
\]

### Proof of (6)--(7)

In each of the three point fibres below, a monic linear prime \(T-c\)
contributes \(\chi(-f(c))\), giving (6). For the quadratic primes, quadratic
reciprocity has sign \(+1\), because the degree product is \(2\cdot3\).
Thus a monic irreducible quadratic \(Q\) contributes \((f/Q)\).

The degree-two coefficient of

\[
 L_f(u)=1-a_fu+qu^2
\]

is \(q\). The \(q-m_1\) nonzero squared-linear denominators contribute
\(q-m_1\), while products of two distinct linear denominators contribute

\[
 e_2={a_f^2-(q-m_1)\over2}.
\]

Subtracting those two parts from \(q\) proves (7). A quadratic factor of
\(f\) gives the one zero sign accounted for by \(m_2\).

For any fixed nonsquare \(\alpha\), the affine bijection

\[
 f(T)\longmapsto \alpha^{-3}f(\alpha T)
\]

preserves each factorization stratum and sends \(a_f\) to \(-a_f\).
Therefore every odd trace moment vanishes separately on each stratum. The
\(\eta_q\) in (8) consequently disappears after summing over a stratum; no
two-branch guess in \(q\bmod4\) is made.

## 3. Exact third-order formulas

Let \(N_{\ell,k}=\binom q\ell\binom Ik\), and abbreviate

\[
 A_{\ell,k}=\sum_r s_1(r).
\]

The \(B3\) sign-inventory theorem gives \(A_{\ell,k}\),
\(\sum_rs_1(r)^2\), \(\sum_rs_2(r)\), \(\sum_rp_1(r)\), and
\(\sum_rp_2(r)\) as explicit polynomials in \(q\). The new identities are

\[
\begin{aligned}
 \sum_r s_1(r)^3
={}&A_{\ell,k}
 +{3q(q-1)\over2}
 \bigl(E_\ell(q-2,-1)+E_\ell(q-2,1)\bigr)E_k(I,-n)\\
 &+6\sum_{f\in\mathcal C_{111}}
     G_{\ell,k}^{(3,0)}(a_f),                                      \tag{9}\\
 \sum_r s_1(r)s_2(r)
={}&(q-\ell)A_{\ell,k}
 +2\sum_{f\in\mathcal C_{12}}
     G_{\ell,k}^{(1,1)}(a_f),                                     \tag{10}\\
 \sum_r s_3(r)
={}&A_{\ell,k}
 +3\sum_{f\in\mathcal C_3}
     G_{\ell,k}^{(0,0)}(a_f).                                     \tag{11}
\end{aligned}
\]

These are the requested all-\(q\) primitive formulas. Expanding (8),
discarding its separately vanishing odd powers, and applying (4) produces
the coefficient polynomials stored in every JSON row.

### Proof of the fibre multiplicities

For \(s_1^3\), partition ordered triples in \(\mathbf F_q^3\).

- The all-equal part is \(A_{\ell,k}\).
- In the exactly-two-equal part, the \(q-2\) nonzero linear-prime signs have
  total \(-\chi(y-x)\), while the irreducible-quadratic signs retain total
  \(-n\). Among ordered \(x\ne y\), the two values of \(\chi(y-x)\) occur
  equally often. This gives the middle term of (9).
- An all-distinct ordered triple is the ordered root set of one member of
  \(\mathcal C_{111}\), with exactly \(3!=6\) orderings. Equations (6)--(8)
  give the last term.

For \(s_1s_2\), the rational points of \(\mathbf F_{q^2}\) contribute
\((q-\ell)s_1(r)\), because the restricted quadratic character is one at
each nonroot. Every nonrational point has degree two. Pairing it with the
rational \(s_1\)-point gives one cubic in \(\mathcal C_{12}\), and its two
conjugate roots give multiplicity two. This proves (10).

For \(s_3\), the rational points contribute \(s_1(r)\). Since three is
prime, every remaining point of \(\mathbf F_{q^3}\) has degree three. Its
Frobenius orbit is one member of \(\mathcal C_3\), with three roots. This
proves (11). These maps are the full affine-fibre bridge; no fibre is
silently replaced by the full cubic family.

Finally, the degree-three Newton coefficient gives

\[
 \boxed{
 \sum_rp_3(r)=\sum_rp_2(r)
 +{\sum_rs_1(r)^3+3\sum_rs_1(r)s_2(r)+2\sum_rs_3(r)\over6}.}       \tag{12}
\]

## 4. What the level-one theorem does and does not close

The three cubic strata have exact sizes

\[
 \binom q3,\qquad {q^2(q-1)\over2},\qquad {q^3-q\over3},             \tag{13}
\]

whose sum is \(q^2(q-1)\). The source-locked genus-one theorem gives, for
\(0\le j\le4\),

\[
 \boxed{
 M_{111,2j}+M_{12,2j}+M_{3,2j}
 =q(q-1)W_{2j}(q).}                                                 \tag{14}
\]

Here

\[
\begin{aligned}
 W_0&=q,\\
 W_2&=q^2-1,\\
 W_4&=2q^3-3q-1,\\
 W_6&=5q^4-9q^2-5q-1,\\
 W_8&=14q^5-28q^3-20q^2-7q-1.
\end{aligned}                                                        \tag{15}
\]

The producer uses (14) to eliminate every \(M_{3,2j}\). It does not replace
\(M_{111,2j}\) or \(M_{12,2j}\) by \(W_{2j}\). Those are level-2 or
rational-2-torsion channels and can carry earlier cohomological terms than
the full level-one family.

This basis is minimal under only (14). The JSON records an exact
\(8\times8\) coefficient minor built from four \(s_1^3\) rows and four
\(s_1s_2\) rows. Its exact specialization at the formal value \(q=17\) has
determinant

\[
 {13\over4194304}\ne0.                                                 \tag{16}
\]

Therefore the polynomial minor is not identically zero, its rank over
\(\mathbf Q(q)\) is eight, and no smaller residual basis follows from the
four level-one total-moment relations. The value \(17\) in this certificate
is not a finite-field sample or theorem input.

## 5. Exact deletion correlations

Put

\[
 N=q-\ell,\qquad J=I-k,\qquad
 B_{\ell,k}=\sum_rs_1(r)^2,\qquad C_{\ell,k}=\sum_rs_2(r),
\]

and abbreviate

\[
 X_{\ell,k}=\sum_rs_1(r)^3,\qquad
 Y_{\ell,k}=\sum_rs_1(r)s_2(r).
\]

All sums below include the choice of external deletion prime or primes.
For conductor degree six with one external linear deletion,

\[
\begin{aligned}
 \sum C_1&=(N-1)A_{\ell,k},\\
 \sum C_3&=N\bigl(q\sum p_1-\sum p_2\bigr)
             -{X_{\ell,k}+Y_{\ell,k}\over2},\\
 \sum C_5&=-Nq^2N_{\ell,k}-q^2A_{\ell,k}
             +q(A_{\ell,k}+B_{\ell,k}).                              \tag{17}
\end{aligned}
\]

For conductor degree four with one external linear deletion,

\[
 \sum C_1=(N-1)A_{\ell,k},\qquad
 \sum C_3=-qNN_{\ell,k}+(1-q)A_{\ell,k}+B_{\ell,k},\qquad
 \sum C_5=0.                                                          \tag{18}
\]

For conductor degree four with one external irreducible-quadratic deletion,

\[
\begin{aligned}
 \sum C_1&=JA_{\ell,k},\\
 \sum C_3&=-qJN_{\ell,k}-{Y_{\ell,k}-NA_{\ell,k}\over2},\\
 \sum C_5&={q\over2}\bigl(C_{\ell,k}-NN_{\ell,k}\bigr).               \tag{19}
\end{aligned}
\]

For conductor degree four with two unordered external linear deletions,

\[
\begin{aligned}
 \sum C_1&={(N-1)(N-2)\over2}A_{\ell,k},\\
 \sum C_3&=-q\binom N2N_{\ell,k}
 -(N-1)\bigl((q-1)A_{\ell,k}-B_{\ell,k}\bigr)
 +{X_{\ell,k}-NA_{\ell,k}\over2},\\
 \sum C_5&=-{q\over2}\bigl(B_{\ell,k}-NN_{\ell,k}\bigr).              \tag{20}
\end{aligned}
\]

Equations (17)--(20) follow by multiplying the primitive \(L\)-polynomial
by the appropriate deletion factors and using

\[
 \sum_{P\nmid r}\left({P\over r}\right)=s_1(r),
 \qquad
 \sum_{Q\nmid r}\left({Q\over r}\right)={s_2(r)-N\over2},             \tag{21}
\]

together with

\[
 e_2\bigl((P/r):P\nmid r\bigr)={s_1(r)^2-N\over2}.                   \tag{22}
\]

The composite-denominator convention remains load-bearing: a positive even
exponent retains the local zero on multiples of that prime, so every such
prime remains a deletion factor.

## 6. Exact completion boundary

The frozen \(B4\) source has 54 signatures. Its new arithmetic needs exactly:

- \(p_3\) for the five degree-eight conductor types;
- \(s_1^3+s_1s_2\) for degree six with one external linear deletion;
- \(s_1s_2\) for degree four with one external quadratic deletion; and
- \(s_1^3\) for degree four with two external linear deletions.

This packet supplies all of those as exact affine expressions in the eight
residuals (5). A downstream 54-row reweight may prove that their coefficients
cancel. Such cancellation is not asserted here and must not be used to
retroactively relabel the individual conductor-type rows as polynomials.

From the successor worktree root, replay with:

    python research/l-families/atlas/function_field/genus2_third_order_primitive_inventory.py --check
    python -O research/l-families/atlas/function_field/genus2_third_order_primitive_inventory.py --check
    python -m unittest tests.test_genus2_third_order_primitive_inventory
    python -O -m unittest tests.test_genus2_third_order_primitive_inventory

The producer uses exact integer and Fraction algebra, enumerates no finite
field or family member, and stays below 4096 declared complete-polynomial,
complete-bivariate, residual-expression, and input-atom operations. This is
an exact reduction, not a novelty claim, a memberwise sign claim, or an RH or
GRH claim.
