# Balanced unitary coefficients: product moments, continuation, and descent

Date: 20 October 2026. Status: proposed source-dependent analytic extension, submitted for independent review.

This addendum permits fixed radial parameters at infinity in the product-moment adapter and final comparison. It leaves the frozen pure-angular files unchanged. Its M2 argument depends on `ANGULAR_PRODUCT_MOMENT.md` and the explicitly identified estimates of Baiying Liu, [arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835v1). The subsequent zero-free conclusion additionally requires `BALANCED_UNITARY_INVERSE_ADDENDUM.md`, which supplies the changed theta reflection and preliminary inverse bound. The source PDF has SHA-256 `5d0fd10274c8444c789b0b7925a1cd3419017fe760be3219b6be51d7fbed9bd5`.

## 1. Canonical normalization and the two families

First let \(F\supseteq\mu_{12}\), and put \(r_F=[F:\mathbb Q]/2\). Use the squared complex absolute value \(|z|_v=|z|^2\). For an actual unitary Hecke character \(\Omega\), use the same ideal/local convention as the inverse note:

\[
 L_{\Omega,S}=\prod_{v\in S}\Omega_v^{-1},\qquad
 L_{\Omega,S}(z_v)
 =(z_v/|z_v|)^{a_v}|z_v|_v^{i\gamma_v},
 \quad a_v\in\mathbb Z,\ \gamma_v\in\mathbb R.
 \tag{1.1}
\]

Thus the idelic local component has the opposite angular and radial signs. Define the ideal norm character by

\[
 \omega_t(\mathfrak a)=(N\mathfrak a)^{it},
 \qquad L(s,\chi\omega_t)=L(s-it,\chi).
\]

Its local weight is \(|z|_v^{it}\). If \(\bar\gamma=r_F^{-1}\sum_v\gamma_v\), replacing \(\Omega\) by \(\Omega\omega_{-\bar\gamma}\) leaves the real parts of its zeros unchanged and makes

\[
 \sum_{v\mid\infty}\gamma_v=0.
 \tag{1.2}
\]

We impose (1.2) from now on and call the character balanced. This is a normalization of an actual global character, not a claim that arbitrary tuples in (1.1) are realizable. All local parameters are fixed before the scale varies.

Fix a finite group \(\Theta_0\) supported in the final fixed \(S\), and set

\[
 \mathcal C_{\Omega,S}=\{\Omega^j\theta:j\in\mathbb Z,\theta\in\Theta_0\},
 \qquad
 \mathcal A_\Omega(F)=\{\Omega^j\xi:j\in\mathbb Z,\xi\text{ finite order of arbitrary conductor}\}.
 \tag{1.3}
\]

Let \(\beta_\Omega(F)\) be the nontrivial-zero supremum of the second family. The first group specifies the fixed prime-coefficient span and exceptional rows. It does not supply the global zero-free premise.

If \((a,\gamma)\ne0\), the map \(h\mapsto(ha,h\gamma)\) is injective. For any fixed finite initial list of exponents, the only realized whole coefficients are its conjugation and finite unit-twist orbit. Consequently the exceptional inducing characters actually encountered lie in a finite list \(\Omega^{\pm h}\Theta_0\), even though \(\mathcal C_{\Omega,S}\) is infinite. If \((a,\gamma)=0\), \(\Omega\) has finite order and the original finite-group argument applies.

## 2. No new poles in fixed-character means

A unitary Hecke function can have a pole only when its character is a pure global norm character \(\omega_t\); that pole is at \(1+it\). If a member \(\Omega^h\theta\) of a realized fixed list has this form, its local data satisfy

\[
 ha=0,\qquad h\gamma_v=t\quad\text{for every }v.
\]

Summing the second equations and using (1.2) gives \(t=0\). Thus only the actual principal character can have a pole, and its pole is at one. This is why a common norm twist is removed before the moment proof.

The fixed-character mean from Section 3 of `ANGULAR_PRODUCT_MOMENT.md` therefore remains

\[
 \sum_l\vartheta(l)1_{(l,R_*)=1}(Nl)^{it}W(Nl/T)
 =c_{\vartheta,R_*}T^{1+it}I_W(t)
  +O\bigl(Z^\varepsilon(1+|t|)^A p_A(W)\bigr),
 \tag{2.1}
\]

where \(c_{\vartheta,R_*}=0\) except for the principal character. Indeed the deleted Euler factors still have the subpower bound on every fixed positive strip. The fixed Hecke functions have polynomial vertical growth there, now with fixed radial gamma shifts. Mellin inversion crosses only the same possible pole at \(1+it\). The complete common coprimality indicator, the common norm mode, and both rectangle tests are unchanged. Equal-product main terms therefore cancel exactly, with the same saving from the smallest original scale. Balanced nontrivial radial characters have zero main term, just as the nontrivial angular characters do.

## 3. Ordinary reflection: signs, poles, and exponential factors

