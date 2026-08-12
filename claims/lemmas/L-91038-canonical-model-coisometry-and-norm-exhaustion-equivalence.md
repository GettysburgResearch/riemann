# L-91038 — The canonical model-space coisometry exists exactly when the hyperbolic port is absent

Claim ID: `L-91038`  
Status: **EXACT MODEL-SPACE COISOMETRY / EXHAUSTION THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: `L-91034`; standard half-plane model-space decomposition  
RH status: **unproved**

## 1. Setup

Work in the right half-plane

\[
 \mathbb H=\{z:\Re z>0\}.
\]

For an analytic inner function `F` put

\[
 K_F(z,w)=\frac{1-F(z)\overline{F(w)}}{z+\overline w}
\]

and write `mathscr K_F` for the corresponding model space.  Retain from
`L-91034`

\[
 \Theta_a(z)=\frac{\xi(1/2-a+z)}{\xi(1/2+a+z)},
\]

its crossed-pole Blaschke factor `B_a`, the deterministic stable inner factor

\[
 \Delta_a=b_a^2b_{2a}^2b_{4a}^2,
\]

and

\[
 A_a=B_a\Theta_a,
 \qquad
 I_a=\Delta_aA_a.
\]

The functions `A_a` and `I_a` are analytic inner.  The exact kernel identity is

\[
 \mathcal K_a^{\rm src}
 =\mathcal K_a^{\rm crit}
  +\mathcal K_a^{\rm st}
  +\mathcal K_a^{\rm hyp},
 \tag{L-91038.1}
\]

where

\[
 \begin{aligned}
 \mathcal K_a^{\rm src}
 &=\frac{K_{I_a}}
 {\Delta_aB_a\overline{\Delta_aB_a}},\\
 \mathcal K_a^{\rm crit}&=K_{\Theta_a},\\
 \mathcal K_a^{\rm st}
 &=\frac{K_{\Delta_a}}
 {\Delta_aB_a\overline{\Delta_aB_a}},\\
 \mathcal K_a^{\rm hyp}
 &=\frac{K_{B_a}}{B_a\overline{B_a}}.
 \end{aligned}
 \tag{L-91038.2}
\]

All scalar products in denominators are evaluated in the two variables, as in
`L-91034`.

## 2. Standard product-space unitary

For inner functions `F,G`,

\[
 \boxed{
 \mathscr K_{FG}=\mathscr K_F\oplus F\mathscr K_G.
 }
 \tag{L-91038.3}
\]

Indeed,

\[
 K_{FG}=K_F+F\overline F K_G,
\]

and the two summands are orthogonal because
`F mathscr K_G subset F H^2` while `mathscr K_F perpendicular F H^2`.

Equivalently, every `h in mathscr K_(FG)` has a unique decomposition

\[
 h=h_F+Fh_G,
 \qquad
 h_F\in\mathscr K_F,
 \quad h_G\in\mathscr K_G,
 \tag{L-91038.4}
\]

and

\[
 \|h\|^2=\|h_F\|^2+\|h_G\|^2.
 \tag{L-91038.5}
\]

## 3. Explicit coisometry when the zero port is absent

Assume

\[
 B_a\equiv1.
 \tag{L-91038.6}
\]

Then `Theta_a=A_a` is inner and

\[
 I_a=\Delta_a\Theta_a.
\]

Define the congruence spaces

\[
 \mathscr S_a
 =\{h/\Delta_a:h\in\mathscr K_{I_a}\},
 \qquad
 \|h/\Delta_a\|_{\mathscr S_a}=\|h\|_{\mathscr K_{I_a}},
 \tag{L-91038.7}
\]

and

\[
 \mathscr D_a
 =\{d/\Delta_a:d\in\mathscr K_{\Delta_a}\},
 \qquad
 \|d/\Delta_a\|_{\mathscr D_a}=\|d\|_{\mathscr K_{\Delta_a}}.
 \tag{L-91038.8}
\]

Their kernels are respectively `mathcal K_a^(src)` and
`mathcal K_a^(st)` with `B_a=1`.

By (L-91038.3), every `h in mathscr K_(I_a)` has the unique decomposition

\[
 h=d+\Delta_a c,
 \qquad
 d\in\mathscr K_{\Delta_a},
 \quad c\in\mathscr K_{\Theta_a}.
 \tag{L-91038.9}
\]

Define

\[
 \boxed{
 \mathcal C_a:\mathscr S_a
 \longrightarrow
 \mathscr K_{\Theta_a}\oplus\mathscr D_a,
 \qquad
 \mathcal C_a(h/\Delta_a)=(c,d/\Delta_a).
 }
 \tag{L-91038.10}
\]

Then `mathcal C_a` is unitary, hence in particular a coisometry.  Indeed,

\[
 \|h/\Delta_a\|_{\mathscr S_a}^2
 =\|c\|_{\mathscr K_{\Theta_a}}^2
  +\|d/\Delta_a\|_{\mathscr D_a}^2,
 \tag{L-91038.11}
\]

and every pair on the right is attained by `h=d+Delta_a c`.

For the reproducing kernels,

