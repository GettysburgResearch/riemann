# Independent review of the all-row completion and raw estimate

Reviewer: `/root/audit_formalization`, an independent analysis agent in this research pass. Date: 2026-10-10.

**Verdict:** both reviewed notes pass this scoped source-and-proof audit. The extension includes every nonzero row, with nonunit zeros and sixth-power copies retained. It proves the displayed completed and raw estimates conditional on the imported analytic inputs. It does not prove the fourth moment, the general diagonal moment hierarchy, or a new zeta zero-free boundary.

## 1. Exact reviewed bytes

| Reviewed artifact in the research authoring directory | Bytes | SHA-256 |
|---|---:|---|
| `theta/ALL_ROW_COMPLETION_AND_RAW_GAIN.md` | 16,037 | `a0e6bd5517a81f44d2a18bd32dc4f0db623b9951c17068e56af7009c8914fdec` |
| `balanced/ALL_ROW_LOCAL_AUDIT.md` | 13,362 | `3e22014aeea7dbcf222f89833a27b56848deece013602a8ec4c94e9bfe46cf17` |

Publication may copy these exact bytes to its packet root. I read both complete notes, independently derived the local scalar and summability calculations, and checked the new raw optimization. The earlier squarefree completed note is bound at `411d7b28c0dabc97807d21683d731126e742d16424b1809787c87849dfb9e8d1`; the earlier squarefree raw note is bound at `8d97d0a4e6a0eef6ca0178e0dca7ff6e2cd059d594eba1e45fee47d57563cc40`. Their original reviews and bytes remain unchanged.

This report is an independent agent mathematical review, not journal peer review, a numerical proof, a Lean verification, or a full independent reconstruction of all imported analytic theorems. In particular, the source theta reflection and transformed-weight estimates, the classical sieves, PR #920's all-cusp support theorem, and its conductor-uniform infinity-type -3 reciprocal theorem remain expressly retained inputs.

## 2. Source formulas checked directly

The arithmetic checks were made against the retained October 5 manuscript at OpenAI/math commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, especially the local factors near lines 1730–1742, the all-row factorization near 2190–2209, the local transformation near 3230–3278, and the full scalar near 3414–3424. I also read the complete `ALL_CUSP_REFLECTION.md` at PR #920 commit `2edc467ef4dea4aa685219ac6a558a158b88768d`, checking that Theorem 4.1 allows any finite periodic multiplier and imposes no unit-modulus condition on it.

The source support theorem is used as an input. This audit verifies that the new multiplier and scale meet its hypotheses; it does not replace that theorem's own geometric and analytic review.

## 3. Exact scalar for a row of arbitrary valuation

The original exterior symbol forces \((a,k)=1\). Thus all primes of a have local exponent 4, while a row prime has exponent \(j=v_p(k)\bmod6\). In the full scalar, the dependence of an active row-prime factor on a is
\[
\chi_p(a)^{2j+2}.
\]
I checked the exceptional cases separately: active j=0 gives exponent 2, and j=4 gives exponent \(-2\equiv 2j+2\pmod6\). At the outer primes, the cross-factor is \(\chi_a(R)^{-2}\), where R is the active row radical. Even-power reciprocity therefore combines these factors to
\[
\chi_a\left(\prod_{p\mid R}p^{2j_p}\right)=\chi_a(k)^2.
\]
Inactive primes have exponent zero modulo six and contribute no missing phase. Their only scalar is \(1-1/Np\).

The inner CRT factors among primes of a cancel with the original cubic Gauss coefficient as in the previous scalar audit. The complete angular dependence remains \(\overline{\alpha(a)}^3\). Multiplying the original exterior \(\chi_a(k)\) gives the quadratic twist \(\chi_a(k)^3\), with fixed-ray factors and bounded row-only scalars retained.

For \(k=u_0sv^2\), the exact identity includes the mask
\[
\chi_a(k)^3=\chi_a(u_0)^3\chi_a(s)^3\mathbf1_{(a,v)=1}.
\]
Both notes keep that mask. They do not discard the square part of the row or replace a zero-extended character by a unit-modulus value.

## 4. Uniform support cutoff and local coefficient separation

For a complete projected group \(a=dg\), the new periodic multiplier is the product of the fixed additive character, the active row local factors, and \(\mathbf1_{d\mid x}\). It has period dividing \(MRd\), while the first denominator is \(c_0Ra\). Their squared norm ratio is exactly
\[
\frac{(Nc_0)^2(Ng)^2}{B(NM)^2}.
\]
The active row radical cancels. An inactive exponent-zero prime occurs in neither the denominator nor the new frequency multiplier; the earlier suggested uncancelled-period obstruction is therefore inapplicable. The all-cusp support theorem supplies the same \(Ng\ll\sqrt B\) cutoff for the complete projected group at every row.

The order of operations is correct: pruning precedes splitting the positive allocation, the cube index, the ramified valuations, or the frequency dyads. No support statement is made for an isolated truncated frequency piece.