For the primitive moving character of type \((ha,h\gamma)\), write \(b_v=|ha_v|/2\) and \(\rho_v=h\gamma_v\). Its completed gamma factors, in convention (1.1), are proportional to

\[
 \prod_v\Gamma(s+b_v-i\rho_v).
 \tag{3.1}
\]

After the functional equation and Mellin substitution \(s\mapsto1-s\), the reflected profile is

\[
 \widehat W^{\sharp,h}(s)
 =\widehat W(1-s)
   \prod_v\frac{\Gamma(s+b_v+i\rho_v)}
                    {\Gamma(1-s+b_v-i\rho_v)}.
 \tag{3.2}
\]

The powers of \(2\pi\) give the original positive conductor scale and fixed unit phases. No power of the varying row conductor is added. The same exact natural-zero Euler restoration and conductor-times-redundant-radical bound apply.

At \(s=\sigma+iT\), the two gamma arguments in each quotient have imaginary parts \(T+\rho_v\) and \(-T-\rho_v\). Their Stirling exponential factors cancel **exactly**. The quotient has polynomial exponent \(2\sigma-1\) at large \(|T+\rho_v|\), independent of the fixed shifts. On the remaining bounded height intervals, fixed contour bounds apply. Constants can depend on the finite list of shifts; no exponential loss in \(T\) or power of the scale is introduced.

The only numerator poles are

\[
 s=-b_v-n-i\rho_v,\qquad n=0,1,2,\ldots .
 \tag{3.3}
\]

Reciprocal gamma factors introduce no poles. Poles on \(\operatorname{Re}s=0\) occur only when \(b_v=0,n=0\). Their small-argument residues are finite sums of

\[
 x^{i\rho}P_\rho(\log x),
 \qquad \deg P_\rho\le r_F-1.
\]

The oscillations have modulus one. Shifting a small fixed distance left, avoiding the remaining pole lines, gives precisely the previous bound
\(W^{\sharp,h}(x)\ll(1+|\log x|)^{r_F-1}\) for \(0<x\le1\). Negative-real-part poles give positive powers of \(x\). Right-line shifts give rapid decay at infinity. The same estimates hold for every required Euler derivative, with fixed constants.

The lower dyadic central masses are therefore still summable. The original row-Hilbert-space scale supremum, its two-variable mixed derivative, and conjugation inside each absolute factor work unchanged. Incoming *common* norm modes are absorbed into test profiles before reflection; the intrinsic balanced vector \(h\gamma\) is not discarded by that operation.

## 4. Prime bounds and the product theorem

For a row outside \(\mathcal C_{\Omega,S}\), multiplication by a fixed prime-basis character in that group cannot produce the principal character. It cannot produce another pure global norm character either: the product still has balanced radial vector. It belongs to the global family \(\mathcal A_\Omega(F)\), with one of finitely many fixed full infinity types.

Under \(\beta_\Omega(F)\le(1+\kappa)/2\), the logarithm and logarithmic-derivative argument on the buffered zero-free disks thus has no extra pole. Convexity is uniform in the moving finite conductor because the fixed radial shifts merely replace height factors by \(1+|T-\rho_v|+b_v\), bounded by a fixed polynomial in \(1+|T|\). The source prime bound remains \(|Q_k|^2\ll Z^{\kappa z+\varepsilon}\). For \(\kappa=1\), use absolute counting as before.

All row Poisson characters remain finite Kummer characters. The fixed coefficient is unitary and multiplicative on the whole column product. The two transforms, common-factor allocations, and finite unit twists neither change \(h\) nor create new radial parameters beyond whole-side conjugation. Every member of the fixed exception group is unramified outside \(S\), so the prescribed valuation count and new-exception divisibility by fourth powers remain valid. Equation (2.1) centers the resulting finite exceptional list at the original scales.

Consequently the full theorem of `ANGULAR_PRODUCT_MOMENT.md` holds for a balanced \(\Omega\):

\[
 \sum_{Nk\ll Z^m}|S_k(n_1)S_k(n_2)Q_k|^2\ll Z^{M+\varepsilon},
 \qquad M=m+q,
 \tag{4.1}
\]

with the same retained moving radicals, zero masks and full prime annuli. For \(z=0\), exclude only principal inducing rows and allow the same arbitrary bounded ordinary lengths. For \(z>0\), exclude \(\mathcal C_{\Omega,S}\), retain the finite conjugation-closed prime basis and mesh, and require
\(n_1+n_2+6\kappa z\le M\), \(13/18\le\kappa\le1\), with the preceding global zero-free premise when \(\kappa<1\). The unchanged normalized induction proves (4.1). Uniformity in moving finite conductors is retained; uniformity in growing initial radial parameters is not asserted.

## 5. The final comparison has the same inputs

Let \(\lambda_v=\pm1\) be the source Eisenstein vector in convention (1.1). Suppose

\[
 (a,\gamma)\notin\{(\lambda,0),(-\lambda,0)\}.
 \tag{5.1}
\]

