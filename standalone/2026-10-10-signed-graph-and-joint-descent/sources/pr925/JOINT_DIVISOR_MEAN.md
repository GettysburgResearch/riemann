# A joint divisor mean with the exact cube reciprocal

**Status:** proposed source-conditional analytic theorem. The divisor
phases are retained inside a joint polynomial before the row norm is
taken. This gives the completed block estimate (3.1) and a stronger
bound for the large-divisor tail in Theorem 5.1. It does not improve the
full moment or the full divisor-series continuation domain.

**Authorship:** joint_divisor_attack. Independent review must identify
the exact frozen content.

**Scope:** squarefree primary rows outside a fixed bad set; fixed finite
ray characters; all good squarefree divisors, with their moving masks;
strict interior complex strips. The theta mean square and the classical
squarefree sextic large sieve are imported analytic inputs. The local
algebra, recombination, dyadic argument and tail bound are proved here.

**Exact sources:** PR #922 mathematical source
`8f2acaacddc10bd8fb053a66070a1d06d25aa922`,
`SECOND_REFLECTION_BOOTSTRAP.md`, equations (1.1)–(3.5), and
`SPECTRAL_ROW_MEAN.md`, equations (1.1)–(3.3). The latter fixes the
OpenAI/math source `adc7f1241b42e322a6451854ab7e4b4c146bf78a`,
October 5 `paper2.tex`, Proposition R and `eq:T`, and the squarefree
sextic large sieve of Blomer–Goldmakher–Louvel, Theorem 1.3. No new
verification of those foundations or Lean formalization is asserted.

## 1. The actual divisor coefficient after cube division

Work over `O=Z[omega]` with the inherited primary generators, norm N,
and literal zero extensions of the residue characters. The fixed set S
contains the primes above 2 and 3 and the fixed ray conductors. Let
`k` be squarefree and prime to S. Put

\[
a_\xi(n)=\overline{\alpha(n)}\gamma_2(n)\xi(n),
\qquad \alpha(n)=n/|n|.
\tag{1.1}
\]

The two fixed ray characters in this note are

\[
\xi_1=\varrho,\qquad \xi_2=\kappa\varrho,
\qquad \kappa=\eta\rho^3,\qquad
\varrho^3=\overline\rho^{\,3}.
\tag{1.2}
\]

These are the actual characters in PR #922. Write

\[
t=1-s,\qquad u=v-s,\qquad
a=\Re u,\qquad b=\Re t.
\tag{1.3}
\]

For a good prime p of norm q define

\[
\begin{aligned}
\varepsilon_k(p)&=\chi_k(p)^3,\\
c_k(p)&=\overline{\alpha(p)}^{\,3}\xi_1(p)^3
                    \varepsilon_k(p),\\
\widetilde c_k(p)&=\kappa(p)^3c_k(p),\\
y_p&=c_k(p)q^{1/2-3t},\qquad
z_p=\widetilde c_k(p)q^{1/2-3u},\\
A_p&=\kappa(p)c_k(p)q^{1/2-2t-u}.
\end{aligned}
\tag{1.4}
\]

All prime products below omit kS. In particular
`epsilon_k(p)^2=1` is used only at the remaining primes.

The conditioned squarefree series and its completion are

\[
\begin{aligned}
G_{k,d}(u)
 &=\sum_m^*\frac{a_{\xi_2}(m)\chi_k(m)\chi_m(d)^4}{(Nm)^u},\\
\mathcal T_{k,d}(u)
 &=G_{k,d}(u)L_{S,kd}(3u-\tfrac12,\widetilde c_k).
\end{aligned}
\tag{1.5}
\]

Thus the cube Euler product omits d as well as kS. The notation for
the cube character in (1.5) means exactly the coefficient in the first
line of (1.4), with the indicated finite ray change. If the imported
source uses `chi_n(k)` in place of `chi_k(n)`, partition k into its
finitely many supplementary ray classes and absorb the resulting
fixed character into both relevant coefficient families. This is the
same primary reciprocity convention as the frozen source.

The old exact divisor representation is

\[
\mathcal Z_k
=L_{S,k}(3t-\tfrac12,c_k)
 \sum_d^*\frac{a_{\xi_2}(d)\chi_k(d)h_k(d)}{(Nd)^u}
                  G_{k,d}(u),
\tag{1.6}
\]

