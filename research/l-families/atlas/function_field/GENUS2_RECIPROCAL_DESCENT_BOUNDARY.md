# Genus-two reciprocal-descent phase boundary

Status: **PROVED as exact formal coefficient algebra** for every even endpoint
in the bounded panel \(2\le d\le20\), with the general \(d\ge12\) step proved
symbolically. The replay enumerates no finite field, curve, quintic, or
degree-\(d\) modulus.

## Start here

The degree-five squarefree sieve always contains the coefficient \(C_5(f)\)
of the quadratic \(L\)-polynomial attached to the reciprocal Euler variable
\(f\). For even \(\deg f=d\), its completed functional equation removes that
coefficient through \(d=10\):

\[
\begin{array}{c|c}
d&C_5(f)\\ \hline
2,4&0,\\
6&-q^2,\\
8&q(q-1)(1+C_1)-qC_2,\\
10&(q-1)(1+C_1+C_2+C_3)-C_4.
\end{array}                                                     \tag{1}
\]

At \(d=12\), \(C_5\) contains the central completed coefficient. For every
even \(d\ge12\), it is not determined by \(C_0,\ldots,C_4\) from the
functional equation. If one then applies quadratic reciprocity to the
uneliminated \(C_5\) row, it becomes \(G_5\). The squarefree degree-five part
of \(G_5\) is the original target. It cancels from both sides and leaves a
consistency identity rather than a moment formula.

Thus **the \(\operatorname{Sym}^{10}\) endpoint is the last
non-self-referential even endpoint for this particular one-step
squarefree-sieve/functional-equation/reciprocity descent**. This is not a
claim that higher moments are unknowable. A refined sieve, a second descent,
geometric input, or a cohomological trace theorem could still determine them.

The canonical machine-readable proof is
`genus2_reciprocal_descent_boundary.json`; its producer and tests are
`genus2_reciprocal_descent_boundary.py` and
`tests/test_genus2_reciprocal_descent_boundary.py`.

## 1. The universal quintic sieve

Let

\[
 \mathcal H_5(q)=\{D\in\mathbf F_q[T]:D\text{ monic squarefree},\ \deg D=5\}
\]

and write

\[
 P_D(u)^{-1}=\sum_{n\ge0}r_D(n)u^n.
\]

At endpoint \(d\), the inverse quadratic Euler product gives

\[
 r_D(d)=\sum_{\substack{f\text{ monic squarefree}\\\deg f=d}}
            \mu(f)\left(\frac Df\right).                       \tag{2}
\]

Fix a squarefree \(f\), let \(\ell\) be its number of linear factors and \(k\)
its number of irreducible-quadratic factors, and put

\[
 C_j(f)=\sum_{\deg h=j}\left(\frac hf\right),\qquad
 S_5(f)=\sum_{D\in\mathcal H_5(q)}\left(\frac Df\right).
\]

Expanding

\[
 \mu^2(D)=\sum_{A^2\mid D}\mu(A),\qquad D=A^2B,
\]

leaves \(\deg A=0,1,2\). The corresponding signed coprime counts are

\[
 1,\qquad -(q-\ell),\qquad
 \binom{q-\ell}{2}-\left(\frac{q(q-1)}2-k\right)
 =\binom{\ell+1}{2}+k-q\ell.
\]

Therefore, independently of \(d\),

\[
\boxed{
 S_5(f)=C_5(f)-(q-\ell(f))C_3(f)
 +\left(\binom{\ell(f)+1}{2}+k(f)-q\ell(f)\right)C_1(f).}
                                                                    \tag{3}
\]

The producer derives the last polynomial identity in the exact ring
\(\mathbf Q[q,\ell,k]\); it is not accepted as a string fixture.

## 2. Completed functional-equation algebra

Let \(d=2m+2\). The quadratic character modulo squarefree \(f\) is primitive
and even, so

\[
 L_f(u)=(1-u)Q_f(u),\qquad \deg Q_f=2m.
\]

Writing \(Q_f(u)=\sum_{j=0}^{2m}Q_ju^j\), the completed functional equation is

\[
 Q_{2m-j}=q^{m-j}Q_j\qquad(0\le j\le m),                         \tag{4}
\]

