# Quantitative completion with actual dual and synthesis traces

Status: proposed source-qualified quantitative sharpening; the frozen original
eta theorem and its checker remain unchanged. Scope: a Hilbert-space lemma
for the same complete native decomposition, then an explicit stronger bound
on every real 0<L<=1+10^-36. No new continuum integration is required.

## T-P1. Exact hypotheses

Let q be a continuous Hermitian form, V a subspace, G a linear map to a
Hilbert space, and z_1,...,z_d finite trials. Every h under consideration
must admit h=z_x+v with v in V, z_x=sum_i x_i z_i. The trials need not be
orthonormal. Assume, for every complex x and every v in V,

    q(v,v)>=kappa ||Gv||^2,                 kappa>0;
    |q(v,z_x)|^2<=q(v,v) x*B x,            B positive semidefinite;
    U-B>=epsilon I,                         U_ij=q(z_j,z_i), epsilon>0;
    trace B<=M,                             M>=0;
    sum_i ||G z_i||^2<=K,                   K>=0.

The Gram trace bound implies x*B x<=M||x||^2. Hilbert--Schmidt
Cauchy--Schwarz implies ||G z_x||<=sqrt(K)||x||, including complex x.
There is no requirement M>=1. Completeness of the dual coupling and
finite lower gate remains essential; a finite positive upper section alone
does not meet these hypotheses.

## T-P2. Direct completion

Put a=||x||, c=sqrt(q(v,v)) and d=sqrt(x*B x). These quantities are
real and nonnegative. The complex cross term, the complete coupling bound
and U>=B+epsilon I give

    q(h,h)>=epsilon*a^2+d^2-2*c*d+c^2
           =epsilon*a^2+(c-d)^2.                         (T-P1)

Let r=c-d, which may have either sign. The primitive triangle inequality,
positive-complement bound and d<=sqrt(M)*a give

    sqrt(kappa)||Gh||
      <=sqrt(K*kappa)*a+c
      <=[sqrt(K*kappa)+sqrt(M)]*a+r.                    (T-P2)

The last expression is nonnegative: it bounds the preceding nonnegative
expression. Weighted Cauchy--Schwarz, valid also when r is negative, yields

    kappa ||Gh||^2
      <= [1+(sqrt(K*kappa)+sqrt(M))^2/epsilon]
          [epsilon*a^2+r^2]
      <= [1+(sqrt(K*kappa)+sqrt(M))^2/epsilon] q(h,h).

Consequently

    q(h,h)>=D(epsilon,M,K,kappa)||Gh||^2,
    D=epsilon*kappa/[epsilon+(sqrt(K*kappa)+sqrt(M))^2]. (T-P3)

This is a primitive norm estimate. It introduces no L2 spectral gap or
minimizer assumption. The proof covers x=0, M=0, K=0 and complex tests.

For comparison, optimize the weighted Young route by writing
t=theta/(1-theta). Its coefficient reserve is epsilon-M*t and its
complement reserve is kappa*t/(1+t). The optimal weighted primitive
triangle bound gives

    D^-1 = min_(0<t<epsilon/M)
           [K/(epsilon-M*t)+(1+t)/(kappa*t)].

For M,K>0 its minimizing t is epsilon/[M+sqrt(M*K*kappa)], reproducing
(T-P3). This optimization is explanatory; the direct proof above also
covers the degenerate limits and supplies the acceptance implication.

## T-P3. Source-specific eta consequence

Import the frozen `EXPLICIT_ETA.md`, SHA-256
`55895ae36d87322cdc4ca3424027bcc63e5a020a0803650a7d2e21d215352ff8`,
its checker `b056bc4411acec38a6e81b8c085b8c04d393acc26c1eed931da2b9e604909d70`,
and their explicitly imported complete native source/coupling hypotheses.
For 1<=L<=1+eta, eta=10^-36, that proof gives a decomposition modulo V_L
using the fixed rescaled fourteen trials; its spanning argument does not
require a moving orthonormal frame. It proves kappa=6/5 and the scalar
finite matrix reserve

    epsilon0-(2*10^24)*eta=8*10^-12=epsilon.             (T-P4)

The earlier theorem chose a smaller reserve for convenience. The present
object uses the already proved full 8*10^-12 bound, without changing the
analytic matrix modulus.

The exact original scalar dual trace is below 0.000424, and the complete
native synthesis trace is below 0.514. The frozen analytic trace moduli
are (787500000000000000000000)*eta for B and
(700000000000000000)*eta for synthesis. The fresh outward trace guards
therefore give uniformly

    M=1/2000, K=13/25, kappa=6/5.                     (T-P5)

Both original traces are imported from the exact complete native receipts;
their actual upper dyadic endpoints, all fourteen diagonals and the old
696-panel source artifact remain authenticated by the frozen eta audit.
The sharper caps are new exact rational guards, not ordinary decimal data.

Here M*K*kappa=39/125000<(9/500)^2. Thus the denominator in (T-P3) is
at most epsilon+M+K*kappa+9/250=epsilon+1321/2000<2/3. Since kappa=6/5,
(T-P3) implies the simple rational reserve

    D >= (9/5)*epsilon = 9/625000000000.                (T-P6)

Every complex native h on every real 1<=L<=1+10^-36 consequently obeys

    q_L(h,h)>=9||G_Lh||^2/625000000000.                 (T-P7)

At L=1 the same actual scalar/synthesis trace caps and stronger original
epsilon0=10^-11 give the larger lower constant 9/(5*10^11). Zero extension
from that interval handles every 0<L<=1 with the smaller common constant
in (T-P7). Therefore (T-P7) holds for every 0<L<=1+10^-36.
The primitive G_L is the same injective native Volterra map. The bounded
length, complete gamma source and moving prime-2 activation remain the
frozen eta theorem's exact scope. No sign at log 3, all-window positivity
or RH follows.

## T-P4. General physical-length reuse

The independently directed physical synthesis trace at L=21/20 is less
than 3/5. If its still-pending complete weighted gate supplies epsilon>0,
trace B<=1 and kappa=1/2, then M*K*kappa<=3/10<(11/20)^2 and
the denominator is below epsilon+12/5. For epsilon<1/10, (T-P3) gives
the conservative rational bound D>=epsilon/5. In particular a completed
epsilon=1/20000000000 gate would yield D>=1/100000000000.

If a fresh complete dual-trace guard also gives M<=1/2, then
M*K*kappa<=3/20<(2/5)^2 and the denominator is below epsilon+8/5.
For epsilon<1/15 this gives D>=3*epsilon/10, hence
3/200000000000 at the same conditional epsilon. Neither physical
consequence is accepted from a sampled or incomplete R. It requires the
owner's complete artifact and fresh full weighted acceptance; this note
does not claim that gate has passed.

`check_trace_priced_eta.py` repeats the original frozen eta checker into a
temporary receipt, compares its full output to the frozen receipt, checks
all source hashes, applies the new exact dyadic trace caps, and verifies
(T-P4)--(T-P6) and the conditional rational physical constants with Fraction
arithmetic. Its certificate explicitly distinguishes the analytic proof
from finite guards and from an independent continuum integration.
