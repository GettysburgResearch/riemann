# A certified smaller boundary conditional on one coherent native tail

**Status: proved conditional implication, with the new arithmetic hypothesis
still open.** Relative to the imported Eisenstein analytic framework and
the explicit tail hypothesis (T) below, the complete consumer gives

\[
 \boxed{\quad L_E(s,\eta)\ne0\quad
     \left(\operatorname{Re}s>\frac{8748856}{10^7}=0.8748856\right)\quad}
 \tag{1}
\]

for every finite-order Hecke character of `E=Q(omega)`, with principal
poles at one permitted. The licensed quadratic base-change factorization
then gives the same conditional region for Dirichlet L-functions and
ordinary zeta. This is more than `10^-6` to the left of `B_flat`.

**Hypothesis (T) is not proved in this packet.** In particular, (1) is not
an unconditional new zero-free region. The contribution here is a complete,
quantitative consumer: the original coherent tail, a specified length
interval, and a specified power saving suffice. A sampled parameter search
is not used to certify any part of that implication.

## 1. Imported framework and the one new arithmetic hypothesis

Use the original sixth-power-free Eisenstein physical rows, fixed finite
ray data, either sextic orientation, the original natural zeros, common
smooth annular profiles, and licensed norm heights. All fixed finite ray
data required by the target-character consumer are covered; constants may
depend on those fixed data. Nonzero angular characters are not added to
this finite-order scope.

