# Low-height Artin transfer from an arbitrary cyclic subgroup

**Status:** Proposed consequence of published Hecke and Dedekind zero-free theorems and Stark's theorem. Independent proof review and prior-art search are required. No new result for the Riemann zeta function is claimed.

**Inputs:** Ahn–Kwon's [order-at-least-three Hecke zero-free theorem](https://doi.org/10.1016/j.jnt.2014.06.008), [Das–Gaba–Lee–Savalia–Wong, Theorem 1.2](https://arxiv.org/html/2506.19319), Ahn–Kwon's separate low-height Dedekind zeta theorem, Stark's low-order Artin holomorphy theorem, the [Platt–Trudgian partial RH verification](https://doi.org/10.1112/blms.12460) for the `M0=Q` case, the conductor–discriminant formula and Artin induction. These are imported, not reproved. See the [prime-order report](../../../reports/2026-10-29-prime-cyclic-transfer.md) and [odd-order extension](../2026-10-29-odd-cyclic-transfer/README.md).

## Theorem

Let `K/k` be a finite Galois extension of number fields with group `G`, and let `H=<h>` be cyclic of order `m>=3`. Put

    M=K^H,  M0=K^(H^2),  g=gcd(2,m),
    D=|disc(K/Q)|,  d=|disc(M/Q)|,  d0=|disc(M0/Q)|,
    phi=phi(m),  T=log D-(m-phi) log d.

Write `[M0:Q]=n0`. For `n0>=2`, define `C_n0` by

    n0       2          3          4          5          6       >=7
    C_n0  16.01983   19.55293   16.72207   13.71235   11.78180   11.51910,

and set

    Delta = min{ phi/(15.10 T), 1/(C_n0 log d0) }   if n0>=2,
    Delta = phi/(15.10 T)                            if n0=1.

For `Re(s)>1-Delta` and `|Im(s)|<(1/3)tan(pi/8)`, every irreducible Artin L-function of degree at least two, and every nonreal one-dimensional Artin L-function, is holomorphic and nonzero. At most one simple real zero of a real one-dimensional character can remain in this region. Every nontrivial irreducible is holomorphic and nonzero at `s=1`; the trivial character has the usual pole of `zeta_k` there.

Every irreducible on which `H^2` acts nontrivially is in particular covered by the nonreal induced factors in the proof. The potential exceptional real one-dimensional representation is necessarily trivial on `H^2`; the trivial representation is included among the real one-dimensional possibilities away from its pole.

For `n0>=2`, the simpler width

    min{phi/15.10, m/(g*C_n0)} / log D

is always permitted. When `n0=1`, the simpler width `phi/(15.10 log D)` is permitted. For `n0>=7` it is also permitted without a minimum: `phi<=m/g` and `15.10>11.51910`. For odd `m` we have `g=1`. If in addition `n0>=5`, then `C_n0<15.10` and the second condition in `Delta` is automatic; this includes the [odd-order result](../2026-10-29-odd-cyclic-transfer/README.md) with `n0>=7` and extends its coverage to *all* degree-at-least-two irreducibles and all nonreal one-dimensional irreducibles, even when they are trivial on `H`.

## Proof

Let `lambda` be a generator of the character group of `H`. Let `f` be its primitive conductor over `M` and put `Q=N_(M/Q)f`. Every `lambda^j` has conductor dividing `f`, and the `phi` faithful powers have the same conductor as `lambda`. The conductor–discriminant formula therefore gives

    D >= d^m Q^phi,    log(dQ)<=T/phi.                    (1)

The `g` characters of `H` of order dividing two are exactly those trivial on `H^2`. Using the two class-field factorizations **over M**, including ramified local factors,

    zeta_K = product_(chi in H-hat) L_M(s,chi),
    zeta_M0 = product_(chi in H-hat, chi^2=1) L_M(s,chi),

we obtain the meromorphic identity

    zeta_K/zeta_M0 = product_(chi in H-hat, chi^2 != 1) L_M(s,chi).    (2)

For odd `m`, `M0=M`; for even `m`, `M0/M` is quadratic. Equation (2) is **not** the factorization for the separate cyclic extension `K/M0`.

Each factor on the right side of (2) has order at least three and conductor parameter at most `dQ`. Ahn–Kwon gives its holomorphic nonvanishing for `Re(s)>1-1/(15.10 log(dQ))` and the stated height. By (1) this contains the first region in `Delta`. Thus the quotient in (2) is holomorphic and nonzero there, and for `s!=1`,

    ord_s zeta_K = ord_s zeta_M0.                         (3)

