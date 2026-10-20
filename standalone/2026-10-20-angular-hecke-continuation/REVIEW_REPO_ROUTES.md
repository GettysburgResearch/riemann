# Independent review of the angular inverse, bootstrap, and descent

Reviewer: `/root/repo_routes_audit`. Date: 20 October 2026.

**Conclusion:** No blocking mathematical gap found in the stated angular extension at the exact file versions below. This is a scoped review of the new adapter arguments and their interfaces to the identified source estimates. It does not independently certify the full upstream preprint or its scalar computation certificates.

## Frozen files reviewed

| File | SHA-256 |
|---|---|
| `ANGULAR_THETA_AND_INVERSE.md`, including its general criterion in Appendix A | `9ed89b4acf05c6fd35e7edbc0da0f0efa00a7b2b919b766846f01da0b003aa99` |
| `ANGULAR_BOOTSTRAP.md` | `0315711623796e7f4d17c3c45a921318ab0f580a1314b46b4b423e99ec924b4c` |
| `FAMILY_DESCENT.md` | `737cb82d8ddb4dab21909d0093c81919edd5e6c5384cec9ab72d49191e0aa0be` |

The comparison source was Baiying Liu, [arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835v1), PDF SHA-256 `5d0fd10274c8444c789b0b7925a1cd3419017fe760be3219b6be51d7fbed9bd5`. I checked the changed arguments against its actual Sections 4--5, 10--14 and the stated fixed-field extension in Theorem 18.2. The exact assembled inverse file was compared with the previously read core and generic drafts, then the added long-row and selected-prime sections were read against source Sections 10.5--11.2.

**Notation delta reviewed:** The initially reviewed inverse hash was `95a0025a2764c280c521b02e805c32307bd9716bfa32aac874becc312d3915d4`. In Section 5.4 the author subsequently renamed the small terminal cutoff from `d` to `d_0`, explicitly separating it from the angular generator integer `d>=2`. I inspected that clarification and reconstructed the original hash by reversing only those replacements. The final hash in the table changes no estimate, hypothesis, or exponent.

I authored `ANGULAR_PRODUCT_MOMENT.md`; this report does **not** label my reading of that file an independent review. Its corresponding exact version, `f03592bb707f7341ddabe77c4911ec7abbfcfc37292447f6d7fc6f4d235aaef6`, is an explicitly required input to the bootstrap, reviewed by the other agents.

## 1. Actual angular vectors and the global quotient

The root-derivative construction uses the complexification of the real Lie algebra, with separate holomorphic and antiholomorphic factors. The commuting relations between opposite factors, together with compact invariance of the original vector, justify the repeated Weyl identity. One cannot obtain this identity by treating the complexification as a single complex matrix algebra; the proof keeps that distinction.

Whittaker equivariance gives the actual nonzero vectors with radial function

\[
 x^{(|m|+1)/2}K_{1/3}(c\sqrt{x}).
\]

Their Mellin shifts are \((|m|+1)/2\pm1/6\). The quotient at \(t\) and \(-t\) has vertical power \(4\operatorname{Re}t\) per complex place, independently of the fixed degree. For \(m=0\), the first numerator pole is exactly \(-1/3\), outside every strict strip used by the source. Higher degrees move it left. The required positive-line absolute sheet integrals converge also at degree zero.

The character \(L_S=\prod_{v\in S}\vartheta_v^{-1}\) satisfies \(L_S(A)=\vartheta((A)_S)\) and is trivial on global \(S\)-units. Thus unit periodization is valid for actual Hecke characters. The finite unit restrictions have open kernels, permitting one common cutoff for the finite realized orbit; finite valuation phases have modulus one.

The source's Jacquet torus characters are pure norm characters, an intrinsic property unchanged by the new vector. On the norm-one quotient the local angular circle acts and preserves measure. A single nonzero angular component therefore annihilates the weighted constant term. This needs no product-shaped unit fundamental domain. The matching Whittaker term survives that same averaging.

Since every coordinate of \(\lambda\) equals \(\pm1\), an integer solution of \(ha=\pm\lambda\) forces \(h=\pm1\). The general criterion \(a\ne\pm\lambda\) consequently protects every power and its conjugate orbit. It does not cover the two resonant types.

## 2. Inverse recursion, amplification, and selected primes

