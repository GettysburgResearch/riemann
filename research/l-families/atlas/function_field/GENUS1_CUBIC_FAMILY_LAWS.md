# Exact genus-one cubic family laws

Status: **DRAFT exact all-odd-field theorem with a stated standard modular-trace input**

Scope: monic squarefree cubics over an odd finite field, their genus-one
curves `y^2=D(x)`, exact trace and symmetric-character moments, and two
different affine quotients. The exhaustive regression is only for
`q=3,5,7,11,13` and inspects 4,023 candidate cubics. It is a check of the formulas,
not their proof.

Exact sources or dependencies: the orbit and character-sum arguments below
are native. The all-weight character identity uses the standard level-one
Eichler--Shimura/Grothendieck trace formula, stated precisely in (14). The
producer evaluates it only through weight 14, where the sole cusp term is the
weight-12 Ramanujan `Delta` trace.

What was actually run: exact prime-field polynomial and orbit enumeration at
`q=3,5,7,11,13`, exact integer moment evaluation through degree 12, and closed
Burnside formulas. There is no interpolation, floating point, curve database,
or exhaustive large-field scan.

Smallest remaining gap: none for the stated family laws. A source-pinned
external review of the standard modular-stack trace formula would be needed
before promoting the all-weight part into an integrated packet.

## 1. Normalization and the three different ensembles

Let `q` be an odd prime power and

\[
 \mathcal H_3(q)=\{D(X)=X^3+aX^2+bX+c:\operatorname{disc}(D)\ne0\}.
\]

There are

\[
 |\mathcal H_3(q)|=q^3-q^2=q^2(q-1)                                      \tag{1}
\]

such cubics. Put

\[
 E_D:Y^2=D(X),\qquad
 a_D=q+1-\#E_D(\mathbb F_q)=-\sum_{x\in\mathbb F_q}\chi(D(x)).             \tag{2}
\]

Thus the numerator of the zeta function is

\[
 L_D(T)=1-a_DT+qT^2.                                                        \tag{3}
\]

Three ensembles must not be conflated.

1. **Marked affine models.** These are the individual cubics in
   `H_3(q)`, averaged uniformly. A choice of monic equation and affine
   coordinate remains part of the object.
2. **The full affine branch quotient.** `AGL(1,q)` acts by

   \[
      D(T)\longmapsto D^{\alpha,\beta}(T)
       =\alpha^{-3}D(\alpha T+\beta).                                       \tag{4}
   \]

   This is a quotient of branch polynomials with infinity retained. It is
   not the quotient by elliptic-curve isomorphism.
3. **Elliptic curves over `F_q`.** An isomorphism between monic odd
   Weierstrass equations has

   \[
      X=u^2T+\beta,\qquad Y=u^3Z,
   \]

   and hence acts by

   \[
      D(T)\longmapsto u^{-6}D(u^2T+\beta).                                  \tag{5}
   \]

   The effective action therefore uses only square multipliers
   `alpha=u^2`. Its coarse orbits are exactly elliptic `F_q`-isomorphism
   classes. The group with parameters `(u,beta)` has the ineffective central
   kernel `u=+-1`; retaining that kernel gives the actual elliptic moduli
   groupoid and its full automorphism groups.

The distinction is visible in the trace. Changing variables in (2) gives

\[
 a_{D^{\alpha,\beta}}=\chi(\alpha)a_D.                                     \tag{6}
\]

A nonsquare multiplier takes an elliptic curve to its quadratic twist and
reverses its trace. Consequently the signed `L`-polynomial does **not**
descend to the full affine branch quotient. It does descend to the
square-affine/elliptic quotient. Even functions of the trace descend to both.

## 2. Exact elliptic-stack and model measures

If `[E]` ranges over elliptic `F_q`-isomorphism classes, orbit-stabilizer for
(5) gives

\[
 \#\{D\in\mathcal H_3(q):E_D\simeq E\}
   ={q(q-1)\over |\operatorname{Aut}_{\mathbb F_q}(E)|}.                    \tag{7}
\]

Summing (7) first with `f=1` and then with an arbitrary isomorphism-invariant
function proves

