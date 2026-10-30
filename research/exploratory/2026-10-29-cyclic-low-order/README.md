# A cyclic-subgroup low-order region for all Artin L-functions

**Status:** Proposed consequence of published analytic theorems; independent review and prior-art search requested. The cited theorems are inputs, not reproved. This statement makes no claim of an unconditional fixed half-plane or of a new zeta zero-free region.

**Sources:** Ahn–Kwon, [*Some explicit zero-free regions for Hecke L-functions*](https://doi.org/10.1016/j.jnt.2014.06.008), in particular the order-at-least-three and Dedekind zeta statements in its published abstract; Stark's low-order Artin-holomorphy theorem, stated for example in [Sahu–Wong](https://doi.org/10.1007/s00605-025-02060-7); classical class field theory, full ramified Artin induction, and conductor–discriminant and tower identities. These analytic results have not been reproved here. Compare the wider-height [odd-cyclic route](../2026-10-29-odd-cyclic-transfer/README.md) and [even-cyclic route](../2026-10-29-even-cyclic-transfer/README.md), which use a separate Dedekind estimate.

## Theorem

Let `K/k` be a finite Galois extension of number fields, with group `G`. Let `H<=G` be cyclic of order `m>=2`, `M=K^H`, `M0=K^(H^2)`, and suppose `M0!=Q`. Write

    D=|disc(K/Q)|,  d=|disc(M/Q)|,
    B = [log D-(m-phi(m)) log d]/phi(m).

Then in

    Re(s)>1-1/(15.10 B),
    |Im(s)|<min{(1/3)tan(pi/8), 1/(4B)},                     (1)

`zeta_K` has at most one zero; any such zero is real and simple. Every irreducible Artin L-function of degree at least two and every nonreal one-dimensional Artin L-function of `K/k` is holomorphic and nonzero in (1). The same holds for every nontrivial real one-dimensional Artin factor, apart from at most one possible simple real zero in total. The trivial factor `zeta_k` has its usual pole at `s=1`, and is not asserted holomorphic there. No normal-generation assumption on `H` or condition on the restriction of the representation to `H` is needed.

## Proof

Choose a generator `lambda` of the character group of `H`. Let `f` be its primitive finite conductor over `M`, put `Q=N_(M/Q) f`, and set `A=dQ`. The conductor of each power divides `f`; each of the `phi(m)` faithful powers has the same conductor. The conductor–discriminant and discriminant-tower identities give

    D >= d^m Q^phi(m),       log A <= B.                        (2)

The quantity `B` is positive: if `d>1`, (2) gives `B>=log d`; if `d=1`, then `D>1` since `K!=Q`, and the formula for `B` gives positivity.

Class field theory identifies the full, ramified factors in

    zeta_K(s)/zeta_M(s) = product_(j=1)^(m-1) L_M(s,lambda^j).    (3)

If `m` is odd then `H^2=H`, `M0=M`, and all nontrivial powers of `lambda` have order at least three. If `m` is even, `M0/M` is quadratic, and `zeta_M0/zeta_M` is the factor attached to the unique quadratic power of `lambda`; every remaining nontrivial power has order at least three. Thus, in either case,

    zeta_K(s)/zeta_M0(s) = product_(chi nontrivial on H^2) L_M(s,chi),  (4)

where the product indexes the characters of `H` nontrivial on `H^2`. (For `H=C4`, for example, the quotient uses the two order-four characters; it is irrelevant that `H^2` itself has order two.)

The conductors of the factors in (4) divide `f`, so their `d`-times-conductor norms are at most `A`. Each factor is entire and is zero-free in (1) by the order-at-least-three Ahn–Kwon theorem and (2). Their finite product is therefore holomorphic and nonzero there, including at 1.

It remains to control `zeta_M0`. If `m` is odd, `d_M0=d` and `log d_M0<=B`. If `m` is even, write `Q2` for the finite conductor norm of the quadratic character. Then `Q2<=Q` by conductor divisibility and

    d_M0=d^2 Q2 <= d A,       log d_M0<=2B.                    (5)

Since `M0!=Q`, Ahn–Kwon's Dedekind theorem applies. Its rectangle has

    Re(s)>1-1/(2 log d_M0),   |Im(s)|<1/(2 log d_M0),

and contains (1), because `2 log d_M0<=4B<15.10 B`. It has at most one zero, which is real and simple if it exists. By the nonzero quotient (4), `zeta_K` has the same zeros and multiplicities as `zeta_M0` in (1) away from `s=1`; both have simple poles at 1. This proves the first assertion.

At a point in (1) away from 1, `ord_s zeta_K` is 0 or 1. Stark's theorem makes all irreducible Artin factors holomorphic there. The identity

    zeta_K = product_(rho in Irr(G)) L(s,rho)^dim(rho)

then shows that none of degree at least two can vanish: a zero of one would contribute at least two to the order. At a possible real simple zero of `zeta_K`, a nonreal one-dimensional character and its distinct conjugate have equal orders, so neither can vanish. There can be at most one real one-dimensional constituent with a zero, and that zero is simple. At 1, Brauer induction and nonvanishing at 1 of nonprincipal finite-order Hecke L-functions show every nontrivial irreducible Artin L-function is holomorphic and nonzero: the signed multiplicity of principal Hecke poles is the multiplicity of the trivial representation, namely zero. This completes the proof.

## Scope and comparison

The low-order conclusion applies to **all** irreducibles, including those trivial on the normal closure of `H`: it comes from `zeta_K`, not from a positive induction support argument. The method does not remove a possible real one-dimensional zero, which can include the trivial Artin factor `zeta_k` away from its pole. A group with no nontrivial one-dimensional representations has every nontrivial Artin factor zero-free in (1).

For fixed `H`, using the actual `log A` and `log d_M0` gives a sharper intersection of the two input rectangles. Substituting `B<=log D/phi(m)` gives a simpler region of width `phi(m)/(15.10 log D)` but the safe simultaneous height is then `min{tan(pi/8)/3, phi(m)/(4 log D)}`. Any comparison with the classical Ahn–Kwon zeta-K rectangle must compare both width and height. No global-best or priority claim is made.

**What was checked:** the character-product identity, conductor inequalities, rectangle containments, Stark order argument, and the distinction between real and nonreal one-dimensional characters. The analytic inputs and literature novelty remain independently unaudited.
