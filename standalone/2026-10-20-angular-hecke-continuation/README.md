# Proposed unitary Hecke continuation at Liu's boundary

Date: 20 October 2026. **Status: source-dependent candidate analytic proofs,
with separate AI-agent component reviews; not an integrated or independently
certified global theorem.**

This continuation develops the missing infinite-order input in the previous
packet. It constructs higher angular vectors in the actual exceptional
theta representation, extends the inverse and product moments, and runs
Liu's continuation argument for nonresonant unitary Hecke families. It also
derives a stronger cubic Type-I estimate with an explicit level cost.

The external starting point is Baiying Liu,
[*Zero-free half-planes for Hecke L-functions over number fields*,
arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835v1), submitted
19 October 2026. That preprint states the boundary

\[
 B_\flat=0.874886647039964\ldots,
 \qquad
 133488B_\flat^4-376596B_\flat^3+384534B_\flat^2
 -167541B_\flat+26231=0
\]

for every **finite-order** Hecke character over every number field.
The new contribution below proposes the same boundary for much larger
families. It does not decrease the numerical finite-order boundary.

## 1. The proposed family theorem

Let \(E=\mathbb Q(\sqrt{-3})\), and let \(K\) be a number field.
The proposed conclusion is absence of zeros in the **open** half-plane
\(\operatorname{Re}s>B_\flat\), with a possible translated principal
pole permitted.

| Family | Proposed scope |
|---|---|
| \(K\) does not contain \(E\) | Every unitary Hecke character of \(K\), including arbitrary fixed angular and radial infinity parameters |
| \(K\) contains \(E\) | Every unitary Hecke character except \(\Lambda_K^{\pm1}\xi N^{it}\), where \(\Lambda_K\) is the norm pullback of the source Eisenstein character, \(\xi\) is finite order, and \(t\in\mathbb R\) |
| Any field with a real place | Every unitary Hecke character; such a field cannot contain \(E\) |
| Holomorphic CM modular forms over an imaginary quadratic field other than \(E\) | Every weight \(k\ge2\), in unitary normalization |
| Holomorphic CM forms with CM field \(E\) | Weights \(k\ge3\); the weight-two family is resonant and remains outside this proof |
| Dihedral Maass forms induced from real quadratic Hecke characters | Their unitary Hecke factors are covered by the general unitary statement |

The assertions concern actual global characters, with their unit
compatibility and finite conductors. Arbitrary prescribed infinity tuples
are not automatically global characters. Constants and thresholds may
depend on fixed archimedean parameters; no estimate uniform in a growing
angular weight or radial parameter is asserted.

The pure-angular proof is in
[ANGULAR_THETA_AND_INVERSE.md](ANGULAR_THETA_AND_INVERSE.md),
[ANGULAR_PRODUCT_MOMENT.md](ANGULAR_PRODUCT_MOMENT.md), and
[ANGULAR_BOOTSTRAP.md](ANGULAR_BOOTSTRAP.md).
The fixed radial extension is proved separately in
[BALANCED_UNITARY_INVERSE_ADDENDUM.md](BALANCED_UNITARY_INVERSE_ADDENDUM.md)
and
[BALANCED_UNITARY_MOMENT_ADDENDUM.md](BALANCED_UNITARY_MOMENT_ADDENDUM.md).
The field and CM examples, including the classical shift
\(s\mapsto s+(k-1)/2\), are explained in
[FAMILY_DESCENT.md](FAMILY_DESCENT.md).

## 2. The analytic change that makes the extension possible

At a complex place, the exceptional representation's actual spherical
vector gives higher angular Whittaker vectors

\[
 W_m(a(y))=x^{(|m|+1)/2}(y/|y|)^mK_{1/3}(c\sqrt{x}),
 \qquad x=|y|^2.
\]

The proof uses the two factors in the complexification of the **real**
Lie algebra \(\mathfrak{sl}_2(\mathbb C)\). Compact invariance and the
commuting opposite factors give the repeated Weyl identity; this is not
an assumed higher-weight functional equation.

Its Mellin shifts are \((|m|+1)/2\pm1/6\). The reflected multiplier
has the same vertical exponent and the same strict strip
\(\operatorname{Re}t>-\delta\), \(\delta<1/3\), including degree
zero. A nonzero angular component at one place annihilates the constant
term on the global unit quotient.

For fixed radial parameters, first remove the common norm twist. The
remaining parameters \(\gamma_v\) satisfy \(\sum_v\gamma_v=0\).
The multiplier then contains

\[
 \frac{\Gamma(A_v+t+i\gamma_v)\Gamma(B_v+t+i\gamma_v)}
      {\Gamma(A_v-t-i\gamma_v)\Gamma(B_v-t-i\gamma_v)}.
\]

Its exponential Stirling factors cancel exactly and its pole real parts
are unchanged. When every angular degree is zero but the balanced radial
vector is nonzero, the addendum uses the actual finite Jacquet spectrum
and translation on the norm-one torus to annihilate the constant term.
The two genuinely resonant balanced types are left explicit.

