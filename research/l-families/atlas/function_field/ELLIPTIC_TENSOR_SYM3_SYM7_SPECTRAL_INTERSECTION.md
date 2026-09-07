# A degree-eight tensor / symmetric-seventh spectral intersection

Status: **exact integral raw intersection theorem for every odd prime power,
exact square-\(q\) Hasse-lattice count, exact residual-support certificate,
and source-locked bounded replay**

This packet classifies equality between
\(\operatorname{Std}(E_A)\otimes\operatorname{Sym}^3(E_B)\) and
\(\operatorname{Sym}^7(E_C)\) local factors. For integral raw traces over
an odd prime-power base, the only intersections are the two \(r=3\)
instances of the universal tensor/symmetric-power torus ladder. They occur
only when the base cardinality is a square. If \(q=p^{2k}\), their union has
exactly

\[
 \boxed{8p^{\lfloor k/4\rfloor}+8p^{\lfloor k/2\rfloor}-4}
 \tag{1}
\]

integral Hasse trace triples.

The proof is not inferred from the finite replay. It uses Chebyshev power
sums, Newton identities, three exact displayed-factor divisions, a small
ideal-membership identity, and univariate factorizations over \(\mathbf Q\).
The producer uses only Python standard-library exact arithmetic. It runs no
Groebner basis, floating-point calculation, random sampling, finite-field
enumeration, curve enumeration, or model enumeration.

## 1. Conventions, weights, and the typed comparison

Every elliptic input uses the geometric-trace convention

\[
 P_t(T)=1-tT+qT^2=(1-\alpha T)(1-\beta T),\qquad
 \alpha+\beta=t,\quad \alpha\beta=q.                     \tag{2}
\]

The geometric traces are \(A,B,C\). Choose \(s\) with \(s^2=q\), and put

\[
 u={A\over s},\qquad v={B\over s},\qquad z={C\over s}.   \tag{3}
\]

The tensor factor has degree eight and weight four. The symmetric-seventh
factor has degree eight and weight seven. Consequently the raw equality is
the typed, dilated equality

\[
 \boxed{
 P_{\operatorname{Std}(A)\otimes\operatorname{Sym}^3(B)}
       (q^{3/2}T)
 =P_{\operatorname{Sym}^7(C)}(T).}                       \tag{4}
\]

When \(q=s^2\) and the positive integer \(s\) is chosen, this reads

\[
 P_{\operatorname{Std}(A)\otimes\operatorname{Sym}^3(B)}(s^3T)
 =P_{\operatorname{Sym}^7(C)}(T).                        \tag{5}
\]

The factors are not equal in the same unscaled variable.

Let \(C_n(x)\) be the normalized torus trace polynomial

\[
 C_0(x)=2,\quad C_1(x)=x,\quad C_n(x)=xC_{n-1}(x)-C_{n-2}(x). \tag{6}
\]

Thus \(C_n(w+w^{-1})=w^n+w^{-n}\).

## 2. Exact normalized coefficient system

For \(1\le n\le4\), the tensor and target power sums are

\[
\begin{aligned}
 p_n^{\rm ten}&=C_n(u)\bigl(C_{3n}(v)+C_n(v)\bigr),\\
 p_n^{\rm tar}&=C_n(z)+C_{3n}(z)+C_{5n}(z)+C_{7n}(z).
\end{aligned}                                               \tag{7}
\]

Newton's identities determine the first four elementary coefficients;
reciprocal symmetry determines the rest. Writing
\(f_i=e_i^{\rm ten}-e_i^{\rm tar}\), exact expansion gives

\[
\begin{aligned}
f_1={}&uv^3-2uv-z^7+6z^5-10z^3+4z,\\
f_2={}&u^2v^4-3u^2v^2+2u^2+v^6-6v^4+10v^2\\
 &-z^{12}+11z^{10}-46z^8+91z^6-86z^4+34z^2-8,\\
f_3={}&u^3v^3-2u^3v+uv^7-5uv^5+5uv^3+2uv\\
 &-z^{15}+14z^{13}-79z^{11}+229z^9-359z^7
   +292z^5-106z^3+12z,\\
f_4={}&u^4+u^2v^6-4u^2v^4+4u^2v^2-4u^2
       +v^8-8v^6+21v^4-20v^2\\
 &-z^{16}+15z^{14}-92z^{12}+296z^{10}-533z^8
   +532z^6-277z^4+68z^2.
\end{aligned}                                               \tag{8}
\]