where `h_k` is squarefree multiplicative and

\[
h_k(p)=\kappa(p)^{-1}q^{u-t}-y_p.
\tag{1.7}
\]

### Proposition 1.1: the completed joint representation

Initially in `Re(u)>1`, `Re(t)>Re(u)`,

\[
\boxed{
\mathcal Z_k
=\frac{L_{S,k}(3t-\tfrac12,c_k)}
        {L_{S,k}(3u-\tfrac12,\widetilde c_k)}
\sum_d^*\frac{a_{\xi_1}(d)\chi_k(d)}{(Nd)^t}
           \Theta_k(d;u,t)\mathcal T_{k,d}(u),}
\tag{1.8}
\]

where

\[
\boxed{\Theta_k(d;u,t)=\prod_{p\mid d}
                \frac{1-A_p}{1-z_p}.}
\tag{1.9}
\]

Both exterior Euler products and their reciprocals are uniformly
bounded in k on every strict strip `a,b>1/2`. The factor at a deleted
prime is one; the d summand is zero when d meets kS.

**Proof.** From (1.5),

\[
G_{k,d}(u)
=\frac{\mathcal T_{k,d}(u)}
       {L_{S,k}(3u-\tfrac12,\widetilde c_k)}
  \prod_{p\mid d}(1-z_p)^{-1}.
\tag{1.10}
\]

At a permitted prime, multiply (1.7) by the outer squarefree
coefficient in (1.6). Since `a_(xi_2)(p)=kappa(p)a_(xi_1)(p)`,

\[
\frac{a_{\xi_2}(p)\chi_k(p)h_k(p)}{q^u}
=\frac{a_{\xi_1}(p)\chi_k(p)}{q^t}(1-A_p).
\tag{1.11}
\]

Equations (1.10)–(1.11) prove (1.8). The initial region is one of
absolute convergence, so these rearrangements are legitimate there.
For the Euler bounds, `3a-1/2` and `3b-1/2` are strictly greater
than one. The absolute products over all good primes dominate every
moving omission. QED.

Replacing `Theta_k(d)` by one in (1.8) would change the function.
In particular the denominator in (1.9) is the moving cube omission,
not an optional normalization.

## 2. An absolutely summable expansion of the row dependence

Remove the quadratic row value from (1.4): write

\[
z_p=z_{0,p}\varepsilon_k(p),\qquad
A_p=A_{0,p}\varepsilon_k(p),
\tag{2.1}
\]

where `z_(0,p)` and `A_(0,p)` are independent of k. On strict strips
`a,b>1/2`, define

\[
e_1(p)=\frac{z_{0,p}-A_{0,p}}{1-z_{0,p}^2},
\qquad e_0(p)=z_{0,p}e_1(p).
\tag{2.2}
\]

The denominator cannot vanish because `|z_(0,p)|=q^(1/2-3a)<1`.
Direct rationalization gives the exact identity

\[
\boxed{
\frac{1-A_p}{1-z_p}
=1+e_0(p)+e_1(p)\varepsilon_k(p).}
\tag{2.3}
\]

Let

\[
r_* =\min(3a-\tfrac12,\ 2b+a-\tfrac12)>1.
\tag{2.4}
\]

Uniformly on a fixed strict strip and uniformly in both imaginary
parts,

\[
|e_1(p)|\ll q^{-r_*},\qquad
|e_0(p)|\ll q^{-r_*-3a+1/2}.
\tag{2.5}
\]

Extend `e_0,e_1` multiplicatively to squarefree indices. Finite
expansion of (2.3) proves

\[
\Theta_k(d)
=\sum_{\substack{r_0r_1\mid d\\(r_0,r_1)=1}}
       e_0(r_0)e_1(r_1)\chi_k(r_1)^3.
\tag{2.6}
\]

For each sufficiently small fixed `delta>0`,

\[
\boxed{
\sum_{r_0,r_1}^{*}\!\mathbf1_{(r_0,r_1)=1}
 |e_0(r_0)e_1(r_1)|(Nr_0Nr_1)^\delta<\infty.}
\tag{2.7}
\]