\[
 \boxed{
 \mathcal C_a k_w^{\rm src}
 =\bigl(k_w^{\rm crit},k_w^{\rm st}\bigr).
 }
 \tag{L-91038.12}
\]

Thus the critical and deterministic outputs consume the complete source norm:

\[
 \boxed{
 \mathcal K_a^{\rm src}
 =\mathcal K_a^{\rm crit}+\mathcal K_a^{\rm st}.
 }
 \tag{L-91038.13}
\]

No abstract square root is used; `(L-91038.10)` is the canonical model-space
coisometry.

## 4. Common filtering preserves exhaustion

Let `T` be any linear map defined on a common dense domain of the three spaces,
with values in Hilbert output spaces, and assume the filtered kernel vectors
are well defined.  Applying `T` in the first variable and `T*` in the second to
(L-91038.13) gives

\[
 \boxed{
 T\mathcal K_a^{\rm src}T^*
 =T\mathcal K_a^{\rm crit}T^*
  +T\mathcal K_a^{\rm st}T^*.
 }
 \tag{L-91038.14}
\]

On the closed span of the filtered kernel vectors, the map

\[
 Tk_w^{\rm src}
 \longmapsto
 \bigl(Tk_w^{\rm crit},Tk_w^{\rm st}\bigr)
 \tag{L-91038.15}
\]

extends isometrically.  This is the exact form in which a correctly constructed
Cauchy/Hardy filter may be attached.  The requirement that the same `T` act on
a common model-space domain is load bearing; it is not supplied by pointwise
multiplication alone.

## 5. Converse: norm exhaustion deletes the Blaschke port

Conversely, suppose that on a uniqueness set in `H` there is a Hilbert-space
coisometry carrying the source kernel vectors to the critical and stable
vectors and exhausting their norm.  Equivalently,

\[
 \mathcal K_a^{\rm src}
 =\mathcal K_a^{\rm crit}+\mathcal K_a^{\rm st}
 \tag{L-91038.16}
\]

on that set.  Analytic continuation extends the equality throughout the common
domain.  Subtracting (L-91038.16) from the exact identity (L-91038.1) gives

\[
 \boxed{\mathcal K_a^{\rm hyp}\equiv0.}
 \tag{L-91038.17}
\]

Since

\[
 \mathcal K_a^{\rm hyp}(z,z)
 =\frac{1-|B_a(z)|^2}
 {2\Re z\,|B_a(z)|^2},
 \tag{L-91038.18}
\]

away from its zeros, (L-91038.17) implies `|B_a(z)|=1` at every interior point.
By the maximum principle, `B_a` is a unimodular constant.  Hence there is no
crossed zero pole at depth greater than `a`.

Therefore

\[
 \boxed{
 \begin{aligned}
 &\text{canonical source-to-(critical+stable) norm exhaustion at scale }a\\
 &\qquad\Longleftrightarrow B_a\text{ is constant}\\
 &\qquad\Longleftrightarrow
 \xi(s)\ne0\text{ for }\Re s>\frac12+a,
 \end{aligned}
 }
 \tag{L-91038.19}
\]

with the usual harmless exclusion of the countable shift-cancellation scales,
removed by continuity or by requiring a dense set of scales.

In particular,

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \text{norm exhaustion holds for every }a>0.
 }
 \tag{L-91038.20}
\]

Any dense countable set of positive scales suffices.

## 6. Arithmetic source identification

Let `mathscr A_a` be any explicit arithmetic Stinespring space, with feature
vectors `Phi_a(z)`.  A source-ordering coisometry

\[
 J_a:\mathscr A_a\twoheadrightarrow\mathscr S_a,
 \qquad
 J_a\Phi_a(z)=k_z^{\rm src},
 \tag{L-91038.21}
\]

exists exactly when the corresponding kernel domination required by Douglas'
lemma holds.  It is norm preserving on the source feature span exactly when
its arithmetic kernel equals `mathcal K_a^(src)`.

If, in addition, the composite `mathcal C_a J_a` exhausts the *entire*
arithmetic norm using only the critical and stable outputs, then `J_a` has no
unused source kernel and (L-91038.16) holds.  Hence (L-91038.19) applies.

Thus the requested arithmetic coisometry has two logically separate joints:

```text
arithmetic source identification:
    explicit arithmetic Gram -> pole-removed model-space source Gram;

model-space norm exhaustion:
    source Gram -> critical Gram + deterministic stable Gram.
```

The second joint is solved explicitly by `(L-91038.10)` under zero-port
absence, and is equivalent to zero-port absence in the converse direction.
The first joint is the completed tangent/source-ordering theorem isolated on
PR #400; Suzuki's Hankel transform closes only its zeroth-order amplitude
version.

## 7. Exact boundary

```text
model-space coisometry under B_a=1                    EXPLICIT / EXACT
critical+stable norm exhaustion under B_a=1           EXACT
norm exhaustion -> B_a constant                       EXACT
all-scale model exhaustion <=> RH                     EXACT
safe arithmetic Hankel source = model source          OPEN
completed first-chaos tangent identification           OPEN / RH-BEARING
unconditional norm exhaustion                          UNPROVED
Riemann Hypothesis                                     UNPROVED
```
