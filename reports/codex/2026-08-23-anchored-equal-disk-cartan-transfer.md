# Anchored equal-disk Cartan transfer

Status: **EXACT FINITE CHECKPOINT; XI COFINAL ABSORPTION OPEN**

Checkpoint base:
f8102c6648829f72a6faaad06141c25b043c3f05.

## Outcome

The previously missing finite analytic interface can be made exact without
quoting a scale-ambiguous display. Normalize \(f\) by \(f(a)\), use Jensen
to count zeros in an inner disk from growth on an expanded disk, and split
the normalized function into a finite Blaschke factor and a zero-free
factor. This yields L-105114 with explicit amplitude- and coordinate-scale
invariant constants.

At \(r_1=R,r_2=2R,r_3=2eR\),

\[
n\le A_f,
\qquad
S_f\le2\varepsilon RA_f,
\]

\[
|f(z)|\ge|f(a)|
\exp\left(-[2+\log(2/\varepsilon)]A_f\right).
\]

For a finite family, the nominal radii add. Combining this with the sharp
projection lemma closes the finite common-rectangle transfer, provided the
whole candidate boundary family lies in the target disk
\(\overline D(a,r_1)\).

## Raw-quotient saving

For

\[
P=F/F',
\qquad
Q=F^2/(F'F''),
\]

only \(F'\) and \(F''\) need lower-modulus disks. Zeros of \(F\) make the
raw quotients vanish and therefore do not enter the smallest exceptional
union. An \(F\)-zero cover is required only if one chooses to pass through
\(F'/F\) or \(F''/F\).

## Source audit

Cuenin's published Lemma 34 and proof provide the modern comparison point:
[DOI 10.1007/s00220-022-04358-1](https://doi.org/10.1007/s00220-022-04358-1).
The display is not imported verbatim. Its right-side growth difference is
amplitude-scale invariant while an unnormalized \(\log|f(z)|\) is not; the
proof itself divides by the anchor. The proof's Caratheodory step also
retains \(2r_1/(r_2-r_1)\).

Dyatlov-Zworski Appendix D.1.3 gives the general Cartan/Jensen background:
[author-hosted book](https://math.mit.edu/~dyatlov/res/res_final.pdf).
L-105114 is self-contained so neither source can silently alter the
normalization or radius convention.

## Xi frontier

Use

\[
\Xi_t(z)=\xi(1/2+iz),
\qquad
g_j=\Xi_t^{(k-1+j)}.
\]

The origin is parity-forbidden as a common anchor for three consecutive
derivatives. A cofinal application still requires authenticated off-center
anchor values, expanded-disk growth for fixed \(k\), complete actual-pole
manifests, and selector absorption.

With only generic \(A_j=O_k(R\log R)\) information and a fixed-width
collar, a uniform guaranteed choice is
\(\varepsilon=O(1/(R^2\log R))\). The resulting permitted reciprocal-margin loss
can be \(\exp(O_k(R(\log R)^2))\) before edge length or selector cost.
This does not close the residue-moment scale.

No Xi evaluation, zero scan, numerical minimum-modulus search, cofinal
edge estimate, RCMV104530, or RH proof is claimed.
