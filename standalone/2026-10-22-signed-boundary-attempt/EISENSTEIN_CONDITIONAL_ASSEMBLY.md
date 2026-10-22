# The direct Eisenstein consumer of the conditional 0.8745 target

22 October 2026. **Source-dependent conditional deduction.** The new
high-conductor moment remains unproved. This note identifies a matching
Eisenstein assembly; it does not assert an attained zero-free boundary.

## 1. Exact conditional statement

Assume the analytic inputs stated by Xu--Sang,
[arXiv:2610.15291v2](https://arxiv.org/html/2610.15291v2), Section 2
and its source index in Appendix G,
over `E=Q(sqrt(-3))`, including the common finite-order bound `7/8`.
Assume in addition `HC(1/100,2/25)` from
`RADICAL_STRATIFICATION.md` for every admissible fixed excluded set
`S`, coefficient ray character, and finite sector used as the target
varies in that comparison, with the stated natural zeros, punctures,
smooth-profile and height uniformity. Constants may depend on the
fixed data; the exponents `1/100` and `2/25` remain common.

Then the source comparison, with the amended detector count proved in
`CONDITIONAL_08745_CERTIFICATE.md`, implies

\[
 L_E(s,\vartheta)\ne0\qquad
 \left(\Re s>\frac{1749}{2000}\right)
\]

for every finite-order Hecke character `vartheta` of `E`, allowing its
principal pole. The same conditional conclusion holds for all Dirichlet
L-functions, including the Riemann zeta function.

This is a conditional implication under both the imported analytic
inputs and the unproved HC estimate. It does not transfer an
Eisenstein hypothesis to a different number field, and does not
require such a transfer.

The two new mathematical dependencies are pinned to:

- `RADICAL_STRATIFICATION.md`, SHA256
  `a13bc6b23c626660f1c45dbc82eff8ed8212ab1a8be64868229d33b31f2455ae`;
- `CONDITIONAL_08745_CERTIFICATE.md`, SHA256
  `ad45ffa1c0c06cfa3e464154971a858c249490d8c4d3962f34a678f7665f6dbd`.

Their independent reviews are separate. The original Eisenstein
source used by Xu--Sang is the 30 September 2026 manuscript at
OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.

## 2. Source interfaces in the same field

The following source locations were inspected directly in version 2.

| Required interface | Xu--Sang location |
|---|---|
| Eisenstein rows, finite coefficient family, literal zeros | Sections 2.1--2.2 |
| Marked M1, unmarked amplified inverse, plain M2 | Equations (4)--(7) |
| Simultaneous detector and its interval `1<=t<=3/2` | Section 2.3, (9) |
| Same compensated probe, direct bound, principal factor | Proposition 3.1 |
| Short M1/M2 crossing and long inverse count | Proposition 4.1 |
| Numerator theorem accepting a supplied row-count exponent `R` | Proposition 5.1 |
| Full endpoint, local errors, contours, all row regimes | Section 6 and Appendices C, E, F |
| Common-boundary continuation and Dirichlet transfer | Lemma 8.1 and the following theorem proof |

No field-dependent statement from Liu's cyclotomic assembly is
inserted into this route. Liu's formulas were useful for the scalar
calculation; the matching analytic interfaces here are Xu--Sang's
Eisenstein ones.

Two notation distinctions matter. Xu--Sang's amplitude `q` equals
`delta*x`; the certificate's temporary count variable `q` equals
`delta*P/D`. They are different quantities. The fixed gain `1/120`
is also different from the arbitrarily small prime-length decrement
used inside the source short-count argument.

## 3. Insert the new moment without changing its coefficient class

At the already assumed boundary `beta=7/8`, the radical reduction
has `kappa=3/4` and removes `R(u)<=D^(2/25)` with a strict
margin on `H>=D^(99/100)`. Adding HC on its actual complement
gives the full raw inverse estimate. Its exact sixth-power amplifier
then gives

\[
 \sum_{0<Nu\le U}^{(6)}|M_u(D)|^2
 \ll (UDq_Q)^\epsilon
 U^{1/6}\max\{U,D^{99/100}\}^{5/6}.
\]

For `D=U^r`, this is precisely the replacement
`e_new(r)=max(1,1/6+(33/40)r)` for the unmarked inverse estimate
in Xu--Sang (5). Their `D^(-1/2)` normalization and the packet's
`(Nn)^(-1/2)` normalization agree upon taking
`W_packet(x)=x^(1/2) W_source(x)`; this preserves the fixed
annular support and seminorm class.

The fixed finite coefficient family is handled character by character.
Whole conjugation supplies the other character orientation. The
infinite-place parameters are norm twists of the same tests; finitely
many derivatives cost a fixed polynomial in their heights. The source
chooses the height exponent after those orders. No growing arithmetic
coefficient family, row-dependent choice of prime lists, or extra
selected factor is being inserted into the new inverse theorem.

The upgraded estimate is used only on the unmarked long inverse
witness. The original marked M1 and plain M2 remain their original
source statements. The radical projector has disappeared legitimately
by adding its two complementary positive physical row sums before
amplification; it is never dropped inside a Poisson transform.

## 4. Why the amended count is accepted by the full assembly

The certificate reconstructs the detector crossing from the actual
short moment capacities. It retains the new flat inverse branch up
to `r=100/99`, uses the new count only where `1<t<3/2`, and
proves the exact short-capacity margins. This replaces the long-count
line in Proposition 4.1's proof while leaving that proof's arithmetic
coefficients and all short branches intact.

For every actual bin with `delta>=1/8`, the known `7/8` boundary
implies `delta<=3/4`. This interval is contained in the new count's
licensed range, with its upper end strictly below `4/5`. The amended count
is smooth with a positive denominator and satisfies

\[
 1-\delta\le R_{\rm new}\le R_{\rm old}
                       \le1-2\delta/3.
\]

Proposition 5.1 accepts any valid input cardinality exponent `R`.
Its supply gate becomes easier when that exponent decreases. The
raised numerator line depends on the original physical amplitude
`delta*x`, so its local factors, correction, conductor deficits and
rowwise contour construction do not change. In Section 6 the only
count-dependent changes are therefore the occurrence of
`(3R+1)/4` and its endpoint.

The coarse lower bound keeps the positive derivative in the row scale;
the upper bound keeps its fixed upper derivative bound and the
numerator-supply margin. The certificate provides the new endpoint
bound `E<=-1/25000`. Its small-delta, floor and small-row margins
are the same required expressions as Xu--Sang (29). All other rows
retain the source estimates.

Thus this is a rerun of Proposition 6.1's proof with an amended
count, rather than a claim that its old endpoint is already negative
at the new parameters. Indeed the certificate's old-envelope negative
control proves the latter claim would be false.

For the exact Xu--Sang margin convention one may take

\[
 g=1/25000,\qquad \zeta=1/10^7,\qquad g_*=1/50000.
\]

Then `g-2zeta>g_*`, and `g_*`, `2zeta` lie in `(0,1/1000)`.
Their lower allowed moment parameter `29991/40000` is below the
chosen `3/4`; their principal threshold `87/100` is below the
certificate's stricter threshold `437/500`. The buffered prime
supply and all remaining admissibility inequalities have already
been checked exactly. The finite detector and amplitude losses can
therefore be chosen within fixed positive margins.

## 5. Continuation and the zeta consequence

The amended row bound gives the same type of strict high-side saving
for the same normalized probe and principal term. Its low estimate
is unchanged. Applying the continuation argument of Lemma 8.1 to
these two estimates contradicts a family supremum larger than
`1749/2000`. This step uses the source's nonvanishing principal
correction, not an assertion about a single target in isolation.

For completeness, the norm pullback of a Dirichlet character `chi`
has, after deleting the finitely many factors above `3 cond(chi)`,
the factorization

\[
 L_E(s,\chi\circ N)=L(s,\chi)L(s,\chi\chi_{-3}).
\]

This identity is understood with those matching deletions. Away from
`s=1`, both Dirichlet factors have no pole in the positive half-plane,
so a zero of either would contradict the Hecke conclusion. At one,
the only possible principal-pole pairing has the other factor
`L(1,chi_-3)=pi/(3 sqrt(3))>0`. Deleted factors have no zeros in
positive real part. This is the source's quadratic transfer, also
checked directly in its Proposition 11.3.

The new unproved analytic requirement on this route is HC over the
Eisenstein field, with the full fixed-family scope above. The
upstream analytic assumptions are still imported. Neither this
consumer nor the scalar certificate proves HC or an unconditional
numerical improvement.
