# Internal degree six: the first nonlinear Segre closure problem

```text
Status: theorem plus sharply delimited closure target; noncomputational pass.
Scope: characteristic zero, ternary Segre with three rank-three factors.
Imports: the transferred model, the completed Chow-base Tor table,
         classical property N3 for Segre embeddings, and Gorenstein duality.
Adds: the complete degree-six transferred complex, an exact representation-
      valued defect identity, a split-functorial 1000-dimensional K_{4,2}
      submodule, and the resulting lower bound on K_{5,1}.
Computation: no new matrix elimination or numerical search is used.
RH status: RH and GRH remain unproved; this theorem does not address them.
```

## 1. The four-term central complex

Use the notation of `TRANSFERRED_KOSZUL_MODEL.md`. Thus

\[
\mathcal T=\Lambda^\bullet C\otimes B,
\qquad
\Delta=\Delta_1+\Delta_2+\Delta_3+\Delta_4,
\qquad \dim C=17.
\]

The ambient internal degree of \(\Lambda^pC\otimes B_{q,j}\) is \(p+j\),
and its total homological degree is \(p+q\). The internal-degree-six part is
therefore the finite complex

\[
0\longrightarrow \mathcal T^{(6)}_6
\longrightarrow \mathcal T^{(6)}_5
\longrightarrow \mathcal T^{(6)}_4
\longrightarrow \mathcal T^{(6)}_3
\longrightarrow0,
\tag{1.1}
\]

where

\[
\mathcal T^{(6)}_6=\Lambda^6C\otimes B_{0,0},
\tag{1.2}
\]

\[
\mathcal T^{(6)}_5=
(\Lambda^5C\otimes B_{0,1})
\oplus
(\Lambda^4C\otimes B_{1,2}),
\tag{1.3}
\]

\[
\begin{aligned}
\mathcal T^{(6)}_4={}&
(\Lambda^4C\otimes B_{0,2})
\oplus
(\Lambda^3C\otimes B_{1,3})\\
&\oplus
(\Lambda^2C\otimes B_{2,4})
\oplus
(C\otimes B_{3,5}),
\end{aligned}
\tag{1.4}
\]

and

\[
\mathcal T^{(6)}_3=
(C\otimes B_{2,5})\oplus B_{3,6}.
\tag{1.5}
\]

The completed Chow dimensions give

\[
\begin{array}{c|r}
n&\dim\mathcal T^{(6)}_n\\ \hline
6&{17\choose6}=12376\\
5&17{17\choose5}+20{17\choose4}=152796\\
4&11{17\choose4}+65{17\choose3}+65{17\choose2}+11\cdot17=79407\\
3&20\cdot17+17=357.
\end{array}
\tag{1.6}
\]

Hence

\[
\chi(\mathcal T^{(6)})
=12376-152796+79407-357
=-61370.
\tag{1.7}
\]

## 2. The exact first nonlinear defect identity

Let

\[
K_{p,q}:=\operatorname{Tor}^{S_E}_p(R,k)_{p+q}.
\tag{2.1}
\]

### Theorem 2.1 -- only \(K_{4,2}\) and \(K_{5,1}\) survive in degree six

The homology of (1.1) vanishes outside total degrees four and five. Thus

\[
H_4(\mathcal T^{(6)})=K_{4,2},
\qquad
H_5(\mathcal T^{(6)})=K_{5,1}.
\tag{2.2}
\]

In the representation ring of \(GL(V)\times S_3\),

\[
\boxed{
[K_{4,2}]-[K_{5,1}]=\mathscr D_6,
}
\tag{2.3}
\]

where

\[
\begin{aligned}
\mathscr D_6={}&
[\Lambda^6C]
-[\Lambda^5C\otimes B_{0,1}]
-[\Lambda^4C\otimes B_{1,2}]\\
&+[\Lambda^4C\otimes B_{0,2}]
+[\Lambda^3C\otimes B_{1,3}]
+[\Lambda^2C\otimes B_{2,4}]\\
&+[C\otimes B_{3,5}]
-[C\otimes B_{2,5}]
-[B_{3,6}].
\end{aligned}
\tag{2.4}
\]

On dimensions,

\[
\boxed{
\dim K_{5,1}-\dim K_{4,2}=61370.
}
\tag{2.5}
\]

### Proof

The ambient presentation \(S_E\twoheadrightarrow R\) is an isomorphism in
degree one. In a minimal resolution every first syzygy therefore has shift
at least two, and inductively every \(i\)-th free summand has shift at least
\(i+1\). Consequently

\[
\operatorname{Tor}^{S_E}_6(R,k)_6=0.
\tag{2.6}
\]

Rubei's property-\(N_3\) theorem for Segre embeddings of three nontrivial
factors gives

