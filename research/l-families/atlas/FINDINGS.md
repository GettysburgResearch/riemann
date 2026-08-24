# Cross-family findings

Status: exact finite statements are separated below from discovery evidence and
open nominations. Nothing in this note proves RH or GRH.

## 1. Exact invariant: unitary local top coefficient

At each included unramified prime, the reciprocal local factor is put in its
unitary variable. In the Phase-0 rows:

```text
GL(1):  1-chi(p)T,                  |top coefficient|=1;
GL(2):  1-(a_p/sqrt(p))T+T^2,       top coefficient=1.
```

Every checked row satisfies this control exactly. It is a normalization
invariant, not a new theorem about zeros. It is valuable operationally because
it catches an unshifted GL(2) factor before different degrees or weights are
pooled.

The superficially stronger statement `|a_p/p^(w/2)|=1` is false. For each of
the three elliptic-curve rows, already at `p=2`, `a_p=-2`, so the normalized
prime coefficient has square `a_p^2/p=2`, not `1`. Zeta and the quadratic
character modulo 5 do have exact second and fourth moment `1` on the declared
window. Thus a GL(1) unit-amplitude pattern is not a degree-free detector law.

For reference, the exact GL(2) finite means through `p<=43` are:

| LMFDB row | imported rank | `M2` | display decimal | `M4` | display decimal |
|---|---:|---:|---:|---:|---:|
| `11.a2` | 0 | `9536727364483/14030349555495` | `0.679721` | `13680377587284913295751529/15142362203798364929591925` | `0.903451` |
| `37.a1` | 1 | `2284882048044/2371850295815` | `0.963333` | `821205796921744526847416/432744140442900231270325` | `1.897671` |
| `389.a1` | 2 | `144147769429982797/91579329321690210` | `1.574021` | `2016668514750617670001638172310929/599055254215042018487340800703150` | `3.366415` |

The decimals are display-only conversions of the exact fractions. The apparent
rank ordering is not evidence of a rank law: conductor, curve, and sample size
all change, and there is only one selected object per rank.

## 2. Exact finite result: the classical reciprocal filter has no common sign

Let `mu_L^cl(n)` be the reciprocal coefficients in the classical Euler
variable and use inclusive endpoints in

\[
W_L^{\rm cl}(X)=(I-\sqrt2S_2)(I-S_2)^2
\sum_{n\le X}\mu_L^{\rm cl}(n),
\qquad S_2M(X)=M(\lfloor X/2\rfloor).
\]

The filter expansion and its double root at `S_2=1` and root at
`S_2=1/sqrt(2)` are checked exactly in `Q(sqrt(2))`. Every reciprocal
coefficient through 256 is generated from the declared local factors, including
the bad factors at 11 and 37. The exact rows are:

| object | `X=32` | `X=64` | `X=128` | `X=256` |
|---|---:|---:|---:|---:|
| zeta | `-4-2sqrt(2)` (-) | `6+4sqrt(2)` (+) | `-4-6sqrt(2)` (-) | `2+4sqrt(2)` (+) |
| quadratic `chi_5` | `-1+sqrt(2)` (+) | `1+sqrt(2)` (+) | `3-sqrt(2)` (+) | `-7-3sqrt(2)` (-) |
| `11.a2`, rank metadata 0 | `-2+2sqrt(2)` (+) | `-1+2sqrt(2)` (+) | `-31+sqrt(2)` (-) | `7+31sqrt(2)` (+) |
| `37.a1`, rank metadata 1 | `14-19sqrt(2)` (-) | `63-14sqrt(2)` (+) | `122-63sqrt(2)` (+) | `259-122sqrt(2)` (+) |
| `389.a1`, rank metadata 2 | `34-24sqrt(2)` (+) | `92-34sqrt(2)` (+) | `301-92sqrt(2)` (+) | `579-301sqrt(2)` (+) |

Thus even this source-faithful common algebra does not produce a common finite
sign across the five objects. This is useful falsification, not a limiting law:
there are only four endpoints and one selected curve at each imported rank.
Moreover the GL(2) rows deliberately use integral classical coefficients. For
motivic weight one their unitary counterparts satisfy
`mu_unitary(n)=mu_classical(n)/sqrt(n)`, whereas the weight-zero GL(1) map is
trivial. Raw magnitudes in the table are therefore not cross-degree moments.

No zeta-specific weighted-`L2` abscissa theorem is transferred. The next valid
family question is a unitary, source-locked moment such as Target C, with local
densities and bad primes explicit.

## 3. Exact refutation: purity does not force the toy signed coefficient probe

For every monic squarefree cubic `D` over `F_5[T]`, the exact computation gives

\[
L_D(u)=1+A_Du+5u^2,
\qquad A_D^2\le16<20.
\]

Consequently both reciprocal roots have modulus `sqrt(5)`. Direct Moebius sums
and the formal reciprocal recurrence also agree through degree three for every
member. Nevertheless, with

\[
B_D(n)=\sum_{\deg f=n}\mu(f)\chi_D(f),
\qquad H_D(n)=5^{-n/2}B_D(n),
\qquad C_D=H_D(1)H_D(2),
\]

the 100-member family has

```text
C_D < 0: 40 members
C_D = 0: 20 members
C_D > 0: 40 members
family mean numerator B_D(1)B_D(2): exactly 0
```

This refutes the naive universalization “Frobenius purity determines a
memberwise signed reciprocal-coefficient correlation.” It simultaneously
exhibits the family/member gap: perfect family cancellation coexists with both
memberwise signs.

This does **not** refute canonical `XD`, `HCNC`, or physical occupancy. `C_D` is
an explicitly labeled toy lag-one probe. A genuine port must derive its degree
kernel from the same reciprocal-L source and preserve the relevant carrier.

### Genus-one control: every moment exposes the modular contribution

The cubic pilot sits inside an exact all-odd-prime-power benchmark. With

\[
E_D:y^2=D(x),\qquad a_D=q+1-\#E_D(\mathbb F_q),
\qquad L_D(T)=1-a_DT+qT^2,
\]

uniform monic squarefree cubic models are exactly the normalized elliptic-stack
measure:

\[
\sum_{[E]/\mathbb F_q}\frac1{|\operatorname{Aut}_{\mathbb F_q}(E)|}=q,
\qquad
\mathbb E_D f(E_D)=\frac1q
\sum_{[E]}\frac{f(E)}{|\operatorname{Aut}_{\mathbb F_q}(E)|}.
\]

If `P_m(a,q)` is the `Sym^m H^1` trace and `Theta_k(q)` is the Frobenius-power
Hecke trace on level-one cusp forms, the standard modular-stack trace formula
gives

\[
\sum_{[E]}\frac{P_m(a_E,q)}{|\operatorname{Aut}(E)|}
=\begin{cases}
q,&m=0,\\
0,&m\text{ odd},\\
-1-\Theta_{m+2}(q),&m>0\text{ even}.
\end{cases}
\]

Consequently every raw even moment has the exact form

\[
W_{2n}(q)=C_nq^{n+1}
-\sum_{j=1}^n c_{n,j}q^{n-j}\bigl(1+\Theta_{2j+2}(q)\bigr),
\qquad
c_{n,j}=\binom{2n}{n-j}-\binom{2n}{n-j-1}.
\]

The Catalan leading term is the `USp(2)` Haar moment. Since the level-one cusp
spaces below weight 12 vanish, the first genuinely automorphic correction is
`-Theta_12(q)` in `W_10`; for a prime field it is `-tau(q)`, while for a prime
power it is the Frobenius-power correction
`Theta_12(p^r)=Tr(T_(p^r))-p^11 Tr(T_(p^(r-2)))`, not generally `tau(p^r)`.
This makes genus one a useful control for higher-genus searches: boundary terms
appear before cuspidal cohomology, and the latter first becomes visible only in
a sufficiently high moment.

There is also a quotient firewall. The full affine branch action contains a
nonsquare multiplier and identifies quadratic twists, so signed trace does not
descend to that quotient. The square-affine quotient gives elliptic
`F_q`-isomorphism classes, where it does. Their exact coarse counts are