Indeed the absolute sum is the Euler product with p-factor
`1+|e_0(p)|q^delta+|e_1(p)|q^delta`; choose
`delta<r_*-1` uniformly over the strip. This proof also shows that
`Theta_k(d)` is uniformly bounded in k,d and both imaginary parts.

Equation (2.3) is a unit identity. At a nonunit the surrounding
factor `chi_k(d)` is zero. We do not apply the rationalization
using the false equality `0^2=1`.

## 3. The joint completed block

Let `Q>=2`, `F,X>=1`, and let `K_Q` be any subset of the squarefree
primary k with `Q<=Nk<2Q` and `(k,S)=1`. Fix a compact interval
`I` inside `(0,infinity)` and `W in C_c^infinity(I)`.
Let `v_d` be any coefficients independent of k, supported on
`F<=Nd<2F`, with `|v_d|<=1`. They need not be multiplicative or
smooth. Define

\[
\begin{aligned}
T_W(X;k,d)=X^{-1/2}
\sum_m^*\sum_{\substack{b_0\equiv1\ (3)\\(b_0,dS)=1}}
&a_{\xi_2}(m)\chi_k(m)\chi_m(d)^4\,
 \overline\alpha(b_0)^3\xi_2(b_0)^3\chi_k(b_0)^3\sqrt{Nb_0}\\
&\hspace{10mm}\cdot W\!\left(\frac{Nm(Nb_0)^3}{X}\right),\\
\mathfrak B_{F,X}(k)
&=F^{-1/2}\sum_d^*v_d a_{\xi_1}(d)\chi_k(d)
               \Theta_k(d;u,t)T_W(X;k,d).
\end{aligned}
\tag{3.0}
\]

There is no condition `(m,b_0)=1`. The conditions `(m,d)=1`
and the row masks are the literal character zeros; the condition
`(b_0,d)=1` is the cube mask in (1.5).

### Theorem 3.1: a joint block mean

On every fixed strict strip `a,b>1/2`, for every epsilon>0,

\[
\boxed{
\sum_{k\in\mathcal K_Q}|\mathfrak B_{F,X}(k)|^2
\ll (QFX)^\epsilon\|W\|_{C^J}^2
\min\left\{
Q+FX+(QFX)^{2/3},\quad
FQ+\frac{Q^2F^2}{X}\right\}.}
\tag{3.1}
\]

The constants are independent of Q,F,X,k and the coefficients v.
They are uniform in both imaginary parts of u,t. The order J is
finite and depends only on the imported input and the fixed strip
and support data.

### 3.1 Proof of the joint polynomial bound

First replace `Theta_k(d)` by one. For fixed cube index b_0 set
`L=X/(Nb_0)^3`. The corresponding term in `mathfrak B` is
`1/Nb_0` times a polynomial normalized by `(FL)^(-1/2)`.
The Gauss CRT identity gives, when `(d,m)=1`,

\[
a_{\xi_1}(d)a_{\xi_2}(m)\chi_m(d)^4
=a_{\xi_1}(dm)\kappa(m).
\tag{3.2}
\]

Consequently the squarefree column index is the single product
`ell=dm`, of norm comparable with FL. Its coefficient, apart
from `a_(xi_1)(ell)`, is

\[
\sum_{d\mid\ell} v_d\kappa(\ell/d)
 \mathbf1_{(d,b_0)=1}
 W\!\left(\frac{N(\ell/d)}{L}\right).
\tag{3.3}
\]

The row factor is `chi_k(ell)`, times the cube row factor of
modulus at most one. Equation (3.3) has absolute value at most
`tau(ell)||W||_infinity`. Ideal counting and the divisor bound
therefore bound the squared norm of these normalized coefficients
by `(FL)^epsilon||W||_infinity^2`. Applying the squarefree sextic
large sieve gives

\[
\ll (QFX)^\epsilon\|W\|_\infty^2
       \left[Q+FL+(QFL)^{2/3}\right].
\tag{3.4}
\]

If FL lies in a fixed bounded interval below one, enlarge its sieve
cutoff by a fixed constant. If it is below the support of all
nonzero ideals, the polynomial is empty. These conventions handle
every small-scale block without changing the stated bound.

