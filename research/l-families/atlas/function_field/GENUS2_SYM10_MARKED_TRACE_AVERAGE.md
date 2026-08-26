# Genus-two \(\operatorname{Sym}^{10}\) marked trace

Status: **PROVED** for every odd prime power.  The replay uses bounded exact
Möbius/Euler algebra, source-locked genus-one trace theorems, and the standard
Eichler--Shimura trace formula.  It enumerates no finite field or genus-two
family.

Let \(\mathcal H_5(q)\) be the monic squarefree quintics over
\(\mathbf F_q\), and put

\[
 P_D(u)=1+a_Du+b_Du^2+qa_Du^3+q^2u^4,
 \qquad P_D(u)^{-1}=\sum_{n\geq0}r_D(n)u^n.                    \tag{1}
\]

Three modular traces occur.  Write \(\Theta_\Delta(q)\) for the
prime-power Frobenius trace of Ramanujan's normalized weight-twelve
level-one form, and write \(\Theta_{8,2}(q)\) and \(\Theta_{10,2}(q)\)
for those of the unique normalized newforms in weights eight and ten on
\(\Gamma_0(2)\).  At \(q=p^r\), these are Frobenius-root power sums, not
generally Fourier coefficients at index \(p^r\).

## 1. The theorem

For every odd prime power \(q\),

\[
\boxed{
 T_{(10,0)}(q)
 =(q-1)\Theta_\Delta(q)-\Theta_{8,2}(q)-\Theta_{10,2}(q)-q-7.} \tag{2}
\]

Equivalently,

\[
\boxed{
 \sum_{D\in\mathcal H_5(q)}r_D(10)
 =q(q-1)\bigl((q-1)\Theta_\Delta(q)-\Theta_{8,2}(q)
 -\Theta_{10,2}(q)-q-7\bigr).}                               \tag{3}
\]

