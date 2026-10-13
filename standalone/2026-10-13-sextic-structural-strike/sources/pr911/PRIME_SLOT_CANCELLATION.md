# Prime-slot phases: exact pair factors and a paid logarithmic cancellation

Status: proved Euler identities, a proved logarithmic bound on a common conjugate Mellin slice, and an explicit conditional trace-to-moment deduction. The independent-frequency trace bound remains open. No new power saving, generalized moment theorem, zero-free line, or RH theorem is claimed.

This continuation preserves the four-hour packet. Its source is the literal October 5 inverse/sextic family, not an arbitrary coefficient extension. The checker authenticates finite algebra and actual residue symbols; it cannot authenticate the open trace estimate.

## P1. Frozen interfaces and the actual leading face

Use the Eisenstein field and the source's primary convention, fixed finite-order Hecke character `nu`, and fixed excluded prime set `S` containing the primes above 2 and 3 and the conductor of `nu`. Set

\[
 \eta_u(n)=\nu(n)\chi_n(u),\qquad
 A_u(X;W)=\sum_{(n,S)=1}\mu_K(n)\eta_u(n)W(Nn/X).
\]

Every character has its literal zero at nonunits. In particular a positive multiple of six in a prime valuation leaves a coprimality mask. This convention is retained throughout.

The upstream source is `/workspace/.riemann-research/sources/qrh11-12.tex`, SHA256 `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`, equations `eq:intro-family` and `eq:ms`. The further frozen interfaces are:

* PR914 `sextic-moment-conductor-core/CONDUCTOR_SECTORS.md`, SHA256 `c160bbb1b1d7c6bcc5514d496ad41f15fd17ea3d36206b0d05cfa0d7d6503983`, Sections 2–7: the actual residual character, principal masks, smooth radial row majorant, and signed singleton remainder.
* PR914 `INTERACTION_GRAPH.md`, SHA256 `46ac022dcbeee727689d1f2bc247ec22eae54850dd7e010ff2de35d42e1405c5`, Proposition 1.1: the cubic Gauss interaction graph is complete. Its edges are not removed here.
* PR915 `sextic-critical-core/REFLECTION_SCALAR_AUDIT.md`, SHA256 `17bdce731735412cc463c50c944df9240736e5797282f2c5a4eed5a07b2e21e2`, Sections 2–6: the reflected scalar has an exact cubic-to-quadratic cancellation with supplementary and angular factors retained. That existing cancellation is not asserted as a new result.
* PR916 `all-order-collision-removal/PROOF.md`, SHA256 `c67f2469e2d2dfce91cdf2b70220fa53978091c0756ffac9a676737e00792a3f`, Sections 2–5: formal collision kernels and their sharp phase-erased logarithmic cost. The present pair factorization keeps their complex phases.

For `2k` pairwise coprime squarefree columns on norm intervals comparable to `D`, every occurring prime is a singleton in the full Hermitian tuple. Their total singleton norm is comparable to `D^(2k)`, so this entire face belongs to PR914's critical remainder when `H=D^h`, `h<2k`, and `D` is sufficiently large. The face includes composite columns and their actual Möbius signs. The checker also isolates the smaller eight-prime finite witness; restricting to prime columns does not define the full source polynomial.

## P2. An exact finite Euler polynomial, including moving masks

Fix a prime cutoff `Y`, a squarefree ideal `Q` prime to `S`, and a nonzero row `u`. There are `r=2k` labeled slots, with `k` left and `k` right. Put

\[
 \theta_{i,u}=\eta_u\ (i\le k),\qquad
 \theta_{i,u}=\overline{\eta_u}\ (i>k),\qquad
 z_{i,p}=\theta_{i,u}(p)(Np)^{-s_i}.
\]

Define the finite, entire function of all `s_i`

