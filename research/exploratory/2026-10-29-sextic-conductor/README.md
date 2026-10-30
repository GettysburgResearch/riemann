# Good-prime conductors of Hu's sextic row characters

**Status:** Proposed proof of a source-facing local conductor lemma. No zero-free region is claimed.

**Scope and inputs:** Fix a number field `K` containing `mu_12` and a finite set of places `S` containing the places above 6 and the fixed ramification data in Hu, [*A seven-eighths zero-free half-plane for unitary Weil L-functions*](https://hexagonmath.org/2610.00216v1), Proposition 3.1(iii), its Kummer identification (p. 7), and §4. Let `u` be a nonzero `S`-integer, sixth-power-free outside `S`, and let `chi_u` be Hu's row character. We assume Hu's explicit identification of the primitive inducing character with the Kummer character of `K(u^(1/6))/K`, with the source's fixed finite twists unramified outside `S`. We use the classical tame Hilbert-symbol formula and local class field reciprocity. These are named inputs; the global character construction in Hu's Proposition 3.1 is not reproved.

## Claim

For every prime `p` outside `S`, the primitive inducing character has conductor exponent

    v_p(f_u) = 1   if 1<=v_p(u)<=5,
    v_p(f_u) = 0   if v_p(u)=0.

In particular every good prime dividing a sixth-power-free row is genuinely ramified. The original natural row presentation and the primitive inducing character have the **same zero** there. At every other good prime their Euler values agree by the Kummer/Frobenius identification in Hu Proposition 3.1. The local conductor at the finitely many places in `S` is uniformly bounded as `u` varies. Consequently

    N(f_u) <= C_(K,S) N(rad(u)) <= C_(K,S) N(uR),

where the radical and norm are taken outside `S`. The only local Euler factors that may need restoration when passing between the natural row numerator and its primitive inducing L-function lie in the fixed set `S`.

## Proof

Let `p` be good, with residue field cardinality `Q`, uniformizer `pi`, and write `u=pi^j a` with `a` a local unit. Since `K` contains `mu_6` and `p` does not divide 6, the residue field contains the six roots of unity and `6 | Q-1`. Local Kummer reciprocity identifies the restriction of the primitive row character to the local unit group, up to a fixed choice of reciprocity orientation, with the tame Hilbert symbol

    t -> (u,t)_(p,6) = (bar(t)^((Q-1)/6))^(+j or -j),   t in O_p^*.

The possible sign depends only on the reciprocity convention and has no effect on nontriviality. This formula follows from the standard tame-symbol expression for the sixth Hilbert symbol; the unit part `a` is immaterial on the unit subgroup. The resulting residue-field character has exact order `6/gcd(6,j)`. For `j=1,...,5` it is nontrivial but trivial on the principal-unit subgroup `1+p`. Thus its Artin conductor exponent is exactly one. For `j=0`, it is trivial on all local units, so the local character is unramified and has conductor exponent zero.

At the finite places in `S`, the local Kummer character depends only on `u` modulo `K_p^{*6}`, apart from one of the fixed local twists. The quotient `K_p^*/K_p^{*6}` is finite: the valuation gives `Z/6Z`, and the sixth-power image has finite index in the local unit group (for example, use the p-adic logarithm on a sufficiently deep principal-unit subgroup). Only finitely many local characters can occur, hence their conductor exponents have a fixed finite maximum. Combining these local factors proves the conductor bound.

At a good row divisor, a ramified primitive local L-factor is 1, matching the source's zero-extended natural coefficient. At any other good prime, the equality of Frobenius values is precisely the assumed global Kummer identification, including its reciprocity orientation; this is not deduced from the conductor exponent alone. The exceptional factors at `S` may be omitted or restored by a finite product. Their values can depend on the row, but their number is fixed, and on `Re(s)>=1/2` the product is bounded above in modulus by `2^|S|`. The reverse product requires separate lower bounds and is not asserted here.

## Consequence for the numerator AFE

The condition needed in [the fixed-field AFE note](../2026-10-29-fixed-field-afe/README.md) is met under Hu's Kummer identification: its varying primitive conductor has norm `O_(K,S)(Nu)`, and natural/primitive Euler restoration is restricted to the fixed set `S`. This deduction does not prove Hu's global Kummer construction, the paired fourth moment, or any uniform low/high contour estimate. In particular no new zero-free region follows.

**Review target:** Check the exact local Artin orientation and confirm that Hu's listed fixed finite twists are unramified outside `S`; check the tame formula including primes with residue degree greater than one. The claimed conductor conclusion is insensitive to inversion of the local character, but equality of its unramified Euler values is not.