I checked the locations of the angular phases, rather than treating them as arbitrary residual coefficients. The two source Gauss conversions send \(\nu\) to \(\nu G_0\xi_1\) and back to \(\nu\xi_1\xi_2\); whole-side conjugation adds the opposite angular type. The actual residual family is finite for each fixed target. The power \(\nu(b)^3\) belongs to the frozen cube coefficient, not a new residual character.

Both terminal identities separate the angular phase. In particular

\[
 L_S((RP)^2/(nb^3))
 =L_S(R)^2L_S(P)^2L_S(n)^{-1}L_S(b)^{-3}
\]

has the row/tuple independence required by the unchanged quadratic and cubic Kummer sieve. The periodic row characters remain finite order. Natural zeros are retained before restoring selected prime lists; this restoration is an exact signed identity.

The selected terminal bounds and both induction margins agree with source Section 11.2. Initialization uses \(\psi(n)\psi(P)=\psi(j)^2\psi(c)\), so the extracted factor is a contraction and the residual angular type is unchanged. The charge for a growing initial coprimality modulus remains explicit.

The sixth-power Euler identities in Sections 6 and 7.1 are exact for a unitary character. Distinct sixth-power-free rows and amplifier ideals map injectively to their product row. Averaging therefore gives the source long exponent \(\max\{1,(1+5r)/6\}\); the principal row yields smooth Möbius cancellation \(D^{11/12+\varepsilon}\). Smooth dyadic convergence then continues the reciprocal on \(\operatorname{Re}s>11/12\). No angular zero-free result is used in that base step.

## 3. Bootstrap interfaces and quantifiers

The relevant zero supremum is over all \(\Omega^h\xi\), with unrestricted finite-order conductor. Using only the fixed \(S\)-supported coefficient group would leave the prime-bound contour unjustified. The bootstrap uses the larger family consistently.

Source Lemma 13.1's nonprincipal shifts require entireness, the ordinary functional equation, and fixed polynomial height bounds; fixed angular gamma shifts preserve these facts. The compensated selection uses unitary target phases. Its identity-ray principal normalizer has no angular target factor. The actual principal Euler correction remains protected on the comparison box by its ordinary Euler domain; no bootstrap conclusion is inserted into that protection.

The detector's physical prime factors acquire inverse fixed-character coefficients, which lie in the stated finite coefficient span. The numerator in source (13.11), (14.12), and Proposition 14.3 remains finite order. A nonunit sixth-power-free numerator row has exterior ramification, so it remains outside the enlarged fixed \(S\)-supported exception group.

The proposed sequence \(11/12\), \(7/8\), \(B_\infty\), \(B_\flat\) follows the imported scalar comparisons with the same moment premises. Numerical parameters and a positive continuation gap are chosen before each target's finite analytic data. Height-cutoff powers can be chosen afterwards. Target-dependent constants and thresholds therefore do not obstruct a common continuation boundary or require the supremum to be attained.

## 4. Descent, examples, and review limits

For \(F=K(\zeta_{12})\), the finite abelian product identity has only positive exponents. Nonzero angular type makes every factor entire, preventing pole cancellation of a zero. The incomplete-Euler proof in Appendix A and the full local-factor formulation in `FAMILY_DESCENT.md` give the same consequence.

When \(E\not\subset K\), an automorphism over \(K\) conjugates \(E\). The pulled-back type is invariant under it, while the Eisenstein type changes sign. Hence neither resonance is possible. When \(E\subset K\), base change only repeats complex types, preserving a stated nonresonance. Zero angular type is finite order, including real signs.

The Gaussian example has vectors \((1,-1)\) and \((1,1)\), giving theta degrees \((0,-2)\) and exactly the displayed gamma shifts. The classical CM normalization shifts the variable by \((k-1)/2\); the document retains this shift and excludes the resonant weight-two Eisenstein family.

No lower universal finite-order boundary is proved here. The conclusion remains conditional on the source exceptional representation and finite local identities, Kummer sieve estimates, norm recursions, contour assembly, and stated scalar certificates. I did not replay those complete external computations. The smallest new load-bearing assertions are the higher-vector reflection with the stated strip, preservation of the separated coefficients, and the companion angular product moment. The review found no failure of those interfaces at these hashes.
