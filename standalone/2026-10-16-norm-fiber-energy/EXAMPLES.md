# Concrete consequences, an explicit Euler constant, and limits

Status: consequences of the proposed unconditional component proofs in
THEOREM.md. No new zeta zero-free region is asserted.

## 1. A genuine covariance asymptotic over the Eisenstein field

Take F=Q(omega), omega^2+omega+1=0, with only primes above 2 and 3 excluded.
Use the native principal coefficients mu_F(I), and c=5/6. Let A(X) be the
FULL Gaussian ideal sum of THEOREM.md, not a finite-prime model.

Its sum over distinct ideals of equal rational norm in the cumulative
critical second energy has the positive asymptotic

    C_equal(D) ~ C_E (log D)^2,

    C_E = exp(2/9) pi^2/[432 sqrt(2pi)]
       * product_(p=1 mod 3, p>=7)
           (1+4/p+1/p^2)(1-1/p)^4
       * product_(p=2 mod 3, p>=5)
           (1+1/p^2)(1-1/p^2)^2.                       (E1)

Both products converge to positive numbers; their local factors are
1+O(p^-2). C_equal is the signed cross-ideal subtotal, not a claim about
all unequal norms or the full energy. Its leading constant is not zero.

Derivation. At a split rational prime the norm-collapsed native local
factor is (1-z)^2, so the coefficient-square factor is
1+4p^-s+p^-2s. At an inert prime it is 1-z^2, so the square factor is
1+p^-2s. Since F tensor F=F x F, use zeta_F(s)^2 as the pole factor.
The omitted rational primes 2 and 3 contribute respectively 9/16 and 4/9
to H(1), hence the required finite factor 1/4. The residue of zeta_F is
L(1,chi_-3)=pi/(3 sqrt(3)); for example

    L(1,chi_-3)=integral_0^1 (1-x)/(1-x^3) dx
              =integral_0^1 1/(1+x+x^2) dx=pi/(3 sqrt(3)).

Insert these in NF3 with kappa=2 and
 gamma_c1=exp(2/9)/(2 sqrt(2pi)). The literal ideal diagonal is O(log D),
so subtracting it leaves (E1) unchanged. This reconstruction uses only the
classical quadratic Euler factors and the proved positive Tauberian step.

For the actual coupled and geometric sources the first prime coefficient
is modified by 1-1/q, but the pole order remains two. Their positive leading
constants are the explicit local-square product (10) in THEOREM.md; they
need not equal C_E. Fixed angular phases b_p are permitted. The claimed
asymptotic does not identify those phases with a finite-order character.

## 2. All-order bounded sectors and exactly what the norm gap means

For the Eisenstein field, the complete equal-product-norm block in the
order-2k Gaussian critical energy is O(Z_w(1+log D)^(2k^2)). For Q it is
O(Z_w(1+log D)^(k^2)); for the degree-four Galois field Q(zeta_12) it is
O(Z_w(1+log D)^(4k^2)). These are safe upper bounds, not optimal logarithmic
exponents. They include native, coupled, two-channel and geometric sources.
At the ORIGINAL fixed scale, both the literal Gaussian and every bounded
fixed compact test instead give the corresponding bound

    C Z_w X^k (1+log X)^(kappa k^2),

for the entire equal-product-norm sector, including its absolute tuple sum.
In particular this pays the diagonal POWER at every fixed moment order;
it is not just a cumulative-energy statement.

If all ordered pairs of k-tuples with

    |prod_i NI_i - prod_i NJ_i| <= floor(exp(sqrt(log(2D))))

are retained, their absolute contribution is subpower in D at every fixed
k and fixed F, uniformly in m. This is a statement about the COMPLETE
Gaussian energy with one fixed row measure. It is not a full fixed-scale
moment, a power saving for the dense complement, or a growing-k theorem.
The shift window is small relative to the typical product norm D^k.
For the fixed Gaussian or compact-test moment replace D by X: the selected
absolute sum is O_epsilon(Z_w X^(k+epsilon)), including every tuple with
product-norm gap at most floor(exp(sqrt(log(2X)))). The dense complement is
not part of that bound.

## 3. A native rough-singleton, nonprincipal witness inside the new sector

At rational prime 7, the two Eisenstein prime ideals are represented by
omega=2 and omega=4 modulo 7. The global sixth root zeta_6=1+omega reduces
to 3 and 5 respectively. For u=2+omega (norm 3), its two residues are 4
and 6. The sextic symbols are zeta_6^4 and zeta_6^3; their quotient is
zeta_6, not one. Both symbols are nonzero, and both ideal primes remain
in the mask. Unit phases cancel in the quotient.

At each order take I=(p,...,p) and J=(p,...,p,bar(p)). Their product norms
agree, while the net charges are +1 and -1 at distinct conjugate ideals.
The norm-49 conductor exceeds a norm-7-scale near-linear row height. The
bar(p) singleton is outside the log-square cutoff. This concrete example
shows why norm collision is not the same as principal-character collision.
It does not purport to represent the size of the complete sector.

## 4. Same-norm interference is not always positive term by term

For the coupled source at m=2 and a_p=b_p=1, at a split rational prime 7,
put c=6/7. The two ideal-prime factors give norm-49 coefficient c^2-2.
The square of its collapsed coefficient is 3844/2401. The sum of squared
IDEAL coefficients at that norm is 6098/2401. The equal-norm cross-ideal
subtotal is therefore -2254/2401.

This finite negative term is compatible with NF3's positive cumulative
main term. It rejects both the claim that every norm fiber has positive
cross-ideal interference and the substitution of the ideal diagonal for
the full norm block. The checker verifies these values exactly.

## 5. What the result does not settle

The remaining dense pairs of DISTINCT product norms can carry an energy
of power size. The signed relation between different norm fibers is still
unestimated at the necessary strength. The new theorem supplies no bound
for the theta comparison residual and does not use the unpushed ramified
operator as a dissipative filter. Those are separate problems.