\[
N_{\rm branch}=q+1+2\mathbf1_{3\mid q-1}
+\mathbf1_{\operatorname{char}\mathbb F_q=3},
\]

\[
N_{\rm ell}=2q+2\mathbf1_{4\mid q-1}
+4\mathbf1_{6\mid q-1}
+2\mathbf1_{\operatorname{char}\mathbb F_q=3}.
\]

The formulas, both orbit partitions, and moments through order 12 are frozen
independently at `q=3,5,7,11,13`. This is a synthesis of classical
Eichler--Shimura/Birch--Ihara structure with explicit family and quotient
bookkeeping, not a claim that the modular trace theorem itself is new.

### The elliptic symmetric cube is a nodal rank-one family inside `USp(4)`

For `P_E(T)=1+AT+qT^2`, the genuine symmetric-cube representation has the
exact factor

\[
1+(A^3-2qA)T+q(A^4-3qA^2+2q^2)T^2
+q^3(A^3-2qA)T^3+q^6T^4.
\]

With normalized base trace `t_0=-A/sqrt(q)`, its first two normalized
coefficients are

\[
x=t_0^3-2t_0,
\qquad y=t_0^4-3t_0^2+2,
\]

and eliminate to the exact curve

\[
-x^4+x^2y+x^2+y^3-2y^2=0.
\]

The normalization is generically recovered by
`t_0=x(y-1)/(x^2-y)`. The curve has exactly three real ordinary nodes
`(-1,1),(0,0),(1,1)` and no cusps. Thus the functorial compact image is
rank one inside the rank-two `USp(4)` coefficient region. Its first trace
separation is already

\[
E_{\operatorname{Sym}^3(SU(2))}(x^4)=4,
\qquad E_{USp(4)}(x^4)=3.
\]

The folds interact unexpectedly with arithmetic. For odd `q`,

\[
(t_1^3-2qt_1)-(t_2^3-2qt_2)
=(t_1-t_2)(t_1^2+t_1t_2+t_2^2-2q),
\]

and the quadratic factor cannot vanish modulo four. Hence the symmetric-cube
trace is injective on integral traces: no real trace fiber contains two
arithmetic lattice points. This does not mean the lattice misses every folded
fiber. Indeed `(x,y)=(0,0)` is on the coefficient curve, but its two
normalization preimages require `t^2=2q`, impossible for odd `q`; it is an
explicit arithmetic false positive to curve-only recognition.

The locked genus-one theorem gives exact all-odd-`q` laws, for example

\[
E(y)=1-q^{-3},
\qquad E(x^2)=1-q^{-2}-q^{-3}-q^{-4},
\]

and exposes the first `Theta_12(q)` terms in selected degree-12 observables.
The frozen `q=3,5,7,11,13` rows transform only 55 source atoms representing
3,650 models. The symmetric-cube lift and local factor are classical; the
nodal packaging, lattice lemma, and finite-family defects are project-specific
calculations without a literature-priority claim.

## 4. Exact genus-two theorem: the first toy-minor mean for all odd prime powers

For each odd prime power `q`, let `H_5(q)` be all monic squarefree quintics over
`F_q[T]`. For `C_D:y^2=D(x)`, write

\[
P_D(u)=1+a_Du+b_Du^2+qa_Du^3+q^2u^4,
\qquad K_D=qa_D^2-b_D^2.
\]

The guarded computation exhausts `H_5(q)` only for `q=3,5,7`. It uses exact
`F_q` and `F_{q^2}` character sums, not numerical roots or per-member Euler
enumeration. The smallest field also retains the independent point-count,
purity, reciprocal-coefficient, and involution checks from the first pilot.

| `q` | members | `K_D<0 / =0 / >0` | exact mean `K_D/q^2` |
|---:|---:|---:|---:|
| 3 | 162 | `102 / 12 / 48` | `-104/243` |
| 5 | 2,500 | `1650 / 50 / 800` | `-1994/3125` |
| 7 | 14,406 | `9702 / 336 / 4368` | `-12340/16807` |

These member rows have an exact geometric compression. For
`alpha in F_q^*` and `beta in F_q`, set

\[
D^{\alpha,\beta}(T)=\alpha^{-5}D(\alpha T+\beta).
\]

This is a right action of `AGL(1,F_q)` on monic squarefree quintics. The base
change of variables and the fact that every base-field scalar is a square in
`F_{q^2}` give

\[
a_{D^{\alpha,\beta}}=\chi_q(\alpha)a_D,
\qquad b_{D^{\alpha,\beta}}=b_D,
\qquad K_{D^{\alpha,\beta}}=K_D.
\]

Choosing `beta=0` and a nonsquare `alpha` gives a sign-reversing symmetry of
the uniform multiset of coefficients. Hence, for
every odd prime power and every `r>=0`,

\[
\sum_D a_D^{2r+1}\Phi(a_D^2,b_D)=0
\]

for every function `Phi`. In particular every odd trace moment vanishes
exactly, and the joint coefficient distribution is invariant under
`(a,b)->(-a,b)`. This is an all-field symmetry lemma, not evidence for the
even moments or equidistribution.

Thus every sign and moment contribution is orbit-invariant. Exhaustively
checking all 656,024 member-action pairs gives:

| `q` | group order | affine orbits | orbit-size histogram | stabilizer-order histogram | negative / zero / positive orbits |
|---:|---:|---:|---|---|---:|
| 3 | 6 | 29 | `3:4, 6:25` | `1:25, 2:4` | `19 / 2 / 8` |
| 5 | 20 | 132 | `1:1, 4:1, 5:3, 10:6, 20:121` | `1:121, 2:6, 4:3, 5:1, 20:1` | `86 / 4 / 42` |
| 7 | 42 | 349 | `21:12, 42:337` | `1:337, 2:12` | `237 / 8 / 104` |

Most orbits are free. The characteristic-five exception
`D(T)=T^5-T` is fixed by all 20 affine elements and has `K_D=-100`; this is a
concrete warning that a uniform average over orbit representatives is not the
family average. Orbit-size weighting recovers every member moment, histogram,
and sign count exactly. The quotient should nevertheless be useful in a
higher-moment proof: it isolates automorphism strata and can cut a symmetry-
aware computation from 17,068 members to 510 weighted representatives.

The family measure can now be stated without ambiguity. Orbit-stabilizer gives

\[
\sum_{[D]}\frac1{|\operatorname{Stab}(D)|}=q^3,
\]

so uniform equations are exactly the stabilizer-weighted measure on this
marked affine quotient, not the uniform measure on coarse representatives.
Burnside's lemma gives the all-odd-`q` coarse count

\[
N_q=q^3+q-1+2\mathbf1_{4\mid q-1}
+4\mathbf1_{5\mid q-1}+\mathbf1_{\operatorname{char}F_q=5}.
\]

The exact coarse-versus-affine-stack total-variation distances at `q=3,5,7`
are `50/783`, `77/1500`, and `2022/119707`. At `q=5`, the orbit fixed by the
entire affine group has coarse weight `1/132` but marked-stack weight `1/2500`,
an amplification by `625/33`. This explains a finite-family bias mechanism;
it is not the full unpointed curve stack.

The same fixed-locus argument extends to every odd hyperelliptic degree
`n=2g+1`. The marked affine-stack cardinality is `q^(2g-1)`, while the exact
coarse orbit count is, with `p=char(F_q)` and `S_m(q)` the number of monic
squarefree degree-`m` polynomials,

\[
q^{2g-1}+
\sum_{\substack{d\mid q-1,\ d\ge2\\ n\bmod d\in\{0,1\}}}
\varphi(d)\frac{q^{\lfloor n/d\rfloor}-(-1)^{\lfloor n/d\rfloor}}{q+1}
+\mathbf1_{p\mid n}\frac{S_{n/p}(q)}q.
\]

