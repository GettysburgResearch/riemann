# Actual-Xi heat positivity and every scalar moment at every shift

Status: proposed complete global source theorem, on the exact finite guards
and explicitly imported count-free census stated below. It is a weaker
property than RH; no universal mixed/Hankel or heat-derivative positivity
is asserted.
Scope: the COMPLETE actual-Xi heat trace at every positive time, and its
complete scalar shifted logarithmic moments at every integer order k>=1
and every nonnegative real shift t. All unknown complex zeros and all
multiplicities remain in the source.
Exact dependencies: the reviewed complete Gamma/prime heat identity HT6;
its complete Euler Gaussian tail; the reviewed count-free complete real
census through 5419; an actual selected root in (14,15); the complete
classical strip A=1/2; and the actual theta/Jensen count N(T)<T*log T for
T>=1024, with its native positive xi seed. No historical zero-count routine
or assumed RH input is used by this theorem.
What was actually run: a separate directed checker authenticates the finite
constant guards, source hashes and inherited census scope. Infinite time
and order coverage is proved below; it is not numerical enumeration.
Smallest remaining gap for RH: complete mixed or Hankel positivity, or
complete monotonicity of K itself. Positive Fourier countermodels satisfy
all scalar conclusions below while retaining off-real zeros.

## GS1. Source, heat representation and the two time regions

Retain the complete heat trace K(u)=sum m_rho*exp(-rho^2*u) and the literal
actual Gamma/prime representation HT6 in
[COMPLETE_PRIME_HEAT_TRACE.md](COMPLETE_PRIME_HEAT_TRACE.md). Write

\[
 I_u(q)=\frac{e^{-q}-e^{-q/4-q^2/(16u)}}{1-e^{-q}},\qquad
 S(u)=\sum_{n\ge2}\Lambda(n)n^{-1/2}e^{-(\log n)^2/(4u)}.
\]

Thus the exact complete formula is

\[
 K(u)=e^{u/4}+
      \frac{-\gamma_E-\log\pi+\int_0^\infty I_u(q)dq-2S(u)}
                         {4\sqrt{\pi u}}.
 \tag{GS1}
\]

Fix the rational constants U=1/100000 and delta=1/20. We bound GS1
uniformly for 0<u<=U, then use the complete spectral head/tail bound for
u>=U. Both regions include their common endpoint, so there is no gap in
positive-time coverage.

## GS2. A complete uniform Gamma lower bound at small times

Comparing the two real exponents shows `I_u(q)>=0` whenever q>=12u.
For 0<q<12u, dropping the Gaussian factor from its negative term gives

\[
 I_u(q)\ge\frac{e^{-q}-e^{-q/4}}{1-e^{-q}}
       \ge-\frac34e^{3q/4}.
\]

The last inequality uses `1-exp(-3q/4)<=3q/4` and
`1-exp(-q)>=q*exp(-q)`. Since the exact finite guard gives exp(9U)<2,
the ENTIRE possibly negative region contributes at least -18u>=-18U.

On [delta,1] the positive part has the exact integral

\[
 J=\int_\delta^1\frac{e^{-q}}{1-e^{-q}}dq
     =\log\frac{1-e^{-1}}{1-e^{-\delta}}.
 \tag{GS2}
\]

The subtracted Gaussian integral on that segment is at most

\[
 \frac{1-\delta}{1-e^{-\delta}}e^{-\delta^2/(16U)}
       <20e^{-125/8}.
 \tag{GS3}
\]

Indeed `1-exp(-delta)>=delta/(1+delta)=1/21`, so the first prefactor is
at most 399/20<20. Also delta>12U, so [delta,1] does not meet the negative
region. All discarded intervals outside (0,12u) have nonnegative integrand.
Therefore the COMPLETE Gamma bracket has the uniform lower bound

\[
 -\gamma_E-\log\pi+\int_0^\infty I_u(q)dq
       \ge C:=J-\gamma_E-\log\pi-20e^{-125/8}-18U.
 \tag{GS4}
\]

This is not a truncated integral approximation; its omitted intervals have
the proved sign. A directed finite evaluation encloses C itself.

## GS3. A complete uniform prime upper bound at small times

For the seven integers 2<=n<=8 use Lambda(n)<=log n, n^(-1/2)<=1,
`log n<=log8<3`, and `log n>=log2`. For 0<u<=U their entire contribution
to S(u) is at most `21*exp(-(log2)^2/(4U))`. No prime inventory is presumed
in this deliberately coarse upper bound.

For n>8, replace u by U in the exponential and use the same literal
von Mangoldt bound. The function
`(log x)*x^(-1/2)*exp(-(log x)^2/(4U))` is decreasing for x>=8, because
the finite guard gives log8>2. Integral comparison, q=log x, and log8>4U
give the complete tail

