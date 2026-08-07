# L-15422 — Cumulative Weyl positivity is one endpoint Volterra branch domination

Claim ID: `L-15422`  
Title: The horizontal Weyl flow has an exact endpoint branch-energy primitive  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-01  
Dependencies: `L-15421`; the normalized branch features of arXiv:2606.29555  
Scope: positive canonical/Volterra route for Issue #180  
Related counterexample candidates: none

## Branch features

Let

\[
 A_s(u)=\frac{\Psi(s+u)}{\Psi(s)}
 \tag{L-15422.1}
\]

be the normalized positive Volterra ratio in the current full-`Phi` model. For `sigma in {+1,-1}` define

\[
 B_{\sigma,\omega}(s,u)
 =e^{\sigma\omega(s+u)/2}A_s(u),
 \tag{L-15422.2}
\]

and, for a test function `f`,

\[
 M_{\sigma,\omega}f(u)
 =\int f(s)B_{\sigma,\omega}(s,u)\,ds,
 \tag{L-15422.3}
\]

\[
 N_{\sigma,\omega}f(u)
 =\int (s+u)f(s)B_{\sigma,\omega}(s,u)\,ds.
 \tag{L-15422.4}
\]

Then

\[
 \boxed{
 \partial_\omega M_{\sigma,\omega}
 =\frac\sigma2 N_{\sigma,\omega}.}
 \tag{L-15422.5}
\]

## Weyl derivative form

The normalized Weyl/Volterra derivative form is

\[
 \boxed{
 \mathcal Q_\omega(f)
 =\frac12\sum_{\sigma=\pm1}
 \operatorname{Re}
 \langle M_{\sigma,\omega}f,
         N_{\sigma,\omega}f\rangle.}
 \tag{L-15422.6}
\]

Define the endpoint branch energy

\[
 \boxed{
 \mathcal V_\omega(f)
 =\frac12\left(
 \|M_{+,\omega}f\|_2^2
 -\|M_{-,\omega}f\|_2^2
 \right).}
 \tag{L-15422.7}
\]

Using (L-15422.5),

\[
 \frac{d}{d\omega}\|M_{+,\omega}f\|_2^2
 =\operatorname{Re}\langle M_{+,\omega}f,N_{+,\omega}f\rangle,
 \tag{L-15422.8}
\]

while

\[
 \frac{d}{d\omega}\|M_{-,\omega}f\|_2^2
 =-\operatorname{Re}\langle M_{-,\omega}f,N_{-,\omega}f\rangle.
 \tag{L-15422.9}
\]

Therefore

\[
 \boxed{
 \mathcal V_\omega'(f)=\mathcal Q_\omega(f).}
 \tag{L-15422.10}
\]

At `omega=0` the two branches agree, so `mathcal V_0=0`. Hence

\[
 \boxed{
 \int_0^\omega \mathcal Q_u(f)\,du
 =\frac12\left(
 \|M_{+,\omega}f\|_2^2
 -\|M_{-,\omega}f\|_2^2
 \right).}
 \tag{L-15422.11}
\]

## Strictly weaker endpoint target

Cumulative Weyl positivity requires only

\[
 \boxed{
 \|M_{-,\omega}f\|_2
 \le
 \|M_{+,\omega}f\|_2
 \quad
 \text{for every }f
 \text{ and }0<\omega<1/2.}
 \tag{L-15422.12}
\]

It does **not** require the derivative form `mathcal Q_u` to be nonnegative at every intermediate `u`. Thus a proof may allow temporary negative horizontal derivative layers, provided the endpoint branch energy remains ordered.

Combining:

1. the exact quotient-to-original Weyl identification;
2. endpoint domination (L-15422.12);
3. the flow identity `L-15421`;

produces a positive de Branges kernel. Since the associated scattering ratio has unimodular boundary values, it is inner and its Hardy Toeplitz operator is an isometry:

\[
 \boxed{T_\omega^*T_\omega=I.}
 \tag{L-15422.13}
\]

Thus the desired coercivity would hold with the strongest possible value `eta=1`.

## Why this changes the proof target

The previous programme sought:

```text
pointwise Weyl positivity for every horizontal shift
or
monotonicity of a continuously dilated Volterra energy.
```

The exact primitive shows that neither is necessary. The complete positive target is one endpoint comparison between two branch norms.

This aligns with the `G_- = C K E G_+` contraction architecture in Appendix C of arXiv:2606.29555. What remains is to prove that contraction in the metric of the **original** Weyl form, rather than only in a normalized quotient metric.

## Gap audit

- The factor `1/2` in (L-15422.7) and the branch signs in (L-15422.8)--(L-15422.9) are load-bearing.
- Complex test functions require real parts in (L-15422.6).
- The branch identity is exact in the normalized Volterra model.
- Transferring it to the original Weyl kernel requires a proved form isometry or exact quotient-to-original identity.
- Endpoint domination is still the substantive arithmetic/operator inequality; this lemma does not assert it.