Its universal leading correction comes from affine involutions and equals
`(q^g-(-1)^g)/(q+1)`. At fixed genus, the orbit-count excess relative to the
stack mass is therefore `q^(-g)` to leading order. This is a presentation
census, not a hyperelliptic moduli count or a Frobenius law.

Before extracting an odd degree, the same fixed-locus classification gives one
rational series for every degree. With

\[
S_q(u)=\frac{1-qu^2}{1-qu},\qquad A_q(u)=\frac{S_q(u)}{1+u},
\]

and `O_(q,n)` the number of affine orbits of monic squarefree degree-`n`
polynomials,

\[
\sum_{n\ge0}O_{q,n}u^n=
\frac{S_q(u)+q\sum_{\substack{d\mid q-1\\d\ge2}}
\varphi(d)(1+u)A_q(u^d)+(q-1)S_q(u^p)}{q(q-1)}.
\]

This exposes an exact automorphism-resonance spectrum: an order-`d`
multiplicative symmetry appears only in degrees `0,1 mod d`, while additive
translation symmetry appears only in degrees divisible by
`p=char(F_q)`. The all-genus odd-degree theorem is coefficient extraction from
this series; the even-degree terms are presentation counts, not an assertion
that the marked even- and odd-degree moduli problems coincide.

Those three rows suggested a formula, but they are no longer its evidence of
proof. The separate DRAFT note
[`GENUS2_MOMENT_IDENTITY.md`](function_field/GENUS2_MOMENT_IDENTITY.md) gives a
complete squarefree-Moebius calculation, and a bounded exact `Q[q]` certificate
checks its degree-two, quartic-factorization, and mixed quartic-reweight tables
and polynomial algebra in 2,925 operations. Independently of the three scans,
it proves for every odd prime power

\[
\begin{aligned}
\mathbb E(a_D^2)
 &=q-1+\frac{q^2+q-2}{q^3},\\
\mathbb E(a_D^4)
 &=3q^2-7q+5+\frac{12}{q}-\frac{14}{q^2}-\frac{11}{q^3},\\
\mathbb E(a_D^2b_D)
 &=\frac{(q+1)(q^2-2q+3)(2q^2-2q-1)}{q^3},\\
\mathbb E(b_D)
 &=q-1+\frac{q^2-1}{q^3},\\
\mathbb E(b_D^2)
 &=2q^2-3q+2+\frac{q^2-3q-1}{q^3},\\
\mathbb E(K_D)
 &=-(q-1)^2+\frac{q+1}{q^3}.
\end{aligned}
\]

The fourth trace moment comes from an exact reweighting of the five
linear-only rows in the same quartic factorization table. Equivalently,

\[
\sum_{D\in\mathcal H_5}a_D^4
=q(q-1)(q+1)(3q^4-10q^3+15q^2-3q-11).
\]

It follows independently of the scans that
`E[(a_D/sqrt(q))^4] -> 3`, the `USp(4)` trace target. This settles the
`q^2 a_D^4` part of

\[
\sum_DK_D^2=q^2\sum_Da_D^4-2q\sum_Da_D^2b_D^2+\sum_Db_D^4.
\]

The `a_D^2b_D^2` and `b_D^4` parts remain open; they require degree-six and
degree-eight marked character correlations rather than another fit to three
fields. The newly proved `a_D^2b_D` moment is a distinct quartic correlation
and is used below to resolve two more representation channels.

The 74-signature roadmap has a useful exact conductor census. Grouping by the
degree of the odd radical gives

| block | radical-degree signature counts |
|---|---|
| `M22` | `0:4, 2:8, 4:5, 6:3` |
| `B4` | `0:9, 2:16, 4:17, 6:7, 8:5` |

Only three `M22` signatures have generic radical degree six. Their weighted
leading coefficients are `1/4, 1/2, 1/4`. Only five `B4` signatures have
generic radical degree eight, with leading coefficients
`1/16, 1/4, 3/8, 1/4, 1/16`. Each list sums to one; all lower-radical strata
have smaller polynomial degree. Thus the leading tuple space is a binomial
mixture of just three and five collision-free conductor types, respectively.
The binomial weights reflect the asymptotic half-split/half-irreducible choice
for each monic quadratic slot. This is exact combinatorics, not a character-sum
estimate, but it sharply localizes where a leading asymptotic proof must begin.

The new first moment of `b_D` has a useful representation-theoretic payoff.
For the normalized Frobenius class, exact `C_2` character identities give

\[
\frac{b_D}{q}=1+\chi_{0,1},\qquad
\frac{a_D^2}{q}=1+\chi_{0,1}+\chi_{2,0},
\]

and

\[
\frac{b_D^2}{q^2}=2+2\chi_{0,1}+\chi_{2,0}+\chi_{0,2}.
\]

The two additional exact decompositions are

\[
\frac{a_D^2b_D}{q^2}=2+3\chi_{0,1}+3\chi_{2,0}+\chi_{0,2}+\chi_{2,1},
\]

and

\[
\frac{a_D^4}{q^2}=3+5\chi_{0,1}+6\chi_{2,0}+2\chi_{0,2}
+3\chi_{2,1}+\chi_{4,0}.
\]

Solving these five equations using the proved coefficient moments isolates an
exact low-weight family profile for every odd prime power:

\[
\left\langle\chi_{0,1}\right\rangle_q
=-\frac1q+\frac1{q^2}-\frac1{q^4},\qquad
\left\langle\chi_{2,0}\right\rangle_q
=\frac1{q^3}-\frac1{q^4},\qquad
\left\langle\chi_{0,2}\right\rangle_q
=-\frac1q-\frac1{q^5},
\]

\[
\left\langle\chi_{2,1}\right\rangle_q
=\frac2{q^3}-\frac1{q^4}-\frac2{q^5},\qquad
\left\langle\chi_{4,0}\right\rangle_q=-\frac3{q^5}.
\]

Thus the two low `omega_2` channels have a leading `q^{-1}` bias, the
`2*omega_1` and `(2,1)` channels are suppressed to `q^{-3}`, and the `(4,0)`
channel first appears at `q^{-5}`. All five tend to zero as Haar orthogonality
predicts. This exact anisotropy resolves every nontrivial channel in the trace
fourth power and is stronger information than the combined toy-minor mean.

It also sharpens the second-moment target. If

\[
H=\chi_{0,4}+\chi_{2,2}+2\chi_{0,3},
\]

then the virtual obstruction splits as `F^2-(Tr U)^4=H+L`, where the proved
five-channel profile gives

\[
\langle L\rangle_q
=-\frac1q-\frac1{q^2}-\frac6{q^3}+\frac6{q^4}.
\]

Consequently the second-moment limit is equivalent to the single honest
high-weight assertion `mean(H)->0`; no cancellation among unknown virtual
low-weight terms remains. A new exact change of basis makes the three missing
raw moments triangular:

```text
R3  = chi_(0,3)                         <-> b_D^3
R22 = chi_(0,3)+chi_(2,2)              <-> a_D^2 b_D^2
R4  = chi_(0,4)+3chi_(2,2)+4chi_(0,3)  <-> b_D^4.
```

All other terms in these packets already have proved family means. A bounded
cubic-moment audit finds 23 factor signatures, including four generic
degree-six types with mixture `(1,3,3,1)/8`. Their primitive `p_1,p_2`
coefficients do not cancel signaturewise, proving that the next step is a
genuine trace average rather than polynomial bookkeeping.

At `q=3,5,7`, the exact channel means match the sparse continuation

\[
\langle\chi_{0,3}\rangle_q\stackrel{?}{=}\frac{q^4-2q-1}{q^6},\quad
\langle\chi_{2,2}\rangle_q\stackrel{?}{=}
\frac{2q^3-q^2-2q-2}{q^6},\quad
\langle\chi_{0,4}\rangle_q\stackrel{?}{=}-\frac{2q^2+1}{q^7}.
\]

If true, these give

\[
\langle H\rangle_q\stackrel{?}{=}
\frac2{q^2}+\frac2{q^3}-\frac1{q^4}-\frac8{q^5}
-\frac4{q^6}-\frac1{q^7},
\qquad q^2\langle H\rangle_q\to2.
\]

