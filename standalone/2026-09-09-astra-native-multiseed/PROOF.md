# NM26 — removing artificial common zeros from native residual feedback

Date: 2026-09-09. Status: proposed component proofs; independent review required.
**RH and the growing-prefix full-energy upper bound are NOT proved.**
The new result is an explicit three-generator construction for the ORIGINAL
factorial-source domain, plus a quantified obstruction to cheap fixed-bank
polynomial feedback. No new zero-free region or external priority is claimed.

## 1. Source, conventions, and the proposed whole-problem iteration

Let p(s)=sum a_n n^(-s) be a finite real Dirichlet polynomial. Fix an integer
Y>=1 and Q=Y+1, and impose

    a_n=mu(n) for every n<=Y;
    p(1)=0, p'(1)=1, p(0)=-2.                              (1)

mu is the ordinary Mobius function. Coincident indices are combined. Define

    A_p(x)=sum a_n floor(x/n),
    E(p)=integral_1^infinity |1-A_p(x)|^2 dx/x^2,
    G_p(s)=zeta(s)p(s), F_p(s)=1-G_p(s).                    (2)

Balance gives A_p=-sum a_n {x/n}, hence boundedness. Mobius inversion gives
A_p=1 on [1,Q). Termwise integration first for Re s>1 and then uniqueness
of analytic continuation gives

    integral_1^infinity A_p(x)x^(-s-1)dx=zeta(s)p(s)/s,
    integral_1^infinity [1-A_p(x)]x^(-s-1)dx=F_p(s)/s       (3)

on Re s>0. The pole at 1 is removable and G_p(1)=1. Thus F_p(1)=0;
F_p(0)=0 as an analytically continued value, not a convergent integral there.
With s=z+1/2, (3) is a Laplace transform in L2(0,infinity), and Plancherel
fixes the COMPLETE physical norm. No boundary meromorphic expression is
assigned a causal source without this construction.

The candidate mechanism studied here is residual multiplication and polynomial
acceleration. For finitely many seeds p_j obeying (1), write F_j=1-zeta p_j.
Let P_m(w_1,...,w_J) be any polynomial all of whose monomials have TOTAL degree
at least m, with P_m(1,...,1)=1. Set

    R_m(s)=P_m(F_1(s),...,F_J(s)).                         (4)

In Re s>1 each F_j has an absolutely convergent Dirichlet series supported
on indices >=Q. Therefore R_m has such a series sum b_n n^(-s) supported
on n>=Q^m. Let r_m(x)=sum_(n<=x)b_n. This is a locally finite, exact source.
Then r_m=0 below Q^m, and initially its Mellin transform is R_m(s)/s.
Write E_m=integral_1^infinity |r_m(x)|^2 dx/x^2, allowing infinity.
When E_m is finite, Cauchy--Schwarz supplies a holomorphic Mellin transform
on Re s>1/2; the identity with R_m/s extends from Re s>1 by uniqueness.

These iterates generally have INFINITE Dirichlet support. They are not
finite coefficient completions, and their L2 finiteness is NOT automatic.
For a point w=beta+i gamma with beta>1/2 and R_m(w)=1, delayed evaluation gives

    E_m >= (2beta-1) Q^[m(2beta-1)]/|w|^2.                 (5)

The proof is integral_(Q^m)^infinity x^(-2beta)dx
=Q^[-m(2beta-1)]/(2beta-1) in Cauchy--Schwarz. In particular, a sequence
E_m=exp(o(m)) would exclude every right-of-line zeta zero, since all F_j
are exactly 1 at such a zero. Reflection would give RH. We do not prove
that upper bound. The goal is to remove spurious obstructions before trying it.

## 2. NM1: every fixed balanced seed has unwanted recurrent zeros

**Theorem.** For each finite p satisfying (1) and each eta>0, there are
infinitely many nonreal zeros w of p with |Re w-1|<eta and unbounded |Im w|.
They can be chosen simple. Consequently EVERY one-variable feedback (4),
with one fixed seed and arbitrary polynomial degree/coefficients, satisfies

    liminf_(m->infinity) log(1+E_m)/(m log Q) >=1.          (6)

Infinite energies are permitted in this extended-value assertion. It holds
unconditionally and therefore still holds if RH is assumed.

Proof of recurrence. Include all prime factors of the support, and also 2,3,
in a finite list with d primes. For each integer M>=2, simultaneous
pigeonhole approximation of the d-1 numbers log p/log2 (p!=2) supplies

    1<=q<=M^(d-1), |q log p/log2-k_p|<=1/M

