# The polar cancellation includes fourth-power and other local labels

**PROPOSED extension of the polar identity only.** Use the base fixed
Gauss-series section of rStation paper8/v1, with its imported exact
periodicity `rho_full(np^6)=rho_full(n)`. The construction, Gram bounds,
zero retention and tail price are those of `GROWING_RESIDUE_DEBIAS.md`.
No estimate for a new Fourier error is asserted here.

Let R be ANY good sixth-power-free ideal. The polar functional

    sum_a b_D(a) sum_(a|n) rho_prim(nR) Phi(Nn/X)              (1)

is a scalar times

    X^(5/6) (NR)^(-1/6) v(R) Phihat(5/6)
       sum_(g|rad R) c_R(g) F_g,                            (2)

where

    c_R(g)=product_(p|g)(L_(R,p)-1),
    L_(R,p)=1/v(p)            if 1<=ord_p R<=4,
             Np/v(p)         if ord_p R=5.                  (3)

Consequently the EXACT constraints `F_g=0` for every squarefree `Ng<=G`
annihilate every pole (1) with `Nrad R<=G`, including `R=f^4` for all
squarefree `Nf<=G`. These labels have norm at most `G^5`, rather than
norm at most G. This distinction matters in every nonpolar or Gram
estimate; it is not suppressed by calling the radical a label length.

## Constant terms with all valuations

For a full theta coefficient, consider a progression with arbitrary
good modulus A. Reduction of its fractions to primitive denominators
`r|A` gives its small-height constant as

    (NA)^(-1) sum_(r|A) c_[r] (Nr)^(-5/6)
                              sum_(d mod r)^* chi_r(d).    (4)

This is obtained BEFORE any Fourier Gauss evaluation. The factor
`(Nr)^(-5/6)` is essential: the inverse cusp map has height
`1/(Nr*y)`. The character sum in (4) vanishes unless every valuation
of r is divisible by six. Thus only `r=t^6` remain, with unit sum
`phi(t^6)`.

For the stated base section, their cusp constants satisfy
`c_[t^6]=c_[1]`. One can derive this without claiming that every sixth
power is congruent to one modulo an arbitrary deep congruence level.
Indeed the imported coefficient periodicity, applied at progression
`A=t^6`, gives polar density `(Nt)^(-5)`. Comparing this with (4)
and inducting over divisors of t determines each new constant. The
identity

    sum_(d|t) phi(d^6)/(Nd)^5 = Nt

is multiplicative and follows at `p^e` by telescoping
`1+sum_(j=1..e)(q^j-q^(j-1))=q^e`. Divisor inversion therefore gives
the asserted constant equality, including a section whose common
constant is zero.

The full polar density for A is hence

    Delta(A)=1/NA sum_(t^6|A) phi(t^6)/(Nt)^5.               (5)

In the needed case `A=aR`, where a is squarefree and R sixth-power-free,
every valuation of A is at most six. Equation (5) simplifies EXACTLY to

    Delta(aR)=(Na NR)^(-1) product_(p^6|aR) Np.             (6)

As a normalization check, at `A=p^6` the local value is `q^(-5)`,
as required by the full coefficient periodicity. Omitting the cusp
height factor would give a wrong value of order one.

## Primitive density and Boolean closure

Expand the actual primitive weight `w=1*h` as in paper8 Section7.
For any prime already in A, its exponent in `[A,d]` does not change,
since d is squarefree. Thus its local factor is
`(1+h(p))Delta(p^e)`. At a prime absent from A the factor is
`1+h(p)/q`. It follows that

    sum_d h(d) Delta([A,d]) = Z_S v(rad A) Delta(A).         (7)

This is a convergent polar-density computation, with the same
fixed-section residue transfer as in the companion theorem; no uniform
growing-A bound for the nonconstant transforms is inferred.

For `A=aR`, the extra factor in (6) occurs precisely when
`ord_p R=5` and `p|a`. Combine it with
`v(rad(aR))=v(a)v(R)/v((a,R))`. The resulting local factor depending
on a is `L_(R,p)` if `p|a`, and one otherwise. Expanding that product
over divisors of `rad R` proves (2)--(3), with every shared prime kept.

The base section's exact sixth-power periodicity is a hypothesis of
this extension. An arbitrary fixed numerator filter need not retain
that periodicity; the squarefree-R result in the companion file still
holds for the fixed filters stated there. A further extension to such
filters would have to carry their finite cusp constants through (4),
rather than assume the same scalar constants. Growing twists or
separate outer Mellin profiles are not included.
