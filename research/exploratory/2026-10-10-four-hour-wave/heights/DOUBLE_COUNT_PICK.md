# Twice-integrated count error: global Pick order 1,400,000

**Status:** native sharpened Gamma remainder and complete-source proof,
submitted for independent review. The Turing integral theorem and published
critical-line census are imported at the exact scope recorded below.

**Scope:** the complete xi source kernel on arbitrary distinct positive
nodes, and growing orders of complete tails at selectable cutoffs. No RH
or all-order full-kernel conclusion follows from a finite order.

**Dependencies:** the complete xi source/node congruence and arbitrary
variable vertical-displacement proof in
[VOLTERRA_RATIONAL_REFINEMENT.md](VOLTERRA_RATIONAL_REFINEMENT.md), the
exact density constants in
[DENSITY_RATIONAL_REFINEMENT.md](DENSITY_RATIONAL_REFINEMENT.md), and the
integer-count cutoff existence proof in
[GOOD_CUTOFF_PICK.md](GOOD_CUTOFF_PICK.md). The sole new analytic source
import is the same published Turing-integral theorem recorded in
[TRUDGIAN_TURING_SOURCE_RECORD.md](../literature/TRUDGIAN_TURING_SOURCE_RECORD.md).

**What was run:** `verify_double_count.py` checks the uniform Bernoulli,
Gamma, displacement and strict source-payment constants exactly, in normal
and optimized Python. It does not rerun the published theorem or census.

## B1. A native theta remainder with its first cancellation retained

Write `z=1/4+it/2`, `x=1/(2t)`, and take the analytic logarithm on the
right half-plane. The already used Euler--Maclaurin formula is

\[
 \log\Gamma(z)=(z-\tfrac12)\log z-z+\tfrac12\log(2\pi)
   +\frac1{12z}-\frac12\int_0^\infty
                    \frac{B_2(\{u\})}{(z+u)^2}\,du.                 \tag{B1}
\]

Integrate the periodic Bernoulli remainder twice, using
`B3'=3B2`, `B4'=4B3`, `B3(0)=0`, `B4(0)=-1/30`:

\[
 -\frac12\int_0^\infty\frac{B_2(\{u\})}{(z+u)^2}\,du
 =-\frac1{360z^3}-\frac14\int_0^\infty
                     \frac{B_4(\{u\})}{(z+u)^4}\,du=:R_4(z).       \tag{B2}
\]

The explicit `-1/(360z^3)` term is included. Since
`B4(v)=v^2(1-v)^2-1/30`, `|B4|<=1/30` for `0<=v<=1`. Hence

\[
 |R_4(z)|\le\frac1{45t^3}+\frac\pi{60t^3}.                         \tag{B3}
\]

Indeed `|z|>=t/2` and the integral of
`(u^2+(t/2)^2)^(-2)` over the positive axis is `pi/(4(t/2)^3)`.
The positive real part of `z` can only decrease that integral.

Let `epsilon(t)` be the error in the theta main term
`(t/2)log(t/(2pi))-t/2-pi/8`. Taking imaginary parts gives exactly

\[
 \epsilon(t)=\frac t4\log(1+x^2)+\frac14\arctan x
               -\frac1{6t(1+x^2)}+\Im R_4(z).                    \tag{B4}
\]

The real logarithm and arctangent inequalities
`u-u^2/2<=log(1+u)<=u` and
`x-x^3/3<=atan x<=x` show

\[
 \frac1{48t}-\frac{7/384+1/45+\pi/60}{t^3}
 \le\epsilon(t)\le
 \frac1{48t}+\frac{1/24+1/45+\pi/60}{t^3}.                         \tag{B5}
\]

Both displayed cubic coefficients are less than `1/8`, using `pi<22/7`.
For all `t>=32`, this proves the convenient strict native bound

\[
 \boxed{0<\epsilon(t)<1/(47t)}.                                  \tag{B6}
\]

This sharper bound retains the cancellation giving the actual leading
term `1/(48t)`. It is stronger than the earlier absolute `1/t` estimate;
that earlier estimate alone would not pay the following integral error.

## B2. A uniformly small primitive of the complete count discrepancy

Keep the right-continuous positive-ordinate count and main term from Q1,
`Delta=N_+-M`. At any good cutoff `T>=H0=3000000000000`, `Delta(T)=0`,
define

\[
 A_T(t)=\int_T^t\Delta(u)\,du,\qquad t\ge T.                     \tag{B7}
\]

The imported unconditional Turing theorem, the exact count identity
`Delta=S+epsilon/pi` away from ordinates, and (B6) give

\[
 |A_T(t)|\le\frac{2067}{1000}+\frac{59}{1000}\log t
                         +\frac1{141}\log(t/T)
              <c_A\log t,
 \quad\boxed{c_A=\frac{559172551}{4050789000}}.                    \tag{B8}
\]

