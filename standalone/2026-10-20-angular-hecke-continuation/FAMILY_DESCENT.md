# Which new Hecke and CM families the angular theorem covers

Date: 20 October 2026.

Status: proposed consequences of the angular theorem in
ANGULAR_BOOTSTRAP.md. The field descent below is a complete finite
abelian base-change argument. It does not identify an infinite-order
character with a finite-order one.

Write \(E=\mathbb Q(\sqrt{-3})\). Let \(\Lambda_E\) be the unitary
primary-generator Hecke character used in Liu's Lemma 4.2. If
\(E\subset K\), put \(\Lambda_K=\Lambda_E\circ N_{K/E}\).

## 1. Pure angular infinity type

Here a unitary Hecke character \(\eta\) has pure angular infinity type
if its complex components are

\[
 z\longmapsto(z/|z|)^{a_v},\qquad a_v\in\mathbb Z,
 \tag{1.1}
\]

and its real components are sign characters. There is no independent
radial parameter at a place. A common unitary norm twist can be
allowed afterwards by translating \(s\) by a purely imaginary
constant; the real zero-free boundary is unchanged.

The character is an actual global Hecke character, so its prescribed
infinity type and finite components obey the unit compatibility law.
The theorem does not claim that every arbitrary integer tuple is a
global character.

### Theorem

Let \(K\) be a number field and \(\eta\) a pure angular unitary Hecke
character.

1. If \(E\not\subset K\), the proposed angular theorem gives
   \(L_K(s,\eta)\ne0\) for \(\operatorname{Re}s>B_\flat\).
2. If \(E\subset K\), the same conclusion holds provided
   the infinity type of \(\eta\) is different from those of both
   \(\Lambda_K\) and \(\overline\Lambda_K\).
3. Finite-order characters remain covered, including the principal
   case with its simple pole at one permitted.

All half-planes are open. No angular-weight-uniform constant or
boundary-line assertion is made.

## 2. The base-change identity, including the possible poles

Set \(F=K(\zeta_{12})\). Then \(F/K\) is a finite abelian extension,
of degree at most four, and \(F\supset\mu_{12}\). Put
\(\eta_F=\eta\circ N_{F/K}\).
For the finite-order characters \(\tau\) of \(\operatorname{Gal}(F/K)\),
viewed as Hecke characters of \(K\), Artin formalism for this
abelian extension gives

\[
 L_F(s,\eta_F)
  =\prod_{\tau\in\widehat{\operatorname{Gal}(F/K)}}
       L_K(s,\eta\tau).
 \tag{2.1}
\]

This identity uses the full Hecke functions, with their ramified
Euler factors. One way to see it is to decompose
\(\operatorname{Ind}_{W_F}^{W_K}1\) into the characters \(\tau\),
tensor by \(\eta\), and take the local inertia-invariant
characteristic polynomials at every finite place. On the
unramified half-plane it is an identity of absolutely convergent
Euler products, and meromorphic continuation preserves it.

If \(\eta\) has nonzero angular infinity type, every factor on the
right is entire. Thus nonvanishing of the left side in an open
half-plane implies nonvanishing of each factor, including
\(\tau=1\). There is no negative exponent and no possible pole to
cancel a zero.

If its angular type is zero, a pure angular character has finite
order: after fixing its finite conductor, its remaining ideal
character factors through a finite ray class group, including
the real signs. The finite-order result already handles this case.
Equivalently, in (2.1) the only possible poles are principal
poles at one, which can be dealt with separately by the usual
nonzero Hecke and zeta residues.

## 3. Why fields not containing \(E\) have no resonance

The only excluded types in the theorem over \(F\) are those of
\(\Lambda_F\) and \(\overline\Lambda_F\).
Suppose \(E\not\subset K\).
There is \(\sigma\in\operatorname{Gal}(F/K)\) acting nontrivially
on \(E\). Otherwise \(E\) would lie in the fixed field \(K\).

The base-changed character \(\eta_F\) is invariant under \(\sigma\).
At infinity, however, \(\sigma\) sends the type of \(\Lambda_F\)
to its negative: it conjugates the chosen embedding of \(E\).
These two types are distinct, since each complex component has
degree \(1\) or \(-1\).

Consequently the type of \(\eta_F\) cannot equal either of them.
More formally, if \(\eta_F/\Lambda_F^{\pm1}\) had trivial infinity
type, invariance would imply that \(\Lambda_F^2\) had trivial
infinity type, a contradiction.

The angular theorem applies to \(\eta_F\), and (2.1) descends
the conclusion to \(K\). This argument uses Galois invariance of
the archimedean type; it does not erase that type.

If \(E\subset K\), base change only repeats the complex types,
up to the common embedding convention. The nonresonance
condition over \(K\) therefore remains nonresonance over \(F\).
This proves the second part as well.

## 4. Concrete family map