Since \(\#\mathcal H_5(q)=q^4(q-1)\) and
\(r_D(10)=q^5\chi_{(10,0)}(U_D)\),

\[
 \mathbb E_D[r_D(10)]={T_{(10,0)}(q)\over q^3},
 \qquad
 \mathbb E_D[\chi_{(10,0)}(U_D)]={T_{(10,0)}(q)\over q^8}.     \tag{4}
\]

The frozen prime fields are post-theorem falsification controls:

| \(q\) | \(T_{(10,0)}(q)\) | \(\sum_Dr_D(10)\) |
|---:|---:|---:|
| 3 | 638 | 3,828 |
| 5 | 18,648 | 372,960 |
| 7 | -100,542 | -4,222,764 |

The sign change is a modular-trace phenomenon, not a memberwise sign theorem.

## 2. Degree-ten reciprocal reduction

The quadratic Euler product gives

\[
 r_D(10)=\sum_{\substack{f\ {\rm monic\ squarefree}\\\deg f=10}}
 \mu(f)\left({D\over f}\right).                               \tag{5}
\]

For such an \(f\), let \(C_j(f)\) be the degree-\(j\) coefficient of its
quadratic Dirichlet \(L\)-function, and let \(\ell(f)\) and \(k(f)\) count
its linear and irreducible-quadratic factors.  Exact quintic
squarefree sieving gives

\[
 S_5(f)=C_5-(q-\ell)C_3+
 \left(\binom{\ell+1}{2}+k-q\ell\right)C_1.                   \tag{6}
\]

The degree-ten character is even.  If
\(L_f(u)=(1-u)Q_f(u)\), then \(Q_f\) has degree eight and its functional
equation gives \(Q_5=qQ_3\).  Therefore

\[
 \boxed{C_5=(q-1)(1+C_1+C_2+C_3)-C_4.}                       \tag{7}
\]

For a monic polynomial \(h\), define

\[
 G_h(z)=\prod_P\left(1-\left({P\over h}\right)z^{\deg P}\right)
 =\sum_{n\geq0}g_n(h)z^n,
 \qquad G_j=\sum_{\deg h=j}g_{10}(h).                         \tag{8}
\]

For later marking, set

\[
\begin{aligned}
 \lambda_{10}(h)
  &=\sum_{\substack{f\ {\rm monic\ squarefree}\\\deg f=10}}
      \mu(f)\ell(f)\left({h\over f}\right),\\
 \lambda_{10}^{[2]}(h)
  &=\sum_{\substack{f\ {\rm monic\ squarefree}\\\deg f=10}}
      \mu(f)\binom{\ell(f)}2\left({h\over f}\right),\\
 \kappa_{10}(h)
  &=\sum_{\substack{f\ {\rm monic\ squarefree}\\\deg f=10}}
      \mu(f)k(f)\left({h\over f}\right).
\end{aligned}                                                  \tag{9}
\]

Thus

\[
 \Lambda_3=\sum_{\deg h=3}\lambda_{10}(h),\qquad
 Q_1=\sum_{\deg h=1}
 \bigl(\lambda_{10}^{[2]}+\lambda_{10}+\kappa_{10}
       -q\lambda_{10}\bigr)(h).                               \tag{10}
\]

Reciprocity has no sign because ten is even.  The constant term in (7)
vanishes after aggregation:

\[
 \sum_{\substack{f\ {\rm monic\ squarefree}\\\deg f=10}}\mu(f)=0,
\]

because \(\sum_f\mu(f)z^{\deg f}=\prod_P(1-z^{\deg P})=1-qz\).
Substitution of (7) into (6) now gives

\[
 \sum_Dr_D(10)
 =(q-1)(G_1+G_2)-G_3-G_4+\Lambda_3+Q_1.                      \tag{11}
\]

The two low-degree rows cancel exactly.  For a linear \(h\), \(G_h=1\),
so \(G_1=0\).  Among monic quadratics, the \(q^2-q\) squarefree moduli
have \(g_{10}=1\), while the \(q\) squares \(L^2\) have \(g_{10}=1-q\);
hence

\[
 \boxed{G_1=G_2=0.}                                           \tag{12}
\]

## 3. The cubic row

For squarefree cubic \(h\), put
\(s_h=\sum_x\chi(h(x))=-a_h\).  Then

\[
 G_h(z)={1\over1+s_hz+qz^2},
\]

so \(g_{10}\) is the weight-ten \(SU(2)\) character polynomial.  The
source-locked genus-one trace theorem gives

\[
 \sum_{h\ {\rm squarefree\ cubic}}g_{10}(h)
 =-q(q-1)(1+\Theta_\Delta(q)).                                \tag{13}
\]

The repeated cubics \(L^3\) contribute zero, while the \(q(q-1)\)
ordered cubics \(L^2M\) contribute one each.  Therefore

\[
 \boxed{G_3=-q(q-1)\Theta_\Delta(q).}                          \tag{14}
\]

For a squarefree cubic, distinguished-linear Euler marking obeys

\[
 \lambda_{10}=-\sum_{m=1}^{10}p_mg_{10-m},
 \qquad
 p_m=\begin{cases}s_h,&m\ {\rm odd},\\q-m_1(h),&m\ {\rm even}.
 \end{cases}                                                   \tag{15}
\]

The producer derives this identity in \(\mathbf Z[q,s,N]\).  Substituting
the unmarked cubic moments through degree ten and the marked
two-torsion moments through degree eight gives

\[
 \Lambda_3^{\rm sf}=q(q-1)
 \bigl(-\Theta_{10,2}-\Theta_\Delta-\Theta_{8,2}+q-14\bigr).   \tag{16}
\]

For \(L^3\), direct Euler marking gives
\(\lambda_{10}=-(q-1)\).  For \(L^2M\), it gives
\(\lambda_{10}=15-5q\), independently of the missing Euler-factor sign.
Consequently

\[
 \boxed{
 \Lambda_3=-q(q-1)
 \bigl(\Theta_{10,2}+\Theta_\Delta+\Theta_{8,2}+4q\bigr).}     \tag{17}
\]

## 4. The quartic channel

This is the first quartic obstruction within this marked-trace tower, and
it is where the level-one trace in (2) acquires its coefficient \(q-1\).

### 4.1 Squarefree quartics

Let \(\mathcal H_4^{\rm sf}\) be the monic squarefree quartics, and let
\[
 (u,b)\cdot h(X)=u^{-4}h(uX+b),
 \qquad (u,b)\in\mathbf F_q^\times\ltimes\mathbf F_q.          \tag{18}
\]
The exact quotient-stack equivalence is
\[
 [\mathcal H_4^{\rm sf}/(\mathbf G_m\ltimes\mathbf G_a)]
 \simeq \{(E,O,P):P\in E(\mathbf F_q),\ P\ne O\}.              \tag{19}
\]
Here the two rational points at infinity are ordered as \(O,P\).
Thus, for every isomorphism-invariant \(F\),
\[
 \sum_{h\in\mathcal H_4^{\rm sf}}F(E_h)
 =q(q-1)\sum_{[E]}
 {(\#E(\mathbf F_q)-1)F(E)\over|\operatorname{Aut}_{\mathbf F_q}(E)|}.
                                                                    \tag{20}
\]

If \(a\) is the elliptic trace and
\[
 P_k(a,q)=\operatorname{Tr}(\operatorname{Sym}^kH^1),
 \qquad P_k=aP_{k-1}-qP_{k-2},                                 \tag{21}
\]
then
\[
 g_{10}=\sum_{k=0}^{10}P_k(a,q).                               \tag{22}
\]
Since \(\#E(\mathbf F_q)-1=q-a\), the identity
\(aP_k=P_{k+1}+qP_{k-1}\) telescopes:
\[
 (q-a)\sum_{k=0}^{10}P_k
 =qP_{10}-\sum_{k=1}^{11}P_k.                                 \tag{23}
\]

On the elliptic stack, with \(1/|\operatorname{Aut}_{\mathbf F_q}(E)|\)
weights understood, odd \(P_k\) have trace zero,
\(\sum P_0=q\), and
\[
 \sum P_k=-1-\Theta_{k+2}(q)\qquad(k>0\ {\rm even}).           \tag{24}
\]
The level-one cusp spaces in weights four, six, eight, and ten vanish;
weight twelve contributes \(\Theta_\Delta\).  Equations (23)--(24) give
\[
 \boxed{
 G_4^{\rm sf}=q(q-1)\bigl(5-q-(q-1)\Theta_\Delta(q)\bigr).}    \tag{25}
\]

### 4.2 Repeated quartics

The following six strata exhaust the \(q^3\) nonsquarefree monic quartics:

| stratum | count | \(g_{10}\) or aggregate input |
|---|---:|---:|
| \(L^4\) | \(q\) | \(1-q\) |
| \(L^3M\) | \(q(q-1)\) | \(1\) |
| \(L^2M^2\) | \(q(q-1)/2\) | \(11-10q\) |
| \(Q^2\), \(Q\) irreducible quadratic | \(q(q-1)/2\) | \(1\) |
| \(L^2MN\) | \(q(q-1)(q-2)/2\) | \(6+5e\) |
| \(L^2Q\) | \(q^2(q-1)/2\) | \(6+5e\) |

Writing \(L=X-\ell\), the missing Euler-factor sign is
\[
 e=\chi((\ell-m)(\ell-n))
\quad\hbox{for }L^2MN,\qquad
 e=\chi(Q(\ell))
\quad\hbox{for }L^2Q.                                         \tag{26}
\]
For fixed \(L\), elementary quadratic-character orthogonality gives
\[
 \sum_{\{M,N\}}e=-{q-1\over2},
 \qquad
 \sum_{Q\ {\rm irreducible\ quadratic}}e=-{q-1\over2}.        \tag{27}
\]
The first identity is half of
\((\sum_{x\ne0}\chi(x))^2-\sum_{x\ne0}\chi(x)^2\).
For the second, identify \(Q\) with a conjugate pair in
\(\mathbf F_{q^2}\setminus\mathbf F_q\); the norm-character sum is
\(-(q-1)\) before division by the pair size.

The \(L^4\) and \(L^3M\) rows cancel, and the remaining rows give
\[
 \boxed{G_4^{\rm rep}=q(q-1)(q-5).}                            \tag{28}
\]
Combining (25) and (28),
\[
 \boxed{G_4=-q(q-1)^2\Theta_\Delta(q).}                        \tag{29}
\]

## 5. The linear-modulus row and conclusion

For a fixed linear modulus, exact marking gives
\[
 \lambda_{10}=-(q-1),\qquad
 \lambda_{10}^{[2]}={(q-1)(4q-13)\over2},\qquad
 \kappa_{10}={q-1\over2}.                                     \tag{30}
\]
The middle term marks \(\binom{\ell}{2}\); hence the sieve's
\(\binom{\ell+1}{2}\) contributes
\(\lambda_{10}^{[2]}+\lambda_{10}\).  Substitution into (10) yields
\[
 \boxed{Q_1=q(q-1)(3q-7).}                                    \tag{31}
\]

Finally substitute (12), (14), (17), (29), and (31) into (11).  After
division by \(q(q-1)\), the \(\Theta_\Delta\) coefficient is
\[
 1+(q-1)-1=q-1,
\]
and the Tate row is \(-4q+3q-7=-q-7\).  This proves (2)--(3).

## 6. Prime-power consequence

At \(q=9\), independent truncated products and the Frobenius-power
recurrence give
\[
 \Theta_\Delta(9)=-290790,\qquad
 \Theta_{8,2}(9)=-4230,\qquad
 \Theta_{10,2}(9)=-15030.                                    \tag{32}
\]
For example,
\(\Theta_\Delta(9)=\tau(9)-3^{11}\tau(1)\); using \(\tau(9)\) alone
would be the wrong extension-field convention.  Without enumerating
\(\mathbf F_9\),
\[
 \boxed{T_{(10,0)}(9)=-2307076.}                              \tag{33}
\]

## 7. Provenance, scope, and replay

The producer source-locks:

- the all-\(q\) genus-one cubic moment packet;
- the Sym\(^8\) marked packet, payload
  423b8c37b69fb56b459beb7ebd9e6b94d12cf658f5819f7ac481e83560f5d0ae;
- the marked two-torsion tower at commit 446c88979, payload
  d6861d94296bd37bba503f87cfa4b00b51a3a2d4f62ae01c707cc45a08588cde.

The \(q=3,5,7\) joint coefficient atoms are a separate held-out source.
They cannot load until both the symbolic theorem and the independent
modular-form certificate close.  Exact integer/rational algebra runs under
operation, input-atom, recurrence-update, Fourier-degree, and wall-clock
caps.

The theorem is a marked family/stack trace identity.  It gives no
memberwise sign, RH or GRH criterion, chosen-member motive or compatible
system, global Euler-product identity, or average-to-principal-member
amplifier.  No external novelty claim is made.

From the repository root:

    python research/l-families/atlas/function_field/genus2_sym10_marked_trace_average.py --check
    python -O research/l-families/atlas/function_field/genus2_sym10_marked_trace_average.py --check
    python -m unittest tests.test_genus2_sym10_marked_trace_average -v
    python -O -m unittest tests.test_genus2_sym10_marked_trace_average -v