The producer rederives (8); it does not accept the display as input.

## 3. The two signed torus graphs

Put

\[
 C_2(z)=z^2-2,\qquad C_4(z)=z^4-4z^2+2.                  \tag{9}
\]

There are two universal graph families:

\[
\boxed{
 (u,v)=(\varepsilon C_4(z),\varepsilon z)
 \quad\hbox{or}\quad
 (u,v)=(\varepsilon z,\varepsilon C_2(z)),\qquad
 \varepsilon\in\{-1,1\}.}                                \tag{10}
\]

The sign is the same in both coordinates. Both the standard representation
and the symmetric cube are odd under the central sign, so simultaneously
negating the two inputs preserves every tensor root.

The two positive graph weight unions are

\[
 \{\pm4\}+\{\pm3,\pm1\}
 =\{\pm1\}+2\{\pm3,\pm1\}
 =\{\pm7,\pm5,\pm3,\pm1\}.                                \tag{11}
\]

The last multiset is exactly that of \(\operatorname{Sym}^7(w)\). The
producer also substitutes all four signed graphs into all four polynomials
in (8), obtaining sixteen zero residuals. These are maximal-torus
identities, not a representation homomorphism.

## 4. Small exact elimination certificate

Define

\[
 g(v)=v(v^2-2),\qquad
 t(z)=z(z^2-2)(z^4-4z^2+2).                               \tag{12}
\]

Then \(f_1=ug-t\). On \(g\ne0\), substitute \(u=t/g\), clear
denominators, and put

\[
 V=v^2,\quad Z=z^2,\quad
 D=(v^2-z^2)\bigl(v^2-(z^2-2)^2\bigr),\quad
 Q_{16}(Z)=Z^2-4Z+2.                                      \tag{13}
\]

Exact sparse polynomial division gives

\[
\begin{aligned}
N_2&=g^2f_2(t/g,v,z)=D(V-2)A(V,Z),\\
N_3&=g^3f_3(t/g,v,z)
    =Dvz(Z-2)Q_{16}(Z)(V-2)B(V,Z),\\
N_4&=g^4f_4(t/g,v,z)=D\mathcal C(V,Z).                    \tag{14}
\end{aligned}
\]

The two small quotients needed in the generic branch are

\[
\begin{aligned}
A={}&V^3+V^2Z^2-3V^2Z-4V^2+VZ^4-7VZ^3+13VZ^2-4VZ+6V\\
 &-Z^4+8Z^3-20Z^2+16Z-4,\\
B={}&V^3+V^2Z^2-3V^2Z-3V^2+VZ^3-7VZ^2+12VZ\\
 &+Z^4-8Z^3+20Z^2-16Z+4.
\end{aligned}                                               \tag{15}
\]

Exact subtraction gives the small ideal-membership identity

\[
 \boxed{A-B=-(V-2)(V-H(Z))},\qquad
 H(Z)=Z^4-8Z^3+20Z^2-16Z+4.                              \tag{16}
\]

If \(D\ne0\), \(V\ne2\), \(Z\notin\{0,2\}\), and
\(Q_{16}(Z)\ne0\), equations (14)--(16) force \(V=H(Z)\).
Direct substitution factors as

\[
\begin{aligned}
A(H(Z),Z)={}&(Z^2-5Z+5)(Z^2-4Z+2)^2\\
 &\cdot(Z^3-6Z^2+9Z-1)(Z^3-5Z^2+6Z-1).                  \tag{17}
\end{aligned}
\]

The \(V=2\) branch is controlled by

\[
 \mathcal C(2,Z)=Z^2(Z-2)^3(Z^2-4Z+2)^3.                 \tag{18}
\]

If \(g=0\), the first equation forces \(t(z)=0\), hence

\[
 Z=0,\qquad Z=2,\qquad\hbox{or}\qquad Z^2-4Z+2=0.        \tag{19}
\]

Thus every nongraph residual candidate lies over

\[
\begin{aligned}
R_{\rm cand}(Z)={}&Z(Z-2)(Z^2-4Z+2)(Z^2-5Z+5)\\
 &\cdot(Z^3-6Z^2+9Z-1)(Z^3-5Z^2+6Z-1).                 \tag{20}
\end{aligned}
\]

This is a directly replayed ideal-membership and factorization certificate,
not a runtime computer-algebra call.

### The \(Z=0\) original-system stratum

At \(z=0\), the first original equation is

