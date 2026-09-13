# Six exact theta moments in a growth-calibrated connected infinite chain

2026-09-12. **Proposed component proofs and a directed finite existence
certificate. Independent mathematical and implementation review required.
The resulting law is NOT theta, and RH is not proved.**

## 1. What changes relative to the latest work

PR #871 at `43a9eea85e20202370cae4b6ffa1a2c30fc3cfc3` already constructs a
connected infinite chain with an analytic density, the three theta real-field
growth coefficients, and exact second/fourth moments at q=1/5. Its sixth moment
differs. We explicitly reuse and reconstruct its growth mechanism. Neither
that infinite-chain idea nor Lee–Yang closure is claimed new here.

This continuation changes the head architecture and allows a small positive
correlation q. It proves the existence of connected infinite chains matching
moments TWO, FOUR AND SIX while preserving ALL THREE growth coefficients.
The certified numerical root is at q=0; a nonsingular analytic parameter
theorem supplies every sufficiently small q>0. No numerical positive-q radius
is certified. This is not the explicit q=1/5 model of #871, nor an improvement
on #863's degree-fourteen FINITE model in matched order. It improves the
matched order within this complete growth-calibrated infinite construction.

## 2. Fixed theta source and the chain

The source is the unchanged even theta density

    phi(t)=sum_(n>=1)[4pi^2 n^4 exp(9t/2)-6pi n^2 exp(5t/2)]
                         exp(-pi n^2 exp(2t)), t>=0,
    w(t)=phi(t)/integral_R phi,   Phi(z)=Xi(z)/Xi(0).

Let mu_(2r)=integral t^(2r)w(t)dt, and kappa_(2r) its cumulants. The checker
reconstructs these moments from the complete defining source; NUMERICS.md
pays every omitted theta index, spatial lattice, alias and rounding error.
No zero table or predecessor moment receipt enters acceptance.

Take a stationary symmetric Markov sign chain with

    P(sigma_(n+1)=sigma_n)=(1+q)/2,  0<=q<1.

Its finite marginals are zero-field nearest-neighbor Ising ferromagnets with
J=atanh(q); E sigma_i sigma_j=q^|i-j|. For q>0 the ENTIRE chain is connected.
The observable is X=sum a_n sigma_n, constructed as an L2 limit.

Write c=1/2, ell(q)=log((1+q)/2),

    d(q)=7/[8 ell(q)],
    a_n=c/n+d(q)log(n)/n^2,                     n>=32.       (1)

For the first 31 weights use four groups, in this fixed order:

    (25 copies of a, 4 copies of b, 1 copy of c0, 1 copy of e).

Here c0 is a head parameter, not the tail coefficient c. Define

    r(q)=(1-q)/(1+q),
    m_q(u)=sinh(u)/sqrt(sinh(u)^2+r(q)^2),
    C(q)=-1+integral_0^1 m_q(u)/u du
              +integral_1^infinity [m_q(u)-1]/u du,
    S=sum_(n>=32)log(n)/n^2,
    B0(q)=[-log2+C(q)+gamma]/2,
    Btheta=-(1+log(2pi))/2,
    A(q)=Btheta-B0(q)+H31/2-d(q)S.                         (2)

Impose the exact head constraint 25a+4b+c0+e=A(q). All these definitions are
source-independent except the moment targets. No actual zeros define a weight.
For q sufficiently close to zero, the tail in (1) is positive, decreasing,
and lies between 1/(4n) and 1/(2n). For example |d(q)|<1.3 suffices: check
log32/32 and (2log32-1)/32, which decrease afterwards.

## 3. Complete connected limits and real-zero geometry

For every finitely supported real vector v,

    Var(sum v_i sigma_i)<=[(1+q)/(1-q)] sum v_i^2.           (3)

This follows by summing the geometric covariance rows and using
2|v_i v_j|<=v_i^2+v_j^2. Since the a_i are square summable, (3) gives the L2
limit of the ACTUAL connected partial sums, without replacing the tail by an
independent random variable.

The imported classical weighted Lee–Yang theorem applies to every finite
marginal: nonnegative edges and observable weights give only real Fourier
zeros. The paired canonical product of its MGF gives

    E X_N^(2j)/(2j)! <= (Var X_N/2)^j/j!,
    E exp(h X_N)<=exp(Var X_N h^2/2).                       (4)

Uniform variance bounds imply uniform exponential integrability and locally
uniform entire convergence to E exp(izX). Hurwitz, together with the value
one at zero, proves that the limiting Fourier transform has only real zeros.
This classical implication is NOT a conclusion about Xi unless the ENTIRE
limiting law is identified with theta.

The limit also has an analytic density. Condition on all even spins of a
large finite chain. The remaining odd spins are conditionally independent,
with conditional biases at most tanh(2J) in absolute value. For real T, each
odd factor has modulus at most

    exp[-(1-tanh(2J)^2) sin^2(Ta_i)/2].