\[
\operatorname{Tor}^{S_E}_3(R,k)_6=0.
\tag{2.7}
\]

There are no chain groups in internal degree six outside total degrees
three through six, so only total degrees four and five can contribute.
Taking the equivariant Euler characteristic of (1.1) gives (2.3)--(2.4),
and (1.7) gives (2.5). \(\square\)

### Corollary 2.2 -- degree six is the first Euler ambiguity

At the identity,

\[
H_R(T)=
\sum_{r\ge0}{r+2\choose2}^{\!3}T^r
=
\frac{1+20T+48T^2+20T^3+T^4}{(1-T)^7}.
\tag{2.8}
\]

Since \(S_E\) has 27 variables,

\[
K_R^{S_E}(T)
=(1-T)^{20}(1+20T+48T^2+20T^3+T^4)
\tag{2.9}
\]

begins

\[
1-162T^2+1720T^3-9234T^4+30456T^5-61370T^6+\cdots.
\tag{2.10}
\]

Minimality and property \(N_3\) therefore force

\[
\beta_{1,2}=162,
\quad
\beta_{2,3}=1720,
\quad
\beta_{3,4}=9234,
\quad
\beta_{4,5}=30456.
\tag{2.11}
\]

At degree six two homological positions occur for the first time, and the
numerator determines only their difference (2.5). Thus a further numerator
or diagonal character panel cannot by itself split the first nonlinear
module from the fifth linear module.

## 3. Eleven of twelve higher operations meet here

A higher structure map

\[
\delta_r:\Lambda^rC\otimes B_{q,j}	o B_{q+r-1,j+r}
\tag{3.1}
\]

appears in internal degree six precisely when \(j+r\le6\), after tensoring
with the remaining exterior power of \(C\). The following eleven operations
occur in (1.1):

\[
\begin{array}{c|l}
r&\text{degree-six occurrence}\\ \hline
2&
B_{0,0}\to B_{1,2},\ B_{0,1}\to B_{1,3},\
B_{1,2}\to B_{2,4},\ B_{1,3}\to B_{2,5},\
B_{2,4}\to B_{3,6}\\
3&
B_{0,1}\to B_{2,4},\ B_{0,2}\to B_{2,5},\
B_{1,2}\to B_{3,5},\ B_{1,3}\to B_{3,6}\\
4&
B_{0,1}\to B_{3,5},\ B_{0,2}\to B_{3,6}.
\end{array}
\tag{3.2}
\]

The sole support-allowed higher operation absent from degree six is

\[
\Lambda^2C\otimes B_{2,5}\longrightarrow B_{3,7},
\tag{3.3}
\]

whose first possible ambient internal degree is seven.

Therefore (1.1) is not merely one more Betti computation. It is the smallest
single complex that sees all but one of the finite higher operations in the
transferred model.

## 4. A forced 1000-dimensional nonlinear submodule

The nonvanishing of \(K_{4,2}\) can be proved without computing the
rank-three Koszul matrices.

For this argument temporarily retain the full product group. Let

\[
R(V_1,V_2,V_3)
=
\bigoplus_{r\ge0}
\operatorname{Sym}^rV_1\otimes
\operatorname{Sym}^rV_2\otimes
\operatorname{Sym}^rV_3.
\tag{4.1}
\]

Choose split inclusions

\[
U_i\hookrightarrow V_i,
\qquad \dim U_i=2,\quad \dim V_i=3,
\tag{4.2}
\]

with linear retractions. Functoriality gives maps of the ambient Koszul
complexes in both directions whose composition is the identity for the
\(U_i\). Hence

\[
K_{p,q}(U_1,U_2,U_3)\hookrightarrow
K_{p,q}(V_1,V_2,V_3)
\tag{4.3}
\]

is split injective.

### Lemma 4.1 -- the \((\mathbf P^1)^3\) master class

For \(\dim U_i=2\),

\[
K_{4,2}(U_1,U_2,U_3)
\cong
(\det U_1)^3\boxtimes
(\det U_2)^3\boxtimes
(\det U_3)^3
\tag{4.4}
\]

is one-dimensional.

### Proof

The Hilbert series is

\[
\sum_{r\ge0}(r+1)^3T^r
=
\frac{1+4T+T^2}{(1-T)^4}.
\tag{4.5}
\]

The ambient polynomial ring has eight variables, so its \(K\)-polynomial is

\[
(1-T)^4(1+4T+T^2)
=1-9T^2+16T^3-9T^4+T^6.
\tag{4.6}
\]

The ring is Gorenstein of codimension four and top shift six, while property
\(N_3\) makes the first three free modules linear. Thus its minimal Betti
sequence is

\[
1,\quad 9\text{ in }(1,2),\quad16\text{ in }(2,3),
\quad9\text{ in }(3,4),\quad1\text{ in }(4,6).
\tag{4.7}
\]