for integers k_p. Put T=2pi q/log2. The phase of 2 is exactly one, and for
each supported integer n,

    |exp(-iT log n)-1| <=2pi Omega(n)/M,                  (7)

where Omega counts prime factors WITH multiplicity. Thus p(s+iT) tends
uniformly to p(s) on every compact set as M tends to infinity. The chosen
q tend to infinity along a subsequence: bounded q with errors tending to
zero would make q log3/log2 an integer, contrary to unique factorization.

Since p'(1)=1, choose a small circle about 1 containing precisely that one
simple zero and lying in |Re s-1|<eta. The minimum of |p| on its boundary is
positive. Equation (7) and Rouche give exactly one zero of p(s+iT) inside
for all sufficiently accurate returns. Its translate is a simple zero of
p near 1+iT. Select disjoint disks to get infinitely many distinct zeros.
These are zeros of the FINITE p, not asserted zeros of zeta.

At any such w!=1, F_p(w)=1 and P_m(F_p(w))=1. Apply (5). Taking a fixed
zero with beta>1-eta first, then m to infinity, then eta down to zero,
proves (6). No quantitative Rouche radius or finite zero computation is
needed. Changing coefficients of P_m cannot remove this interpolation
constraint as long as P_m(1)=1. QED.

This rejects scalar polynomial reuse of a fixed balanced seed. It does not
reject choosing a new native seed at each horizon, nor a different control
law which does not have (4). Small initial error is not a closing argument.

## 3. NM2: three arbitrarily close seeds remove all common auxiliary zeros

For an integer H>=Q and r in {2,3}, define

    Delta_(r,H)(s)=H^(-s)(1-r^(1-s))^2(1-r^(-s)).          (8)

Its four coefficients, at H,Hr,Hr^2,Hr^3, are

    1, -(2r+1), r^2+2r, -r^2.                            (9)

In particular Delta(1)=Delta'(1)=Delta(0)=0. For any fixed real epsilon!=0 put

    p_0=p, p_2=p+epsilon Delta_(2,H),
    p_3=p+epsilon Delta_(3,H).                            (10)

**Theorem.** All three seeds preserve every condition (1). Their only common
zero in Re s>1/2 is s=1, where all three zeros are simple. The common zero
divisor of G_0,G_2,G_3 in that half-plane is EXACTLY the actual zeta zero
divisor, with its analytic multiplicities. Moreover

    sqrt(E(p_r)) <= sqrt(E(p))+2(r+1)^2 |epsilon|/sqrt(H). (11)

The perturbations can therefore be made arbitrarily small in the full
physical norm while removing the shared unwanted zero divisor.

Proof. Algebra gives the three zero jets and the support condition.
If all three p_j vanish, both Delta factors vanish. On Re s>1/2 the factor
1-r^(-s) is nonzero. Hence the simultaneous vanishing requires

    (s-1)log2 in 2pi i Z, (s-1)log3 in 2pi i Z.

Unique factorization forces s=1: 3^k=2^l implies k=l=0, including signed
integers. Since the common derivative at 1 is 1, multiplication by zeta
removes those simple zeros and gives G_j(1)=1. At every other point at
least one p_j is nonzero. Consequently a zeta zero of multiplicity m is a
common G zero of minimum multiplicity exactly m. No simplicity of zeta
zeros is assumed.

The Delta profile vanishes below H. Since it is balanced, everywhere its
absolute value is at most the sum of the absolute coefficients, namely
2(r+1)^2. Integration of x^-2 above H and the triangle inequality prove
(11), with the ENTIRE future retained. QED.

### One completely specified bank with E<1/50

SEED.md gives the sixteen coefficients of a rational q and defines exactly

    delta=1-q'(1),
    s0(s)=q(s)+(2delta/log2)3^(1-s)(1-2^(1-s))(1-2^(-s)).  (12)

A new directed full-tail replay proves E(s0)<49/2500. Use p=s0, H=3 and
epsilon=2^(-16) in (10). Then supports are <=16,24,81 respectively, and
all three preserve mu(n) for n<=2, balance, derivative 1 and center -2.
For each member,

    E(p_j)<(7/50+1/2048)^2<1/50.                          (13)

These are specified finite ordinary-arithmetic polynomials with exact real
logarithmic coefficients, not an optimization existence claim. The three
individual norms are bounded by (11); three separate long norm integrals
were NOT computed. No common-zero assertion is inferred from a finite scan.

## 4. NM3: an explicit bounded factorization and the exact original domain

