# Approximate functional equation for the finite-order numerator over a fixed complex field

**Status:** Proposed derivation from the standard primitive Hecke functional equation, with source-facing application still conditional. It is not a proof of Hu's fourth moment, the variable-geometry high-side expansion, or a zero-free region. Independent mathematical review is requested.

**Scope:** A fixed number field `K` containing `mu_12`, so all archimedean places are complex, and the finite-order primitive numerator characters in Hu's [preprint](https://hexagonmath.org/2610.00216v1), formula (6.12). This reproduces the fixed-complex-field calculation in Liu, [arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835v1), §14.2 and Lemma 14.2, and the conductor/profile discussion in Proposition 14.3. The earlier Eisenstein-field case appears in Xu–Sang, [arXiv:2610.15291v2](https://arxiv.org/abs/2610.15291v2), Appendix B. No novelty is claimed for this calculation. Exact input and quantifiers are stated below.

## Analytic statement

Let `[K:Q]=2r`. Fix `0<=theta<=1/10` and `w=1/2+theta+it`. Let `chi` be a primitive, finite-order nonprincipal Hecke character of `K`, of finite conductor `f`. At every complex place its unitary local character is trivial. In a fixed standard gamma normalization, write

    Lambda(s,chi) = Q_chi^(s/2) Gamma(s)^r L(s,chi),
    Lambda(s,chi) = epsilon_chi Lambda(1-s,conjugate(chi)),
    Q_chi = |D_K| N(f) (2 pi)^(-2r),   |epsilon_chi|=1.

A fixed factor `2^r` from `Gamma_C(s)=2(2pi)^(-s)Gamma(s)` cancels from the functional equation. The displayed analytic continuation, functional equation, and finite-place Euler conventions are classical inputs. There are no poles of the completed function for nonprincipal primitive `chi`.

Define

    V_w(x) = (1/2pi i) integral_(Re v=2)
                 exp(v^2) [Gamma(w+v)/Gamma(w)]^r x^(-v) dv/v.

Then

    L(w,chi) = sum_a chi(a) N(a)^(-w) V_w(N(a)/sqrt(Q_chi))
      + epsilon_chi Q_chi^(-theta-it) [Gamma(1-w)/Gamma(w)]^r
          sum_a conjugate(chi(a)) N(a)^(-(1-w))
              V_(1-w)(N(a)/sqrt(Q_chi)).

Both sums range over nonzero integral ideals and converge absolutely with the weights. To derive this identity, integrate `Lambda(w+v,chi) exp(v^2)/v` from `Re v=2`; shift to `Re v=-2`, crossing only the pole at `v=0`; use the functional equation and `v -> -v` on the shifted line, and expand both L-series absolutely. Standard vertical-strip growth of completed Hecke L-functions and the Gaussian justify the horizontal limits. These analytic estimates are imported rather than reproved here.

Put `T=1+|t|`. For every fixed integers `j,N>=0`, the asserted uniform profile bounds are

    |(x d/dx)^j V_w(x)| <<_(K,j,N) (1+x/T^r)^(-N),
    |(x d/dx)^j { [Gamma(1-w)/Gamma(w)]^r x^(2theta) V_(1-w)(x) }|
        <<_(K,j,N) (1+x/T^r)^(-N).

These hold uniformly for `0<=theta<=1/10`, with constants depending on the fixed field and derivative/decay orders. For the first, shift the defining `v` line to `Re v=N` when `x>=T^r`, using Stirling uniformly with the Gaussian; for `x<=T^r`, shift it to `Re v=-1/4`, where the only crossed pole is `v=0` and `Re(w+v)>=1/4`. Euler derivatives insert powers of `v`, and the Gaussian controls the vertical integration. Stirling gives `|Gamma(1-w)/Gamma(w)|^r << T^(-2r theta)`; on `x<=T^r` this cancels `x^(2theta)`, while on the complement increasing the chosen decay order absorbs it. The same estimates remain valid after any fixed number of `log Q_chi` derivatives because these become fixed combinations of Euler derivatives in `x`.

## Dyadic coefficient balance

On a block `N(a)~D`, the first sum contributes a normalized central block with scalar `D^(-theta)` and a profile of bounded Euler seminorms, after the unit phase `(N(a)/D)^(-it)` is included. For the dual sum, the absolute scalar is `Q_chi^(-theta) D^theta` times the gamma ratio. With `x=D/sqrt(Q_chi)`, the exact identity

    Q_chi^(-theta) D^theta = D^(-theta) x^(2theta)

puts the same `D^(-theta)` factor outside and the remaining conductor and gamma factors into the bounded dual profile above. Conjugate the *whole* block where needed; the root number and conductor phase have absolute value one and can be removed after taking absolute values. Thus a dyad of length `D=U^m` has the `U^(-theta m)` decay assumed in the abstract numerator interface, subject to matching the coefficients and masks to Hu's moment.

## Conductors, tails, and choice order

Assume the physical row `u` has `N(u)~U`, and the standard local identification gives

    N(f_chi_u) <= C_(K,S) N(rad(u)) <= C_(K,S) U.

This holds if every good prime is tamely ramified at conductor exponent at most one and the local conductor at the finitely many bad primes belongs to a fixed bounded set; verifying those facts for the **actual** row symbols and their original zero extensions remains a source interface, not a result of the gamma argument. There are `O(log U)` primitive conductor dyads.