\[
 \boxed{\sum_{[E]}{1\over|\operatorname{Aut}_{\mathbb F_q}(E)|}=q},
 \qquad
 \boxed{{1\over|\mathcal H_3(q)|}\sum_D f(E_D)
   ={1\over q}\sum_{[E]}{f(E)\over|\operatorname{Aut}_{\mathbb F_q}(E)|}}. \tag{8}
\]

Uniform marked models are therefore exactly the normalized elliptic-stack
measure. They are not the uniform measure on coarse elliptic isomorphism
classes. If the ineffective `+-1` kernel is removed, the effective quotient
has stack cardinality `2q`, while the actual elliptic stack has cardinality
`q`; these are the same normalized probability measure.

For the full affine branch action, (1) and `|AGL(1,q)|=q(q-1)` similarly give
stack cardinality `q`. Its stack average agrees with the model average only
for statistics invariant under (4), such as `a_D^(2n)`.

## 3. Symmetric-power character theorem

Let `alpha_E,beta_E` be the roots of (3), so
`alpha_E+beta_E=a_E` and `alpha_E*beta_E=q`. Define

\[
 P_m(a_E,q)=\sum_{r=0}^m\alpha_E^{m-r}\beta_E^r,
 \quad P_0=1,\quad P_1=a_E,\quad
 P_m=a_EP_{m-1}-qP_{m-2}.                                                   \tag{9}
\]

This is the trace of `Sym^m H^1(E)`. Normalized to the compact group, it is

\[
 q^{-m/2}P_m(a_E,q)=U_m\!\left({a_E\over2\sqrt q}\right),                 \tag{10}
\]

the irreducible character of `USp(2)=SU(2)` of highest weight `m`.

For even `k`, let `S_k` denote level-one cusp forms of weight `k`. If
`q=p^r`, define the Frobenius-power Hecke trace

\[
 \Theta_k(q)=
 \operatorname{Tr}(T_{p^r}\mid S_k)
 -p^{k-1}\operatorname{Tr}(T_{p^{r-2}}\mid S_k),                           \tag{11}
\]

where the second term is zero for `r<2` and `T_1` is the identity. For one
Hecke eigenform with Satake roots `gamma_p,delta_p`, (11) is
`gamma_p^r+delta_p^r`. In particular

\[
 \Theta_{12}(p)=\tau(p),\qquad
 \Theta_{12}(p^r)=\tau(p^r)-p^{11}\tau(p^{r-2}).                            \tag{12}
\]

The second formula is important: for a nonprime field `Theta_12(q)` is not
in general `tau(q)`. For example

\[
 \Theta_{12}(9)=252^2-2\cdot3^{11}=-290790,
 \qquad \tau(9)=-113643.                                                    \tag{13}
\]

The standard level-one Eichler--Shimura/Grothendieck trace identity, in the
normalization (9), is

\[
 \boxed{
 \sum_{[E]/\mathbb F_q}{P_m(a_E,q)\over|\operatorname{Aut}_{\mathbb F_q}(E)|}
 =
 \begin{cases}
 q,&m=0,\\
 0,&m\text{ odd},\\
 -1-\Theta_{m+2}(q),&m\ge2\text{ even}.
 \end{cases}}                                                              \tag{14}
\]

This is the sole imported theorem in the all-weight moment result. Its
content is transparent here: the `-1` is the Eisenstein/boundary contribution
and `-Theta` is the cuspidal cohomology. It is valid in characteristic 3 as a
stack identity; no `p>3` short-Weierstrass assumption is being inserted.