The cube sum is finite: `Nb_0 << X^(1/3)`. Weighted Cauchy with
weight `1/Nb_0`, followed by (3.4), gives the three sums

\[
Q\sum_{b_0}\frac1{Nb_0},\qquad
FX\sum_{b_0}\frac1{(Nb_0)^4},\qquad
(QFX)^{2/3}\sum_{b_0}\frac1{(Nb_0)^3}.
\tag{3.5}
\]

The first has only a logarithm and the other two converge. Thus
the first expression in (3.1) is proved when `Theta=1`.

Now insert the exact expansion (2.6), and fix `r_0,r_1`, with
`r=r_0r_1`. Write `d=rj`. The surviving terms have
`(r,jm b_0)=1`, `(j,m)=1`. Repeated use of (3.2) leaves the
single squarefree column `ell=jm`, with the additional fixed
column character `chi_ell(r)^4` and the divisor coefficient
`v_(rj) kappa(m)`. The row factors outside this polynomial are
`chi_k(r)chi_k(r_1)^3chi_k(b_0)^3`, all of modulus at most one.

The effective outer scale is `F_r=F/Nr`, and the change of
normalization contributes `(Nr)^(-1/2)`. The preceding argument
therefore bounds the norm of this component by

\[
\ll (QFX)^\epsilon\|W\|_\infty
 (Nr)^{-1/2}
 \left[Q+\frac{FX}{Nr}
              +\left(\frac{QFX}{Nr}\right)^{2/3}\right]^{1/2}.
\tag{3.6}
\]

If `Nr>2F`, the component is empty. Otherwise `F_r>=1/2`,
so the same bounded-scale convention applies. All moving
coprimality restrictions only remove terms from the relevant
coefficient vector; none is dropped in the identity.

Minkowski is used here only over the absolutely summable correction
indices `r_0,r_1`, after the entire j,m divisor covariance has
been retained. Equations (2.7) and (3.6) prove the first bound
of (3.1) for the actual `Theta`.

### 3.2 Proof of the theta bound

For fixed d the imported completed theta mean, in exactly the
normalization (3.0), is

\[
\sum_{k\in\mathcal K_Q}|T_W(X;k,d)|^2
\ll(QFX)^\epsilon\|W\|_{C^J}^2
          \left(Q+\frac{Q^2F}{X}\right).
\tag{3.7}
\]

The source's reference parameter can be chosen as
`max(2Q,2F,X,2)` with its `C_0=1`, so J does not grow with
the indices. The same source use was justified in PR #922.
The estimate for all source rows may be restricted to `K_Q`.

Use the uniform bound on `Theta_k(d)` proved after (2.7),
Minkowski in the finite d sum, and `O(F)` choices of d.
The normalization `F^(-1/2)` leaves a factor `F^(1/2)` in
the row norm. Squaring gives the second expression in (3.1).
This proves Theorem 3.1. QED.

The first bound in (3.1) is at most

\[
F\left[Q+X+(QX)^{2/3}\right],
\tag{3.8}
\]

which is the polynomial estimate obtained by taking a norm for
each d before summing. The improved factors are F in the row
count term and `F^(1/3)` in the mixed term. The term FX is
unchanged; that distinction matters in the next calculation.

## 4. A finite divisor block of the Dirichlet series

Let `v_d` again be arbitrary coefficients independent of k,
bounded by one and supported on `F<=Nd<2F`. Define

\[
\mathscr D_F(k;u,t)=
\sum_d^* v_d\,
 \frac{a_{\xi_1}(d)\chi_k(d)\Theta_k(d;u,t)}{(Nd)^t}
                  \mathcal T_{k,d}(u).
\tag{4.1}
\]

This is a finite sum of the continued theta functions. It is not
defined by an absolutely convergent uncompleted inner series on
`a<=1`.

### Proposition 4.1: four explicit terms

On fixed strict strips

\[
\tfrac12<a_0\le a\le a_1<\tfrac56,\qquad b>\tfrac12,
\tag{4.2}
\]

one has

\[
\begin{aligned}
\|\mathscr D_F(\,\cdot\,;u,t)\|_{\ell^2(\mathcal K_Q)}
\ll &(QF)^\epsilon(2+|\Im u|)^M\bigl[
 Q^{1/2}F^{1/2-b}\\
&+Q^{1-a}F^{3/2-b-a/2}
 +Q^{3/4-a/2}F^{5/4-b-a/2}\\
&+Q^{1-4a/5}F^{3/2-b-4a/5}\bigr].
\end{aligned}
\tag{4.3}
\]

