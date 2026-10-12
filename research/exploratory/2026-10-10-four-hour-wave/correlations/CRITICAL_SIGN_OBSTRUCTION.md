# Critical pointwise positivity is stronger than the negative-mass rate

Status: proposed analytic deductions and a conditional sign obstruction;
independent review requested. Scope: the literal critical SHARP source
beta(n)=mu(n)-1_{67|n}mu(n/67), with F(x)=H_1(x) from
../arithmetic/NEGATIVE_MASS.md. RH remains open. A conditional failure of
pointwise positivity does not obstruct the subpower negative-mass criterion.

## 1. Eventual nonnegativity would imply RH and simplicity

The exact Mellin transform is

    M_F(s)=(1-67^{-(s+1/2)})(s+3/2)/[s(s-1/2)zeta(s+1/2)].

Its pole at s=1/2 is removable; it has a simple pole at zero with residue

    a0=-3(1-67^{-1/2})/zeta(1/2)>0.

Suppose F(x)>=0 for all sufficiently large real x. Its negative mass is
then bounded, so the proved positive-transform Landau argument implies RH.
Moreover F is absolutely Mellin integrable on Re(s)>0: the eventual
positive transform converges there, and the bounded initial interval is
entire. Its simple real-axis pole gives

    lim_{sigma downarrow0} sigma M_F(sigma)=a0.

For every real omega, absolute integration and the bounded initial signed
part imply

    |M_F(sigma-i omega)| <= M_F(sigma)+C,  0<sigma<=1,

where C is finite and independent of sigma. Thus sigma M_F(sigma-i omega)
remains bounded. Any multiple nontrivial zero rho=1/2+i gamma would give a
pole of order greater than one at +i gamma. Taking omega=-gamma in the
displayed bound contradicts this pole order.
The numerator cannot cancel: |67^{-rho}|=67^{-1/2}<1, and the remaining
factors are nonzero at every nontrivial zero. Hence eventual nonnegativity
implies both RH and simplicity of every nontrivial zero.

This simplicity conclusion is unconditional as an implication. No simple
zero conjecture or global zero census is used in deriving it.

## 2. A finite nonresonance contract and a positive trigonometric test

Choose N distinct positive critical ordinates gamma_j with simple zeros
rho_j=1/2+i gamma_j. Their exact residues are

    a_j=(1-67^{-rho_j})(rho_j+1)/
        [(rho_j-1/2)(rho_j-1)zeta'(rho_j)].

Fix an integer K>=1. Impose the following explicit finite nonresonance
hypothesis: for every vector k in {-K,...,K}^N, its frequency
omega(k)=sum k_j gamma_j is zero only for k=0; and it equals any positive
or negative nontrivial zero ordinate only for k=+e_j or k=-e_j,
respectively. This is a hypothesis, not a checked property of the zeros.
Linear independence over Q of the complete set of distinct positive
nontrivial zero ordinates implies this contract.

Let

    D_K(t)=1+2 sum_{k=1}^K (1-k/(K+1)) cos(kt)
          =|sum_{h=0}^K exp(iht)|^2/(K+1)>=0.

Choose phases phi_j so Re(exp(i phi_j) conjugate(a_j))=-|a_j|, and set
P(u)=product_j D_K(gamma_j u+phi_j)>=0. The nonresonance hypothesis makes
its constant coefficient one and its coefficients at +/-gamma_j equal
(1-1/(K+1))exp(+/-i phi_j). Every other frequency is a regular point of
M_F on the imaginary axis. If F were eventually nonnegative, section1
would permit the following absolutely convergent Abel average for sigma>0:

    sigma integral_0^infty F(exp u)P(u)exp(-sigma u)du.

The bounded initial signed segment contributes a quantity tending to zero;
the remaining integral is nonnegative. Expand the finite polynomial P and
let sigma decrease to zero. Mellin residues and nonresonance give the limit

    a0-2 K/(K+1) sum_{j=1}^N |a_j| >=0.

(Sign convention: the transform at exp(+i omega u) is M_F(sigma-i omega),
whose residue is the conjugate of a_j for omega=gamma_j.) Therefore the strict
inequality

    2 K/(K+1) sum_j |a_j|>a0

contradicts eventual nonnegativity. F must take negative values at
arbitrarily large real endpoints. This argument does not require a
conditionally convergent explicit formula or an interchange of an infinite
zero sum: P has finitely many terms, however enormous their number.

## 3. A directed finite residue target

The attached checker uses 1000 disjoint exact dyadic intervals to certify
1000 distinct simple critical zeros by opposite Hardy-Z endpoint signs
and a nonzero zeta derivative throughout each interval. The signed
Hardy-Z derivative also proves a unique line crossing in each interval.
The zeta-zero
routine proposes their locations; endpoint signs certify existence. Their
residue enclosures use the entire intervals, rather than treating proposed
root midpoints as exact zeros. It encloses the constant a0 and the complete
finite sum. With K=9, the tested strict margin is greater than 1/50.

The finite arithmetic certificate does not certify nonresonance. The
resulting sign conclusion is conditional on the finite contract above,
or on the usual full linear-independence conjecture. It does not assert an
unconditional negative value of actual F.

## 4. Reconnaissance and remaining gap

critical_scan.cpp uses ordinary long-double Kahan sums and a complete
linear Mobius sieve. It checks both one-sided interval endpoints of
F(x)=4sqrt(x)sum_{n<=x}beta(n)/n-3sum_{n<=x}beta(n)/sqrt(n), and integrates
negative intervals if encountered. The scan through 100000000 found no
negative interval. Its minimum was 1 at x=1; neither result is directed.
Within each interval between jumps the expression is affine in sqrt(x),
so endpoint inspection is complete in exact arithmetic. Floating inspection
is explicitly reconnaissance.

The negative-mass criterion requires only a subpower cumulative rate, not
eventual nonnegativity. Oscillatory critical residues and multiple zeros
remain compatible with that rate. This packet identifies a reason to
pursue quantitative negative-mass control rather than infer a pointwise
positivity conjecture from a large finite scan.
