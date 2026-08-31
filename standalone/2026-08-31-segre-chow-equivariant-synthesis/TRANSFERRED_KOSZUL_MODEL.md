# The finite transferred Koszul model of the ternary Segre--Chow bridge

```text
Status: theorem; noncomputational homological-algebra continuation.
Scope: characteristic zero, d=m=3, finite graded algebra.
Imports: the completed Chow-base Tor table, the canonical splitting
         V^{\otimes3}=Sym^3(V)\oplus C, and standard homological perturbation.
Adds: a four-arity transferred model, a complete support classification,
      and a rank-free proof that the Chow Koszul complex is not formal over
      Sym(C).
Computation: no new matrix rank or numerical search is used in this note.
RH status: RH and GRH remain unproved; this theorem does not address them.
```

## 1. Setup

Let

\[
V=k^3,\qquad E=V^{\otimes3},\qquad W=\operatorname{Sym}^3V,
\qquad E=W\oplus C,
\]

where the splitting is the characteristic-zero symmetrizer splitting. Thus

\[
\dim W=10,\qquad \dim C=17.
\]

Put

\[
S_E=\operatorname{Sym}E,\qquad S_W=\operatorname{Sym}W,
\qquad S_C=\operatorname{Sym}C,
\]

and

\[
R=\bigoplus_{r\ge0}(\operatorname{Sym}^rV)^{\otimes3}.
\]

Let

\[
K_W=(\Lambda^\bullet W\otimes R,d_W),
\qquad
B_q=H_q(K_W)=\operatorname{Tor}^{S_W}_q(R,k).
\]

The completed PR #769 table says that the only nonzero bidegrees
\(B_{q,j}\) are

\[
\begin{array}{c|c}
q&j\\ \hline
0&0,1,2\\
1&2,3\\
2&4,5\\
3&5,6,7.
\end{array}
\tag{1.1}
\]

Write

\[
G=GL(V)\times S_3.
\]

Every internal strand of \(K_W\) is finite-dimensional. Since \(G\) is
reductive in characteristic zero, cycles and boundaries admit graded
\(G\)-stable complements. We may therefore choose a graded equivariant
contraction

\[
(B,0)
\mathop{\rightleftarrows}^{\iota}_{\pi}
(K_W,d_W),
\qquad
\pi\iota=1_B,
\qquad
 d_Wh+hd_W=1-\iota\pi,
\tag{1.2}
\]

with \(h\) of homological degree \(+1\). By the usual normalization of a
contraction we may also arrange

\[
h\iota=0,\qquad \pi h=0,\qquad h^2=0.
\tag{1.3}
\]

No \(S_C\)-linearity is asserted or needed for this choice.

## 2. The transferred-model theorem

### Theorem 2.1 -- finite equivariant transfer

There is a graded \(G\)-equivariant differential

\[
\Delta=\Delta_1+\Delta_2+\Delta_3+\Delta_4
\tag{2.1}
\]

on

\[
\mathcal T=\Lambda^\bullet C\otimes B
\tag{2.2}
\]

such that

\[
H_n(\mathcal T,\Delta)_j
\cong
\operatorname{Tor}^{S_E}_n(R,k)_j.
\tag{2.3}
\]

For the signed horizontal Koszul differential \(d_C\) determined by the
chosen total-complex convention, the components can be taken to be

\[
\Delta_r=
\pi d_C(hd_C)^{r-1}\iota
\qquad(1\le r\le4).
\tag{2.4}
\]

Equivalently, \(\Delta_r\) is determined by a structure map

\[
\delta_r:\Lambda^rC\otimes B_{q,j}
\longrightarrow B_{q+r-1,j+r},
\tag{2.5}
\]

and acts on a general term by

\[
\Lambda^pC\otimes B_{q,j}
\longrightarrow
\Lambda^{p-r}C\otimes B_{q+r-1,j+r}.
\tag{2.6}
\]

Thus every \(\Delta_r\)

