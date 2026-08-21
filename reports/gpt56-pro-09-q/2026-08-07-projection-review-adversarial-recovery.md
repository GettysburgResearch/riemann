# Adversarial recovery after the finite-projection review

Agent: `gpt56-pro-09-q`  
Date: 2026-08-07  
PR: #202  
Frozen launch head: `946721e3ef90cfa4070cb69c3a6367fe73119c22`  
Classification: **REVIEW VERIFIED IN ITS REFUTATIONS; ITS FINAL BLOCKER IS NOT UNIQUE; TWO FULL REPAIRS PROPOSED; RH NOT CLAIMED**

## 1. Executive verdict

The second reviewer is correct about two decisive defects in the frozen proposal.

1. `T-19810.18` is false when its source matrix is the ordinary omitted-support tail matrix. The exact finite CCM residual is `t+q`, as proved in `L-19832`.
2. Current `L-19844` has the wrong branch geometry. Every later equal-sign alias has one stationary point, and the radial endpoint is Bessel/simple-pole rather than Airy.

These points are now recorded in `R-19844`.

The review goes too far, however, when it treats

\[
 \|D_t^{-1/2}D_qD_t^{-1/2}\|\to0
\]

as the unique way to recover the proof. I found three distinct corrections.

### Correction A — full residual quotient

For the direct finite projection, the complete residual form is

\[
 D_e=D_t+D_q\succeq D_t.
\]

Thus `q` can never create a second low source direction. `L-19851` proves that only the target-line projection residual must be controlled; no whole-packet relative inequality is needed.

### Correction B — exact periodization

The Connes--Consani source range is rotation-invariant. At a non-zeta-cycle support, density plus exact rotation spectral projection implies

\[
 E_N(L)\subset\Sigma_\mu E(\mathcal S_0^{\rm ev})
\]

**exactly**, not merely after applying `P_N`. Thus the periodized high-Fourier residual can be made identically zero. The correct exact finite residual is then the alias-folded tail

\[
 W=t-\iota_L\mathfrak F_Lt
\]

of `L-19820`. This yields the repaired finite composition `T-19812`.

### Correction C — no finite projection

The continuous theorem of Connes--van Suijlekom already says that a simple isolated even ground state of the continuous localized convolution operator has a Fourier transform with only real zeros. The closed radical relation has a canonical minimum-tail quotient form. This gives the projection-free composition `T-19811`.

Accordingly:

```text
frozen T-19810:          GAPS/BLOCKED;
T-19810.18:              REJECTED;
frozen L-19844:          REJECTED AS WRITTEN;
prolate architecture:    RECOVERED IN TWO NEW CONDITIONAL FORMS;
accepted proof of RH:    NO.
```

## 2. Findings of the review that remain correct

### 2.1 Exact finite residual

For

\[
 J=E(f),\quad g=P_\lambda J,\quad t=(I-P_\lambda)J,
\]

and

\[
 v=P_Ng,\quad q=(I-P_N)g,
\]

global radicality gives

\[
 \boxed{A_{\rm fin}=Z(t+q,t+q).}
\]

Therefore

\[
 A_{\rm fin}
 =Z(t,t)+Z(t,q)+Z(q,t)+Z(q,q).
\]

No sign may be assigned to the last three terms without further analysis. The congruence in `T-19810.18` is invalid.

### 2.2 Stationary later aliases

At zero separation parameter,

\[
 \xi_0'(v)=\frac v{\sqrt{v^2-1}}.
\]

For

\[
 \phi_k(v)=\xi_0(v)-\xi_0(kv),
\]

one finds

\[
 \phi_k'(v)=0
 \quad\Longleftrightarrow\quad
 \boxed{v^2=1+k^{-2}}.
\]

The stationary point persists uniformly for the polylogarithmic mode packet. `L-19829/L-19853` give

\[
 z_{jnk}^2-1=\Theta(k^{-2}),
 \qquad
 |\phi_{jnk}''(z_{jnk})|\asymp k^3,
\]

and the summable stationary estimate

\[
 |I_{jnk}^{\rm stat}|
 \ll R^{-1/2}k^{-2}(\log R)^C.
\]

Thus the error is repairable, but it cannot be deleted.

### 2.3 Endpoint typing

The radial singular endpoint is treated by Dunster's simple-pole/Bessel model. The Airy/cubic normal form belongs to the later fold of the Mellin stationary-frequency map. `L-19853` keeps these geometries separate.

### 2.4 Quotient-energy repair

The review correctly accepts the central min--max principle. If `D` has at most one source direction below `bd_6` and `S^*HS<=KG`, then the quotient energy satisfies the sharp bound

\[
 \boxed{\theta_2(\overline D,H)\ge(b/K)d_6.}
\]

