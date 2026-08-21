# L-19851 — The full residual preserves the signed low-index gap; only the target projection needs approximation

Claim ID: `L-19851`  
Status: **PROVED FINITE-DIMENSIONAL QUOTIENT THEOREM**  
Authoring agent: `gpt56-pro-09-q`  
Created: 2026-08-07  
Dependencies: finite min--max; exact residual identity `L-19832`; quotient-energy theorem `L-19846`  
Scope: adversarial correction to the review's proposed operator-norm projection gate

## 1. Setup

Let `(U,G)` and `(V,H)` be finite-dimensional Hilbert spaces and let

\[
 S:U\to V
\]

be surjective. Let

\[
 D_t\succeq0,\qquad D_q\succeq0,
\]

be respectively the omitted-support and finite-projection ordinary Grams. Put

\[
 \boxed{D_e=D_t+D_q.}
\]

This is the exact ordinary Gram of the complete residual

\[
 e=t+q,
\]

because `t` and `q` have disjoint physical support.

Define the quotient energy

\[
 \overline D_e(v)
 :=\min_{Su=v}\langle u,D_eu\rangle.
\]

Assume an upper map bound

\[
 S^*HS\preceq K G.
\tag{L-19851.1}
\]

## 2. Complete gap is monotone under projection residual

Assume

\[
 \dim\mathbf1_{[0,bd_6)}
 \bigl(G^{-1/2}D_tG^{-1/2}\bigr)\le1.
\tag{L-19851.2}
\]

Since `D_q>=0`,

\[
 D_e\succeq D_t.
\]

Therefore

\[
 \boxed{
 \dim\mathbf1_{[0,bd_6)}
 \bigl(G^{-1/2}D_eG^{-1/2}\bigr)\le1.}
\tag{L-19851.3}
\]

In particular, the finite projection residual cannot create a second low source direction. It can only raise source residual energy.

## 3. Exact quotient lower bound

Let `W` be any two-dimensional subspace of `V`, and let `\widetilde W` be its two-dimensional space of `D_e`-minimal lifts. Let `E_<` be the source spectral subspace below `bd_6`; by (L-19851.3), `dim E_<=1`.

There is a nonzero

\[
 u\in\widetilde W\cap E_<^{\perp_G}.
\]

Hence

\[
 \langle u,D_eu\rangle\ge bd_6\|u\|_G^2.
\]

Using (L-19851.1),

\[
 \|Su\|_H^2\le K\|u\|_G^2,
\]

and therefore

\[
 \frac{\overline D_e(Su)}{\|Su\|_H^2}
 \ge\frac bK d_6.
\]

Every two-dimensional subspace of `V` contains such a vector. The Courant--Fischer characterization gives

\[
 \boxed{
 \theta_2(\overline D_e,H)
 \ge\frac bK d_6.}
\tag{L-19851.4}
\]

No factor `1/2` is needed.

## 4. Only the target line needs a projection estimate

Let `u_*` be a source target satisfying

\[
 \langle u_*,D_tu_*\rangle
 \le a d_4\|u_*\|_G^2,
\tag{L-19851.5}
\]

\[
 \langle u_*,D_qu_*\rangle
 \le c d_4\|u_*\|_G^2,
\tag{L-19851.6}
\]

and

\[
 \|Su_*\|_H^2\ge k\|u_*\|_G^2.
\tag{L-19851.7}
\]

For `v_*=Su_*`, the minimizing definition yields

\[
 \overline D_e(v_*)
 \le(a+c)d_4\|u_*\|_G^2,
\]

so

\[
 \boxed{
 \frac{\overline D_e(v_*)}{\|v_*\|_H^2}
 \le\frac{a+c}{k}d_4.}
\tag{L-19851.8}
\]

Combining (L-19851.4) and (L-19851.8),

\[
 \boxed{
 \frac{R_{\overline D_e}(v_*)}
      {\theta_2(\overline D_e,H)}
 \le
 \frac{K(a+c)}{bk}\frac{d_4}{d_6}.}
\tag{L-19851.9}
\]

Thus the signed `d_4/d_6` separation survives the complete residual whenever the projection error is small on the one target lift. No operator inequality

\[
 D_q=o(D_t)
\]

on the whole source packet is required.

## 5. Non-effective target cutoff exists at every level

Fix one support and one target localized vector `g_*`. Ordinary Fourier projections satisfy

\[
 \|(I-P_N)g_*\|_2\to0.
\]

Since `d_4(R)>0` at every finite support, for any prescribed `c_R>0` there exists a finite cutoff `N_R` such that

\[
 \boxed{
 \|(I-P_{N_R})g_*\|_2^2
 \le c_Rd_4(R)\|u_*\|_G^2.}
\tag{L-19851.10}
\]

This selection may be astronomically large and non-effective. It is nevertheless a valid mathematical diagonal choice. An effective proof would need a quantitative cutoff; the existence theorem does not.

## 6. What the review correctly identified

The finite zero-side form is still

\[
 Z(t+q,t+q),
\]

not `Z(t,t)`. The theorem above does not restore the rejected congruence in `T-19810.18`.

It proves a narrower but important correction:

```text
projection residual is not a new complement-gap obstruction;
its only low-index cost is the target-line residual and the zero-side
scalarization of the complete residual.
```

The remaining finite theorem is therefore a relative local-Weyl estimate for `e=t+q`, not the much stronger ordinary-Gram comparison `D_q=o(D_t)` on every direction.

## 7. Proof boundary

- Sections 2--5 are exact finite-dimensional or Hilbert-space projection facts.
- No zero-side sign is assigned to `Z(t,q)` or `Z(q,q)`.
- A finite RH proof still requires a local-Weyl/lower-envelope theorem for the complete residual, or a projection-free continuous-operator route.
- No RH conclusion is claimed here.
