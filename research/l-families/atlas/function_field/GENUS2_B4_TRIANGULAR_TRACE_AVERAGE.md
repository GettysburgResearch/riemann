# Genus-two B4 triangular trace average

Status: **PROVED exactly for every odd prime power**.

Scope: for

\[
 \mathcal H_5(q)=\{D\in\mathbf F_q[T]:D\text{ monic, squarefree, }\deg D=5\},
\]

this packet evaluates \(\sum_D b_D^4\), closes the last triangular
weight-eight character channel, and proves the marked-stack trace
\(T_{0,4}(q)\).  The default replay enumerates no field, polynomial, curve,
or family member.

Exact dependencies: the source-locked 54-signature ledger in
`genus2_second_moment_reduction.json`; the lower moment and
\(\chi_{0,3}\) theorem in `GENUS2_B3_PRIMITIVE_TRACE_AVERAGE.md`; the
\(\chi_{2,2}\) theorem in `GENUS2_M22_TRIANGULAR_TRACE_AVERAGE.md`; and the
eight-channel formal inventory in
`GENUS2_THIRD_ORDER_PRIMITIVE_INVENTORY.md`.  Packet B never assigns guessed
values to Packet A's level-two residuals.

## 1. The theorem

For every odd prime power \(q\),

\[
\boxed{
\sum_{D\in\mathcal H_5(q)}b_D^4
=q(q-1)\bigl(
10q^7-29q^6+21q^5+44q^4-47q^3-56q^2-10q-1
\bigr).}                                                        \tag{1}
\]

Since \(|\mathcal H_5(q)|=q^4(q-1)\),

\[
\boxed{
\mathbb E[b_D^4]
=\frac{10q^7-29q^6+21q^5+44q^4-47q^3-56q^2-10q-1}{q^3}.}       \tag{2}
\]

The exact pointwise triangular identity is

\[
\begin{aligned}
R_4
&=\chi_{0,4}+3\chi_{2,2}+4\chi_{0,3}\\
&=\frac{b^4}{q^4}-\frac{5a^2b}{q^2}-\frac{2a^4}{q^2}
  +\frac{14a^2}{q}-\frac{3b^2}{q^2}-2.
\end{aligned}                                                       \tag{3}
\]

Substituting (1), the proved lower moments, and the source-locked
\(\chi_{0,3}\) and \(\chi_{2,2}\) laws gives

\[
\boxed{\langle\chi_{0,4}\rangle_q=-\frac{2q^2+1}{q^7}.}           \tag{4}
\]

For the marked-Weierstrass stack normalization

\[
T_{0,4}(q)=\frac{q^4}{q(q-1)}
\sum_{D\in\mathcal H_5(q)}\chi_{0,4}(D),
\]

the denominator-free result is therefore

\[
\boxed{T_{0,4}(q)=-(2q^2+1).}                                     \tag{5}
\]

## 2. Exact 54-signature reweight

The four ordered monic-quadratic slots have 54 factor-exponent signatures.
Their radical-degree census is

| radical degree | 0 | 2 | 4 | 6 | 8 |
|---:|---:|---:|---:|---:|---:|
| signatures | 9 | 16 | 17 | 7 | 5 |

The weighted type-count polynomial is exactly \(q^8\).  For one signature,
let \(C_j\) be the degree-\(j\) coefficient of its imprimitive quadratic
character \(L\)-polynomial.  The squarefree degree-five sieve is

\[
S_5=C_5-(q-L)C_3+
\left(-Lq+\binom{L+1}{2}+Q\right)C_1,                              \tag{6}
\]

where \(L,Q\) are the numbers of distinct linear and irreducible-quadratic
primes in the denominator.  The producer evaluates (6) in every row and
then applies its exact ordered-tuple weight.

For radical degree eight, if

\[
P_r(u)=1+p_1u+p_2u^2+p_3u^3+qp_2u^4+q^2p_1u^5+q^3u^6,
\]

then the even-character polynomial is \((1-u)P_r(u)\), so

\[
C_1=p_1-1,\qquad C_3=p_3-p_2,\qquad C_5=q^2p_1-qp_2.              \tag{7}
\]

The degree-six and degree-four deletion rows use exactly the marked
correlations proved in Packet A.  Degree two reduces to elementary sign
inventories, and degree zero is principal.  No finite-field specialization
enters this calculation.

## 3. What really happens to the level-two channels

Packet A deliberately retained the eight independent formal moments

\[
M_{111,2j},\ M_{12,2j}\qquad(j=1,2,3,4),                           \tag{8}
\]

where `111` denotes a fully split squarefree cubic and `12` denotes a linear
factor times an irreducible quadratic.  The 54-row reweight gives the exact
coefficient table

| residual | coefficient |
|---|---:|
| \(M_{111,2}\) | \(252q^2-3096q+8274\) |
| \(M_{12,2}\) | \(84q^2-960q+2286\) |
| \(M_{111,4}\) | \(234-27q\) |
| \(M_{12,4}\) | \(78-9q\) |
| \(M_{111,6},M_{12,6},M_{111,8},M_{12,8}\) | \(0\) |

Thus the genuinely dangerous sixth and eighth moments cancel identically.
The fourth-moment coefficients satisfy

\[
234-27q=3(78-9q),                                                  \tag{9}
\]

so the only surviving fourth-order quantity is