There is no extra polynomial dependence on `Im(t)` in this
bound; allowing one would also be harmless for Mellin inversion.

**Proof.** Use the exact completed dyadic reconstruction in
PR #922, with `X=2^j` and `W_u(y)=y^(-u)W_0(y)`:

\[
\mathcal T_{k,d}(u)
=\sum_X X^{1/2-u}T_{W_u}(X;k,d).
\tag{4.4}
\]

A separate first cutoff may be used. Its support and derivative
bounds obey the same estimates. For a>1/2 the reconstruction
converges normally in each finite row space, by (3.7). Inserting
(4.4) in (4.1), and replacing `v_d` by
`v_d(Nd/F)^(-t)`, whose modulus is bounded on each real strip,
gives the bound

\[
F^{1/2-b}(2+|\Im u|)^M
\sum_X X^{1/2-a}
\left\{
\min\left(Q+FX+(QFX)^{2/3},\ FQ+Q^2F^2/X\right)
\right\}^{1/2},
\tag{4.5}
\]

with the small losses from (3.1) retained initially.

For nonnegative numbers, `min(sum_i A_i,sum_j B_j)` is at most
`sum_(i,j) min(A_i,B_j)`. Also a common upper summand may be
removed at the cost of that summand. Consequently the minimum
in (4.5) is at most Q plus the four quantities

\[
\begin{gathered}
\min(FX,FQ),\qquad \min(FX,Q^2F^2/X),\\
\min((QFX)^{2/3},FQ),\qquad
\min((QFX)^{2/3},Q^2F^2/X).
\end{gathered}
\tag{4.6}
\]

The square root of a sum is at most the sum of square roots.
The crossovers and dyadic contributions, before multiplication
by `F^(1/2-b)`, are as follows:

| Summand | Crossover X | Bound for the dyadic norm sum |
|---|---|---|
| Q | no crossover | `Q^(1/2)` |
| `min(FX,FQ)` | Q | `F^(1/2)Q^(1-a)` |
| `min(FX,Q^2F^2/X)` | `QF^(1/2)` | `Q^(1-a)F^(1-a/2)` |
| `min((QFX)^(2/3),FQ)` | `(QF)^(1/2)` | `(QF)^(3/4-a/2)` |
| `min((QFX)^(2/3),Q^2F^2/X)` | `(QF)^(4/5)` | `(QF)^(1-4a/5)` |

For example the last row has lower summand
`(QF)^(1/3)X^(5/6-a)` and upper summand
`QF X^(-a)`. Both geometric sums have the displayed size on
the strict strip (4.2). The preceding row has the same lower
summand and upper summand `(QF)^(1/2)X^(1/2-a)`.
The two linear rows are evaluated in the same way, with lower
summand `F^(1/2)X^(1-a)`. All crossovers are at least one.

The second row of the table is bounded by its third row because
F>=1. Multiplying by `F^(1/2-b)` proves (4.3).
The derivative bound for W_u is polynomial in `Im(u)`.
Choose the initial small losses below all strict strip margins;
the powers of the crossovers then absorb into `(QF)^epsilon`.
This proves the stated uniform estimate. QED.

## 5. A stronger large-divisor tail

The coefficient of the highest power of F in (4.3) is the linear
term

\[
Q^{1-a}F^{3/2-b-a/2}.
\tag{5.1}
\]

Thus this argument retains the old convergence condition
`2b+a>3`. It nevertheless gives a conductor saving for the
part of the series with large divisors.

### Theorem 5.1

Fix strict strips `1/2<a<5/6` and `eta>0`, and set

\[
b=\frac{3-a}{2}+\eta.
\tag{5.2}
\]

Let `R>=Q^(2/3)`. The exact tail of (1.8), obtained by retaining
`Nd>=R`, obeys