- preserves ambient internal degree \(p+j\);
- lowers total homological degree \(p+q\) by one;
- lowers the \(C\)-wedge filtration by \(r\);
- raises Chow homological degree by \(r-1\).

Moreover:

1. \(\Delta_1\) is the ordinary Koszul differential for the induced
   \(C\)-action on \(B\).
2. \(\Delta_r=0\) for every \(r\ge5\).
3. The filtered chain-homotopy type of \((\mathcal T,\Delta)\) is independent
   of the contraction (1.2).
4. Individual representatives \(\delta_r\) can change under filtered gauge
   equivalence, but the induced differentials on the change-of-rings
   spectral sequence are canonical.
5. The map induced by \(\delta_r\) on the appropriate earlier-page homology
   is the spectral-sequence differential
   \[
   d^r:E^r_{p,q,j}\longrightarrow E^r_{p-r,q+r-1,j}.
   \tag{2.7}
   \]

### Proof

The full \(E\)-Koszul complex is the total complex

\[
K_E=\Lambda^\bullet C\otimes K_W
\tag{2.8}
\]

with differential \(d_W+d_C\). Tensor the contraction (1.2) with
\(\Lambda^\bullet C\) and apply the basic homological perturbation lemma to
the perturbation \(d_C\). It gives a transferred differential

\[
\pi d_C(1-hd_C)^{-1}\iota
=
\sum_{r\ge1}\pi d_C(hd_C)^{r-1}\iota
\tag{2.9}
\]

and filtered quasi-isomorphisms between the transferred complex and
\(K_E\). The inverse in (2.9) is a finite sum on every vector because each
\(d_C\) lowers the finite \(C\)-wedge degree. Formula (2.3) follows.

Each occurrence of \(d_C\) removes one \(C\)-wedge factor, while each
occurrence of \(h\) raises the \(W\)-Koszul homological degree by one. This
proves (2.5)--(2.6). The final projection lands in
\(B_{q+r-1}\). Since (1.1) has \(B_q=0\) for \(q>3\), every component with
\(r\ge5\) vanishes. The standard uniqueness clause in homological
perturbation gives filtered chain-homotopy invariance. Filtering by
\(C\)-wedge degree identifies the filtration-\(r\) component with the
canonical \(d^r\) after the lower filtration components have been passed to
homology. \(\square\)

## 3. Complete support classification

The ordinary component \(\delta_1:C\otimes B_{q,j}\to B_{q,j+1}\) can be
nonzero in exactly six slots:

\[
\begin{array}{c|c}
q&\text{possible }\delta_1\\ \hline
0&B_{0,0}\to B_{0,1},\quad B_{0,1}\to B_{0,2}\\
1&B_{1,2}\to B_{1,3}\\
2&B_{2,4}\to B_{2,5}\\
3&B_{3,5}\to B_{3,6},\quad B_{3,6}\to B_{3,7}.
\end{array}
\tag{3.1}
\]

Beyond the ordinary action, there are exactly twelve support-allowed higher
operations.

For arity two:

\[
\begin{aligned}
&\Lambda^2C\otimes B_{0,0}\to B_{1,2},
&&\Lambda^2C\otimes B_{0,1}\to B_{1,3},\\
&\Lambda^2C\otimes B_{1,2}\to B_{2,4},
&&\Lambda^2C\otimes B_{1,3}\to B_{2,5},\\
&\Lambda^2C\otimes B_{2,4}\to B_{3,6},
&&\Lambda^2C\otimes B_{2,5}\to B_{3,7}.
\end{aligned}
\tag{3.2}
\]

For arity three:

\[
\begin{aligned}
&\Lambda^3C\otimes B_{0,1}\to B_{2,4},
&&\Lambda^3C\otimes B_{0,2}\to B_{2,5},\\
&\Lambda^3C\otimes B_{1,2}\to B_{3,5},
&&\Lambda^3C\otimes B_{1,3}\to B_{3,6}.
\end{aligned}
\tag{3.3}
\]

