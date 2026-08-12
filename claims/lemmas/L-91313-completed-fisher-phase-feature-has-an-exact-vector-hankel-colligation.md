# L-91313 — The completed Fisher phase feature has an exact vector-valued Hardy colligation

Claim ID: `L-91313`  
Status: **PROVED EXACT MODEL-SPACE COMPRESSION AND POSITIVE AUXILIARY FACTORIZATION**  
Created: 2026-08-12  
Depends on: `L-91301`, `L-91306`, `L-91309`, `L-91312`  
RH status: **unproved**

## 1. Purpose

`L-91312` expresses the complete boundary phase tangent as a Fisher covariance
on one fixed completed source space, but leaves the Hardy/model-space
compression open.  The compression is automatic once the carrier features are
kept as a vector-valued Hardy symbol.

This lemma constructs the exact conservative tangent colligation.  Its
auxiliary defect is explicit and positive.  No claim is made that this
auxiliary is already the zeta screw/Weil defect; that final identification is
separate and RH-bearing.

## 2. Completed source feature

Fix a safe `a>1/2`.  Let `P_a` be the completed exponential-tilt law of
`L-91309`, put

\[
 \sigma_a(Y)=Y-\mathbb E_aY,
 \qquad
 V_a=\mathbb E_a[\sigma_a^2]>0,
 \qquad
 e_a=\sigma_a/\sqrt{V_a}.
 \tag{L-91313.1}
\]

Let

\[
 h_{a,x}(Y)
 =\frac{e^{-ixY}}{\varphi_a(-x)}
  -\frac{e^{ixY}}{\varphi_a(x)}
 \tag{L-91313.2}
\]

be the centered phase feature of `L-91312`, and let

\[
 m_a(x)=a\partial_a\Theta_a(x).
 \tag{L-91313.3}
\]

Define the vector-valued boundary symbol

\[
 \boxed{
 \mathbf h_a(x;Y)
 =a\sqrt{V_a}\,\Theta_a(x)h_{a,x}(Y)
 \in L^2(P_a).
 }
 \tag{L-91313.4}
\]

Let the fixed score contraction be

\[
 \boxed{
 c_a(v)=\langle v,e_a\rangle_{L^2(P_a)}.
 }
 \tag{L-91313.5}
\]

With the inner-product convention chosen consistently with `L-91312.10`,

\[
 \boxed{
 c_a(\mathbf h_a(x))=-m_a(x).
 }
 \tag{L-91313.6}
\]

Thus the scalar completed tangent is one fixed rank-one observation of the
source-valued phase feature.

## 3. Vector-valued Hardy Hankel operator

Let

\[
 \mathcal S_a=L^2(P_a),
 \qquad
 \mathscr H_a=
 (P_-\otimes I_{\mathcal S_a})
 M_{\mathbf h_a}P_+.
 \tag{L-91313.7}
\]

It is initially defined on the common rational/exponential Hardy core; all
identities extend whenever the corresponding closed quadratic forms are
finite.

Let

\[
 H_{m_a}=P_-M_{m_a}P_+.
 \tag{L-91313.8}
\]

Because the scalar contraction acts only in the source fibre, it commutes with
both Hardy projections.  Equation (L-91313.6) gives

\[
 \boxed{
 H_{m_a}
 =-(I_{H^2_-}\otimes c_a)\mathscr H_a.
 }
 \tag{L-91313.9
}

This is the missing model-space/Hardy compression in `L-91312`.

## 4. Exact Pythagorean auxiliary

Let

\[
 \Pi_a=|e_a\rangle\langle e_a|
 \]

be the score projection in `S_a`, and define

\[
 \boxed{
 \mathscr E_a
 =(I_{H^2_-}\otimes(I-\Pi_a))\mathscr H_a.
 }
 \tag{L-91313.10}
\]

Orthogonal decomposition of the source fibre gives, for every Hardy input
`f,g`,

\[
 \boxed{
 \langle\mathscr H_af,\mathscr H_ag\rangle
 =\langle H_{m_a}f,H_{m_a}g\rangle
  +\langle\mathscr E_af,\mathscr E_ag\rangle.
 }
 \tag{L-91313.11}
\]

Equivalently,

\[
 \boxed{
 \mathscr H_a^*\mathscr H_a
 =H_{m_a}^*H_{m_a}+\mathscr E_a^*\mathscr E_a
 \succeq H_{m_a}^*H_{m_a}.
 }
 \tag{L-91313.12}
\]

No Douglas square root of an unknown target appears: both the observation and
the auxiliary projection are explicit.

## 5. Suzuki model-space shape

By `L-91306`, after the canonical completed unitary conjugation the
model-space normal tangent is the scalar Hankel block `H_(m_a)`.  With the
normalization of `L-91301`,

\[
 \boxed{
 \mathcal J_a^*\mathcal J_a
 =2H_{m_a}^*H_{m_a}.
 }
 \tag{L-91313.13}
\]

Hence the explicit completed Fisher-Hardy reserve

\[
 \boxed{
 \mathcal C_a^{\rm phase}
 :=2\mathscr H_a^*\mathscr H_a
 }
 \tag{L-91313.14}
\]

has the exact conservative decomposition

\[
 \boxed{
 \mathcal C_a^{\rm phase}
 =\mathcal J_a^*\mathcal J_a
  +2\mathscr E_a^*\mathscr E_a.
 }
 \tag{L-91313.15}
\]

Thus the model-space projection, causal/anti-causal Hardy split, and every
carrier cross term are compatible with the Fisher covariance contraction.

## 6. Delays, orientations, and bridge packets

Positive Hardy delays are inner multipliers and commute with the fibre
contraction `c_a`.  Reflection gives the opposite Hardy orientation.  Taking
direct sums therefore preserves (L-91313.11) on every finite
carrier/orientation/delay packet.

Any bridge vector belonging to the closed delayed form core is treated by the
same closed operator identity; no separate scalar polarization is needed.

## 7. Relation to the prime Poisson component

`T-91301` embeds the actual ordinary-prime score first chaos by the explicit
tail-Hankel Julia dilation.  The completed vector symbol (L-91313.4) is the
source-specific prime-plus-gamma/pole phase feature.  Its score projection
recovers the sum of those tangent channels, while the orthogonal fibre is a
positive completed auxiliary.

This is the operator-level embedding requested by CJHI:

```text
completed source phase first chaos
 -> two-sided Hardy tangent
  + explicit positive orthogonal source fibre.
```

## 8. The remaining defect identity

The positive auxiliary

\[
 2\mathscr E_a^*\mathscr E_a
 \tag{L-91313.16}
\]

is canonical for the Fisher phase-feature colligation.  It has not been proved
to equal the delayed zeta screw/Weil Gram of `T-91008`.

That equality cannot be inferred merely because both forms are positive under
RH.  Establishing

\[
 \boxed{
 2\mathscr E_a^*\mathscr E_a
 =\mathbb K_a^{\rm del}
 }
 \tag{L-91313.17}
\]

on the corrected delayed core would finish CDFHGI and prove RH.  A strict
positive domination with the correct coefficient-one bookkeeping may also
suffice if it is connected to the resident screw criterion, but an arbitrary
larger reserve does not.

## 9. Exact boundary

```text
Fisher phase feature as vector Hardy symbol          EXACT
score observation recovers completed phase tangent  EXACT
model-space/Hardy projection intertwining            EXACT
full polarized Pythagorean auxiliary                 EXACT
delays and two orientations                          EXACT
prime first-chaos component                          T-91301
auxiliary = delayed zeta screw defect                OPEN / RH-EQUIVALENT
Riemann Hypothesis                                   UNPROVED
```
