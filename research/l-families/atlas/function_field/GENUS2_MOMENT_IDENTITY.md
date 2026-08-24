# Exact genus-two squarefree-quintic moment identity

Status: exact theorem proved in this DRAFT research packet; an independent
read-only derivation audit found no mathematical gap. It is not yet a frozen
integrated theorem node.

Scope: every odd prime power \(q\); all monic squarefree quintics over
\(\mathbf F_q\). The proof does not use the scans at \(q=3,5,7\).

Exact dependencies: polynomial quadratic reciprocity, polynomial Moebius
inversion, and the standard exact form of the \(L\)-polynomial of a primitive
even quadratic character of conductor degree two or four. The latter is
recalled below through the zeta function of \(Y^2=r(T)\); no zero bound or
equidistribution theorem is used.

What was actually run: the standard-library certificate
`genus2_moment_identity.py` checks the finite algebra in \(\mathbf Q[q]\).
It performs no finite-field or family enumeration.

Smallest remaining gap: translate the proof into a proof assistant or obtain a
frozen-head review before integration. No unproved asymptotic, equidistribution,
or scan-to-all-\(q\) step occurs in the statement below.

## The theorem

Let \(q\) be an odd prime power, let \(\chi\) and \(\chi_2\) be the quadratic
characters of \(\mathbf F_q\) and \(\mathbf F_{q^2}\), extended by zero, and
let

\[
 \mathcal H_5=
 \{D\in\mathbf F_q[T]:D\text{ monic, squarefree, and }\deg D=5\}.
\]

For \(D\in\mathcal H_5\), put

\[
 a_D=\sum_{x\in\mathbf F_q}\chi(D(x)),\qquad
 b_D=\frac{\displaystyle\sum_{z\in\mathbf F_{q^2}}\chi_2(D(z))+a_D^2}{2},
 \qquad K_D=q a_D^2-b_D^2.
\]

