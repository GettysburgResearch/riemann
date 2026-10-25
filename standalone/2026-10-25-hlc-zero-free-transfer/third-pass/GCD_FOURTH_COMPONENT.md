# A fourth-moment bound for the coherent gcd-ratio component

**Status: source-dependent component theorem; independent internal review
recorded in `REVIEW_GCD_FOURTH_COMPONENT.md`.**
This improves a smooth component of the actual gcd-ratio return while
retaining its complete original outer-product support, both Möbius signs,
natural zeros, primitive dual, and nonsquarefree physical rows. The
complement remains unestimated.

Let D=U^r and let the reduced numerator have dyadic norm B=U^b.
With the capped envelope in (5), the new bound is

\[
 \boxed{\quad J_B(U,D;Q)\ll_\epsilon
 (B/D)^{1/4}U^{[1+\mathcal E_{.51}(2b)]/2+\epsilon}
                     (1+|t|)^A p_J(V)^2.\quad}              \tag{1}
\]

The dyadic profile is common and smooth. For the coherent selector
$\chi_0(Na/U^{7/9})$, equal to one through one and zero from two onward,

\[
 \boxed{\quad J_{\rm gcd,head}\ll_\epsilon
 U^{179/126-r/4+\epsilon}(1+|t|)^A p_J(V)^2.\quad}             \tag{2}
\]

Throughout $29/25\le r\le117/100$, the saving is at least

\[
 \frac{1+5r}{6}-\left(\frac{179}{126}-\frac r4\right)
                     \ge\frac{17}{6300}>\frac1{1000}.        \tag{3}
\]

This is a component theorem, not a full tail estimate. It cannot be
spliced into the different original-product decomposition without
estimating the overlap.

## 1. Source premises and precise scope

Use the original sixth-power-free Eisenstein physical rows $Nu\asymp U$,
fixed finite ray data, either sextic orientation, and a common puncture
$N\operatorname{rad}Q\le U^{C_Q}$ for a prescribed fixed $C_Q$.
Write $\psi_u^0$ for the natural presentation without that extra
puncture, $\psi_u=\psi_u^0 1_{(\,\cdot\,,Q)=1}$, and $\psi_u^*$ for its
primitive inducing character. All powers retain their zero extension.

The inducing family is nonprincipal. Bounded principally induced
exceptions must be handled in the complete source expression before this
theorem is applied. This new theorem uses finite-order ray presentations
and norm heights. It does not inherit the older scalar gcd theorem's
allowance of fixed nonzero angular twists: the new coefficient bound
uses a zero-free premise for the row characters themselves.