\[
 uv(v^2-2)=0.                                             \tag{21}
\]

If \(v=0\), the second equation is \(2(u^2-4)=0\). If
\(v^2=2\), it is \(-4=0\), impossible. If \(u=0\), put
\(V=v^2\); the second and fourth equations factor as

\[
\begin{aligned}
f_2&=(V-4)(V^2-2V+2),\\
f_4&=V(V-4)(V^2-4V+5).
\end{aligned}                                               \tag{22}
\]

The exact Bezout identity

\[
\left({1\over2}-{V^2\over10}\right)(V^2-2V+2)
+\left({V\over10}+{1\over5}\right)V(V^2-4V+5)=1          \tag{23}
\]

forces \(V=4\). The only points over \(Z=0\) are

\[
 (u,v)=(\pm2,0),(0,\pm2),                                \tag{24}
\]

and all four lie on (10). Therefore \(Z=0\) is not a nongraph residual
factor.

### Genuine residual factors and the classification boundary

Exact univariate remainder calculations exhibit nongraph strata on every
other irreducible factor:

\[
\begin{array}{c|c}
\text{relation for }Z&\text{one trace description}\\
\hline
Z=2&u=0,\ v=\pm z\\
Z^2-4Z+2=0&u=0,\ v=\pm C_3(z)\\
Z^2-4Z+2=0&u=\pm C_3(z),\ v=\pm C_2(z)
  \quad\text{(independent signs)}\\
Z^2-5Z+5=0&(u,v)=\varepsilon(z,C_6(z))\\
Z^3-6Z^2+9Z-1=0&(u,v)=\varepsilon(C_2(z),C_5(z))\\
Z^3-5Z^2+6Z-1=0&(u,v)=\varepsilon(C_2(z),C_3(z)).
\end{array}                                                \tag{25}
\]

Hence the exact squarefree nongraph \(Z\)-support is (20) with \(Z\)
removed. The fixture does not claim that (25), with multiplicities, is a
complete enumeration of every individual algebraic point. It records exact
support and exact witness strata. The factors correspond to finite torus
orders \(8,16,20,9/18\), and \(7/14\), respectively.

## 5. Complete integral raw theorem

Let \(q=p^e\) for an odd prime \(p\), and let \(A,B,C\in\mathbf Z\).
Because

\[
 Z=z^2={C^2\over q}\in\mathbf Q,                         \tag{26}
\]

the four nonlinear factors in (20) cannot vanish rationally. The two
quadratics have nonsquare discriminants \(8\) and \(5\). Each monic cubic
has rational-root candidates only \(\pm1\), and both fail. The \(Z=0\)
case is graph-only. The remaining value \(Z=2\) would require

\[
 C^2=2q,                                                  \tag{27}
\]

which is impossible for an odd prime power.

Away from the special strata, \(D=0\) and \(f_1=0\) recover exactly
the signed graphs in (10). Therefore:

> **Integral raw intersection theorem.** For every odd prime power \(q\)
> and every \(A,B,C\in\mathbf Z\), the typed degree-eight factor equality
> (4) holds if and only if \(q\) is a square, say
> \(q=s^2\) with \(s\in\mathbf Z_{>0}\), and, for one
> \(\varepsilon\in\{-1,1\}\), either
>
> \[
> B=\varepsilon C,\qquad
> s^3A=\varepsilon(C^4-4qC^2+2q^2),                      \tag{28}
> \]
>
> or
>
> \[
> A=\varepsilon C,\qquad
> sB=\varepsilon(C^2-2q).                                \tag{29}
> \]

For nonsquare \(q\), the first graph gives

\[
 q^2A=\varepsilon s(C^4-4qC^2+2q^2).                    \tag{30}
\]

Rational-versus-irrational separation would force \(A=0\) and
\(Z^2-4Z+2=0\), impossible for rational \(Z\). The second graph gives

\[
 qB=\varepsilon s(C^2-2q),                               \tag{31}
\]

forcing (27). Hence the nonsquare intersection is empty.

## 6. Square-\(q\) divisibility and exact count

Let \(q=p^{2k}\) and \(s=p^k\). On branch I, integrality requires

\[
 s^3\mid F(C),\qquad F(C)=C^4-4s^2C^2+2s^4.             \tag{32}
\]

If \(d=v_p(C)<k\), the three terms have valuations
\(4d,2k+2d,4k\), and the first is uniquely minimal. If \(d\ge k\),
\(s^4\mid F\). Thus

