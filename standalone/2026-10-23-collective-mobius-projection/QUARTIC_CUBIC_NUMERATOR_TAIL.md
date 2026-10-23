# Primitive-sieve tail with the physical cubic numerator

Status: proved component, 23 October 2026. The physical orientation identified in `QUARTIC_PHYSICAL_ORIENTATION.md` requires g_4(k^3,c), not g_4(k,c). This note supplies the corresponding all-physical-row tail. It does not supply a centered spectral estimate for cubic numerators.

Use the same Gaussian conventions and fixed bounded annular W as `QUARTIC_ALL_ROW_SIEVE_AND_TAIL.md`. Let |xi(c)|<=1 be any column weight independent of k, and define

\[
 T_R^{[3]}(k,D)=\sum_c {\xi(c)g_4(k^3,c)\over Nc}W(Nc/D)
                 \sum_{d^2\mid c,\ Nd>R}\mu(d).
\]

For K,D,R>=1, all nonzero physical k satisfy

\[
 \boxed{\sum_{0<Nk\le K}|T_R^{[3]}(k,D)|^2
 \ll_\epsilon(KD)^\epsilon
 \left[{K\over R}+{(KD)^{2/3}\over R^3}
                   +{DK^{1/4}\over R^{7/2}}\right].} \tag{C1}
\]

Fixed ramified and ray data only change constants. If W is supported in [a,b], the tail is identically zero for R>(bD)^(1/4), and also for R>K. As usual the zero row requires separate restoration.

## 1. Exact local branches

Write c=mq, m squarefree, q powerful, (m,q)=1. The coefficient B_R(q) is exactly the same radical divisor sum as in Q8--Q11 of the companion proof. Put p=Npi. At a nonprincipal local modulus pi^e, e>=2 and 4 does not divide e, a nonzero Gauss sum requires

\[
 3v_\pi(k)=e-1.
\]

Thus e=3a+1 with integer a>=1, and 4 does not divide e. The first allowed value is e=7,a=2. The branch has row divisor rho=pi^a, exact valuation a, and normalized magnitude p^-1/2.

At e=4j the Ramanujan identity gives the following two exact terms:

\[
 {g_4(k^3,\pi^{4j})\over p^{4j}}
 =1_{\pi^{\lceil4j/3\rceil}\mid k}
       -p^{-1}1_{\pi^{\lceil(4j-1)/3\rceil}\mid k}. \tag{C2}
\]

Therefore the full branch table is

| Exponent | rho | w |
|---|---|---|
| e=3a+1, 4 does not divide e | pi^a, exact valuation | p^(-1/2) |
| e=4j, first term | pi^ceil(4j/3) | 1 |
| e=4j, second term | pi^ceil((4j-1)/3) | p^(-1) |

No modulus exponent 2 or 3 survives. Every prime occurring nonsquarefreely in c has exponent at least 4. This proves the sharper empty-tail condition from Nrad(q)^4<=Nq<=bD. Every such prime also divides k, which proves the second empty-tail condition.

## 2. Apply the all-row sieve in the actual row

For a fixed branch k=rho*r, the squarefree m factor is

\[
 g_4((\rho r)^3,m)=g_4(1,m)\chi_m(\rho)\chi_m(r).
\]

All rho and CRT phases, xi(mq), and zeros at common primes are fixed column coefficients. The residual local q factor has modulus at most w and may be removed from a positive row norm. The column length is O(D/Nq), its squared coefficient norm is O_W(1), and the physical row length is K/Nrho. Hence Q3 gives exactly

\[
 w^2\left[{K\over N\rho}
 +\left({KD\over N\rho Nq}\right)^{2/3}
 +{D\over Nq}\left({K\over N\rho}\right)^{1/4}\right](KD)^\epsilon. \tag{C3}
\]

This uses the positive character orientation, which is allowed by conjugating the arbitrary coefficients in Q3. It does not sum unrestricted numerator values up to K^3.

For each nonzero k there are divisor-many supported q branches: e<=3v_pi(k)+1, and primes of q divide k. Rowwise Cauchy, including the divisor bound on B_R(q), therefore has only epsilon cost, exactly as in the native proof.

The local masses for the three terms in C3 have leading exponents 2,4,9/2. In detail:

| Branch | exponent in w^2/Nrho | exponent in w^2/(Nrho*Nq)^(2/3) | exponent in w^2/[Nq*(Nrho)^(1/4)] |
|---|---|---|---|
| e=3a+1 nonprincipal | a+1 | (8a+5)/3 | (13a+8)/4 |
| e=4j first | ceil(4j/3) | (2/3)[4j+ceil(4j/3)] | 4j+ceil(4j/3)/4 |
| e=4j second | 2+ceil((4j-1)/3) | 2+(2/3)[4j+ceil((4j-1)/3)] | 2+4j+ceil((4j-1)/3)/4 |

All three minima occur in the first Ramanujan branch j=1, with rho=pi^2. The first nonprincipal branch a=2 is strictly smaller in magnitude in every column. The remaining exponents increase linearly, so each local sum is p^-lambda times a bounded factor 1+O(p^-c), for lambda=2,4,9/2 and a fixed c>0. Fixing the squarefree radical a and summing Na>R gives respectively R^-1, R^-3, R^-7/2 with epsilon loss. This proves C1.

## 3. Conditional reattachment budget

If a separate physical theorem supplies a full vector of squared norm O((KD)^epsilon K), then Cauchy and the inverse prefactor H/D at K=D^2/H give

\[
 (KD)^\epsilon\left[DR^{-1/2}
       +DH^{1/6}R^{-3/2}
       +D^{3/4}H^{3/8}R^{-7/4}\right]. \tag{C4}
\]

The tail squared also belongs in the exact norm difference and is smaller if each displayed term is <=H and 1<=H<=D. With H=D^alpha and R=D^r, the three constraints are

\[
 r\ge2-2\alpha,\qquad
 r\ge\frac23-\frac{5\alpha}{9},\qquad
 r\ge\frac37-\frac{5\alpha}{14}. \tag{C5}
\]

At alpha=14/15 the largest is 4/27. If one additionally postulates a correctly normalized physical low-divisor error H^(2-u)D^(u-1)R^gamma, this cutoff permits gamma<=(9/20)(1-u), with strict slack needed for epsilon losses.

That last low-divisor formula is only an illustrative extra premise. It has not been derived for this physical orientation. In particular, the native DDHL packet formula with numerator k and L=D/sqrt(K) cannot be imported: the direct k^3 representation has numerator scale K^3 and packet parameter D/K^(3/2), and its rows are sparse. Neither C1 nor C4 proves a centered mean, identifies its diagonal, or implies a new zero-free boundary.
