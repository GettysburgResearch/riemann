# The first nonzero Segre--Chow transgression in the ternary cube

```text
Status: PROPOSED THEOREM with two exact modular rank certificates;
        independent proof/code review required.
Scope: characteristic zero, d=m=3, finite graded algebra.
Imports: PR #769's proved Chow-base Tor table and literal orbit-sum source;
         standard Koszul/change-of-rings spectral sequence.
Adds:   exact C-action, first nonzero d2, first ambient associated-graded
        strands, and a no-go theorem for E2 degeneration.
RH status: RH and GRH are unproved; this theorem does not address them.
```

## 1. Setup and the literal bicomplex

Let

\[
 V=\mathbf Q^3,
 \qquad E=V^{\otimes3},
 \qquad W=\operatorname{Sym}^3V\subset E,
 \qquad C=E/W.
\]

In characteristic zero the symmetrizer gives a canonical splitting
\(E=W\oplus C\). Put

\[
 S_E=\operatorname{Sym}E,
 \qquad S_W=\operatorname{Sym}W,
 \qquad S_C=\operatorname{Sym}C,
\]

and

\[
 R=\bigoplus_{r\ge0}(\operatorname{Sym}^rV)^{\otimes3}.
\]

The Koszul complex for \(E=W\oplus C\) is the total complex of

\[
 \mathcal K_{p,q,j}
 =\Lambda^p C\otimes\Lambda^qW\otimes R_{j-p-q},
\]

with vertical differential \(d_W\) and horizontal differential \(d_C\).
Taking vertical homology and then horizontal homology gives

\[
 E^2_{p,q,j}
 =\operatorname{Tor}^{S_C}_p(B_q,\mathbf Q)_j,
 \qquad
 B_q=\operatorname{Tor}^{S_W}_q(R,\mathbf Q),
\]

and

\[
 E^2_{p,q,j}\Longrightarrow
 \operatorname{Tor}^{S_E}_{p+q}(R,\mathbf Q)_j.
\]

This is not merely an abstract derived construction: every map is induced by
multiplication of the literal tensor generators on the three symmetric
factors of \(R\).

## 2. Imported Chow-base data

PR #769 proves

\[
 \dim B_{1,2}=20,
 \qquad \dim B_{1,3}=65,
 \qquad \dim B_{2,4}=65,
\]

with

\[
 B_{2,4}=
 [552]\otimes(\mathbf1+\sigma)
 +([642]+[543])\otimes\varepsilon.
\]

It also proves that every omitted Tor bidegree vanishes. These dimensions
supply characteristic-zero upper bounds. They are not inferred from the new
modular computation.

## 3. Theorem

### Theorem 3.1 -- generation of the first Chow syzygy module

The multiplication map induced by the quotient directions,

\[
 \boxed{
 \mu_C:C\otimes B_{1,2}\longrightarrow B_{1,3},
 }
\]

is surjective.

Hence

\[
 E^2_{0,1,3}=0
\]

and

\[
 \dim E^2_{1,1,3}
 =17\cdot20-65=275.
\]

### Theorem 3.2 -- first nonzero higher differential

At internal degree four,

\[
 E^2_{2,1,4}
 =\ker\!\left(
 \Lambda^2C\otimes B_{1,2}
 \longrightarrow C\otimes B_{1,3}
 \right)
\]

has dimension

\[
 {17\choose2}\cdot20-17\cdot65=1615.
\]

The change-of-rings transgression

\[
 \boxed{
 d^2_{2,1,4}:E^2_{2,1,4}\longrightarrow
 E^2_{0,2,4}=B_{2,4}
 }
\]

is surjective and has rank 65.

In particular, the spectral sequence does not degenerate at \(E^2\), and
there is no termwise identity

\[
 \operatorname{Tor}^{S_E}(R,\mathbf Q)
 \stackrel?=\Lambda^\bullet C\otimes
 \operatorname{Tor}^{S_W}(R,\mathbf Q).
\]

The Euler-character cofactor remains true; the displayed termwise
factorization is false.

### Corollary 3.3 -- first ambient associated-graded strands

Let

\[
 B_0=R/(W)R
\]

as an \(S_C\)-module and put

\[
 J_2=\ker(\operatorname{Sym}^2C\to B_{0,2}).
\]

Then

\[
 \dim J_2={18\choose2}-11=142.
\]

The filtration on ambient quadratic Tor has semisimple associated graded

