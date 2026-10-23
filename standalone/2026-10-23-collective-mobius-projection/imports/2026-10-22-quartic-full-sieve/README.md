# Full quartic completion: a proved tail and the missing centered estimate

**Status: research contribution; no new zero-free boundary has been proved.**

The requested goal is a substantial improvement of the repository's
source-qualified zero-free half-plane. This packet does not achieve that
goal. Its main new result is an estimate for the full omitted part of the
squarefree-modulus projector in the quartic route. It includes every nonzero
physical row. A separate exact completion identity includes all numerator
valuations. The low-divisor centered spectral estimate remains open.

The inherited benchmark is still the source-qualified
`0.874886647039964...` discussed in the previous research branches. None of
the component results below changes that number or the integrated status of
the repository. In particular, no conditional decimal is presented as an
achieved boundary.

## 1. Main new estimate

Over the Gaussian integers, write

$$
T_R(k,D)=\sum_{c\ {\rm primary}}
 \frac{\xi(c)g_4(k,c)}{Nc}W(Nc/D)
 \sum_{\substack{d^2\mid c\\Nd>R}}\mu(d).
$$

Here `W` is supported in a fixed positive annulus and the column weight
`xi` is bounded by one; fixed angular, ray, and coprimality data are allowed.
The new full-row estimate is

$$
\boxed{\displaystyle
\sum_{0<Nk\le K}|T_R(k,D)|^2
 \ll_\epsilon (KD)^\epsilon
 \left(\frac K R+\frac{D^2}{R^4}\right).}
$$

The proof uses exact local prime-power Gauss sums, the support of those
sums in the physical row, and the complete multiplicative large sieve
`X+M^2`. It does not replace the rows by their squarefree cores. At
`K=D^2/H` and `R^3>=H`, the right side is `K/R`, up to a small power.
The zero row is explicitly excluded and must be handled separately in an
automorphic application.

This controls the actual omitted projector, rather than a single scalar
pairing. It still does not control the centered full second moment:
reattaching it to an estimate for the retained part requires the correct
finite arithmetic diagonal and all cross terms.

**Full proof:** [QUARTIC_PRIMITIVE_SIEVE_TAIL.md](QUARTIC_PRIMITIVE_SIEVE_TAIL.md).

## 2. Exact completion for all numerator valuations

The companion completion proof extends the published low-valuation
puncture identities to every nonzero numerator. Its new local step is

$$
\Delta_p(s,\xi)\psi_{\gamma p}(k,s,\xi;v)
 =\psi_\gamma(k,s,\xi;v)
  -\xi(p)^4(Np)^{4-4s}\psi_\gamma(k/p^4,s,\xi;v),
 \qquad p^4\mid k,
$$

where `p` does not divide `gamma`. The proof retains the Ramanujan term
at the fourth power; it does not discard repeated fourth-power rows.

After combination with the published puncture formulas, every correction
has an explicit row scale, column scale, amplitude, and angular factor.
The packet parameter `L=D/sqrt(K)` decreases under these maps. This is a
scale identity, not an estimate: when `L<1`, the reciprocal cusp height
`1/L` can increase and must be charged.

**Full proof:** [QUARTIC_ALL_ROW_COMPLETION.md](QUARTIC_ALL_ROW_COMPLETION.md).

### Correction to the inherited quartic coefficient identity

The source check found a wrong finite sign in the earlier quartic encoding.
In the DDHL convention, the correct identity for every odd primary `c` is

$$
\boxed{\widetilde g_4(c)^2=\mu(c)\frac{c}{|c|}.}
$$