When `n0>=2`, the second region in `Delta` lies in the applicable Das et al. degree-specific domain, where `zeta_M0` has at most one exceptional real zero. Ahn–Kwon's separate `1/(2 log d0)` low-height zeta theorem implies that this possible real zero is simple. Hence (3) gives `ord_s zeta_K` equal to zero or one away from `s=1`, with a possible order-one zero only on the real axis. Stark's theorem makes each irreducible Artin L-function holomorphic at such an `s`.

When `n0=1`, the equality `M0=Q` forces `M=Q`, `H=G`, and odd `m`, because `M⊆M0` and `H²=G=H`. The faithful character is then a nontrivial Dirichlet character with finite conductor `Q>=2`. Formula (1) gives `log D>=phi log Q`; hence `Delta<=1/(15.10 log 2)<1/2`. The region is contained in `Re(s)>1/2`. The [Platt–Trudgian partial RH verification](https://doi.org/10.1112/blms.12460) excludes nonreal zeta zeros there because the height is below 1; ζ has no real zero for σ>0, and its Euler product excludes zeros for σ>1. Its pole at one is treated separately. Thus `ord zeta_M0=0` throughout the region away from one, and Stark yields holomorphy there. In this special case all nontrivial irreducible Artin L-functions are nonvanishing, and the trivial zeta factor has no zero there.

Use the regular-representation factorization

    zeta_K(s) = product_(rho in Irr(G)) L(s,rho)^(dim rho).

At a zero, all individual orders are now nonnegative integers. Since their weighted sum is at most one, no degree-at-least-two irreducible can vanish, and at most one degree-one irreducible can vanish, with order one. If that character is nonreal, its distinct complex conjugate also vanishes at the same real point, a contradiction. A real one-dimensional character takes only values `+1` and `-1`, and is automatically trivial on `H^2`.

Separately, Frobenius reciprocity applied to the nonreal factors in (2) directly excludes any irreducible whose restriction to `H` contains a character of order at least three; this is exactly the condition that `H^2` acts nontrivially. At `s=1`, the standard Brauer–Hecke argument gives holomorphy and nonvanishing of nontrivial irreducible Artin L-functions, and the trivial Artin L-function has its usual simple pole.

The faithful character is nontrivial, so `dQ>1`: if `d=1`, then `M=Q` and `Q>=2`; otherwise `d>1`. Thus (1) gives `T>=phi log(dQ)>0`. Also `D>=d0^[K:M0]=d0^(m/g)`, and `T<=log D`. Therefore the simplified width follows. For `n0>=2` and `g=1`, `T>=phi log d0`; therefore the Hecke condition is already inside the low-order domain whenever `C_n0<15.10`. For even `m`, the separate intersection is necessary for this proof: the elementary tower bounds only give `T>=phi log d0/2`, which does not imply the needed `C_n0` condition.

## Order-at-least-five refinement

If `3` and `4` do not divide `m`, every character in (2) has order at least five. The Ahn–Kwon coefficient `0.1149` quoted in [Zaman 2016, equation (1.1)](https://arxiv.org/html/1502.05679) then yields the same conclusions for `n0>=2` on

    Re(s)>1-min{0.1149 phi/T, 1/(C_n0 log d0)},  |Im(s)|<=0.13.

For `n0=1`, omit the second entry in the minimum: `0.1149 phi/T<=0.1149/log 2<1/2`, so the same Platt–Trudgian argument applies.

The explicit subregion with width `min{0.1149 phi, m/(g*C_n0)}/log D` follows for `n0>=2` as above. If `3` does not divide `m` but `4` does, every quotient character has order at least four; the coefficient `0.1004` quoted in the same source gives the analogous region with 0.1004 replacing 0.1149. The stronger 0.1149 case excludes both order-three and order-four characters; an order-two character, when present, has already been removed into `zeta_M0`. When `3|m`, the quoted order-three coefficient 0.0662 is slightly weaker than `1/15.10`, so the original Ahn–Kwon input is preferable.

## A Dedekind zeta corollary without quadratic subfields

Suppose k=Q and G has no quotient of order two. Then the trivial character is its only real one-dimensional character. The theorem excludes zeros of all other irreducible factors, and each factor is holomorphic away from s=1. The remaining factor is ζ_Q. Since `dQ>=2` in the proof and `Delta<=1/[15.10 log(dQ)]<=1/(15.10 log 2)<1/2`, the region lies strictly to the right of 1/2. The cited Platt–Trudgian verification excludes nonreal ζ_Q zeros there at the stated small height, and ζ_Q has no real zero for σ>0. Hence **ζ_K itself is zero-free in the theorem's region**, with its simple pole at s=1. If G=S_n for n>=5, its only nontrivial real one-dimensional character is sign; the theorem leaves at most one simple real zero from that factor. For G=A_n, n>=5, there is no sign factor and the zero-free ζ_K conclusion applies.

Eliminating exceptional zeros in normal extensions without quadratic subfields is a classical consequence of Stark: see [Pierce–Turnage-Butterbaugh–Wood, Theorem 5.9 and Theorem N](https://dukespace.lib.duke.edu/bitstreams/6ca77058-c44c-4932-8fa5-cb7c8c9570ec/download). The observation here is only a transfer of the explicitly stated widths, with no global priority claim. For n0>=7 the simpler width is `phi/(15.10 log D)`; since phi>=2, its coefficient is at least 2/15.10, about 52.6% wider than the degree-at-least-seven Das et al. ζ_K width `1/(11.51910 log D)` where that baseline applies. The latter covers |t|<=1. At the much smaller heights |t|<1/(2 log D), the Ahn–Kwon bound for ζ_K permits one simple real zero in width `1/(2 log D)`; the no-quadratic-subfield argument removes it. Depending on phi and the field-specific discriminants, this thin-height bound or the present one may be wider. The recent claimed fixed half-plane cited in the prior-art notes would supersede these logarithmic widths if verified; it is not an input here.

## A full-height refinement under Zaman's large-parameter hypothesis

Assume `[M0:Q]=n0>=2` and retain the degree-dependent `C_n0` above. Let `n=[M:Q]`, and let `f` be the faithful character conductor from the proof, with `Q=N_(M/Q)f`. Fix a function `nu(x)` satisfying the hypotheses of [Zaman 2016, Theorem 1.1](https://arxiv.org/html/1502.05679): increasing, at least 4, and `nu(x)>>log(x+4)`. For example one may fix `nu(x)=4+log(x+4)`. Suppose `d Q n^n` is sufficiently large in the precise sense of that theorem, whose threshold may depend on the fixed `nu`. Put

    Lambda = log d + (3/4)log Q + n nu(n),
    c_m = 0.1227 if 3|m or 4|m;
          0.1489 if neither 3 nor 4 divides m but 5|m;
          0.1764 if none of 3,4,5 divides m.

Then the conclusions of the theorem hold throughout

    Re(s)>1-min{ c_m/Lambda, 1/(C_n0 log d0) },  |Im(s)|<=1.

This is a genuinely wider ordinate range than the preceding Ahn–Kwon input, but only under Zaman's stated large-parameter hypothesis; no explicit threshold is asserted here.

Indeed, every nonreal power of `lambda` is a character of the narrow ray class group modulo `f`, possibly imprimitive. Its order is preserved under the natural surjection from that ray group to its inducing quotient. Zaman's product theorem with `r=3`, `5`, or `6` as dictated by the three cases above gives at most one zero, necessarily belonging to a real character. The relevant product contains no real characters because all characters of order at least three are nonreal, so it has **no** zero in the quoted rectangle. Thus every natural ray L-function in (2) is zero-free there. Removing its finitely many extra Euler factors changes no zeros for `Re(s)>0`, so the primitive factors are zero-free as well. The inequality `Lambda>=4n` ensures that the rectangle lies in `Re(s)>0`.

The second minimum term is still required: it ensures `ord_s zeta_M0<=1`, enabling the Stark and conjugation steps exactly as above. When `M0=Q`, the group is cyclic odd as in the `n0=1` case above; under the same Zaman large-parameter premise the nontrivial irreducibles are directly zero-free in `Re(s)>1-c_m/Lambda`, `|Im(s)|<=1`, without this second restriction. The trivial `zeta(s)` factor is not covered by that direct assertion.

**What was checked:** The two class-field factorizations, faithful-power conductor bound, discriminant comparisons, regular-character order calculation and complex-conjugate zero argument. The source theorems and full ramified local Artin formalism are imported. No worldwide priority claim is made.
