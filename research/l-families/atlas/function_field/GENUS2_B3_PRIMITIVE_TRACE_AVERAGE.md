# Genus-two B3 primitive trace average

Status: **PROVED** by exact character-sum algebra for every odd prime power.

Scope: let \(q\) be an odd prime power and let \(\mathcal H_5(q)\) be the
monic squarefree quintics in \(\mathbf F_q[T]\). No finite field or family
member is enumerated. The replay is
`genus2_b3_primitive_trace_average.py`; its frozen result is
`genus2_b3_primitive_trace_average.json`.

Exact dependencies: the identity

\[
 b_D=\sum_{f\in\mathcal M_2}\left(\frac Df\right)
\]

and the squarefree sieve from `GENUS2_MOMENT_IDENTITY.md`, the exact 23-row
factor-signature ledger from `genus2_high_weight_channel_probe.json`, and the
marked-Weierstrass normalization in
`GENUS2_MARKED_WEIERSTRASS_STACK_ADAPTER.md`. All three inputs are
content-hash locked by the producer.

## 1. The theorem

For every odd prime power \(q\),

\[
\boxed{
 \sum_{D\in\mathcal H_5(q)}b_D^3
 =q(q-1)
 \left(4q^6-9q^5+7q^4+8q^3-12q^2-9q-1\right).
}
\tag{1}
\]

