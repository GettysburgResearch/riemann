# A fixed abelian-field generalization of the ordinary-zeta bridge

Status: proved finite coefficient and operator identities, using the classical abelian factorization of a Dedekind zeta function. The field and every character are fixed. This is a general source adapter, not a new character-sum estimate or a construction of a new replica family.

The Eisenstein construction is an instance of a broader principle: when a reciprocal source contains several fixed Dirichlet L-factors, the unwanted nonprincipal factors can be removed by periodic cancellation while preserving a positive power exponent. The cost is a fixed number of scale derivatives. No subcritical bound for a reciprocal companion L-function is used.

## 1. Several mean-zero periodic filters

Let `c_1,...,c_r` be fixed periodic sequences of mean zero. Put

\[
C_j(t)=\sum_{1\le n\le t}c_j(n),\qquad
b_j=\sup_{t\ge0}|C_j(t)|<\infty,
\qquad
\mathcal T_jF(D)=\sum_{n\ge1}c_j(n)F(D/n).
\tag{1.1}
\]

Assume `F` is `r` times continuously differentiable and is zero on a fixed initial interval `(0,a)`. Let `E=D d/dD` be its logarithmic derivative. The proof of Proposition 1 in `PERIODIC_DILATION_TRANSFER.md` applies to each sequence and yields

\[
\mathcal T_jF(D)=\int_0^1 C_j(1/t)(EF)(Dt)\,\frac{dt}{t}.
\tag{1.2}
\]

All these dilation operators and `E` commute on this causal class. Iterating gives the exact formula

\[
\boxed{
(\mathcal T_1\cdots\mathcal T_rF)(D)
=\int_{(0,1]^r}
\left(\prod_{j=1}^r C_j(1/t_j)\right)
(E^rF)(Dt_1\cdots t_r)
\prod_{j=1}^r\frac{dt_j}{t_j}.
}
\tag{1.3}
\]

For each fixed `D`, causality restricts this integral to `t_1...t_r >= a/D`, a set of finite logarithmic volume; hence its bounded-integrand rearrangements are legitimate. Finite physical dilation sums give the same formula. For `r=0`, the empty composition is the identity.

**Theorem 1.** In any fixed Banach norm, if

\[
\|(E^rF)(y)\|\le M y^\alpha\quad(0<y\le D),\qquad\alpha>0,
\]

then

\[
\boxed{
\|\mathcal T_1\cdots\mathcal T_rF(D)\|
\le M D^\alpha\,\frac{\prod_{j=1}^r b_j}{\alpha^r}.
}
\tag{1.4}
\]

**Proof.** Apply the norm inequality to (1.3) and integrate each `t_j^{alpha} dt_j/t_j`, whose integral is `1/alpha`. QED.

The norm may be the weighted `ell^p` norm over a common fixed row family. For a literal ideal sum with a smooth window `W`, `E^r` changes only that window to `(-t d/dt)^r W`. Thus a common-height moment estimate for this one fixed derivative window transfers at exactly the same column exponent. All shorter scales and the same row set must be included in that premise. Neither a single-window-only bound nor pointwise smoothness with unspecified constants supplies this hypothesis.

## 2. Exact coefficient restoration for a fixed abelian field

Let `K/Q` be a fixed finite abelian extension of degree `d`. Its classical factorization is

\[
\zeta_K(s)=\zeta(s)\prod_{j=1}^{d-1}L(s,\chi_j),
\tag{2.1}
\]

where the `chi_j` are the associated nonprincipal primitive Dirichlet characters. In particular they are periodic and of mean zero. The primitive trivial character has conductor one, so its factor is the full ordinary `zeta(s)`; this convention avoids deleting unmentioned rational Euler factors.

For a fixed finite set `S` of prime ideals of `K`, define

\[
A_{K,S}(D;W)=\sum_{(\mathfrak n,S)=1}
\mu_K(\mathfrak n)W(N\mathfrak n/D),
\qquad
\mathcal R_S=\prod_{\mathfrak p\in S}(I-\mathsf S_{N\mathfrak p}),
\tag{2.2}
\]

