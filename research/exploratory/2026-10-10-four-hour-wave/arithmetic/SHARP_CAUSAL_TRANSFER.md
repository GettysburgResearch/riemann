# Positive causal transfer from the critical SHARP source

Status: **Root-reviewed component identities C-S1--C-S4 and an exact
two-atom method counterexample.** Root independently accepted the full
analytic proof and source controls and replayed all three groups in both
normal and optimized modes. Literal native beta is retained in the identities;
the counterexample uses an explicitly different finite source. It does
not disprove native critical positivity or RH.

Prior credit: `claims/refutations/R-99930-supercritical-positivity-does-not-cross-the-critical-carrier.md`
already records the general obstruction to reversing positive smoothing
and an exact ladder for the zero-at-activation kernel. This note gives
the real-power causal transfer for T(1)=1, retaining its activation jump.
No general smoothing-firewall novelty is claimed.

## C-S1. The exact positive causal density

For u>=0 put g(u)=4e^(u/2)-3 and g_m(u)=g(u)^m; extend both by zero to
u<0. For every real m>=1 define

    k_m(u)=2(m-1)e^(-3u/2)
       +4m(m-1) integral_0^u e^(-3(u-v)/2)e^v g(v)^(m-2)dv,
       u>=0.

The density is nonnegative, strictly positive for m>1, and zero for m=1.
It is continuous locally, including k_m(0)=2(m-1). Its exact causal
convolution identity is

    g_m=g+ k_m*g.                                         (C-S1)

For a proof retaining the endpoint atom, distributional differentiation
of the zero-extended g gives

    D(D-1/2)g=delta_0'+(3/2)delta_0.

The same operator applied to g_m gives

    D(D-1/2)g_m=delta_0'+(2m-1/2)delta_0
                    +4m(m-1)e^u g(u)^(m-2)1_(u>=0).

Here g_m(0)=1 and g_m'(0)=2m; omitting either boundary value would change
the formula. Meanwhile the displayed k_m solves

    k_m'+(3/2)k_m=4m(m-1)e^u g(u)^(m-2),
    k_m(0)=2(m-1).

Consequently D(D-1/2) applied to g+k_m*g equals the displayed expression
for g_m, including its two atoms. The difference is a zero-initial-data
causal solution of D(D-1/2)h=0 and is therefore zero. Alternatively their
Laplace transforms agree in Re s>m/2 by multiplication with
(s+3/2)/(s(s-1/2)); all functions have finite exponential order there.

## C-S2. Literal native source and positivity direction

Write F(e^u)=H_1(e^u). On every compact causal interval the shifted-source
sum has finitely many terms, so convolution and the native beta sum can
be interchanged without an infinite rearrangement. Applying C-S1 to each
shift u-log n gives

    H_m(e^u)=F(e^u)+integral_0^u k_m(u-v)F(e^v)dv.          (C-S2)

Thus F>=0 on [1,X] implies H_m>=0 on [1,X] for every m>=1. The convolution
term is continuous at each activation, while the jump in both H_m and F
is exactly beta(n)/sqrt(n). This identity does not delete activation atoms
or replace beta by an absolute source.

Pointwise negative parts satisfy

    (H_m(e^u))_- <= F_-(e^u)+(k_m*F_-)(u),

because the convolution kernel is positive. These are implications from
the critical source to its larger powers. They supply no critical sign
from the sign of a larger power.

## C-S3. Quantified finite-horizon persistence near power one

For 1<=m<=2, since g(v)>=1, the formula in C-S1 gives

    0<=k_m(u)<=(m-1)k_2(u),
    k_2(u)=(16/5)e^u-(6/5)e^(-3u/2).

Its exact integral is

    K_2(U)=integral_0^U k_2(u)du
          =(16/5)e^U+(4/5)e^(-3U/2)-4.

For M_U=sup_(0<=v<=U)|F(e^v)|<infinity, C-S2 consequently proves

    sup_(0<=u<=U)|H_m(e^u)-F(e^u)|<=(m-1)M_U K_2(U).       (C-S3)

If F(e^u0)=-d<0 with 0<u0<=U and d>0, all powers satisfying
1<m<=2 and (m-1)M_U K_2(U)<d remain negative there. This is an explicit
finite-horizon continuity guard; no bound uniform as U grows is claimed.

## C-S4. A fixed supercritical positivity theorem has no abstract converse

For an explicitly nonnative two-atom source let

    F_model(x)=T(x)-62T(x/256),
    H_(3/2),model(x)=T(x)^(3/2)-62T(x/256)^(3/2).

Equivalently the source coefficients in the native weight convention
are beta_model(1)=1, beta_model(256)=-992 and zero elsewhere. They are
not the Möbius/extra-67 coefficients. At the inclusive activation x=256,

    F_model(256)=61-62=-1.

For x>=256 the positive ratio T(x)/T(x/256) is strictly larger than
16: multiplying by its positive denominator leaves the strict inequality
-3>-48. Its 3/2 power is therefore greater than 64>62. Hence the model
H_(3/2) is positive at every x>=256; below that activation it is the
positive single-source T(x)^(3/2). The same argument proves positivity
for every real m>=3/2 while its critical model value is negative.

More generally, for any fixed m0>1 choose an integer q so large that
q^m0>4q-3, put N=q^2, and choose a rational C in (4q-3,q^m0). Then
T(x)^m-C T(x/N)^m is positive for all x>=1 and all m>=m0, but its
critical value at x=N is 4q-3-C<0. This is an exact two-atom obstruction
to an abstract reverse transfer. It does not construct a native
counterexample. Source-specific arithmetic remains essential to bridge
the critical gap, even after a lower global supercritical threshold.

`test_sharp_causal_transfer.py` checks the symbolic differential forcing
and closed m=2,3 convolution identities, the exact finite-horizon kernel
integral, and the rational two-atom guards. Its finite symbolic controls
do not machine-prove the infinite native source theorem.