\[
 \mathcal C_{r,Y,Q,u}(\mathbf s)
 =\prod_{\substack{p\notin S, p\nmid Q\\Np\le Y}}
       \left(1-\sum_{i=1}^r z_{i,p}\right).                 \tag{P2}
\]

Its coefficients are exactly the signed allocations of each eligible prime to at most one slot. Consequently it is the multivariate Dirichlet polynomial of pairwise coprime squarefree columns, with coefficient `mu(n_i) theta_i(n_i)` in each slot. A prime dividing `u` has every `z_i=0` and contributes one, rather than a fictitious character value. Exclusion of `Q` deletes the corresponding local factors. No fixed ray phase is replaced by its modulus in this identity.

If every smooth norm test is supported in `[a,b]` and its physical scale is at most `D`, choosing `Y=bD` includes every eligible prime in every nonzero tested column. The finite Euler polynomial also contains columns beyond that norm support; their individual Mellin integrals vanish exactly. Thus finite Mellin inversion of (P2) gives the literal tested coprime face. It requires neither infinite Euler convergence nor an unproved shift through reciprocal-L poles.

## P3. All reciprocal pair factors

For finite cutoffs define

\[
 L_{Y,Q}(s,\theta)=\prod_{p\notin SQ, Np\le Y}
                       (1-\theta(p)(Np)^{-s})^{-1}.
\]

On `Re s_i>0`, the following identity holds exactly:

\[
 \boxed{\quad
 \mathcal C_{r,Y,Q,u}(\mathbf s)
  =\prod_i L_{Y,Q}(s_i,\theta_{i,u})^{-1}
   \prod_{i<j}L_{Y,Q}(s_i+s_j,\theta_{i,u}\theta_{j,u})^{-1}
   \mathcal E_{r,Y,Q,u}(\mathbf s).\quad}                 \tag{P3}
\]

The local remainder is

\[
 E_p(\mathbf z)=
 \frac{1-\sum_i z_i}
 {\prod_i(1-z_i)\prod_{i<j}(1-z_i z_j)}.                 \tag{P4}
\]

There are `binom(2k,2)` pair factors, with no omissions:

* The `binom(k,2)` left pairs have character `nu^2 chi_(.) (u)^2`.
* The `binom(k,2)` right pairs have its conjugate.
* The `k^2` cross pairs have the principal character **with all the original `S,u,Q` prime deletions**. Here `nu bar(nu)=1` at eligible primes. A deleted prime contributes one, not a restored principal Euler factor.

The same-side sextic part is cubic, but an arbitrary fixed `nu^2` ray character remains. Calling the complete character cubic would lose this datum. These are Euler identities before theta reflection; they do not bypass the exact Gauss interaction graph or its ray scalar.

The local degree-one and degree-two terms of `E_p-1` vanish. Its complete degree-three term is

\[
 -\sum_{i\ne j}z_i^2z_j
 -2\sum_{i<j<\ell}z_i z_j z_\ell.                        \tag{P5}
\]

This verifies the signs of the pair factors: they are reciprocal L-factors. Replacing them by positive zeta factors is the phase-erased operation that produced the prior absolute collision cost.

## P4. Unequal-variable absolute region and uniformity

The infinite remainder product converges absolutely and is holomorphic in the domain

\[
 \Re s_i>0,\qquad 2\Re s_i+\Re s_j>1\quad(i\ne j).     \tag{P6}
\]

The inequalities for triples of distinct indices follow from the displayed ordered-pair inequalities. One can equivalently add `Re(s_i+s_j+s_l)>1` without changing this domain. The equal-variable sufficient condition is `Re s_i>1/3`.

Proof: setting all variables but one to zero makes `E_p` identically one. After the canceled degrees one and two, every nonzero monomial therefore contains either `z_i^2 z_j`, `i!=j`, or a three-distinct-variable product. On a compact subset of (P6), these monomials have norm exponent at least `1+delta`, for some `delta>0`; further factors have positive norm exponent. The rational expression (P4) has an absolutely convergent power series when every `|z_i|<1`. For sufficiently large primes its tail is bounded by a constant times the finite sum of those minimal cubic monomials. Hence `sum_p |E_p-1|` converges by elementary ideal counting. The finitely many smaller factors are holomorphic since every denominator has modulus bounded away from zero on compact subsets of `Re s_i>0`. Zeros of the numerator are allowed.

