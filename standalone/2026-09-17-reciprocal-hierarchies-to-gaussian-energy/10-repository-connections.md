# 10. Repository interfaces and pinned provenance

**Scope:** targeted relationship map, not a fresh audit of all branches or an integration verdict. A historical chat report is not upgraded to a new source read. All additions in RHG26 are confined to this packet.

## 1. Publication baseline and relevant frozen work

The live main branch was read during publication and was at `f99d9e3908dde4865377c75d9ca051c1f545bf4f`, tree `8bddd12122e8a772683c9ed0b37dbcb945036893`. README and AGENTS require source-qualified exploratory claims and independent review. This packet follows the add-only standalone pattern and changes no canonical status.

| Repository reference | Frozen source recorded in this conversation | Use and reading boundary |
|---|---|---|
| Main | `f99d9e3908dde4865377c75d9ca051c1f545bf4f` | Publication base; README/AGENTS read during packaging |
| Integration #830 | `a20e80654d33afc128261895291ccc37bb328402` | Historical handoff reference; not substituted for main or freshly reviewed |
| #828 grounding capacity | PR identifier; no full head supplied in the visible discussion | Chat-derived product-box formula reproduced below; not a fresh audit or new discovery claim |
| #836 causal completion | PR identifier; no full head supplied here | Historical exact-prefix energy connection; no fresh full replay |
| #848 XCC26 | `99101457b32b6f10f4eda88ca998048404b860ea` | Causal factorial witness and crossings, as pinned by the #869 source |
| #866 DG26 | `cb05d3052611bd1804459887e84fdec3cb7064af` | Polynomial trace/cutoff programme; orientation from #869 source |
| #869 original | `6603f8b04f9a2d073123a328ac0298a498c93a96` | Historical three-route arithmetic proof |
| #869 follow-up | `5e559c9cbf5aee84ff7ed78dc91b55df744aef56` | Live PR metadata verified; `standalone/2026-09-12-four-route-deep-pass/arithmetic.md` lines 1–160 freshly read |
| #875 initial arithmetic | `be149104721ae7b65b624c100118edfd7b76b69b` | Historical covariance/diagonal source; later extensions not silently included |
| #875 later additions | `177cf75e93b5614c5d5f0db1e4721ac69727e5ce`, `00af30b4b3f810c7cd03fe94ba2f43b6c6b90538` in PR publication receipts | Metadata/body orientation only during packaging; no re-execution |
| #876 homotopy | PR identifier only | Historical opening read reported in chat; no imported completion |
| Issues #736/#764; L-91029 | Identifiers from the original handoff | Character-family, causal-Euler and prime-power semigroup leads; not newly audited here |

