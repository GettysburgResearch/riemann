# L-91403 — The prime-inclusive quasi-Lévy source has an explicit completed Hardy colligation

Claim ID: `L-91403`  
Status: **PROVED EXACT PRIME-INCLUSIVE COMPLETED TANGENT COLLIGATION; SCREW-DEFECT IDENTIFICATION OPEN**  
Created: 2026-08-12  
Depends on: `L-91301`, `L-91306`, `L-91307`, `L-91316`, `L-91401`, `L-91402`  
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
 e_\sigma=\frac{(1,x,-x)}{N_\sigma}
\]

be its normalized radial score, and let

\[
 c_\sigma(v)=\langle v,e_\sigma\rangle
\]

be the norm-one score observation.

The explicit source-valued symbol

\[
 \mathbf q_a(t)
 =aN_\sigma\Theta_a(t)
  \left(-2it\lambda_\sigma',G_t,G_t\right)
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

Its positive atomic source summand is exactly the ordinary-prime Poisson score
of `L-91307`.

## 2. Vector-valued Hardy Hankel operator

Let `P_+` and `P_-` be the standard two Hardy projections. Define on the common
rational/exponential core

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
(L-91403.2) gives

\[
 \boxed{
 H_{m_a}
 =(I_{H_-^2}\otimes c_\sigma)\mathscr Q_a.
 }
\tag{L-91403.5}
\]

Thus Suzuki's complete tangent Hankel is an explicit contraction of the
prime-inclusive positive source Hankel.

All identities are initially quadratic-form identities on the common core and
extend to the corresponding closures whenever finite.

## 3. Exact positive auxiliary

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

Orthogonal source-fibre decomposition yields, for all core inputs `f,g`,

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

No signed metric appears: the minus sign of the quasi-Lévy measure is carried
by the score vector, while both source fibres have positive norm.

## 4. Suzuki model-space reserve

By `L-91301/L-91316`, after the canonical completed unitary conjugation,

\[
 \boxed{
 \mathcal J_a^*\mathcal J_a
 =2H_{m_a}^*H_{m_a}.
 }
\tag{L-91403.9}
\]

Define the explicit quasi-Lévy completed source form

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
model-space shape. Unlike the earlier Fisher-only factorization, its source
contains the actual ordinary-prime Poisson first chaos as an orthogonal direct
summand.

## 5. Identification of the prime visible block

The positive atomic channel in `nu_sigma^+` is

\[
 dN_\sigma(x)
 =\sum_{p,r}\frac{p^{-r\sigma}}r
  \delta_{r\log p}(dx).
\]

The radial score multiplies it by `a x`, giving exactly

\[
 a x\,dN_\sigma=d\beta_a.
\tag{L-91403.12}
\]

Since every prime atom lies above `1/2`, `G_t(x)=e^{itx}-e^{-itx}` on the
atomic channel. Hence its scalar score observation is

\[
 \chi_a^{\rm p}(t)
 =\int(e^{itx}-e^{-itx})d\beta_a(x).
\tag{L-91403.13}
\]

After the standard Hardy reflection, this channel is exactly the tail-Hankel
operator

\[
 \mathsf H_{\beta_a}
\]

of `L-91307`. At `a=4` it has the explicit `D_0,D_1,D_2` Julia reserve.

The remaining source coordinates in `mathscr Q_a` are the explicit short-jump
archimedean channel, long-jump archimedean channel, and deterministic drift.
They constitute the gamma/pole/theta completion of the prime output.

## 6. Relation to the moving-unitary completion

`L-91306` decomposes the same completed tangent using

\[
 \Theta_a=\Gamma_aZ_a
\]

and identifies the gamma/pole part as a skew moving-unitary connection.

The quasi-Lévy source decomposition and the moving-unitary decomposition are
two exact readings of the same scalar multiplier `m_a`:

```text
quasi-Levy reading:
  prime atoms + two archimedean jump channels + drift;

moving-unitary reading:
  ordinary-prime derivative + gamma/pole connection.
```

Their scalar observations agree by (L-91403.2). The quasi-Lévy construction
supplies the previously missing single positive source fibre containing all
channels before observation.

## 7. Positive delays and two orientations

For `g in K_(Theta_a)`, use the compressed delay colligation of `L-91401`:

\[
 S_\tau g=T_\tau g+M_{\Theta_a}R_\tau g.
\tag{L-91403.14}
\]

The delayed source output is represented by

\[
 \boxed{
 g\longmapsto
 \left(
  \mathscr Q_aT_\tau g,
  R_\tau g
 \right).
 }
\tag{L-91403.15}
\]

For arbitrary finite mixed-delay packets, the source-fibre Pythagorean identity
(L-91403.7) and the delay identity of `L-91401` retain every cross term.  The
leakage cocycle makes repeated delays compatible.

Reflection gives the second Hardy orientation, and direct sum gives the
completed two-sided delayed colligation.

## 8. Bridge coordinate

Write the two Hardy pieces of the bridge as

\[
 \widehat b_a=H_a^+-H_a^-.
\]

Project each piece into its resident model space and Julia leakage as in
`L-91401`. The resident bridge vectors are valid inputs to `mathscr Q_a` on the
closed core whenever their source form is finite. Thus the bridge has an
explicit place in the completed colligation:

```text
resident plus/minus model-space components
 + delay leakage
 + quasi-Levy source auxiliary.
```

What is not proved is that the resulting positive bridge/source defect equals
the bridge entry of the zeta screw/Weil Gram.

## 9. What this completes

The following requested component is now explicit in one source-ordered
positive Hilbert geometry:

\[
 \boxed{
 \text{ordinary-prime Poisson first chaos}
 \hookrightarrow
 \text{completed two-sided delayed Hardy tangent}
 \oplus
 \text{explicit positive quasi-Levy/Julia auxiliary}.
 }
\tag{L-91403.16}
\]

The embedding does not identify the completed probability law with a Poisson
law. It embeds the prime Poisson first chaos as a direct summand of the positive
Jordan decomposition of the completed quasi-Lévy tangent source.

## 10. Exact remaining defect identity

The constructed positive source-minus-shape auxiliary is

\[
 \boxed{
 \mathcal D_a^{\rm QL}
 =2\mathscr R_a^*\mathscr R_a
 }
\tag{L-91403.17}
\]

plus the explicit compressed-delay leakage and the finite bridge leakage when
those coordinates are adjoined.

The remaining RH-bearing theorem is the coefficient-one identity

\[
 \boxed{
 \mathcal D_a^{\rm QL,del,bridge}
 =\mathbb K_a^{\rm del},
 }
\tag{L-91403.18}
\]

in the exact Guinand--Weil/Suzuki normalization.

A generic positive auxiliary cannot be renamed the screw defect. The equality
must be proved on all finite carrier/delay/orientation/bridge packets.

## 11. Exact boundary

```text
prime-inclusive completed positive source fibre       EXACT
complete tangent as score observation                 EXACT
vector Hardy Hankel colligation                       EXACT
positive source auxiliary                             EXACT
ordinary-prime tail-Hankel as direct source summand   EXACT
gamma/pole/theta completion channels                  EXPLICIT
compressed delays and two orientations                EXACT
bridge geometric placement                            EXACT
quasi-Levy auxiliary = delayed screw/Weil defect      OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVED
```