This proof is uniform in the row `u`, the moving mask `Q`, and all imaginary parts on each closed real-part subregion: `|theta_i(p)|<=1`, and deleted primes only remove factors from the absolute coefficient majorant. Derivatives of any fixed order are uniform as well, after adding powers of `log Np` to the convergent majorant. The remainder need not be nonzero everywhere. Holomorphy of the remainder does not eliminate poles of infinite reciprocal L-factors.

For infinite Euler products, (P3) first holds where every `Re s_i>1`. After identifying `eta_u` with the source's imprimitive finite-order Hecke character, it also gives a meromorphic continuation wherever the indicated L-functions are available and the remainder is in (P6). At generic cross hyperplanes `s_i+s_j=1`, the principal reciprocal L-factor vanishes. This is a zero of the exact collision factor; it is not a general cancellation of individual reciprocal-L poles.

## P5. A proved inverse-logarithmic bound on the common conjugate slice

Set all left variables to `1/2+it`, and all right variables to `1/2-it`, for any real `t`. Let `q=Np`, and put `a=eta_u(p) q^(-it)` at an eligible prime. Then `|a|=1`, and the absolute value of the product of **all** local pair factors is

\[
 |1-a^2/q|^{k(k-1)}(1-1/q)^{k^2}
 \le (1+1/q)^{k(k-1)}(1-1/q)^{k^2}
 =(1-1/q)^k(1-1/q^2)^{k(k-1)}
 \le(1-1/q)^k.                                         \tag{P7}
\]

The uniformly absolutely convergent remainder from P4 is bounded by a constant depending only on `k` and the fixed excluded set. Therefore the finite collision factor obeys

\[
 \left|\frac{\mathcal C_{2k,Y,Q,u}}
 {\prod_i L_{Y,Q}(s_i,\theta_i)^{-1}}\right|
 \le C_k\prod_{\substack{Np\le Y\\p\nmid SuQ}}(1-1/Np)^k. \tag{P8}
\]

At a row-prime zero the local ratio is one. This is why the row mask in (P8) is necessary.

The full product is `O_S(1/log Y)` by elementary ideal counting, without a Mertens asymptotic: its reciprocal Euler product contains the positive harmonic sum over every ideal prime to `S` of norm at most `Y`, and that sum is at least `c_S log Y` by the lattice ideal count and partial summation. A norm-budget deletion bound gives

\[
 \prod_{p\mid uQ, p\notin S}(1-1/Np)^{-1}
 \ll_K 1+\log\log(3N(uQ)).                              \tag{P9}
\]

For completeness, the elementary small-prime bound is `prod_(Np<=T)(1-1/Np)^(-1)=O_K(log T)`. To prove it put `delta=1/log T`: the ratio to the product at `1+delta` has logarithm at most `delta sum_(Np<=T) log(Np)/(Np-1)=O_K(1)` by rational Chebyshev and its prime-ideal specialization. The product at `1+delta` is at most `zeta_K(1+delta)=O_K(1/delta)` by ideal counting. These exact inequalities are also frozen in four-hour-wave `arithmetic/MASK_DENSITY_REFINEMENT.md`, R-M1–R-M5, SHA256 `ecddc2ee84fac81d6905663e3f08c7fbff62d54c08f2a01aa402f9e640b98d2c`.

Now split the deleting primes at `T=max(2,log N(uQ))`. The primes at most `T` cost `O(log T)` by that elementary bound. At larger primes, their number is at most `log N(uQ)/log T`; their sum of reciprocals is at most `log N(uQ)/(T log T)`, and the product of their inverse factors is bounded using `-log(1-1/q)<=2/q`. This proves (P9), including bounded norms by changing the constant. No prime-ideal theorem, Mertens asymptotic, RH or quasi-RH hypothesis enters this product bound.