\[
 \begin{split}
 \sum_{n>8}\Lambda(n)n^{-1/2}e^{-(\log n)^2/(4u)}
 &\le\int_{\log8}^\infty q e^{q/2-q^2/(4U)}dq\\
 &\le\int_{\log8}^\infty q e^{-q^2/(8U)}dq
   =4Ue^{-(\log8)^2/(8U)}.
 \end{split}
 \tag{GS5}
\]

Consequently, uniformly on the entire small-time region,

\[
 S(u)\le D:=21e^{-(\log2)^2/(4U)}
                    +4Ue^{-(\log8)^2/(8U)}.
 \tag{GS6}
\]

The directed guard C-2D>0, combined with GS1–GS6, proves

\[
 K(u)\ge e^{u/4}+\frac{C-2D}{4\sqrt{\pi u}}>0
                          \qquad(0<u\le U).
 \tag{GS7}
\]

No finite zero census is used in this small-time source estimate.

## GS4. The whole tail at every remaining time

Use the independently established count-free real head R=5419. Every
source zero with positive real coordinate gamma<=R is real, and there is
an authenticated root gamma_* in (14,15). Its heat contribution is at
least exp(-225u). The COMPLETE unknown tail has gamma>R and |beta|<=1/2.
The r=0 case of the source-count/Stieltjes estimate HD5 gives

\[
 |K_{\rm tail}(u)|\le(R^2+1/u)e^{-u(R^2-1/4)}.
 \tag{GS8}
\]

For clarity, this uses the COMPLETE actual count N(T)<T*log T<=T^2 for
T>=R, not a tail restricted to real zeros. Partial summation retains the
closed-head endpoint with its correct negative sign before discarding it
in the safe direction. This argument is recorded in full in
[FINITE_CENSUS_HEAT_DERIVATIVE_CONE.md](FINITE_CENSUS_HEAT_DERIVATIVE_CONE.md).

The tail/head upper ratio

\[
 B(u)=(R^2+1/u)e^{-u(R^2-1/4-225)}
 \tag{GS9}
\]

is strictly decreasing for u>0: both factors are positive and decreasing,
and R^2-1/4-225>0. The directed finite guard B(U)<1 therefore proves
`|K_tail(u)|<exp(-225u)<=K_head(u)` for EVERY u>=U. Thus K(u)>0 on
the complete large-time region. Together with GS7,

\[
                         K(u)>0\qquad\text{for EVERY }u>0.
 \tag{GS10}
\]

Head completeness is load-bearing. Mere sign existence in a finite list
would not exclude unknown low off-real contributions from the head.
The imported head proof is count-free, with native strict sign facts and
complete logarithmic-moment exclusion; the historical Gram/Rosser complete
count is not an input to that theorem or to this composition.

## GS5. Every scalar complete moment, without a real-spectrum conclusion

The closed complete head is real and the unknown tail has gamma>5419>A.
There are no imaginary-axis roots. Every source node therefore has
Re(rho^2)>0, and outside a finite set it is comparable to |rho|^2.
For every nonnegative real t and integer k>=1, the complete absolute
inverse-square sum pays the Gamma/Laplace interchange:

\[
 \begin{split}
 C_k(t)&=\sum_{\operatorname{Re}\rho>0}
                           m_\rho(\rho^2+t^2)^{-k}\\
       &=\frac1{(k-1)!}\int_0^\infty
                      u^{k-1}e^{-t^2u}K(u)du>0.
 \end{split}
 \tag{GS11}
\]

The sum retains all real and nonreal multiplicities and is real by full
conjugate grouping. This proves strict positivity of EVERY complete scalar
shifted logarithmic moment of ACTUAL Xi at EVERY nonnegative real shift.
At t=0 it gives every unshifted complete scalar moment as well.

Equivalently, `f(X)=d_X log[Xi(i sqrt X)/Xi(0)]` is completely monotone
on X>0, and its normalized integral logarithm is a Bernstein function:
g(0)=0, g>=0 and g'=f is completely monotone. This describes scalar
derivatives of f, not complete monotonicity of K. The latter requires all
heat derivatives and is equivalent to RH by HT7–HT8.

The independently reviewed strictly positive Fourier Bessel/cosine model
in `cofinal-audit/HEAT_POSITIVE_FOURIER_COUNTERMODEL.md` has every property
in GS10–GS11 while retaining a late off-real lattice. It shows why this
actual-source global positivity theorem does not silently settle RH or
the universal Hankel/Hausdorff criterion. No simplicity assertion beyond
the finite inherited census is included.

The finite checker authenticates only its explicit directed constants and
frozen source map. The global transport, complete Euler/count tails and
all-order integral implication are the analytical proof above and require
their own exact-source independent review.
