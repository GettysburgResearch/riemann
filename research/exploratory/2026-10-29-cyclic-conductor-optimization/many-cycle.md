# Many-cycle comparison using order-dependent conductors

**Status:** Proposed arithmetic corollary of the [order-by-order conductor bound](README.md), awaiting independent mathematical and prior-art review. It imports the analytic theorems and low-order transfer recorded there. It concerns a coefficient of `1/log D`, not a fixed half-plane.

Let `n>=11` and put `r=floor(log_2(n+5))-3>=1`. Bertrand's postulate gives primes `p_i` in the disjoint intervals `2^i<p_i<2^(i+1)` for `i=2,...,r+1`. Write `P=product_i p_i`. Since

    3+sum_i p_i < 3+(2^(r+3)-8) = 2^(r+3)-5 <= n,

one may choose disjoint cycles of lengths `3,p_2,...,p_(r+1)` in `A_n`. Their product generates a cyclic subgroup of order `m=3P`. Its normal closure is the simple group `A_n`; the index is at least seven because a smaller coset action would embed `A_n` into `S6`.

In the notation of the linked conductor optimization, `W_3=2P`, while every divisor `e|m` with `e>=5` has `W_e>=phi(m)=2 product_i(p_i-1)`. The order-three Hecke coefficient is `c_3=1/15.10`, while `c_e=0.1149` for `e>=5`. The bound

    product_i (1-1/p_i)
       > product_(i=2)^infinity (1-2^(-i))
       >= [product_(i=2)^6 (1-2^(-i))] (1-1/64)
       = 38757285/67108864
       > (1/15.10)/0.1149

shows `0.1149 W_e > (1/15.10) W_3` for every `e>=5`. The tail product is bounded using `product(1-x_i)>=1-sum x_i`, and `sum_(i=7)^infinity 2^(-i)=1/64`.

Thus the order-three factor determines the conservative Hecke width coefficient `2P/15.10` in terms of the absolute discriminant. The Dedekind low-order cap is no smaller, because `m/11.51910=3P/11.51910>2P/15.10`. Every nontrivial irreducible Artin L-function of every `A_n`-Galois extension `K/k` is therefore holomorphic and nonzero on

    Re(s)>1-2P/(15.10 log D),   |Im(s)|<=0.13,

where `D=|disc(K/Q)|`, including at `s=1`. Since `p_i-1>=2^i` and `P>=product_i 2^i=2^(r(r+3)/2)`, the fully explicit, weaker width `2^(r(r+3)/2+1)/(15.10 log D)` follows.

The previous many-cycle construction omitting the 3-cycle gave a coefficient `2^(r(r+3)/2)/11.51910` with its own `r`; at a **fixed common r**, the new coefficient is larger by `2*11.51910/15.10`. Their definitions of `r` differ (`n+5` versus `n+8`), so that ratio is not automatically a comparison at every fixed `n`. This statement is not an assertion of best-known or externally novel bounds.
