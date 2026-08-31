> Part of the [PR #766/#769/#781 proof-oriented synthesis packet](README.md).

# 2. New Theorem I: master Segre–Chow cofactor, Tor strands, spectral sequence, and duality

## Theorem I

Let \(k\) have characteristic zero. Let \(V\) have dimension \(d\), let \(m\ge2\), and use the notation fixed in [README §0](README.md#0-notation-and-the-four-objects-that-must-not-be-conflated). Set

\[
N:=\dim W=\binom{d+m-1}{m},\qquad
c:=N-m(d-1)-1,\qquad s:=N-d.
\]

Define

\[
B_{q,j}:=\operatorname{Tor}^{S_W}_q(R,k)_j.
\]

Then:

### (I.1) Finiteness and Cohen–Macaulay range

The graded \(S_W\)-module \(R\) is finite and Cohen–Macaulay of codimension \(c\). Hence

\[
B_{q,j}=0\qquad(q>c).
\]

### (I.2) Canonical individual strand complex

Each \(B_{q,j}\) is a canonical \(GL(V)\times S_m\)-module, and is the \(q\)-th homology of the finite \(j\)-strand of the Koszul–Cartan complex

\[
\mathcal K^{(j)}_q
=
\Lambda^qW\otimes(\operatorname{Sym}^{j-q}V)^{\otimes m},
\]

with the convention that \(\operatorname{Sym}^aV=0\) for \(a<0\). The differential is induced by the inclusion \(W\hookrightarrow R_1\) followed by coordinatewise Cartan multiplication.

In particular,

\[
B_{0,j}=
\operatorname{coker}\!\left(
W\otimes(\operatorname{Sym}^{j-1}V)^{\otimes m}
\longrightarrow
(\operatorname{Sym}^{j}V)^{\otimes m}
\right),
\]

and

\[
B_{1,j}=
\frac{
\ker\!\left(
W\otimes(\operatorname{Sym}^{j-1}V)^{\otimes m}
\to
(\operatorname{Sym}^{j}V)^{\otimes m}
\right)}
{
\operatorname{im}\!\left(
\Lambda^2W\otimes(\operatorname{Sym}^{j-2}V)^{\otimes m}
\to
W\otimes(\operatorname{Sym}^{j-1}V)^{\otimes m}
\right)}.
\]

### (I.3) The recurrence numerator is the Chow-base Tor Euler character

In \(R(GL(V)\times S_m)[T]\),

\[
\mathcal N_{m,d}(T):=
\sum_{q,j}(-1)^q[B_{q,j}]T^j
\]

is the equivariant \(K\)-polynomial of \(R\) over \(S_W\). Evaluating the \(S_m\)-character at the identity gives

\[
N_{m,d}(A,T)=
\det(1-TA\mid W)\,F_{d,m}(A,T)
=
\sum_{q,j}(-1)^q
\operatorname{Tr}(A\mid B_{q,j})T^j.
\]

### (I.4) Canonical change-of-rings spectral sequence

The canonical splitting \(E=W\oplus C\) gives a \(GL(V)\times S_m\)-equivariant, internally graded spectral sequence

\[
E^2_{p,q,j}
=
\operatorname{Tor}^{\operatorname{Sym}C}_p(B_q,k)_j
\Longrightarrow
\operatorname{Tor}^{S_E}_{p+q}(R,k)_j.
\]

Consequently, in the representation ring,

\[
K_R^E(T)
=
\lambda_{-T}(C)\,\mathcal N_{m,d}(T),
\]

and therefore

\[
K_R^E(A,T)
=
N_{m,d}(A,T)\det(1-TA\mid C).
\]

This is an Euler-character identity. It does **not** assert a termwise tensor-product formula for ambient Tor, and it does not assert degeneration of the spectral sequence.

### (I.5) Equivariant Gorenstein duality

Let

\[
L_{d,m}:=
\det(W)\otimes(\det V)^{-m}\otimes
\operatorname{sgn}^{\,d-1}.
\]

Then

\[
B_{c-q,\,s-j}
\cong
B_{q,j}^{\vee}\otimes L_{d,m}.
\]

In particular,

\[
B_{c,s}\cong L_{d,m}
\]

is one-dimensional, and \(B_{q,j}=0\) for \(j>s\). Thus

\[
\deg_T N_{m,d}=s=N-d.
\]

Since

\[
\det(\operatorname{Sym}^mV)
=
(\det V)^{\binom{d+m-1}{d}},
\]

the top Tor representation is

\[
B_{c,s}\cong
(\det V)^{\binom{d+m-1}{d}-m}
\otimes\operatorname{sgn}^{\,d-1}.
\]

At the identity conjugacy class of \(S_m\),

\[
[T^s]N_{m,d}(A,T)
=
(-1)^c
\det(A)^{\binom{d+m-1}{d}-m}.
\]

This is exactly the representation-theoretic lift of PR #766's scalar top-coefficient law.

### (I.6) Representation-valued reciprocity

The Euler polynomial satisfies

\[
\mathcal N_{m,d}(T)
=
(-1)^c L_{d,m}\,T^s
\mathcal N_{m,d}^{\vee}(T^{-1}).
\]

This is the Chow-module Gorenstein mechanism behind the reciprocal numerator.

## Proof of Theorem I

### Proof of (I.1)

The multiplication map

\[
\operatorname{Sym}^mV\longrightarrow
V^{\otimes m}=R_1
\]

makes \(R\) a graded \(S_W\)-module. Geometrically this is the map from the Segre product to the Chow variety sending an ordered tuple of linear forms to their product. Unique factorization gives finite fibers up to permutation. Classically, the full Segre ring and its \(S_m\)-invariant normalization are finite over the Chow coordinate ring. In the notation of [Raicu–Sam–Weyman, *On some modules supported in the Chow variety*](https://arxiv.org/abs/2108.10910), \(R\) is their algebra \(A_{m,d-1}\), and their Proposition 2.7 gives the required module-finiteness.

Their Cohen–Macaulay module-of-covariants result gives projective dimension equal to the Chow codimension:

\[
\operatorname{pdim}_{S_W}R
=
\dim W-\dim R
=
N-\bigl(m(d-1)+1\bigr)
=
c.
\]

Hence the Tor groups vanish above \(c\).

### Proof of (I.2)

The Koszul complex of the polynomial ring \(S_W\) with coefficients in \(R\) is

\[
K_\bullet(W;R)=R\otimes\Lambda^\bullet W.
\]

Its degree-\(j\) part is precisely

\[
\Lambda^qW\otimes R_{j-q}
=
\Lambda^qW\otimes(\operatorname{Sym}^{j-q}V)^{\otimes m}.
\]

The differential is the standard Koszul differential, using the action of \(W\subset R_1\). It is \(GL(V)\)-equivariant. Since \(S_m\) acts trivially on the symmetric summand \(W\) and permutes the tensor factors of \(R\), the differential is also \(S_m\)-equivariant. Its homology is \(\operatorname{Tor}^{S_W}(R,k)\), proving all assertions.

### Proof of (I.3)

Let a finite equivariant minimal free resolution be

\[
F_q=\bigoplus_j S_W(-j)\otimes B_{q,j}.
\]

Taking equivariant Hilbert series gives

\[
\operatorname{Hilb}_R
=
\frac{\sum_{q,j}(-1)^q[B_{q,j}]T^j}
{\lambda_{-T}(W)}.
\]

Evaluation at \(A\) sends \(\lambda_{-T}(W)\) to
\(\det(1-TA\mid W)\), while

\[
\operatorname{Hilb}_R(A,T)=F_{d,m}(A,T).
\]

Multiplication gives the formula for \(N_{m,d}\).

### Proof of (I.4)

Characteristic zero gives the canonical symmetrizer decomposition

\[
E=W\oplus C,
\qquad
S_E\cong S_W\otimes\operatorname{Sym}C.
\]

Derived associativity gives

\[
R\otimes_{S_E}^{\mathbf L}k
\simeq
\left(R\otimes_{S_W}^{\mathbf L}k\right)
\otimes_{\operatorname{Sym}C}^{\mathbf L}k.
\]

The standard hyperhomology spectral sequence is exactly the displayed spectral sequence.

Taking Euler characteristics of the Koszul complex over \(C\) multiplies by
\(\lambda_{-T}(C)\). This proves the representation-ring cofactor identity. Nonzero higher differentials may redistribute actual Tor modules, so only the additive Euler identity follows without a degeneration theorem.

### Proof of (I.5)

The Segre ring of \((\mathbf P(V^\vee))^m\) with the line bundle
\(\mathcal O(1,\ldots,1)\) is Gorenstein. Equivariantly,

\[
\omega_R
\cong
(\det V)^m\otimes
\operatorname{sgn}^{\,d-1}\otimes
R(-d).
\]

The sign is the Koszul sign from permuting \(m\) factors of top cohomological degree \(d-1\).

The polynomial ring has

\[
\omega_{S_W}
\cong
\det(W)\otimes S_W(-N).
\]

Since \(R\) is Cohen–Macaulay of codimension \(c\),

\[
\omega_R\cong
\operatorname{Ext}^{c}_{S_W}(R,\omega_{S_W}).
\]

Dualize a minimal free resolution termwise. A summand
\(S_W(-j)\otimes B_{q,j}\) becomes

\[
S_W(-(N-j))\otimes B_{q,j}^{\vee}\otimes\det(W).
\]

Comparing this dual resolution with the original resolution shifted by \(d\) and twisted by
\((\det V)^m\otimes\operatorname{sgn}^{d-1}\) gives

\[
B_{c-q,N-d-j}
\cong
B_{q,j}^{\vee}\otimes
\det(W)\otimes(\det V)^{-m}\otimes
\operatorname{sgn}^{d-1}.
\]

Taking \(q=j=0\) gives the one-dimensional top Tor. Negative internal degrees vanish, so no internal degree can exceed \(N-d\).

### Proof of (I.6)

Apply (I.5) term by term to

\[
\sum_{q,j}(-1)^q[B_{q,j}]T^j
\]

and substitute \((q,j)\mapsto(c-q,s-j)\). The factor \((-1)^cL_{d,m}T^s\) emerges immediately.

\(\square\)

## Consequence for the “uniform strand formula” question

There is a uniform formula in the following precise sense:

- every fixed \((q,j)\) Chow-base strand is the homology of the functorial Schur/Koszul complex
  \[
  \Lambda^\bullet(\operatorname{Sym}^mV)
  \otimes(\operatorname{Sym}^{j-\bullet}V)^{\otimes m};
  \]
- its terms admit uniform plethysm and Schur–Weyl decompositions.

There is not, from the three branches or the cited classical inputs, a uniform closed Schur decomposition of those homology groups for all \(d,m\). [Raicu–Sam–Weyman](https://arxiv.org/abs/2108.10910) explicitly pose the general minimal-resolution problem. Lascoux and [Netay](https://arxiv.org/abs/1108.3733) solve the two-factor **ambient Segre** problem, and [Snowden's \(\Delta\)-module theorem](https://arxiv.org/abs/1006.5248) gives finite master descriptions for fixed ambient homological degree, but neither result by itself computes the Chow-base Tor groups. The spectral sequence above is the precise interface.

---
