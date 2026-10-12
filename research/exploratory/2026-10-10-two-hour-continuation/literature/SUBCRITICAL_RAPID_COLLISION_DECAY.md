# Arbitrary polynomial decay of the exact subcritical collision factor

Status: proved elementary strengthening of the frozen subcritical tube.
This bounds only its collision factor. Individual reciprocal factors,
complementary frequencies, and the literal signed moment remain unpaid.

## RD1. A positive finite Euler product grows faster than any fixed power

Fix the source field K, a finite fixed forbidden-prime set S, and
0<alpha<1. Write

\[
 Z_Y=\prod_{\substack{p\notin S\\Np\le Y}}
                    (1-(Np)^{-\alpha})^{-1},\qquad
 A_Y=\sum_{\substack{Nn\le Y\\(n,S)=1}}(Nn)^{-\alpha}.
\tag{RD1}
\]

The fixed-S ideal lattice count gives A_Y>=cY^(1-alpha) for sufficiently
large Y. This uses no prime-ideal asymptotic. Fix an integer m>=1 and any
delta>0. The expansion of A_Y^m is a positive weighted sum over products
n=n1...nm, each factor of norm at most Y and prime to S. Every product
has norm at most Y^m and all its prime factors have norm at most Y.
Its multiplicity is at most the complete ordered ideal divisor function

\[
 d_m(n)=\prod_{p^e\parallel n}\binom{e+m-1}{m-1}
                \le C_{K,m,\delta}(Nn)^\delta.
\tag{RD2}
\]

For completeness, the binomial coefficient is at most m^e. At primes
with Np>=m^(1/delta) this is at most (Np)^(delta e). There are only
finitely many smaller primes; at each the supremum of the polynomial
in e divided by (Np)^(delta e) is finite. Multiplying those fixed
constants proves RD2 for all ideals, including arbitrary prime powers.

The positive Euler expansion Z_Y contains every product ideal above
with coefficient one, so

\[
 A_Y^m\le C_{K,m,\delta}Y^{m\delta} Z_Y,
 \qquad
 Z_Y^{-1}\le C'_{K,S,m,\alpha,\delta}
                    Y^{-m(1-\alpha-\delta)}.
\tag{RD3}
\]

Choose delta=(1-alpha)/2. For every fixed B>0, choose a fixed integer
m>2B/(1-alpha). This proves

\[
 \boxed{Z_Y^{-1}\ll_{K,S,\alpha,B}Y^{-B}
                       \quad\text{for every fixed }B>0.}
\tag{RD4}
\]

Constants depend on the displayed fixed data and on B. No assertion is
uniform as alpha approaches 1 or S changes with Y. All primes deleted
by the moving source mask are handled separately below, not put into S.

## RD2. Source conjugate slice and independent-frequency tube

Use the exact source factorization P1–P4 and the frozen
`PRIME_SLOT_SUBCRITICAL_TUBE.md`, SHA256
`5aca641b5c58e8d2efaf643c660d98cb5970235478bd9e0622e1d6014c4a1c28`.
Fix 1/3<sigma<1/2, alpha=2sigma, k, and
0<=kappa<1/[2(2k-1)]. The full independent-frequency tube ST6 has
width kappa/logY in every slot around one common conjugate frequency.
Its positive pair floor is lambda=k[1-2kappa(2k-1)]>0.
The absolute degree-three remainder is uniformly bounded because
3sigma>1. ST9 bounds the full pair product by a fixed constant times
the eligible positive Euler product to the power lambda.

For any epsilon_0>0 the moving deletion cost, including lambda, is
bounded by C_(epsilon_0)(Nu NQ)^(epsilon_0), by ST4's large-prime
argument with a smaller preliminary exponent. Applying RD4 with
arbitrarily large B therefore proves, for every fixed A>0,

\[
 |Q_{2k,Y,Q,u}(\mathbf s)|
 \ll_{k,\sigma,\kappa,A,\epsilon_0}
                   Y^{-A}(Nu NQ)^{\epsilon_0}
 \quad\text{throughout ST6}.
\tag{RD5}
\]

If N(uQ)<=Y^c with fixed c, choose B large enough to absorb
c epsilon_0; the norm-budget version is simply |Q|<=C_A Y^(-A).
For the complete source row family, NQ<=Y^k and H comparable to Y^h,
choose B to absorb (h+k)epsilon_0 instead. Then every row satisfies

\[
 \boxed{|Q|\ll_A Y^{-A}(1+Nu/H)^{\epsilon_0}.}
\tag{RD6}
\]

The polynomial norm weight is integrable against the actual spatial
Schwartz majorant. The fixed compact Fourier companion does not make
that spatial majorant compactly supported. No row tail is discarded.
The common conjugate slice is included, with lambda=k.

## RD3. Exact scope and finite controls

This is arbitrary polynomial suppression of the exact collision factor,
uniform in the central frequency and all literal source ray phases.
It is not suppression of the full finite coprime Euler polynomial C:
individual reciprocal Euler factors can compensate or dominate it.
The Mellin tube still shrinks as 1/logY, and the source norm tests do
not force their independent Mellin frequencies into it. Neither those
individual factors nor the tube complement is bounded here. No new
source moment or zero-free boundary is claimed.

The independent analytic check by `final_height_review` accepted the
positive product expansion, the complete divisor multiplicity, the fixed
S quantifier, and RD4. `check_subcritical_rapid.py` supplies finite exact
ordered-product multiplicity controls and directed positive Euler
containment at the source's good prime norms. Finite controls are not
claimed to prove the asymptotic lattice/divisor estimate.
