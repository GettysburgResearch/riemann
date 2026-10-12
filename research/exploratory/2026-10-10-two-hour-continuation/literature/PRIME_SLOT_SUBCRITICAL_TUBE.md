# A power saving for the exact collision factor below the half line

Status: proved source-faithful finite-Euler factor bounds. These are bounds
for the collision factor, not for the individual reciprocal Euler factors
or the full signed moment. No new zero-free boundary is claimed.

## ST1. Frozen factor and domain

Use P1–P4 of `PRIME_SLOT_CANCELLATION.md`, frozen SHA256
`d37ad696b46c7dda15a7faf314c46cda2d7d67e25ac8d3288c7f138aac373c13`.
For the literal source row `u`, moving squarefree exclusion `Q`, cutoff
`Y`, and `2k` labeled Hermitian slots, define the exact finite collision
factor

\[
 \mathcal Q_{2k,Y,Q,u}(\mathbf s)
 =\frac{\mathcal C_{2k,Y,Q,u}(\mathbf s)}
        {\prod_i L_{Y,Q}(s_i,\theta_{i,u})^{-1}}.
\tag{ST1}
\]

All slot real parts below are a fixed `sigma` with `1/3<sigma<1/2`.
Every denominator is nonzero because its local variable has modulus
less than one. P3 factors Q into all reciprocal pair factors and the
remainder E. P4 bounds E uniformly in u, Q, and all imaginary parts,
because `3 sigma>1`. At deleted primes all variables are zero and the
local factor is one. All finite-order `nu` phases remain present.

Write `alpha=2 sigma`, so `2/3<alpha<1`, and assume the norm budget
`N(uQ)<=Y^c` for a fixed `c>0`. Multiplication by a fixed constant in
this budget changes only the constants below.

## ST2. A common conjugate slice pays a polynomial factor

Set every left slot to `sigma+it` and every right slot to `sigma-it`.
The exact local pair bound P7 now holds with `1/q` replaced by
`q^(-alpha)`:

\[
 |\text{all pairs at }p|
 \le (1-q^{-\alpha})^k(1-q^{-2\alpha})^{k(k-1)}
 \le (1-q^{-\alpha})^k.
\tag{ST2}
\]

Elementary ideal counting gives

\[
 \prod_{p\notin S, Np\le Y}(1-(Np)^{-\alpha})
 \ll_{S,\alpha}Y^{-(1-\alpha)}.
\tag{ST3}
\]

Indeed the reciprocal positive Euler product contains every ideal prime
to S of norm at most Y. Their norm interval `[Y/2,Y]` alone contributes
at least `c_(S,alpha) Y^(1-alpha)`, by the fixed-S lattice ideal count.
This proves ST3 without a prime-ideal theorem or product asymptotic.

Every fixed positive `epsilon` also gives

\[
 \prod_{p\mid uQ, p\notin S}(1-(Np)^{-\alpha})^{-1}
 \ll_{\alpha,c,\epsilon}Y^\epsilon.
\tag{ST4}
\]

For sufficiently large prime norms each local factor is at most
`(Np)^(epsilon/c)`. Their product is bounded by `Nrad(uQ)^(epsilon/c)`.
The finitely many smaller primes have a fixed product cost. Assigning
a smaller preliminary epsilon also absorbs any fixed power of this
deletion product.

Combining ST1–ST4 with the uniformly bounded remainder proves

\[
 \boxed{|\mathcal Q_{2k,Y,Q,u}|
 \ll Y^{-k(1-2\sigma)+\epsilon}.}
\tag{ST5}
\]

This is a polynomial saving for the actual finite collision factor on
this slice. It strengthens the endpoint inverse-log bound P10; it does
not bound the complete finite Euler polynomial C.

## ST3. A tube of independent frequencies also pays

Fix `0<=kappa<1/[2(2k-1)]`, a real central frequency t, and write

\[
 s_i=\sigma+i(t+\delta_i)\quad(i\le k),\qquad
 s_{k+j}=\sigma+i(-t+\varepsilon_j)\quad(j\le k),
\]

\[
 |\delta_i|,|\varepsilon_j|\le\kappa/\log Y.
\tag{ST6}
\]

Put `lambda=k[1-2 kappa(2k-1)]>0`. At an eligible prime of norm q,
write `z_i=q^(-sigma) v_i`, `|v_i|=1`. On the unperturbed conjugate
slice the real pair sum is

\[
 \Re\sum_{i<j}v_i v_j
 =k^2+k(k-1)\Re a^2\ge k,
 \quad a=\eta_u(p)q^{-it}.
\tag{ST7}
\]

