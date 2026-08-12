# L-91403 — The prime-inclusive quasi-Lévy source has an explicit completed Hardy colligation

Claim ID: `L-91403`  
Status: **PROVED EXACT PRIME-Fock-INCLUSIVE COMPLETED TANGENT COLLIGATION; SCREW-DEFECT IDENTIFICATION OPEN**  
Created: 2026-08-12  
Depends on: `L-91036`, `L-91301`, `L-91306`, `L-91307`, `L-91316`, `L-91401`, `L-91402`  
RH status: **unproved**

## 1. Source-valued completed tangent symbol

Fix `a>1/2`, put `sigma=1/2+a`, and let

\[
 \mathcal S_\sigma
 =\mathbb C
  \oplus L^2(\nu_\sigma^+)
  \oplus L^2(\nu_\sigma^-)
\]

be the positive two-channel quasi-Lévy source of `L-91402`.

Let

\[
 \mathfrak n_\sigma
 =\|(1,x,-x)\|_{\mathcal S_\sigma},
 \qquad
 e_\sigma=\frac{(1,x,-x)}{\mathfrak n_\sigma},
\]

and let

\[
 c_\sigma(v)=\langle v,e_\sigma\rangle
\]

be the norm-one score observation.

The explicit source-valued symbol

\[
 \boxed{
 \mathbf q_a(t)
 =a\mathfrak n_\sigma\Theta_a(t)
  \left(-2it\lambda_\sigma',G_t,G_t\right)
 }
\tag{L-91403.1}
\]

satisfies

\[
 \boxed{
 c_\sigma(\mathbf q_a(t))
 =m_a(t),
 \qquad
 m_a(t)=a\partial_a\Theta_a(t).
 }
\tag{L-91403.2}
\]

The positive atomic source summand contains the ordinary-prime Poisson
one-particle space through the explicit isometry `I_a^p` of `L-91402`, and its
symmetric second quantization embeds the entire prime Fock system.

## 2. Vector-valued Hardy Hankel operator

Let `P_+` and `P_-` be the standard Hardy projections. On the common
rational/exponential form core, define

\[
 \boxed{
 \mathscr Q_a
 =(P_-\otimes I_{\mathcal S_\sigma})
  M_{\mathbf q_a}P_+.
 }
\tag{L-91403.3}
\]

Let

\[
 H_{m_a}=P_-M_{m_a}P_+.
\tag{L-91403.4}
\]

Since the fibre observation commutes with the Hardy projections,

\[
 \boxed{
 H_{m_a}
 =(I_{H_-^2}\otimes c_\sigma)\mathscr Q_a.
 }
\tag{L-91403.5}
\]

Thus Suzuki's complete tangent Hankel is an explicit contraction of one
prime-inclusive positive source Hankel. The identities extend to the
corresponding closed forms whenever finite.

## 3. Exact positive source auxiliary

Let

\[
 \Pi_\sigma=|e_\sigma\rangle\langle e_\sigma|
\]

and define

\[
 \boxed{
 \mathscr R_a
 =(I_{H_-^2}\otimes(I-\Pi_\sigma))\mathscr Q_a.
 }
\tag{L-91403.6}
\]

Orthogonal source-fibre decomposition gives, for all core inputs `f,g`,

\[
 \boxed{
 \langle\mathscr Q_af,\mathscr Q_ag\rangle
 =\langle H_{m_a}f,H_{m_a}g\rangle
  +\langle\mathscr R_af,\mathscr R_ag\rangle.
 }
\tag{L-91403.7}
\]

Equivalently,

\[
 \boxed{
 \mathscr Q_a^*\mathscr Q_a
 =H_{m_a}^*H_{m_a}
  +\mathscr R_a^*\mathscr R_a.
 }
\tag{L-91403.8}
\]

No signed metric appears. The minus sign of the quasi-Lévy completion is stored
in the score vector, while both source fibres carry positive norm.

## 4. Suzuki model-space reserve

After the canonical completed unitary conjugation of
`L-91301/L-91316`,

\[
 \boxed{
 \mathcal J_a^*\mathcal J_a
 =2H_{m_a}^*H_{m_a}.
 }
\tag{L-91403.9}
\]

Define

\[
 \boxed{
 \mathcal C_a^{\rm QL}
 =2\mathscr Q_a^*\mathscr Q_a.
 }
\tag{L-91403.10}
\]

Then

\[
 \boxed{
 \mathcal C_a^{\rm QL}
 =\mathcal J_a^*\mathcal J_a
  +2\mathscr R_a^*\mathscr R_a
 \succeq\mathcal J_a^*\mathcal J_a.
 }
\tag{L-91403.11}
\]

This is an exact source-ordered positive domination of the completed
model-space shape.

## 5. Literal prime one-particle and Fock subspaces

Let

\[
 d\mathsf N_\sigma(x)
 =\sum_{p,r}\frac{p^{-r\sigma}}r
  \delta_{r\log p}(dx).
\]

The atomic channel satisfies

\[
 d\beta_a(x)=a x\,d\mathsf N_\sigma(x).
\tag{L-91403.12}
\]

Therefore

\[
 (\mathcal I_a^{\rm p}g)(x)=\sqrt{a x}\,g(x)
\]

is an isometry

\[
 \boxed{
 \mathcal I_a^{\rm p}:
 L^2(\beta_a)\hookrightarrow L^2(\mathsf N_\sigma)
 \subset\mathcal S_\sigma.
 }
\tag{L-91403.13}
\]

Its symmetric second quantization is the explicit Fock embedding

\[
 \boxed{
 \Gamma_s(\mathcal I_a^{\rm p}):
 \Gamma_s(L^2(\beta_a))
 \hookrightarrow
 \Gamma_s(\mathcal S_\sigma).
 }
\tag{L-91403.14}
\]

By `L-91036`, the completed source-linear tangent reads only the compensated
first-chaos image; higher prime chaos sectors are preserved as orthogonal
unused environment.

## 6. The prime visible block is the tail-Hankel operator

Every prime atom lies above `1/2`, so `G_t(x)=e^{itx}-e^{-itx}` on the atomic
channel. Its score observation is

\[
 \boxed{
 \chi_a^{\rm p}(t)
 =\int(e^{itx}-e^{-itx})d\beta_a(x).
 }
\tag{L-91403.15}
\]

After the standard Hardy reflection, the corresponding positive-frequency
block is exactly

\[
 (\mathsf H_{\beta_a}g)(t)
 =\int_{u>t}g(u-t)d\beta_a(u).
\tag{L-91403.16}
\]

At `a=4`, `L-91307` supplies its explicit `D_0,D_1,D_2` Julia reserve.

The remaining coordinates of `mathscr Q_a` are the explicit short-jump
archimedean channel, long-jump archimedean channel, and deterministic drift.
They form the gamma/pole/theta completion of the prime output.

## 7. Agreement with the moving-unitary completion

`L-91306` decomposes the same completed tangent through

\[
 \Theta_a=\Gamma_aZ_a
\]

and identifies the gamma/pole part as a skew moving-unitary connection. The two
readings are:

```text
quasi-Levy source:
  prime atoms + short/long archimedean jumps + drift;

moving-unitary boundary:
  ordinary-prime derivative + gamma/pole connection.
```

Their score observations agree because both equal `m_a`. The quasi-Lévy
construction supplies one positive source fibre containing all channels before
observation.

## 8. Positive delays and two orientations

For `g in K_(Theta_a)`, use the compressed delay colligation of `L-91401`:

\[
 S_\tau g=T_\tau g+M_{\Theta_a}R_\tau g.
\tag{L-91403.17}
\]

The delayed source output is

\[
 \boxed{
 g\longmapsto
 \left(\mathscr Q_aT_\tau g,R_\tau g\right).
 }
\tag{L-91403.18}
\]

The source-fibre Pythagorean identity and the mixed-delay identity of `L-91401`
retain every carrier/delay cross term. The leakage cocycle makes repeated
delays compatible. Reflection gives the second Hardy orientation.

## 9. Bridge coordinate

Write the bridge as

\[
 \widehat b_a=H_a^+-H_a^-.
\]

Project each Hardy piece into its resident model space and Julia leakage as in
`L-91401`. Whenever the resulting source form is finite on the closed core, the
resident bridge vectors are valid inputs to `mathscr Q_a`. Thus the bridge has
an explicit geometric place in the colligation:

```text
resident plus/minus model-space components
 + delay leakage
 + quasi-Levy source auxiliary.
```

Its coefficient-one identification with the zeta screw bridge entry remains
open.

## 10. Completed embedding and remaining defect

The requested component is now explicit in one source-ordered positive Hilbert
geometry:

\[
 \boxed{
 \Gamma_s(L^2(\beta_a))
 \hookrightarrow
 \Gamma_s(\mathcal S_\sigma)
 \longrightarrow
 \text{completed two-sided delayed Hardy tangent}
 \oplus\text{positive reserve}.
 }
\tag{L-91403.19}
\]

The conclusion-producing arrow factors through the first-chaos image. It does
not assert that the completed probability law is Poisson infinitely divisible.

The constructed source-minus-shape auxiliary is

\[
 \mathcal D_a^{\rm QL}=2\mathscr R_a^*\mathscr R_a,
\]

augmented by the explicit delay/orientation/bridge leakages. The sole remaining
RH-bearing identity is

\[
 \boxed{
 \mathcal D_a^{\rm QL,del,bridge}
 =\mathbb K_a^{\rm del}
 }
\tag{L-91403.20}
\]

in the exact Guinand--Weil/Suzuki normalization.

## 11. Exact boundary

```text
prime one-particle embedding I_a^p                    EXACT
full symmetric-Fock embedding Gamma_s(I_a^p)          EXACT
prime-inclusive completed positive source fibre       EXACT
complete tangent as score observation                 EXACT
vector Hardy Hankel colligation                       EXACT
positive source auxiliary                             EXACT
ordinary-prime tail-Hankel visible block              EXACT
gamma/pole/theta completion channels                  EXPLICIT
compressed delays and two orientations                EXACT
bridge geometric placement                            EXACT
positive reserve = delayed screw/Weil defect          OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVED
```