Then \(\#\mathcal H_5=q^5-q^4=q^4(q-1)\), and

\[
 \boxed{\mathbb E_{\mathcal H_5}[a_D^2]
 =q-1+\frac{q^2+q-2}{q^3}},
\]

\[
 \boxed{\mathbb E_{\mathcal H_5}[b_D^2]
 =2q^2-3q+2+\frac{q^2-3q-1}{q^3}},
\]

and consequently

\[
 \boxed{\mathbb E_{\mathcal H_5}[K_D]
 =-(q-1)^2+\frac{q+1}{q^3}}.
\]

These are identities for the full family, not asymptotic statements.

## Character conventions and low-degree \(L\)-polynomials

For a monic irreducible \(P\), define

\[
 \left(\frac{F}{P}\right)=
 \begin{cases}
 0,&P\mid F,\\
 (F\bmod P)^{(|P|-1)/2}\in\{\pm1\},&P\nmid F,
 \end{cases}
\]

where \(|P|=q^{\deg P}\), and the second value is identified with \(\pm1\)
in the residue field. For
monic \(h\), extend this multiplicatively in the denominator:

\[
 \left(\frac{F}{h}\right)
 =\prod_P\left(\frac{F}{P}\right)^{v_P(h)}.
\]

Thus the symbol is zero when \((F,h)\ne1\), including when an exponent in
\(h\) is even. For coprime monic \(F,G\), polynomial quadratic reciprocity is

\[
 \left(\frac{F}{G}\right)
 \left(\frac{G}{F}\right)
 =(-1)^{((q-1)/2)\deg F\deg G}.
\]

Every interchange used below has degree product even, so its reciprocity sign
is \(+1\). Correlations between two linear factors are evaluated in their
displayed orientation and are not silently interchanged.

For a monic \(h\), set

\[
 r(h)=\prod_{v_P(h)\ {\rm odd}}P.
\]

If \(r(h)\ne1\), the underlying primitive quadratic character has squarefree
conductor \(r(h)\). On polynomials coprime to \(h\), the character modulo
\(h\) equals the character modulo \(r(h)\); primes in the support of \(h\) but
not \(r(h)\) merely delete Euler factors. With

\[
 L_h(u)=\sum_{F\ {\rm monic}}\left(\frac Fh\right)u^{\deg F},
\]

the exact deletion formula is

\[
 L_h(u)=L_{r(h)}(u)
 \prod_{\substack{P\mid\operatorname{rad}(h)\\P\nmid r(h)}}
 \left(1-\left(\frac{P}{r(h)}\right)u^{\deg P}\right).
\tag{1}
\]

All nonprincipal conductors below have even degree. Indeed, for
\(c\in\mathbf F_q^\times\),

\[
 \left(\frac{c}{r}\right)=\chi(c)^{\deg r},
\]

so these primitive characters are even, meaning trivial on constants.

We use the following exact low-degree lemma.

**Even quadratic \(L\)-polynomial lemma.** If \(r\) is monic, squarefree,
and the primitive quadratic character modulo \(r\) is nontrivial and even,
then

\[
 \deg r=2\implies L_r(u)=1-u,
\tag{2}
\]

and

\[
 \deg r=4\implies L_r(u)=(1-u)(1+c_r u+q u^2)
\tag{3}
\]

for an integer \(c_r\). In particular, the coefficient of \(u^3\) in (3) is
always \(-q\).

Here is the exact justification, including the sign in (3). Primitivity
follows locally from squarefreeness and the nontrivial quadratic character at
each prime of \(r\). Evenness supplies the factor \(1-u\). The smooth
projective curve \(Y^2=r(T)\) has two \(\mathbf F_q\)-rational points above
infinity because \(\deg r\) is even and the leading coefficient is the square
\(1\). Comparing its closed-point Euler product with the finite Dirichlet
Euler product gives

\[
 L_r(u)=(1-u)P_r(u),
\]

where \(P_r\) is the numerator of the curve zeta function. For degree two the
curve has genus zero, so \(P_r=1\). For degree four it has genus one, and the
exact zeta functional equation gives \(P_r(u)=1+c_r u+q u^2\). Only its
degree, constant coefficient, and leading coefficient are used; no estimate
for \(c_r\) is needed. An explicit even-degree reference for the trivial
factor and completed functional equation is H. Jung,
[“Note on the mean value of \(L(1/2,\chi)\) in the hyperelliptic
ensemble”](https://doi.org/10.1016/j.jnt.2013.02.005), *Journal of Number
Theory* 133 (2013), Section 2.2. Its \(2g+2\) formula at \(g=1\) gives (3).

## Rewriting \(b_D\) as a degree-two character sum

Let \(\mathcal M_n\) denote the monic degree-\(n\) polynomials. If
\(v_x=\chi(D(x))\), then every nonzero element of \(\mathbf F_q\) is a square
in \(\mathbf F_{q^2}\), and hence

\[
 \chi_2(D(x))=v_x^2\qquad(x\in\mathbf F_q).
\]

The points of \(\mathbf F_{q^2}\setminus\mathbf F_q\) occur in conjugate
pairs, one pair for each monic irreducible quadratic \(Q\). If \(z\) is a
root of \(Q\), then \(\chi_2(D(z))=(D/Q)\). Consequently

\[
 \sum_{z\in\mathbf F_{q^2}}\chi_2(D(z))
 =\sum_xv_x^2+
 2\sum_{\substack{Q\ {\rm monic\ irreducible}\\\deg Q=2}}
 \left(\frac{D}{Q}\right).
\]

Combining this with
\(a_D^2=\sum_xv_x^2+2\sum_{x<y}v_xv_y\), and partitioning monic quadratics
into \(L^2\), \(LM\) with \(L\ne M\), and irreducible \(Q\), gives

\[
 \boxed{b_D=\sum_{f\in\mathcal M_2}\left(\frac{D}{f}\right)}.
\tag{4}
\]

This also proves directly that the displayed definition of \(b_D\) is an
integer.

## The \(a_D^2\) moment

The untwisted squarefree Euler product first gives the family size:

\[
 \sum_{D\ {\rm monic\ squarefree}}u^{\deg D}
 =\prod_P(1+u^{\deg P})
 =\frac{1-q u^2}{1-q u},
\]

whose degree-five coefficient is \(q^5-q^4\).

Fix a monic linear \(L=T-x\). The diagonal sum is the number of squarefree
quintics not divisible by \(L\), because
\(\chi(D(x))^2=1_{L\nmid D}\). Its squarefree Euler product is

\[
 A=[u^5]\frac{1-q u^2}{(1-q u)(1+u)}
 =q^5-2q^4+2q^3-2q^2+2q-1.
\tag{5}
\]

For distinct \(x,y\), let
\(\psi(F)=(F/(T-x)(T-y))\). This is a primitive even quadratic character of
conductor degree two, so \(L(u,\psi)=1-u\) by (2). The twisted squarefree
Euler product is therefore

\[
 \begin{aligned}
 B
 &=\sum_{D\in\mathcal H_5}\psi(D)\\
 &=[u^5]\prod_P(1+\psi(P)u^{\deg P})\\
 &=[u^5]\frac{(1-u)(1-q u^2)}{(1-u^2)^2}
 =2q-3.
 \end{aligned}
\tag{6}
\]

The factor \((1-q u^2)/(1-u^2)^2\) in (6) is
\(\prod_{P\nmid(T-x)(T-y)}(1-u^{2\deg P})\). There are \(q\) diagonal and
\(q(q-1)\) ordered off-diagonal pairs, so (5)--(6) give

\[
 \begin{aligned}
 \sum_{D\in\mathcal H_5}a_D^2
 &=qA+q(q-1)B\\
 &=q^4(q-1)^2+q(q-1)(q^2+q-2).
 \end{aligned}
\tag{7}
\]

Dividing (7) by \(q^4(q-1)\) proves the first claimed mean.

## Squarefree sieve for the \(b_D^2\) moment

For a monic quartic \(h\), write

\[
 C_n(h)=\sum_{B\in\mathcal M_n}\left(\frac{B}{h}\right),
\]

and let \(\ell(h)\) and \(k(h)\) be the numbers of distinct linear and
irreducible-quadratic primes in the support of \(h\). Polynomial Moebius
inversion, with \(D=A^2B\), gives

\[
 \begin{aligned}
 S(h)&:=\sum_{D\in\mathcal H_5}\left(\frac{D}{h}\right)\\
 &=C_5(h)-(q-\ell(h))C_3(h)\\
 &\quad+
 \left(\binom{\ell(h)+1}{2}+k(h)-q\ell(h)\right)C_1(h).
 \end{aligned}
\tag{8}
\]

For completeness, the degree-one Moebius coefficient in (8) is
\(-(q-\ell)\). The degree-two coefficient is extracted from

\[
 \sum_{(A,h)=1}\mu(A)t^{\deg A}
 =\frac{1-qt}{\prod_{P\mid h}(1-t^{\deg P})},
\]

and is exactly \(\binom{\ell+1}{2}+k-q\ell\). No term of higher degree can
occur because \(\deg D=5\).

By (4),

\[
 \sum_{D\in\mathcal H_5}b_D^2
 =\sum_{f,g\in\mathcal M_2}S(fg)
 =\sum_{\deg h=4}w(h)S(h),
\tag{9}
\]

where \(w(h)\) is the number of monic degree-two divisors of \(h\). Thus
\(w(h)\) is exactly the multiplicity of \(h=fg\) among ordered pairs
\((f,g)\).

## The nine quartic rows

Let

\[
 I=\frac{q(q-1)}2
\]

be the number of monic irreducible quadratics. In the table, letters
\(L,M,N,R\) denote distinct monic linears whenever they occur together, and
\(Q,Q_1,Q_2\) denote monic irreducible quadratics, with \(Q_1\ne Q_2\).
The \(C_3\) column is the value for each \(h\) of the displayed type. The
boldfaced \(\sum C_1\) column is the aggregate over all \(h\) of that type.
This distinction is used in the correction algebra.

In the same row order, the primitive conductors \(r(h)\) are
\(1,1,1,LM,Q,LM,Q_1Q_2,QLM,LMNR\). Thus every nontrivial conductor is
squarefree of even degree, exactly as required by (2)--(3).

| Type of \(h\) | Number of \(h\) | \(w\) | \((\ell,k)\) | \(C_3(h)\) | **\(\sum C_1(h)\)** | \(C_5(h)\) |
|---|---:|---:|---:|---:|---:|---:|
| \(L^4\) | \(q\) | 1 | \((1,0)\) | \(q^2(q-1)\) | \(q(q-1)\) | \(q^4(q-1)\) |
| \(L^2M^2\) | \(\binom q2\) | 3 | \((2,0)\) | \(q(q-1)^2\) | \(\binom q2(q-2)\) | \(q^3(q-1)^2\) |
| \(Q^2\) | \(I\) | 1 | \((0,1)\) | \(q^3-q\) | \(Iq\) | \(q^3(q^2-1)\) |
| \(L^3M\) | \(q(q-1)\) | 2 | \((2,0)\) | \(0\) | \(-q(q-1)\) | \(0\) |
| \(QL^2\) | \(qI\) | 2 | \((1,1)\) | \(0\) | \(-q(q-1)^2/2\) | \(0\) |
| \(LMN^2\) | \(\binom q2(q-2)\) | 4 | \((3,0)\) | \(0\) | \(-q(q-1)(q-3)/2\) | \(0\) |
| \(Q_1Q_2\) | \(\binom I2\) | 2 | \((0,2)\) | \(-q\) | \(-q(q^2-1)/8\) | \(0\) |
| \(QLM\) | \(I\binom q2\) | 2 | \((2,1)\) | \(-q\) | \(q(q-1)^2/4\) | \(0\) |
| \(LMNR\) | \(\binom q4\) | 6 | \((4,0)\) | \(-q\) | \(q(q-1)(q-3)/8\) | \(0\) |

These are all quartics possessing a monic quadratic divisor; hence the table
is exhaustive for (9). The weights follow by listing the degree-two divisors.

Here is an audit of every character-sum entry. If \(h\) is a square, its
character is principal with the primes in \(\operatorname{rad}(h)\) excluded.
Thus its generating function is

\[
 \sum_{n\ge0}C_n(h)u^n
 =\frac{\prod_{P\mid h}(1-u^{\deg P})}{1-qu},
\tag{10}
\]

which gives the first three rows. If \(h\) is not a square, its character is
nonprincipal. Monic quintics cover every residue class modulo the monic
quartic \(h\) exactly \(q\) times, so complete character cancellation gives
\(C_5(h)=0\).

For \(L^3M\), (2) gives \(L_h(u)=1-u\). For \(QL^2\) and \(LMN^2\),
(1)--(2) give

\[
 L_h(u)=(1-u)(1-\varepsilon u),\qquad\varepsilon\in\{\pm1\},
\]

so \(C_3(h)=0\) and \(C_1(h)=-(1+\varepsilon)\). Finally, the three
squarefree quartic rows are primitive even conductor-degree-four characters,
and (3) gives \(C_3(h)=-q\).

It remains only to audit the aggregate \(C_1\) values. Put \(n=(q-1)/2\).
For a fixed monic linear \(B\), the \(q-1\) values \((B/L)\), with \(L\ne B\),
consist of \(n\) plus signs and \(n\) minus signs. Consequently their
elementary-symmetric generating polynomial is

\[
 \prod_{L\ne B}\left(1+\left(\frac BL\right)t\right)
 =(1-t^2)^n,
\tag{11}
\]

so \(e_2=-n\) and \(e_4=\binom n2\). Also

\[
 \sum_{\deg Q=2\ {\rm irreducible}}\left(\frac BQ\right)=-n.
\tag{12}
\]

To prove (12), evaluate all monic quadratics at the root of \(B\). Their
total quadratic-character sum is zero. Reducible quadratics are multisets of
two monic linears: squares contribute \(q-1\), and distinct pairs contribute
\(e_2=-n\). Their total is \(n\), leaving \(-n\) for the irreducibles.
Reciprocity between \(B\) and \(Q\) has sign \(+1\) because the degree product
is two.

Now:

- \(L^3M\) has \(C_1=-1\), the standard distinct-root quadratic
  correlation.
- Summing \(C_1(QL^2)=-1-(L/Q)\), and using (12), gives
  \(-qI+I=-q(q-1)^2/2\).
- For fixed \(N\), summing \(C_1(LMN^2)=-1-(N/L)(N/M)\) over pairs
  \(L,M\ne N\), and using \(e_2=-n\), gives
  \(-\binom{q-1}{2}+n=-(q-1)(q-3)/2\). Multiply by \(q\).
- For \(Q_1Q_2\), fixing \(B\) and using (12) gives
  \(e_2=((-n)^2-I)/2=-(q^2-1)/8\). Multiply by \(q\).
- For \(QLM\), fixing \(B\) gives the product \((-n)(-n)=n^2\) of the
  quadratic sum (12) and the linear-pair sum from (11). Multiply by \(q\).
- For \(LMNR\), fixing \(B\) gives \(e_4=\binom n2\) from (11). Multiply
  by \(q\).

This proves every entry of the table. It also covers \(q=3\): rows whose
combinatorial count vanishes simply contribute zero.

## Explicit \(T_0\) and correction algebra

Let \(T_0=\sum_h w(h)C_5(h)\). Only the three square rows contribute, and

\[
 \begin{aligned}
 T_0
 &=q\,q^4(q-1)
 +3\binom q2 q^3(q-1)^2
 +I q^3(q^2-1)\\
 &=q^4(q-1)
 \left(q+\frac32(q-1)^2+\frac12(q^2-1)\right)\\
 &=q^4(q-1)(2q^2-2q+1).
 \end{aligned}
\tag{13}
\]

Let \(\Delta\) be the contribution of the last two terms of (8). For a row
\(\tau\), whose displayed \(C_1\) is already aggregated, its contribution is

\[
 \Delta_\tau=w_\tau\left[
 -(q-\ell_\tau)\#(\tau)C_{3,\tau}
 +\left(\binom{\ell_\tau+1}{2}+k_\tau-q\ell_\tau\right)
 \sum_{h\in\tau}C_1(h)\right].
\tag{14}
\]

Substitution of the nine rows into (14) gives, in the order of the table,

\[
\begin{array}{rcl}
\Delta_{L^4}&=&-q(q-1)^2(q^2+1),\\
\Delta_{L^2M^2}&=&3I(q-2)\bigl[-q(q-1)^2+3-2q\bigr],\\
\Delta_{Q^2}&=&Iq(-q^3+q+1),\\
\Delta_{L^3M}&=&2q(q-1)(2q-3),\\
\Delta_{QL^2}&=&q(q-1)^2(q-2),\\
\Delta_{LMN^2}&=&6q(q-1)(q-2)(q-3),\\
\Delta_{Q_1Q_2}&=&2q^2\binom I2-\dfrac{q(q^2-1)}2,\\
\Delta_{QLM}&=&2q(q-2)I^2-q(q-2)(q-1)^2,\\
\Delta_{LMNR}&=&6q(q-4)\binom q4
+\dfrac32(5-2q)q(q-1)(q-3).
\end{array}
\tag{15}
\]

Expanding and collecting (15), or checking the same identity coefficient by
coefficient in \(\mathbf Q[q]\), yields

\[
 \Delta=-q(q-1)(q^4-q^3-q^2+3q+1).
\tag{16}
\]

The accompanying certificate stores the nine counts, weights,
\((\ell,k)\), \(C_3\), aggregate \(C_1\), and \(C_5\) values independently;
reconstructs every line of (15); and verifies (13) and (16) as polynomial
identities rather than by interpolation.

Combining (13) and (16) gives

\[
 \begin{aligned}
 \sum_{D\in\mathcal H_5}b_D^2
 &=q^4(q-1)(2q^2-3q+2)\\
 &\qquad+q(q-1)(q^2-3q-1).
 \end{aligned}
\tag{17}
\]

Division by \(q^4(q-1)\) proves the second claimed mean. Finally, by the
definition of \(K_D\), equations (7) and (17) give

\[
 \mathbb E[K_D]
 =q\mathbb E[a_D^2]-\mathbb E[b_D^2]
 =-(q-1)^2+\frac{q+1}{q^3},
\]

which completes the proof.

## Scope firewall and replay

This theorem concerns a finite family of function-field quadratic
\(L\)-polynomials for each odd prime power \(q\). It is not an assertion about
integer \(L\)-functions, RH, or GRH, and it does not infer an infinite theorem
from the previously computed fields \(q=3,5,7\). Those scans are regression
controls only; no scan value occurs in the proof.

The algebraic certificate has fixed limits of nine rows, formal-series degree
five, polynomial degree twelve, and 10,000 coefficient operations. Its
formal polynomial specializations make sense at arbitrary odd integers, but
the family-theoretic interpretation above is asserted only for odd prime
powers. Run:

```text
python research/l-families/atlas/function_field/genus2_moment_identity.py
python tests/test_genus2_moment_identity.py
python -O tests/test_genus2_moment_identity.py
```
