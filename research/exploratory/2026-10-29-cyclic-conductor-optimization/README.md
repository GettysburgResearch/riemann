# Order-by-order conductor optimization in cyclic Artin transfer

**Status:** Proposed deterministic sharpening of the cyclic transfer. It is conditional on the same cited Hecke, Dedekind and Stark theorems, not on an unproved analytic estimate. Independent review and a literature search are required; no worldwide priority claim is made.

**Setting and sources:** Use the notation and hypotheses of [the arbitrary-cyclic transfer](../2026-10-29-cyclic-transfer/README.md): `K/k` finite Galois, `H=<h>` cyclic of order `m>=3`, `M=K^H`, `M0=K^(H^2)`, and absolute discriminants `D,d,d0`. The full zero-free theorem there uses Ahn–Kwon's published `1/15.10` coefficient for all nonreal finite-order Hecke characters, the refinements `0.1004` for order four and `0.1149` for order at least five quoted in [Zaman 2016, equation (1.1)](https://arxiv.org/html/1502.05679), and the degree-specific Das–Gaba–Lee–Savalia–Wong constants `C_n`. The present note refines the way different character orders share the fixed discriminant.

## Exact conductor ledger

For each `e|m`, `e>1`, let `f_e` be the conductor of any character of **exact** order `e` of `H`, viewed as a Hecke character over `M`, and set `Q_e=N_(M/Q) f_e`. All characters of exact order `e` have the same conductor: they are powers of one such character by integers coprime to `e`, which preserve its kernel on every local unit and ramification subgroup. If `e|v|m`, then `f_e` divides `f_v`, because the order-`e` character is a power of the order-`v` character.

Consequently the full conductor–discriminant formula is

    R := log D-m log d = sum_(e|m, e>1) phi(e) log Q_e.                (1)

For every nontrivial divisor `e`, put

    W_e = sum_(v|m, e|v) phi(v).

Since `Q_v>=Q_e` whenever `e|v`, (1) gives the simultaneous bound

    log Q_e <= R/W_e.                                                  (2)

Writing `p^a || m` and `p^b || e`, multiplicativity gives the useful closed form

    W_e = m product_(p|e) (1-p^(b-1-a)).                              (3)

To see this, among the `p^a` characters of a cyclic `p^a`-group, exactly `p^a-p^(b-1)` have order divisible by `p^b`; factors at primes not dividing `e` are unrestricted. In particular `W_m=phi(m)` and `W_e>=phi(m)` for every `e|m`.

## Zero-free region at the narrower height

Let `C_n0` be the degree-specific low-order zeta constant in the linked transfer, and assume `[M0:Q]=n0>=2`. For `e>=3` set

    c_3 = 1/15.10,    c_4=0.1004,    c_e=0.1149 for e>=5.

Define

    Delta_H = min_(e|m, e>=3) c_e / [log d + R/W_e],
    Delta   = min{Delta_H, 1/[C_n0 log d0]}.

Then all degree-at-least-two and all nonreal one-dimensional irreducible Artin L-functions of `K/k` are holomorphic and nonzero for

    Re(s)>1-Delta,      |Im(s)|<=0.13,

with the same at-most-one simple real one-dimensional exception and the same pole convention at `s=1` as in the linked cyclic transfer. The proof applies the relevant order-specific Hecke constant to each nonreal character in the factorization `zeta_K/zeta_M0` and then repeats its Das/Stark and regular-representation argument. The minimum over divisors is essential: different character orders can have different conductors and different constants.

If the actual conductors are known, replacing each denominator `log d+R/W_e` by `log(d Q_e)` gives a further valid improvement. They can be recovered from intermediate absolute discriminants. Let `M_v=K^<h^v>` for `v|m`, so `[M_v:M]=v`, and put `L_v=log d_(M_v)-v log d`. The conductor–discriminant identity and Möbius inversion give

    phi(e) log Q_e = sum_(v|e) mu(e/v) L_v.                          (4)

Equation (4) includes the trivial field `M_1=M`, with `L_1=0`. It uses the **actual** conductor norms; it is not a claim that arbitrary nonnegative values satisfying the aggregate inequality are arithmetically realizable.

## Illustration: `m=15`

The nonreal orders are 3, 5, 15. Equation (3) gives `W_3=10`, `W_5=12`, and `W_15=8`. Thus, with `R=log D-15 log d`,

    Delta_H = min{ (1/15.10)/(log d+R/10),
                    0.1149/(log d+R/12),
                    0.1149/(log d+R/8) }
            = (1/15.10)/(log d+R/10).

The last equality follows by cross-multiplication, using `R>=0`: the coefficient `0.1149` and the two denominators make the order-three expression no larger than either order-five expression. The uniform-coefficient argument with the faithful-character bound alone instead gives `(1/15.10)/(log d+R/8)`. Thus this source-derived comparison improves the Hecke part of that particular width by the factor `(log d+R/8)/(log d+R/10)`, between 1 and 5/4. The actual final region remains intersected with the low-order `zeta_M0` region; its gain may therefore be smaller. This calculation does not settle whether a better published region already exists.

**What was checked:** the divisor/character-count identity, conductor monotonicity, inversion formula, and the `m=15` algebra. The existence and zero-free scope of the cited Hecke factors and the Stark step are inherited as stated; no computation of L-functions or independent proof of the analytic inputs was performed.

## Illustration: `m=105` and `A15`

Let `m=105=3*5*7`. Formula (3) gives `W_3=105(1-1/3)=70`; every divisor `e>=5` has `W_e>=W_105=phi(105)=48`. Thus the `e=3` character order supplies

    c_3 W_3 = 70/15.10 = 4.635761589...,

while every other nonreal order supplies at least `0.1149*48=5.5152`. Since `W_e<=m`, (2) implies `log(d Q_e)<=log D/W_e`. Therefore the Hecke part of the zero-free width is at least `70/(15.10 log D)`.

Because `m` is odd, `M0=M`, and `d^105<=D`; in degree at least seven the Dedekind low-order width is at least `105/(11.51910 log D)`, which is larger. The linked transfer therefore gives all its covered irreducibles the region

    Re(s)>1-70/(15.10 log D),     |Im(s)|<=0.13.                    (5)

For comparison, using only the faithful conductor bound and the order-three constant gives width `48/(15.10 log D)`. This is a factor `70/48` improvement of that **specific derived bound**, not a comparison against all previously published theorems.

An explicit example is `G=A15`, with `H` generated by a product of disjoint cycles of lengths 3, 5 and 7. The element lies in `A15`, has order 105, and its nontrivial normal closure is all of the simple group `A15`. The fixed field has degree at least seven: otherwise its coset action would embed the simple group `A15` in `S6`. Hence every nontrivial irreducible Artin L-function of every `A15`-Galois extension `K/k` is holomorphic and nonzero in (5), including at `s=1`. Here `D` is the absolute discriminant of the full Galois field `K`, and no new zeta theorem is claimed.
