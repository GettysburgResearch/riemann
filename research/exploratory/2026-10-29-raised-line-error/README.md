# Complete slot-error bound on Hu's raised numerator line

**Status:** Proposed source-conditional theorem and proof, not a zero-free theorem. Its content is the local-product and error-slot interface needed to transplant the Xu–Sang amplified numerator to Hu's unitary target. The source local table and Kummer identification are explicit inputs, not reproved here.

**Sources:** Hu, [unitary Weil preprint](https://hexagonmath.org/2610.00216v1), (6.10)–(6.13) and Proposition 3.1; OpenAI's [quasi-RH preprint](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf), Lemma 7.1, with the crucial `V^(1_(j<=1))` in (7.11); Xu–Sang, [arXiv:2610.15291v2](https://arxiv.org/abs/2610.15291v2), Lemma 6.2 and Appendix C.2. The argument below supplies the global product and finite error-slot aggregation from those inputs, including a unitary but potentially infinite-order target.

## Theorem from the stated inputs

Fix `K` containing `mu_12`, a unitary Hecke target `psi`, a finite bad set `S`, and a fixed finite collection of disjoint good-prime windows with positive scales `P_i=Z^ell_i`. Let `u` be a nonprincipal sixth-power-free physical row coprime to `S`, `U~Nu`, and let `chi_u^*` be the primitive finite-order inducing numerator. Assume the source local formulas, their stated unit-modulus phases, and Hu's Kummer identification of `chi_u`. Fix `e>0` and a point on a raised contour with

    51/100<=a<=7/8, Re(s)>=a+16e,
    Re(z)=z0=17/50, Re(w)=1/2-vartheta,
    0<=vartheta<=min(1/10,a-1/2).

For any fixed set `I` of error slots in the full finite main/error expansion, let `E_i(u)` be the selected local error in slot `i`, after the common `Q^(z-1)` factor, and let `H_u=product_(p notin S) H_p` be the full unselected Euler product, including the primes occurring in the selected windows. At each chosen prime use the normalized local quotient `B_p=G_p/H_p`, so the identity is `product_(p not selected) H_p product_(p selected) G_p = H_u product_(p selected) B_p`. The disjoint slot supports guarantee that each selected prime occurs once. Then, after enlarging the fixed prime cutoff in `S` depending on `e`, for every `epsilon>0`,

    |H_u| |L_K^S(w,chi_u)| product_(i in I) |E_i(u)|
       <<_(K,S,e,I,epsilon) U^(vartheta+epsilon) (1+|Im w|)^A
          |L_K(1-w,conjugate(chi_u^*))|
          product_(i in I) P_i^(z0-1/2).

Here `A` is finite and fixed for the field and contour range. Constants may depend on the fixed window functions and slot count. The row-dependent primitive root number and conductor phase are absent from the right side because their absolute values are one. For `I` empty, the estimate is the same functional-equation bound with the full correction. This theorem does not bound the reflected L-value on a row class, and does not justify a contour move.

## 1. The common correction product

At an unramified row prime the corrected source identity gives, with `sigma=Re(s)` and `w0=Re(w)`,

    |H_p-1| << Q^(-sigma-6z0) + Q^(-sigma-w0)
                + Q^(-w0-6z0) + Q^(4-6sigma-6z0)
                + Q^(1-sigma-w0-6z0).

These terms are bounded by `Q^(-1-c)` for some `c=c(e)>0`: use `sigma+w0>=1+16e`, `sigma>=51/100`, `w0>=2/5`, `6z0=51/25`. Thus the product over all good non-row primes and its reciprocal are uniformly bounded after the fixed cutoff.

At a row prime, `D=W=0` but the separate source `W_loc` is retained. In the source table, the common term involving `V^(1_(j<=1))` has size at most `Q^(-16e)` for `j>=2`, while the five remaining valuation-table terms have a uniform negative exponent (at most `-1/50` before the positive `e` savings). Thus `|H_p-1| << Q^(-c')` with `c'=min(16e,1/50)>0`, uniformly in phases. Increase the cutoff to make `|H_p-1|<=1/2`. For every `epsilon>0`, the finite product over `p|u` and its reciprocal are then `O_epsilon(U^epsilon)` by `sum_(p|u) log(1+C Q^(-c')) <= epsilon log U+O_epsilon(1)`. This proves `|H_u|<<U^epsilon` and avoids assuming a summable row-prime majorant.

## 2. Pointwise local error decomposition

For `p` not dividing `u`, the explicit cancellation checked in [the numerator interface](../2026-10-28-hu-numerator-interface/README.md) gives the selected local quotient as the main term `-conjugate(chi_u(p))` plus an error bounded by `O(Q^(-51/100))`. Summing a slot against `Q^(z-1)` by the fixed-field ideal count gives `O(P_i^(z0-51/100))`.

At `p|u`, apply the same table before dropping its zero extensions. For `j=v_p(u)`, all non-strict error terms, after extracting `Q^z`, have exponents at most `-51/100`. For `j>=2` there is in addition one term at exponent `-w0=-1/2+vartheta`: it comes from the common table term with `V^(1_(j<=1))=1`. There are at most `O(log U)` row-prime divisors. Therefore each slot error is pointwise bounded by

    |E_i(u)| << U^epsilon P_i^(z0-51/100)
       + sum_(p in slot i, p|u, v_p(u)>=2) C Q^(z0-1/2+vartheta).

The fixed prime cutoff controls the local denominators. This bound is to be applied after all selected local factors are expanded; it does not replace the physical main prime polynomials or their masks.

## 3. Use one conductor deficit for the whole strict tuple

Hu's Kummer identification and tame local class field theory give `N f_u <= C N rad(u)`: see [the sextic conductor lemma](../2026-10-29-sextic-conductor/README.md). The finite-order primitive functional equation on `Re(w)=1/2-vartheta` gives

    |L_K^S(w,chi_u)| << (N f_u)^vartheta (1+|Im w|)^A
                          |L_K(1-w,conjugate(chi_u^*))|,

with only bounded fixed-`S` Euler factors. Expand the product of the pointwise slot-error bounds. In each term, let `J` be the set of primes contributing the strict summands. The slots are disjoint, so these primes are distinct. The simultaneous ideal-divisibility identity implies

    (N f_u)^vartheta product_(p in J) Q^vartheta
       <= C^vartheta U^vartheta product_(p in J) Q^(-(v_p(u)-2)vartheta)
       <= C^vartheta U^vartheta.

Hence every strict prime contributes at most `Q^(z0-1/2)` after the single conductor factor is combined with the **whole** strict tuple. Every non-strict slot contributes at most `U^epsilon P_i^(z0-1/2)`. Summing the finite choices and at most `(log U)^|I|` strict tuples gives the theorem. No conductor saving is counted twice.

## Boundaries and review gates

- The Kummer identification and full ramified local table are source inputs. In particular, `W_loc` must not be replaced by the zero-extended `W`; an error in the field/sector transfer invalidates the theorem.
- The theorem concerns the fixed raised line and absolute values after the finite main/error expansion. The full holomorphic correction, horizontal joins, buffered reciprocal of the genuinely unitary denominator, and all-height majorants must be established separately before moving the original contour.
- Applying the moment requires the **same** physical main-slot polynomials and row class, the allowed finite-character coefficients, common masks, a fixed mesh, and the fixed-field AFE. This theorem supplies no row-count or averaged numerator bound by itself.
- The implied constants may depend on fixed window and slot data but all exponent savings and cutoffs must be chosen in the source's stated order before the late height parameter.

**What was checked:** exact valuation exponents in the source's rendered local table, the absolute convergence exponents, the simultaneous conductor arithmetic, and finite slot aggregation. No numerical L-value evaluation, Lean check, or proof of Hu's analytic source identities was run. Independent mathematical review is requested.
