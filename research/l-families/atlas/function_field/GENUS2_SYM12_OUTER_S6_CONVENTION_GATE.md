# Genus-two `Sym^12`: exact outer-`S_6` convention gate

Status: exact finite character theory plus a primary-source convention audit.
No point counts, Fourier expansions, or large linear algebra are used.

Companion replay:
[`genus2_sym12_outer_s6_convention_gate.py`](genus2_sym12_outer_s6_convention_gate.py).
Canonical output:
[`genus2_sym12_outer_s6_convention_gate.json`](genus2_sym12_outer_s6_convention_gate.json).

## 1. Result

The outer-automorphism ambiguity does **not** transport the natural marked
kernel to the transitive `S_5` for the current official `(12,3)` rows.

The two conventions actually used by the relevant packets agree up to an
inner automorphism:

1. Clery--van der Geer's split-root convention fixes the action by permuting
   the six labelled Weierstrass roots and has
   `M_2(Gamma[2]) = s[2,2,2]`.
2. Bergstrom--Clery fix the `S_6` isomorphism used by the official dimension
   tables and likewise have `M_2(Gamma[2]) = s[2,2,2]`.

There are only two identifications up to inner automorphism.  Exceptional
outer pullback sends

\[
s[5,1]\longleftrightarrow s[2,2,2],
\tag{1}
\]

so it does not fix `s[2,2,2]`.  Equality of the two `M_2` labels therefore
rules out the outer class.  Inner ambiguity only conjugates the subgroup and
does not change fixed-vector multiplicities.

Moreover, the covariant/form comparison carries no additional sign twist.
The map `mu` is induced by the natural six-root quotient, the source fixes
the same natural `S_6` action on both sides, and `nu o mu` is the identity.
The alternating form `chi_5` maps to the alternating Vandermonde product
`prod_(i<j) p_ij`; its quadratic character is already an `S_6` constituent,
not an extra tensor factor added to every covariant.  The source's regularity
theorem identifies the regular covariants with the image of `mu`.
Concretely, for a regular covariant `c=mu(F)` and `h` in the natural marked
`S_5`, equivariance and injectivity give

\[
h c=c\quad\Longrightarrow\quad
\mu(hF-F)=0\quad\Longrightarrow\quad hF=F.
\tag{2}
\]

This rules out a hidden sign on the particular regular kernel, not merely on
one convenient generator.

Thus the `15`-dimensional regular marked kernel from the preceding packet is
in the **natural point-stabilizer** convention used by the official rows.
Outer or sign relabelling cannot dispose of it.  The remaining exact task is
to decompose those `15` directions into Yoshida/lift and general pieces.

## 2. Exact outer map

Let `alpha` be the exceptional outer automorphism.  On cycle types it has
the nontrivial swaps

\[
\begin{aligned}
[2,1^4]&\longleftrightarrow[2^3],\\
[3,1^3]&\longleftrightarrow[3^2],\\
[6]&\longleftrightarrow[3,2,1],
\end{aligned}
\tag{3}
\]

and fixes `[4,1^2]`, `[4,2]`, `[2^2,1^2]`, `[5,1]`, and the
identity class.  In particular it preserves parity, as it must because
`A_6` is characteristic.

Murnaghan--Nakayama applied to (3) gives the irreducible pullback map

\[
\begin{array}{c|c}
\lambda&\alpha^*s[\lambda]\\ \hline
[6]&[6]\\
[5,1]&[2^3]\\
[4,2]&[4,2]\\
[4,1^2]&[3,1^3]\\
[3^2]&[2,1^4]\\
[3,2,1]&[3,2,1]\\
[3,1^3]&[4,1^2]\\
[2^3]&[5,1]\\
[2^2,1^2]&[2^2,1^2]\\
[2,1^4]&[3^2]\\
[1^6]&[1^6].
\end{array}
\tag{4}
\]

This also sharpens a common shorthand.  Pure outer pullback does **not**
send `[2^3]` to `[3^2]`; those two Specht modules differ by tensoring with
sign.  Any source comparison phrased only as “the outer automorphism
reconciles `[2^3]` and `[3^2]`” is not yet a complete convention map.

## 3. The four marked selectors

Let `H_nat` be the point stabilizer and
`H_out=alpha(H_nat)` the transitive outer `S_5`.  Standard branching gives