\[
\boxed{
\left\|
\frac{L_{S,k}(3t-\tfrac12,c_k)}
     {L_{S,k}(3u-\tfrac12,\widetilde c_k)}
\sum_{Nd\ge R}^{*}
 \frac{a_{\xi_1}(d)\chi_k(d)\Theta_k(d;u,t)}{(Nd)^t}
              \mathcal T_{k,d}(u)
\right\|_{\ell^2(\mathcal K_Q)}
\ll Q^{1-a+\epsilon}R^{-\eta+\epsilon}
          (2+|\Im u|)^M.}
\tag{5.3}
\]

The same bound holds with any additional coefficients independent
of k and bounded by one in the d sum. All constants are uniform
on fixed compact real substrips with a positive eta margin.
The exterior ratio is the literal ratio in (1.8).

**Proof.** Substitute (5.2) into the four terms in (4.3). They
become

\[
\begin{gathered}
Q^{1/2}F^{a/2-1-\eta},\qquad
Q^{1-a}F^{-\eta},\\
Q^{3/4-a/2}F^{-1/4-\eta},\qquad
Q^{1-4a/5}F^{-3a/10-\eta}.
\end{gathered}
\tag{5.4}
\]

For `F>=Q^(2/3)`, each is bounded by
`Q^(1-a)F^(-eta)`. For the first, the ratio to that expression
is at most `Q^((4a/3)-(7/6))`, which is less than one for
`a<5/6`. For the third the ratio is at most
`Q^(a/2-5/12)`, also at most one on that strip. For the fourth
the ratio is exactly bounded by

\[
Q^{a/5}F^{-3a/10}\le1.
\tag{5.5}
\]

Decompose `Nd>=R` into the disjoint blocks
`2^jR<=Nd<2^(j+1)R`, allowing arbitrary bounded weights in each.
Equation (4.3), Minkowski over these dyadic blocks, and a loss
smaller than eta give a convergent geometric sum with size
`Q^(1-a+epsilon)R^(-eta+epsilon)`. This is an actual norm
limit, agreeing with the normally convergent divisor
representation from PR #922 on the overlap. The cube ratio is
uniformly bounded by Proposition 1.1. This proves (5.3). QED.

For example, on `a=3/4` and `b=9/8+eta`, the new bound is

\[
\|\text{tail}_{Nd\ge R}\|_2
\ll Q^{1/4+\epsilon}R^{-\eta+\epsilon},
\qquad R\ge Q^{2/3}.
\tag{5.6}
\]

The previous full-series row estimate and direct d-Minkowski
argument give only `Q^(1/2+epsilon)R^(-eta+epsilon)` at these
parameters. The new conclusion is therefore a factor
`Q^(1/4)` in the norm, or `Q^(1/2)` in the energy, for this
specified tail. This statement is about the literal continued
Dirichlet divisor expansion, with its completion and masks.

## 6. What changed, and the remaining full-series obstruction

This proof retains d and m in one squarefree product until after
the classical row sieve. The cube quotient is handled by the exact
quadratic-row expansion (2.6), rather than discarded or estimated
by an arbitrary row-dependent coefficient. That is why the
joint bound (3.1) is available.

The term FX is the obstruction in this argument. Balancing it
against `Q^2F^2/X` occurs at `X=QF^(1/2)` and produces (5.1).
For fixed Q and F tending to infinity, (5.1) has the largest
F exponent among the four terms of (4.3). Thus summing this
particular positive majorant still requires `2b+a>3`.
This is a limitation of the proved estimate, not a proof that
the actual signed series has a singularity on that plane.

Summing all F on the old domain gives a norm bounded by

\[
Q^\epsilon(2+|\Im u|)^M
\left[Q^{1/2}+Q^{1-a}+Q^{3/4-a/2}+Q^{1-4a/5}\right].
\tag{6.1}
\]

For `5/8<a<5/6`, this recovers `Q^(1/2+epsilon)` and hence
the old full-series mean. The large-divisor improvement (5.3)
does not remove the contribution of the smaller divisors,
including d=1. It supplies no new full moment exponent.

A stronger attack must use further arithmetic information in
the joint coefficient (3.3), a compatible second-axis completion,
or cancellation between the remaining Mellin blocks. The exact
cube factor (1.9) must survive any such operation.

## 7. The cubic A2 powerfree coefficient: an exact identification

The pure joint squarefree core associated to this proof is

