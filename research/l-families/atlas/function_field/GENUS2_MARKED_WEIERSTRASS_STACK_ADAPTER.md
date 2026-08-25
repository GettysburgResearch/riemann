# Genus-two marked-Weierstrass stack adapter

**Status:** exact all-odd-\(q\) groupoid and trace lemma. This closes the
model/measure adapter gate for even-central-weight \(\operatorname{Sp}_4\)
local systems. It does **not** evaluate any previously conjectural
high-weight trace.

**Scope:** every finite field \(k=\mathbf F_q\) of odd characteristic; smooth
genus-two curves with one marked \(k\)-rational Weierstrass point.

**Exact dependencies:** only the source normalization in the locked internal
family-measure and high-weight-channel packets. The proof below is
self-contained. The bounded producer performs symbolic rational arithmetic
and source-hash checks, not finite-field or curve enumeration.

## 1. The groupoid, not the coarse affine quotient

Let

\[
  \mathcal H_5(k)=\{D\in k[T]:D\text{ monic, squarefree, }\deg D=5\}
\]

and attach to \(D\) the marked curve

\[
  (C_D,W_D):\qquad y^2=D(x),\qquad W_D=\infty.
\]

There are

\[
 |\mathcal H_5(k)|=q^5-q^4=q^4(q-1)
\]

such models. Define

\[
 \widetilde G(k)=\{(r,\beta):r\in k^\times,\ \beta\in k\}
\]

with affine composition

\[
 (r_1,\beta_1)(r_2,\beta_2)
 =(r_1r_2,\beta_1+r_1^2\beta_2).
\]

It acts on the right on monic quintics by

\[
 D\mid(r,\beta)(T)=r^{-10}D(r^2T+\beta).
\tag{1}
\]

The corresponding coordinate change is an actual marked-curve isomorphism:

\[
 C_{D\mid(r,\beta)}\longrightarrow C_D,\qquad
 (T,Y)\longmapsto(r^2T+\beta,r^5Y).
\tag{2}
\]

Indeed, the square of the new \(y\)-factor is \(r^{10}=(r^2)^5\),
exactly cancelling the monic normalization in (1).

Let

\[
 G_{\rm sq}(k)=k\rtimes(k^\times)^2
\]

be translations together with square scalings. The map

\[
 \widetilde G(k)\longrightarrow G_{\rm sq}(k),\qquad
 (r,\beta)\longmapsto(r^2,\beta)
\tag{3}
\]

is onto. Its kernel is \(\{(1,0),(-1,0)\}\). The nontrivial kernel
element fixes \(D\) but acts on \(C_D\) as
\((x,y)\mapsto(x,-y)\), the central hyperelliptic involution. Thus

\[
 |\widetilde G(k)|=q(q-1),\qquad
 |G_{\rm sq}(k)|=\frac{q(q-1)}2.
\tag{4}
\]

### Exact groupoid lemma

Let \(\mathcal W_{2,1}(k)\) denote the Deligne--Mumford groupoid of smooth
genus-two curves over \(k\) with one marked \(k\)-rational Weierstrass point.
Then

