# R-19853 — The infinite arithmetic radical obstructs an actual one-line moat at zero

Claim ID: `R-19853`  
Status: **PROVED STRUCTURAL SCOPE FIREWALL**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-12  
Dependencies: the exact arithmetic radical map; continuity of the polarized Weil form on a fixed Hardy strip; density of the finite Fourier spaces  
Scope: distinguishes the positive residual pencil of `L-19867` from the actual localized Weil compression  
Nonclaim: isolation at a nonzero spectral parameter or after quotienting an entire radical packet is not excluded

## 1. Abstract theorem

Let `H` be a Hilbert form domain and let `Q` be a continuous Hermitian form:

\[
 |Q(f,g)|\le C_Q\|f\|_H\|g\|_H.
 \tag{R-19853.1}
\]

Let

\[
 \mathcal R=\{r\in H:Q(r,g)=0\text{ for every }g\in H\}
 \tag{R-19853.2}
\]

be its radical.  Assume `dim R=infinity`.

Let `V_j` be finite-dimensional subspaces whose union is dense in `H`, and let
`A_j` be the self-adjoint compression defined by

\[
 \langle A_jf,g\rangle_H=Q(f,g),
 \qquad f,g\in V_j.
 \tag{R-19853.3}
\]

Then, for every fixed positive integer `m`,

\[
 \boxed{s_m(A_j)\longrightarrow0,}
 \tag{R-19853.4}
\]

where the singular values are ordered increasingly.  Equivalently, since
`A_j` is self-adjoint, at least `m` eigenvalues counted with multiplicity enter
every neighborhood of zero along a cofinal subsequence.

More quantitatively, for every prescribed sequence `epsilon_j downarrow0`, one
may choose a cofinal diagonal family of finite spaces for which

\[
 s_m(A_j)\le C_m\epsilon_j.
 \tag{R-19853.5}
\]

Thus the actual compression cannot have a unique near-zero line with a
complementary two-sided moat larger than the simultaneous approximation error
of the second radical direction.

## 2. Proof

Choose linearly independent vectors

\[
 r_1,\ldots,r_m\in\mathcal R
 \tag{R-19853.6}
\]

and orthonormalize them in `H`.  By density, choose

\[
 v_{a,j}\in V_j,
 \qquad
 \|v_{a,j}-r_a\|_H\le\epsilon_j
 \tag{R-19853.7}
\]

simultaneously for `1<=a<=m`.  For all sufficiently large `j`, their Gram
matrix lies between `1/2 I` and `3/2 I`.  Put

\[
 S_j=\operatorname{span}\{v_{1,j},\ldots,v_{m,j}\}.
 \tag{R-19853.8}
\]

Let `v=sum a_a v_(a,j)` be a unit vector in `S_j`, and put
`r=sum a_a r_a`.  Uniform control of the finite Gram matrix gives

\[
 \|v-r\|_H\le C_m\epsilon_j.
 \tag{R-19853.9}
\]

Because `r` lies in the radical, for every unit `g in V_j`,

\[
 |\langle A_jv,g\rangle_H|
 =|Q(v,g)|
 =|Q(v-r,g)|
 \le C_QC_m\epsilon_j.
 \tag{R-19853.10}
\]

Taking the supremum over `g` gives

\[
 \sup_{\substack{v\in S_j\\\|v\|_H=1}}
 \|A_jv\|_H
 \le C_QC_m\epsilon_j.
 \tag{R-19853.11}
\]

The min--max characterization of singular values now yields

\[
 s_m(A_j)\le C_QC_m\epsilon_j,
 \tag{R-19853.12}
\]

which proves the theorem.

## 3. Infinite arithmetic radical

In the centered Weil setting, the arithmetic map sends every admissible source
`f` to a vector `E(f)` whose transform contains the completed zeta factor.
Therefore

\[
 \widehat{E(f)}(\rho)=0
 \tag{R-19853.13}
\]

at every nontrivial zero, with multiplicity, and the zero-side formula gives

\[
 Q_W(E(f),g)=0
 \qquad(g\text{ in the form domain}).
 \tag{R-19853.14}
\]

There are infinitely many independent admissible sources.  In one self-dual
Hermite sector, for example,

\[
 \phi_j
 =H_0(0)H_{4j}-H_{4j}(0)H_0,
 \qquad j\ge1,
 \tag{R-19853.15}
\]

satisfy the exact value/integral source conditions and are linearly
independent.  Multiplication by the nonzero zeta factor on `Re s>1` shows that
their arithmetic images remain independent.  Hence the global Weil radical is
infinite-dimensional.

Compact repair and Fourier projection approximate every fixed finite packet of
these vectors in a Hardy form norm.  The diagonal schedule may be chosen so
that the approximation error decays at any prescribed exponential rate for a
fixed packet.

## 4. Consequence for the requested isolated-line theorem

Take `r_1` to be the Xi target and `r_2` any independent arithmetic radical.
Both can be approximated simultaneously on the same cofinal Fourier schedule.
Then the actual localized Weil compression has at least two singular values at
zero scale.  More generally it has arbitrarily many on successively larger
fixed packets.

Therefore the statement

```text
one Xi-like line near zero
+ a two-sided complementary moat for the actual Weil compression
```

is false unless the construction first quotients or separates the entire
visible radical packet, or moves the target to a nonzero spectral parameter.

`L-19867` is not contradicted: its matrix is the **ordinary positive residual
Gram** built from a specially chosen exterior source reservoir.  That auxiliary
pencil has an exact identity complement even though the actual indefinite Weil
compression has a growing near-radical cluster.

## 5. Proof boundary

- The theorem is unconditional functional analysis once the exact arithmetic
  radical map and Hardy-form continuity are fixed.
- It refutes only an actual one-dimensional moat at the zero/radical scale.
- A block theorem isolating an increasing radical packet, a nonzero interior
  line, or the Pontryagin--Darboux vertical-defect route of `T-19815` remains
  logically possible.
- RH is neither assumed nor concluded.