\[
 s^3\mid F(C)\quad\Longleftrightarrow\quad
 p^{\lceil3k/4\rceil}\mid C.                             \tag{33}
\]

Within \(|C|\le2s\), branch I has

\[
 8p^{\lfloor k/4\rfloor}+2                               \tag{34}
\]

triples across its two signs. Similarly,

\[
 s\mid C^2-2s^2
 \quad\Longleftrightarrow\quad
 p^{\lceil k/2\rceil}\mid C,                             \tag{35}
\]

so branch II has

\[
 8p^{\lfloor k/2\rfloor}+2.                              \tag{36}
\]

The other Hasse bounds are automatic because \(C_4\) and \(C_2\) map
the compact trace interval \([-2,2]\) into itself.

For the overlap, write the graph signs as \(\varepsilon,\delta\), and put
\(\eta=\delta/\varepsilon\). Equality requires

\[
 C_4(z)=\eta z,\qquad z=\eta C_2(z).                     \tag{37}
\]

For \(\eta=1\), \(z=2,-1\); for \(\eta=-1\), \(z=1,-2\).
Each value has two choices of \(\varepsilon\), giving exactly eight
overlap triples. Subtracting them from (34)+(36) proves (1).

This is a Hasse coefficient-lattice count. It does not assert the existence
of three linked elliptic curves or a geometric correspondence.

## 7. Compact moment context

An exact Clebsch--Gordan multiplicity recursion gives the trace moments
through degree eight

\[
\begin{aligned}
\operatorname{Std}\otimes\operatorname{Sym}^3
  &: [1,0,1,0,8,0,170,0,5096],\\
\operatorname{Sym}^7
  &: [1,0,1,0,8,0,260,0,11096].
\end{aligned}                                               \tag{38}
\]

The first family uses independent Haar elements in its two \(SU(2)\)
factors, so its moments are the products of the standard and symmetric-cube
moments. The fingerprints alias through degree four and first separate at
degree six, \(170\) versus \(260\). Both fourth moments are \(8\), versus
\(3\) for a generic \(USp(8)\) standard trace. These are compact Haar
fingerprints only; they do not recover arithmetic origin or imply a
local-to-global theorem.

## 8. Bounded authenticated replay

The producer authenticates, by schema, canonical payload, LF-normalized
fixture hash, and LF-normalized producer hash:

1. genus1_cubic_family_laws, for the five locked trace supports;
2. elliptic_symmetric_power_full_factor_sign_aliases, for the base-factor
   and geometric-trace convention;
3. elliptic_symmetric_power_cyclotomic_spectral_aliases, for finite-order
   context;
4. elliptic_tensor_sym2_sym5_spectral_intersection, for the all-\(r\)
   ladder specialized here at \(r=3\).

It checks all

\[
 7^3+9^3+11^3+13^3+15^3=7{,}975                         \tag{39}
\]

ordered triples in the locked \(q=3,5,7,11,13\) supports. Each has zero
hits, as the nonsquare theorem requires. It also checks all \(13^3\) Hasse
triples at \(q=9\) and all \(21^3\) at \(q=25\). Each square row has
exactly twelve hits, agreeing with (1). Factor construction is cached by
\((A,B)\) and by \(C\); this is a small exact coefficient replay, not a
field or curve enumeration.

The accounted ledger remains strictly below its exclusive 25,000-unit cap.
All caps and source checks are explicit runtime branches and survive
optimized Python mode.

## 9. Scope firewalls

- The exact nongraph \(Z\)-support is not renamed a complete point-by-point
  algebraic residual classification.
- Torus spectral graphs do not produce a representation homomorphism.
- One-place factor equality supplies no motive, compatible system, Euler
  product identity, or automorphic transfer.
- Integral Hasse triples are not asserted to be simultaneously realized by
  linked curves.
- No literature-priority claim is made for the Chebyshev identities.
- Nothing here proves a zero-free region, RH, or GRH.

## 10. Reproduction

From the repository root:

```text
python -B research/l-families/atlas/function_field/elliptic_tensor_sym3_sym7_spectral_intersection.py --check
python -B -O research/l-families/atlas/function_field/elliptic_tensor_sym3_sym7_spectral_intersection.py --check
python -B -m unittest tests.test_elliptic_tensor_sym3_sym7_spectral_intersection
python -B -O -m unittest tests.test_elliptic_tensor_sym3_sym7_spectral_intersection
```