\[
 \boxed{
 \mathcal W_{2,1}(k)\simeq
 \mathcal H_5(k)//\widetilde G(k).}
\tag{5}
\]

Here // denotes the action groupoid on \(k\)-points, not a set of coarse
orbits.

**Essential surjectivity.** Every genus-two curve in odd characteristic has
its canonical hyperelliptic double cover. Its genus-zero quotient has the
rational image of the marked point, so it is isomorphic over \(k\) to
\(\mathbf P^1\). Send that marked branch point to \(\infty\). The other five branch points give
an equation \(y^2=f(x)\) with \(f\) squarefree of degree five. If \(c\) is
its leading coefficient, rescale \(x\) by an element in the square class of
\(c\); because five is odd, the new leading coefficient is a square. A
rescaling of \(y\) then makes the quintic monic.

**Full faithfulness.** An isomorphism of marked genus-two curves commutes
with the unique hyperelliptic involution and descends to an automorphism of
the quotient \(\mathbf P^1\) fixing \(\infty\). It is therefore
\(x\mapsto\alpha x+\beta\). Between two monic quintic models, lifting it
requires a scalar \(\gamma\) on \(y\) satisfying

\[
  \gamma^2=\alpha^5.
\tag{6}
\]

Since five is odd, (6) has a solution in \(k\) exactly when \(\alpha\) is a
square. Writing \(\alpha=r^2\) gives precisely the two lifts
\(\gamma=\pm r^5\) in (2). Consequently, for every \(D\),

\[
 1\longrightarrow\mu_2
 \longrightarrow\operatorname{Aut}_k(C_D,W_D)
 \longrightarrow\operatorname{Stab}_{G_{\rm sq}(k)}(D)
 \longrightarrow1,
\tag{7}
\]

and hence

\[
 |\operatorname{Aut}_k(C_D,W_D)|
 =2|\operatorname{Stab}_{G_{\rm sq}(k)}(D)|.
\tag{8}
\]

This accounts for all extra-automorphism strata: an automorphism preserving
the marked Weierstrass point must descend to an affine base transformation,
so none is missing from (7).

## 2. What the nonsquare affine coset does

The full affine group acts on polynomials by

\[
 D\mid(\alpha,\beta)(T)=\alpha^{-5}D(\alpha T+\beta).
\tag{9}
\]

If \(\alpha\) is nonsquare, equation (6) has no \(k\)-solution. Thus (9) is
not an isomorphism of the two marked curves over \(k\). Over \(k_2\), choose
\(\gamma^2=\alpha^5\). Frobenius sends \(\gamma\) to \(-\gamma\), so the
descent cocycle is the hyperelliptic involution. Therefore the nonsquare
coset exchanges a marked curve with its nontrivial quadratic twist.

This is the precise distinction hidden by the earlier full-AGL model
quotient:

* \(G_{\rm sq}\) records genuine base changes of monic marked curves;
* the central \(\mu_2\) records the two lifts and belongs to every marked
  automorphism group;
* the nonsquare AGL coset identifies quadratic twists, not isomorphic
  marked curves.

The full-AGL quotient is therefore not itself the marked-curve groupoid.
It nevertheless gives the same numerical average for twist-even
observables, which is why the earlier normalization was numerically right
for the three even channels considered below.

## 3. Exact stack mass and invariant trace formula

For any finite action groupoid \(X//G\), orbit--stabilizer gives

\[
 \sum_{[x]}\frac{f(x)}{|\operatorname{Stab}_G(x)|}
 =\frac1{|G|}\sum_{x\in X}f(x)
\tag{10}
\]

whenever \(f\) is invariant under the actual arrows. Applying (10) to (5)
first with \(f=1\) gives

\[
 \boxed{
 \sum_{[(C,W)]\in\mathcal W_{2,1}(k)}
 \frac1{|\operatorname{Aut}_k(C,W)|}
 =\frac{q^4(q-1)}{q(q-1)}=q^3.}
\tag{11}
\]

Let \(\lambda=(a,b)\) be a dominant \(\operatorname{Sp}_4\) weight in
fundamental-weight coordinates and put

\[
 w=a+2b.
\tag{12}
\]

Let \(\mathbb V_\lambda\) be the corresponding local system, using the
homogeneous \(\operatorname{GSp}_4\) extension of degree \(w\). At a marked
curve, write \(U_D\in\operatorname{USp}(4)\) for normalized Frobenius. If
\(w\) is even, the fibre trace is exactly

\[
 \operatorname{Tr}(\operatorname{Frob}_D\mid\mathbb V_{\lambda,D})
 =q^{w/2}\chi_\lambda(U_D).
\tag{13}
\]

The character is invariant under genuine marked-curve isomorphisms, so
(10) proves

\[
 \boxed{
 \operatorname{Tr}^{\rm stk}_q(\mathbb V_\lambda)
 =\frac{q^{w/2}}{q(q-1)}
   \sum_{D\in\mathcal H_5(k)}\chi_\lambda(U_D),
 \qquad w\ \text{even}.}
\tag{14}
\]

Here the left side means the groupoid Frobenius trace

\[
 \sum_{[(C,W)]}
 \frac{\operatorname{Tr}(\operatorname{Frob}_{(C,W)}
       \mid\mathbb V_{\lambda,(C,W)})}
 {|\operatorname{Aut}_k(C,W)|}.
\]

By the standard trace formula for Deligne--Mumford stacks, it is also the
alternating compactly-supported cohomological Frobenius trace. No
equidistribution or asymptotic theorem is used in (14).

## 4. Frobenius sign convention

The project fixes

\[
 L_D(u)=1+a_Du+b_Du^2+qa_Du^3+q^2u^4.
\tag{15}
\]

Since \(a_D=\sum_{x\in k}\left(\frac{D(x)}k\right)\),

\[
  \#C_D(k)=q+1+a_D.
\]

Thus the Frobenius trace on \(H^1\) in the project convention is \(-a_D\),
and the normalization used throughout the atlas is

\[
 L_D(u)=\det(1-\sqrt q\,uU_D),\qquad
 \operatorname{Tr}(U_D)=-\frac{a_D}{\sqrt q},\qquad
 e_2(U_D)=\frac{b_D}{q}.
\tag{16}
\]

For a reciprocal symplectic spectrum,

\[
 \det(1-sU)=1-\operatorname{Tr}(U)s+e_2(U)s^2
            -\operatorname{Tr}(U)s^3+s^4,
\]

so substituting \(s=\sqrt q\,u\) reproduces both the \(a_Du\) and
\(qa_Du^3\) signs in (15). There is no additional factor
\((-1)^w\) in (13); the minus sign is already contained in
\(\operatorname{Tr}(U_D)=-a_D/\sqrt q\).

## 5. Even channels closed; odd channels cancel

For \(\lambda=(a,b)\), the centre acts by

\[
 \chi_\lambda(-U)=(-1)^{a+2b}\chi_\lambda(U).
\tag{17}
\]

The three high-weight channels have

| channel | \(w=a+2b\) | stack trace supplied by (14) |
|---|---:|---|
| \(\chi_{0,3}\) | 6 | \(q^3/[q(q-1)]\sum_D\chi_{0,3}(U_D)\) |
| \(\chi_{2,2}\) | 6 | \(q^3/[q(q-1)]\sum_D\chi_{2,2}(U_D)\) |
| \(\chi_{0,4}\) | 8 | \(q^4/[q(q-1)]\sum_D\chi_{0,4}(U_D)\) |

Thus the exact geometric/measure adapter formerly missing from these three
candidate records is now proved.

For completeness, choose any nonsquare \(\nu\in k^\times\). The map

\[
 D(T)\longmapsto\nu^{-5}D(\nu T)
\]

is a bijection of \(\mathcal H_5(k)\), and Section 2 shows that it replaces
normalized Frobenius by \(-U_D\), up to conjugacy. Hence

\[
 \sum_D\chi_\lambda(U_D)
 =(-1)^w\sum_D\chi_\lambda(U_D).
\]

In characteristic-zero coefficients, this proves the exact cancellation

\[
 \boxed{
  \operatorname{Tr}^{\rm stk}_q(\mathbb V_\lambda)=0
  \quad\text{when }w\text{ is odd}.}
\tag{18}
\]

Equation (18) is a cancellation across quadratic twists. It does not say
that the trace of each individual curve is zero. If a polynomial model is
fixed by a particular nonsquare affine operation, the same equality merely
forces that model's odd character value to vanish.

## 6. Exact boundary of the result

This packet closes one gate only: it identifies the raw monic-quintic sum,
with its precise factor \(q^{w/2}/[q(q-1)]\), as the marked-Weierstrass
stack trace for every even-central-weight channel.

It does **not** prove

\[
 T_{0,3}=q^4-2q-1,\qquad
 T_{2,2}=2q^3-q^2-2q-2,\qquad
 T_{0,4}=-(2q^2+1).
\]

Those remain three-field, minimum-\(L^1\) conjectural continuations. This
packet also supplies no Tate/Eisenstein/endoscopic/Siegel decomposition, no
one-dimensional eigenpacket identification, and no RH or GRH implication.

The broader use of pointed hyperelliptic counts and genus-two counts to
access cohomology and Siegel modular forms is developed by
[Bergström](https://arxiv.org/abs/math/0611813),
[Bergström--Faber--van der Geer](https://arxiv.org/abs/0803.0917), and, in level one, by
[Faber--van der Geer](https://arxiv.org/abs/math/0305094). Those works are
context for the next cohomological step, not dependencies of the elementary
groupoid proof above, and no novelty claim is made here.

## Replay

The producer source-locks the existing family-measure, high-weight-channel,
and guarded-inference packets. It performs fewer than 4,096 exact
integer/rational coefficient operations and refuses source, schema, payload,
or output drift.

    python research/l-families/atlas/function_field/genus2_marked_weierstrass_stack_adapter.py --check
    python tests/test_genus2_marked_weierstrass_stack_adapter.py
    python -O tests/test_genus2_marked_weierstrass_stack_adapter.py