Choose odd indices in [|T|,2|T|] with |T| sufficiently large. Their phases lie
in [1/8,1/2], and there are a positive constant times |T| of them. The other
factors have modulus <=1. Passing to the infinite chain proves
|E exp(iTX)|<=exp(-c_q |T|) for a positive c_q. Fourier inversion supplies a
nonnegative analytic density on a nonzero complex strip. The constants need
not be optimal or uniform over all q<1.

## 4. All three real-field growth coefficients are retained

This section reconstructs #871's mechanism for our varying q and head.
Let f_q(u)=log lambda_q(u), where

    lambda_q(u)=[(1+q)cosh u+
          sqrt((1-q)^2+(1+q)^2 sinh^2u)]/2.

Then f'_q=m_q, f_q(u)=u+ell(q)+O_q(exp(-2u)) at infinity, and f_q(u)=O_q(u^2)
at zero. The transfer matrices cannot simply be replaced by independent
largest eigenvalues. The required bounded comparison follows as follows.

Let P be the two-by-two transition matrix, v0=(1,1)/sqrt2, and
T(u)=P^(1/2)diag(exp u,exp(-u))P^(1/2). The exact MGF is
v0^T T(ha_1)...T(ha_N)v0. Normalize its Perron vector to (1,tau(u)); direct
calculation shows tau decreases from 1 to
(1-sqrt q)/(1+sqrt q)>0. Comparing T_i times adjacent positive Perron vectors
entrywise bounds the logarithmic error in replacing this product by
product lambda_q(ha_i) by

    log2+sum_i |log(tau(ha_(i+1))/tau(ha_i))|.

The finite head has at most 31 transitions. On the monotone tail the remaining
sum telescopes. Hence

    log E exp(hX)=sum_(n>=1) f_q(ha_n)+O_q(1), h>=0.        (5)

At q=0 it is simply the independent product, so (5) holds there too.

For completeness put g(t)=f_q(1/t)-t^-1 1_(t<=1). It is integrable and of
bounded variation, including its jump at one. Its integral equals C(q) by
integration by parts. The full Riemann sum and harmonic sum therefore give

    sum_(n>=1) f_q(x/n)=x log x+[gamma+C(q)]x+O_q(1).        (6)

In replacing c/n by (1), the first Taylor variation is
hd sum log(n)n^-2 m_q(ch/n). The summed second-order remainder is
O_q(log^2(h)/h), since f''_q(u)<=K_q exp(-2u), all intermediate positive fields
are >=ch/(2n), and the complete sum
h^2 sum log^2(n)n^-4 exp(-ch/n) has that bound.

The functions [m_q(1/t)-1]/t^2 and its product with log t are integrable and of
bounded variation. Their complete Riemann sums, and
integral_0^infinity(m_q(u)-1)du=ell(q), show

    sum_(n>=32)[f_q(ha_n)-f_q(ch/n)]
          =hd(q)S+[d(q)/c]ell(q) log h+O_q(1).             (7)

Replacing the first 31 harmonic weights changes the sum by
h[A(q)-c H31]+O_q(1). Combining (2), (5)–(7) proves

    log E exp(hX)= (h/2)log h
          -[(1+log(2pi))/2]h+(7/4)log h+O_q(1).            (8)

This is precisely the three-term real-field growth of the normalized theta
MGF, by the classical xi formula and real-axis Stirling expansion. It is not
a complex relative error or equality of transforms. Equation (8) also excludes
a nonzero Gaussian convolution factor and implies unbounded support.

## 5. An exact independent seed with six native moments

At q=0, m_0(u)=tanh u. The elementary Mellin identity

    integral_0^infinity u^(s-1)sech^2u du
              =2^(2-s) Gamma(s) eta(s-1)

holds first for Re s>2 by the exponential series and then for Re s>0 by
analytic continuation. Differentiate at s=1 and use
zeta(0)=-1/2, zeta'(0)=-log(2pi)/2, psi(1)=-gamma. Integration by parts gives
C(0)=-1+gamma+log(4/pi). Thus the calibration simplifies exactly to

    d0=-7/(8log2),
    A0=H31/2-gamma-log2-d0 S.                              (9)

The two zeta values are classical DLMF 25.6.1 and 25.6.11 inputs. The numerical
checker evaluates (9) only with rational logarithm and Euler–Maclaurin
bounds; it does not call a zeta or digamma evaluator.

Let T_k=sum_(n>=32)[1/(2n)+d0 log(n)/n^2]^k, and define

    s1=kappa2, s2=-kappa4/2, s3=kappa6/16.

