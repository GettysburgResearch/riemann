# Field towers do not supply a free horizontal amplification

Status: exact representation-theoretic audit of a proposed new route.
No improved zero-free boundary is asserted.

Scope: finite extensions, their permutation representations, finite-image
Artin representations and unitary norm twists. No claim of global Artin
holomorphy is used.

Dependencies: Artin additivity/inductivity and Frobenius reciprocity; for an
unconditional analytic zero-persistence statement below an imported boundary,
use an abelian extension, where the other factors are entire Hecke functions.

## 1. What the repository already has

PR #1009 at `d8e93ba4ab4dc593711c791ce3a002cb5d4796af`,
`standalone/2026-10-20-liu-all-field-artin-and-barrier/artin_chebotarev.md`,
already proves the following implication by classical Brauer induction:
universal finite-order Hecke nonvanishing on \(\Re s>B\) gives nonvanishing
and holomorphy, after the required principal pole removal, for every
finite-image Artin representation on that same half-plane. It already covers
tensor, symmetric and exterior powers. Repeating that transfer would not be a
new route to a smaller numerical boundary.

Liu's arXiv:2610.26835v1, Theorem 17.1, is the source-qualified external input
for \(B=B_\flat=0.874886647039964\ldots\). This audit neither independently
verifies that long analytic proof nor strengthens its conclusion.

## 2. Exact common-factor multiplicity

Let \(E/K\) be a connected finite extension. In a common finite Galois
closure, write \(G=\operatorname{Gal}(L/K)\),
\(H=\operatorname{Gal}(L/E)\), and
\(V_E=\operatorname{Ind}_H^G1_H\). Then

\[
 \langle V_E,1_G\rangle_G
 =\langle1_H,1_H\rangle_H=1.
\tag{2.1}
\]

The Artin induction identity therefore gives the formal meromorphic
factorization

\[
 \zeta_E(s)=\zeta_K(s)L_K(s,V_E-1_G).
\tag{2.2}
\]

The coefficient of the trivial representation is exactly one, however large
\([E:K]\) is. Passing farther up a connected field tower does not turn that
forced factor into \(\zeta_K^{[E:K]}\).

For an abelian extension the complementary factor in (2.2) is a product of
nonprincipal finite-order Hecke functions, hence is entire. Every nontrivial
zero of \(\zeta_K\) persists, with at least its original multiplicity, but
(2.1) does not force extra multiplicity. Additional simultaneous zeros of the
complementary factors would be a new arithmetic input.

For a general extension, representation decomposition alone does not prove
holomorphy of the complementary Artin factor at a point below the currently
known zero-free boundary. One must supply a valid divisibility/holomorphy
theorem or restrict to a case such as the abelian one above. This caveat is
separate from, and does not weaken, the exact representation identity (2.1).

## 3. Products and tensor powers pay for the multiplicity

For a genuine finite-dimensional representation \(V\), set
\(m(V)=\dim V^G\). The canonical invariant-space decomposition gives

\[
 V=1_G^{\oplus m(V)}\oplus V_0,
 \quad
 L_K(s,V)=\zeta_K(s)^{m(V)}L_K(s,V_0),
 \quad
 0\le m(V)\le\dim V.
\tag{3.1}
\]

Tensor powers may increase \(m(V)\); they also increase the degree. The
ratio in (3.1) never exceeds one. At \(s=1\), under the standard Artin
pole-order identity in the known holomorphic region, the forced pole order is
the same \(m(V)\). One cannot count the extra target-zero multiplicities
without also retaining the corresponding degree and principal contribution.

For a product \(\prod_{i=1}^r\zeta_{E_i}(s)^{a_i}\), \(a_i\) nonnegative
integers, the forced \(\zeta_K\)-power is \(\sum_i a_i\), while the
permutation degree is \(\sum_i a_i[E_i:K]\). A virtual combination with
negative coefficients is a quotient. Its negative coefficients can introduce
poles precisely at the zeros one is trying to exclude; positivity arguments
for genuine zeta functions do not automatically apply to it.

This does not prove that every field-tower method is impossible. It proves
that the apparent free multiplicity gain is absent from these exact
factorizations. A useful new tower theorem would have to add quantitative
zero correlation, an analytic estimate beating its actual degree cost, or
something else beyond representation algebra.

## 4. Norm twisting only moves height

For the unitary norm character \(N^{it_0}\),

\[
 L_K(s,\eta N^{it_0})=L_K(s-it_0,\eta).
\tag{4.1}
\]

A zero's real part is unchanged. A real norm twist \(N^a\) would shift it
horizontally, but that character is nonunitary when \(a\ne0\). It also
changes the natural normalization of the functional equation. Applying the
same unitary zero-free statement to such a character would be an invalid
change of hypotheses.

## 5. An exact family zero-density target and its shared-factor cost

Let \(\mathcal F_Q\) be any finite family of abelian extensions of a fixed
base \(K\). For a compact set \(\Omega\) avoiding \(s=1\), let
\(N_E(\Omega)\) count the zeros of \(\zeta_E\) there, with multiplicity.
The entire-factor observation after (2.2) gives

\[
 \frac1{|\mathcal F_Q|}\sum_{E\in\mathcal F_Q}N_E(\Omega)
 \ge N_K(\Omega).
\tag{5.1}
\]

Thus an \(o(1)\) mean-zero-count theorem for the *full* zeta functions would
exclude base-field zeros in \(\Omega\). This is a useful precise target, but
it does not follow from a zero-density theorem for the quotients
\(\zeta_E/\zeta_K\): the latter have removed the very common zeros used
on the right of (5.1). The inherited common factor must be retained explicitly
when comparing a prospective density theorem to this target.

## Primary references

- J. W. Cogdell, *On Artin L-functions*, author-hosted manuscript,
  https://math.osu.edu/~cogdell/artin-www.pdf, discussion of additivity,
  inductivity and Brauer factorization, pp. 10--12.
- J. S. Milne, *Class Field Theory*, v4.03, VIII Section 10,
  https://www.jmilne.org/math/CourseNotes/CFT.pdf.
- Baiying Liu, *Zero-free half-planes for Hecke L-functions over number
  fields*, https://arxiv.org/html/2610.26835v1, Theorem 17.1 and Section 19.

All conclusions above are deductions about the stated factorization scheme;
they are not a claim that all methods using field variation have been ruled out.
