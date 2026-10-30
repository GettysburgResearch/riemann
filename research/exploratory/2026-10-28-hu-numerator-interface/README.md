# A high-side numerator interface for Hu's unitary target

**Audit correction:** An earlier draft incorrectly read the imported table’s `V^(1_(j<=1))` as `V * 1_(j<=1)`. The corrected ramified exponents below were independently rechecked against the rendered source. The source identity and the full high-side argument remain unaudited.

**Correction and audit:** An earlier calculation omitted a ramified term for valuations j ≥ 2. The formulas below retain it and received an independent internal check; the source-table transfer remains an explicit input.

**Status:** Conditional analytic interface. It is not a proof of the physical hypotheses, Hu's source estimates, or a new zero-free region.

**Source:** Hu, [*A seven-eighths zero-free half-plane for unitary Weil L-functions*](https://hexagonmath.org/2610.00216v1), Theorem 4.2 and (6.10)–(6.12); Xu and Sang, [arXiv:2610.15291v2](https://arxiv.org/abs/2610.15291v2), Proposition 5.1 and §6. The fixed-field version of the argument below requires all coefficient classes, masks, losses, and height quantifiers to be checked in these sources; no full replay is claimed.

## Source observation

In Hu (6.12), a physical row contributes

    zeta_K^S(6z) L_K^S(w,chi_u) H_(u,psi)(s,w,z) / L_K^S(s,psi conjugate(chi_u)).

Thus the numerator character `chi_u` is finite order even when the fixed target `psi` has infinite order. The target is still present in the detector, local correction, and denominator; it cannot be dropped there. For the numerator average, a finite-order character approximate functional equation suffices, with field and fixed finite local data held fixed. Hu's paired fourth moment, Theorem 4.2, includes `kappa=3/4` under its finite-order `7/8` zero-free premise; it is therefore a possible input to a **first** improved stage. It does not by itself establish any stage with `kappa<3/4`.

## Abstract moment-to-first-moment lemma

Let `U>=2`, `kappa>0`, `0<=q`, `R>=0`, `L>=0`, and let `B` be a finite row class whose inducing characters are nonprincipal, with

    #B << U^(R+epsilon) (1+H)^A.

Assume the following estimates, with constants uniform over the indicated row class and all permitted dyadic blocks, and with an arbitrarily small common power loss:

1. Each normalized block `S_m(u)` appearing in the numerator's approximate functional equation has length `U^m`, and the coefficient from the shifted line is at most `U^(-vartheta*m)` times a uniformly controlled smooth profile. The dual block has this same effective bound after its conductor scale is incorporated in the profile. The retained blocks have `m` in a fixed bounded interval; tails can be made arbitrarily small with fixed seminorm costs.
2. Given `0<=z<=L`, a fixed selection of physical prime slots is available for the entire row class and satisfies `|Q_sel(u)|^2 >= U^(2qz-epsilon)` on every row. For `0<=m<=1/2` the product fourth moment

       sum_(u in B) |S_m(u)|^4 |Q_sel(u)|^2 << U^(1+epsilon) (1+H)^A

   holds whenever `2m+6*kappa*z<=1`. The zero-slot fourth moment holds for all remaining retained blocks. Whole-character conjugation, finite Euler restorations, rowwise conductor profiles, and rounding to whole slots are included in these assumptions.
3. For any `m`, absolute ideal counting supplies `|S_m(u)| << U^(m/2+epsilon) (1+H)^A`. Here `H>=1` bounds the relevant heights and its polynomial cost is retained.

Put `K=(3R+1)/4` and `0<=vartheta<1/2`. Under the above hypotheses either of the following choices gives

    sum_(u in B) |L_K(1/2+vartheta+it,chi_u^*)|
       << U^(K-vartheta/2+epsilon) (1+H)^A',

uniformly in the allowed heights:

- `vartheta=q v`, where `0<=v<=min(L,1/(6*kappa))`;
- `vartheta=q/(6*kappa)`, provided `R <= (6*kappa-2q)L` and `L<1/(6*kappa)`. If `L>=1/(6*kappa)`, the preceding supply-limited case already permits full capacity.

**Derivation.** For `0<=m<=1/2` in the supply-limited case, choose `z=v(1-2m)`. It fits both slot supply and moment capacity. The rowwise slot lower bound and fourth moment give `sum_B |S_m|^4 << U^(1-2qz+epsilon)`. Hölder with the row count gives `sum_B |S_m| << U^(K-qz/2+epsilon)`. The shifted coefficient contributes `U^(-vartheta*m)`, and because `vartheta=qv`,

    -vartheta*m - q v (1-2m)/2 = -vartheta/2.

For `m>=1/2`, use the zero-slot moment and the block coefficient to get at least the same decay. Sum the fixed-logarithmic number of blocks and absorb the stated losses.

In the full-capacity case let `m0=1/2-3*kappa*L>0`. The same argument applies for `m>=m0`. For `0<=m<=m0`, the absolute rowwise bound gives exponent `R+(1/2-vartheta)m`, largest at `m0`; with `vartheta=q/(6*kappa)`, its difference from `K-vartheta/2` is exactly

    [R-(6*kappa-2q)L]/4 <= 0.

This proves the abstract lemma subject to the displayed hypotheses. It is the same Hölder and short-block mechanism as Xu–Sang Proposition 5.1, stated here to isolate what Hu's physical data must provide.

## Exact physical gates

- Check that the selected slots used in the row detector are the **same physical prime polynomials** as in Hu (6.10), including conjugations and every zero-extension mask, and that `chi_u^*` falls within Hu Theorem 4.2's allowed row family and exceptional-set convention.
- Derive the approximate functional equation and its dyadic profile bounds for the inducing characters over a fixed arbitrary field, including variable conductor, gamma factors, primitive/imprimitive Euler corrections, and polynomial height dependence. The numerator's fixed infinity type is finite-order; the denominator's genuinely unitary type remains in all separate analytic interfaces.
- Transport the detected row-count exponent, local correction and amplitude-dependent `w`-line through Hu's variable geometry and unit-sector decomposition. The gain above is offset by the functional-equation and outside `Y` factors and must be budgeted in the **same** physical probe, not treated as an isolated zero-free estimate.
- Prove the full low-side source matching, all nonprincipal high and tail ranges, principal noncancellation, target-uniform saving, and descent. Without these, the displayed numerator average does not improve Hu's `7/8` claim.

**What was checked:** The displayed Hölder and two-case exponent calculations; source observation (6.12). The analytic moment, profiles, slot transport and continuation were not independently proved.

## Elementary whole-slot selection

The rounding component of hypothesis 2 can be isolated independently of the source's analytic estimates. Let finitely many slot widths `w_i>=0` sum to `L>0`, and let their rowwise squared-amplitude lower exponents be `2 w_i g_i`, where `0<=g_i<=G`. Assume `sum_i w_i g_i >= q L` for a fixed `q>=0`. For every requested `0<=z<=L`, order slots by decreasing `g_i` and take the fractional initial segment of total width `z`. Its weighted average is at least the average over all slots, so its gain is at least `qz`. Discarding the last fractional slot gives a **whole-slot** subcollection of total width at most `z` and gain at least

    qz - G max_i w_i.

If `|Q_i(u)|^2 >= U^(2 w_i g_i)` for every row in a fixed class, the selected product satisfies

    product_selected |Q_i(u)|^2 >= U^(2qz - 2G max_i w_i)

uniformly over that class. This proof also covers zero-amplitude slots, a zero request and ties. It justifies the combinatorial rounding loss once the amplitude bins and the same physical `Q_i` have been established. It does not show that a given mixed-moment theorem permits those physical slots or their masks.

## Slot orientation and conductor-profile reduction

The following checks part of the first two gates, conditional on the cited source's definitions and moment theorem. Write `P_i=Z^ell_i`, `Q=N(p)`, and let `W_i` be the fixed **real-valued** physical window (Hu takes nonnegative windows). Define the normalized positive-orientation polynomial

    Q_i^+(u;z) = P_i^(-1/2) sum_(p notin S) W_i(Q/P_i)
                       (Q/P_i)^(conjugate(z)-1) chi_u(p).

Hu (6.10), with the original zero extensions of the residue character, gives the exact identity

    Q_i(u;z) = - P_i^(z-1/2) conjugate(Q_i^+(u;z)).

The conjugate applies to the **entire** factor: the window, norm phase, character and every common zero mask. Therefore a rowwise lower bound for the normalized physical factor is exactly a lower bound for `|Q_i^+|`, at the same row and ordinate. Taking an absolute value does not justify conjugating only the residue symbol while dropping a mask.

For the numerator in (6.12), take Hu Theorem 4.2 with `lambda_u=xi_u=chi_u` and `omega_0=1`. The actual character in both plain columns and selected slots is then `chi_u`; the relative slot coefficient is the constant finite character. A fixed ray restriction, if imposed by a sector, expands by finite character orthogonality and gives a finite linear combination of permitted coefficients. The original good-prime exclusion and `chi_u(p)=0` at row primes remain in every slot. For Hu’s sixth-power-free physical rows, his §7.1 asserts that a row with a good prime divisor induces a character outside the fixed exceptional family `Theta`; rows supported entirely on the fixed set `S` have bounded norm and are assigned to the separately treated small-row range. This exceptional-row assertion is an imported source fact, and its local ramification proof has not been replayed here. Multiplying each annular test by `(Q/P_i)^(conjugate(z)-1)` is a smooth profile change on its fixed compact support, with finitely many seminorms bounded by a polynomial in `1+|Im z|`. This proves the algebraic orientation match for each fixed sector **if** the original physical polynomial is the one in (6.10), and if its sector masks are exactly those admitted in Theorem 4.2. It does not prove that the local-error decomposition can be dominated by these same main factors or that all detector presentations have the needed source uniformity.

The numerator's primitive conductor profile can be separated without assuming that conductor is constant across rows. On one dyad of primitive conductor norm `C<=N(f_u)<2C` and one Dirichlet block `D<=N(n)<2D`, write the smooth approximate-functional-equation profile as a function `F(log(N n/D), log(N f_u/C))`, after extracting the appropriate power of `D`. For every fixed finite seminorm order and bounded shifts, compact support plus Fourier inversion represents `F` by an absolutely integrable density of products

    (N n/D)^(it_1) (N f_u/C)^(it_2).

The second factor has absolute value one and is constant in the inner `n` sum for that row. Minkowski and the source moment's bounded-height profile uniformity then reduce to weights common to all rows in that conductor dyad. Conductor dyadization costs only `O(log U)` provided the conductor is at most a fixed power of `U`; arbitrary cutoffs, tails, gamma quotients, and the height factors still require the usual fixed-field Hecke approximate functional equation and its seminorm estimates. This separation proves that a varying conductor **alone** is not a need for row-dependent slot coefficients; it does not establish those approximate-functional-equation estimates.

At any omitted finite prime, the imprimitive L-function is the primitive inducing L-function multiplied by factors of the form `1-chi_u^*(p)Q^(-s)` where relevant. In the half-plane `Re(s)>=1/2`, its modulus is at most `2`; for a set of primes supported on a polynomially bounded row conductor or row ideal, the product is at most `2^omega(a) <<_epsilon (N a)^epsilon`. This elementary upper bound is sufficient when upper-bounding the imprimitive L-function by the primitive one, **after** the restoration has been correctly identified prime by prime. It does not bound the reciprocal restoration, identify a missing Euler factor, or supply a lower bound. Hu's finite fixed set `S` may be absorbed in the fixed constants.

These checks are exact for the stated specializations but retain three material gaps: an independent source audit of the identity between the actual numerator inducing character and `chi_u` at every ramified/zero-extended prime; the full fixed-field approximate functional equation with controlled separated profiles; and the variable-geometry high-side expansion, especially error slots and amplitude-dependent contours. No numerical zero-free improvement follows from this section by itself.

## Simultaneous ramified-label budget

The conductor saving used to keep the reflected numerator can be expressed without any source-specific asymptotic. Let a nonzero ideal `u` have valuations `j_p` in `{0,...,5}` outside a fixed finite set, and suppose the primitive finite-order numerator has conductor `f_u` satisfying `N f_u <= C N rad(u)` for a fixed constant `C`. If `J` is any set of distinct good primes dividing `u` with `j_p>=2`, then

    N f_u <= C N u product_(p in J) (N p)^(-(j_p-1)).

This is a prime-by-prime consequence of `N rad(u) = N u product_(p|u) (N p)^(-(j_p-1))`; dropping factors outside `J` can only enlarge the right side. For `vartheta>=0`, multiplying the functional-equation factor `(N f_u)^vartheta` by one strict ramified local factor `(N p)^(vartheta-1/2)` for each `p in J` yields

    (N f_u)^vartheta product_(p in J) (N p)^(vartheta-1/2)
      <= C^vartheta (N u)^vartheta
         product_(p in J) (N p)^(-1/2-(j_p-2)vartheta)
      <= C^vartheta (N u)^vartheta product_(p in J) (N p)^(-1/2).

The same conductor deficit is used once for the whole set of distinct labels, not once per independent application of a global conductor inequality. This algebra remains valid when the labels arise from different fixed, disjoint slots. Hu Proposition 6.3 asserts the needed squarefree-radical conductor bound for its sextic rows, while Xu–Sang Appendix C uses the same ledger. To turn this into the full physical error estimate, one still must verify Hu's local error decomposition at the raised line term by term, including the phases, all other ramified classes, and the unselected correction. The lemma alone does not supply those local bounds or the required nonzero local denominators.

## Unramified local error at the raised numerator line

This calculation checks the unramified part of the raised-line matching directly from Hu (6.11)–(6.13), conditional on those source identities. At a good prime `p` not dividing the row, set

    Q=Np, v=Q^(-1), V=Q^(-6z), W=chi_u(p) Q^(-w),
    D=psi(p) conjugate(chi_u(p)) Q^(-s),
    R=vartheta(p)^6 Q^(4-6s) V, c=conjugate(chi_u(p)).

All character phases have modulus one; `Q^(-w)=c W` and `conjugate(psi(p)) Q^s=c/D`. With Hu's `P=P_p`, `Pstar=P_p^*`, his local identity reads

    P-Pstar = 1/(1-V)+W/(1-W),
    Pstar+D = [R((1-v)/(1-V)+W-D)
                    - D(Q-1) W V/(1-V)]/(1-R).

The second identity is obtained by simplifying Hu's displayed local formula, including the denominator `1-V`. Suppose `Re(s)>=51/100`, `Re(z)=17/50`, and `Re(w)>=2/5`. For sufficiently large `Q`, all `|D|,|V|,|W|,|R|` are uniformly small, and the identities imply

    |Pstar+D| << |R| + |D| Q |W V|,
    |P-1| << |D|+|V|+|W|+|R|+|D| Q |W V|.

Thus `P` and the unselected correction are bounded away from zero. Write `B=G_p/H_p`. Using Hu (6.13), the local Euler normalization, and the two identities above, cancellation of the linear `W` term gives

    B/c + 1 << |D| + |V| + |R|/|D| + Q |W V|.

Indeed, put `E=Pstar+D`; after substituting `Pstar=-D+E`, the numerator of `(B/c+1)(1-V)(1-W)P` is

    V(1-W)^2 + E(1-V)(1-W)(1+1/D-W)
                 - D(1-V)(1-W)(1-W).

Each remaining bounded factor is controlled uniformly after the fixed initial-prime cutoff. Taking absolute values gives exactly the four powers

    Q^(-Re(s)), Q^(-6 Re(z)), Q^(4-5 Re(s)-6 Re(z)),
    Q^(1-Re(w)-6 Re(z)).

On the displayed line each is `O(Q^(-51/100))`. The calculation is unchanged by a fixed infinite-order target because it uses only the unit modulus of its local value. In a fixed annular slot `Q~P_i`, summing against the extracted `Q^(z-1)` factor and using `O(P_i)` ideals in the norm range gives an absolute error `O(P_i^(Re(z)-51/100))`, up to fixed window constants. Thus the *unramified normalized error* needed in Xu–Sang Appendix C.2 has the stated size for Hu's local rational formula. The estimate is local: applying the infinite product and contour argument still requires the source's separate `Re(s+w)>1` margin. It does not cover ramified rows, the complete error expansion, contour shifts, or the original local identity's proof.

## Ramified local table: a sufficient upper-bound check

We also check that the valuation powers used in the error estimate are sufficient, conditional on the full local table in OpenAI Lemma 7.1 and Hu's assertion that the same table, up to unit phases, holds over his field. This is not an independent derivation of that table. Let `p|u` be good, `j=v_p(u)` in `{1,...,5}`, `sigma=Re(s)`, `z0=Re(z)=17/50`, and `w0=Re(w)`. Assume `51/100<=a<=7/8`, `sigma>=a+16e`, and `w0=1/2-vartheta`, where `e>0`, `0<=vartheta<=1/10` and `vartheta<=a-1/2` (so `w0>=max(2/5,1-a)` and `sigma+w0>=1+16e`). At this prime the zero extensions give `D=W=0`, but the separate `W_loc` in the local table is **not** set to zero. Hu's local normalization yields

    H_p=(1-V) P_p,       G_p=conjugate(psi(p)) Q^s (1-V) P_p^* - Q^(-w),
    P_p=1/(1-V)+P_p^*.

The source's table, bounding all unit phases by one and retaining its `1/(1-R)` denominator, gives

    |P_p^*| << |R| + 1_(j=1) Q^(1-sigma-w0-6z0)
                      + 1_(j>=2) Q^(1-sigma-w0) + T_j,
    T_1=Q^(-sigma-w0),
    T_2=Q^(3/2-3sigma),
    T_3=Q^(2-3sigma-w0)+Q^(2-4sigma),
    T_4=Q^(5/2-4sigma-w0),
    T_5=Q^(3-6sigma).

The small power in the second term is bounded using the actual `s` and `w`, with no assumption on an infinite-order phase. The constraints imply every displayed term is at most a fixed negative power of `Q`; after enlarging the fixed prime cutoff, `|H_p|>=1/2`. Consequently, for `B_p=G_p/H_p`,

    |B_p| << Q^(-w0) + Q^sigma ( |R| + 1_(j=1) Q^(1-sigma-w0-6z0)
                                         + 1_(j>=2) Q^(1-sigma-w0) + T_j ).

After multiplying the physical selected factor `Q^(z-1)` and extracting `Q^z`, the powers contributed by the `T_j` are, respectively,

    j=1: -1-w0;  j=2: 1/2-2sigma;
    j=3: 1-2sigma-w0, 1-3sigma;
    j=4: 3/2-3sigma-w0;  j=5: 2-5sigma.

Each is strictly below `-1/2` on the stated constraints. The baseline term `R` contributes `3-5sigma-6z0<-1/2`, and the `j=1` extra term contributes `-w0-6z0<-1/2`. The direct `Q^(-w0)` term contributes `-1-w0`. The additional `j>=2` term contributes the strict exponent `-w0`, because the source has `V^(1_(j<=1))`, which equals one for `j>=2`. This is exactly the term that needs the simultaneous conductor-deficit ledger above. Bounds are uniform in unit phases and imaginary parts, but their cutoff and constants depend on the stated margins. As in Xu–Sang, the finite prime tuple and fixed arithmetic data must be chosen in the prescribed order. This proves a **local upper-bound interface**, not the full high-side moment or contour result.