| Family | Proposed zero-free region | Reason |
|---|---|---|
| Every finite-order Hecke character over every number field | \(\operatorname{Re}s>B_\flat\) | The imported Liu theorem; no new numerical improvement for this family. |
| Every pure angular Hecke character over an imaginary quadratic \(K\ne E\) | \(\operatorname{Re}s>B_\flat\) | \(K\) does not contain \(E\); the base-change type cannot resonate. |
| \(\Lambda_E^m\xi\), \(m\in\mathbb Z\setminus\{-1,1\}\), \(\xi\) finite order | \(\operatorname{Re}s>B_\flat\) | For \(|m|\ge2\), apply the multiplicatively closed family generated by \(\Lambda^{|m|}\); \(m=0\) is finite order. |
| \(\Lambda_K^m\xi\) over any \(K\supset E\), with \(m\ne\pm1\) | \(\operatorname{Re}s>B_\flat\) | The same type criterion and abelian descent. |
| A pure angular character over a field with a real place | \(\operatorname{Re}s>B_\flat\) | Such a field cannot contain the imaginary quadratic field \(E\). |
| The two types \(\Lambda_K^{\pm1}\xi\) when \(E\subset K\) | Not supplied by this angular argument | An orbit can reach the all-spherical theta coefficient and its nonzero constant term. |

These are assertions about the stated source-dependent proof.
They are not a claim of literature-wide priority.

## 5. The Gaussian character of angular degree one

The simplest genuinely new archimedean example is
\(K=\mathbb Q(i)\), \(F=\mathbb Q(\zeta_{12})\).
Choose representatives of the two complex places of \(F\) with
the same embedding of \(E\) and opposite embeddings of \(K\).
Then the two angular type vectors are

\[
 \lambda=(1,1),\qquad a=(1,-1).
 \tag{5.1}
\]

For a Gaussian Hecke character of angular degree one pulled back to \(F\),
the theta target has angular degrees

\[
 a-\lambda=(0,-2).
 \tag{5.2}
\]

At the first place use the spherical vector; at the second use
the second negative-root derivative. The direct radial factors,
with \(x=|y|_v\), are

\[
 x^{1/2}K_{1/3}(c\sqrt{x}),\qquad
 x^{3/2}K_{1/3}(c\sqrt{x}).
 \tag{5.3}
\]

The product Mellin multiplier therefore has the shape

\[
 E(t)A^t
 \frac{\Gamma(1/3+t)\Gamma(2/3+t)
       \Gamma(4/3+t)\Gamma(5/3+t)}
      {\Gamma(1/3-t)\Gamma(2/3-t)
       \Gamma(4/3-t)\Gamma(5/3-t)}.
 \tag{5.4}
\]

Its leftmost archimedean pole is at \(-1/3\).
Every strip needed by the inverse proof is strictly to its right,
and the height exponent is \(8\operatorname{Re}t\), exactly
\(4r_F\operatorname{Re}t\) for \(r_F=2\).
The second angular component kills the global constant term.
It is unnecessary for the first component to do so as well.

For every power \(h\), the vector \((h,-h)\) differs from both
\((1,1)\) and \((-1,-1)\). Thus the entire multiplicative family
needed for the bootstrap is available, including finite-order
twists and both conjugate orientations.

## 6. CM modular-form interpretation

For a primary reference for the conventions in this section, see
Pascal Molin and Aurel Page, [Computing groups of Hecke characters,
19 October 2022](https://webusers.imj-prg.fr/~pascal.molin/pdf/hecke.pdf),
Section 2.4, Lemma 4, Section 2.5.2, and Theorem 37. The cited
statements concern Hecke gamma factors, algebraic and unitary
normalizations, and the Hecke correspondence for CM forms.

The classical Hecke correspondence associates a holomorphic CM
form of weight \(k\ge2\) to an algebraic Hecke character
\(\psi\) of an imaginary quadratic field. In unitary normalization,

\[
 \eta(\mathfrak a)
       =\psi(\mathfrak a)(N\mathfrak a)^{-(k-1)/2},
 \qquad
 L_f\!\left(s+\frac{k-1}{2}\right)=L_K(s,\eta).
 \tag{6.1}
\]

Its angular degree is \(k-1\), up to conjugation and a finite-order
twist. Formula (6.1) specifies the normalization; no assertion
about zeros should omit this shift.

The proposed theorem consequently covers:

- CM forms of every weight \(k\ge2\) whose imaginary quadratic
  CM field is different from \(E\);
- CM forms of weight \(k\ge3\) whose CM field is \(E\).

In the usual classical variable the region is

\[
 \operatorname{Re}s>\frac{k-1}{2}+B_\flat .
 \tag{6.2}
\]

For a weight-two CM form covered above, this is
\(\operatorname{Re}s>1.374886647039964\ldots\), equivalently
\(\operatorname{Re}s>B_\flat\) after centering the critical line
at \(1/2\). The two resonant types over \(E\), which include
its weight-two CM family, remain outside this argument.