Here `pi>3` and `logT>28729/1000` imply
`c_A=2067/28729+59/1000+1/141`. Isolated count conventions do not affect
the integral; the right-continuous value at `T` remains essential below.

## B3. Integrate the sampling error twice

For every complex proper rational function in the original denominator
class of dimension `n>=850000`, set

`B_R=integral_T^infinity logb |R(b)|^2 db`, `q=n^2/T`.

The continuously weighted form of the Volterra polynomial proof gives

\[
 \|R'\|_{\log}\le C_1q\|R\|_{\log},\qquad
 \|R''\|_{\log}\le C_2q^2\|R\|_{\log},
 \quad C_1=6383/10000,\quad C_2=2037/5000.                         \tag{B9}
\]

For clarity these are unshifted continuous norms. Apply the same
`D=t partial_t` operator bounds and the exact V6 derivative formulas
directly in the continuous weighted polynomial space. The prefactor
amplification is then one; the real rational multipliers obey the weaker
bounds already used in V6. Thus precisely the same coefficient guards
`d+3/n<=C1` and
`d^2+(6/n+1/n^2)d+9/n^2+7/n^3<=C2`, `d=3191/5000`, apply.

With `f=|R|^2`, Cauchy--Schwarz now gives

\[
 \int_T^\infty\log b\,|f''(b)|db
  \le2(C_2+C_1^2)q^2B_R.                                        \tag{B10}
\]

Twice integrate the complete Stieltjes count error:

\[
 2\int_{(T,\infty)}f\,d\Delta
   =-2\int_T^\infty\Delta f'
   =2\int_T^\infty A_T f'',
 \qquad
 \left|2\int_{(T,\infty)}f\,d\Delta\right|
       <Jq^2B_R,
 \boxed{J=4c_A(C_2+C_1^2)
          =\frac{45562883070469639}{101269725000000000}}.          \tag{B11}
\]

The first lower boundary vanishes because `Delta(T)=0`; the second
because `A_T(T)=0`. At infinity `Delta=O(log b)`, `A_T=O(log b)` and
proper-rational decay gives `f=O(b^-2)`, `f'=O(b^-3)`, so both upper
boundary terms vanish. All integrals converge absolutely. An atom at
`T` belongs to the below-or-at-`T` part, exactly as in Q5.

Consequently, with the unchanged exact density constants

`m_*=(113/355)(1-1838/28729)`, `U_*=106/333`,

the real reference reserve is `(m_*-Jq^2)B_R` and the complete sampling
upper bound is `S_2(q)B_R=(U_*+Jq^2)B_R`. These statements hold for every
complex numerator, including each `D^jP` in the variable-displacement
series; no constant-displacement assumption enters.

## B4. The full conjugate-source payment

Allow the actual independent displacements `|a_b|<=1/2`, both signed-pole
classes, all analytic multiplicities and Taylor depths. All geometric
identities in V5--V7 are unchanged. Their only former small-`q` use was
the numerical amplification guard and scalar payment, now replaced here.
For `q<=131/200`,

\[
 (d+2/n)q<4181/10000,\qquad
 \exp(4181/10000)<\kappa_2=38/25.                                \tag{B12}
\]

Thus the complete discrete Minkowski/variable-path bound gives the
conjugate-source Taylor loss

`(C2+C1^2) kappa_2^2 q^2 S_2(q)B/4`.

Subtracting it from the reference reserve proves

\[
 m_*-Jq^2-\tfrac14(C_2+C_1^2)\kappa_2^2q^2(U_*+Jq^2)
 \ge\boxed{\frac{133326033815066275292957582984782363769}
                 {79810670272500000000000000000000000000000}>0}. \tag{B13}
\]

The expression decreases with `q>=0`; the exact minimum occurs at
`q=131/200`. The margin is about `0.00167053`. All complete sums and
remainder limits retain the original proper-rational convergence proof.

## B5. Global and selectable-height conclusions

At any good cutoff `T>=H0`, every even `n>=850000` satisfying

\[
 \boxed{200n^2\le131T}                                           \tag{B14}
\]

has a strictly positive complete tail kernel on any `n` distinct positive
nodes. Principal submatrices cover smaller sizes. The cofinal good-cutoff
construction Q4 gives selectable tail order `sqrt(131T/200)+O(1)`.

For the global theorem, Q3 supplies one common `T_* in [H0,H0+20]` with
`Delta(T_*)=0`, independent of the nodes. The imported published census
through `3000175332800` contains this full selection interval. Its
below-or-at-`T_*` source is nonnegative, while

`200*(1400000)^2<131*H0<=131*T_*`.

Adding that complete source yields global Pick order **1,400,000**. The
largest even order paid by (B14) at `H0` is **1,401,784**. This remains a
source-qualified finite-order result, with a separate cofinal statement
about changing tail kernels, and is compatible with RH still being open.