\[
\mathscr B_k(t,u)
=\sum_{(d,m)=1}^{*}
 \frac{a_{\xi_1}(d)a_{\xi_2}(m)
          \chi_m(d)^4\chi_k(dm)}{(Nd)^t(Nm)^u}.
\tag{7.1}
\]

The coefficient in (7.1), after removing its multiplicative
angular, ray and row factors, is exactly the powerfree cubic
A2 coefficient. That arithmetic identification and its complete
coefficient extension were already established in PR #914 at
`0cc0428fedbbfc340044c7451b3d392c1da9a103`,
`standalone/2026-10-10-sextic-moment-conductor-core/A2_COMPLETION.md`,
Sections 1–4. Here it identifies the joint Dirichlet core arising
from the exact cube-adjusted representation (1.8), with the
additional fixed character kappa on its m axis. It is not a new
general A2 identification. The short reconstruction below makes
this interface explicit without importing a functional equation.

Write the cubic symbol as `(x/y)_3=chi_y(x)^2`. For two
coprime pairs `(d,m)` and `(d',m')`, the CRT identity for the
normalized cubic Gauss sums and cubic reciprocity give the
twisted multiplicativity factor

\[
\left(\frac d{d'}\right)_3^2
\left(\frac m{m'}\right)_3^2
\left(\frac d{m'}\right)_3^{-1}
\left(\frac {d'}m\right)_3^{-1}.
\tag{7.2}
\]

Indeed the two same-axis Gauss products give the exponent 2;
the two cross-axis factors also have exponent 2, which equals
-1 modulo 3. Together with the local values `1,gamma_2(p),
gamma_2(p)` at the exponent pairs `(0,0),(1,0),(0,1)`, this
uniquely determines every squarefree coprime coefficient.

Formula (7.2) is the cubic specialization of Chinta–Gunnells,
[*Constructing Weyl group multiple Dirichlet series*,
arXiv:0803.0691v2](https://arxiv.org/pdf/0803.0691v2),
equations (4.3)–(4.4), for Cartan type A2. The local coefficient
table in their [A2 paper,
arXiv:math/0703040v1](https://arxiv.org/pdf/math/0703040v1),
equations (1.4), (2.8)–(2.9), after division by `q^((i+j)/2)`, is

\[
1+\gamma_2(p)(X+Y)
 +q^{1/2}(XY^2+X^2Y)
 +q^{1/2}\gamma_2(p)X^2Y^2.
\tag{7.3}
\]

To check the normalization, use
`g(p,p^2)=q g_2(1,p)` and
`g_1(1,p)g_2(1,p)=q` for a good cubic prime, and
`gamma_2(p)=q^(-1/2)g_1(1,p)` in matching additive
normalization. A different fixed additive convention contributes
the corresponding fixed cubic character to the coefficient
family; it cannot be ignored when claiming a global identity.

The insertion vectors `(1,2)` and `(2,1)` have zero pairing
modulo 3 with both coordinate axes under the A2 Cartan matrix.
They therefore add masks, but no cubic cross-twist, to the
remaining squarefree core. The vector `(2,2)` pairs to 2 with
both axes and supplies a common cubic twist. This explains the
three correction sectors relevant to a genuine A2 completion.

Equations (7.2)–(7.3) identify coefficients. The estimates of
Sections 1–6 do not assume the global A2 analytic continuation.
Applying such a theorem to (7.1) still requires the precise
archimedean angular data, the quadratic part of the sextic row,
all local sections at the growing row conductor, the correction
terms and uniform bounds for the resulting family. In particular
the powerfree identification alone does not prove a second
functional equation for the actual function (1.8).

## 8. Validation boundary and smallest failure

Finite rational checks can verify (1.11), (2.3), the four
crossover powers and the threshold comparisons in (5.4)–(5.5).
They cannot verify the imported all-scale theta mean or the
classical sextic large sieve. The proof above uses those stated
inputs and proves the new deduction by ordinary analytic
estimates; it is not a finite-computation certificate of a global
moment theorem.

The smallest new load-bearing assertions are the exact masked
representation (1.8) and the joint row estimate (3.1). Failure
of either would invalidate Theorem 5.1. Failure of a proposed
global A2 adapter would not invalidate Sections 1–6, which do
not use that adapter.
