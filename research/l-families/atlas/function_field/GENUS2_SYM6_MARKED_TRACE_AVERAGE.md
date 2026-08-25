# Genus-two \(\operatorname{Sym}^6\) marked trace

Status: **PROVED** by bounded exact Möbius/Euler-product algebra for every
odd prime power.

Let \(\mathcal H_5(q)\) be the monic squarefree quintics in
\(\mathbf F_q[T]\), and write

\[
 P_D(u)=1+a_Du+b_Du^2+qa_Du^3+q^2u^4,\qquad
 {1\over P_D(u)}=\sum_{n\ge0}r_D(n)u^n.                            \tag{1}
\]

The theorem replay enumerates no field and no quintic. It uses exact
univariate polynomial algebra, the source-locked genus-one cubic moment laws,
and the source-locked marked-root moment lemma from the \(B4\) packet. The
complete \(q=3,5,7\) joint coefficient laws are read only after the symbolic
identity closes, as held-out falsification controls.

## 1. The theorem

For every odd prime power \(q\),

\[
\boxed{
 \sum_{D\in\mathcal H_5(q)}r_D(6)=-4q(q-1).
}                                                                 \tag{2}
\]

Since \(\#\mathcal H_5(q)=q^4(q-1)\),

\[
\boxed{
 \mathbb E_D[r_D(6)]=-{4\over q^3}.
}                                                                 \tag{3}
\]

If \(U_D\in USp(4)\) is normalized Frobenius, the complete-symmetric
character identity gives

\[
 r_D(6)=q^3\chi_{(6,0)}(U_D).
                                                                    \tag{4}
\]

The source-locked marked-Weierstrass adapter therefore turns (2) into

\[
\boxed{
 \mathbb E_D[\chi_{(6,0)}(U_D)]=-{4\over q^6},
 \qquad
 T_{(6,0)}(q)=-4.
}                                                                 \tag{5}
\]

Thus the constant \(q=3,5,7\) row seen by the native reciprocal-wavelet
packet is an all-field theorem, not an interpolation.

For comparison, direct recurrence expansion gives

\[
\begin{aligned}
r_D(6)={}&a_D^6-5a_D^4b_D+4qa_D^4+6a_D^2b_D^2\\
 &-6qa_D^2b_D-2q^2a_D^2-b_D^3+2q^2b_D.             \tag{6}
\end{aligned}
\]

The proof below does not separately evaluate the two apparently new raw
moments \(a_D^6\) and \(a_D^4b_D\). It computes their required combination
directly at the Euler-reciprocal level.

## 2. Möbius and the squarefree sieve

The quadratic Dirichlet Euler product of a squarefree quintic gives

\[
 r_D(6)=\sum_{\substack{f\ {\rm monic}\\\deg f=6}}
          \mu(f)\left({D\over f}\right).                            \tag{7}
\]

For squarefree \(f\) of degree six, let \(\ell(f)\) and \(k(f)\) be its
numbers of linear and irreducible-quadratic prime factors. Put

\[
 C_j(f)=\sum_{\deg h=j}\left({h\over f}\right),\qquad
 S_5(f)=\sum_{D\in\mathcal H_5(q)}\left({D\over f}\right).
\]

Expanding

\[
 \mu^2(D)=\sum_{A^2\mid D}\mu(A)
\]

and separating \(\deg A=0,1,2\) gives

\[
\boxed{
 S_5(f)=C_5(f)-(q-\ell(f))C_3(f)
 +\left(\binom{\ell(f)+1}{2}+k(f)-q\ell(f)\right)C_1(f).
}                                                                 \tag{8}
\]

The degree-two coefficient in (8) is signed. Among squarefree quadratic
\(A\), a product of two distinct linears has \(\mu(A)=+1\), while an
irreducible quadratic has \(\mu(A)=-1\). Hence the coprime signed count is

\[
 \binom{q-\ell}{2}-\left({q(q-1)\over2}-k\right)
 =\binom{\ell+1}{2}+k-q\ell.
\]

The character modulo squarefree degree-six \(f\) is primitive and even, so

\[
 L_f(u)=(1-u)
 \bigl(1+A_fu+B_fu^2+qA_fu^3+q^2u^4\bigr),
\]

and therefore \(C_5(f)=-q^2\). On the other hand,

\[
 \sum_{\deg f=6}\mu(f)=0
\]

because \(\sum_f\mu(f)u^{\deg f}=1-qu\). The complete \(C_5\) row in (8)
vanishes after summing over \(f\).

## 3. Turning the remaining rows into reciprocal Euler coefficients

For a monic \(h\), define

\[
 G_h(z)=\prod_P\left(1-\left({P\over h}\right)z^{\deg P}\right)
       =\sum_{n\ge0}g_n(h)z^n.                                    \tag{9}
\]

Let \(\lambda_n(h)\) be the same degree-\(n\) coefficient after weighting
each squarefree \(f\) by its number \(\ell(f)\) of linear factors. Define
\(\lambda_n^{(2)}(h)\) by the weight \(\binom{\ell(f)}2\), and
\(\kappa_n(h)\) by the number \(k(f)\) of quadratic factors.

Quadratic reciprocity has no sign when the degree-six variable \(f\) is
swapped with \(h\). Summing (8) over \(f\) therefore reduces (2) to

\[
 \sum_Dr_D(6)=-qG_3+\Lambda_3+Q_1,                                \tag{10}
\]

where

\[
\begin{aligned}
G_3&=\sum_{\deg h=3}g_6(h),\\
\Lambda_3&=\sum_{\deg h=3}\lambda_6(h),\\
Q_1&=\sum_{\deg h=1}
 \left(\lambda_6^{(2)}(h)+\kappa_6(h)-(q-1)\lambda_6(h)\right).
\end{aligned}                                                     \tag{11}
\]

The three terms in (10) are evaluated separately below.

## 4. Squarefree cubic moduli

Let \(h\) be a monic squarefree cubic. Put

\[
 a_h=-\sum_{x\in\mathbf F_q}\chi(h(x)),\qquad
 s_h=\sum_{\deg P=1}\left({P\over h}\right)
     =-\chi(-1)a_h.
\]

If \(m_1(h)\) is the number of rational roots of \(h\), then the number of
nonzero linear-prime signs is \(N_h=q-m_1(h)\), and

\[
 G_h(z)={1\over1+s_hz+qz^2}.
\]

Its sixth coefficient is

\[
 g_6=-q^3+6q^2s^2-5qs^4+s^6.                                    \tag{12}
\]

Marking one selected linear prime in the Euler product gives

\[
\begin{aligned}
\lambda_6={}&
N\bigl(-q^2+q-1+(3q-1)s^2-s^4\bigr)\\
&+(3q^2-2q+1)s^2+(1-4q)s^4+s^6.                  \tag{13}
\end{aligned}
\]

For completeness, if \(g_j=[z^j]G_h\), (13) is the direct expansion of

\[
 \lambda_6=-s(g_5+g_3+g_1)-N(g_4+g_2+g_0).                       \tag{14}
\]

Let

\[
 T_{2j}=\sum_{h\ {\rm squarefree\ cubic}}a_h^{2j},\qquad
 J_{2j}=\sum_hm_1(h)a_h^{2j}.
\]

The source-locked genus-one packet gives

\[
\begin{aligned}
T_0&=q^2(q-1),\\
T_2&=q(q-1)(q^2-1),\\
T_4&=q(q-1)(2q^3-3q-1),\\
T_6&=q(q-1)(5q^4-9q^2-5q-1).
\end{aligned}                                                     \tag{15}
\]

The elementary type count and the \(B4\) marked-root lemma give exactly the
three marked quantities that occur in (13):

\[
\begin{aligned}
J_0&=q(q-1)^2,\\
J_2&=q(q-1)(q+1)(q-2),\\
J_4&=2q(q-1)(q+1)(q^2-2q-1).
\end{aligned}                                                     \tag{16}
\]

No marked sixth moment is needed: the \(s^6\) coefficient in (13) is
independent of \(N=q-m_1\).

Substitution of (15)--(16) into (12)--(13) gives

\[
\boxed{
\sum_{h\ {\rm squarefree\ cubic}}g_6(h)=-q(q-1),
\qquad
\sum_{h\ {\rm squarefree\ cubic}}\lambda_6(h)
=q(q-1)(q-8).
}                                                                 \tag{17}
\]

This is the only place where arithmetic trace moments enter.

## 5. Repeated cubic moduli

There are two repeated-factor types.

For \(h=L^3\), \(G_h=1\). Hence \(g_6(h)=0\) and
\(\lambda_6(h)=-(q-1)\). There are \(q\) such cubics.

For \(h=L^2M\), \(L\ne M\), put \(e=(L/M)\). Then

\[
 G_h(z)={1\over1-ez},\qquad
 g_6(h)=1,\qquad
 \lambda_6(h)=9-3q.                                               \tag{18}
\]

The last value is independent of \(e\), and there are \(q(q-1)\) ordered
pairs \((L,M)\). Adding (17)--(18) yields the exact cancellations

\[
\boxed{
G_3=0,\qquad
\Lambda_3=-2q^2(q-1).
}                                                                 \tag{19}
\]

## 6. Linear moduli

Fix a monic linear \(h\). Then \(G_h=1\). Among the \(q-1\) nonzero
linear-prime signs there are equally many \(+1\) and \(-1\), while the sum
of the irreducible-quadratic signs is \(-(q-1)/2\).

Marking one linear factor, a pair of linear factors, or one quadratic
factor gives

\[
\begin{aligned}
\lambda_6(h)&=-(q-1),\\
\lambda_6^{(2)}(h)&={(q-1)(2q-7)\over2},\\
\kappa_6(h)&={q-1\over2}.
\end{aligned}                                                     \tag{20}
\]

For the middle row, put \(n=(q-1)/2\). The \(++\) and \(--\) pairs each
contribute the degree-four coefficient \(5\) of
\((1\mp z)^{-2}\), while a \(+-\) pair contributes \(-1\). Thus

\[
 \lambda_6^{(2)}=5\left(2\binom n2\right)-n^2
 ={(q-1)(2q-7)\over2}.
\]

The bracket in \(Q_1\) is consequently \(2(q-1)(q-2)\) for each of the
\(q\) linear moduli:

\[
\boxed{Q_1=2q(q-1)(q-2).}                                        \tag{21}
\]

Finally, (10), (19), and (21) give

\[
 -q\cdot0-2q^2(q-1)+2q(q-1)(q-2)=-4q(q-1),
\]

which proves (2).

## 7. Literature and claim boundary

Bergström's Theorem 11.6 prints the **unmarked** result

\[
 e_c(\mathcal M_2,V_{(6,0)})=-1.
\]

That does not determine the marked-Weierstrass trace: the forgetful fibre
weights each curve by its number of rational ramification points.
Bergström--Faber--van der Geer define the correct stack
\(\mathcal M_2(w^1)\), but their level-two point computation is bounded and
their later ambient identifications have explicit conjectural components.
The proof above supplies the missing marked all-field evaluation directly.
No external novelty claim is made.

This theorem is:

- an exact family average, not a memberwise sign theorem;
- a marked-stack trace, not an identification of individual cohomology
  groups or a motive;
- unrelated to any global number-field Euler-product equality;
- and not an RH or GRH implication.

## 8. Held-out controls and replay

The complete frozen joint \((a_D,b_D)\) laws give:

| \(q\) | \(\sum_Dr_D(6)\) | theorem |
|---:|---:|---:|
| 3 | \(-24\) | \(-4q(q-1)\) |
| 5 | \(-80\) | \(-4q(q-1)\) |
| 7 | \(-168\) | \(-4q(q-1)\) |

These values are checked only after the symbolic proof and are never read as
theorem input.

From the repository root:

    python -B research/l-families/atlas/function_field/genus2_sym6_marked_trace_average.py --check
    python -B -O research/l-families/atlas/function_field/genus2_sym6_marked_trace_average.py --check
    python -B -m unittest tests.test_genus2_sym6_marked_trace_average -v
    python -B -O -m unittest tests.test_genus2_sym6_marked_trace_average -v

The producer declares a combined cap of \(4096\) symbolic operations and
held-out input atoms. It uses exact Fraction and integer arithmetic only.