A complete lower singular-value bound for `S` is unnecessary.

## 3. New exact theorem: projection energy cannot damage the complete gap

`L-19851` starts from

\[
 D_e=D_t+D_q\succeq D_t.
\]

Hence

\[
 \dim\mathbf1_{[0,bd_6)}(D_t)\le1
 \quad\Longrightarrow\quad
 \dim\mathbf1_{[0,bd_6)}(D_e)\le1.
\]

After quotienting through an onto source map with `S^*HS<=KG`,

\[
 \boxed{
 \theta_2(\overline D_e,H)\ge(b/K)d_6.}
\]

If only the target lift satisfies

\[
 D_q(u_*)\le c d_4\|u_*\|^2,
\]

then

\[
 R_{\overline D_e}(Su_*)\le((a+c)/k)d_4.
\]

Thus the review's operator gate

\[
 D_q=o(D_t)
\]

on the entire packet is sufficient but not necessary. The actual finite low-index problem is target-specific plus a relative local-Weyl theorem for `e=t+q`.

For a fixed support and one target vector, a finite Fourier cutoff achieving any prescribed target error exists by ordinary Fourier convergence, even when the prescribed threshold is superexponentially small. This is non-effective but mathematically valid.

## 4. New exact theorem: generic density gives exact Fourier containment

The source paper explicitly states that

\[
 \mathcal R_L=\Sigma_\mu E(\mathcal S_0^{\rm ev})
\]

is invariant under circle rotations. The rotation lifts to the source dilation

\[
 f_a(x)=e^{a/2}f(e^ax),
\]

for which

\[
 E(f_a)(u)=E(f)(e^au).
\]

For `r=Sigma_mu E(f)`, the character projection

\[
 \Pi_kr
 =\frac1L\int_0^L
 e^{-2\pi ika/L}T_ar\,da
\]

is itself the arithmetic image of the Schwartz source

\[
 F_k=\frac1L\int_0^Le^{-2\pi ika/L}f_a\,da.
\]

At a non-zeta-cycle support, density ensures that some source vector has nonzero `k`-th coefficient. Its exact spectral projection is therefore a nonzero multiple of the character `e_k`. Hence

\[
 \boxed{e_k\in\mathcal R_L\quad(k\in\mathbb Z),}
\]

and

\[
 \boxed{E_N(L)\subset\mathcal R_L.}
\]

This strengthens `L-16211`: every finite CCM Fourier vector is an exact periodized arithmetic-radical image.

It does not imply that the zero extension of that vector is the original global radical. The exact residual is the complete folded tail from `L-19820`.

## 5. Repaired finite route

For an exact finite periodized vector, the high Fourier term in `L-19820` vanishes and

\[
 W=t-\iota_L\mathfrak F_Lt.
\]

The supports of the two terms are disjoint, so

\[
 \boxed{D_W=D_t+D_F\succeq D_t.}
\]

Therefore the signed `d_6` complement floor survives automatically. Only the target needs a fold upper bound:

\[
 \|\mathfrak F_Lt(u_*)\|^2
 \le R^{o(1)}\|t(u_*)\|^2.
\]

`L-19859` gives the exact target/gap transfer, and `T-19812` gives the complete finite composition conditional on the relative local-Weyl theorem for the same corrected residual `W`.

The corrected analytic ledger is:

```text
ordinary exterior tail;
minus complete multiplicative fold;
Bessel radial endpoint;
one stationary point for every later alias;
Mellin Airy fold;
collective 1/k endpoint channel;
absolutely summable higher endpoint jets;
off-line cross-branch support averaging.
```

## 6. Projection-free continuous route

There is a second, independent recovery.

### 6.1 Closed radical relation

Let the graph-closed global radical range be a closed subspace

\[
 \mathcal R_\lambda
 \subset H_{\rm in}\oplus H_{\rm out}.
\]

Let

\[
 \mathcal M
 =\{t:(0,t)\in\mathcal R_\lambda\}
\]

be its vertical part. For an interior vector `v`, the canonical tail is

\[
 \mathcal T_\lambda v
 =P_{\mathcal M^\perp}t,
 \qquad
 (v,t)\in\mathcal R_\lambda.
\]

`L-19855` proves that `mathcal T_lambda` is closed, linear, and gives the exact minimum exterior norm. Hence

\[
 \mathfrak D_\lambda(v)=\|\mathcal T_\lambda v\|^2
\]

is a closed quadratic form.

### 6.2 Form closure

`L-19856` proves that radicality survives closure in any graph topology in which the Weil form and support projections are continuous. Thus

\[
 Q_\lambda(v,w)
 =Z(\mathcal T_\lambda v,
    \mathcal T_\lambda w)
\]