For fixed v and \(t=(s,\operatorname{rad}v)\), the variable row \(s'=s/t\) is squarefree and avoids v. The outer factors e,f,g also avoid v. For an active prime of v with j different from 4, the extra local factor splits multiplicatively into an e-factor and an \(n',b'\)-factor after f is fixed. Its zero extension remains in the latter. For j=4, the divisibility condition is simply \(p\mid n'b'\), independent of e,f,g. After freezing b', these are exactly bounded separate coefficient vectors for the two-sieve estimate, with total squared amplitude at most \(Q_4\).

No new g-dependence appears. The negative-allocation reciprocal therefore still has infinity type -3, the fixed v-mask lies in its base character, and the moving e-exclusion is handled by the already proved radical-weight operator. Replacing e by \(re'\) in that operator preserves the fixed v-restrictions and coefficient bounds. The growing finite conductors remain polynomially bounded, as required by the imported reciprocal input.

## 5. Repeated rows and bad-prime rows really are summable

The quadratic row sieve uses \(H'=H/(Nt(Nv)^2)\); the reflected length uses \(H'Nr_v\), where \(r_v\) is the active radical inside v. These two lengths are kept distinct. The resulting block estimate has the three terms shown in (3.5), multiplied by \(Q_4\).

At a prime with \(m=v_p(v)\) and \(\delta=\mathbf1_{p\mid t}\), one has \(j\equiv2m+\delta\pmod6\). The case j=4 requires \(\delta=0\) and \(m\equiv2\pmod3\), so in particular m is at least two. Thus
\[
Q_4\le J(v)=\prod_{p^2\mid v}Np.
\]
Distinct v,t strata are disjoint sets of original rows. Summing their squared norms, with divisor-bounded branch costs, requires only the Euler sums with weights \(J(v)/(Nv)^2\) and \(J(v)/(Nv)^{4/3}\). Their first local costs are respectively \(q^{-2},q^{-3}\) and \(q^{-4/3},q^{-5/3}\). Both products converge with a positive margin. The proof does not pay a Minkowski factor for the number of original row strata.

The passage from good rows to arbitrary rows is also explicit. Writing \(k=uzk_0\), with z supported on S, replaces the fixed character by \(\xi_z(n)=\xi(n)\chi_n(uz)\) on physical good indices. Only valuations modulo six and finitely many units matter, so this is a fixed finite character family. Complete multiplicativity gives the physical completed identity in (5.1), including its cube coefficient. The height becomes \(H/Nz\); its powers 1,2,4/3 have convergent finite-prime geometric sums. Bounded nonempty dyadic row ranges below one are harmless. Therefore the statement includes all nonzero element rows, not just rows prime to S.

## 6. Raw inverse and exponent optimization

The finite cube inverse and regrouping by d=hb hold at every row. The long part retains \((a,d)=1\), allows overlap between n and d, and keeps the literal coefficient \(\sum_{h\mid d,Nh>R}\mu(h)\). Its raw column an is squarefree, so the refined all-row sieve applies with normalized envelope
\[
H+H^{1/6}L+(HL)^{2/3},\qquad L=D^2/(Nd)^3.
\]
The all-row copy cost \(H^{1/6}\) is essential and is retained. The long inverse has squared norm at most
\[
D^\epsilon[H+H^{1/6}D^2R^{-3}+H^{2/3}D^{4/3}R^{-2}],
\]
while the short terms are the companion's \(HD\), \(H^2D^{5/12}R^{7/4}\), and \(H^{4/3}D^{2/3}R^2\).

I independently balanced these expressions before reading the final draft. The two valid choices are
\[
R=D^{4/15}H^{-7/30},\quad
E\ll D^{6/5+\epsilon}H^{13/15},\quad
1\le H\le D^{38/87},
\]
and
\[
R=D^{1/3}H^{-22/57},\quad
E\ll D^{1+\epsilon}H^{151/114},\quad
D^{38/87}\le H\le D^{19/22}.
\]
The junction, admissible cutoff ranges, and remaining-term comparisons all agree. At \(H=D^{1/2}\), the cutoff is \(D^{8/57}\) and the energy exponent is \(379/228\), compared with the classical all-row exponent \(25/12\). The diagonal-size consequence through \(H\le D^{114/151}\) is also arithmetically correct.

## 7. Scope of the advance

The all-row limitation in the earlier squarefree notes is overcome for this literal completed family and its q=f=1 raw cube inverse. Their earlier notes need not be edited: this addendum supplies the additional proof. The stronger estimate still depends on the imported uniform angular reciprocal theorem, and the arbitrary outer-divisor-multiplier extension belongs only to the weaker estimate.

The new raw polynomial has Gauss coefficients; it is not the original Möbius polynomial whose full fourth moment is sought. Moving A2 exclusions on both physical axes, an additional auxiliary ideal and its intersections, the requisite covariance comparison, and the adverse transformed height near \(D^{3-\theta}\) remain untreated here. The short-height powers are row-range and mean-square exponents, not zeta zero-free boundaries. These limitations are stated accurately in the reviewed notes.

No published source or earlier frozen note was changed by this review. No new numerical experiment or kernel proof is claimed. The conclusion binds only the exact bytes listed above.