A primary literature anchor is Kaplan--Petrow, *Elliptic curves over a finite
field and the trace formula*, especially the trivial-subgroup specialization
of their exact Chebyshev/Hecke moment formula
([arXiv:1510.03980](https://arxiv.org/abs/1510.03980)). Their treatment works
over prime powers and explicitly places the classical Birch--Ihara formulas
inside the trace-formula framework. Equation (14) is the corresponding
modular-stack normalization used here.

Combining (8), (10), and (14) gives the exact character moments

\[
 \boxed{
 \mathbb E_{D\in\mathcal H_3(q)}
 U_{2j}\!\left({a_D\over2\sqrt q}\right)
 =-{1+\Theta_{2j+2}(q)\over q^{j+1}},\quad j\ge1,}                          \tag{15}
\]

and every odd character moment is zero. The latter also follows elementarily
from the nonsquare-twist involution (6).

## 4. Every raw trace moment

The `SU(2)` character decomposition is the elementary identity

\[
 a^{2n}=\sum_{j=0}^n c_{n,j}q^{n-j}P_{2j}(a,q),\qquad
 c_{n,j}={2n\choose n-j}-{2n\choose n-j-1}.                                \tag{16}
\]

Here `c_(n,0)=C_n=(1/(n+1))*binom(2n,n)` is the `n`-th Catalan number.
Identity (16) follows either by induction from (9), or by counting the
highest-weight multiplicities in the `2n`-fold tensor power of the standard
`SU(2)` representation. Applying (14) proves, for every `n>=0`,

\[
 \boxed{
 W_{2n}(q):=\sum_{[E]}{a_E^{2n}\over|\operatorname{Aut}_{\mathbb F_q}(E)|}
 =C_nq^{n+1}-\sum_{j=1}^n
 c_{n,j}q^{n-j}\bigl(1+\Theta_{2j+2}(q)\bigr).}                            \tag{17}
\]

All odd sums vanish, and (7) yields the raw marked-model laws

\[
 \boxed{\sum_{D\in\mathcal H_3(q)}a_D^{2n}=q(q-1)W_{2n}(q)},\qquad
 \boxed{\mathbb E_D[a_D^{2n}]={W_{2n}(q)\over q}}.                         \tag{18}
\]

The character sum in (2) is `-a_D`, so (17)--(18) are simultaneously all
moments of the quadratic character sum.

The first seven stack-weighted even moments are

\[
\begin{aligned}
W_0={}&q,\\
W_2={}&q^2-1,\\
W_4={}&2q^3-3q-1,\\
W_6={}&5q^4-9q^2-5q-1,\\
W_8={}&14q^5-28q^3-20q^2-7q-1,\\
W_{10}={}&42q^6-90q^4-75q^3-35q^2-9q-1-\Theta_{12}(q),\\
W_{12}={}&132q^7-297q^5-275q^4-154q^3-54q^2-11q-1
           -11q\Theta_{12}(q).
\end{aligned}                                                              \tag{19}
\]

Thus the first automorphic correction appears at the tenth raw moment. This
is a theorem, not a polynomial guessed from the four regression fields.

## 5. Comparison with `USp(2)`

For Haar `U in USp(2)`, `tr(U)=2cos(theta)` has

\[
 \mathbb E_{\rm Haar}[\operatorname{tr}(U)^{2n}]=C_n,
 \qquad
 \mathbb E_{\rm Haar}[\operatorname{tr}(U)^{2n+1}]=0,                      \tag{20}
\]

and every nontrivial irreducible-character mean is zero. Dividing (17) by
`q^(n+1)` gives the exact finite-field comparison

\[
 \boxed{
 \mathbb E_D\left[\left({a_D\over\sqrt q}\right)^{2n}\right]
 =C_n-\sum_{j=1}^n
 {c_{n,j}\bigl(1+\Theta_{2j+2}(q)\bigr)\over q^{j+1}}.}                    \tag{21}
\]

For `n<=4` every relevant cusp space vanishes, so the discrepancy is an
explicit polynomial in `q^(-1)` beginning at `q^(-2)`. At `n=5`, the
weight-12 term first permits a `q^(-1/2)`-sized oscillation. Deligne's bound
`|Theta_k(q)|<=2 dim(S_k) q^((k-1)/2)` makes (21) converge to the Catalan
moment for every fixed `n`. Equation (15) gives the sharper character-by-
character comparison.

## 6. Exact Burnside orbit laws

### 6.1 Full affine branch quotient

For a nontranslation affine element, translate its unique fixed point to
zero. If its multiplier has order `d`, a fixed monic cubic has shape

\[
 D(S)=S^r h(S^d),\qquad r=3\bmod d.                                        \tag{22}
\]

Squarefreeness leaves only:

- order 2: `D=S^3+cS`, with `c!=0`, giving `q-1` fixed models;
- order 3: `D=S^3+c`, with `c!=0`, giving `q-1` fixed models.

There are `q*phi(d)` affine elements with multiplier order `d`. A nonzero
translation fixes a cubic only in characteristic 3, where its fixed models
are

\[
 D(S)=S^3-\beta^2S+c,qquad c\in\mathbb F_q,                               \tag{23}
\]

all squarefree. Burnside's lemma therefore gives

\[
 \boxed{N_{\rm branch}(q)
 =q+1+2\mathbf1_{3\mid q-1}+\mathbf1_{\operatorname{char}\mathbb F_q=3}.} \tag{24}
\]

The `+1` is the universal order-two branch symmetry. It does not mean that
the associated elliptic automorphism is rational: when `-1` is a nonsquare,
the order-two multiplier in (4) is a twist-identification rather than an
elliptic isomorphism.

### 6.2 Elliptic isomorphism classes

Restricting (22) to square multipliers changes the exceptional conditions.
Order 2 occurs exactly when `4|(q-1)`; order 3 occurs exactly when
`6|(q-1)`. The effective square-affine group has order `q(q-1)/2`, so

\[
 \boxed{N_{\rm ell}(q)
 =2q+2\mathbf1_{4\mid q-1}+4\mathbf1_{6\mid q-1}
      +2\mathbf1_{\operatorname{char}\mathbb F_q=3}.}                    \tag{25}
\]

These are coarse elliptic `F_q`-isomorphism classes. In particular (24) and
(25) count genuinely different quotients.

Writing `delta_branch=N_branch-q` and `delta_ell=N_ell-2q`, the usual
orbit-versus-stack comparison gives

\[
 \operatorname{TV}(\mu_{\rm branch,coarse},\mu_{\rm branch,stack})
 \le {\delta_{\rm branch}\over q},\qquad
 \operatorname{TV}(\mu_{\rm ell,coarse},\mu_{\rm model/stack})
 \le {\delta_{\rm ell}\over2q}.                                          \tag{26}
\]

Both are `O(q^(-1))`, but they are nonzero finite-field changes of measure.

## 7. Every positive even coarse moment

Burnside also gives a closed correction to (17), not merely the orbit count.
Let

\[
 C_{2n}(q)=\sum_{[E]/\mathbb F_q}^{\rm coarse}a_E^{2n},\qquad n\ge1.        \tag{27}
\]

The identity element contributes `2W_(2n)` after division by the effective
square-affine group. Only the three fixed strata above remain.

For the order-two (`j=1728`) stratum, which occurs when `4|(q-1)`, use the
Frobenius-compatible integers `A_4,B_4` with

\[
 q=A_4^2+B_4^2.                                                            \tag{28}
\]

More precisely, write `q=p^r`. If `p=1 mod 4`, choose
`p=a^2+b^2` and define `A_4+iB_4=(a+ib)^r`; changing associate or conjugate
does not change the symmetric expression below. If `p=3 mod 4`, necessarily
`r` is even and one takes `(A_4,B_4)=(p^(r/2),0)`. An arbitrary
two-square representation of `q` is not sufficient: at `q=25`, the relevant
ordinary Frobenius coordinates are `3,4`, not `5,0`.

The four quartic-twist traces of `Y^2=X^3+cX` are
`+-2A_4,+-2B_4`. The resulting Burnside correction is

\[
 R_4(n,q)=(2A_4)^{2n}+(2B_4)^{2n}.                                        \tag{29}
\]

It is independent of the associate/conjugate choice in (28).

For the order-three (`j=0`) stratum, which occurs when `6|(q-1)`, use the
Frobenius-compatible integers `A_6,B_6` with

\[
 q=A_6^2+3B_6^2.                                                           \tag{30}
\]

If `p=1 mod 3`, choose `p=a^2+3b^2` and define
`A_6+B_6 sqrt(-3)=(a+b sqrt(-3))^r`. If `p=2 mod 3`, the condition
`q=1 mod 6` forces even `r`, and one takes `(p^(r/2),0)`. As above, this
Frobenius-power prescription, rather than an arbitrary representation of
`q`, is load-bearing for extension fields.

The six sextic-twist traces of `Y^2=X^3+c` are
`+-2A_6`, `+-(A_6+3B_6)`, and `+-(A_6-3B_6)`. Hence

\[
 R_6(n,q)={4\over3}\left((2A_6)^{2n}
 +(A_6+3B_6)^{2n}+(A_6-3B_6)^{2n}\right).                                 \tag{31}
\]

Again the symmetric expression is independent of the permitted sign/unit
choice. Equations (29) and (31) are the usual elementary quartic- and
sextic-twist calculations; they also cover inert primes raised to an even
power by taking the second coordinate zero.

It remains to make the characteristic-3 term explicit. Write `q=3^r` and
put

\[
 H_{2n}(q)=\sum_{c\in\mathbb F_q}a_{X^3-X+c}^{2n}.                          \tag{32}
\]

The Artin--Schreier map `x->x^3-x` has kernel `F_3` and image the absolute-
trace-zero hyperplane. Resolving its three cosets with a quadratic Gauss sum
gives

\[
 H_{2n}(q)=
 \begin{cases}
 2\cdot3^{n-1}q^{n+1},&r\text{ odd},\\
 (4^n+2)q^{n+1}/3,&r\text{ even}.
 \end{cases}                                                              \tag{33}
\]

Indeed, for odd `r` the three trace values are `0,+-sqrt(3q)`, each on
`q/3` values of `c`. For even `r` they are `-2g,g,g`, with `g^2=q`, again
on three equal cosets. Scaling `X=beta Z` shows that every nonzero translation
has the same even moments. Its correction after Burnside division is

\[
 R_3(n,q)={2H_{2n}(q)\over q}
 =\begin{cases}
 4\cdot3^{n-1}q^n,&r\text{ odd},\\
 2(4^n+2)q^n/3,&r\text{ even}.
 \end{cases}                                                              \tag{34}
\]

Combining the strata proves the all-`q`, all-positive-even-moment formula

\[
 \boxed{
 C_{2n}(q)=2W_{2n}(q)
 +\mathbf1_{4\mid q-1}R_4(n,q)
 +\mathbf1_{6\mid q-1}R_6(n,q)
 +\mathbf1_{\operatorname{char}\mathbb F_q=3}R_3(n,q).}                  \tag{35}
\]

Uniform coarse elliptic averaging divides (35) by `N_ell(q)`, whereas the
model/stack average is `W_(2n)(q)/q`. These are exact but different laws.

Quadratic twist is an involution on coarse elliptic classes. Nonfixed classes
pair with traces `t,-t`, while a fixed class must have `t=0`; hence every odd
coarse moment also vanishes.

Finally, a full affine branch orbit either combines two square-affine orbits
with traces `t,-t`, or is a nonsplit trace-zero orbit. Therefore, for `n>=1`,

\[
 \boxed{
 \sum_{\mathcal H_3(q)/\mathrm{AGL}(1,q)}a_D^{2n}
 ={1\over2}C_{2n}(q).}                                                      \tag{36}
\]

Only the even power is meant in (36); a signed choice of `a_D` on a branch
orbit is not defined.

## 8. Frozen regression and interpretation firewall

The producer exhausts exactly the five tiny prime fields below.

| `q` | candidate cubics | squarefree models | branch orbits | elliptic classes |
|---:|---:|---:|---:|---:|
| 3 | 27 | 18 | 5 | 8 |
| 5 | 125 | 100 | 6 | 12 |
| 7 | 343 | 294 | 10 | 18 |
| 11 | 1331 | 1210 | 12 | 22 |
| 13 | 2197 | 2028 | 16 | 32 |

The `q=13` row is deliberately included because its square-affine Burnside
law contains both the order-two and order-three CM corrections at once. The
producer independently rebuilds trace histograms, both orbit partitions, stabilizer
histograms, model moments through degree 12, and the coarse even moments. The
total of 4,023 candidate cubics lies below the declared 20,000-candidate cap.

These computations authenticate the implementation and catch normalization
errors; they do not prove (14), (17), (24), (25), or (35). The proofs are the
stack trace identity, character algebra, Burnside fixed-locus classification,
CM twist calculation, and Artin--Schreier/Gauss-sum calculation above.

Nothing here transfers a finite-field distribution to number-field
`L`-functions. It proves no zero-free region, RH, or GRH. The `USp(2)`
comparison is an exact family-moment comparison, not a memberwise law.