The companion balanced inverse addendum proves the theta reflection, both inverse moments, and the preliminary \(11/12\) bound for every \(\Omega^h\xi\). The nonresonance required there holds for every power: if \(h\gamma\ne0\), the balanced radial weight removes the constant term; otherwise an equality \(ha=\pm\lambda\) forces \(h=\pm1\) and contradicts (5.1).

Here are the remaining changes to Sections 13--14 of the source. Lemma 13.1 uses the same nonprincipal entire Hecke functions and (3.1), so its Mellin shifts and common-divisor loss are unchanged. Its constants and height orders may depend on the finite radial list. The compensated theta average receives the new radial profiles from the inverse addendum; their permitted strip and vertical power remain the source ones. Finite-place coefficients, exterior norm counts and separated angular/radial phases are unchanged. The principal local estimates and the identity-ray normalizer use unitary phases; no radial target factor is added to that normalizer.

The detector's finite presentation list and fixed inverse prime coefficients belong to (1.3). All its buffered reciprocal and prime bounds use \(\beta_\Omega(F)\). There are no new pure-norm inducing poles by Section 2. The reflected numerator remains the finite-order \(L_F(w,\chi_u)\); its approximate functional equation is unchanged. Its amplified average uses (4.1), and a nonunit sixth-power-free numerator row still has exterior ramification, hence lies outside \(\mathcal C_{\Omega,S}\).

Thus the source comparison and the argument in `ANGULAR_BOOTSTRAP.md` give, under the identified upstream inputs and the companion inverse proof,

\[
 \boxed{L_F(s,\Omega^h\xi)\ne0
 \quad\text{for }\operatorname{Re}s>B_\flat,
 \qquad B_\flat=0.874886647039964\ldots .}
 \tag{5.2}
\]

The noncircular order is \(11/12\to7/8\to B_\infty\to B_\flat\). Each preceding bound is for the full global family. Numerical comparison gaps are fixed before the target-dependent height orders and thresholds, so unbounded radial parameters across the family require no uniform constants. Common norm twists translate the imaginary variable afterwards. The two excluded balanced types receive no conclusion from this argument by taking a limit of radial parameters.

## 6. Base change and fields with real places

For an arbitrary number field \(K\), write the local weights at real places as \(\operatorname{sgn}(x)^{e_v}|x|^{i\gamma_v}\), and at complex places as in (1.1). Put \(d_v=[K_v:\mathbb R]\), and define

\[
 \gamma_K=\frac{\sum_{v\mid\infty}d_v\gamma_v}{[K:\mathbb Q]}.
 \tag{6.1}
\]

This canonical common norm twist commutes with base change to \(F=K(\zeta_{12})\). To verify it, let \(n=[F:K]\). Each real place has \(n/2\) complex places above it, and each complex place has \(n\). At a real place, \(N_{\mathbb C/\mathbb R}z=|z|^2=|z|_v\), so its radial coefficient is copied unchanged and its sign disappears. Complex local base change also copies the radial coefficient unchanged. Hence the average of the resulting \(r_F\) radial parameters is exactly (6.1). Norm characters commute with norm pullback on ideals because absolute ideal norms compose.

Let \(E=\mathbb Q(\sqrt{-3})\). If \(E\not\subset K\), the balanced pulled-back character is invariant under \(\operatorname{Gal}(F/K)\), while some automorphism of that group sends the Eisenstein angular vector to its negative. It therefore cannot have either exceptional type \((\pm\lambda,0)\). In particular, above any real place its angular degree is zero, which itself prevents equality with the everywhere degree-one Eisenstein vector.

If the balanced type is nonzero, the abelian identity

\[
 L_F(s,\eta\circ N_{F/K})
 =\prod_{\tau\in\widehat{\operatorname{Gal}(F/K)}}L_K(s,\eta\tau)
 \tag{6.2}
\]

has entire factors: none is a pure global norm character. Their positive exponents prevent cancellation of a zero by a pole. If the balanced type is zero, the character is finite order times a common norm twist and the finite-order theorem applies by translation. The full local-factor identity and finite Euler omissions have the same justification as `FAMILY_DESCENT.md`.

We therefore obtain the proposed consequence:

- Over every \(K\) not containing \(E\), **every unitary Hecke character** has no zeros in \(\operatorname{Re}s>B_\flat\), with its possible translated principal pole permitted. This includes all fields having a real place.
- Over \(K\supset E\), the same statement holds except for the characters of the form \(\Lambda_K\xi\omega_t\) or \(\overline\Lambda_K\xi\omega_t\), where \(\xi\) is finite order and \(t\in\mathbb R\). These are exactly the two resonant balanced infinity types; their treatment remains outside this proof.

The second assertion follows because base change repeats the complex angular types and preserves (6.1). A quotient with trivial balanced infinity type factors through a finite ray class group. These are source-dependent consequences of (5.2), not a smaller numerical boundary for the finite-order family or a claim of uniform bounds as the fixed infinity parameters grow.