Primary links:
- [main](https://github.com/GettysburgResearch/riemann/tree/f99d9e3908dde4865377c75d9ca051c1f545bf4f)
- [frozen #869 arithmetic](https://github.com/GettysburgResearch/riemann/blob/5e559c9cbf5aee84ff7ed78dc91b55df744aef56/standalone/2026-09-12-four-route-deep-pass/arithmetic.md)
- [frozen #875 arithmetic](https://github.com/GettysburgResearch/riemann/blob/be149104721ae7b65b624c100118edfd7b76b69b/standalone/2026-09-12-astra-collision-chain-flow/ARITHMETIC.md)
- [frozen #848 proof](https://github.com/GettysburgResearch/riemann/blob/99101457b32b6f10f4eda88ca998048404b860ea/standalone/2026-09-12-astra-crossing-cofinal/PROOF.md)

The fresh #869 reading confirms the relevant boundary: native covariance is identified with annular reciprocal-Möbius energy up to a paid collar; the common exponent is identified; the subpower upper bound remains open. Different diagonals and norms cannot be exchanged merely because their exponent has the same zero-theoretic interpretation.

## 2. Finite Golomb Euler thinning preserves off-critical poles

Let Q_y=product_(g<=y)g, E_y(s)=product_(g<=y)(1-g^(-s))^(-1), and
\[
b_y(n)=\mu(n)1_{(n,Q_y)=1}.
\]
Exactly for Re s>1,
\[
\sum_n b_y(n)n^{-s}=E_y(s)/\zeta(s).
\]
For the compact Mellin detector of the handoff,
\[
F_y(X)=\sum_{n\le X}\frac{b_y(n)}{\sqrt n}K(X/n),
\quad
\mathcal MF_y(z)=\widehat K(z)\frac{E_y(z+1/2)}{\zeta(z+1/2)}.
\]
For fixed y, E_y is holomorphic and nonzero on Re s>0, so it cannot cancel an off-critical reciprocal-zeta pole. The original source is restored by the exact finite identity
\[
F_\mu(X)=\sum_{d\mid Q_y}\frac{\mu(d)}{\sqrt d}F_y(X/d).
\]
Taking absolute values incurs
\[
A_y=\prod_{g\le y}(1+g^{-1/2}),\qquad
\log A_y\sim\frac{2\sqrt y}{\log y\log_2y},
\]
while \(\log Q_y\sim y/\log_2y\). Thus slow harmonic divergence at exponent 1 does not guarantee a small critical exponent-1/2 restoration or character-conductor cost. These are absolute upper budgets, not lower bounds on an optimally signed recombination.

## 3. A genuine capacity improvement from Golomb thinning

For a finite prime alphabet A, use squarefree products n and harmonic probability proportional to 1/n. The product-box edge energy from the conversation has exact root-contrast capacity
\[
\mathfrak G_A=\int_0^\infty
\left[\prod_{p\in A}\left(1+\frac1p e^{-(1+1/p)(\log p)t}\right)-1\right]dt.
\]
For all primes through Y the reported repository result is
\(\mathfrak G_A=\zeta(2)^{-1}\log_2Y+O(1)\).
For A=G intersect [1,Y], the product is bounded by
\[
\prod_{g\in G}(1+g^{-1-t})\le Z_G(1+t).
\]
By Chapter 03, Z_G(1+t)~C_G log(1/t), integrable at zero; the tail at infinity is exponentially integrable. Hence
\[
\sup_Y\mathfrak G_{G\cap[1,Y]}<\infty.
\]
The fixed-coordinate spectral gap is bounded below, so the corresponding anchored variance inequality is uniform. This is a genuine component improvement, not just a slower divergence statement.

However, the complementary prime alphabet B has
\[
Z_B(1+t)=\zeta(1+t)/Z_G(1+t)\sim
1/[C_Gt\log(1/t)],
\]
which remains nonintegrable. The squarefree product differs by a finite nonzero denominator factor near t=0. The complement retains an obstruction; restoring it must be paid.

## 4. Why SHARP at the critical power is not fixed by a deeper fixed tower

The inherited m>=2 SHARP argument uses summable prime weights of exponent (m+1)/2. At m=1 they become harmonic. Replacing primes by G slows divergence to log_3Y, but every fixed level of the proposed logarithmic tower still diverges. A global subunit-sum argument is not restored merely by taking a deeper fixed family. Depth varying with detector scale requires a new uniform estimate and a source-restoration proof.

## 5. The causal completion barrier

If a finite coefficient sequence preserves a_n=mu(n) through Y, its cumulative sum through every x<=Y is fixed. For the complete causal energy
\[
J(a)=\int_1^\infty\left|\sum_{n\le x}a_n\right|^2x^{-2}dx,
\]
one necessarily pays the prefix contribution
\(\sum_{k\le Y}M(k)^2/[k(k+1)]\), with endpoint conventions fixed by the completion. The historical #836 result identifies the exact late-completion minimum in its setup. Later coefficients cannot erase earlier accumulated energy. An oracle using future Möbius coefficients is a sharpness example, not a short-prefix estimate.

The smooth Q_j and Gaussian G_omega are different norms. Chapters 06 and 09 explicitly pay their noncausal leakage rather than assume this causal prefix argument applies unchanged.

## 6. The useful interface for future repository work

Potential inputs from character families, residue martingales, finite-torus methods, approximate polynomial models or prime-factor decompositions must be stated as inequalities for one of:

1. the literal native covariance, with its full product support and diagonal;
2. the complete reciprocal-Möbius energy and endpoint;
3. Q_j or fixed G_omega, with a proved norm adapter;
4. a moment-packet decomposition with every residual and inter-group cost retained.

A family-level estimate, a finite-model positivity result, or a common growth exponent does not establish the required source-specific upper comparison. This packet adds interfaces and audit material; it does not promote any other branch to accepted mathematics.