The inequality `|exp(ix)-1|<=|x|` and `log q<=log Y` show that each
slot changes by at most kappa. Every pair changes by at most `2kappa`.
There are `k(2k-1)` pairs, so throughout ST6

\[
 \Re\sum_{i<j}v_i v_j\ge\lambda.
\tag{ST8}
\]

For `0<x<1`, the absolutely convergent logarithm gives
`log|1-x xi|=-x Re(xi)+O(x^2/(1-x))`, uniformly for `|xi|=1`.
Apply it to each reciprocal pair factor with `x=q^(-alpha)`.
The accumulated error is summable: `2alpha=4sigma>1`. Consequently

\[
 |\text{all pair factors}|\le C\exp\left(
           -\lambda\sum_{\substack{p\notin S, p\nmid uQ\\Np\le Y}}
                              (Np)^{-\alpha}\right)
 \le C\prod_{\substack{p\notin S, p\nmid uQ\\Np\le Y}}
                         (1-(Np)^{-\alpha})^\lambda.
\tag{ST9}
\]

The second inequality uses the same summable quadratic correction between
`log(1-q^(-alpha))` and `-q^(-alpha)`. Small primes contribute fixed
constants; zeros of the numerator are harmless for an upper bound.
ST3, ST4 and the bounded remainder now prove the complete tube estimate

\[
 \boxed{|\mathcal Q_{2k,Y,Q,u}(\mathbf s)|
 \ll_{k,\sigma,\kappa,c,\epsilon}
              Y^{-\lambda(1-2\sigma)+\epsilon}.}
\tag{ST10}
\]

At `kappa=1/[4(2k-1)]`, this exponent is `k(1-2sigma)/2`.
For example at `sigma=2/5`, the common-slice saving is `Y^(-k/5+epsilon)`
and this tube pays `Y^(-k/10+epsilon)`. No restriction is made on the
central frequency t. The tube has nonzero width in all `2k` independent
frequencies, but shrinks as `1/log Y` around one common conjugate pair.

## ST4. What this estimate does and does not price

At the actual source scale `Y=bD`, incidence masks satisfy
`NQ<=(bD)^k`. On any fixed finite row-norm subrange
`Nu<=C D^h`, the norm budget above is met with any fixed `c>h+k`,
for large D. The source spatial majorant Phi is Schwartz and need not
have compact support; its Fourier companion Psi has compact support.
The finite subrange is therefore not the complete source row family.

There is also a weighted version valid for every source row. For any
`epsilon_0>0`, the same local-factor argument proves the deletion cost,
including the fixed power lambda, is at most
`C_(epsilon_0) (Nu NQ)^(epsilon_0)`. With `H` comparable to `Y^h`,
`NQ<=Y^k`, and `epsilon_0<epsilon/(h+k+1)`, ST10 becomes

\[
 |\mathcal Q_{2k,Y,Q,u}(\mathbf s)|
 \ll Y^{-\lambda(1-2\sigma)+\epsilon}
          (1+Nu/H)^{\epsilon_0}
 \quad\text{throughout ST6, for every }u.
\tag{ST11}
\]

The same argument gives the common-slice version with lambda replaced
by k. The polynomial row weight is integrable against the actual
Schwartz majorant, so retaining the entire row tail costs no new power
of Y in this collision-factor bound. This statement still leaves the
individual reciprocal factors and the complementary frequencies unpaid.
The factor bound preserves the exact source coefficients, composite
allocations, norm cutoff, and principal zeros, without an arbitrary
coefficient-class extension.

ST10 gives a literal suppression of the collision factor on a specified
Mellin tube. The remaining individual finite reciprocal Euler factors
can be large. Even at one actual sixth-character value `eta=-1`, the
finite local source polynomial is `1+2k q^(-sigma)>1` although its pair
factors on the conjugate slice are suppressed. A bound for Q alone
cannot bound C by suppressing these individual factors.

The complement of ST6 is also unpaid. At one prime with k=2, left values
`x,-x` and their right conjugates give `Q=(1-x^2)^(-2)>1` for every
`0<x<1`, exactly as in P6. The independent-frequency source Mellin
integral is not concentrated in ST6 by the fixed compact norm tests.
Neither discarding its complement nor shifting an infinite reciprocal-L
contour through zeros is licensed by this finite factor estimate.

The complete trace contract P13 therefore remains open. The new paid
result is ST5/ST10, with the power explicitly attached to the collision
factor and its precise frequency region.