\[
3M_{111,4}+M_{12,4}.                                               \tag{10}
\]

This is not an arbitrary level-two moment.  A split cubic has three rational
roots and a `12` cubic has one, so (10) is exactly the fourth moment of the
cubic family with one rational root marked.  The computation therefore
descends from the full factorization-stratified basis to a
\(\Gamma_1(2)=\Gamma_0(2)\)-type marked-root family before evaluating the
survivor.

## 4. Marked-root moment lemma

The exact low-order identities needed by the descent are

\[
\boxed{
M_{111,2}=\frac{q(q-1)(q-3)(q+1)}6,
\qquad
M_{12,2}=\frac{q(q-1)^2(q+1)}2,}                                  \tag{11}
\]

and

\[
\boxed{
3M_{111,4}+M_{12,4}
=2q(q-1)(q+1)(q^2-2q-1).}                                         \tag{12}
\]

Here is a direct character-sum proof.

### 4.1 Fully split second moment

For the Legendre cubic \(x(x-1)(x-\lambda)\), put

\[
A_\lambda=\sum_x\chi(x(x-1)(x-\lambda)).
\]

Expanding the square and summing over \(\lambda\) uses only

\[
\sum_t\chi((t-a)(t-b))=
\begin{cases}q-1,&a=b,\\-1,&a\ne b.\end{cases}                    \tag{13}
\]

The two singular parameters \(0,1\) each contribute one, giving

\[
\sum_{\lambda\ne0,1}A_\lambda^2=q^2-2q-3=(q-3)(q+1).              \tag{14}
\]

An ordered affine normalization of three roots has \(q(q-1)\) choices, and
each unordered split cubic has six orderings.  This proves the first formula
in (11).

### 4.2 The translated marked-root family

After translating the marked root to zero, write

\[
f_{u,v}(X)=X(X^2+uX+v),\qquad
S(u,v)=\sum_x\chi(f_{u,v}(x)).                                    \tag{15}
\]

The squarefree locus is \(v\ne0\) and \(u^2\ne4v\).  Before removing these
two singular divisors, two-variable character orthogonality gives

\[
\sum_{u,v}S(u,v)^2=q(q-1)^2.                                      \tag{16}
\]

Each singular divisor contributes \(q-1\) to a positive even moment and
their intersection contributes zero.  Hence the valid second moment per
marked root is \((q-1)(q+1)(q-2)\).  Multiplication by the \(q\) possible
roots gives

\[
3M_{111,2}+M_{12,2}=q(q-1)(q+1)(q-2),                              \tag{17}
\]

which, with the first formula in (11), proves the second.

For the fourth moment, classify the ordered \(x\)-quadruple in the expansion
of \(S^4\) by multiplicity partition.  The exact unrestricted contributions
are

| partition | contribution |
|---|---:|
| `4` | \(q(q-1)^2\) |
| `31` | \(0\) |
| `22` | \(3(q-1)^3(q-2)\) |
| `211` | \(-6(q-1)(q-3)\) |
| `1111` | \(3q(q-1)(q-3)-(q-1)(q-4)(q^2-2q-3)\) |

The first four rows follow immediately from (13).  For the all-distinct row,
use two of the four affine forms

\[
X_i^2+uX_i+v
\]

as coordinates.  The remaining two forms give the usual cross-ratio
quadratic Jacobi sum.  Its constant part is \(3q(q-1)(q-3)\); its trace part
is \(-(q-1)(q-4)\sum_{\lambda\ne0,1}A_\lambda^2\).  Equation (14) gives the
displayed `1111` row.  This step uses only the Legendre *second* moment; no
factorization-stratified fourth moment is assumed.

Adding the five rows gives

\[
\sum_{u,v}S(u,v)^4=2q(q-1)(q^2-q-3).                              \tag{18}
\]

Subtracting \(2(q-1)\) for the two singular divisors and multiplying by the
\(q\) possible marked roots proves (12).

## 5. Held-out falsification controls

Two additional exact prime-field computations were performed independently
of the symbolic proof:

| \(q\) | \(\chi_q(-1)\) | squarefree quintics | observed \(\sum b_D^4\) | candidate difference |
|---:|---:|---:|---:|---:|
| 11 | -1 | 146,410 | 16,219,859,920 | 0 |
| 13 | +1 | 342,732 | 77,445,995,952 | 0 |

They used batched exact \(\mathbf F_q/\mathbf F_{q^2}\) character
evaluation and took under two seconds together on the development machine.
The producer records explicit maximum character-evaluation atom counts.
These rows sample both reciprocity branches, but they are held-out
falsification controls only: neither value is read by the theorem algebra.

## 6. Replay and firewalls

From the successor worktree root:

    python research/l-families/atlas/function_field/genus2_b4_triangular_trace_average.py --check
    python -O research/l-families/atlas/function_field/genus2_b4_triangular_trace_average.py --check
    python -m unittest tests.test_genus2_b4_triangular_trace_average
    python -O -m unittest tests.test_genus2_b4_triangular_trace_average

The default replay uses exact `Fraction` polynomial algebra, all 54 source
signatures, all 12 primitive rows, and all 13 marked-deletion rows under a
4096 operation-plus-input-atom cap and a five-second wall cap.  It performs
no interpolation.  Equations (1)--(5) make no novelty, memberwise sign, RH,
or GRH claim.
