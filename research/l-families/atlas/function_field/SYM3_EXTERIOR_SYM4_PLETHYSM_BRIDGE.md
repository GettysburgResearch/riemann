# The Sym3 exterior-square / Sym4 plethysm bridge

Status: exact characteristic-zero representation algebra and a source-locked finite transform

Scope: formal local factors and normalized coefficient curves; finite incidence only for the already locked $q=3,5,7$ genus-two atoms

What was run: sparse polynomial identities and a deterministic pass over 251 pre-enumerated signed atoms
Smallest next family: the general $\bigwedge^2\operatorname{Sym}^{\mathrm{odd}}$ plethysm ladder

## Result

For a two-dimensional characteristic-zero representation $V$,

\[
 \boxed{\bigwedge^2\operatorname{Sym}^3V
 \simeq (\det V)^3\oplus(\operatorname{Sym}^4V\otimes\det V).}
 \tag{1}
\]

If $L_E(T)=1-tT+qT^2$, the primitive exterior factor of its symmetric cube
is the determinant twist of its symmetric fourth:

\[
 \boxed{R_{q^3}(T)=P_{\operatorname{Sym}^4E}(qT).}
 \tag{2}
\]

After normalization, the corresponding coefficient map sends

\[
 (x,y)\longmapsto(s,k)=(y-1,x^2-y)
\]

and obeys

\[
 \boxed{F_4(y-1,x^2-y)=-F_3(x,y).}
 \tag{3}
\]

Thus the Sym3-curve hits and the pullback of the Sym4 curve agree on every
input, not merely on the frozen data. On the 251 locked genus-two signed
coefficient atoms, their common zero set consists of exactly seven atoms
representing 451 marked quintics. Quotienting the sign of the first
coefficient leaves exactly two images for each $q$, with respectively
$18,55,378$ members. This is a commutative coefficient diagram and frozen
incidence statement, not an identification of motives or families.

## 1. Classical plethysm identity

Diagonalize $V$ with weights $\alpha,\beta$. The four weights of
$\operatorname{Sym}^3V$ are

\[
 \alpha^3,\qquad \alpha^2\beta,\qquad
 \alpha\beta^2,\qquad \beta^3.
\]

Their six unordered pair products are

\[
 \alpha^5\beta,\qquad \alpha^4\beta^2,\qquad
 (\alpha\beta)^3,\qquad(\alpha\beta)^3,\qquad
 \alpha^2\beta^4,\qquad\alpha\beta^5.
\]

One copy of $(\alpha\beta)^3$ is $(\det V)^3$; the remaining five weights
are those of $\operatorname{Sym}^4V\otimes\det V$. Equivalently, the two
Schur summands are $S_{(3,3)}V$ and $S_{(5,1)}V$. Equality of torus
characters gives (1), because rational $GL_2$ representations are semisimple
in characteristic zero. The producer independently compares the two
complete weight multisets, including multiplicity two at weight $(3,3)$.

This is classical Clebsch--Gordan/plethysm, not a project novelty claim.

## 2. Exact local-factor square

Write the symmetric-cube quartic in the generic reciprocal form

\[
 1+a_3T+b_3T^2+Qa_3T^3+Q^2T^4,
\]

where

\[
 Q=q^3,\qquad a_3=-t^3+2qt,\qquad
 b_3=q(t^4-3qt^2+2q^2).
 \tag{4}
\]

For a reciprocal quartic with parameters $(a,b,Q)$, the locked primitive
exterior formula is

\[
\begin{aligned}
 R_Q(T)={}&1+(Q-b)T+Q(a^2-b)T^2-Q^2(a^2-b)T^3\\
          &+Q^3(b-Q)T^4-Q^5T^5.
\end{aligned}
\tag{5}
\]

Put

\[
 C=t^4-3qt^2+q^2,\qquad
 D=q(t^2-2q)C.
 \tag{6}
\]

The two load-bearing reductions are