The formula is a structured three-field conjecture, not a theorem. It
supersedes `9/4` as the preferred sparse target but does not falsify anything:
the earlier `9/4` value was only a visual cluster of the same three points.
Only `q=5` samples `chi_q(-1)=+1`, so a reciprocity branch remains unresolved.

Therefore

\[
\mathbb E(K_D/q^2)
=-\left(1-\frac1q\right)^2+\frac{q+1}{q^5}
\longrightarrow -1.
\]

The exact reciprocal identity

\[
B_D(1)B_D(3)-B_D(2)^2=qa_D^2-b_D^2
\]

turns this into an all-odd-prime-power first-moment theorem for the normalized toy Hankel
minor. The proof handles the even primitive quartic-character correction and
the `q=3` edge explicitly. The frozen scans are regression controls only.

The compact-group calculation is exact as well. For `U in USp(4)`, put

\[
F(U)=(\operatorname{Tr}U)^2-e_2(U)^2.
\]

Exact Laurent-character algebra gives

\[
F=-(1+\chi_{\omega_2}+\chi_{2\omega_2}),
\qquad -20\le F\le\frac43,
\]

and the character on the right is an honest 20-dimensional representation
`G=1+chi_omega2+chi_2omega2` containing the trivial representation. Therefore,
for every integer `m>=0`, not merely for the twelve computed orders,

\[
\int_{USp(4)}F(U)^m\,dU
=(-1)^m\dim\!\left((G^{\otimes m})^{USp(4)}\right),
\qquad
(-1)^m\int F^m>0.
\]

Thus every Haar moment is an integer with strict alternating sign. This is a
compact-group theorem only; it supplies no finite-family convergence.

The sign mechanism is now known to be much broader than genus two. For every
`g>=1`, reciprocity and dual Jacobi--Trudi give

\[
e_{g-1}e_{g+1}-e_g^2=-s_{(2^g)}.
\]

Thus weak alternating Haar signs for the reciprocal-centre minor are forced
by Schur negativity in every symplectic rank. Even the literal fixed-depth
probe `e_1^2-e_2^2` is minus an honest character for every `g>=2`, so its
strict alternating moments are not genus-two-specific either.

A balanced virtual direction removes that background. On `USp(4)`, put

\[
B=2e_1^2-e_2^2=\chi_{2\omega_1}-\chi_{2\omega_2}.
\]

Every odd Haar moment of `B` is zero and

\[
\operatorname{Haar}(B^{2r})=
\frac1{r+1}\binom{2r}{r}^2.
\]

Indeed its exact law is the product of independent arcsine and Wigner
semicircle variables on `[-2,2]`; hence its Haar sign is exactly balanced.
In the quintic family, however,

\[
\langle B_D\rangle_q=q^{-1}+q^{-3}-q^{-4}+q^{-5}>0.
\]

This exact arithmetic bias against a zero compact-group baseline is a sharper
family diagnostic than rediscovering the representation-forced sign of `F`.

An independent bounded scan now freezes the complete joint `(a_D,b_D)` law at
`q=3,5,7`, rather than retaining only detector totals. It visits all 20,175
monic candidates under a 20,000-per-field cap and finds respectively 32, 81,
and 138 joint atoms. The exact `(B_D<0,=0,>0)` member counts are

\[
(48,12,102),\qquad(986,50,1464),\qquad(6258,336,7812).
\]

These finite rows are not a monotonicity or equidistribution theorem. Their
main proof value is provenance: the same member ledger independently locks
`sum b_D^3`, `sum a_D^2b_D^2`, and `sum b_D^4`, so the high-weight channel
packet now consumes source data rather than its own former regression
constants.

Exact `C_2` algebra reduces the first unresolved balanced odd moment to one
explicit virtual weight-six average:

\[
B^3=6B-2\chi_{0,3}+R_6,
\qquad
R_6=2\chi_{2,3}+3\chi_{6,0}-3\chi_{4,2}
+\chi_{2,4}-\chi_{0,6}.
\]

Thus

\[
\langle B_D^3\rangle_q=
6(q^{-1}+q^{-3}-q^{-4}+q^{-5})
-2\langle\chi_{0,3}\rangle_q+\langle R_6\rangle_q.
\]

The cubic coefficient lock evaluates `chi_(0,3)` in each frozen field; the
smallest honest all-field task is now `mean(R_6)`, not a four-term raw
coefficient expansion. No all-`q` formula for that last average is asserted.

Frobenius powering reveals a second exact structure. If `B_r` is the same
balanced control formed from the roots raised to the `r`-th power, then the
*entire infinite echo sequence* is determined pointwise by `(B_1,B_2)`. Put

\[
p=-B_1,\qquad h=(B_1^2+B_2)/2,\qquad B_0=-4.
\]

Then

\[
B_r=pB_{r-1}-hB_{r-2}+pB_{r-3}-B_{r-4}\qquad(r\ge4),
\]

with an explicit cubic formula for `B_3`. Hence higher powers amplify
resonances but add no independent pointwise detector coordinate. Under Haar,
distinct echoes are pairwise orthogonal, yet for `1<=r<s<t` their first
nonlinear coupling is the exact additive-frequency law

\[
\langle B_rB_sB_t\rangle=
\begin{cases}
-2,&r+s=t,\ r=1,\\
-4,&r+s=t,\ r\ge2,\\
0,&r+s\ne t.
\end{cases}
\]

This is a proved Fourier/Weyl-support resonance, not a numerical fit. The
frozen coefficient laws also show that even the infinite echo loses
information: after quotienting the automatic trace-sign symmetry, it has
1, 5, and 7 collision classes at `q=3,5,7`. Several recurrence-certified
periodic strata have cyclotomic normalized spectra, making them concrete
supersingularity or extra-endomorphism candidates, but not classifications.
Finally, the three fields suggest

\[
\langle B_2\rangle_q\stackrel{?}{=}
-\frac{(q-1)(q^5+q^2-q+1)}{q^7};
\]

this last display remains explicitly quarantined as a three-field conjecture.

The balanced direction is locally canonical, but not globally unique. Since
`e_3=e_1` on `USp(4)` and

\[
\operatorname{Haar}(e_1^2,e_2^2,e_1e_3)=(1,2,1),
\]

the complete integer first-moment-null lattice in the raw coefficient-square
span is

\[
\mathbb Z(2,-1,0)+\mathbb Z(-1,0,1).
\]

The second generator is the zero class-function relation
`e_1e_3-e_1^2`; after quotienting it, the unique primitive line is exactly
`B=2e_1^2-e_2^2`. Three exhaustive low-weight coefficient boxes independently
leave only `B` among center-even/noncentral directions. This makes the choice
of `B` structural inside the declared span rather than an aesthetic fit.

The global representation ring is richer. With

\[
u=x_1^2+x_1^{-2},\qquad v=x_2^2+x_2^{-2},\qquad B=-uv,
\]

every element of

\[
\boxed{B\,\mathbb Z[u^2+v^2,u^2v^2]}
\]

has support in the residue class `(2,2) mod 4`, while the complete `C_2` Weyl
density has no support there. All its odd Haar moments therefore vanish, so
each such virtual character has a symmetric compactly supported law. This is
an infinite certified null module, not a claim to exhaust every symmetric
virtual character. Separately, every combination of irreducibles with odd
first fundamental-weight coordinate is symmetric under the central involution
`U->-U`. The bounded search thus distinguishes three facts that should not be
conflated: uniqueness in the coefficient-square quotient, isolation in small
center-even boxes, and non-uniqueness in the full representation ring.

The range makes the negative first moment quantitatively useful without any
equidistribution input. Put `Z_D=K_D/q^2`, let `rho_-(q)` be the proportion of
the family with `Z_D<0`, and write

\[
A(q)=\left(1-\frac1q\right)^2-\frac{q+1}{q^5}
=\frac{P(q)}{q^5},
\qquad P(q)=q^5-2q^4+q^3-q-1.
\]