Thus for any fixed `c>0`, uniformly for `N(uQ)<=Y^c`, `Y>=3`,

\[
 \boxed{\quad |\text{collision factor}|\ll_{k,S,c}
     \left(\frac{1+\log\log Y}{\log Y}\right)^k.\quad}   \tag{P10}
\]

This is a paid logarithmic cancellation, in the opposite direction from the phase-erased logarithmic growth. It gives no power saving. It also does not bound the individual finite reciprocal L-factors.

## P6. A concrete off-slice obstruction

The common-frequency condition in P5 is substantive. At a single prime let `k=2`, `x=q^(-1/2)`, and choose left values `z_1=x,z_2=-x`, with conjugate right values `z_3=x,z_4=-x`. These values occur locally by shifting the second Mellin frequency by `pi/log q`. The numerator of (P2) is one, whereas the product of the four single reciprocal-L factors is `(1-x^2)^2`. The local collision factor is therefore

\[
 (1-1/q)^{-2}>1.                                       \tag{P11}
\]

Consequently P10 cannot be imposed on independent Mellin frequencies. Restricting a multi-dimensional Mellin integral to its common-frequency diagonal would change the source norm tests. The complete moment still needs the independent-frequency trace in P8 below.

## P7. A zero-cost radial unit projector

Let `epsilon=zeta_6` be the chosen primitive sixth unit. For every good prime `p`, Euler's definition gives

\[
 \chi_p(\epsilon)=\epsilon^{(Np-1)/6}.
\]

Every good prime norm is `1 mod 6`, including inert prime-ideal norms. For a Hermitian tuple define its unit charge

\[
 c(\mathbf n,\mathbf m)
 =\sum_p(r_p-s_p)(Np-1)/6\pmod6.                       \tag{P12}
\]

For any radial row weight, summing a tuple kernel over a complete unit orbit kills it exactly unless this charge is zero. Its nonunit zeros are unchanged under the orbit, and `chi_p(-1)` is the cube of the displayed unit value, so it is retained as well. The fixed coefficient character `nu` does not vary with the row and does not change this projector.

For squarefree columns the charge can also be calculated from their norms as `sum_left (Nn-1)/6 - sum_right (Nm-1)/6 mod 6`, since products of `1+6c_p` are `1+6 sum c_p mod 36`. This is a finite congruence selection rule. It has no proved polynomial-density saving.

## P8. Precisely priced conditional trace contract

Here is a sufficient analytic target expressed before norm filtering, rather than a restatement of the tested moment. Fix `k`, the source data, fixed norm tests supported in `[a,b]`, and `h=1+theta`, `0<theta<=1/10`. For every `D>=2` put `H=D^h`, `Y=bD`. Consider every eligible exact incidence allocation among the `2k` original Hermitian slots: pairwise coprime squarefree ideals `q_I` for subsets `I` with `|I|>=2`, `c_i=prod_(I contains i) q_I`, `Nc_i<=bD`, and `Q=prod_I q_I`. Then `NQ<=(bD)^k`.

Let `omega_q(u)` be the literal exterior row multiplier `prod_I chi_(q_I)(u)^(r_I) conjugate(chi_(q_I)(u))^(s_I)`, where `r_I,s_I` count left and right slots in `I`. An exponent difference divisible by six still retains the zero mask; it is not replaced by one. Fixed `nu` factors and Möbius signs lie outside the row trace.

**Open contract T(k,h):** for every `epsilon>0` there is a finite `B` and a constant, independent of `D`, all these moving allocations, and independent real frequencies `t_1,...,t_(2k)`, such that

