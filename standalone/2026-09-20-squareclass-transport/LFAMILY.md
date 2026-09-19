# STC26 L-family result: all inert-square factors are inexpensive to remove

**Proposed component proofs for independent review. No GRH conclusion.**
This continues #738 through its explicitly declared CM CUBIC-twist extension;
it does not turn that programme's original quadratic twists into cubic ones.
The construction below is arithmetic preprocessing of reciprocal coefficients,
not a new family of automorphic twists.

## 1. The local fact and the correct normalization

For E_m: y^2=x^3+m^2/4, at an odd good prime p not dividing 3m with p=2 mod 3,
cubing permutes F_p. Therefore the sum of quadratic characters of
x^3+m^2/4 is zero, #E_m(F_p)=p+1, and a_p=0. The arithmetic-normalized
reciprocal local factor is

$$1-a_pT+pT^2=1+pT^2.\tag{1}$$

This is the same local input used in PET26/SBC26; no new point-count theorem
is claimed. Good inert primes have NO degree-one reciprocal coefficient.
In unitary normalization the factor is 1+T^2. These conventions must not be
mixed: the exact fixtures below use the arithmetic coefficient +p at p^2.

The new observation for this programme is quantitative: at the central
energy exponent, the cost of a p^2 insertion is 1/p, not 1/sqrt(p). This
allows an ENTIRE growing inert bank, not merely primes of polylogarithmic
size, to be restored inexpensively.

## 2. Uniform deletion and restoration on the full finite observation interval

Let I be any finite set of odd good inert primes, and let v be the reciprocal
source with those local factors removed. Thus v(n)=0 when any p in I divides
n; all other Euler factors, including bad primes, remain in v. For a signature
epsilon in {+1,-1}^I, define

$$\nu_\epsilon(n)=\sum_{d\mid P_I,\ d^2\mid n}
 \epsilon(d)d\,v(n/d^2),\qquad P_I=\prod_{p\in I}p.\tag{2}$$

The native source is epsilon=+1. The sign variants are AUXILIARY sequences,
not genuine quadratic twists: a quadratic character has chi(p^2)=1 and
cannot produce these independent signs.

For arithmetic coefficients use the center-one energy

$$\mathcal E_1(a;X)=\int_1^X\left|\sum_{n\le x}a(n)\right|^2\frac{dx}{x^3}.$$

This is NOT the zeta dx/x^2 energy. Put

$$B_+(I)=\prod_{p\in I}(1+1/p),\qquad
 B_-(I)=\prod_{p\in I}(1-1/p)^{-1}.$$

**STC26-L1.** For every v, X, I and signature,

$$\boxed{B_-^{-2}\mathcal E_1(v;X)\le
 \mathcal E_1(\nu_\epsilon;X)\le B_+^2\mathcal E_1(v;X).}\tag{3}$$

Proof. Set f_a(t)=e^{-t}sum_{n<=e^t}a(n), zero at negative time, on
0<t<log X. The dilation U_d f(t)=d^{-1}f(t-log d) has norm at most d^{-1}.
Equation (2) is the exact operator product

$$f_{\nu_\epsilon}=\prod_{p\in I}(1+\epsilon_p pU_{p^2})f_v.$$

Each pU_{p^2} has norm at most 1/p, so the forward norm is at most B_+.
Its inverse is the causal geometric series in -epsilon_p pU_{p^2}; the
absolute norm sum is at most (1-1/p)^{-1}. These inverses are exact on the
finite interval: sufficiently long shifts act as zero. Multiplying bounds
and squaring proves (3). No coefficient-size, rank or zero assumption enters.
No completion after the observation endpoint is silently identified. QED.

The same proof in unitary normalization uses e^{-t/2} and dx/x^2, with
coefficient one at p^2, and gives precisely the same B_+,B_-.

## 3. An exponentially large auxiliary family with constant-cost averaging

Define A_I(X) as the uniform average of the energies in (3), and put
D_I=product_{p in I}(1+1/p^2). Orthogonality of the signs in (2) gives

$$\boxed{A_I(X)=\sum_{d\mid P_I,\ d^2<X}\frac1{d^2}
 \mathcal E_1(v;X/d^2).}\tag{4}$$

The d^{-2} is essential. Squaring the arithmetic coefficient d gives d^2,
while changing x=d^2u in dx/x^3 contributes d^{-4}. There is no omitted
family-cardinality factor and no integer rounding of X/d^2.

By positivity and monotonicity,

$$\mathcal E_1(v;X)\le A_I(X)\le D_I\mathcal E_1(v;X),\qquad
 D_I\le\prod_p(1+p^{-2})=15/\pi^2.\tag{5}$$

Consequently the NATIVE member can be recovered from the average:

$$\boxed{\mathcal E_1(\nu_+;X)\le B_+^2 A_I(X),\quad
 A_I(X)\le D_I B_-^2\mathcal E_1(\nu_+;X).}\tag{6}$$

Even a signature chosen to minimize the finite energy is comparable:

$$\mathcal E_1(\nu_+;X)\le(B_+B_-)^2
 \min_\epsilon\mathcal E_1(\nu_\epsilon;X).\tag{7}$$

This is a valid individualization step for this restricted family, unlike
the all-rough-prime degree-one sign family in PROOF.md Section 5.
It does not evaluate A_I or the stripped source's energy unconditionally.

## 4. The bank may contain EVERY active good inert prime

Take I={p<sqrt(X): p is odd, p=2 mod 3, p does not divide 3m}.
Every other good inert factor first contributes at or beyond X and is
causally irrelevant on this interval. The standard PNT in the fixed
progression 2 mod 3, by partial summation, gives

$$\sum_{p\le z,\ p\equiv2\ (3)}\frac1p
 =\tfrac12\log\log z+C+o(1).$$

Since sum p^{-2} converges,

$$B_+^2=O(\log X),\qquad B_-^2=O(\log X),\qquad
 (B_+B_-)^2=O((\log X)^2).\tag{8}$$

Fixed-curve asymptotics have positive constants. The displayed upper O
bounds can be uniform in m because excluding bad primes only decreases
these products. This uses ordinary fixed-modulus PNT, not GRH. The exact
finite bounds (3)-(7) do not require any prime asymptotic.

Thus the full inert-prime sector can be removed/restored at polylogarithmic
energy cost, and the whole auxiliary sign family can be averaged without
an exponential cardinality penalty. The split-prime source is STILL unknown.
No native all-scale subpower estimate for it has been established here.

## 5. Critical warning: off-center zeros survive, but central rank does not

For arithmetic s with Re(s)>1, define

$$J_m(s)=\prod_{p\text{ good inert}}(1+p^{1-2s}).$$

The product converges absolutely and locally uniformly to a holomorphic
nonzero function in that OPEN half-plane. Initially in the absolutely
convergent L-series region, the stripped reciprocal series equals

$$V_m(s)=\frac{1}{L(s,E_m)J_m(s)}.\tag{9}$$

Equation (9) continues it meromorphically to Re(s)>1. All poles associated
with off-critical zeros on that side persist; no such zero is canceled by
J_m. This statement does NOT include the central boundary s=1.

Indeed the same fixed-progression prime asymptotic gives, for real eta->0+,

$$J_m(1+\eta)\sim C_m\eta^{-1/2},\qquad C_m>0.\tag{10}$$

One derivation is to take logarithms: the terms of degree at least two
have an absolutely convergent limit, while the first terms are
sum_{p good inert}p^{-1-2eta}=(1/2)log(1/eta)+C'_m+o(1), by Abelian
partial summation of the prime reciprocal sum. Exponentiate.

If the actual L-function has analytic rank r, then along that real approach

$$V_m(1+\eta)\sim c_m\eta^{-(r-1/2)},\qquad c_m\ne0.\tag{11}$$

For the Sylvester paper's rank-one curves this is a HALF-ORDER singularity,
not a simple pole. In particular V_m cannot have a meromorphic extension
through s=1 with an integer-order pole. The stripped object is not the
completed elliptic L-function and does not retain its central deflation
rule or functional equation.

**Use the stripped coefficients for energy analysis; restore the Euler
product before applying the prior rank-one Pick/deflation detector.** The
paper's global analytic-rank theorem is imported, not re-proved by this
packet. The off-center statement and the central warning must travel together.

## 6. Relating the two energy normalizations, rather than conflating them

For any arithmetic source a(n), let a_u(n)=a(n)/sqrt(n). Summation by parts
on the finite interval gives, with h=f_a and g=e^{-t/2}sum_{n<=e^t}a_u(n),

$$g(t)=h(t)+\tfrac12\int_0^t e^{-(t-u)/2}h(u)du,$$
$$h(t)=g(t)-\tfrac12\int_0^t e^{-(t-u)}g(u)du.$$

The causal L1 kernel bounds yield ||g||<=2||h|| and ||h||<=(3/2)||g||.
Thus the two full finite energies are uniformly comparable, but are not
numerically equal. The executed fixtures use only the arithmetic one.

## 7. Exact finite fixture and limits

family.py uses E_17's directly counted good-prime factors at split primes
7,13,19 and every odd good inert prime below 64:
5,11,23,29,41,47,53,59. This is a FINITE Euler model; other split and bad
factors are not modeled. At X=4096 it enumerates all 256 auxiliary signatures,
checks all 1,048,320 coefficient comparisons against a separate square-divisor
assembly, and proves the finite Parseval identity using exact rational
energies, including X/d^2 endpoints. The mixed 5^2*11^2=3025 term is present.
Deleting it, omitting the arithmetic coefficient p, or using the wrong
geometric inverse is not allowed.

The model energies are approximately:
stripped 0.701345323311; native 0.691100504728; averaged 0.736246897177;
minimum 0.686811224503; maximum 0.790293046879.
These are finite algebraic regression values, not energies of the complete
E_17 L-function, nor rank/zero/height computations. The standard Euler and
Parseval ingredients are classical; no new general theory of CM is claimed.