Because `Z_D>=-20` and the nonnegative members contribute at least zero,
`-A(q)=E(Z_D)>=-20 rho_-(q)`. Moreover

\[
P(t+3)=t^5+13t^4+67t^3+171t^2+215t+104>0
\qquad(t\ge0).
\]

Consequently, for every odd prime power,

\[
\boxed{\rho_-(q)\ge\frac{P(q)}{20q^5}},
\qquad \liminf_{q\to\infty}\rho_-(q)\ge\frac1{20}.
\]

In particular every such family contains a negative member. The frozen lower
bounds are `26/1215`, `997/31250`, and `617/16807` at `q=3,5,7`; they are
deliberately conservative compared with the enumerated proportions. This is a
one-sided density floor, not a limiting sign law, equidistribution result, or
claim that any member has a canonical analytic-detector sign.

Exact Kostant-character decomposition gives 3, 9, 16, 25, 36, and 49
irreducible constituents (counted by distinct highest weights) in `G^m` for
`m=1,...,6`. Its trivial multiplicities, independently checked by the
normalized `C_2` Weyl constant term, give the first six signed Haar moments

```text
-1, 3, -11, 56, -374, 3117.
```

The same exact triangular conversion gives centered moments
`0,2,-4,27,-178,1533` and cumulants `-1,2,-4,15,-98,803`; in particular the
limiting variance target is exactly 2 and the law is strongly non-Gaussian.

Those six raw moments already imply a rigorous Haar sign bound. Define

\[
R(x)=1+\frac{5405x+264x^2-23x^3}{12023}.
\]

On `0<=x<=4/3`,

\[
R(x)-1=\frac{x(5405+264x-23x^2)}{12023}\ge0,
\]

because the concave quadratic has positive endpoint values `5405` and
`51445/9`. Hence `1_{x>=0}<=R(x)^2` on the full support `[-20,4/3]`. Exact
substitution of the six Haar moments gives

\[
\mathbb E_{\mathrm{Haar}}R(F)^2=\frac{7663}{12023},
\qquad
\boxed{\mu_{\mathrm{Haar}}(F<0)\ge\frac{4360}{12023}}
\approx0.362638.
\]

This simple cubic-square construction is certified but not strongest. A
support-adapted rational polynomial sharpens it. Set `t=(3x+28)/32` and

\[
p(t)=\frac{(t+1)(20t-13)^2(40t-7)^2(2927-2792t)}{14407470}.
\]

The support `x in [-20,4/3]` becomes `t in [-1,1]`, and `x>=0` becomes
`t>=7/8`. The displayed factorization makes `p>=0` on the full interval.
Moreover `p(7/8)=p(1)=1`, and exact division gives

\[
p(t)-1=(t-7/8)(1-t)Q(t).
\]

In the coordinate `z=8t-7`, all five degree-four Bernstein coefficients of
`Q` are positive. Thus `1_{x>=0}<=p((3x+28)/32)` exactly. The Haar expectation
is

\[
\mathbb E_{\mathrm{Haar}}p\!\left(\frac{3F+28}{32}\right)
=\frac{3879608783}{6358302720},
\qquad
\boxed{\mu_{\mathrm{Haar}}(F<0)
\ge\frac{2478693937}{6358302720}}
\approx0.389836.
\]

The corresponding frozen lower bounds are approximately
`0.230556, 0.303319, 0.323855` at `q=3,5,7`, all below the observed
`17/27, 33/50, 33/49` and all strictly stronger than the cubic-square bounds.
No optimality among degree-six majorants is claimed. More importantly,
convergence of only the first six finite moments would already imply
`liminf rho_-(q)>=2478693937/6358302720`. That conditional implication needs
neither full weak convergence nor boundary-mass control; it is a concrete
payoff from proving Targets `m=2,...,6`.

A second bounded constant-term replay extends the exact Haar sequence through
order twelve:

```text
-30321, 327688, -3815668, 46998100, -605231862, 8084025096
```

for orders `7,...,12`. It uses 238,743 capped Laurent pair-products and no
sampling or numerical integration. Those moments certify a stronger
degree-twelve majorant. In the same coordinate `t=(3x+28)/32`, it has the
factorization

\[
p(t)=C\prod_{r\in R}(t-r)^2(t^2+At+B),
\]

where

\[
R=\left\{-\frac35,-\frac{43}{200},\frac{11}{60},
\frac{67}{125},\frac{35}{48}\right\}.
\]

The exact rational `A,B,C` are frozen in the certificate. There, `C>0` and
`B-A^2/4>0` prove global nonnegativity. The contacts
`p(7/8)=p(241/250)=1`, `p'(241/250)=0`, and ten positive exact Bernstein
coefficients for

\[
\frac{p(t)-1}{(t-7/8)(t-241/250)^2}
\]

on `[7/8,1]` prove the pointwise majorant. Exact moment substitution gives

\[
\mu_{\mathrm{Haar}}(F<0)\ge
\frac{153081644970674178368978470022738347661743507912075314789490808683}
{318454738700269877013669525120657835305950388794994707229994647552}
\approx0.480701.
\]

The same polynomial gives valid frozen lower bounds approximately
`0.314646, 0.397992, 0.407579` at `q=3,5,7`. The candidate was discovered by
floating optimization, but acceptance uses only the exact factorization,
Bernstein certificate, and rational moments. No degree-twelve optimality is
claimed. Conditionally, convergence of the first twelve finite moments would
give the displayed `0.480701` liminf floor without full equidistribution.

The exact finite fractions are retained in the fixture; their display values
show how slowly the higher tails appear:

| moment | Haar `USp(4)` | `q=3` | `q=5` | `q=7` |
|---:|---:|---:|---:|---:|
| 1 | `-1` | `-0.427984` | `-0.638080` | `-0.734218` |
| 2 | `3` | `1.101052` | `1.683251` | `1.998001` |
| 3 | `-11` | `-2.095209` | `-4.167283` | `-5.592910` |
| 4 | `56` | `5.176492` | `12.974911` | `19.477453` |
| 5 | `-374` | `-12.337390` | `-42.659645` | `-75.358513` |
| 6 | `3117` | `30.726756` | `150.912978` | `321.292681` |
| 7 | `-30321` | `-76.703368` | `-560.428796` | `-1470.300970` |
| 8 | `327688` | `193.618022` | `2171.257750` | `7100.403220` |
| 9 | `-3815668` | `-490.965821` | `-8696.808820` | `-35670.979300` |
| 10 | `46998100` | `1250.939590` | `35783.433400` | `184513.460000` |
| 11 | `-605231862` | `-3198.093800` | `-150404.219000` | `-975465.486000` |
| 12 | `8084025096` | `8200.750030` | `642985.199000` | `5243311.720000` |

For all 36 frozen comparisons, the finite moment has the Haar sign and smaller
absolute magnitude, and its absolute gap decreases from `q=3` to 5 to 7. This
is a compact clue about missing extreme-tail mass, not a one-sided theorem or a
rate fit. The sixth moment at `q=7` is about one tenth of its Haar target, while
the twelfth is only `0.0006486` of its target: increasing moment order exposes
how much extreme-tail mass is still absent at these small fields. This argues
for character decomposition or effective equidistribution, not a materially
larger brute-force scan.

The exact histogram supports make the missing tail asymmetric:

```text
q=3: [-8/3, 8/9],  q=5: [-116/25, 29/25],  q=7: [-282/49, 59/49].
```

The positive endpoint is already moving toward the Haar edge `4/3`, while the
most negative `q=7` value is only about `-5.76`, far from the Haar edge `-20`.
Thus the high even-moment deficit is specifically consistent with an absent
far-negative tail, not merely with coarse histogram resolution.

That finite negative edge is exceptionally concentrated. At `q=3,5,7` its
coefficient pairs `(a_D,b_D)` may be taken as `(-2,6)`, `(-4,14)`, and
`(-7,25)`, giving `K_D=-24,-116,-282`. In each field every minimum member is
one affine orbit, of sizes `6,10,42`; the stabilizer orders are `1,2,1`.
Consequently the most moment-sensitive tail is controlled by a single weighted
geometric stratum in each frozen family, not by a diffuse population.