The pinned arithmetic source is
`openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
`preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`,
Git blob `268c4e3206d460c617d3d2129742a72b831b3def`.
The imported premises are its all-family finite-order 7/8 cap, its
empty-prime-slot ordinary fourth moment, the ordinary primitive functional
equation, and common smooth-profile calculus. The buffered physical-row
counts are Xu--Sang,
[arXiv:2610.17675v2](https://arxiv.org/html/2610.17675v2),
Lemma 6.2 and Proposition 6.3, with their polynomial-height scope and
order of choices. The complete external framework is not independently
certified by this deduction.

The exact gcd return and scalar harmonic Mellin representation are proved
in `GCD_NATIVE_COEFFICIENT.md`, equations (9)--(12) and (19)--(23).
The natural dual and common conductor-profile separation are those of
`INVERSE_POWER_COMPONENT.md`, Sections 4--5. The new coefficient
argument and extra coprimality inversion are given explicitly below.

Lengths range over prescribed bounded powers of U. In the original
inverse identity use smooth cutoffs $m_i(n)=\mu_E(n)w_0(Nn/y_i)$ with

\[
             y_1y_2=2D,\qquad 2y_1<D,\quad 2y_2<D            \tag{4}
\]

for sufficiently large U. The equal choice $y_i=\sqrt{2D}$ and the
unequal choice in `ASYMMETRIC_HB_TAIL.md` are both permitted. The
complete smooth outer support through $4y_1y_2=8D$ is retained before
gcd grouping. All fixed profile derivatives are common to the row sum.

The explicit envelope is

\[
\begin{split}
 \mathcal R(\delta)&=\frac{15-16\delta}{15-6\delta},\\
 \mathcal E(s)&=\max_{0\le\delta\le3/4}
                         \{\mathcal R(\delta)+s\delta\}\\
 &=
 \begin{cases}
 1,&0\le s\le2/3,\\
 \displaystyle\frac83+\frac{5s}{2}-\frac{10}{\sqrt6}\sqrt s,
                  &2/3\le s\le200/147,\\
 \displaystyle\frac27+\frac{3s}{4},&s\ge200/147,
 \end{cases}\\
 \mathcal E_{.51}(s)&=\max\{1+s/50,\mathcal E(s)\}.
\end{split}                                                   \tag{5}
\]

On a buffered bin with $\delta=2a-1$, the above-floor count is
$U^{\mathcal R(\delta)+\epsilon}$, the bottom count is O(U) at
$\delta=1/50$, and the cap gives $\delta\le3/4$. The printed floor
is retained. The same physical bins work for additional Euler deletions:
these have no zero in the right half-plane.

## 2. Exact coprimality inversion and its k weight

Put

\[
 A_{y_1,y_2}(r)=\sum_{h_1h_2=r}
  \mu_E(h_1)\mu_E(h_2)w_0(Nh_1/y_1)w_0(Nh_2/y_2),
 \qquad
 C_a(P;y_1,y_2)=\sum_{(d,P)=1}\frac{A_{y_1,y_2}(ad)}{Nd}.
                                                               \tag{6}
\]

These sums are finite. Put $P_u=\operatorname{rad}(\mathfrak f_u Q_s)$,
including the primitive conductor, all redundant natural deleted primes,
and the common extra puncture Q. The exact reduced component is

\[
\begin{split}
 M_{u,B}={}&-\varepsilon_u\sqrt{D/\mathcal C_u}
 \sum_a\frac{\eta(Na/B)\psi_u(a)C_a(P_u;y_1,y_2)}{Na}\\
 &\quad\times
 \sum_{e\mid Q_s}\frac{\mu_E(e)\psi_u^*(e)}{Ne}
 \sum_{b:(a,b)=1}\overline{\psi_u^*(b)}
       \Phi_t\!\left(\frac{NbD}{\mathcal C_uNaNe}\right).
\end{split}                                                   \tag{7}
\]

Here eta is a common smooth annular profile, $\mathcal C_u$ is the
primitive conductor scale including the fixed field constant, and $Q_s$
is the common deleted radical in a fixed bad-place sector. It is not
inserted into $\mathcal C_u$. Define $J_B=\sum_u w_U(u)|M_{u,B}|^2$.

Insert $1_{(a,b)=1}=\sum_{k\mid a,b}\mu_E(k)$ and set
$a=kA,b=kB'$. Only squarefree k remain. On the original support,

\[
 \psi_u(k)\overline{\psi_u^*(k)}=1_{(k,P_u)=1}.
\]

The kernel depends on $NB'/NA$, so k cancels from its argument. The
fixed-k term is exactly

\[
\begin{split}
 M_{u,B,k}={}&-\frac{\mu_E(k)}{Nk}1_{(k,P_u)=1}
 \varepsilon_u\sqrt{D/\mathcal C_u}
 \sum_A\frac{\eta(NA/R)\psi_u(A)C_{kA}(P_u;y_1,y_2)}{NA}\\
 &\quad\times
 \sum_{e\mid Q_s}\frac{\mu_E(e)\psi_u^*(e)}{Ne}
 \sum_{B'}\overline{\psi_u^*(B')}
       \Phi_t\!\left(\frac{NB'D}{\mathcal C_uNA\,Ne}\right),
 \qquad R=B/Nk.
\end{split}                                                   \tag{8}
\]

The original component is the coherent sum of (8). Nonempty terms have
$Nk\ll B$. There is no residual coprimality condition on $A,B'$.

The weight is $(Nk)^{-1}$, not $(Nk)^{-1/2}$. In central normalization,
replacing a by kA gives one square root of that weight and replacing the
dual variable by kB' gives the other. The actual ordinary dual scale is
$\mathcal C_uNA\,Ne/D$, independent of k except through A.

## 3. Safe Euler factors for the modified coefficient

Fix $\beta>7/8$ close to 7/8 and put $\theta=1-\beta\in(0,1/8)$.
For a finite radical P let

\[
 F_P(v)=\zeta_E(v)^{-1}\prod_{p\mid P}(1-(Np)^{-v})^{-1}.
\]

The companion's exact scalar Mellin formula, on $(a,P)=1$, is

\[
 C_a(P;y_1,y_2)=\frac1{(2\pi i)^2}
 \int_{(-\theta)}\int_{(-\theta)}
 F_P(1+s)F_P(1+z)y_1^sy_2^z\,
       \mathfrak b_a(s,z)\widehat w_0(s)\widehat w_0(z)
                                         \,ds\,dz .         \tag{9}
\]

Both integrals are absolutely convergent. Their earlier shifts cross no
residue: the poles of $\widehat w_0$ at zero cancel against $F_P(1)=0$.
The scalar cap gives

\[
 |F_P(\beta+i\tau)|\ll_{\beta,\epsilon}
                                (NP(3+|\tau|))^\epsilon.    \tag{10}
\]

The coefficients $\mathfrak b_a$ are multiplicative and supported on
cubefree ideals. At a good prime of norm q set
$x=q^{-s},y=q^{-z},\Delta_p=(1-x/q)(1-y/q)$. The local values are

\[
 \mathfrak b_1=1,\qquad
 \mathfrak b_p=-\frac{x+y-xy/q}{\Delta_p},\qquad
 \mathfrak b_{p^2}=\frac{xy}{\Delta_p}.                       \tag{11}
\]

The $xy/q$ term is the essential repeated-prime term checked in
`TAIL_RETURN.md`.

Fix squarefree k and a row with $(k,P_u)=1$. Initially for
$\operatorname{Re}w>1+\theta$, define

\[
 \mathcal A_{u,k}(w;s,z)
   =\sum_A\frac{\mathfrak b_{kA}(s,z)\psi_u(A)}{(NA)^w}.
                                                               \tag{12}
\]

At $p\mid k$ its local factor is
$\mathfrak b_p+\mathfrak b_{p^2}\psi_u(p)q^{-w}$; the second
coefficient is $\mathfrak b_{p^2}$, not $(\mathfrak b_p)^2$.
At $p\nmid kP_u$ it is
$D_p(T)=1+\mathfrak b_pT+\mathfrak b_{p^2}T^2$ with
$T=\psi_u(p)q^{-w}$.

Let $L_{\psi_u}^{(k)}$ be the natural L function with additional k
Euler factors deleted. The exact factorization is

\[
 \mathcal A_{u,k}(w;s,z)=
 \frac{K_{u,k}(w;s,z)H_{u,k}(w;s,z)}
 {L_{\psi_u}^{(k)}(w+s)L_{\psi_u}^{(k)}(w+z)},                \tag{13}
\]
where
\[
\begin{split}
 K_{u,k}&=\prod_{p\mid k}
       \{\mathfrak b_p+\mathfrak b_{p^2}\psi_u(p)q^{-w}\},\\
 H_{u,k}&=\prod_{p\nmid kP_u}
  \frac{D_p(\psi_u(p)q^{-w})}
       {(1-x\psi_u(p)q^{-w})(1-y\psi_u(p)q^{-w})}.
\end{split}                                                   \tag{14}
\]

No $D_p^{-1}$ or $\mathfrak b_p^{-1}$ is taken. Both can vanish
in situations not excluded by nonvanishing of the ordinary local
factors. The k factors are kept explicitly.

The needed correction estimate follows from

\[
\begin{split}
 D_p(T)-(1-xT)(1-yT)
  ={}&\frac{-(x^2+xy+y^2)/q+xy(x+y)/q^2}{\Delta_p}\,T\\
    &+\frac{xy(1-\Delta_p)}{\Delta_p}\,T^2 .
\end{split}                                                   \tag{15}
\]

On $\operatorname{Re}s=\operatorname{Re}z=-\theta$,
$|x|=|y|=q^\theta$, and Delta is bounded away from zero at each prime
uniformly in both heights. For $\sigma=\operatorname{Re}w>2\theta$
the ordinary local denominators are nonzero and the correction product
is absolutely convergent. Its leading errors are

\[
       O(q^{2\theta-1-\sigma})
                   +O(q^{3\theta-1-2\sigma}).               \tag{16}
\]

On $\sigma=a+\theta+8e$ their summability exponents are
$a+\beta+8e$ and $2a+\beta+16e$. Both exceed one by a fixed amount,
because $a\ge.51$ and $\beta>7/8$. Thus $H_{u,k}$ is uniformly bounded
on the needed strip, independently of row, deleted primes and heights.
Its local factors may have zeros; only an upper bound is used.

Each explicit k factor is $O_\beta(q^\theta)$ there. Absorbing fixed
per-prime constants by a subpower divisor bound gives

\[
               |K_{u,k}|\ll_{\beta,\epsilon}
                                      (Nk)^{\theta+\epsilon}. \tag{17}
\]

The incomplete L functions have the same primitive zeros as the original
presentation. Their extra radical is a prescribed power of U, because
$Nk\ll B$. Thus the original buffered reciprocal estimate applies without
new bin assignments or a density theorem for a new family.

## 4. The fixed-k pointwise estimate and fourth moment

Define the actual normalized outer block

\[
 Z_{u,k}(R;W)=R^{-1/2}\sum_A C_{kA}(P_u;y_1,y_2)
                                     \psi_u(A)W(NA/R).     \tag{18}
\]

It is used only on $(k,P_u)=1$; otherwise its fixed-k term (8) is zero.

**Lemma.** On a buffered bin with $\delta=2a-1$,

\[
 |Z_{u,k}(R;W)|\ll_\epsilon
 (B/D)^\theta R^{\delta/2}(Nk)^\epsilon U^\epsilon
                   (1+|v|)^A p_J(W),\qquad R=B/Nk.          \tag{19}
\]

**Proof.** Substitute (9) into the finite block. For fixed s,z, Mellin
inversion of W starts on the absolutely convergent line
$\operatorname{Re}w=2$ in (12). In the bounded-height portion, shift to
$\operatorname{Re}w=a+\theta+8e$. Both reciprocal arguments in (13)
then have real part $a+8e$ and lie in the same row's buffered rectangle.
The reciprocal estimate, (16), and (17) give normalized scale

\[
              (Nk)^\theta R^{a+\theta-1/2}U^{O(e)+\epsilon}.
\]

The real cutoff weight is
$(y_1y_2)^{-\theta}=(2D)^{-\theta}$. Thus, up to a fixed constant,
the scale is exactly

\[
 D^{-\theta}(Nk)^\theta R^{\theta+\delta/2}
                      =(B/D)^\theta R^{\delta/2}.           \tag{20}
\]

The scalar factors (10) cost only an allocated subpower and an integrable
polynomial in the s,z heights.

The frequency restrictions are essential. First choose the source's
internal orders and its positive polynomial buffer $H_1=U^\tau$.
Restrict the imaginary parts of s,z, the norm height of W, and every
other separation frequency entering the same argument to fixed small
shares of that buffer. The truncated w contour uses another share.
Each actual argument w+s or w+z, including the profile's norm twist,
then lies inside the assigned rectangle. The allowance is shared; no
contour receives an independent full copy of the buffer.

The remaining w tails and horizontal joins are estimated on the
absolute line or in that same rectangle. Their external Mellin decay
order is chosen after tau. The uniform strip bounds (16)--(17) give
any desired small power error, at a fixed finite seminorm cost.

For the discarded large s,z or profile frequencies, no inverse contour
is shifted. The coefficient bound
$|\mathfrak b_{kA}|\ll(Nk)^\theta(NA)^\theta d_E(kA)^C$
gives the trivial normalized bound
$(Nk)^\theta R^{\theta+1/2}U^\epsilon$.
Relative to the desired buffered estimate, this costs at most a fixed
power of U, since all lengths are bounded powers. If a frequency exceeds
a fixed fraction of $U^\tau$, that cost is absorbed by one fixed
polynomial in that frequency. The rapid decay of $\widehat w_0$ on
the line $-\theta$, and the external profile Fourier decay, make the
full integrals convergent with that polynomial weight. Those derivative
orders are selected after tau and do not change the inherited buffer.

A later detector may reduce its own norm-height exponent after the new
finite profile and polynomial height orders are known. That consumer
choice is distinct from the already fixed source buffer; no source
rectangle is enlarged. The proof does not assume that the polynomial-height
density input holds at arbitrary Mellin heights. QED.

Raise (19) to the fourth power and sum over the original physical bins,
including their printed floor. For $R=U^\rho\ge1$,

\[
 \sum_u w_U(u)1_{(k,P_u)=1}|Z_{u,k}(R;W)|^4
 \ll_\epsilon (B/D)^{4\theta}
       U^{\mathcal E_{.51}(2\rho)+\epsilon}
                         (1+|v|)^A p_J(W)^4.               \tag{21}
\]

The k subpower is absorbed using $Nk\ll B$. Nonempty scales below one
are bounded below by a fixed support constant and rescale to length zero.
This is a new bound proved by the actual Euler factorization and physical
row count. A row-dependent coefficient has not been submitted to an
arbitrary-coefficient moment theorem.

## 5. The natural ordinary dual and harmonic k sum

Convert the inner dual sum in (8) to central normalization. Restore the
fixed bad-place redundant zeros by the geometric Euler expansion indexed
by h, retaining all primitive values. On a primitive-conductor sector
$\mathcal C_u\asymp\mathcal C_*$ and dual norm dyad N, the exact
normalizer before common-profile separation is

\[
 \frac1{Nk}\frac1{\sqrt{Ne\,Nh}}\sqrt{\frac N{L_0}},
 \qquad L_0=\frac{\mathcal C_*R\,Ne}{D\,Nh}.                  \tag{22}
\]

The root number, primitive values at e,h, and indicator $(k,P_u)=1$
are bounded row scalars. The primitive conductor remains separate from
the puncture and k.

The common kernel in the conductor ratio, outer ratio NA/R, and dual
ratio Nn/N separates as in `INVERSE_POWER_COMPONENT.md`, equations
(24)--(26). Its normalized outer factor is precisely (18), with a common
smooth profile. The ordinary factor is the conjugate original natural
family without the extra Q puncture, after the fixed bad-place restoration.
Its supplied fourth moment is $U^{1+\epsilon}$ at every prescribed
bounded-power length.

Hölder with (21) and the ordinary fourth moment gives

\[
 \|M_{\cdot,B,k}\|_2\ll_\epsilon
 \frac1{Nk}(B/D)^\theta
 U^{[1+\mathcal E_{.51}(2\rho)]/4+\epsilon}
                  (1+|t|)^A p_J(V),\qquad
 \rho=\log_U(B/Nk).                                        \tag{23}
\]

The summations implicit in (23) have the following precise bounds.

- The dual prefactor is retained:
  $\sum_N\sqrt{N/L_0}(1+N/L_0)^{-J}\ll1$, also for $L_0<1$.
- The fixed bad-place h sum has summable $(Nh)^{-1/2}$ mass.
- The growing common e sum has subpower
  $\sum_{e\mid Q_s}(Ne)^{-1/2}$ mass.
- Conductor sectors and common dyadic profiles cost logarithmic factors.
- Beyond a prescribed bounded-power dual norm, rapid decay and a trivial
  bound control the infinite tail. The ordinary moment is used only
  inside its stated length range.

The extra outer coefficient depends on the original row through $P_u$,
but (21) already controls that dependence. Only the ordinary factor is
submitted to the supplied common-profile moment. No independent
row-selected column sequence enters that theorem.

Since $\mathcal E_{.51}$ is nondecreasing and $Nk\ge1$, replace its
argument in (23) by 2b. Minkowski over the exact coprimality inversion
then costs

\[
                   \sum_{Nk\ll B}\frac1{Nk}\ll\log(2B).     \tag{24}
\]

This is the harmonic ideal sum, not a divisor count for a single ideal
and not a square-root harmonic sum. Squaring proves

\[
 J_B\ll_\epsilon (B/D)^{2\theta}
 U^{[1+\mathcal E_{.51}(2b)]/2+\epsilon}
                         (1+|t|)^A p_J(V)^2.                \tag{25}
\]

For a final epsilon, choose $\beta=7/8+\eta$ sufficiently close to
7/8 first. Then $2\theta=1/4-2\eta$. Since B,D lie in prescribed
bounded-power ranges and B is at least one, changing this to the exponent
1/4 costs only the allocated epsilon. This proves (1). Constants may
depend on beta; no uniform limiting assertion at beta=7/8 is made.

## 6. The smooth head and its exact uniform margin

Replace the annular ratio profile in (7) by $\chi_0(Na/U^{7/9})$ and
use a common smooth dyadic partition. This is a smooth cutoff theorem.
A literal sharp terminal dyad is not licensed by the buffered inverse
argument.

The exponent in (1) increases with b, including its positive b/4 scalar
contribution. The coherent dyadic norms are therefore bounded by their
endpoint. At b=7/9, the capped linear branch dominates the printed floor:

\[
 \mathcal E_{.51}(14/9)=\frac27+\frac76=\frac{61}{42}.
\]

Thus

\[
 \frac{b-r}{4}+\frac{1+\mathcal E_{.51}(2b)}2
       =\frac9{14}+b-\frac r4
       =\frac{179}{126}-\frac r4.                           \tag{26}
\]

This proves (2). Its exact saving is

\[
 \frac{1+5r}{6}-\left(\frac{179}{126}-\frac r4\right)
   =\frac{13r}{12}-\frac{79}{63}
   \ge\frac{17}{6300}\quad(r\ge29/25).                      \tag{27}
\]

The reserve beyond 1/1000 is exactly $107/63000$.

The general formula also allows b=39/50=.78, giving
$9/14+.78-r/4$. At the actual critical length its saving is about
0.00475923; at r=29/25 its saving is only 1/2100. That larger cutoff
is not used to claim a uniform 1/1000 saving on the whole consumer
interval.

The cutoff 7/9 exceeds the old critical inverse-product length
0.7456999427..., but the reduced numerator is the reflected outer product
divided by its gcd with the dual variable. The full coefficient (6)
combines every original outer scale before a norm is taken. Inserting
an original-product selector changes that coefficient and requires a
separate proof. The exact selector-return issue is examined separately
in `RATIO_CUTOFF_RETURN.md`; no overlap estimate is inferred here.

The complementary reduced-ratio component with weight
$1-\chi_0(Na/U^{7/9})$ remains open. A suitable 1/1000 saving for that
complete component would combine with (2) to supply the full inverse
input on the consumer interval. This is a conditional implication,
not a proof of the missing complement.

## 7. Verification limits

`check_gcd_fourth_component.py` checks the local multiplicative
coefficient factorization, modified k-prime factors, exact coprimality
inversion and k^{-1} normalization, and rational envelope margins.
Negative controls replace $\mathfrak b_{p^2}$ by
$(\mathfrak b_p)^2$, drop the repeated-prime term, or replace k^{-1}
by k^{-1/2}. It also checks an exact allowed local configuration with
$\mathfrak b_p=0$ and $\mathfrak b_{p^2}\ne0$, showing why the
modified factor must not be normalized by $\mathfrak b_p$.
All predicates remain active under `python -O`.

These finite checks do not certify the imported cap or density theorem,
ordinary fourth moment, analytic buffer argument, or unproved complement.
Those premises and limitations remain attached to the theorem.