\[
\dim s[\lambda]^{H_{\rm nat}}=1
\quad\Longleftrightarrow\quad
\lambda=[6]\text{ or }[5,1].
\tag{5}
\]

Transporting (5) through (4), and optionally tensoring with sign, gives four
exact fingerprints:

| subgroup/character convention | selected `S_6` irreducibles |
|---|---|
| natural, trivial | `[6]`, `[5,1]` |
| outer, trivial | `[6]`, `[2^3]` |
| natural, sign | `[1^6]`, `[2,1^4]` |
| outer, sign | `[1^6]`, `[3^2]` |

The replay obtains this table twice: from (3)--(4), and by the exact subgroup
character average over all seven conjugacy classes of `S_5`.

## 4. Application to the frozen `(12,3)` rows

The conditional `k=3` general-space query frozen by the preceding packet is

```text
[3,1^3], [2^3], [2^2,1^2], [2,1^4], [1^6].
```

Each row occurs once and the Specht dimensions sum to `30`.  Applying the
four selectors gives

| convention | fixed dimension in these rows |
|---|---:|
| natural, trivial | `0` |
| outer, trivial | `1` |
| natural, sign | `2` |
| outer, sign | `1` |

The official natural/trivial answer is therefore exactly `0`.  Had the
official marked subgroup really been the transitive outer `S_5`, the row
`[2^3]` would already contribute one fixed vector.  This is a useful
convention checksum independent of any point count or dimension
interpolation.

This does **not** prove that the general channel vanishes.  The five rows are
still the conditional nonregular `k=3` continuation recorded in the prior
packet.  Nor does the total `15`-dimensional marked kernel imply a
`15`-dimensional general space: at odd scalar weight all forms are cuspidal,
but Yoshida/lift and general summands still have to be separated.

## 5. What is closed and what remains

Closed exactly:

1. the exceptional class and irreducible permutations;
2. the natural, outer, sign, and outer-plus-sign `S_5` selectors;
3. the official-row fingerprints `0,1,2,1`;
4. the fact that the split-root and current official conventions are in the
   same inner class;
5. the absence of an additional parity sign in the regular covariant/form
   identification.

Still open:

1. the Yoshida/general decomposition of the `15` marked directions;
2. unconditional validity of the official `k=3` general-space rows;
3. the stable/general Galois channel `G` and the all-`q` `Sym^12` formula;
4. the separately source-caveated Eisenstein one-Tate discrepancy.

The next bounded calculation should therefore act on the `15`-dimensional
kernel with a lift/Yoshida diagnostic.  Repeating the valuation rank or
transporting to the outer `S_5` cannot resolve the remaining question.

## 6. Replay and sources

Run:

```text
python research/l-families/atlas/function_field/genus2_sym12_outer_s6_convention_gate.py --check
pytest -q tests/test_genus2_sym12_outer_s6_convention_gate.py
```

The replay constructs the full `S_6` character table by
Murnaghan--Nakayama, checks its orthogonality, pulls it through (3), and
performs the four exact subgroup averages.  Its largest group has order
`720`; it performs zero point counts.

Primary inputs:

- Bergstrom--Faber--van der Geer,
  [*Siegel modular forms of genus 2 and level 2: cohomological computations
  and conjectures*](https://arxiv.org/abs/0803.0917), Sections 2 and 5:
  `A_2(w^1)` is the quotient by the stabilizer of one labelled Weierstrass
  point.
- Bergstrom--Clery,
  [*Dimension formulas for spaces of vector-valued Siegel modular forms of
  degree two and level two*](https://arxiv.org/abs/2309.04388), Section 2 and
  Theorem 3.1: the official `S_6` normalization and
  `M_2(Gamma[2])=s[2^3]`.
- Clery--van der Geer,
  [*Tautological modular forms of level two and degree two*](https://arxiv.org/abs/2605.13300),
  Sections 2, 6, and 8: the natural root action, the covariant/form inverse,
  the same `M_2` type, and the marked point-stabilizer quotient.

The symmetric-group facts are classical.  The project contribution here is
the exact convention reconciliation and its application to the frozen
`Sym^12` rows.  No claim of external novelty, stable-channel nonvanishing,
or RH relevance is made from this finite audit alone.
