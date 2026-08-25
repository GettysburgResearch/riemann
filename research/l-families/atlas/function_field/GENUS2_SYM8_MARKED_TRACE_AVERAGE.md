# Genus-two \(\operatorname{Sym}^8\) marked trace

Status: **PROVED** for every odd prime power, using bounded exact
Möbius/Euler-product algebra and the standard Eichler--Shimura theorem on
\(Y_0(2)\).

Let \(\mathcal H_5(q)\) be the monic squarefree quintics over
\(\mathbf F_q\), and write

\[
 P_D(u)=1+a_Du+b_Du^2+qa_Du^3+q^2u^4,
 \qquad {1\over P_D(u)}=\sum_{n\geq0}r_D(n)u^n.                 \tag{1}
\]

The theorem replay enumerates no field, curve, or quintic. Its native part
uses exact polynomial algebra, the source-locked genus-one cubic moments,
and the source-locked low marked-root moments. The only non-Tate input is a
precisely stated modular-curve trace theorem. The complete \(q=3,5,7\)
spectroscopy values are read only after the proof closes.

## 1. The theorem

Put

\[
 f(z)=\eta(z)^8\eta(2z)^8=\sum_{n\geq1}c_nQ^n,
 \qquad Q=e^{2\pi iz}.                                           \tag{2}
\]

This is the unique normalized newform in \(S_8(\Gamma_0(2))\). If
\(q=p^r\) is an odd prime power, define the Frobenius-power trace

\[
 \Theta_{8,2}(p^r)=c_{p^r}-p^7c_{p^{r-2}},                       \tag{3}
\]

where the second term is zero when \(r<2\). Equivalently, if
\(\alpha_p,\beta_p\) are the good-prime roots, then

\[
 \Theta_{8,2}(p^r)=\alpha_p^r+\beta_p^r.                         \tag{4}
\]

For every odd prime power \(q\),

\[
 \boxed{
  \sum_{D\in\mathcal H_5(q)}r_D(8)
  =q(q-1)\bigl(-\Theta_{8,2}(q)-q-6\bigr).}
                                                                    \tag{5}
\]