For arity four:

\[
\Lambda^4C\otimes B_{0,1}\to B_{3,5},
\qquad
\Lambda^4C\otimes B_{0,2}\to B_{3,6}.
\tag{3.4}
\]

There are no other higher slots. This is a support theorem, not a claim that
every displayed operation is nonzero in every gauge.

The exact transgression already proved in
`CHAIN_LEVEL_TERNARY_TRANSGRESSION.md` is the canonical page-two map induced
by the third slot in (3.2):

\[
\Lambda^2C\otimes B_{1,2}\longrightarrow B_{2,4}.
\tag{3.5}
\]

Its induced map on \(E^2_{2,1,4}\) is surjective of rank 65.

## 4. A noncomputational non-formality theorem

### Theorem 4.1 -- the Chow Koszul complex is not formal over \(S_C\)

As an object of the graded equivariant derived category of \(S_C\)-modules,

\[
K_W\not\simeq\bigoplus_q B_q[-q].
\tag{4.1}
\]

Here the right side carries the ordinary induced \(S_C\)-module structures
on the homology modules and zero differential. In particular, at least one
higher transferred operation is unavoidable in every filtered model.

### Proof

The completed Chow table gives

\[
E^2_{0,2,4}
=\operatorname{Tor}^{S_C}_0(B_2,k)_4
=B_{2,4},
\qquad \dim B_{2,4}=65,
\tag{4.2}
\]

because \(B_{2,3}=0\), so no positive-degree \(C\)-multiple can enter this
lowest degree of \(B_2\).

The ambient Segre embedding of three nontrivial projective factors satisfies
property \(N_3\). Hence

\[
\operatorname{Tor}^{S_E}_2(R,k)_4=0.
\tag{4.3}
\]

This is the classical theorem of Rubei,
[*Resolutions of Segre embeddings of projective spaces of any dimension*](https://arxiv.org/abs/math/0404417).

The position (4.2) lies in column \(p=0\), so it has no outgoing
spectral-sequence differential. It must therefore be killed by an incoming
higher differential before \(E^\infty\).

If (4.1) held, derived tensoring with \(k\) over \(S_C\) would give the direct
sum

\[
K_W\otimes^{\mathbf L}_{S_C}k
\simeq
\bigoplus_q
(B_q\otimes^{\mathbf L}_{S_C}k)[-q],
\tag{4.4}
\]

and the class (4.2) would survive as a direct summand of total Tor. This
contradicts (4.3). \(\square\)

### Corollary 4.2 -- rank-free versus source-bound conclusions

The proof above uses no rank computation. It forces the complete
65-dimensional strand to disappear, but by itself allows the disappearance
to be shared between

\[
d^2:E^2_{2,1,4}\to E^2_{0,2,4}
\quad\text{and}\quad
 d^3:E^3_{3,0,4}\to E^3_{0,2,4}.
\tag{4.5}
\]

The exact source-bound replay proves the stronger statement that \(d^2\)
alone is already surjective. Thus the computational theorem identifies the
page and source of a cancellation whose existence is forced independently
by geometry.

## 5. Meaning of the reduction

The twenty-step ambient resolution is not being replaced by an Euler
character. It is being replaced, up to filtered chain homotopy, by a finite
higher-homotopy problem on the ten Chow homology strands:

\[
\boxed{
\operatorname{Tor}^{S_E}(R,k)
=H\!\left(
\Lambda C\otimes B,
\Delta_1+\Delta_2+\Delta_3+\Delta_4
\right).
}
\tag{5.1}
\]

The recurrence numerator determines the alternating class of \(B\). The
completed Chow resolution determines every individual \(B_{q,j}\). What is
still missing for complete ambient closure is precisely the filtered gauge
class of the twelve support-allowed higher operations in (3.2)--(3.4),
together with the six ordinary actions in (3.1).

The next note shows that one internal degree sees eleven of those twelve
higher slots simultaneously.