# L-91313 — The completed Fisher phase feature has an exact vector-valued Hardy colligation

Claim ID: `L-91313`  
Status: **PROVED EXACT FISHER/MODEL-SPACE COLLIGATION; PRIME-POISSON SOURCE IDENTIFICATION OPEN**  
Created: 2026-08-12  
Corrected: 2026-08-12  
Depends on: `L-91301`, `L-91306`, `L-91309`, `L-91312`, `L-91316`, `L-91401`, `R-91402`  
RH status: **unproved**

## 1. Completed Fisher source feature

Fix a safe `a>1/2`.  Let `P_a` be the completed xi probability law of
`L-91309`, and put

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

be the centered phase feature of `L-91312`, and write

\[
 m_a(x)=a\partial_a\Theta_a(x).
\tag{L-91313.3}
\]

Define

\[
 \boxed{
 \mathbf h_a(x;Y)
 =a\sqrt{V_a}\,\Theta_a(x)h_{a,x}(Y)
 \in L^2(P_a).
 }
\tag{L-91313.4}
\]

The normalized score contraction

\[
 c_a(v)=\langle v,e_a\rangle_{L^2(P_a)}
\tag{L-91313.5}
\]

satisfies, with the repository inner-product convention,

\[
 \boxed{
 c_a(\mathbf h_a(x))=-m_a(x).
 }
\tag{L-91313.6}
\]

Thus the completed scalar phase tangent is one rank-one observation of an
explicit positive source-valued feature.

## 2. Vector-valued Hardy Hankel operator

Put

\[
 \mathcal S_a=L^2(P_a),
 \qquad
 \mathscr H_a=
 (P_-\otimes I_{\mathcal S_a})
 M_{\mathbf h_a}P_+,
\tag{L-91313.7}
\]

initially on the common rational/exponential Hardy core.  Let

\[
 H_{m_a}=P_-M_{m_a}P_+.
\tag{L-91313.8}
\]

Since the score contraction acts only in the source fibre, it commutes with the
Hardy projections, and

\[
 \boxed{
 H_{m_a}
 =-(I_{H_-^2}\otimes c_a)\mathscr H_a.
 }
\tag{L-91313.9}
\]

This is the exact Fisher-source observation of the completed tangent Hankel
block.

## 3. Exact positive auxiliary

Let

\[
 \Pi_a=|e_a\rangle\langle e_a|
\]

and define

\[
 \boxed{
 \mathscr E_a
 =(I_{H_-^2}\otimes(I-\Pi_a))\mathscr H_a.
 }
\tag{L-91313.10}
\]

Orthogonal decomposition in the Fisher source fibre gives, for every Hardy
input pair `f,g`,

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
 =H_{m_a}^*H_{m_a}+\mathscr E_a^*\mathscr E_a.
 }
\tag{L-91313.12}
\]

No square root of an unknown target kernel occurs.

## 4. Suzuki model-space shape

After the completed unitary conjugation of `L-91306`, the scalar Hankel block
is Suzuki's model-space normal tangent.  In the normalization of `L-91301`,

\[
 \boxed{
 \mathcal J_a^*\mathcal J_a
 =2H_{m_a}^*H_{m_a}.
 }
\tag{L-91313.13}
\]

Hence

\[
 \boxed{
 \mathcal C_a^{\rm phase}
 :=2\mathscr H_a^*\mathscr H_a
 =\mathcal J_a^*\mathcal J_a
  +2\mathscr E_a^*\mathscr E_a.
 }
\tag{L-91313.14}
\]

This is an exact positive completed Fisher/model-space colligation.

`L-91316` gives the equivalent model-space source form

\[
 \mathcal J_a
 =a\sqrt{2V_a}\,\mathcal C_a\mathcal A_a.
\tag{L-91313.15}
\]

## 5. Correct delay and orientation extension

A raw positive Hardy delay does not generally preserve `K_(Theta_a)`.  For
`g in K_(Theta_a)`, `L-91401` supplies

\[
 S_\tau g=T_\tau g+M_{\Theta_a}R_\tau g
\tag{L-91313.16}
\]

orthogonally.  The delayed completed tangent is

\[
 \widetilde{\mathcal J}_aS_\tau g
 =\mathcal J_aT_\tau g,
\tag{L-91313.17}
\]

while `R_tau g` is retained as a positive Julia leakage coordinate.

For arbitrary mixed delays,

\[
 \boxed{
 \langle S_{\tau_i}g_i,S_{\tau_j}g_j\rangle
 =\langle T_{\tau_i}g_i,T_{\tau_j}g_j\rangle
  +\langle R_{\tau_i}g_i,R_{\tau_j}g_j\rangle.
 }
\tag{L-91313.18}
\]

Applying the same construction after Hardy reflection gives the opposite
orientation.  Thus all delay and orientation geometry is exact once the
leakage is included; raw invariance is not asserted.

The two Hardy pieces of the finite bridge admit the same resident/leakage
boundary decomposition.  Their arithmetic source norm remains open.

## 6. Relation to the ordinary-prime Poisson component

`T-91301` gives an explicit tail-Hankel Julia dilation for the actual
ordinary-prime Poisson first chaos.  The present lemma gives an explicit
Fisher-Hankel dilation for the completed xi probability source.

The scalar observations are compatible with the same completed phase tangent,
but the source laws are not identical.  `R-91402` imports Nakamura's theorem
that the completed law is not infinitely divisible for safe `a>1/2`, and hence
cannot be the same positive Poisson/Levy law.

Therefore the following remains **unproved**:

```text
ordinary-prime Poisson/Julia source
 -> completed Fisher phase source
  + positive renormalization environment.
```

The present lemma is exact on the Fisher side; it does not construct that
renormalized source map.

## 7. Correct remaining theorem

Construct the common source map `W_a` of corrected `T-91302`.  Once this map
identifies the Fisher-Hankel source norm with the completed prime/gamma/pole
source norm, the resulting source-minus-output auxiliary must be shown to equal

\[
 \mathbb K_a^{\rm del},
\]

the corrected delayed zeta screw/Weil Gram with both orientations and the
bridge.

The canonical Fisher auxiliary

\[
 2\mathscr E_a^*\mathscr E_a
\]

cannot be declared to be that defect before the common-source map is proved.

## 8. Exact boundary

```text
completed Fisher phase feature                         EXACT
score observation recovers completed phase tangent     EXACT
Fisher/model-space Hardy colligation                    EXACT
positive orthogonal Fisher auxiliary                    EXACT
raw delay invariance                                    REFUTED
compressed delay/orientation geometry                   EXACT
ordinary-prime Poisson source = completed Fisher source REFUTED
renormalized common source map                          OPEN
common-source defect = delayed screw/Weil Gram          OPEN / RH-BEARING
Riemann Hypothesis                                      UNPROVED
```