\[
 b_3=q(C+q^2),\qquad
 a_3^2-b_3=(t^2-2q)C=\frac Dq.
 \tag{7}
\]

Substitution into (5) gives

\[
 R_{q^3}(T)
 =1-qCT+q^2DT^2-q^5DT^3+q^{10}CT^4-q^{15}T^5.
 \tag{8}
\]

On the other hand,

\[
 P_{\operatorname{Sym}^4E}(U)
 =1-CU+DU^2-q^2DU^3+q^6CU^4-q^{10}U^5.
 \tag{9}
\]

Replacing $U$ by $qT$ in (9) gives (8) coefficient by coefficient. The
producer verifies (7) and all six coefficients in the polynomial ring
$\mathbb Z[t,q]$, rather than on a numerical grid. The replay test supplies
a separate direct-root derivation.

The diagram is therefore

\[
\begin{array}{ccc}
 L_E & \xrightarrow{\operatorname{Sym}^3} & P_{\operatorname{Sym}^3E}\\
 \big\downarrow{\operatorname{Sym}^4\otimes\det}
 &&\big\downarrow{\text{primitive }\bigwedge^2}\\
 P_{\operatorname{Sym}^4E}(qT)&=&R_{q^3}(T).
\end{array}
\]

## 3. Normalized coefficient diagram

The Sym3 coefficient curve is

\[
 F_3(x,y)=-x^4+x^2y+x^2+y^3-2y^2.
\]

For a primitive exterior factor, the normalized coordinates are

\[
 s=y-1,\qquad k=x^2-y.
\]

The Sym4 thin-slice curve is

\[
 F_4(s,k)=k^2+sk-s^2-s^3.
\]

Direct expansion gives

\[
\begin{aligned}
 F_4(y-1,x^2-y)
 &=x^4-x^2y-x^2-y^3+2y^2\\
 &=-F_3(x,y),
\end{aligned}
\]

which proves (3) over $\mathbb Z[x,y]$. With the Sym3 normalization
parameter $t_0=t/\sqrt q$, the Sym4 parameter used by the locked packet is

\[
 w=t_0^2-2,\qquad s=w^2+w-1,\qquad k=ws.
 \tag{10}
\]

### Nodes and the arithmetic ghost

The three Sym3 nodes behave as follows:

| Sym3 point | normalization condition | image $(s,k)$ | status on $F_4$ |
|---:|:---|---:|:---|
| $(-1,1)$ | $t_0^2+t_0-1=0$ | $(0,0)$ | node |
| $(1,1)$ | $t_0^2-t_0-1=0$ | $(0,0)$ | node |
| $(0,0)$ | $t_0^2=2$ | $(-1,0)$ | smooth |

Thus the two side nodes collapse to the single Sym4 node. Its two $w$
preimages solve $w^2+w-1=0$, so neither is rational. At the central Sym3
node, $t_0^2=2$ and hence $w=0$; the image is the smooth point $(-1,0)$,
where

\[
 (\partial_sF_4,\partial_kF_4)=(-1,-1).
\]

Smoothness does not repair arithmetic origin. For odd $q$, an integral
elliptic trace at the central point would require $t^2=2q$, impossible
because $v_2(2q)=1$. The ghost therefore survives the coefficient map; it
has merely lost its singular-point warning.

## 4. Frozen 251-atom incidence

The finite transform reads the already completed genus-two/Sym3 intersection
fixture. For every signed atom it sets

\[
 x^2=\frac{a_D^2}{q},\qquad y=\frac{b_D}{q},\qquad
 s=\frac{b_D-q}{q},\qquad k=\frac{a_D^2-b_D}{q},
\]

and checks both the locked scaled $F_3$ residual and (3). No field element,
curve, or family member is enumerated.

