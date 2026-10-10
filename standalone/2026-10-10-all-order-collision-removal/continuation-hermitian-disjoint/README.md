# Hermitian all-prime-disjoint closure

**PROPOSED COMPONENT PROOFS; independent review pending. The high-conductor arithmetic estimate, full higher moments, 17/24 and RH remain unproved.**

Base: PR #916 at `e5d68883991b390798d993b0bafa7975ab801886`. The saved Gaussian packet is now published unchanged. Its old failed-push statements are historical, not the current publication status. The compact radial checkpoint `1b55960` is also preserved.

## A smaller arithmetic target

Previously, each k-factor product was internally coprime, but the two products could still share primes. Apply the inverse kernel to all 2k positions, using conjugate characters in the second half. After one explicitly larger FIXED excluded-prime cutoff, the signed integrated statistic I_C containing only pairwise-coprime factors across ALL 2k positions satisfies

    (1-q) I_M <= I_C <= (1+q) I_M, q<=1/3,
    I_M <= (3/2) I_C.

I_M is the complete integrated 2k-th moment. This comparison holds for any fixed nonnegative row measure, including the Gaussian. It does not say either quantity is small. It absorbs the completed signed collision error; it does not discard absolute collision terms.

Consequently the analytic problem may now use only COPRIME product columns r,s. Every nontrivial row character is primitive modulo rs. There is no changing common-prime mask, and the only ordinary diagonal is r=s=1, which contributes O(H). A finite-prime reinsertion proof preserves the original target exponent.

Read [PROOF.md](PROOF.md) for the complete mixed-colour identity, fixed cutoff, Holder comparison and reinsertion.

## A stronger low-conductor bound for this primitive scalar

For Q<=H the absolute primitive covariance has the Gaussian bound

    A_prim,<=Q << D^epsilon H Q^(-delta) exp(-c H/Q).

Thus Q<=H^(1-eta) is smaller than every fixed negative power of H, for each fixed eta>0. The old changing-gcd sum prevented this exponential decay from surviving its absolute summation. Here that sum has been removed by relative absorption, not falsely set to zero.

The remaining signed statistic has ONLY

    gcd(r,s)=1,
    Q=Nr Ns>H^(1/(1-delta)),
    Nr=Ns modulo 36.

A useful upper bound for it is still unproved. With excess lambda at H=D^h it would give the familiar conditional boundary

    1/2+delta+(lambda+5h/6)/(2k).

[DUAL_CORE.md](DUAL_CORE.md) supplies the exact primitive Gaussian transform, the sector proof and the full conditional adapter. It also proves why two bare Gaussian transformations return the original row scale rather than create a free contraction.

## Executed finite checks

Normal and optimized runs reproduce **12,028 exact predicates** with identical output. Two deliberately false formulas are rejected in each mode, and a tampered result is rejected in both modes. These are finite arithmetic checks, not an infinite moment certificate.

The new tests include mixed-colour identities through eight positions, genuine Eisenstein character zeros and phases, exact scale reconstructions, and weighted norm comparisons in explicitly declared finite prime alphabets at sigma=3/4, 2/3 and 5/8. They also find pointwise NEGATIVE disjoint sums, preventing misuse of the integrated positivity theorem. For example a fourth-order fixture has C=-12 while |A|^4=49.

    python -I -S -B check_hermitian_disjoint.py --check result.json
    python -O -I -S -B check_hermitian_disjoint.py --check result.json
    python -I -S -B check_hermitian_disjoint.py --negative-controls

The script uses the preserved Gaussian packet's arithmetic module and verifies its exact Git blob before loading it. See [VALIDATION.md](VALIDATION.md) for coverage and limits. No independent review, Lean build, new zero-free boundary, or proof of the primitive high-conductor estimate is claimed.