\[
 \left|\sum_{u\ne0}\Phi(u/\sqrt H)\omega_q(u)
 \mathcal C_{2k,bD,Q,u}(1/2+it_1,\ldots,1/2+it_{2k})\right|
 \le C H D^\epsilon\prod_i(1+|t_i|)^B.                 \tag{P13}
\]

Here `Phi` is the fixed smooth radial majorant imported in PR914. The trace has no norm tests or physical length variables inside the finite Euler polynomial. The condition supplies all independent frequencies, the exact incidence exterior multipliers, and the moving masks at the one common row range. It is stronger than a filtered leading-face estimate. A bound only at `Q=1`, only for the common conjugate slice, or only at each smaller column's own row range does not supply P13.

If P13 holds, finite Mellin inversion gives each exact incidence piece an upper absolute row-trace bound

\[
 \ll H D^\epsilon\prod_i(D/Nc_i)^{1/2}
 =H D^{k+\epsilon}\prod_I(Nq_I)^{-|I|/2}.              \tag{P14}
\]

The polynomial frequency cost is integrable against the fixed smooth Mellin transforms. Pair incidences have harmonic sums `O(log D)`; incidences of size at least three have convergent sums. Summing the exact incidence decomposition therefore proves the literal smooth full moment

\[
 M_{2k}^{\Phi}(D,H)\ll H D^{k+\epsilon},               \tag{P15}
\]

after absorbing `log(D)^(binom(2k,2))` into a smaller input loss. The sharp moment is at most the smooth full moment by the majorant. PR914's controlled sectors then give the actual signed smooth `R_k=O(H D^(k+epsilon))`. This conclusion uses the source coefficients and exact allocations; it introduces no arbitrary divisor-bounded coefficient class.

More generally, an additional `D^a`, `a>=0`, on the right of P13 costs exactly `D^a` in P15. The exact all-order family and signed-remainder scope is frozen in four-hour-wave `literature/GENERALIZED_MOMENT_ATTACK.md`, G1–G2, SHA256 `923fac6659314cff53319a80207d1aca7b58d90a154efec4f6de31844f21e94e`. The extraction itself is imported from PR915 `sextic-critical-core/LOG_FREE_REPLICATED_SPIKES.md`, SHA256 `b59978c1c5d3b5cb904c7f22d675a67bb71b2af512db9f0577e568a04565a86b`, Theorem 2.1 and Section 4 equation (4.6): its single fixed Mellin test, every fixed twist, and positive-density sixth-power replicas price such an estimate at the conditional zero-free boundary

\[
 \Re s>\tfrac12+\frac{5h}{12k}+\frac{a}{2k}.           \tag{P16}
\]

Neither P13 nor this new boundary is proved here. P10 saves logarithms on one slice and does not pay the independent-frequency contract.

## P9. Finite native controls and scope

`check_prime_slot_cancellation.py` checks the full multivariate identity through total degree six at `r=2,4,6,8`, including all pair terms and the complete cubic remainder. It reconstructs the actual eight-prime/150-row witness independently from finite fields. It verifies the balanced fourth-slot identity

\[
 L_{\rm distinct}(u)=|F(u)^2-P_2(u)|^2
 -4V(u)|F(u)|^2+8\Re(F(u)\overline{Q_1(u)})
 +2V(u)^2-6E_4(u),                                   \tag{P17}
\]

where `F=sum z_p`, `P_2=sum z_p^2` retains the cubic characters, `V=sum |z_p|^2`, `Q_1=sum z_p |z_p|^2`, and `E_4=sum |z_p|^4`. The left side sums over all ordered four-prime tuples with every prime distinct. This authenticates exact collision subtraction; replacing `P_2` by a nonnegative bound would lose its phase.

The checker also verifies every unit-killed native tuple kernel, the zero mask, finite local pair bounds for actual sixth phases, and the exact off-slice control P11. Its finite results do not establish the infinite product bounds, infinite Euler convergence, T(k,h), or an asymptotic moment saving.