with `S_aF(D)=F(D/a)`. Set `T_j` to be (1.1) with `c_j=chi_j`.

**Theorem 2.** For every compactly supported window in `(0,infinity)` and every `D>0`, the exact finite identity is

\[
\boxed{
\mathcal R_S\mathcal T_1\cdots\mathcal T_{d-1}
A_{K,S}(D;W)
=\sum_{n\ge1}\mu_{\mathbb Z}(n)W(n/D).
}
\tag{2.3}
\]

**Proof.** In the half-plane `Re s>1`, or as formal coefficientwise Euler products, the Dirichlet series on the left is

\[
\left[\prod_{\mathfrak p\in S}(1-(N\mathfrak p)^{-s})\right]
\left[\prod_{j=1}^{d-1}L(s,\chi_j)\right]
\frac{1}{\zeta_K(s)\prod_{\mathfrak p\in S}(1-(N\mathfrak p)^{-s})}
=\frac1{\zeta(s)}.
\]

Coefficient uniqueness, followed by the finite pairing with `W(n/D)`, proves (2.3). The product over `S` is over prime ideals, so two or more prime ideals with the same norm supply the corresponding repeated factors. QED.

The displayed factorization (2.1) is classical, not a claim of this packet. A primary exposition is Andrew V. Sutherland's MIT 18.785 lecture notes, [Lecture 19, Fall 2021, Theorem 19.15](https://math.mit.edu/classes/18.785/2021fa/LectureNotes19.pdf), on Dedekind zeta factorization for abelian cyclotomic subfields, together with [Lecture 20](https://math.mit.edu/classes/18.785/2021fa/LectureNotes20.pdf), which applies Kronecker–Weber to arbitrary finite abelian extensions. The proof of the quadratic case is also supplied directly by the split/inert/ramified Euler factors in this packet's Eisenstein bridge.

Combining Theorems 1 and 2 gives an exponent-preserving transfer from an `r=d-1` derivative bound for the fixed-field source to the ordinary Möbius source. The finite operator `R_S` changes its constant by at most

\[
\prod_{\mathfrak p\in S}(1+(N\mathfrak p)^{-\alpha}).
\tag{2.4}
\]

The derivative count and constants may depend on the fixed field. This theorem gives no uniform control when `d`, the discriminant, the character conductors, or `S` grow with `D`.

## 3. The transformed profile and the exact limits of the extension

For a smooth compactly supported window, the product of filters can again be absorbed into one profile:

\[
\widetilde W(x)=
\sum_{n_1,\ldots,n_r\ge1}
\left(\prod_j\chi_j(n_j)\right)
W(n_1\cdots n_r x).
\tag{3.1}
\]

The sum is finite at each positive `x`. Every mean-zero periodic sequence has a finite Fourier expansion with no zero-frequency coefficient. Applying the Poisson proof in `PERIODIC_DILATION_TRANSFER.md` one filter at a time shows that this profile vanishes above a fixed upper endpoint and is flat to every order at zero. The induction is legitimate because the intermediate profile, extended by zero to the negative real axis, remains a compactly supported smooth function on the real line. Its Mellin transform is exactly

\[
\widehat{\widetilde W}(s)=\widehat W(s)\prod_{j=1}^rL(s,\chi_j).
\tag{3.2}
\]

This removes the specified companion factors at the principal source; it is not nonvanishing on every Hecke row. The profile need not be real or nonnegative before the complete conjugate-character product is assembled. The one-sided sign inequality of the `chi_{-3}` case used its special nonnegative prefix sums and does not automatically hold for these general complex filters.

The coefficient transformation commutes with any independently established exact scale-dilation replica identity. It does not prove that an arbitrary field has a physical row family parameterized by all ideals, an order-six residue symbol, the same density of replicas, or the same imported mean-square theorem. Those arithmetic and geometric inputs remain separate. The complete sparse-capture theorem in this packet is stated only for the literal Eisenstein family where those inputs have been proved.

The generalization is useful because it gives a precise source-level interface for combining fixed-field reciprocal methods with ordinary Möbius detectors. It supplies a way to remove unwanted fixed factors, not a new mechanism for bounding the surviving reciprocal zeta factor.