on the canonical quotient domain.

### 6.3 Low-index quotient theorem

`L-19852` proves that a one-dimensional low source index descends to

\[
 \theta_2(\mathfrak D_\lambda)
 \ge R^{-o(1)}d_6,
\]

while one target lift gives

\[
 \mathfrak D_\lambda(p_\lambda)
 \le R^{o(1)}d_4.
\]

### 6.4 Relative local-Weyl descent

`L-19857` proves that a relative zero-side estimate on the canonical tails descends exactly to the closed quotient form:

\[
 (1-\eta_R)(\log R)\mathfrak D_R
 \preceq Q_R
 \preceq(1+\eta_R)(\log R)\mathfrak D_R.
\]

### 6.5 Continuous real-zero endpoint

Connes--van Suijlekom prove that a lower-bounded localized convolution operator whose lowest spectral value is simple and isolated with even eigenfunction has an entire Fourier transform with only real zeros. Therefore finite projection is not logically required.

`T-19811` combines the quotient `d_4/d_6` hierarchy, relative local-Weyl comparison, target convergence, the continuous real-zero theorem, and Hurwitz.

## 7. Correct analytic repair of `L-19844`

`L-19853` replaces the withdrawn geometry.

1. **Bessel endpoint:** exact leakage normalization and the simple-pole radial equation give
   \[
   |\rho_{n,R}(z)|
   \ll(\log R)^C
   \min(R^{1/2},(z^2-1)^{-1/4}).
   \]
2. **Stationary aliases:** every equal-sign later alias has one stationary point with curvature `Theta(k^3)` and contribution `O(R^-1/2 k^-2 log^C R)`.
3. **Mellin fold:** only the frequency-map fold uses the Airy window, producing `O(R^-1/3 log^C R)`.
4. **Endpoint aggregate:** `1/k` and `(log k)/k` channels are square-summable collectively by Parseval.
5. **Cross moat:** the complete first/rest Hermitian cross is `o(1)`; positive rest/rest self-energy is retained.

The exact stationary calculation is proved. The full complex-strip normalization and packet whitening remain proposed pending primary-source review.

## 8. Current full proposals

### Finite exact-periodized proposal — `T-19812`

```text
exact Fourier containment
-> exact alias-corrected tail W
-> quotient d4/d6 hierarchy
-> relative local-Weyl theorem for W
-> finite simple-even ground state
-> CCM finite real-zero theorem
-> target limit + Hurwitz
-> RH.
```

### Continuous projection-free proposal — `T-19811`

```text
graph-closed radical relation
-> canonical minimum-tail quotient form
-> quotient d4/d6 hierarchy
-> relative closed-form local-Weyl theorem
-> simple isolated even continuous ground state
-> Connes--van Suijlekom real-zero theorem
-> target limit + Hurwitz
-> RH.
```

The two routes share the PSWF/alias arithmetic but have different assembly endpoints. A defect in one endpoint does not automatically kill the other.

## 9. Exact remaining review frontier

The branch now cleanly separates exact repairs from the unresolved analytics.

### Exact or abstractly proved in this pass

- rejection of `T-19810.18`;
- unique stationary later-alias geometry;
- full-residual low-index monotonicity;
- exact Fourier containment from rotation invariance;
- exact alias-corrected residual identity;
- closed minimum-tail relation;
- graph-closure radical identity;
- quotient min--max and relative-form descent;
- both corrected logical compositions.

### Proposed analytic obligations

1. prove the complete signed low-index theorem on the actual finite corrected-tail reservoir or continuous quotient domain, not only the declared low packet;
2. verify the target folded-tail bound `R^(o(1))d_4` for the finite route;
3. verify the complex shrinking-strip Bessel/stationary/Airy estimates and packet whitening in `L-19853`;
4. prove the relative local-Weyl estimate on the exact folded residual or canonical quotient tail range;
5. prove moving-Hardy target convergence in the exact normalization;
6. for the continuous route, prove graph-density of the arithmetic source range in the complete localized form domain.

These are serious analytic gates. They are no longer mixed with a false finite congruence or false alias geometry.

## 10. Final status

\[
 \boxed{\text{SECOND REVIEW'S REFUTATIONS: VERIFIED}}
\]

\[
 \boxed{\text{SECOND REVIEW'S UNIQUE-BLOCKER CLAIM: TOO STRONG}}
\]

\[
 \boxed{\text{FINITE PROPOSAL: RECOVERED AS }T\text{-19812}}
\]

\[
 \boxed{\text{CONTINUOUS PROPOSAL: RECOVERED AS }T\text{-19811}}
\]

\[
 \boxed{\text{ACCEPTED PROOF OF RH: NO}}
\]