Fix a height range `|t|<=H<=U^tau` with `tau <= 1/(100(r+1))`. For `D>U^2`, the weight argument divided by `T^r` is at least a fixed multiple of `U^(3/2-r tau)`. Arbitrary profile decay, the elementary bound `# {a:N(a)<=X} <<_K X`, and at most polynomially many rows imply that the tail above this range is `O(U^-B)` for any fixed prescribed `B`, after choosing a sufficiently large **fixed** decay order. The number of retained dyads is `O(log U)`. The admissible `tau` depends on the fixed field degree; using a field-independent bound such as `1/100` without accounting for `r` is not justified.

To handle a row-dependent conductor, fix a dyad `C<=Q_chi<2C`. For the product `F_u(q)=S_(m,q)(u)^2 Q_sel(u)`, take `q=log Q_chi`; the selected slot factor is independent of this parameter. One-dimensional Sobolev on the common compact interval `log C<=q<=log(2C)` bounds the sum of rowwise suprema by integrals of `sum |F_u(q)|^2` and `sum |partial_q F_u(q)|^2`. The derivative of `S^2` gives two plain blocks, one with a profile derivative, multiplied by the **same** slot product. If Hu's paired moment accepts these same fixed-parameter profiles, their derivatives, character orientations, and all common masks, its bound applies uniformly in `q`. Integrating over the interval and summing conductor dyads costs at most logarithms and the fixed profile/height factors. This is a conditional application of the moment theorem, not a proof of its coefficient-class hypotheses.

Fixed bad-prime restoration may be removed by splitting off ideals supported on `S`, whose central coefficients have summable total mass over fixed `S`; every other local factor and original zero extension must match the physical character. All profile orders, slot count and loss budgets are chosen before the late height exponent and the external tail order.

## Remaining checks

- Independently review the gamma-ratio contour shifts, including uniformity at small `t`, the field constants and the conductor dyad Sobolev step.
- Verify the actual sextic row conductor and all primitive/imprimitive local identities, including the bad-prime unit sectors, rather than assuming the displayed conductor inequality.
- Check that Hu Theorem 4.2 admits both differentiated plain profiles in exactly the same selected-slot product with its fixed-character restrictions and original masks. The contour-dependent slot phases, physical row support, local error ledger and variable geometry remain separate obligations.

**What was done:** an analytic derivation from the standard Hecke functional equation and elementary fixed-field estimates, with the physical conductor/moment applications explicitly conditional. No Lean build, computation of the target L-functions, or proof of a zero-free region was performed.

## Local conductor reduction under explicit sextic-symbol hypotheses

The preceding conductor input follows from a small, exact local assertion, which is independent of the variable geometry. Enlarge the fixed set `S` to contain all primes above 6 and the fixed auxiliary modulus. Suppose the row is sixth-power-free outside `S` and the associated primitive character has the following source properties:

1. At a good prime `p` with `j=v_p(u) in {1,...,5}`, its local unit character is the `j`th power of the primitive sextic residue character on `(O_K/p)^*`.
2. At a good prime `p` not dividing `u`, the local character is unramified.
3. At every `p in S`, its local character depends only on the image of `u` in `K_p^*/K_p^{*6}`, up to a fixed finite family of twists.

As `K` contains `mu_12`, every good residue field contains `mu_6`; its primitive sextic character has exact order six. For `j=1,...,5`, its `j`th power is nontrivial and factors through the residue field, so its local conductor exponent is exactly one. At an unramified good prime the exponent is zero. For a fixed nonarchimedean local field the quotient `K_p^*/K_p^{*6}` is finite: the valuation contributes `Z/6Z`, and the unit quotient is finite because the sixth-power map has open image on the compact unit group. Thus hypothesis 3 admits only finitely many local characters and has a uniform conductor-exponent maximum. Consequently

    f_chi_u = f_S(u) product_(p|u, p notin S) p,
    N(f_S(u)) <= C_(K,S),

and `N(f_chi_u) <= C_(K,S) N(rad(u))`. At every good prime dividing `u`, the primitive local factor is 1, agreeing with the zero extension of `chi_u` at that prime. At other good primes, agreement of the values of the chosen physical and inducing characters must be checked from their global normalization; it does not follow solely from the conductor exponent. The three numbered local hypotheses, in particular the Hilbert-symbol phase and source normalization at `S`, remain to be verified from Hu's actual definitions. No statement here presumes that arbitrary sixth-power-free ideal labels automatically satisfy them.

**Source identification:** Hu Proposition 3.1(iii), equations (3.1)–(3.2) and its Kummer-theory proof state that `a -> chi_a(u)` is induced away from its displayed zeros, that the primitive conductor is `<<_(K,S) N rad(uR)`, and that the good local character is tame and unramified when `u` is a unit. The paragraph just after Lemma 4.12 further states that, for sixth-power-free physical `u`, every exterior prime dividing `u` is ramified and nonprincipal in the local Kummer character, so all sufficiently large rows avoid the finite exceptional family. Thus these are not additional new analytic conjectures if Hu's cited source claims are taken as inputs. A local-normalization audit of those source claims remains outstanding here.