\[
 \operatorname{gr}\operatorname{Tor}^{S_E}_{1,2}(R,\mathbf Q)
 \cong J_2\oplus B_{1,2},
\]

and therefore dimension

\[
 142+20=162.
\]

Since \(B_{0,3}=0\),

\[
 \dim\operatorname{Tor}^{S_C}_2(B_0,\mathbf Q)_3
 =17\cdot142-{19\choose3}=1445.
\]

Together with Theorem 3.1,

\[
 \dim\operatorname{Tor}^{S_C}_1(B_1,\mathbf Q)_3=275.
\]

No higher differential can enter or leave these two degree-three positions,
so

\[
 \operatorname{gr}\operatorname{Tor}^{S_E}_{2,3}(R,\mathbf Q)
 \cong
 \operatorname{Tor}^{S_C}_2(B_0,\mathbf Q)_3
 \oplus
 \operatorname{Tor}^{S_C}_1(B_1,\mathbf Q)_3,
\]

and

\[
 1445+275=1720.
\]

These are exactly the ambient dimensions independently obtained in PR #766.
The filtration is canonical; the direct-sum splitting as a
\(GL(V)\times S_3\)-representation exists by semisimplicity but is not claimed
canonical.

## 4. Chain-level definition of the transgression

Represent a class of \(E^2_{2,1,4}\) by

\[
 x\in\Lambda^2C\otimes K^W_{1,2},
 \qquad d_Wx=0.
\]

The horizontal-cycle condition means that \(d_Cx\) is vertically exact. Pick

\[
 y\in C\otimes K^W_{2,3}
 \quad\text{with}\quad
 d_Wy=d_Cx
\]

(up to the harmless sign determined by the total-complex convention). Then

\[
 d_W(d_Cy)=-d_C(d_Wy)=-d_C^2x=0,
\]

so \(d_Cy\) defines a class in \(B_{2,4}\), and

\[
 d^2[x]=[d_Cy].
\]

Changing \(x\) or \(y\) by an allowed boundary changes \(d_Cy\) by a
vertical boundary, so the class is well defined. This is the zig-zag
implemented by the exact replay.

## 5. Exact rank proof

The replay uses the following bases, all constructed rather than imported:

- the 10 composition-indexed orbit sums spanning \(W\);
- the 17 standard tensor words obtained by deleting one word in each orbit,
  giving a complement \(C\);
- the monomial bases of \((\operatorname{Sym}^rV)^{\otimes3}\);
- the wedge bases of \(W\) and \(C\).

It constructs every Koszul column over the integers and performs sparse
column elimination modulo 65521 and independently modulo 65537. Both runs
produce:

\[
\begin{array}{c|c}
\text{map}&\text{rank}\\ \hline
K^W_{1,2}\to K^W_{0,2}&205\\
K^W_{2,2}\to K^W_{1,2}&45\\
K^W_{1,3}\to K^W_{0,3}&1000\\
K^W_{2,3}\to K^W_{1,3}&1095\\
K^W_{2,4}\to K^W_{1,4}&6625\\
K^W_{3,4}\to K^W_{2,4}&3030.
\end{array}
\]

The induced \(C\)-action has rank 65. The horizontal map out of
\(\Lambda^2C\otimes B_{1,2}\) has rank 1105, its entire target dimension.
Finally, adjoining all zig-zag images to the vertical-boundary columns raises
rank from 3030 to 3095, an increment of 65.

A rank over \(\mathbf F_p\) is witnessed by a nonzero minor of the integer
matrix, and hence is a lower bound over \(\mathbf Q\). PR #769 gives
\(\dim_{\mathbf Q}B_{2,4}=65\), so the transgression rank cannot exceed 65.
The modular lower bound 65 therefore proves rational surjectivity.

The two primes are redundant mathematically but adversarially useful: they
have identical rank profiles, and no rational reconstruction or floating
linear algebra is used.

## 6. Scope and falsifiers

The smallest falsifiers are:

1. failure of any literal Koszul composition;
2. rank below 65 for \(C\otimes B_{1,2}\to B_{1,3}\);
3. a zig-zag output not lying in \(\ker d_W\);
4. rank increment below 65 after adjoining the transgression outputs to
   \(\operatorname{im}d_W:K^W_{3,4}\to K^W_{2,4}\).

The theorem does not determine every later differential. It does not claim
that one rank-65 transgression alone proves the full classical property
\(N_3\) of the ambient Segre embedding. It proves the precise disappearance
of the Chow-base \(B_{2,4}\) strand and the nondegeneration/no-go statement.