The concentration becomes dominant at order twelve: those single minimum
orbits supply respectively `58.3993%`, `61.9548%`, and `73.4068%` of the full
even twelfth moment. Thus a high-moment proof cannot safely average away rare
automorphism strata; at the current fields, one orbit already carries most of
the statistic.

There is also a geometric marker on these edge orbits. If `x_1,x_2` are the
two real symplectic trace coordinates, then

\[
(x_1-x_2)^2=\frac{a_D^2-4b_D+8q}{q}.
\]

On the three minimum orbits this equals `4/3, 0, 5/7`. The characteristic-five
minimum therefore lies exactly on the repeated-angle diagonal, consistent
with its extra involution, while the other two are nearby but not on it. A
tail proof should expect a special non-regular repeated-angle stratum rather
than a condition uniform over regular Frobenius classes.

The exact tail geometry is more heterogeneous than that first description
suggested. The minimum Frobenius polynomials are split nonisotypic at `q=3`,
repeated isotypic at `q=5`, and irreducible over `Q` (hence `F_7`-simple) at
`q=7`, where the real trace field is `Q(sqrt(5))`. At `q=7`, the realized
repeated-angle rung contributes only `2.39209%` of the twelfth absolute moment,
whereas the simple minimum contributes `73.40684%`. Repeated-angle strata must
be separated, but they cannot be the whole tail model.

There is also an exact realization gap. The deepest integral reciprocal
quartics allowed by the `USp(4)` coefficient region have `K=-117,-356,-821`
at `q=3,5,7`, yet none occurs in the marked quintic supports. The missing tail
is therefore not explained by coefficient integrality alone; Jacobian and
marked-family realization become the next geometric input. For the `q=5`
minimum, the non-affine inversion `x->1/x` gives two explicit elliptic quotient
maps, confirming both its splitting and the fact that affine stabilizers are
not full unmarked automorphism groups.

A separate deterministic Weyl quadrature asks the corresponding sign-law
question. Four phase shifts on periodic grids through `512 x 512` (1,376,256
cells in total, with a five-second guard) give a final phase mean
`0.737849043834` for the Haar mass of `F<0`; the four estimates at the finest
grid have spread `0.000070698736`. The exact finite negative proportions are

```text
q=3: 17/27,     q=5: 33/50,     q=7: 33/49,
```

and increase toward the display estimate. The quadrature reproduces the exact
Haar density constant and first two moments as internal controls, but it is not
directed interval arithmetic. Thus `mu_Haar(F<0) approximately 0.738` is a
numerical nomination for a future sign-distribution theorem, not a certified
probability, convergence claim, or rate.

At the displayed phase mean, the square-root-scaled gaps

```text
sqrt(q) * (mu_Haar-rho_-(q)): 0.187442, 0.174076, 0.170333
```

are notably steadier than the unscaled or `q`-scaled gaps. This nominates an
effective `q^{-1/2}` sign-law rate, with a possible one-sided leading constant
near `0.17`. It is deliberately not fitted into the atlas result: the Haar
value is not a certified interval, there are only three finite fields, and an
indicator rate additionally requires quantitative control near `F=0`.

One part of that future implication is already elementary: `F=0` is the zero
set of a nonzero polynomial in the two trace coordinates, hence has Haar
measure zero. Thus any independently proved weak convergence of the family
class measures to Haar would force convergence of the negative proportions.
Obtaining an effective sign rate would still require quantitative control near
that boundary.

Thus the proved finite-family first-moment limit equals the exact Haar mean
`-1`. This does not prove convergence of moments two through twelve, full
`USp(4)` equidistribution, a memberwise sign, or any number-field statement.
The statistic remains a toy reciprocal-coefficient minor, not Pick/Loewner,
`XD`, or `HCNC`.

At `q=3`, the involution `D(T) -> -D(-T)` also sends `P_D(u)` to `P_D(-u)`.
It forces the parity-odd probe `B_D(1)B_D(2)` to have mean zero; enumeration
gives the exact `54/54/54` negative/zero/positive split. The theorem above is
parity-even, so its negative mean is not that tautological cancellation.

### A higher-variety family: the tensor shadow inside `SO(8)`

The genus-one and genus-two packets combine without another field scan into a
genuinely different weight-two family. For an ordered pair `(E,C)`, retain the
primitive Kunneth factor

\[
H^1(E)\otimes H^1(C)\subset H^2(E\times C).
\]

The omitted complement consists of two Tate lines. Tensoring the two
alternating pairings gives a symmetric form, so the normalized compact image
is

\[
\frac{USp(2)\times USp(4)}{\{(I,I),(-I,-I)\}}longrightarrow SO(8).
\]

It has rank three inside rank-four `SO(8)`. This missing rank has a pointwise
coefficient certificate. Write the degree-eight factor as

\[
Q(T)=1+c_1T+c_2T^2+c_3T^3+c_4T^4
+q^2c_3T^5+q^4c_2T^6+q^6c_1T^7+q^8T^8
\]

and normalize
`u=c_1/q`, `v=c_2/q^2`, `w=c_3/q^3`, `h=c_4/q^4`. Every member satisfies

\[
\boxed{u^2h-u^4+2u^2v+u^2-2uw-w^2=0.}
\]

No division by `u` enters, so the trace-zero stratum is included and forces
`w=0`. The producer derives the degree-eight polynomial twice, from explicit
coefficients and from the identity
`p_n(E\otimes C)=p_n(E)p_n(C)`. It also locks the sign bridge from the
genus-one geometric trace `t_E` to the polynomial coefficient `A=-t_E`; this
prevents an aggregate twist symmetry from hiding mislabeled member witnesses.

The first trace-moment fingerprint is already order four:

\[
\operatorname{Haar}_{USp(2)\times USp(4)}(\operatorname{Tr}^4)=2\cdot3=6,
\qquad
\operatorname{Haar}_{SO(8)}(\operatorname{Tr}^4)=3.
\]

At the same representation degree, the product image has
`E(h)=E(uw)=1`, whereas generic `SO(8)` gives `0,0`. The finite ordered-model
family inherits exact all-odd-`q` corrections from the locked marginal
theorems:

\[
\begin{aligned}
\mathbb E(v)&=-\frac{(q-1)(q^3-q^2+q+1)}{q^6},\\
\mathbb E(h)&=\frac{q^6-2q^5+q^4-2q^2-2q+2}{q^6},\\
\mathbb E(uw)&=\frac{(q-1)(q+1)^2(q^4-4q^3+5q^2-q-5)}{q^7}.
\end{aligned}
\]

The complete frozen `q=3,5,7` laws are exact convolutions of only 2,471
source histogram-atom pairs; they enumerate no field, curve, or product
surface. Their measure is the product of the two marked-model/curve-stack laws
on ordered factors, not uniform coarse product-variety isomorphism classes.
The hypersurface proves that this particular tensor construction cannot have a
generic `SO(8)` coefficient law; it does not prove equidistribution even in the
smaller product group, nor does it transfer to a number-field family.

### The containing tensor hypersurface has a pinch-point singular family

The ambient hypersurface containing the coefficient image admits the exact
adapted form

\[
 F=(h+2v+2)u^2-u^4-(u+w)^2.
\]

Over characteristic different from two its full reduced affine singular locus
is the plane `u=w=0`. The transverse binary quadratic has determinant
`-(h+2v+2)`, so its rank drops along the line `h+2v+2=0`. With
`lambda=h+2v+2-u^2` and `r=u+w`, the total germ is
`r^2=u^2 lambda`, a pinch point times the free `v`-line; a fixed-`(v,h)` slice
on the rank-drop line is an `A_3` plane-curve singularity over `C`, not an
intrinsic classification of a source variety.

The product-parameter pullback is unexpectedly rigid:

\[
 h+2v+2=(x+z-2)^2+xy,
 \quad x=A^2/q,\ y=a^2/q,\ z=b/q.
\]