| $q$ | source signed atoms | source members | common hit atoms | common hit members | sign-compressed hits |
|---:|---:|---:|---:|---:|---:|
| 3 | 32 | 162 | 3 | 18 | 2 |
| 5 | 81 | 2500 | 2 | 55 | 2 |
| 7 | 138 | 14406 | 2 | 378 | 2 |
| audit sum | 251 | 17068 | 7 | 451 | 6 |

The exact hit images are:

| $q$ | $(s,k)$ | signed preimages $(a_D,b_D;\text{members})$ | members | classification |
|---:|:---:|:---|---:|:---|
| 3 | $(-1,0)$ | $(0,0;12)$ | 12 | central arithmetic ghost |
| 3 | $(1,1)$ | $(-3,6;3),(3,6;3)$ | 6 | source-witnessed shapes |
| 5 | $(-1,0)$ | $(0,0;50)$ | 50 | central arithmetic ghost |
| 5 | $(1,-2)$ | $(0,10;5)$ | 5 | source-witnessed shape |
| 7 | $(-1,0)$ | $(0,0;336)$ | 336 | central arithmetic ghost |
| 7 | $(1,-2)$ | $(0,14;42)$ | 42 | source-witnessed shape |

The JSON stores exact signed-hit rows and canonical hashes of the complete
251-row transform transcript. The sums across different $q$ are audit totals
only; they do not define a common probability space.

## 5. Source and interpretation firewalls

The producer freezes the completed JSON payloads for the elliptic Sym3,
elliptic Sym4, primitive genus-two exterior-square, and genus-two/Sym3
intersection packets by schema, canonical payload hash, and LF-normalized
file hash. Their embedded producer, note, and test locks are thereby frozen
transitively. A changed upstream payload is refused rather than silently
inherited.

The determinant twist in (1) is essential:

- $\operatorname{Sym}^3H^1(E)$ has weight $3$, so its exterior square has
  weight $6$.
- The removed summand $(\det V)^3$ contributes $1-q^3T$.
- The survivor is $\operatorname{Sym}^4V\otimes\det V$, hence
  $P_{\operatorname{Sym}^4}(qT)$, not the untwisted polynomial.
- The survivor still has a pointwise $q^3$ middle eigenvalue. That is not a
  second common Tate subrepresentation: $\operatorname{Sym}^4V$ is
  irreducible, and its middle-weight axis varies with the diagonalized
  Frobenius torus.
- Normalized coefficient equality does not identify the original genus-two
  weight-one factor with an elliptic Sym3 factor, nor their motives,
  monodromy groups, measures, compatible systems, or Euler products.

The Sym3 and Sym4 transfers are classical. The relevant boundaries are
Kim--Shahidi's symmetric-cube functoriality and Henry Kim's symmetric-fourth
transfer. Those automorphy theorems are not reproved and are not needed for
the finite algebra here. The project-specific contribution is only the
commutative coefficient diagram and frozen incidence transform. No
literature-priority, analytic-continuation, zero-free-region, RH, or GRH
claim is made.

## 6. Next target and replay

For odd $m$, classical Clebsch--Gordan gives the ladder

\[
 \bigwedge^2\operatorname{Sym}^mV
 \simeq
 \bigoplus_{\substack{1\le i\le m\\i\ \mathrm{odd}}}
 \operatorname{Sym}^{2m-2i}V\otimes(\det V)^i.
\]

The next project target is to derive its successive normalized coefficient
maps and source-locked incidence pullbacks, still without fresh enumeration.

Replay from the repository root:

~~~text
python -B research/l-families/atlas/function_field/sym3_exterior_sym4_plethysm_bridge.py --check
python -B -m unittest tests.test_sym3_exterior_sym4_plethysm_bridge
python -B -O -m unittest tests.test_sym3_exterior_sym4_plethysm_bridge
~~~

The producer uses exact integers, Fraction values, and sparse integer
polynomials. Its guarded ledger remains below an exclusive 512-unit cap;
these are declared high-level checks, not literal arithmetic instructions or
wall-clock complexity.