The independent even sign cumulants are c2=1,c4=-2,c6=16. Hence exact moments
through six, together with (9), amount to the four equations

    25a+4b+c0+e=A0,
    25a^(2r)+4b^(2r)+c0^(2r)+e^(2r)=s_r-T_(2r), r=1,2,3. (10)

The exact seed is the unique root in the radius 10^-12 infinity-norm box
about the four terminating rational centers in calibrated_chain.py, displayed
here only approximately:

    a  =0.0221474072944199194546750617255483...
    b  =0.0629420812837275127122815563179909...
    c0 =0.1113970777650096508879646441011078...
    e  =0.0047318790614544977006562261968943....

These are ACTUAL weights, not squared weights. Every group is positive and
the four weights are separated. The complete tail and native theta intervals
produce the following strict directed inequalities for the exact rational
inverse R of the center Jacobian:

    ||R||_infinity <143414,
    ||R F(center)||_infinity <1.183e-21,
    sup_box ||I-R DF||_infinity <4.789e-9,
    beta+L*10^-12 <10^-12.                                (11)

The map x -> x-RF(x) is a contraction into the box. Banach proves the exact
root for the COMPLETE equations, not rounded targets. All 16 inverse identities
and every whole-box derivative entry are reconstructed. See NUMERICS.md for
the complete T_k remainder; no omitted tail is treated as zero.

## 6. The connected six-moment theorem

**Theorem I1.** There is epsilon>0 such that, for EVERY 0<q<epsilon, positive
head weights a(q),b(q),c0(q),e(q) near the certified seed satisfy (2) and match
the actual theta moments 2,4,6 in the complete connected infinite chain.
All odd moments vanish. The conclusions (3)–(8) hold for these same chains.
No explicit numerical epsilon is asserted.

Here are the analytic details needed for the infinite-dimensional part of this
finite parameter argument. For sorted indices, with repetitions allowed,

    kappa(sigma_i,sigma_j,sigma_k,sigma_l)
             =-2q^(k-i+l-j).

For six sorted indices write g1,...,g5 for adjacent gaps. The sixth joint
cumulant is

    4q^(g1+2g2+g3+2g4+g5)(1+3q^(2g3)).                   (12)

The second formula follows by inserting the Markov product moment
E prod_(j=1)^(2r) sigma_(i_j)=q^sum_(j=1)^r(i_(2j)-i_(2j-1)) into the
moment–cumulant partition formula. It covers repeated indices, including the
unit-spin value 16 when all gaps vanish. The finite checker independently
enumerates those partitions and Markov configurations.

For complex |q|<=r0<1 these formulas are bounded by geometric functions of
ALL adjacent gaps. For any fixed gaps, Holder bounds the sum over translations
of an absolute product of 2r weights by sum_i |a_i|^(2r). The latter is locally
uniformly finite in the head parameters and q, since (1) and (2) are analytic
near q=0 and a_i=O(1/i). Summing the geometric gaps proves normal convergence
of the second, fourth and sixth cumulant series and all their parameter
holomorphy. The integrals defining C(q) are analytic in a complex neighborhood
of zero by uniform analytic square-root and exponential tail bounds.

Apply the analytic implicit-function theorem to the head-sum constraint and
the three cumulant constraints, divided by c2,c4,c6. At q=0 their Jacobian is
exactly DF in (11), hence nonsingular. The resulting analytic head parameters
preserve strict positivity in a sufficiently small neighborhood. Every q>0
there gives genuinely positive nearest-neighbor interactions, not disconnected
blocks connected only in a heuristic limit. This proves I1.

## 7. The model is demonstrably not Xi

The same complete calculation evaluates the standardized eighth-moment error
at q=0, while enforcing all lower moments:

    -0.007685169 < [E X^8-mu8]/mu2^4 < -0.007685167.       (13)

The retained interval in results.json is tighter. Because the fourth cumulant
power-sum coefficient is c8=-272, the checker obtains this from the full T8
and the entire root box, not a sampled head value. By continuity, after
shrinking epsilon if necessary, this error remains strictly negative throughout
0<q<epsilon. Therefore EVERY chain in that asserted neighborhood is NOT the
theta law. No numerical bound on that smaller epsilon is asserted either.

The remaining constructive question is target-reaching moment extension at
unbounded orders while preserving positive interactions, complex compactness,
and source identity. A local nonsingular finite-order seed is not that theorem.
The weighted Lee–Yang/entire-limit/Hurwitz ending is complete once an all-order
realizing family exists, but that premise remains OPEN-I.

Primary imports: weighted Lee–Yang and its classical entire closure (Newman–Wu,
arXiv:1901.06596); Jacobi/xi representation; DLMF 25.6.1, 25.6.11 and real-axis
Stirling. The bounded Perron comparison and growth calibration are explicitly
adapted from #871, whose independent mathematical review remains outstanding.