Let H0=L2(0,infinity;dt), with all real causal shifts S_a, a>=0. Define

    d(t)=e^(-t/2)g(t),
    g(t)=floor(e^t)(1-t)+log(floor(e^t)!),
    D(z)=(s-1)zeta(s)/s^2,       s=z+1/2.                 (14)

The elementary expression g=1-{e^t}+integral_0^t{e^u}du proves 0<g<=1+t.
Writing g as sum_(n<=e^t)[1-t+log n] proves its Laplace transform first
for Re s>1; the bound continues it to Re s>0. Hence d belongs to H0 and
L1, and (14) is its actual Laplace transform, not a formal source.

For each finite balanced p_j of support <=N_j set

    h_j(t)=e^(-t/2) A_(p_j)(e^t),
    kappa_j(dt)=sum_n a_(j,n)/sqrt(n) delta_(log n)(dt)
       + e^(t/2) sum_(n<=e^t) a_(j,n)/n dt.               (15)

The density in (15) is zero for t>log N_j by balance. Thus kappa_j is a
finite signed measure supported in [0,log N_j]. Direct transformation gives

    L kappa_j(z)=s p_j(s)/(s-1),
    h_j=d*kappa_j.                                       (16)

The first quotient has its removable value 1 at s=1. One explicit norm
bound for the filter is

    ||kappa_j||_TV <= sum_n |a_(j,n)|/sqrt(n)
                      +2sqrt(N_j) sum_n |a_(j,n)|/n.      (17)

Thus each map f -> kappa_j*f is bounded on the ORIGINAL H0. Formula (16)
is proved in the initial half-plane and then by L1/L2 Laplace uniqueness.
This is a source-preserving bounded map, not an identification of unrelated
positive matrices. Also ||h_j||^2=1+E(p_j), by p_j'(1)=1.

**Theorem.** For the triple (10),

    closure span{S_a h_j:a>=0, j=0,2,3}
                  = closure span{S_a d:a>=0}.             (18)

Under Laplace transformation both spaces are B H2, where B is the pure
Blaschke product of ALL shifted zeta zeros Re rho>1/2, with multiplicity.
No assertion B=1 is made.

Proof. We use classical scalar Hardy inner--outer factorization and the
Beurling--Lax characterization of closed translation-invariant subspaces
[E2]. Each H_j(z)=zeta(s)p_j(s)/s is in H2 by its actual bounded step source.
It is analytic through every finite boundary point Re z=0. Consequently
its inner factor has no singular measure there: ordinary boundary zeros
have finite-order logarithmic singularities, not singular inner mass.
Any singular inner factor must be exp(-az), a>=0, supported at infinity.
But H_j(x)~1/x on the positive real axis because a_(j,1)=1. If a>0, the
outer H2 evaluation bound |O(x)|<=||O||/sqrt(2x), together with the other
inner factors' modulus <=1, contradicts this asymptotic. Thus a=0.
Exactly the same argument applies to D(x)~1/x. These facts also specify
the otherwise important infinite-boundary convention.

For finitely many H2 generators the closed translation-invariant space
is the common inner divisor times H2. This follows by applying the scalar
invariant-subspace theorem to their joint generated space: its defining
inner function divides every generator's inner part and is the greatest
such common divisor. NM2 shows that this common divisor is precisely B.
The factorial transform has exactly the same interior zeros and no singular
inner factor. This proves (18). The direct inclusion from left to right
also follows constructively from (16) and approximation of the compact
measure convolutions by finite combinations of shifts. QED.

The theorem uses ALL real shifts. It does NOT replace them by integer
multiplicative dilations, prove bounded coefficient synthesis, or estimate
a finite-rank approximation rate. It removes EXTRA shared seed zeros;
the original possible zeta obstruction survives unchanged. General cyclicity
and factorization mechanisms are classical, not claimed as new here.

## 5. NM4: no bounded analytic inverse for a fixed normalized seed bank

Fix ANY finite collection satisfying (1), not necessarily the special
triple. Let d>=2 be the number of primes in the union of supports, with
2 and 3 adjoined if necessary, and let Omega count prime factors. Define

    C0=max(1,2pi max_j sum_n |a_(j,n)| Omega(n)/n).         (19)

The same simultaneous approximation as in Section 2 gives, for every
integer M>=2, a time

    0<T<10 M^(d-1), T>1,
    max_j |p_j(1+iT)| <= C0/M.                            (20)

No large coefficients or irrational logarithms are rounded in this paper
statement. It concerns the fixed exact bank.

We need only an elementary zeta upper bound at these safe points. The floor
integral [E1] gives, for integer N>=1 and Re s>0, s!=1,

    zeta(s)=sum_(n<=N)n^-s +N^(1-s)/(s-1)
                 -s integral_N^infinity {x}x^(-s-1)dx.