Set-theoretically, the reduced singular preimage is the union `A=0` or `a=0`.
Put `R=A^2+b-2q`. After clearing powers of the invertible normalization `q`,
the scheme pullbacks are `I_sing=(Aa)` and `I_rank=(Aa,R^2)`, with
`rad(I_rank)=(Aa,R)`. Its two reduced rank-drop branches are

\[
 A=0,\ b=2q,
 \qquad
 a=0,\ b=2q-A^2,
\]

and both map to `h=-2v-2`, `-4<=v<=0`. They carry the exact formal
factorizations

\[
 P_C=(1+qT^2)(1+aT+qT^2),
\]

and

\[
 P_C=(1+AT+qT^2)(1-AT+qT^2),
\]

respectively. The locked product-model rank-drop counts at `q=3,5,7` are
`66,5000,72324`. These are coefficient and polynomial facts; no
Honda--Tate/Tate, Jacobian splitting, singular-variety, or extra-endomorphism
claim is imported.

### Integral `+q` factorization is invisible to the current scalar controls

For

\[
 P(T)=1+aT+bT^2+qaT^3+q^2T^4,
 \qquad \Delta=a^2-4b+8q,
\]

an integral factorization

\[
 P(T)=(1-rT+qT^2)(1-sT+qT^2)
\]

exists exactly when `Delta=d^2>=0` and `d` has the parity of `a`; then
`r=(-a-d)/2`, `s=(-a+d)/2`. The complete frozen member fractions are
`1/6`, `141/500`, and `85/343` at `q=3,5,7`, with repeated-factor member
counts `0,15,84`.

The complement is deliberately not called “nonsplit over `Z`”: the `q=5`
row `(a,b)=(0,-10)` satisfies
`P(T)=(1-5T^2)^2` but has no factorization with both constant terms `+q`.
Likewise, a detector fiber is called mixed only when it crosses this precise
boundary. The exact `(fibers, mixed, members in mixed)` triples are

```text
q=3: B (14,1,12), F (12,1,24), complete echo (17,1,12)
q=5: B (33,3,246), F (24,6,700), complete echo (39,1,6)
q=7: B (55,5,2898), F (53,5,2856), complete echo (67,2,924).
```

Thus even the infinite balanced echo, already determined by `(B_1,B_2)`,
cannot recover the factor locus. Exact power-to-identity certificates for
normalized cyclotomic spectra occur on both sides as well. Affine split-orbit
totals are forced to `5` and `38` at `q=3,5`, while every retained global
orbit-size and state-total constraint still permits `86,87,88` at `q=7`.
This is an information-loss result, not an endoscopic-density theorem.

### Primitive exterior square: a moving local eigenline and orientation anomaly

The six-dimensional `exterior^2 H^1(C)` has a canonical polarization Tate
line. Removing it gives the primitive degree-five, weight-two factor

\[
\begin{aligned}
R(T)={}&1+(q-b)T+q(a^2-b)T^2-q^2(a^2-b)T^3\\
      &+q^3(b-q)T^4-q^5T^5,
\end{aligned}
\]

the standard representation of `USp(4)/{+-I}=SO(5)`. This is an ambient
representation statement, not a proof of full family monodromy. Character
labels below use the `C2` convention: `C2 (0,1)` corresponds to the `B2 (1,0)`
standard five, and `C2 (2,0)` to the `B2 (0,2)` adjoint ten. In normalized
coordinates

\[
 R(z/q)=1-sz+kz^2-kz^3+sz^4-z^5,
 \quad s=b/q-1=\chi_{0,1},\quad k=(a^2-b)/q=\chi_{2,0}.
\]

It therefore remembers exactly `(a^2,b)` and forgets only the sign of `a`.
Every odd special orthogonal matrix has eigenvalue one, so after removal of
the polarization line every member still satisfies

\[
 R(T)=(1-qT)
 [1+(2q-b)T+q(a^2-2b+2q)T^2+q^2(2q-b)T^3+q^4T^4].
\]

On each finite-field fiber the second eigenspace is an actual
Frobenius-stable `Q_l(-1)` line. Its axis moves with Frobenius, so the ambient
irreducible `SO(5)` representation forces no line common to all elements. The
actual family monodromy is not proved full and can specialize: on an
endoscopic splitting the anti-diagonal of the two elliptic Tate lines remains
inside the primitive factor. What is formal is assembling the varying
quartics into a compatible family or cross-prime system. This compatibility
gap nominates a concrete compensation problem for the extracted good factors.

Exact locked all-`q` formulas give, among other entries,

\[
 E(s^2)=1-q^{-1}+q^{-3}-q^{-4}-q^{-5},
 \qquad
 E(sk)=-q^{-1}+q^{-2}+3q^{-3}-3q^{-4}-2q^{-5}.
\]

The exact `SO(5)` trace moments through six are
`1,0,1,0,3,1,15`; the fifth moment `1` is the orientation/volume-tensor
invariant and would vanish for `O(5)`. Yet the frozen fifth moments are

\[
-8059/6561,\quad -541001/390625,\quad -5982775/5764801.
\]

Their opposite sign is a sharp high-weight anomaly to explain, not an
all-`q` formula or evidence against eventual `SO(5)` equidistribution.

## 5. Exact twist precursor: root conditioning and covariance are distinct inputs

Fix the imported `11.a2` model and the conductor-coprime, root-number-
unconditioned family of fundamental discriminants
`1<|d|<=X`, `gcd(d,11)=1`. At the 13 good primes through 43, the pilot stores
the complete exact matrices

\[
G_X=V^{\mathsf T}V/N,
\qquad
\operatorname{Cov}_X=V^{\mathsf T}(NI-\mathbf1\mathbf1^{\mathsf T})V/N^2,
\qquad V_{d,p}=\chi_d(p).
\]

Both are positive semidefinite by these identities. Their diagonals are not
silently replaced by one: `G_X(p,p)` is the exact proportion with `p` not
dividing `d`, compared against `p/(p+1)`. For the pooled `ALL` partitions:

| `X` | members | max absolute local-density error | max absolute raw off-diagonal | mean square of raw off-diagonals |
|---:|---:|---:|---:|---:|
| 256 | 141 | `83/4512` at 31 | `20/141` at `(7,43)` | `3592/775359` |
| 512 | 285 | `13/1710` at 17 | `11/95` at `(17,41)` | `13993/6335550` |
| 1024 | 570 | `4/665` at 41 | `7/95` at `(13,37)` | `10669/12671100` |
| 2048 | 1142 | `29/17130` at 29 | `51/1142` at `(13,43)` | `4532/12715599` |

The table is exact finite data, not a fitted decay exponent. The off-diagonal
mean square decreases across these four bounds, but neither the maximizing pair
nor individual correlations are monotone.

For

\[
W_d=\sum_{p\le43,\ p\ne11}\frac{a_p\chi_d(p)}{\sqrt p},
\]

the mean, second moment, and centered variance are retained as exact
multiquadratic coordinates. The limiting diagonal comparator for this fixed
prime packet would be

\[
\sum_p\frac{a_p^2}{p+1}=\frac{467501}{60192}
\approx7.766829479.
\]

At `X=2048`, the exact finite-density diagonal has display value
`7.762203643`, while the full exact-radical second moment has display value
`7.913589466`. The weighted off-diagonal correction changes sign between
`X=1024` and `X=2048`; decreasing unweighted RMS therefore does not by itself
control the detector weight.

The missing root-number partition was then sourced and implemented. For a
fundamental discriminant coprime to 11, the imported twist formula and base
sign of `11.a2` give

\[
\varepsilon_d=\varepsilon(11.a2)\chi_d(-11)
=\operatorname{sign}(d)\left(\frac d{11}\right).
\]

This is not the sign of `d`. The two exact cohorts are disjoint and exhaustive:

| `X` | root `+` | root `-` | display `E_+(W^2)` | display `E_-(W^2)` |
|---:|---:|---:|---:|---:|
| 256 | 65 | 76 | `7.106138779` | `6.946078817` |
| 512 | 140 | 145 | `6.361660919` | `7.843036974` |
| 1024 | 281 | 289 | `7.142742673` | `8.082996301` |
| 2048 | 568 | 574 | `8.062818685` | `7.765920135` |