and coefficient comparison gives

\[
 C_j=Q_j-Q_{j-1},\qquad Q_j=1+C_1+\cdots+C_j
 \quad(j\le m).                                                  \tag{5}
\]

Equations (4)--(5) give the rows in (1):

- \(d=6\), \(m=2\): \(Q_5=0\) and \(Q_4=q^2\), hence
  \(C_5=-q^2\).
- \(d=8\), \(m=3\): \(Q_5=q^2Q_1\) and \(Q_4=qQ_2\), hence
  \(C_5=q(q-1)(1+C_1)-qC_2\).
- \(d=10\), \(m=4\): \(Q_5=qQ_3\), while \(Q_4\) is central, hence
  \(C_5=(q-1)(1+C_1+C_2+C_3)-C_4\).
- \(d=12\), \(m=5\): \(Q_5\) itself is central and free, so
  \(C_5=Q_5-(1+C_1+\cdots+C_4)\).
- \(d\ge14\): \(Q_5\) lies below the center and is again a free completed
  coefficient.

The producer constructs these expressions in an exact sparse-polynomial
ring over \(q,C_1,\ldots,C_4,Q_5\) for every even
\(d=2,4,\ldots,20\). The support of \(Q_5\) first appears exactly at
\(d=12\).

### An explicit non-determination witness

For \(m\ge5\), consider the two formal completed polynomials

\[
 Q^{(0)}(u)=1+q^m u^{2m}                                      \tag{6}
\]

and

\[
 Q^{(1)}(u)=
 \begin{cases}
 1+u^5+q^5u^{10},&m=5,\\
 1+u^5+q^{m-5}u^{2m-5}+q^mu^{2m},&m>5.
 \end{cases}                                                    \tag{7}
\]

Both satisfy (4). For \(L^{(i)}=(1-u)Q^{(i)}\), their coefficients agree at

\[
 (C_0,C_1,C_2,C_3,C_4)=(1,-1,0,0,0),
\]

but \(C_5^{(0)}=0\) and \(C_5^{(1)}=1\). This proves that the completed
functional equation does not determine \(C_5\) from the first five
coefficients once \(d\ge12\).

This witness is deliberately only a formal functional-equation witness. No
claim is made that either polynomial is realized by a quadratic character,
a curve, or a pure Frobenius spectrum.

## 3. Why reciprocity becomes self-referential

All polynomial sums in this section are over **monic** polynomials. For any
monic \(h\), define

\[
 G_h(z)=\prod_P\left(1-\left(\frac Ph\right)z^{\deg P}\right)
       =\sum_{n\ge0}g_n(h)z^n,
 \qquad
 G_j^{(d)}=\sum_{\deg h=j}g_d(h).                               \tag{8}
\]

For squarefree degree-\(d\) polynomials \(f\), define

\[
 \lambda_d(h)=\sum_{\deg f=d}\mu(f)\ell(f)\left(\frac hf\right),
 \quad
 \lambda_d^{[2]}(h)=\sum_{\deg f=d}\mu(f)
       \binom{\ell(f)}2\left(\frac hf\right),
 \quad
 \kappa_d(h)=\sum_{\deg f=d}\mu(f)k(f)\left(\frac hf\right).
\]

Then the two marked rows are exactly

\[
 \Lambda_3^{(d)}=\sum_{\deg h=3}\lambda_d(h),
 \qquad
 Q_1^{(d)}=\sum_{\deg h=1}
 \bigl(\lambda_d^{[2]}+\lambda_d+\kappa_d-q\lambda_d\bigr)(h).
\]

If \(d\) is even, polynomial quadratic reciprocity has sign \(+1\), because
\(d\deg h\) is even. Summing (3) over squarefree degree-\(d\) polynomials
\(f\) therefore gives, before using the functional equation,

\[
 T_d:=\sum_{D\in\mathcal H_5(q)}r_D(d)
 =G_5^{(d)}-qG_3^{(d)}+\Lambda_3^{(d)}+Q_1^{(d)}.                \tag{9}
\]

Split the degree-five row into squarefree and nonsquarefree moduli:

\[
 G_5^{(d)}=
 \sum_{\substack{D\text{ squarefree}\\\deg D=5}}g_d(D)
 +\sum_{\substack{h\text{ nonsquarefree}\\\deg h=5}}g_d(h)
 =T_d+R_5^{(d)}.                                                 \tag{10}
\]

The second equality is exact: for squarefree \(D\), expanding (8) gives

\[
 g_d(D)=\sum_{\deg f=d}\mu(f)\left(\frac fD\right)
       =\sum_{\deg f=d}\mu(f)\left(\frac Df\right)=r_D(d),     \tag{11}
\]

where the middle equality again uses even-degree reciprocity.

Substitution of (10) into (9) cancels \(T_d\) and leaves only

\[
\boxed{
 R_5^{(d)}-qG_3^{(d)}+\Lambda_3^{(d)}+Q_1^{(d)}=0.}             \tag{12}
\]

The producer verifies the target coefficient is exactly zero in a second
sparse-polynomial ring. Equation (12) is a useful consistency check on the
nonsquarefree and lower-degree Euler rows, but it contains no value of
\(T_d\).

## 4. The last pre-boundary rows

Let \(M_d=\sum_{\deg f=d}\mu(f)\). The polynomial Euler product gives

\[
 \sum_f\mu(f)u^{\deg f}=1-qu,
\]

so \(M_d=0\) for \(d\ge2\). Also \(G_1^{(d)}=G_2^{(d)}=0\) for
\(d\ge1\): the linear inverse \(L\)-series is \(1\), while the degree-two
aggregate is

\[
 q(q-1)\cdot1+q(1-q)=0.                                        \tag{13}
\]

Thus the explicit \(C_5\) rows before the boundary are

\[
\begin{array}{c|c|c}
d&C_5\text{ aggregate}&\text{one-step descent}\\ \hline
6&-q^2M_6=0&T_6=-qG_3+\Lambda_3+Q_1,\\
8&q(q-1)(M_8+G_1)-qG_2=0&T_8=-qG_3+\Lambda_3+Q_1,\\
10&(q-1)(M_{10}+G_1+G_2+G_3)-G_4&
T_{10}=(q-1)(G_1+G_2)-G_3-G_4+\Lambda_3+Q_1.
\end{array}                                                     \tag{14}
\]

The \(d=6\) and \(d=8\) rows are independently derived and then checked
against source-locked canonical packets. The \(d=10\) row is independently
derived; the untracked \(\operatorname{Sym}^{10}\) draft present during construction was
not imported or source-locked.

## 5. Scope and interpretation

The boundary is methodological, not epistemic:

- It proves exactly where this one-step reciprocal descent first feeds the
  target back into itself.
- It does not rule out aggregate identities that eliminate \(G_5\) by some
  additional theorem.
- It does not rule out a second descent, a refined marked sieve, point-count
  geometry, automorphic trace formulas, or cohomological calculations.
- It makes no memberwise sign, RH, GRH, motive, compatible-system, or global
  Euler-product claim.

This is best read as a planning theorem: future higher-symmetric-power work
should not merely extend the \(d=6,8,10\) algebra mechanically. It needs a
new input precisely at the squarefree degree-five part of \(G_5\).

## 6. Replay, caps, and provenance

From the repository root:

```text
python research/l-families/atlas/function_field/genus2_reciprocal_descent_boundary.py --check
python -O research/l-families/atlas/function_field/genus2_reciprocal_descent_boundary.py --check
python -m unittest tests.test_genus2_reciprocal_descent_boundary
python -O -m unittest tests.test_genus2_reciprocal_descent_boundary
ruff check research/l-families/atlas/function_field/genus2_reciprocal_descent_boundary.py tests/test_genus2_reciprocal_descent_boundary.py
```

The producer is capped at endpoint \(20\), 2,048 exact symbolic operations,
32 imported source atoms, 65,536 source bytes, and three wall-clock seconds.
The canonical replay currently uses far less than those caps.

The only imported packets are the committed, exact \(\operatorname{Sym}^{6}\)
and \(\operatorname{Sym}^{8}\) marked-trace JSON fixtures. Their LF-normalized file hashes,
canonical payload hashes, and audited commits are embedded in the output.
They are loaded only after the formal phase panel and self-reference
certificate have closed.
