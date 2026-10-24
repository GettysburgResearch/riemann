# The new sextic moment and PR1019's complementary inverse vector

24 October 2026. Exact coefficient audit. The new μγ₂ theorem does not
estimate the unresolved complement in PR1019. This is a comparison of
specific formulas, not an impossibility claim about a future argument.

## 1. Refreshed repository evidence

The GitHub metadata was checked again on 24 October 2026. PR1019 remains
a draft at
`GettysburgResearch/riemann@3bcc1daaeb51c71cb2785b9744cde0d641f68f4c`.
The following files were fetched at that exact head, and their local
bytes were matched to their reported Git blobs. All paths below are
under `standalone/2026-10-23-collective-mobius-projection/`.

| File | SHA256 | Git blob |
| --- | --- | --- |
| `LABEL_UNIFORM_MOBIUS_RESIDUES.md` | `12c765c1fdccec8ebb087b7608b80bb7b2d30114bf664ac1e43a2966b9d8f89d` | `e4a2c656723f5707e50fdec60ed92978cf610b93` |
| `PRIMITIVE_LABEL_CONTINUATION.md` | `a10b7626fc5a7ab7315f8327c53b2fcbe1381a2f04816a04aa697309803976ee` | `782f4cd3bc908972e75b4bcd4d322343609242ca` |
| `extensions/2026-10-23-natural-projection/NATURAL_LABEL_PRIMITIVE_PROJECTION.md` | `623253614f939fd071a131499eed8fd401429dcc6e4f6ad6a8561b121e7ce0a1` | `072af5914386506b0de6bee983de3828ab33f5a1` |
| `extensions/2026-10-23-coherent-support/COHERENT_FULL_REMAINDER_VECTOR.md` | `f6058c80c4bde0f049f7f7a50740cfae4d4a158a88e1bc6c0cb8534be8f215a4` | `b582bd47aaedff3146c301a7c033d857c6027b2f` |

The matrix convention was independently checked against Section 7 of
[rStation paper 10, version 2](https://rstation.ai/problems/riemann_hypothesis/papers/10),
the source used by PR1019. On squarefree good rows z it has

\[
 A_{z,n}=w(Nz/U)^{1/2}\chi_n(z),\qquad
 v_R(z)=U^{-1/2}w(Nz/U)^{1/2}\gamma_1(z)
                                    \overline{\chi_z(R)}.
 \tag{1}
\]

The Gauss phase in (1) is a row factor of the label frame. It is not a
Gauss factor in the coefficient vector b. PR1019's `L1` states

\[
 b_n=\frac{\mu(n)\nu_0(n)}{\sqrt{Nn}}
                         W(Nn/D)1_{(n,Q)=1}.
 \tag{2}
\]

Consequently x=A_U overline(b) is the raw sextic Möbius row vector.
Its arithmetic column is μ times fixed ray/profile data, with the
displayed puncture. The new theorem instead has column μγ₂θ.

## 2. The exact post-Poisson mismatch

The pinned quasi-Riemann Gauss identity is

\[
 \gamma_1(n)\gamma_2(n)=\mu(n)\alpha(n)G(n)
\]

on squarefree good n. The first Poisson transform of the
positive-orientation raw inverse has the following column, multiplying
conjugated sextic rows before whole-sum conjugation:

\[
 \mu(n)\gamma_1(n)
       =\alpha(n)G(n)\overline{\gamma_2(n)}.
 \tag{3}
\]

There is no Möbius factor left on the right side. After conjugating
the whole inner sum, the corresponding positive sextic orientation is

\[
 \gamma_2(n)\alpha(n)^{-1}\overline{G(n)}.
 \tag{4}
\]

For the scalar inverse this differs from the nonresonant theorem in two exact
ways: the factor μ is absent, and the apparent remaining angular type
is −1. The new one-full-factor argument requires angular type plus
one to be nonzero.

The separate `SEXTIC_RESONANT_ANGLE_COMPLETION.md` (SHA256
`c82806241f69e570814ec06b8e174f8bebf183e2ec34b59d9ef14e881ec5da1b`)
now prices angular type −1 for the coefficient μγ₂, with its additional
A^(5/6)B^(1/3) term. It does not insert the missing μ in (4), so
neither theorem applies to that raw-inverse coefficient as written.

More directly, apply the next primitive Gauss factor to (4). The
identity yields

\[
 \gamma_2(n)\alpha(n)^{-1}\overline{G(n)}\gamma_1(n)
                         =\mu(n),
 \tag{5}
\]

whereas applying it to the theorem's μγ₂θ gives μ²αGθ.
Formula (5) returns an inverse coefficient. It does not produce the
squarefree full-character coefficient to which the ordinary Hecke
functional equation in the new proof applies. This is unaffected by
conjugating the whole original family or by distributing fixed ray
characters. For nonzero original angular type the angular obstruction
can change, but the missing Möbius factor in (3)--(5) remains.

An insertion of γ₂ into b is a unitary diagonal change of the column
vector on its squarefree support. It preserves the input Euclidean
norm but generally changes A_U b and its specified row projection.
The new estimate is for its stated arithmetic coefficient; it is not
an arbitrary-coefficient operator norm invariant under that change.

## 3. The primitive and continuous expressions retain this mismatch

In `PRIMITIVE_LABEL_CONTINUATION.md`, Section 2 fixes the selected
label-prime set and states that the free coefficient is
μ(m) overline(χ_m(t)). Section 3 retains μ times the original fixed
ray data, with its full puncture and free inverse row
c₀(ed₀)²lt. These are the actual coefficients used in the completed
primitive remainder. The μ(d)γ₂(d) appearing in a selected local
inversion is attached to the frozen selected divisor d. It is not
γ₂(m) on the free column m and cannot be relabeled as that factor.

The coherent full-contour identity retains the same original b in
every label pairing and every completion scale. Its estimates improve
that label vector, but do not alter (2) or manufacture the missing
free-column Gauss coefficient. The natural-length projection result
likewise concerns P_K x for precisely this x.

If V collects the label vectors and G=V*V, the exact complementary
vector is

\[
 (I-P_K)x=x-VG^{-1}V^*x,\qquad P_K=VG^{-1}V^*.
 \tag{6}
\]

The second term in (6) is a coupled label sum with the actual Gram
inverse and label pairings. It is not a new fixed multiplicative
column coefficient. Neither the coefficient theorem nor the existing
projection estimate supplies a bound for (6). In particular, an upper
bound for P_K x cannot be subtracted from an upper bound for x to
deduce a saving for its complement.

PR1019's latest bound

\[
 \|P_Kx\|^2\ll
 U+D^{11/12}K^{1/12}+D^{5/6}K+U^{1/3}D^{2/3}
\]

therefore remains a projection result with its stated label and Gram
ranges. The new A+B theorem gives a complete estimate for a different,
explicit sextic coefficient family. A coefficient-preserving estimate
for (6), or a signed return canceling it, is still needed to transfer
these results to the full inverse consumer.