The arithmetic adapters retain the cube-divisor coefficients, shared-prime
zeros, selected-prime factors, finite unit corrections, and moving
conductors. Transforms close in a finite realized coefficient list for
each target. The zero-free premise in the product moment uses the larger
family \(\{\Omega^h\xi\}\) with **arbitrary finite-order conductor**,
rather than only characters supported in the fixed excluded set.

These inputs give the noncircular progression

\[
 11/12\ \longrightarrow\ 7/8\ \longrightarrow\
 0.874957019420098946\ldots\ \longrightarrow\ B_\flat.
\]

The numerical comparison is imported from Liu. The new work justifies its
analytic interfaces for the enlarged family. Base change to
\(K(\zeta_{12})\), followed by an abelian product identity, gives the
field theorem without identifying an infinite-order character with a
finite-order one.

## 3. A concrete cubic cancellation estimate

For a fixed nonzero integer \(\ell\), a squarefree primary
\(r\in\mathbb Z[\omega]\), \(R=Nr\), and a fixed smooth annular
weight \(W\), the transfer theorem in
[ANGULAR_TYPE_I.md](ANGULAR_TYPE_I.md) proves

\[
 \boxed{
 \sum_u\widetilde g(ur)\alpha(u)^\ell W(Nu/X)
 \ll_{\ell,W,\varepsilon}
 X^{(2\beta+1)/6+\varepsilon}R^{(5-2\beta)/12+\varepsilon},}
\]

assuming zero-freeness of the actual angular Hecke factor
\(L_E^{(3)}(z,\alpha^{3\ell})\) for \(\operatorname{Re}z>\beta\).
It uses the exact functional equation and transformed coefficients in
Dunn–Radziwiłł,
[*Bias in cubic Gauss sums: Patterson's conjecture*, v3](https://arxiv.org/html/2109.07463v3),
Proposition 5.2. No GRH-dependent theorem from their Section 8 is imported.

Every nonzero \(3\ell\) avoids the two resonant angular degrees. Using
the candidate theorem at \(\beta=B_\flat\) gives

\[
 X^{0.458295549013321\ldots+\varepsilon}
 R^{0.270852225493339\ldots+\varepsilon}.
\]

At fixed level this improves the same functional equation's direct
Euler-product estimate \(X^{1/2+\varepsilon}\). The full comparison
saves \((X/R^{1/2})^{(1-\beta)/3}\), so the level dependence is
material. The \(\ell=0\) version includes an explicit
\(X^{5/6}\) main term, rather than claiming cancellation of that bias.

The theorem also bounds a cubic Gauss block carrying a coherent short
Möbius-divisor mark. At fixed level and total scale \(Y\), it falls
below \(Y^{5/6}\) with a fixed power margin when the marked divisor
length is at most
\(Y^{0.461552769395323\ldots-\eta}\), \(\eta>0\).
The remaining quadratic component and the complete mixed operator mean
are not supplied by this estimate.

## 4. Stronger protection of the principal correction

The inherited identity is

\[
 H_\eta(s)=L_F^S(6s-3,(\overline\Lambda\eta)^6)K_\eta(s),
 \qquad K_\eta\text{ a holomorphic unit for }\operatorname{Re}s>1/2.
\]

For a finite-order target \(\eta\), the extracted character has
angular degree \(-6\lambda\) and is covered by the candidate angular
theorem. Thus
[PRINCIPAL_PROTECTION.md](PRINCIPAL_PROTECTION.md) improves the
nonvanishing domain of \(H_\eta\) from \(\operatorname{Re}s>2/3\) to

\[
 \operatorname{Re}s>\frac{3+B_\flat}{6}
                    =0.645814441173327\ldots .
\]

This number is a boundary for the principal correction. It is not a new
zero-free boundary for finite-order Hecke functions.

## 5. Review, reproduction, and what remains open

The primary sources and exact versions are in [SOURCES.json](SOURCES.json).
The finite-order usage audit identifies the changed analytic interfaces.
Independent component reviews by separate AI agents are bound to file
hashes; they are distinguished from author checks and human review in
[REVIEW.md](REVIEW.md). The full upstream preprint and its numerical
comparison certificates remain imported dependencies. The packet has not
received integration approval.

Run from this directory:

```bash
python -I -S -B replay.py
```

This checks the packet manifest and reruns exact finite Lie algebra,
Mellin-shift, root-isolation, and exponent identities. These checks do
not certify the analytic proofs or global zero-freeness. See
[LOCAL_ALGEBRA.json](LOCAL_ALGEBRA.json) for the exact arithmetic scope.

The existing source factorization in PR #1006 was missed in the first
attribution comparison. [ATTRIBUTION_CORRECTION.md](ATTRIBUTION_CORRECTION.md)
gives its exact commit, blob, and formula. The new analytic input is kept
distinct from that inherited calculation.

[MIXED_MEAN_STATUS.md](MIXED_MEAN_STATUS.md) records the complete
\(U^{6/5+\varepsilon}\) mixed-moment target and all its relevant length
regimes. Its long inverse edge already requires more improvement than
the previously quoted \(7/40\) corner gap. The Type-I result resolves
one structured cubic block, not this complete target. A smaller universal
finite-order boundary and the two resonant unitary families remain open
in this contribution. RH remains unproved.
