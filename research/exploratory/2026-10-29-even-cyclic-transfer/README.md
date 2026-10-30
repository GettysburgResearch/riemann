# Even-cyclic transfer with one possible exceptional point

**Status:** Proposed consequence of the cited classical Hecke, Dedekind and Stark theorems; independent review and prior-art search requested. It does not assert removal of an exceptional real zero and does not use a conjectural fixed half-plane.

**Sources:** Ahn–Kwon, [*Some explicit zero-free regions for Hecke L-functions*](https://doi.org/10.1016/j.jnt.2014.06.008), including the order-two and order-at-least-three results stated in its published abstract; Das–Gaba–Lee–Savalia–Wong, [Theorem 1.2](https://arxiv.org/abs/2506.19319); Stark's low-order Artin-holomorphy theorem, stated for example in [Sahu–Wong](https://doi.org/10.1007/s00605-025-02060-7). We use standard conductor–discriminant, Artin induction, class-field identifications and nonvanishing of nonprincipal Hecke L-functions at 1, including ramified local factors.

## Theorem with an exception

Let `K/k` be finite Galois with group `G`, and let `H` be cyclic of even order `m>=2`. Put

    M=K^H,  d=|disc(M/Q)|,  D=|disc(K/Q)|,
    B = [log D-(m-phi(m)) log d]/phi(m).

Assume `[M:Q]>=7`. For every irreducible complex representation `rho` of `G` on which `H` acts nontrivially, its full Artin L-function is holomorphic and nonzero in

    Re(s) > 1 - 1/(15.10 B),
    |Im(s)| < min{(1/3)tan(pi/8), 1/(4B)},                 (1)

except possibly at one real point `beta_2`. If present, `beta_2` is the unique simple zero in (1) of the primitive quadratic Hecke L-function attached to the unique order-two character of `H`. The statement includes `s=1`. The real point may depend on the extension and may not exist.

In fact, if `beta_2` exists, it is a simple zero of exactly one one-dimensional Artin factor `L(s,nu)`, where `nu|_H` is the quadratic character; every other irreducible Artin factor is holomorphic and nonzero there. Thus every covered irreducible of degree at least two is zero-free throughout (1), and so is every covered irreducible whose restriction to `H` contains a character of order greater than two. If no one-dimensional character of `G` restricts to the quadratic character of `H`—in particular, if `H` is contained in the commutator subgroup—then `beta_2` cannot occur in (1), and all covered irreducibles are zero-free there.

## Proof

Choose a faithful character `lambda` of `H`, with primitive Hecke conductor `f` over `M`, and put `Q=N_(M/Q)f` and `A=dQ`. For each power `lambda^j`, its local conductor divides `f`; for the `phi(m)` faithful powers the conductor is exactly `f`. The conductor–discriminant formula gives

    D >= d^m Q^phi(m),       log A <= B.                        (2)

In particular `B>=log d>0`, since `[M:Q]>=7` implies `d>1`. Let `A_j` denote the corresponding analytic conductor `d` times the finite conductor norm for `lambda^j`. Then `A_j<=A` for every `j`.

For `j != 0,m/2`, `lambda^j` has order at least three. The order-at-least-three Ahn–Kwon estimate gives a holomorphic and nonvanishing full Hecke L-function throughout (1), since `A_j<=A` and `log A<=B`. The unique quadratic factor `L_2` has at most one zero in (1), which is real and simple if present: its Ahn–Kwon order-two rectangle has `Re(s)>1-1/(4 log A_2)` and `|Im(s)|<1/(4 log A_2)`, which contains (1). Denote this possible zero by `beta_2`.

The cyclic zeta factorization, including ramified finite places, is

    zeta_K(s)/zeta_M(s) = product_(j=1)^(m-1) L_M(s,lambda^j).  (3)

For `s` in (1), distinct from `1` and `beta_2`, all factors on the right are holomorphic and nonzero. Consequently `ord_s zeta_K=ord_s zeta_M`. Moreover `15.10 B >= 15.10 log d > 11.51910 log d`, and the ordinate is less than one. The Das et al. theorem therefore makes `ord_s zeta_M` either zero or one there: it admits at most one real zero in the containing region, and that zero is simple by Ahn–Kwon's independent zeta theorem in its `1/(2 log d)` rectangle. Stark's low-order theorem makes every irreducible Artin factor of `K/k` holomorphic at `s`.

Each nontrivial `lambda^j` induces to a genuine character of `G`. Its Hecke L-function is nonzero at `s`; by Frobenius reciprocity its irreducible constituents occur with nonnegative multiplicities, so their holomorphic Artin L-functions cannot vanish at `s`. Every irreducible nontrivial on `H` appears in one of these induced characters. At `s=1`, Brauer induction and nonvanishing at 1 of every nonprincipal finite-order Hecke L-function give holomorphy and nonvanishing of each nontrivial irreducible Artin factor: the signed number of principal poles equals the multiplicity of the trivial representation, which is zero.

Suppose `L_2(beta_2)=0`. Let `M_2=K^{ker(lambda^{m/2})}`, the quadratic subextension of `K/M`. Its zeta function is `zeta_(M_2)=zeta_M L_2` and its absolute discriminant satisfies

    d_(M_2)=d^2 Q_2=d A_2,
    log d_(M_2) <= log d + log A <= 2B.

Thus `beta_2` lies in Ahn–Kwon’s simple-zero rectangle for `zeta_(M_2)`: indeed `15.10 B > 2 log d_(M_2)` and the zero is real. Since `L_2` has a simple zero there, `zeta_M(beta_2)` cannot also vanish; otherwise `zeta_(M_2)` would have a zero of order at least two. Equation (3) therefore makes `zeta_K` have a simple zero at `beta_2`. Stark makes all irreducible Artin factors holomorphic there. In `zeta_K=product_rho L(s,rho)^dim(rho)`, all orders are nonnegative integers with weighted sum one: exactly one one-dimensional factor has a simple zero, and every other irreducible factor is nonzero.

The factor `L_2=L(s,Ind_H^G(lambda^{m/2}))` vanishes at `beta_2`. Its irreducible constituents have nonnegative multiplicities, so the unique vanishing factor `nu` must occur in that induced character. Frobenius reciprocity gives `nu|_H=lambda^{m/2}`. Conversely, a one-dimensional character restricts trivially to any subgroup of `[G,G]`, so the stated group-theoretic condition precludes this possibility and hence the exceptional zero.

## Boundary and comparison

The height in (1) is deliberately small: it is inherited from the unconditional order-two Hecke theorem. The quadratic-intermediate-field argument removes its exceptional point for all higher-dimensional factors and localizes any remaining zero to a single global one-dimensional character; it does not exclude that character's possible real zero. If `H` has an odd-order subgroup, the stronger [odd-cyclic transfer](../2026-10-29-odd-cyclic-transfer/README.md) also applies to representations visible on that subgroup and offers a larger fixed height. No external priority or best-bound claim is made.

**What was checked:** conductor divisibility, the rectangle containments, induction and order algebra. The cited analytic theorems are inputs; no independent reproof or numerical L-function computation was performed.