There is no stable finite sign effect in these four second moments. To measure
whether the two local-character laws are separating, set

\[
\Delta_X(p,r)=G_{X,+}(p,r)-G_{X,-}(p,r),\qquad p<r.
\]

The exact off-diagonal contrast summaries derived from the stored matrices are:

| `X` | `max |Delta_X|` | pair | exact mean square over 78 pairs | RMS display |
|---:|---:|---:|---:|---:|
| 256 | `83/247` | `(37,41)` | `22556369/1903480800` | `0.108858` |
| 512 | `156/1015` | `(29,41)` | `398459/91837200` | `0.065869` |
| 1024 | `9594/81209` | `(7,31)` | `815350219/257201165559` | `0.056304` |
| 2048 | `3713/40754` | `(5,31)` | `3293698081/2072788867968` | `0.039862` |

Both displays decrease on the frozen windows, while the maximizing pair moves.
Moreover `sqrt(N)` times the RMS stays of order one on these four rows, which
is compatible with sampling-scale fluctuation but is not a fitted rate or a
theorem.

The same stored sufficient statistics also separate the two marginal channels
that the off-diagonal table omits:

\[
m_X(p)=\frac{s_{X,+}(p)}{N_{X,+}}-\frac{s_{X,-}(p)}{N_{X,-}},
\qquad
d_X(p)=G_{X,+}(p,p)-G_{X,-}(p,p).
\]

| `X` | largest signed `m_X(p)` | RMS over 13 primes | `sqrt(N)` RMS | largest signed `d_X(p)` | RMS over 13 primes | `sqrt(N)` RMS |
|---:|---:|---:|---:|---:|---:|---:|
| 256 | `129/494` at 43 | `0.129637` | `1.539358` | `367/4940` at 5 | `0.040940` | `0.486131` |
| 512 | `97/580` at 43 | `0.097490` | `1.645824` | `37/1015` at 5 | `0.016574` | `0.279799` |
| 1024 | `-9714/81209` at 13 | `0.068315` | `1.630997` | `128/4777` at 23 | `0.013513` | `0.322617` |
| 2048 | `-14843/163016` at 37 | `0.044893` | `1.517080` | `1677/81508` at 23 | `0.011668` | `0.394317` |

The exact character-mean contrast has a strikingly stable `sqrt(N)`-scaled RMS
on these four windows, whereas the density channel is smaller. This is a
finite sampling-scale clue only: the maximizing prime moves, signs change, and
four fixed packets cannot supply a rate or asymptotic law. The next missing
arithmetic input is a root-conditioned, weighted, uniform off-diagonal and
marginal estimate as the prime window grows; central ranks and zeros were not
computed.

## 6. Exact covariance: central zeros are rank-one atoms with a convention sign

Write the centered completed function as

\[
\Lambda(z)=z^rG(z),\qquad
F_\Lambda(z)=\frac r z+F_G(z),\qquad u_i=x_i^{-1}.
\]

The two detector conventions must remain separate:

\[
\frac{F(x)-F(y)}{x-y}:\qquad M_{\rm raw}=B-r uu^{\mathsf T},
\]

\[
\frac{F(x)+F(y)}{x+y}:\qquad M_{\rm raw}=B+r uu^{\mathsf T}.
\]

Thus the legitimate central atom is negative semidefinite for the Loewner
difference and positive semidefinite for the Pick sum/Hankel kernel. Calling
both simply “the Pick matrix” erases a load-bearing sign.

If the root number is `epsilon`, parity authorizes only

\[
r_{\rm forced}=\frac{1-\varepsilon}{2},
\qquad e=r-r_{\rm forced}.
\]

The exact parity/full residual satisfies

\[
M^{\rm parity}-M^{\rm full}=\sigma e uu^{\mathsf T},
\qquad
\|M^{\rm parity}-M^{\rm full}\|_F^2
=e^2\left(\sum_i x_i^{-2}\right)^2,
\]

where the squared scalar is convention-independent. At nodes `(1,2)`, the
factor is `(5/4)^2=25/16`. The imported rank-stress rows therefore give:

| curve | root number | order `r` | forced | excess `e` | squared residual |
|---|---:|---:|---:|---:|---:|
| `11.a2` | `+1` | 0 | 0 | 0 | 0 |
| `37.a1` | `-1` | 1 | 1 | 0 | 0 |
| `389.a1` | `+1` | 2 | 0 | 2 | `25/4` |

The arithmetic metadata is discovery-only; the algebra conditional on those
integers is exact.

## 7. Exact hostile control: deflation is not positivity

The synthetic quartic background remains indefinite after the full central
atom is removed. In the declared three-node control, the deflated Loewner
background has determinant `-36`, and the deflated Pick-sum background has two
negative directions despite determinant `+36`. Therefore central deflation is
bookkeeping that removes legitimate rank contamination; it is not a positivity
theorem for the remaining L-function geometry.

## 8. What appears genuinely transferable

The experiments suggest a narrow hierarchy:

1. **Transferable exactly:** Euler reciprocal algebra, unitary local scaling,
   central-order factorization, rank-one atoms, the parity/full norm identity,
   and the fact that Frobenius-power traces obey finite recurrences. For the
   balanced genus-two echo, that recurrence collapses the complete power
   sequence to two coordinates.
2. **Exactly solvable in this family:** the genus-two first toy-minor mean and
   its consequent negative-sign density floor, together with the affine
   transformation law of the toy minor. The squarefree-sieve proof works for
   every odd prime power, whereas the full sign law and higher moments still
   require new character correlations or equidistribution.
3. **A reusable control family:** the genus-one cubic family has an all-moment
   modular-stack formula. Its Catalan terms, boundary correction, and first
   cuspidal contribution at moment ten provide a concrete model of how compact
   monodromy and automorphic cohomology coexist in one exact family law.
4. **Measure-dependent even before arithmetic:** marked equations, coarse
   branch orbits, and isomorphism classes are different ensembles. The rational
   all-degree Burnside series predicts their affine automorphism resonances, but
   it does not choose the geometric measure for a new local system.
5. **Monodromy is finer than functional-equation type:** the tensor product
   `H^1(E) tensor H^1(C)` is orthogonal of degree eight, yet lies on an exact
   rank-three coefficient hypersurface and separates from generic `SO(8)` at
   the fourth trace moment. Orthogonal symmetry alone does not identify the
   family.
6. **A universal memberwise factor need not be a forced common summand:** each
   finite-field primitive exterior-square fiber has a genuine `q`-eigenline,
   while the ambient irreducible `SO(5)` representation supplies no common
   axis. Actual family monodromy and endoscopic specialization must be studied
   separately; Euler-factor extraction and compatible motivic decomposition
   are logically different operations.
7. **Singular coefficient geometry is not singular source geometry:** the
   tensor hypersurface has a pinch-point singular family whose pullback lands
   on exact factorization branches, but neither fact makes a source curve or
   product variety singular or proves extra endomorphisms.
8. **Null directions are representation-ring objects:** `B` is primitive and
   unique in the coefficient-square quotient but generates an infinite exact
   residue-null module globally. A finite low-weight search can establish local
   isolation without establishing global uniqueness.
9. **Family-dependent:** local coefficient moments, monodromy averages, rank
   distributions, and low-zero statistics.
10. **Not implied by purity alone in these pilots:** a common memberwise sign for
   either toy coefficient probe at genus one or two. A genuine source-derived
   kernel could still have deterministic positivity and must be checked on its
   own Frobenius-character image.
11. **Not supplied by small raw correlations:** the weighted off-diagonal bound
   needed for a growing reciprocal-prime detector. Its local density, root-
   number conditioning, and weight geometry are separate arithmetic inputs.

That hierarchy is more useful than another broad plot: it tells a later proof
attempt precisely which steps are algebra and which require arithmetic geometry,
twist moments, or an individualization theorem.