The extra factor `(-1/c)_4` in
[the earlier note at its frozen revision](https://github.com/GettysburgResearch/riemann/blob/d3b3d19573b8dc47ac6e37abd108d54982e9e5f1/standalone/2026-10-18-amplified-boundary-and-global-attacks/field/PRINCIPAL_CORRELATIONS_AND_QUARTIC.md)
is incorrect. The prime `c=-1+2i` already gives the opposite sign.
The correction proves the identity at split and inert primes, extends it
by CRT and the exact nonsquarefree zeros, and repairs the first-Poisson
coefficient. The required angular degree remains nonzero. Neither the
tail lemma nor the all-row completion depends on the erroneous sign.

**Correction and full proof:** [CORRECTED_QUARTIC_CODEC.md](CORRECTED_QUARTIC_CODEC.md).

## 3. Why the original positive-energy optimization was not pursued as a boundary result

An exact optimization of the pinned cubic reflection improves the full
marked inverse-moment premises from

$$
r+2z<m,\qquad 2r+8z<3m
$$

to

$$
\boxed{r+2z<m,\qquad 2r+\tfrac{22}{3}z<3m,}
$$

with fixed strict margins and the source's precise uniformity. This is a
source-dependent theorem proposal, not a reproof of the underlying theta
reflection. Its changed terminal estimate, child transition, and
initialization are all displayed.

The improved second constraint is inactive at the current zero-count
optimizer: for `z=(1-r)/2` and `r>=23/37`, the old expression is already
`2r+8z<=102/37<3`. The first constraint is unchanged. An explicit retained
positive block attains the first constraint, so further tuning of the
second one does not address the active loss.

A separate count of inactive sixth powers improves the reflected energy
in a larger-slot regime. Its low-side exponent is not a zero-free
boundary; the high-side estimate must also be satisfied.

**Proofs:** [EXACT_COLUMN_MARKED_INVERSE.md](EXACT_COLUMN_MARKED_INVERSE.md)
and [REFINED_POWERFUL_ROW_ENERGY.md](REFINED_POWERFUL_ROW_ENERGY.md).

## 4. A substantial target with an exact consumer

One precise target bypasses the existing physical comparison. If the full
sixth-order inverse moment satisfies row volume for

$$
\sum_{0<Nu\le H}|M_u(D)|^2\ll_\epsilon H(HD)^\epsilon,
\qquad H\ge D^{21/25},
$$

with the common smooth-profile uniformity stated in the proof, then the
principal sixth-power amplifier gives

$$
\zeta(s)\ne0\qquad(\Re s>17/20).
$$

The target estimate is **unproved**. Relative to the imported moment at
that scale, it needs a full `D^(2/15)` saving. This is the intended size of
the improvement; the implication is inherited amplification, not a new
claim to have established the target.

**Consumer and proof:** [DIRECT_PRINCIPAL_TARGET.md](DIRECT_PRINCIPAL_TARGET.md).

## 5. The smallest unresolved step in the quartic route

An automorphic treatment of the retained squarefree-modulus sieve must
prove a centered quadratic estimate with its exact finite arithmetic
diagonal, uniformly in the divisor cutoff, all row divisibility masks,
angular components, and every cusp. A positive full-series mean alone
does not provide this statement.

Two specific normalization issues remain material. First, a bounded norm
of a vector on a finite cover does not give a bounded value at one chosen
component: with Haar-normalized counting on `n` cosets, that evaluation
has norm `sqrt(n)`. Second, reducing the Mellin scale below one can move
mass to the reciprocal cusp height. Both costs must be proved within the
actual scalar average; omitting either creates an unsupported saving.

[QUARTIC_SPECTRAL_INTERFACE.md](QUARTIC_SPECTRAL_INTERFACE.md) records the
exact angular Bessel reconstruction, ordinary level identity, and these
unresolved estimates separately. It does not authorize substituting a
guessed level exponent into a numerical boundary formula.

## 6. Sources, review, and preservation

- The quartic local formulas are from
  [David--Dunn--Hamieh--Lin, arXiv:2306.11875v4](https://arxiv.org/html/2306.11875v4),
  especially Section 3. The all-row completion also uses
  [Castillo--de Faveri--Dunn, arXiv:2604.01316v2](https://arxiv.org/html/2604.01316v2),
  Lemma 6.1 and Corollary 6.2.
- The full-numerator positive mean of
  [de Faveri--Dunn--Hoffstein, arXiv:2607.07911v2](https://arxiv.org/html/2607.07911v2),
  Proposition 8.1, is a reference for the spectral exploration. It is not
  an input to the native tail proof, and is not a centered primitive mean.
- The marked results depend on *The Quasi-Riemann Hypothesis*, source
  commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`, source SHA256
  `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.
  The proof notes identify every changed source use site.
- Reviews are internal, scoped mathematical checks at the recorded
  revision. They are not external peer review or formal verification.
  No finite experiment is used to certify an infinite analytic estimate.
- This packet adds files on a new research branch descended from
  `e87c5f669f81fe6371af926917d1c5b21023bce8`, the published head of
  [PR #1015](https://github.com/GettysburgResearch/riemann/pull/1015).
  Its preceding proof files and branch are preserved.