Since \(\#\mathcal H_5(q)=q^4(q-1)\), this is equivalently

\[
\boxed{
 \mathbb E[b_D^3]
 =\frac{4q^6-9q^5+7q^4+8q^3-12q^2-9q-1}{q^3}.
}
\tag{2}
\]

Substitution into the exact character identity

\[
 \chi_{0,3}
 =\frac{b_D^3}{q^3}-\frac{b_D^2}{q^2}
  -\frac{2a_D^2b_D}{q^2}-\frac{b_D}{q}
  +\frac{3a_D^2}{q}
\tag{3}
\]

and the four previously proved lower moments gives

\[
\boxed{
 \mathbb E_{\mathcal H_5(q)}[\chi_{0,3}(U_D)]
 =\frac{q^4-2q-1}{q^6}.
}
\tag{4}
\]

The marked-stack adapter therefore turns (4) into the denominator-free
identity

\[
\boxed{
 T_{0,3}(q)
 =\frac{q^3}{q(q-1)}
   \sum_{D\in\mathcal H_5(q)}\chi_{0,3}(U_D)
 =q^4-2q-1.
}
\tag{5}
\]

Thus `B3-PRIMITIVE-TRACE-AVERAGE`, isolated as the first open lemma in the
high-weight channel packet, is closed. This is an exact family theorem, not a
memberwise sign statement.

## 2. The finite sign-inventory lemma

Put

\[
 I=\frac{q(q-1)}2,
 \qquad n=\frac{q-1}2.
\]

For \(N\) signs \(\varepsilon_i\in\{\pm1\}\) whose total is \(S\), write

\[
 E_j(N,S)=e_j(\varepsilon_1,\ldots,\varepsilon_N).
\]

Newton's identities determine this polynomial exactly:

\[
 jE_j(N,S)
 =\sum_{i=1}^j(-1)^{i-1}E_{j-i}(N,S)p_i,
 \qquad
 p_i=\begin{cases}S,&i\text{ odd},\\N,&i\text{ even}.
 \end{cases}
\tag{6}
\]

Let \(r\) be squarefree with exactly \(\ell\) linear prime factors and \(k\)
irreducible-quadratic prime factors. In this packet only
\(\ell+2k=4\) or \(6\). Set

\[
 s_1(r)=\sum_{x\in\mathbf F_q}\chi(r(x)),
 \qquad
 s_2(r)=\sum_{z\in\mathbf F_{q^2}}\chi_2(r(z)),
\]

and let every sum below run over all such \(r\). Then, with
\(N_{\ell,k}=\binom q\ell\binom Ik\),

\[
\boxed{
 \sum_r s_1(r)
 =qE_\ell(q-1,0)E_k(I,-n),
}
\tag{7}
\]

\[
\boxed{
 \begin{aligned}
 \sum_r s_1(r)^2
 &=q\binom{q-1}{\ell}\binom Ik\\
 &\quad+q(q-1)E_\ell(q-2,-1)E_k(I,-n),
 \end{aligned}
}
\tag{8}
\]

and

\[
\boxed{
 \begin{aligned}
 \sum_r s_2(r)
 &=q\binom{q-1}{\ell}\binom Ik\\
 &\quad+2I E_\ell(q,-1)E_k(I-1,-(n+1)).
 \end{aligned}
}
\tag{9}
\]

These formulas remain literal when a factorization type is empty at a small
field: the relevant binomial or elementary-symmetric polynomial is zero.

### Proof of the sign inventories

For a fixed \(x\in\mathbf F_q\), the \(q-1\) nonzero values
\(\chi(x-a)\) have total zero. The \(I\) values \(\chi(Q(x))\), over monic
irreducible quadratics \(Q\), have total \(-n\). To see the second assertion,
sum over all monic quadratics. Their total character sum at \(x\) is zero;
the reducible quadratics are multisets of two linears and contribute the
complete symmetric sum

\[
 h_2=\frac{0^2+(q-1)}2=n.
\]

This proves (7).

For ordered \(x\ne y\), the \(q-2\) nonzero signs

\[
 \chi((x-a)(y-a))
\]

have total \(-1\), the standard two-point quadratic correlation. Evaluation
at \(x,y\) maps the \(q^2\) monic quadratics bijectively to
\(\mathbf F_q^2\), so their total product-character sum is zero. The
reducible part contributes

\[
 h_2=\frac{(-1)^2+(q-2)}2=n,
\]

and hence the irreducible-quadratic signs again total \(-n\). Separating the
diagonal \(x=y\) from the \(q(q-1)\) ordered off-diagonal pairs proves (8).

For (9), the rational points of \(\mathbf F_{q^2}\) contribute the same
diagonal term. Fix a monic irreducible quadratic \(Q_0\) and one of its two
roots. The \(q\) linear-prime signs modulo \(Q_0\) total \(-1\). Reduction
modulo \(Q_0\) maps the \(q^2\) monic quadratics bijectively to
\(\mathbf F_{q^2}\), whose complete quadratic-character sum is zero. The
reducible part now contributes

\[
 h_2=\frac{(-1)^2+q}{2}=n+1,
\]

so the \(I-1\) nonzero signs from \(Q\ne Q_0\) total \(-(n+1)\). There are
\(I\) conjugate pairs and two roots per pair, proving (9). All reciprocity
swaps have even degree product and therefore sign \(+1\).

## 3. Primitive \(p_1,p_2\) are now explicit

For a squarefree conductor of degree six write

\[
 L_r(u)
 =(1-u)(1+p_1(r)u+p_2(r)u^2+qp_1(r)u^3+q^2u^4).
\tag{10}
\]

The degree-one and degree-two Dirichlet coefficients give

\[
 p_1(r)=1+s_1(r),
 \qquad
 p_2(r)=1+s_1(r)+\frac{s_1(r)^2+s_2(r)}2.
\tag{11}
\]

For completeness, the second equality follows by partitioning monic
quadratics into squares, products of distinct linears, and irreducibles; the
three contributions sum to \((s_1^2+s_2)/2\).

Equations (7)--(11) evaluate every primitive average that survived the
earlier signature-level noncancellation test. The four degree-six results are
as follows.

| \((\ell,k)\) | \(\sum_r p_1(r)\) | \(\sum_r p_2(r)\) |
|---:|---:|---:|
| \((6,0)\) | \(q(q-7)(q-5)(q-3)(q-1)(q+1)/720\) | \(q(q-5)(q-3)(q-1)(q^3-11q^2+23q+5)/720\) |
| \((4,1)\) | \(q(q-3)^2(q-1)^2(q+1)/48\) | \(q(q-3)(q-1)^2(q^3-5q^2+3q+3)/48\) |
| \((2,2)\) | \(q(q-1)^4(q+1)/16\) | \(q(q-1)^2(q+1)(q^3-3q^2+3q-3)/16\) |
| \((0,3)\) | \(q(q-1)^4(q+1)/48\) | \(q(q-1)(q+1)(q^4-2q^3-7)/48\) |

No curve enumeration, Hasse bound, or interpolation enters this table.

## 4. The marked degree-four deletion also closes

The remaining apparent nuisance is a conductor-degree-four row with one
external squared linear prime. Write

\[
 L_r(u)=(1-u)(1+c_r u+qu^2),
 \qquad s_1(r)=c_r-1.
\]

If \(P\nmid r\) is the deletion prime and
\(\varepsilon_P=(P/r)=\chi(r(P))\), then

\[
 C_1(rP^2)=c_r-1-\varepsilon_P,
 \qquad
 C_3(rP^2)=-q-\varepsilon_P(q-c_r).
\tag{12}
\]

For a type with \(\ell\) linear roots there are \(q-\ell\) possible \(P\),
and

\[
 \sum_{P\nmid r}\varepsilon_P=s_1(r),
 \qquad
 \sum_{P\nmid r}c_r\varepsilon_P=s_1(r)+s_1(r)^2.
\tag{13}
\]

Therefore the marked rows require only the already evaluated expressions
(7) and (8):

\[
 \sum_{r,P}C_1=(q-\ell-1)\sum_r s_1(r),
\tag{14}
\]

\[
 \sum_{r,P}C_3
 =-q(q-\ell)N_{\ell,k}
  +(1-q)\sum_r s_1(r)+\sum_r s_1(r)^2.
\tag{15}
\]

Thus there is no residual deletion-character average.

### Independent degree-two deletion audit

The ten conductor-degree-two signatures are especially sensitive to the
composite-denominator convention. Here \(L_r(u)=1-u\). If the deletion set
is empty, one linear prime, two linear primes, or one quadratic prime, the
only possibly nonzero coefficients are respectively

\[
 (C_1,C_3)=(-1,0),
 \quad(-1-\varepsilon,0),
 \quad(-1-\varepsilon_1-\varepsilon_2,-\varepsilon_1\varepsilon_2),
 \quad(-1,\varepsilon).
\tag{16}
\]

For \(r=LM\), the \(q-2\) external linear signs total \(-1\), and the
irreducible-quadratic signs total \(-n\). For irreducible \(r=Q_0\), the
\(q\) linear signs total \(-1\), and the \(I-1\) signs from
\(Q\ne Q_0\) total \(-(n+1)\). Applying the elementary sum \(E_2\) to the
two-linear case evaluates every aggregate \(C_1,C_3\) in those ten rows.
An independent plus/minus-binomial audit, separate from the producer's
Newton recurrence, matched all ten row polynomials coefficientwise.

## 5. Closing the 23 signatures

For a monic degree-six product \(h=f_1f_2f_3\), let \(r(h)\) be its odd
radical, let \(C_j(h)=[u^j]L_h(u)\), and let \(l,k\) count the linear and
irreducible-quadratic primes in its support. Polynomial Möbius inversion gives

\[
 S_5(h)
 =C_5(h)-(q-l)C_3(h)
  +\left(\binom{l+1}{2}+k-ql\right)C_1(h).
\tag{17}
\]

The composite-denominator convention is load-bearing here. By definition

\[
 \left(\frac Fh\right)=\prod_P\left(\frac FP\right)^{v_P(h)},
\]

and each local symbol is zero when \(P\mid F\). Thus an even exponent makes
the local value one only away from \(P\); it does **not** remove the zero on
multiples of \(P\). Every positive even-exponent prime must remain in the
deletion set

\[
 L_h(u)=L_{r(h)}(u)
 \prod_{P\in E(h)}
 \left(1-\left(\frac P{r(h)}\right)u^{\deg P}\right).
\tag{18}
\]

The radical-degree-zero rows use the principal Euler product. The
degree-two rows use \(L_r=1-u\) and the same one- and two-sign identities
above. Equations (7)--(15) settle the degree-four and degree-six rows. The
23 frozen ordered-triple signatures have radical-degree census
\((4,10,5,4)\) in degrees \((0,2,4,6)\), and their weighted type-count
polynomials sum coefficientwise to \(q^6\). They then give these four
independently checked blocks, written in expanded form:

| \(\deg r\) | weighted contribution to \(\sum_D b_D^3\) |
|---:|---:|
| 0 | \(5q^8-23q^7+62q^6-134q^5+250q^4-357q^3+309q^2-112q\) |
| 2 | \(39q^5-330q^4+1084q^3-1566q^2+773q\) |
| 4 | \(6q^7-56q^6+206q^5-196q^4-809q^3+2214q^2-1365q\) |
| 6 | \(-q^8+4q^7+10q^6-110q^5+256q^4+85q^3-949q^2+705q\) |

Their coefficientwise sum is

\[
 4q^8-13q^7+16q^6+q^5-20q^4+3q^3+8q^2+q,
\]

which factors as the right side of (1). The JSON retains all 23 individual
\(C_1,C_3,C_5,S_5\) aggregate polynomials, so the block compression does not
hide a row-level cancellation.

## 6. Replay and proof boundary

From the successor worktree root:

```text
python research/l-families/atlas/function_field/genus2_b3_primitive_trace_average.py --check
python -O research/l-families/atlas/function_field/genus2_b3_primitive_trace_average.py --check
python -m unittest tests.test_genus2_b3_primitive_trace_average
python -O -m unittest tests.test_genus2_b3_primitive_trace_average
```

The producer uses only integer and `Fraction` arithmetic. It consumes 23
signature atoms and seven primitive conductor types under a cap of 4096
declared complete-polynomial operations plus input atoms.

This packet proves an exact finite-field family law. It makes no claim that
the formula is externally novel, supplies no memberwise positivity, and
implies no RH or GRH statement. The smallest invalidating point would be a
failure of one of the three sign inventories (7)--(9), the squarefree sieve
(17), or the source-locked 23-signature weights.