Take s=1+iT, N=ceil(T), T>=1. The three terms are at most
1+log N, 1/T and sqrt(1+T^2)/N respectively. Therefore

    |zeta(1+iT)|<=4+log(T+1)
                   <=7+(d-1)log M.                      (21)

Equations (20)-(21) prove

    inf_(Re s>1/2) sum_j |zeta(s)p_j(s)| =0.              (22)

Indeed take M to infinity; the recurring T may be taken unbounded as before.
Consequently no functions b_j bounded and analytic on Re s>1/2 can obey

    sum_j b_j(s) zeta(s)p_j(s)=1                          (23)

there. Evaluation at the times (20) proves the contradiction. The same
assertion holds for the compact-filter symbols s p_j(s)/(s-1), whose
moduli are bounded by 2|p_j| at these times. Thus coprimeness in NM2 does
not give a bounded analytic Bezout inverse, even if RH holds.

This does NOT exclude unbounded analytic controllers, polynomially growing
controllers in another norm, unbounded-degree cancellation, or a changing
bank. Nor does it contradict the equality of CLOSED spaces (18).

## 6. Quantitative coefficient cost of every polynomial feedback from the bank

Let P_m be as in (4), of total degree D_m>=m. Define the coefficient mass

    A_m=sum_alpha |coefficient of w^alpha in P_m| >=1.     (24)

Use C0,d above and K=24 C0(d+6). Then every such complete residual satisfies

    E_m >= c_bank Q^m/(1+A_m D_m)^[4(d-1)],               (25)
    c_bank=[404(2K^2)^[2(d-1)]]^(-1)>0.

This explicit constant is deliberately not sharp. The theorem allows
E_m=infinity; it does not prove that high feedback powers belong to L2.

Proof. Choose the integer M=ceil[K^2(1+A_m D_m)^2] and the common return T
from (20). Since log M<=sqrt M for M>=1, (20)-(21) give

    eta:=max_j |G_j(1+iT)|
         <=C0(d+6)/sqrt M <=1/[24(1+A_m D_m)].             (26)

For each monomial of degree l<=D_m, telescoping its l factors gives

    |product_j(1-G_j)^alpha_j -1|
       <=l eta(1+eta)^(l-1)<=D_m eta exp(D_m eta).

Since D_m eta<=1/24, summing absolute coefficient values and using
P_m(1,...,1)=1 proves |R_m(1+iT)-1|<1/12. In particular |R_m|>1/2.
Delayed evaluation at beta=1 now gives

    E_m >= Q^m/[4(1+T^2)]
         >= Q^m/[404 M^[2(d-1)]].                        (27)

Finally M<=2K^2(1+A_m D_m)^2 proves (25). Every phase and the entire
future in (27) are retained; a single boundary sample is NOT substituted
for a norm, since the evaluation point is strictly INSIDE its Hardy domain.
QED.

Two consequences make the stopping point explicit:

* If log(1+A_m D_m)=o(m), then
  liminf log(1+E_m)/(m log Q)>=1, so the proposed subpower finish fails.
* If E_m=exp(o(m)), then necessarily
  liminf log(1+A_m D_m)/m >=log Q/[4(d-1)].

The second statement is a NECESSARY coefficient/degree cost, not a proof
that the required full-norm cancellation is impossible. Exponentially
large coefficients can cancel; their cost cannot be ignored. For (12)-(13)
the bank uses six primes, Q=3, so the displayed necessary rate is log3/20.
No optimality for this exponent is asserted.

## 7. The exact conditional ending remains unpaid

For the triple the unwanted fixed-seed common zeros are removed. If one can
choose feedback polynomials P_m satisfying (4) with full energies E_m=exp(o(m)),
then (5), applied to any actual zero rho with Re rho>1/2, is a contradiction.
This supplies an end-to-end sufficient argument from the one explicit
UNPROVED estimate, without a hidden source change or assumed zero simplicity.

We did not construct such P_m or prove a subpower estimate for independently
chosen finite native minima. The bounded filter factorization (16), equality
of generated spaces (18), small fixed seed errors (13), and removal of common
auxiliary zeros do NOT discharge that estimate. Section 6 identifies a cost
which any successful polynomial-feedback construction must confront.

The attempted advance is qualitative but source-specific: three small native
seeds have exactly the original arithmetic obstruction and an explicit bounded
forward map from the factorial source. The quantitative inverse is still
uncontrolled. This packet is not a completed RH proof awaiting a final routine
check, and it does not reclassify any earlier proposal as accepted.
