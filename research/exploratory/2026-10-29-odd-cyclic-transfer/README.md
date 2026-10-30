# A low-height transfer from odd cyclic subgroups

**Status:** Proposed consequence of published zero-free and Stark theorems; independent mathematical review and prior-art search requested. The result is conditional only in the ordinary sense of using those cited theorems, not on a conjectural zero-free estimate.

**Scope:** A finite Galois extension `K/k` of number fields with an odd-order cyclic subgroup. The conclusion covers all irreducible Artin representations of degree at least two and all nonreal one-dimensional characters. It makes no claim about zeta itself or quadratic characters. See [the prime-order version](../../../reports/2026-10-29-prime-cyclic-transfer.md) for the related mechanism and comparisons.

**Inputs:** Ahn–Kwon's [order-at-least-three Hecke zero-free theorem](https://doi.org/10.1016/j.jnt.2014.06.008); Das–Gaba–Lee–Savalia–Wong's [Dedekind zeta Theorem 1.2](https://arxiv.org/html/2506.19319); Stark's low-order holomorphy theorem; the conductor–discriminant formula, class field theory, and full Artin induction. The cited Hecke and Dedekind theorems and their strict/boundary conventions are imported, not reproved here.

## Theorem

Let `K/k` be finite Galois with group `G`, and let `H` be a cyclic subgroup of odd order `m>=3`. Put `M=K^H`, `D=|disc(K/Q)|`, `d=|disc(M/Q)|`, and `phi=phi(m)`. Suppose `[M:Q]>=7`. Every irreducible representation `rho` of `G` either of degree at least two or a nonreal one-dimensional character has a full Artin L-function that is holomorphic and nonzero on

    Re(s)>1 - phi/[15.10 (log D-(m-phi) log d)],
    |Im(s)| < (1/3) tan(pi/8).                         (1)

The region includes `s=1`, with holomorphic continuation there. Every character of H is of odd order, so any one-dimensional representation nontrivial on H is nonreal. Replacing the denominator's parenthesized quantity by `log D` gives a simpler, generally weaker region.

## Proof

Choose a generator `lambda` of the character group of `H` and let `f` be the finite conductor of the associated primitive Hecke character over `M`. Denote `Q=N_(M/Q) f` and `A=d Q`. Every nontrivial power `lambda^j` has conductor dividing `f`, since taking a power cannot shrink the kernel of its local character on any ramification subgroup. Every *faithful* power, of which there are exactly `phi`, has exactly conductor `f`, because raising to a unit modulo `m` does not change a local kernel. Hence the conductor–discriminant formula gives

    D >= d^m Q^phi,
    log A <= [log D-(m-phi)log d]/phi.                 (2)

The region is well-defined: `d>1` by `[M:Q]>=7`, `D>=d^m`, and thus its denominator is positive.

Because `m` is odd, every `lambda^j`, `1<=j<m`, has order at least three. Ahn–Kwon's theorem says its full primitive Hecke L-function is holomorphic and nonzero in `Re(s)>1-1/(15.10 log A_j)` and `|Im(s)|<(1/3)tan(pi/8)`, where `A_j<=A`; nonprincipal finite-order Hecke L-functions are entire. Inequality (2) shows that all these regions contain (1). The class-field identity, including ramified local factors, gives

    zeta_K(s)/zeta_M(s) = product_(j=1)^(m-1) L_M(s,lambda^j).            (3)

The quotient extends holomorphically and nonvanishingly throughout (1). Away from `s=1`, `ord_s zeta_K = ord_s zeta_M`.

The Das et al. theorem gives at most one exceptional real zero of `zeta_M` in `Re(s)>=1-1/(11.51910 log d)`, `|Im(s)|<=1`. If such a zero exists, it is simple by Ahn–Kwon's separate low-height zeta theorem, because this real zero lies within its `1/(2 log d)` region. Since (2) and `D>=d^m` imply

    15.10 [log D-(m-phi)log d]/phi >= 15.10 log d > 11.51910 log d,

region (1) lies inside the cited low-order domain. Thus `ord_s zeta_K<=1` at each `s!=1` in (1). Stark's theorem implies all irreducible Artin L-functions of `K/k` are holomorphic at such an `s`.

At any such point, Artin factorization gives `ord_s zeta_K = sum_rho dim(rho) ord_s L(s,rho)`. All summands are nonnegative by Stark, and their sum is at most one. Thus every irreducible of degree at least two has order zero. This degree argument covers all such irreducibles, whether or not `H` acts nontrivially. A nonreal one-dimensional character χ and its distinct conjugate χ̄ have conjugate L-values on the real axis. If L(s,χ) vanished at a point of the region, then ζ_K would vanish there as well, and its only possible zero is real; L(s,χ̄) would also vanish there, forcing order at least two. Hence nonreal one-dimensional L-functions are zero-free regardless of their restriction to H.

For each `j`, the nonzero Hecke L-function on the right side of (3) equals the Artin L-function of `Ind_H^G lambda^j`. Its irreducible constituents occur with nonnegative integer multiplicities; after Stark supplies their holomorphy, none can vanish at `s`. Every irreducible representation nontrivial on `H` contains some nontrivial `lambda^j` in its restriction, so Frobenius reciprocity covers it. At `s=1`, Brauer induction, nonvanishing of nontrivial finite-order Hecke L-functions at one, and Frobenius reciprocity show that a nontrivial irreducible Artin L-function is holomorphic and nonzero. The proof does not assert the same for the trivial Artin representation, whose pole at one is allowed outside the covered class.

## Stronger input when no character has order 3

If the least prime factor of `m` is at least five, every nontrivial `lambda^j` has order at least five. The Ahn–Kwon constant `0.1149` quoted in [Zaman 2016, equation (1.1)](https://arxiv.org/html/1502.05679), valid for `|Im(s)|<=0.13`, may then replace `1/15.10`. Intersecting with the same low-order region yields

    Re(s) > 1 - min{ 0.1149 phi/[log D-(m-phi)log d],
                       1/[11.51910 log d] },
    |Im(s)|<=0.13.                                      (4)

The explicit subregion with width `min{0.1149 phi, m/11.51910}/log D` follows from `d^m<=D` and `log D-(m-phi)log d<=log D`. This intersection with the low-order condition is essential. When `m` has a factor 3, the quotient includes order-three Hecke characters, so the order-at-least-five input cannot be applied to all factors.

Even orders require a different argument: the order-two character of `H` is real and may have an exceptional zero, so the nonvanishing of the entire quotient (3) does not follow from the nonreal Hecke theorem. The odd subgroup of an even cyclic group may still be used, but it covers only representations nontrivial on that odd subgroup.

**What was checked:** the local conductor-divisibility argument, discriminant inequalities, arithmetic of the two width comparisons, and the positive induction/low-order transfer. No exhaustive literature search or independent audit of the imported analytic proofs was performed. The result is an elementary extension of the prime-order route, not a claim of external priority.

## Alternating-group illustration

Let `G=A8` and take `H` generated by the disjoint product `(123)(45678)`. Then `|H|=15`, `phi(15)=8`, and `[G:H]=1344`. Since `A8` is simple, the normal closure of this nontrivial subgroup is all of `G`. Thus every nontrivial irreducible Artin L-function for an `A8`-Galois extension `K/k` satisfies the simpler discriminant region

    Re(s)>1-1/[1.8875 log D],
    |Im(s)|<(1/3)tan(pi/8).

This is twice the width of the simplified `3.775 log D` denominator obtained from a 5-cycle by the prime-order construction. It is a comparison of these two derived bounds, not a claim of best-known status; the exact intermediate-field denominators can also be compared separately.

More generally, for `n>=8` select disjoint cycles of lengths `3` and `p`, where `p>=5` is a prime at most `n-3`. Their product belongs to `A_n`, has order `3p` and totient `2(p-1)`, and its nontrivial normal closure is `A_n`. All nontrivial irreducibles are therefore covered with simplified denominator `15.10/[2(p-1)] log D`. For `n=8` take `p=5`; for `n>=9`, Bertrand's postulate supplies a prime `p>(n-3)/2` with `p<=n-3`. Thus one can choose a denominator strictly smaller than `15.10/(n-5) log D`. These statements use the preceding theorem and make no worldwide novelty claim.

## Many disjoint odd-prime cycles

For every `n>=8`, define

    r = floor(log_2(n+8)) - 3 >= 1.

For each `i=2,...,r+1`, Bertrand's postulate supplies a prime `p_i` with `2^i < p_i < 2^(i+1)`. These primes are distinct and at least five. Moreover

    sum_i p_i < sum_(i=2)^(r+1) 2^(i+1) = 2^(r+3)-8 <= n.

Choose disjoint cycles of lengths `p_i` in `A_n`. Their product generates an odd cyclic subgroup `H` of order `m=product_i p_i`, and

    phi(m)=product_i(p_i-1) >= 2^(sum_(i=2)^(r+1) i)
                              = 2^(r(r+3)/2).

Each cycle is even. The nontrivial subgroup `H` has normal closure `A_n`, because `A_n` is simple for `n>=5`, and `[A_n:H]>=7`: otherwise the coset action would give a nontrivial homomorphism from `A_n` into `S_6`, necessarily injective by simplicity, impossible since `|A_n|>=|A8|>6!`. Hence `[K^H:Q]>=7` for every `A_n`-Galois extension `K/k` of number fields. The theorem applies to **every nontrivial irreducible** and yields, with absolute discriminant `D=|disc(K/Q)|`, the explicitly weaker but uniform region

    Re(s)>1 - 2^(r(r+3)/2)/(15.10 log D),
    |Im(s)|<(1/3)tan(pi/8).

Every prime divisor of `m` is at least five, so the `0.1149` input also gives the smaller-height region

    Re(s)>1 - 2^(r(r+3)/2)/(11.51910 log D),
    |Im(s)|<=0.13.

For the latter, the coefficient in (4) is at least `phi(m)/11.51910`: indeed `m>=phi(m)` and `0.1149>1/11.51910`. The displayed bound follows from the lower bound for `phi(m)`. Both formulae are simplified subregions of (1) and (4); their denominators do not include the potentially sharper intermediate-field discriminant. As `n` grows, `2^(r(r+3)/2)` eventually exceeds every fixed power of `n`. This is a growth statement for the coefficient of `1/log D`, not a claim of a constant-width or globally new zero-free half-plane.