The imports are the pinned ordinary framework used in
`SIGNED_NATIVE.md`, the smoothed component theorem in
`INVERSE_POWER_COMPONENT.md`, and the original Eisenstein analytic
consumer of Xu--Sang,
[arXiv:2610.15291v2](https://arxiv.org/html/2610.15291v2):
Propositions 3.1, 4.1 and 5.1, equations (27)-(29), Section 6 and
Appendices B-C. This amplified-moment paper is distinct from their
`2610.17675v2` buffered-density paper used by the component theorem.
The underlying preprints are explicit premises, not independently
certified by this deduction.

Liu's [arXiv:2610.26835v1](https://arxiv.org/html/2610.26835v1) supplies
the convenient scalar notation and `B_flat` comparison. Its Part II
theorems assume a field containing `mu_12`; they are not applied as
field theorems to `E`. The analytic deduction below uses `kappa=3/4`
and the original Eisenstein moments. The interval down to `kappa_flat`
in (12) is an additional scalar certificate, not a required new analytic
extension of M2.

Let `psi_u` be the actual completely multiplicative zero-extended
presentation, including a common puncture `Q` with
`Nrad(Q)<=U^C_Q` for any prescribed fixed `C_Q`. Write `D=U^r` and
`y=sqrt(2D)`. Fix one smooth cutoff `w_0`, equal to one on `[0,1]`,
zero on `[2,infinity)`, and between zero and one. For a common profile
`W` supported in `(1,2)`, put
`V_t(z)=z^(it)W(z)` and

\[
 a_y(\mathfrak r)=
 \sum_{\mathfrak a\mathfrak b=\mathfrak r}
    \mu_E(\mathfrak a)\mu_E(\mathfrak b)
         w_0(N\mathfrak a/y)w_0(N\mathfrak b/y).
 \tag{2}
\]

Fix also one smooth outer cutoff `chi_0`, equal to one on `[0,1]`, zero
on `[2,infinity)`, and between zero and one. The same fixed cutoff is
used in the proved component theorem and the following hypothesis.
The complete tail is the single coherent expression

\[
\begin{split}
 M_{u,>}(U,D,t;W)={}&-D^{-1/2}
 \sum_{\mathfrak r}
       a_y(\mathfrak r)\psi_u(\mathfrak r)
          \bigl[1-\chi_0(N\mathfrak r/U^{13/20})\bigr]\\
 &\quad\times\sum_{\mathfrak c}\psi_u(\mathfrak c)
               V_t(N(\mathfrak r\mathfrak c)/D).
\end{split}                                                    \tag{3}
\]

Both short Möbius factors, all repeated-prime terms, and every original
zero remain. Equivalently, this is the complete complementary sum in the
smoothed version of the exact reflected identity (11) of `SIGNED_NATIVE.md`.
Its support has `Nr>U^(13/20)`, but its transition on the next fixed
annulus is smooth. The complementary component has the weight
`chi_0(Nr/U^(13/20))` and support through `2U^(13/20)`. No sharp outer
cutoff is claimed by the buffered-height component argument. No absolute values
are inserted between its outer dyads or its puncture divisors in (3).

**Open hypothesis (T).** For every epsilon>0 there are fixed finite height
and profile orders `A,J`, in the original scope above, such that

\[
 \sum_u w(u)|M_{u,>}(U,U^r,t;W)|^2
 \ll_\epsilon
 U^{(1+5r)/6-1/1000+\epsilon}
                 (1+|t|)^A p_J(W)^2,
 \quad \frac{29}{25}\le r\le\frac{117}{100}.
 \tag{T}
\]

Here the mean includes the complete nonprincipal physical family and a
bounded nonnegative row weight. Constants are uniform in `U,r`, the
allowed common profiles and heights, and the original common masks;
they may depend on the prescribed puncture exponent and fixed arithmetic
data. If the puncture cost is written separately as `(NQ)^epsilon`, choose
the preliminary epsilon small enough to absorb it in the displayed loss.
Fixed rescalings of the annulus have the usual common-profile scope.

This is a hypothesis about the actual tail (3). A diagonal estimate, an
unsigned component estimate, or an independently chosen test for every
row is insufficient.

### The tail hypothesis really yields a full inverse gain

The smooth coefficient `m_y(n)=mu_E(n)w_0(Nn/y)` agrees with Möbius
through norm `y`, so
`mu_E=2m_y-m_y*m_y*1` through norm `y^2`. For sufficiently large `D`,
the `2m_y` term is absent on `(D,2D)`. This gives the exact decomposition
`M_u=M_{u,<=}+M_{u,>}`, up to the harmless common phase `D^(it)`.
The smoothed cutoff theorem in `INVERSE_POWER_COMPONENT.md` gives

\[
 \sum_u w(u)|M_{u,\le}(U,D,t;W)|^2
 \ll_\epsilon U^{\gamma_0+\epsilon}(1+|t|)^{A_0}p_{J_0}(W)^2,
 \qquad\gamma_0=\frac{83}{24}-\frac{\sqrt{195}}6.
 \tag{4}
\]

Throughout the interval in (T),

\[
 \frac{1+5r}{6}-\gamma_0
                    \ge\frac{17}{15}-\gamma_0>\frac1{1000}.
\]

The strict radical comparison is exact: it is equivalent to
`sqrt(195)>3489/250`, and
`195-(3489/250)^2=14379/62500>0`. Thus the enlarged proved component,
with the fixed smooth selector equal to one through `R=U^(13/20)` and
zero beyond `2U^(13/20)`, leaves only the complement (3) as the new
arithmetic hypothesis. The fixed factor two in its support does not
affect the exponent in (4).

The row Hilbert-space triangle inequality therefore proves the complete
native inverse bound with exponent `(1+5r)/6-1/1000+epsilon` there.
Thus (T) is not being substituted for a bound on the whole inverse without
controlling the other component.

## 2. The improved detector count retains the old short-length floor

Put `alpha=5/6`, `eta_0=1/1000`, and `r_a=29/25`. For a source-compatible
class `(delta,x)`, with `0<delta<=5/6` and `0<=x<=1/2`, write

\[
\begin{split}
 c&=2/(3\kappa),& D_\kappa&=3-(1+c)x,&
 P_\kappa&=(2-cx)(1-x),\\
 A_\delta&=\alpha-\delta,& C_\kappa&=\delta P_\kappa/D_\kappa,&
 J_\kappa&=A_\delta D_\kappa+\delta P_\kappa.
\end{split}
\]

The original count and the short/long branches are

\[
\begin{split}
 R_\kappa&=1-\delta+
       \frac{A_\delta C_\kappa}{2(A_\delta+C_\kappa)},\\
 S_\kappa(t)&=1-\delta+C_\kappa(3/2-t),\\
 L_\delta(t)&=1/6+A_\delta t.
\end{split}                                                   \tag{5}
\]

Use just four detector cutoffs,

\[
 \mathcal T=\left\{\frac{581}{500},\frac{291}{250},
                    \frac{583}{500},\frac{146}{125}\right\}
             =\{1.162,1.164,1.166,1.168\}.
 \tag{6}
\]

For a long witness of exponent `r<r_a`, the old inverse gives at most
`L_delta(r_a)`. For `r_a<=r<=t`, (T) and (4) give at most
`L_delta(t)-eta_0`. Short witnesses still give `S_kappa(t)`.
Consequently each complete class satisfies the count with exponent

\[
 R_{\kappa,t}^{\rm trial}
  =\max\{S_\kappa(t),L_\delta(t)-\eta_0,L_\delta(r_a)\}.
 \tag{7}
\]

The last term is essential. The gain at `t` cannot be used for witnesses
below the improved length interval. Define the usable count

\[
 \boxed{\quad R_\kappa^*=
       \min\bigl(R_\kappa,\min_{t\in\mathcal T}
                                      R_{\kappa,t}^{\rm trial}\bigr).\quad}
 \tag{8}
\]

These are finitely many valid upper bounds for the same compatible class.
They need no new assertion of independence between detector witnesses.
The two detector witnesses retain one common character. The physical prime
amplitudes and the physical numerator retain the fixed-twist relations
licensed by the Eisenstein source; the numerator need not have the
detector's fixed twist. Fixed slot coefficients, independent of the row,
are retained when that source transfers physical amplitudes to a detected
presentation. No amplitude is moved between unrelated presentations.
The source detector has
`r<=t+O(1/log U)`; fixed annular rescalings give the same small displacement.
At the lower edge it is absorbed by the old floor in (7) and the reserved
epsilon. The largest cutoff is `0.002` below the upper edge in (T).

For later uses,

\[
                 1-\delta\le R_\kappa^*\le R_\kappa
                                      \le1-2\delta/3.     \tag{9}
\]

Indeed every short branch in (7) is at least `1-delta`, because `t<3/2`.
The old bound gives the two upper inequalities. This preserves the
source's numerator-capacity and row-scale estimates.

## 3. A rational geometry and the complete endpoint claim

Choose

\[
 B_0=\frac{8748856}{10^7},\qquad
 \ell=\frac{156679}{937500},\qquad b=\frac{43267}{500000},
 \quad l_x=\frac{1-b-\ell}{2},\quad l_y=\frac{1+b-\ell}{2},
 \quad h=\frac{1+b+3\ell}{2}.                              \tag{10}
\]

Then `B_0=11/12-ell/4`, as required by the direct majorant. In particular

\[
 h=\frac{3969767}{5000000},\quad
 l_y=\frac{6895573}{15000000},\quad
 C_0=-\frac14+\frac b6+\frac{5\ell}4=-\frac{80017}{3000000}.
\]

Replacing the class count in the licensed averaged numerator by (8)
replaces `(3R+1)/4` by `(3R^*+1)/4`. It gives endpoint exponent

\[
 E_\kappa^*(\delta,x)=C_0+\frac\delta2+
 \delta x\left\{\ell+\frac1{3\kappa}
                      \left(\frac h4-\frac{l_y}2\right)\right\}
                       -\frac{3h}{4}(1-R_\kappa^*).
 \tag{11}
\]

**Exact endpoint certificate.** With the geometry (10),

\[
 \boxed{\quad E_\kappa^*(\delta,x)\le-10^{-6}\quad
   (1/8\le\delta\le5/6,\ 0\le x\le1/2),\quad
          \kappa_\flat\le\kappa\le3/4.\quad}             \tag{12}
\]

In particular the scalar inequality covers the requested fixed input
`kappa_flat`. The analytic consumer only needs the directly licensed
parameter `kappa=3/4`; no approximate algebraic number enters acceptance.

### Reduction to the rational endpoint in kappa

At fixed `x`, `P_kappa/D_kappa` increases with `kappa`, since its
derivative with respect to `c=2/(3kappa)` is
`-x(1-x)^2/D_kappa^2`. Thus `R_kappa`, every short branch, and (8) are
nondecreasing in `kappa`. Also `h/4-l_y/2<0`, so the amplitude coefficient
in (11) increases with `kappa`. Hence `E_kappa^*<=E_(3/4)^*`.

### A proved reduction to x=1/2 for delta>=1/4

At `kappa=3/4` put

\[
 f(x)=\frac{(2-8x/9)(1-x)}{3-17x/9},\qquad
 K=\ell+\frac{-1-b+5\ell}{18}
                           =\frac{20679931}{135000000}.
\]

Elementary polynomial inequalities on `[0,1/2]` give

\[
 f(x)\ge14/37,\qquad 0\le-f'(x)\le2/3.                  \tag{13}
\]

For example `P-(14/37)D=(1-2x)(32/37-4x/9)>=0`;
`(2/3)D^2+(P'D-PD')=10/9-20x/9+170x^2/243>0`.
The checker verifies these and the remaining sign exactly.

For `delta>=1/4`, with `A=5/6-delta` and `C=delta f(x)`,

\[
 0\le\frac A{A+C}\le\frac{37}{43}.
\]

The old endpoint, with the old count, therefore satisfies

\[
 \partial_x E_{\rm old}\ge
 \delta\left(K-\frac h4(37/43)^2\right)>0.               \tag{14}
\]

The endpoint obtained from a short branch has derivative at least
`delta{K-(h/2)(3/2-t)}>=delta(K-17h/100)>0`.
Each of the two long-branch endpoints has derivative `delta K>0`.
Taking their maximum and then the minimum in (8) preserves monotonicity.
Consequently the entire improved endpoint has its largest value at
`x=1/2` when `delta>=1/4`. These derivative inequalities are strict exact
rational inequalities, not observations on a grid.

### Small rectangle and six exact intervals

Let `rho_0=10^-6`, `J=(5/6-delta)D+delta P`, and let `E(R)` denote
the affine expression (11) with its count replaced by `R`, at `kappa=3/4`.
All the following polynomial denominators are positive on their domains:

\[
 \begin{array}{ll}
 P_{\rm old}=-2J(E(R)+\rho_0),&R=R_{3/4},\\
 P_{S,t}=-D(E(S(t))+\rho_0),&
 P_{L,t}=-(E(L(t)-\eta_0)+\rho_0),\\
 P_F=-(E(L(r_a))+\rho_0).&
 \end{array}                                               \tag{15}
\]

The first is of degree at most two in `delta` and three in `x`; the
other polynomials have degree at most one in `delta`. Their full exact
definitions and every Bernstein coefficient appear in the checker and
its generated report.

On the small rectangle `[1/8,1/4] x [0,1/2]`, every tensor Bernstein
coefficient of `P_old` is positive, with minimum
`2326099811/116640000000>1/100`. Thus the old count already suffices there.
For `delta>=1/4`, (14) reduces the proof to `x=1/2`. The exact cover is:

| Delta interval | Available count used | Lower bound for every required polynomial coefficient |
|---|---|---:|
| `[1/4,473/1024]` | old | `7/10^6` |
| `[473/1024,953/2048]` | `t=581/500` | `2/10^6` |
| `[953/2048,15/32]` | `t=291/250` | `6/10^5` |
| `[15/32,967/2048]` | `t=583/500` | `7/10^5` |
| `[967/2048,487/1024]` | `t=146/125` | `4/10^5` |
| `[487/1024,5/6]` | old | `5/10^7` |

Each trial-count row certifies all three polynomials `P_S,t`, `P_L,t`,
and `P_F`. The last of these retains witnesses below the improved interval.
For an interval `[a,b]`, the polynomial is written in the Bernstein basis
after `delta=a+(b-a)z`. Every basis function is nonnegative on `[0,1]`,
and their sum is one; positive coefficients prove the claimed sign on the
whole interval. The same argument applies to the tensor basis on the
small rectangle. There are no gaps between the intervals in the table.
This proves (12).

## 4. Finite prime supply and every remaining scalar gate

No infinite prime supply is granted. Set `zeta=10^-9`. The checker
verifies all the additional scalar conditions of the source using
`7497/10000<=kappa<=3/4`. Representative exact inequalities are

\[
\begin{gathered}
 b>0,\quad1/6<\ell<1/5,\quad B_0>437/500,\quad
 l_x>\ell,\quad l_y-\ell>11b/6,\\
 6\kappa\ell>3/4,\quad \ell/h<1/(6\kappa),\quad
 \ell/(h+\zeta)>21/100,\quad h/2<l_y<1/2.
\end{gathered}                                               \tag{16}
\]

The last prime-supply margin is greater than `0.0004963` above `21/100`.
Thus the counting theorem has full supply with, for example,
`rho_sup=1/100`. It also supplies the actual numerator amplifier despite
`ell/h<1/(6kappa)`. Indeed, for `delta>=1/8`, `g=delta x<=delta/2`,
`L=ell/d>21/100`, and (9),

\[
 (6\kappa-2g)L-R_\kappa^*
 \ge\frac{21}{100}(6\cdot7497/10000-\delta)
                              -(1-2\delta/3)
 \ge\frac{1279}{750000}>0.                                \tag{17}
\]

The last expression increases with `delta`, so its minimum is at `1/8`.
This is the finite-supply condition in the source's maximal-capacity
numerator argument. Lowering the class count makes it easier to satisfy.

For `0<delta<1/8` use the original supply-limited numerator and old count.
Writing

\[
 A_{\rm sm}=1/2+(\ell/2)(1/2+2\ell/h)-h/2,
\]

the remaining endpoint and small-row gates are checked as

\[
\begin{gathered}
 \max(C_0,C_0+A_{\rm sm}/8)<-1/250,\\
 C_0+(1/2+3\ell/2)/50<-1/100,\\
 13h/75-l_y/2+1/50<-1/20.                                 \tag{18}
\end{gathered}
\]

Their extra margins beyond the displayed thresholds exceed, respectively,
`0.0001744`, `0.0016586`, and `0.0222338`. These handle the small-delta,
floor, and small-row contributions, including the source's bounded
nonprincipal exceptions. Far and principal rows use the unchanged source
estimates. Common punctures and all original local factors remain in that
assembly.

The complete moderate-row exponent uses
`K_star=(3R_star+1)/4` in place of the source's corresponding quantity.
By (9), its derivative in the row scale remains between `7/200` and `1`.
For small delta the original supply-limited argument is unchanged.
Thus the endpoint controls all moderate dyads, and extending them to
`d<=h+zeta` costs at most `zeta`. In particular
`2zeta<rho_0/2`, as required for a strict remaining margin.

## 5. Contour, height, and closure order

The original Eisenstein outside factors can be checked directly, without
transferring a theorem from a larger field. Xu--Sang's equation (18) has
the Mellin factor `X^(1/2-z) Z^(s+z-1) Y^(w-1)` and row factor
`(Nu)^(-z)`. The original Eisenstein AFE has one complex gamma factor.
Two identical normalized plain blocks and the actual selected prime
amplitudes give the first moment
`U^((3R_star+1)/4-theta/2)` by the original M2 and Holder; its full-capacity
case is valid by (17). Reflection contributes `U^theta`, while the
outside numerator factor is `Y^(-1/2-theta)`. Including the physical
prime factors and dividing by the direct exponent gives

\[
 a-B_0-l_y(1/2+\theta)+h(z_0-1/6)-\ell/2+\ell g
       +d\{(3R_\kappa^*+1)/4+\theta/2-z_0\},\qquad z_0=17/50.
 \tag{19}
\]

At `d=h`, the identities in (10) reduce (19) exactly to (11).
This is the original Eisenstein equation (27), with its input class
cardinality replaced by the proved count (8). Its local-error argument
uses the primitive conductor deficit once for the complete set of strict
labels; changing a count does not change that identity. The E AFE and
fixed bad Euler factors are those of Xu--Sang Appendices B-C, not the
higher-degree cyclotomic construction.

The new count changes only the cardinality exponent of an already
source-compatible amplitude class. It does not change its prime factors,
character presentation, bin zeros, or numerator contour. Consequently the
source's finite tuple expansion, conductor deficits for strict local
labels, and complete-family contour shifts remain applicable. The
numerator shift still obeys `0<=theta<=min(delta/2,1/10)`.

Choose the numerical geometry and the four cutoffs first. Then choose the
moment losses, bin meshes, and prime-window mesh inside a fixed fraction
of the proved `10^-6` margin and the supply margin. Fix all internal
detector, tail-hypothesis, and Sobolev orders before choosing the
polynomial height cutoff small enough to absorb their height costs.
Choose the external Mellin truncation order afterwards. The common
puncture exponent is fixed before these choices. This is the source's
order of choices, with the additional finite orders from (T) included;
there is no growing family of derivative orders or unlicensed angular
extension.

The functions in (5)-(8) are uniformly Lipschitz on the certified compact
rectangle. Therefore bin rounding and finite dyadic displacements fit
in the reserved losses. One may take the source's preliminary remainder
margin `r_* = min(rho_0/2,1/1000)=5*10^-7` and a nonprincipal budget
`r_*/8`, before making those choices. All inequalities used above are
strict, so sufficiently fine fixed meshes exist.

The original Eisenstein closure proof now repeats with the improved count. More
explicitly, let `beta` be the finite-order Eisenstein zero supremum and
suppose `beta>B_0`. The pinned `7/8` family cap licenses `kappa=3/4`
in the original Eisenstein M2. The direct estimate has
exponent `C(B_0)+epsilon_low`, with
`0<epsilon_low<(beta-B_0)/4`. Equations (12), (16)-(18), and the unchanged
local assembly give a strictly positive high-side saving `m`.
The late height choice then gives continuation to

\[
 \sigma_{\rm cont}=
       \max\{B_0+\epsilon_{\rm low},\beta-m/2\}<\beta.
\]

The source's Euler correction is holomorphic and nonzero there, because
`sigma_cont>=B_0>437/500`. The continuation therefore contradicts the
definition of the family zero supremum. This proves (1), conditionally
on (T) and the explicitly imported framework.

Natural omitted Euler factors have zeros only on `Re s=0`, so restoring
them does not change this conclusion. For a Dirichlet character `chi`,
quadratic base change to `E` factors its norm-lift L-function as
`L(s,chi)L(s,chi chi_-3)`. The Eisenstein conclusion excludes zeros of
either factor in the same strict half-plane; the permitted principal pole
at one causes no cancellation of a nontrivial zero there. This gives the
stated Dirichlet and zeta consequences. No extension to every number field
is asserted without the corresponding native tail hypothesis and
consumer.

## 6. Reproducibility and the remaining open task

`check_conditional_consumer.py` uses only standard-library exact rational
arithmetic. It verifies the denominator signs, the monotonicity
inequalities, every Bernstein coefficient on the small rectangle and six
intervals, finite supply, all remaining scalar gates, and the source
quartic root bracket. It passes also under `python -O`, because every
acceptance is an explicit check.

The root bracket gives the exact lower bound

\[
 B_\flat-B_0>
      \frac{261759991}{250000000000000}>10^{-6}.
\]

A negative control removes the hypothetical saving: at the exact class
`delta=469345/10^6`, `x=1/2`, the old endpoint is positive and every
zero-saving trial count is at least the old crossing count. Thus the
certificate cannot claim the new boundary while silently retaining only
the old inverse input.

The open arithmetic task is precisely (T), for the complete smooth
expression (3) beyond `U^(13/20)`, on the indicated short length interval.
The source HLC logarithmic gain, the already bounded product contribution, and the restricted
large-amplitude inverse estimate do not prove (T). The conditional
consumer shows exactly what would follow if that remaining estimate is
established.