Since \(\#\mathcal H_5(q)=q^4(q-1)\), this gives

\[
 \boxed{
  \mathbb E_D[r_D(8)]
  ={ -\Theta_{8,2}(q)-q-6\over q^3}.}                            \tag{6}
\]

For normalized Frobenius \(U_D\in USp(4)\), the complete-symmetric
character identity is

\[
 r_D(8)=q^4\chi_{(8,0)}(U_D).                                    \tag{7}
\]

The source-locked marked-Weierstrass adapter therefore turns (5) into

\[
 \boxed{
 T_{(8,0)}(q)=-\Theta_{8,2}(q)-q-6,
 \qquad
 \mathbb E_D[\chi_{(8,0)}(U_D)]
 ={ -\Theta_{8,2}(q)-q-6\over q^7}.}                             \tag{8}
\]

Thus the three finite values \(-21,199,-1029\) are shadows of an exact
level-two modular trace, not an interpolated polynomial.

For reference, direct recurrence expansion gives

\[
\begin{aligned}
r_D(8)={}&a_D^8-7a_D^6b_D+6qa_D^6+15a_D^4b_D^2
          -20qa_D^4b_D+q^2a_D^4\\
 &-10a_D^2b_D^3+12qa_D^2b_D^2+9q^2a_D^2b_D-6q^3a_D^2\\
 &+b_D^4-3q^2b_D^2+q^4.                              \tag{9}
\end{aligned}
\]

The proof does not evaluate those raw genus-two moments separately.

## 2. Möbius and the squarefree sieve

The quadratic Dirichlet Euler product gives

\[
 r_D(8)=\sum_{\substack{f\text{ monic}\\ \deg f=8}}
          \mu(f)\left({D\over f}\right).                         \tag{10}
\]

For squarefree \(f\) of degree eight, let \(\ell(f)\) and \(k(f)\) be its
numbers of linear and irreducible-quadratic factors. Put

\[
 C_j(f)=\sum_{\deg h=j}\left({h\over f}\right),\qquad
 S_5(f)=\sum_{D\in\mathcal H_5(q)}\left({D\over f}\right).
\]

The same exact squarefree sieve as in the weight-six packet gives

\[
 \boxed{
 S_5(f)=C_5(f)-(q-\ell(f))C_3(f)
 +\left(\binom{\ell(f)+1}{2}+k(f)-q\ell(f)\right)C_1(f).}        \tag{11}
\]

The potentially self-referential \(C_5\) row is removed before reciprocity.
Because the degree-eight primitive character is even,

\[
 L_f(u)=(1-u)
 \left(1+A_fu+B_fu^2+C_fu^3+qB_fu^4+q^2A_fu^5+q^3u^6\right).
\]

Comparing coefficients gives

\[
 \boxed{C_5=q(q-1)C_1-qC_2+q(q-1).}                              \tag{12}
\]

Moreover \(\sum_{\deg f=8}\mu(f)=0\), since
\(\sum_f\mu(f)u^{\deg f}=1-qu\). Thus the constant in (12) cancels.

For any monic \(h\), define

\[
 G_h(z)=\prod_P\left(1-\left({P\over h}\right)z^{\deg P}\right)
       =\sum_{n\geq0}g_n(h)z^n.                                  \tag{13}
\]

Let \(\lambda_n(h)\), \(\lambda_n^{(2)}(h)\), and \(\kappa_n(h)\) be
the same coefficient after weighting the squarefree Euler term by,
respectively, \(\ell(f)\), \(\binom{\ell(f)}2\), and \(k(f)\).
Degree-eight reciprocity has no sign. Summing (11) and using (12) yields

\[
\begin{aligned}
\sum_Dr_D(8)
={}&q(q-1)G_1-qG_2-qG_3+\Lambda_3+Q_1,                 \tag{14}\\
G_j={}&\sum_{\deg h=j}g_8(h),\\
\Lambda_3={}&\sum_{\deg h=3}\lambda_8(h),\\
Q_1={}&\sum_{\deg h=1}
 \left(\lambda_8^{(2)}(h)+\kappa_8(h)-(q-1)\lambda_8(h)\right).
\end{aligned}
\]

For linear \(h\), \(G_h=1\), hence \(G_1=0\). A squarefree quadratic has
\(G_h=(1-z)^{-1}\), so its eighth coefficient is one; there are
\(q(q-1)\) such polynomials. For \(h=L^2\),

\[
 G_h(z)={1-qz\over1-z},\qquad g_8(h)=1-q,
\]

and there are \(q\) choices. Therefore

\[
 \boxed{G_2=q(q-1)+q(1-q)=0.}                                    \tag{15}
\]

This is the exact cancellation that prevents (14) from feeding the desired
degree-eight quantity back into itself.

## 3. The cubic descent

Let \(h\) be a squarefree monic cubic, let \(m_1(h)\) be its number of
rational roots, and put

\[
 a_h=-\sum_x\chi(h(x)),\qquad
 s_h=\sum_{\deg P=1}\left({P\over h}\right),\qquad
 N_h=q-m_1(h).
\]

Then \(s_h^2=a_h^2\) and

\[
 G_h(z)={1\over1+s_hz+qz^2}.
\]

Its eighth coefficient is

\[
 g_8=s^8-7qs^6+15q^2s^4-10q^3s^2+q^4.                           \tag{16}
\]

Marking one linear factor in the Euler product gives

\[
 \lambda_8=-s(g_7+g_5+g_3+g_1)-N(g_6+g_4+g_2+g_0).              \tag{17}
\]

After inserting \(N=q-m_1\), (17) becomes

\[
\begin{aligned}
\lambda_8={}&s^8+(1-7q)s^6+m_1s^6
 +(15q^2-5q+1)s^4-(5q-1)m_1s^4\\
 &+(-10q^3+6q^2-3q+1)s^2
 +(6q^2-3q+1)m_1s^2\\
 &+(q^3-q^2+q-1)(q-m_1).                              \tag{18}
\end{aligned}
\]

Write

\[
 T_{2j}=\sum_{h\text{ squarefree cubic}}a_h^{2j},\qquad
 J_{2j}=\sum_h m_1(h)a_h^{2j}.                                   \tag{19}
\]

The source-locked genus-one theorem supplies \(T_0,\ldots,T_8\), and the
source-locked marked-root lemma supplies

\[
\begin{aligned}
J_0&=q(q-1)^2,\\
J_2&=q(q-1)(q+1)(q-2),\\
J_4&=2q(q-1)(q+1)(q^2-2q-1).                         \tag{20}
\end{aligned}
\]

Substitution into (16)--(18), leaving only \(J_6\) formal, gives

\[
\begin{aligned}
\sum_{h\text{ squarefree cubic}}g_8(h)&=-q(q-1),\\
\sum_{h\text{ squarefree cubic}}\lambda_8(h)
 &=J_6-q(q-1)(5q^4-5q^3-18q^2-11q+9).               \tag{21}
\end{aligned}
\]

The repeated cubics contribute as follows:

\[
\begin{array}{c|c|c}
h&g_8(h)&\lambda_8(h)\\ \hline
L^3&0&-(q-1)\\
L^2M,\ L\ne M&1&12-4q.
\end{array}                                                        \tag{22}
\]

There are \(q\) cubics of the first type and \(q(q-1)\) of the second.
Consequently

\[
 \boxed{G_3=0,\qquad
 \Lambda_3=J_6-q(q-1)(5q^4-5q^3-18q^2-7q-2).}                  \tag{23}
\]

## 4. The linear-modulus row

Fix a monic linear \(h\). Then \(G_h=1\). Among the \(q-1\) nonzero
linear-prime signs there are equally many \(+1\) and \(-1\). Direct marking
gives

\[
\begin{aligned}
\lambda_8(h)&=-(q-1),\\
\lambda_8^{(2)}(h)&={(q-1)(3q-10)\over2},\\
\kappa_8(h)&=-{q(q-1)\over2}.                         \tag{24}
\end{aligned}
\]

For the middle row, equal-sign pairs contribute seven and opposite-sign
pairs contribute \(-1\). For the last row, the quadratic marked factor must
use its fourth power, hence every nonzero quadratic sign contributes \(-1\).
The bracket in \(Q_1\) is therefore \(2(q-1)(q-3)\), and

\[
 \boxed{Q_1=2q(q-1)(q-3).}                                      \tag{25}
\]

Equations (14)--(15), (23), and (25) prove the native reduction

\[
 \boxed{
 \sum_Dr_D(8)
 =J_6-q(q-1)(5q^4-5q^3-18q^2-9q+4).}                            \tag{26}
\]

No modular form, sampled field, or conjectural genus-two cohomology enters
this step. It isolates the smallest possible residual channel.

## 5. The marked-cubic sixth moment

A pair \((h,r)\), where \(h\) is a squarefree monic cubic and \(r\) is one
of its rational roots, is an elliptic curve together with a chosen nonzero
rational two-torsion point. The square-affine model group, including its
central \(\mu_2\), has order \(q(q-1)\). Orbit--stabilizer gives

\[
 J_6=q(q-1)
 \sum_{[(E,T)]}{a_E^6\over|\operatorname{Aut}_{\mathbf F_q}(E,T)|},
 \qquad 0\ne T\in E[2](\mathbf F_q).                             \tag{27}
\]

This is the \(Y_1(2)=Y_0(2)\) modular stack. Let

\[
 P_m(a,q)=\operatorname{Tr}(\operatorname{Sym}^mH^1(E)),qquad
 P_m=aP_{m-1}-qP_{m-2}.                                          \tag{28}
\]

The stack trace formula, localization, and Eichler--Shimura identity on
\(Y_0(2)\) give, over every odd finite field,

\[
\begin{aligned}
\sum_{[(E,T)]}{P_0\over|\operatorname{Aut}(E,T)|}&=q-1,\\
\sum_{[(E,T)]}{P_2\over|\operatorname{Aut}(E,T)|}&=-2,\\
\sum_{[(E,T)]}{P_4\over|\operatorname{Aut}(E,T)|}&=-2,\\
\sum_{[(E,T)]}{P_6\over|\operatorname{Aut}(E,T)|}
 &=-\Theta_{8,2}(q)-2.                                  \tag{29}
\end{aligned}
\]

The two constants in the positive symmetric powers are the two cusps.
The first two cusp spaces vanish:
\(S_4(\Gamma_0(2))=S_6(\Gamma_0(2))=0\). The unique cuspidal channel in
the last row is (2).

More precisely, for even \(m>0\) and \(\ell\ne2,p\), localization gives

\[
0\longrightarrow\mathbf Q_\ell^{\,2}
\longrightarrow H_c^1(Y_0(2)_{\overline{\mathbf F}_p},\mathbb V_m)
\longrightarrow H_!^1(Y_0(2)_{\overline{\mathbf F}_p},\mathbb V_m)
\longrightarrow0.                                                \tag{29a}
\]

The two boundary lines have Frobenius eigenvalue one. Scholl's
Theorem 1.2.4(i) identifies the interior term with the good-prime
two-dimensional representation attached to each normalized eigenform;
his Section 4.2 handles levels below three by auxiliary level and invariants.
The restriction sometimes stated as \(p\geq m+2\) belongs to the crystalline
clause, not to this \(\ell\)-adic good-prime statement. Thus characteristic
three is included.

The elementary \(SU(2)\) decomposition

\[
 a^6=P_6+5qP_4+9q^2P_2+5q^3P_0                              \tag{30}
\]

now proves

\[
 \boxed{
 J_6=q(q-1)
 \bigl(5q^4-5q^3-18q^2-10q-2-\Theta_{8,2}(q)\bigr).}             \tag{31}
\]

Substitution of (31) into (26) proves (5).

## 6. Eta product and the prime-power convention

The eta-quotient criterion proves directly that (2) lies in
\(S_8(\Gamma_0(2))\): its weight is eight; the two exponent sums are

\[
 1\cdot8+2\cdot8=24,
 \qquad 2\cdot8+1\cdot8=24;
\]

its character is trivial, and both cusp orders are positive. The standard
dimension formula gives

\[
 \dim M_8(\Gamma_0(2))=3,qquad
 M_8=\langle E_8(z),E_8(2z),f(z)\rangle.                          \tag{32}
\]

Thus \(S_8(\Gamma_0(2))\) is one-dimensional. Since
\(S_8(SL_2(\mathbf Z))=0\), the normalized eta product is new.
Ryan--Sirolli--Villegas-Morales--Zheng, Proposition 2.6, gives a concise
independent certificate: \(\Delta_2=f\) has a simple zero at each of the two
cusps and no interior zero, and multiplication by \(\Delta_2\) is an
isomorphism \(M_k(\Gamma_0(2))\simeq S_{k+8}(\Gamma_0(2))\).

The producer independently multiplies

\[
 Q\prod_{n\geq1}(1-Q^n)^8(1-Q^{2n})^8
\]

through degree nine and obtains

\[
 f=Q-8Q^2+12Q^3+64Q^4-210Q^5-96Q^6
   +1016Q^7-512Q^8-2043Q^9+O(Q^{10}).                            \tag{33}
\]

In particular

\[
 c_9=c_3^2-3^7=-2043,
 \qquad
 \Theta_{8,2}(9)=c_9-3^7c_1=-4230.                              \tag{34}
\]

Equation (8) therefore predicts, without enumerating \(\mathbf F_9\),

\[
 \boxed{T_{(8,0)}(9)=4230-9-6=4215.}                             \tag{35}
\]

This illustrates why \(c_{p^r}\) alone is not the correct extension-field
trace.

## 7. Held-out controls and source audit

Only after the symbolic theorem and eta-product expansion close does the
producer read the frozen native-wavelet rows. It also independently
recomputes \(\sum_Dr_D(8)\) from all 251 atoms in the source-locked joint
\((a_D,b_D)\) laws:

| \(q\) | \(c_q=\Theta_{8,2}(q)\) | frozen \(T_{(8,0)}\) | theorem |
|---:|---:|---:|---:|
| 3 | 12 | -21 | -21 |
| 5 | -210 | 199 | 199 |
| 7 | 1016 | -1029 | -1029 |

They are falsification controls, not theorem inputs.

The primary-source ledger in the JSON pins the following roles:

1. Kai Behrend, [*The Lefschetz trace formula for algebraic
   stacks*](https://personal.math.ubc.ca/~behrend/ladic.pdf), Theorem 1.0.1,
   for the stack-weighted trace formula.
2. A. J. Scholl, [*Motives for modular
   forms*](https://www.dpmms.cam.ac.uk/~ajs1005/preprints/mf.pdf),
   Theorem 1.2.4(i) and Section 4.2, for the good-prime modular Galois
   representation and the low-level case.
3. Nathan Kaplan and Ian Petrow, [*Elliptic curves over a finite field and
   the trace formula*](https://arxiv.org/abs/1510.03980), *Proc. London Math.
   Soc.* 115 (2017), 1317--1372, for prime-power Chebyshev/Hecke formulas
   with prescribed torsion.
4. The same authors, [*Traces of Hecke operators and refined weight
   enumerators of Reed--Solomon codes*](https://arxiv.org/abs/1506.04440),
   Theorems 8--9, give an independent prescribed-two-torsion check. The
   marked-point combination is their one-two-torsion row plus twice their
   full-two-torsion row; its \(\Gamma_0(4)\) traces cancel.
5. Ryan--Sirolli--Villegas-Morales--Zheng,
   [*Explicit families of congruences for the overpartition
   function*](https://doi.org/10.1007/s11139-024-00953-z), Proposition 2.6,
   for the exact level-two eta-product divisor and dimension statement.
6. B. Ramakrishnan and Brundaban Sahu,
   [*On the number of representations of an integer by certain quadratic
   forms in sixteen variables*](https://www.niser.ac.in/~brundaban.sahu/convolution-16.pdf),
   especially equations (9) and the basis statement in Section 3.1. They
   identify (2) as the unique normalized weight-eight level-two newform.

The exact curve-open answer also follows formally by subtracting the exact
decomposable boundary from the \(S_5\)-projection of the
Bergström--Faber--van der Geer ambient formula. That ambient nonregular and
endoscopic formula is conjectural in the audited source, so it is not used
as a proof here. No global novelty claim is made.

## Replay

From the repository root:

```text
python research/l-families/atlas/function_field/genus2_sym8_marked_trace_average.py --check
python -O research/l-families/atlas/function_field/genus2_sym8_marked_trace_average.py --check
python -m unittest tests.test_genus2_sym8_marked_trace_average -v
python -O -m unittest tests.test_genus2_sym8_marked_trace_average -v
```

The producer uses exact rational/integer algebra under a hard 4096
operation-plus-input-atom cap. It makes no RH, GRH, memberwise sign, motive,
compatible-system, or global Euler-product claim.