Equivariantly,

\[
\omega_R
\cong
(\det U_1)(\det U_2)(\det U_3)\otimes R(-2),
\tag{4.8}
\]

while

\[
\det(U_1\otimes U_2\otimes U_3)
=
(\det U_1)^4(\det U_2)^4(\det U_3)^4.
\tag{4.9}
\]

Ambient Gorenstein duality therefore gives the top character (4.4).
\(\square\)

### Theorem 4.2 -- the rank-three master submodule

There is a product-group embedding

\[
\boxed{
S_{(3,3)}V_1\boxtimes
S_{(3,3)}V_2\boxtimes
S_{(3,3)}V_3
\hookrightarrow K_{4,2}(V_1,V_2,V_3).
}
\tag{4.10}
\]

Consequently, for \(\dim V_i=3\),

\[
\boxed{
\dim K_{4,2}\ge 10^3=1000,
\qquad
\dim K_{5,1}\ge62370.
}
\tag{4.11}
\]

### Proof

The nonzero class (4.4) survives under the split injection (4.3). With
\(U_i\) chosen as the first two basis directions, it has highest weight
\((3,3,0)\) for each \(GL(V_i)\). The product-group submodule that it
generates is therefore the external tensor product in (4.10). Weyl's
dimension formula gives

\[
\dim S_{(3,3)}(k^3)
=
\frac{(3-3+1)(3-0+2)(3-0+1)}2
=10.
\tag{4.12}
\]

This proves the first inequality in (4.11). Equation (2.5) gives the second.
\(\square\)

This supplies a concrete master source for the classical failure of property
\(N_4\). Oeding--Raicu--Sam also identify \(K_{4,2}\ne0\) as the sharp
first quadratic-strand nonvanishing for products with at least three
nontrivial factors; see
[*On the (non-)vanishing of syzygies of Segre embeddings*](https://arxiv.org/abs/1708.03803).
The theorem above records the split-functorial representation carried from
\((\mathbf P^1)^3\) into the ternary rank-three case.

No equality

\[
K_{4,2}\stackrel?=
S_{(3,3)}V_1\boxtimes S_{(3,3)}V_2\boxtimes S_{(3,3)}V_3
\tag{4.13}
\]

is claimed here. Establishing or refuting that equality is part of the
remaining closure problem.

## 5. Representation-theoretic attack on the known rank-65 transgression

The first higher map has target

\[
\begin{aligned}
B_{2,4}={}&
S_{(5,5,2)}V\otimes\mathbf1
\oplus S_{(5,5,2)}V\otimes\sigma\\
&\oplus S_{(6,4,2)}V\otimes\varepsilon
\oplus S_{(5,4,3)}V\otimes\varepsilon.
\end{aligned}
\tag{5.1}
\]

The four target dimensions are

\[
10,\quad20,\quad27,\quad8,
\tag{5.2}
\]

summing to 65. A pure proof of the source-bound rank theorem can therefore
be reduced to four nonzero highest-weight pairings:

1. decompose the \(\Delta_1\)-cycle space in
   \(\Lambda^2C\otimes B_{1,2}\);
2. construct one cycle of each target highest weight in (5.1);
3. apply the zig-zag defining \(\delta_2\);
4. pair with a dual highest-weight vector in the corresponding target;
5. prove all four scalars are nonzero.

Schur's lemma then gives surjectivity onto each irreducible target separately.
This would upgrade the existing total-rank certificate to an explanatory
representation theorem and would supply one of the principal blocks of the
degree-six differential.

## 6. Exact closure criterion

Complete ternary degree-six closure now has a precise meaning:

\[
\boxed{
\text{determine the }G\text{-equivariant differential of (1.1),
then compute its }H_4\text{ and }H_5.
}
\tag{6.1}
\]

The output is the genuine split

\[
\mathscr D_6=[K_{4,2}]-[K_{5,1}],
\tag{6.2}
\]

not another virtual identity. The recommended order is:

1. decompose the known \(d^2\) into the four pieces (5.1);
2. decompose every term of (1.1) into
   \(GL_3\times S_3\) multiplicity spaces;
3. impose \(\Delta^2=0\), beginning with
   \[
   \Delta_1\Delta_2+\Delta_2\Delta_1=0,
   \qquad
   \Delta_2^2+\Delta_1\Delta_3+\Delta_3\Delta_1=0;
   \tag{6.3}
   \]
4. use Chow and ambient Gorenstein duality to relate opposite blocks, with a
   chain-level cyclic compatibility proved before it is used;
5. identify the full \(K_{4,2}\) and \(K_{5,1}\) characters.

Only after this central split is known should a broad later-degree replay be
considered. Degree six is the first place where the numerator ceases to
select the actual modules, and it already contains eleven of the twelve
possible higher operations.
