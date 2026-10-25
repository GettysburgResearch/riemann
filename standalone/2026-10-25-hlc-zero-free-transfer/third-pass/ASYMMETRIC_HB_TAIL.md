# A proved far tail and a smaller remaining middle band

**Status: source-dependent component theorem.** The asymmetric smooth
Heath--Brown identity below proves a power saving for its complete
coherent outer-product tail beyond the row scale $U$. Together with the
proved smooth head, it reduces the remaining new arithmetic hypothesis
to a middle band. The middle band is not estimated here, so this is not
an unconditional improvement of the zero-free boundary.

For every prescribed bounded range
$29/25\le r\le C$, put $D=U^r$ and $\alpha=2/125$. In the exact
decomposition defined below, the new far-tail theorem is

\[
 \boxed{\quad
 \sum_u w_U(u)|M_u^{\rm far}(U,D,t;W)|^2
  \ll_\epsilon U^{(1+5r)/6-1/750+\epsilon}
                      (1+|t|)^A p_J(W)^2 .
 \quad}                                                     \tag{1}
\]

It includes every original outer product above $U$, with a fixed smooth
transition between $U$ and $2U$. Both Möbius signs, all original natural
zeros, the same physical rows, and every admitted common puncture remain.
This controls the troublesome $R\asymp D$ range in this exact identity.
It is an estimate of a coherent tail, rather than a selected short
product or a diagonal term.

On $29/25\le r\le117/100$, the complementary head through
$U^{13/20}$ is also below the inherited full-inverse exponent by more
than $1/1000$. The remaining coherent middle band has support

\[
                       U^{13/20}<Nr<2U.                    \tag{2}
\]

An estimate with a $1/1000$ saving for this middle band would therefore
supply the full inverse input of `CONDITIONAL_CONSUMER.md`. It is not
necessary to assume that saving for all larger outer products as well.

## 1. Source scope and two required estimates

Use the physical family, finite-order presentations, primary-ideal
conventions, common smooth profiles, and bounded nonnegative row weight
of `INVERSE_POWER_COMPONENT.md`. In particular,

\[
 \psi_u(n)=\nu(n)\chi_n(u)^\varsigma1_{(n,Q)=1},\qquad
 Nu\asymp U,\quad u\ {\rm sixth\!-\!power\!-\!free},
 \quad \varsigma\in\{-1,1\}.                                \tag{3}
\]

The ray data are fixed, the original natural zeros remain, and the
common puncture satisfies $N\operatorname{rad}Q\le U^{C_Q}$ for a
prescribed fixed $C_Q$. We retain the nonprincipal inducing family;
bounded principally induced exceptional presentations must have been
handled in the complete source expression. No nonzero angular character
is added to the finite-order zero-free premise. Norm heights are allowed
with a fixed polynomial cost.

The exact pinned source is
`openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
`preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`,
Git blob `268c4e3206d460c617d3d2129742a72b831b3def`.
Its `thm:main` supplies the family cap
$\operatorname{Re}\rho\le7/8$. Its
`lem:inverse-amplification` gives the actual native moment

\[
 \sum_u w_U(u)|M_{\psi_u}(U^b;V)|^2
  \ll_\epsilon U^{e(b)+\epsilon}
                   (1+|v|)^A p_J(V)^2,\qquad
 e(b)=\max\left\{1,\frac{1+5b}{6}\right\},                   \tag{4}
\]

for bounded nonnegative $b$. The external proof of the cap and the
original moment is an explicit premise, not independently certified by
the present deduction.

The common puncture version of (4) follows from the original natural
version, without changing its primitive character. If
$\psi_u=\psi_u^0 1_{(\,\cdot\,,Q)=1}$, exact Euler inversion gives

\[
 M_{\psi_u}(B;V)
   =\sum_{\operatorname{rad}h\subset\operatorname{rad}Q}
      \frac{\psi_u^0(h)}{\sqrt{Nh}}\,
          M_{\psi_u^0}(B/Nh;V).                            \tag{5}
\]

Only $Nh\ll B$ can contribute on an annulus. The scalar mass is at most
$\prod_{p\mid Q}(1-(Np)^{-1/2})^{-1}\ll_\epsilon U^\epsilon$.
The phases in (5) have modulus at most one. Since $e$ is nondecreasing,
Minkowski and (4) on the shorter scales prove (4) with the same exponent
for the admitted puncture. No independently selected mask is attached to
each row.

We also use the following global capped pointwise bound, for either a
plain or inverse block $P_{\psi_u}$ of log-length $\ell\ge0$:

\[
 |P_{\psi_u}(U^\ell;V)|^2
     \ll_\epsilon U^{3\ell/4+\epsilon}
                   (1+|v|)^A p_J(V)^2.                    \tag{6}
\]

Here $\ell$ lies in a prescribed bounded set. To obtain (6), use the
global cap and move the ordinary or reciprocal Mellin integral to
$\operatorname{Re}s=7/8+\eta$, with a small fixed $\eta>0$.
There are no primitive poles in the nonprincipal family and no zeros of
the natural Euler deletion factors in this half-plane. On a zero-free
disk centered at $3+iv$, polynomial conductor/height growth,
Borel--Caratheodory, and three-circles for the Euler-normalized
holomorphic logarithm give an arbitrarily small power bound for both
$L_{\rm orig}$ and $L_{\rm orig}^{-1}$ on that line. The conductor is
$O(U)$, the deletion radical is a prescribed power of $U$, and the
Euler logarithm on the smaller disk is uniformly bounded. Thus the same
local proof as `INVERSE_POWER_COMPONENT.md`, Section 3, applies.

For (6) there is no finite-height extrapolation: the imported cap is
global in height, so the disks are available at every height. The
pointwise bound may be written with a small power of
$U(3+|v|)$ and then weakened to the displayed fixed polynomial height
cost. Finite Mellin derivative orders control the infinite tails. This
gives $U^{2\ell(7/8-1/2)+\epsilon}=U^{3\ell/4+\epsilon}$.
The estimate uses only common profiles, and applies to their actual total
norm frequency.

## 2. An exact unequal-cutoff identity

Fix smooth cutoffs $w_0,\chi_0:[0,\infty)\to[0,1]$, equal to one on
$[0,1]$ and zero on $[2,\infty)$. Choose $\chi_0$ nonincreasing.
Set

\[
 y_1=U^\alpha,\qquad y_2=\frac{2D}{U^\alpha},\qquad
 m_i(n)=\mu_E(n)w_0(Nn/y_i),\qquad
 a_{y_1,y_2}(r)=\sum_{ab=r}m_1(a)m_2(b).                    \tag{7}
\]

The exact identity is

\[
                \mu_E=m_1+m_2-m_1*m_2*1
                           \qquad(Nn\le y_1y_2=2D).        \tag{8}
\]

Indeed, $\delta_1-m_i*1$ is supported above $y_i$; the product of these
two expressions vanishes through $y_1y_2$. Convolve by $\mu_E$ and
expand. Both cutoffs are genuinely shorter than $D$ for sufficiently
large $U$: $2y_1<D$ and $2y_2<D$. Thus $m_1+m_2$ is absent on the
original $(D,2D)$ annulus. With $V_t(x)=x^{it}W(x)$, the actual inverse
equals

\[
 M_u=-D^{-1/2}\sum_{a,b,c}
      \mu_E(a)\mu_E(b)w_0(Na/y_1)w_0(Nb/y_2)
                 \psi_u(a)\psi_u(b)\psi_u(c)
                 V_t(NaNbNc/D).                            \tag{9}
\]

No pairwise coprimality is imposed. In particular the repeated-prime
terms in the ordinary convolution remain. Complete multiplicativity with
the zero extension proves that (9) retains the same puncture and every
original row zero.

In (9), multiply the summand by one of the following outer-product
weights:

\[
\begin{split}
 \lambda_{\rm head}(R)&=\chi_0(R/U^{13/20}),\\
 \lambda_{\rm far}(R)&=1-\chi_0(R/U),\\
 \lambda_{\rm middle}(R)&=\chi_0(R/U)-\chi_0(R/U^{13/20}).
\end{split}                                                   \tag{10}
\]

The resulting coherent expressions are $M_u^{\rm head}$,
$M_u^{\rm far}$, and $M_u^{\rm middle}$ respectively.
Their sum is exactly $M_u$. For large $U$ the weights are bounded
between zero and one, but no positivity of the character sums is used.
The middle weight has exactly the support restriction (2); its two
transition intervals are part of the definition.

The asymptotic lower threshold for (8)--(9) may be large because
$\alpha$ is small. All bounded ranges are absorbed in the constants.
No assertion about a finite numerical zero-height verification is made.

## 3. Proof of the entire far-tail bound

Dyadically split $Na\asymp A$, $Nb\asymp B$, $Nc\asymp C_1$ in
(9), using common smooth windows. Write

\[
 a_0=\log_U A,\qquad b_0=\log_U B,\qquad c_0=\log_U C_1 .
\]

A nonempty triple in the far piece satisfies, up to fixed multiplicative
constants in its scales,

\[
 a_0+b_0+c_0=r,\qquad
 0\le a_0\le\alpha,\qquad
 a_0+b_0\ge1,\qquad
 b_0\le r-\alpha.
 \tag{11}
\]

In particular,

\[
                       1-\alpha\le b_0\le r-\alpha.
 \tag{12}
\]

The dyadic endpoints introduce only $O(1/\log U)$ in these equalities
and inequalities. They contribute a bounded constant to the estimates,
or may be absorbed in the final epsilon. Nonempty bounded scales are
rescaled to a fixed annulus at length zero.

The common profile for a triple is a product of the three annular
windows and

\[
 w_0(Ax/y_1)w_0(By/y_2)
 [1-\chi_0(ABxy/U)]\,
        V_t((ABC_1/D)xyz).                                 \tag{13}
\]

All fixed logarithmic derivatives are uniformly bounded, with a fixed
polynomial cost in $t$ and seminorms of $W$. A cutoff derivative is
supported where its own argument is in a fixed transition interval.
On a nonempty triple $ABC_1/D$ lies in a fixed compact set.

Logarithmic Fourier separation in the three variables expresses the
triple as an absolutely convergent weighted integral of

\[
                 M_{\psi_u}(A;V_1)\,
                 M_{\psi_u}(B;V_2)\,
                 S_{\psi_u}(C_1;V_3),                      \tag{14}
\]

with a bounded normalization factor $\sqrt{ABC_1/D}$. All three
factors use the same character (3), including its zeros. Each separated
profile is common to the row sum. The fixed weighted Fourier $L^1$
norm absorbs the polynomial costs of the actual norm frequencies in
(4) and (6); no unrelated frequency allowances are reused.

Use (6) pointwise for the first inverse and the plain factor, and use
(4) for the second inverse. The squared row norm of each product in
(14) is at most

\[
 U^{e(b_0)+\frac34(a_0+c_0)+\epsilon}
   =U^{e(b_0)+\frac34(r-b_0)+\epsilon}.                     \tag{15}
\]

This is a valid joint estimate because the two capped bounds are
pointwise on each actual row, while the remaining factor is exactly the
original Möbius polynomial in the supplied moment (4). It does not
replace a two-inverse coefficient by an arbitrary sieve coefficient.

Let $e_0(r)=(1+5r)/6$. If $b_0\ge1$, then

\[
 e_0(r)-\left[e(b_0)+\tfrac34(r-b_0)\right]
       =\frac{r-b_0}{12}\ge\frac{\alpha}{12}.               \tag{16}
\]

If $b_0\le1$, the same difference is

\[
 -\frac56+\frac r{12}+\frac{3b_0}{4}
   \ge\frac{r-1-9\alpha}{12}.                              \tag{17}
\]

Whenever $r\ge1+10\alpha$, the last quantity is at least
$\alpha/12$. Thus the exact scalar conclusion is

\[
 e(b_0)+\frac34(r-b_0)
       \le e_0(r)-\frac{\alpha}{12}
       \qquad(1-\alpha\le b_0\le r-\alpha,\
                       r\ge1+10\alpha).                   \tag{18}
\]

Taking $\alpha=2/125$ gives $1+10\alpha=29/25$ and
$\alpha/12=1/750$. Apply Minkowski to the weighted Fourier integrals
and then to the $O((\log U)^3)$ nonempty triples. This proves (1) for
the complete coherent far sum, with the reserved epsilon absorbing all
logarithmic factors and the common puncture mass.

All source, Fourier and profile orders are fixed before a consumer
chooses its small polynomial height. The usual source parameter Sobolev
argument gives the same estimate for its fixed finite-dimensional
rowwise detector choices. It does not grant arbitrary row-dependent
coefficient sequences.

## 4. The unequal-cutoff head has the same proved exponent

The proof of `INVERSE_POWER_COMPONENT.md`, Lemma 1, permits the two
different scales $y_1,y_2$ in (7). In its dyadic inverse-factor separation
one simply replaces
$w_0(Ax/y)w_0(By/y)$ by
$w_0(Ax/y_1)w_0(By/y_2)$. The logarithmic derivatives are still
uniform, the two factor exponents still add to
$\delta\log_U(AB)/2$, and both lengths remain in prescribed bounded
ranges. The normalized outer coefficient consequently has the same
fourth-moment envelope.

The ordinary reflection, natural dual restoration, conductor sectors,
small-dual-scale bound, and puncture sums in Sections 4--5 of that note
depend on this outer estimate and on its common profiles; they do not
require equality of $y_1$ and $y_2$. The ordinary fourth moment therefore
gives

\[
 \sum_u w_U(u)|M_u^{\rm head}|^2
    \ll_\epsilon U^{\Gamma_0+\epsilon}(1+|t|)^{A_0}p_{J_0}(W)^2,
 \qquad
 \Gamma_0=\frac{83}{24}-\frac{\sqrt{195}}6.                   \tag{19}
\]

This uses the printed $.51$ floor, exactly as the proved head theorem;
no adjustable-floor result is needed. In particular,

\[
 \Gamma_0<\frac{17}{15}-\frac1{1000}
        \le e_0(r)-\frac1{1000}\qquad(r\ge29/25).            \tag{20}
\]

The radical margin in (20) is the exact
$14379/62500$ squared comparison recorded in that theorem.

## 5. A smaller sufficient arithmetic hypothesis

The remaining condition can now be stated for one expression:

\[
 \sum_u w_U(u)|M_u^{\rm middle}(U,U^r,t;W)|^2
  \ll_\epsilon U^{e_0(r)-1/1000+\epsilon}
                         (1+|t|)^A p_J(W)^2,\qquad
             \frac{29}{25}\le r\le\frac{117}{100}.           \tag{M}
\]

Here $M_u^{\rm middle}$ is exactly (9)--(10), including the two unequal
cutoffs and all repeated-prime terms. This is an open hypothesis.
It is a different decomposition from the symmetric tail in
`CONDITIONAL_CONSUMER.md`; no piece from one decomposition is identified
with a piece from the other.

Since $1/750>1/1000$, (1), (19) and the Hilbert-space triangle
inequality show that (M) gives the complete original inverse bound with
the $1/1000$ saving. The rest of the certified consumer uses precisely
that full inverse bound. Hence (M) can replace the earlier sufficient
tail hypothesis in that conditional implication. The numerical endpoint
certificate itself is unchanged. No assertion that (M) has been proved
is made.

## 6. What the higher-order and joint-moment attempts leave

The asymmetric choice removes the $R\asymp D$ range that a symmetric
fourth-moment treatment did not control. It does not remove the old
critical pair inside the middle band. The distinction can be checked
explicitly using the source-compatible scalar class from
`MIXED_NUMERATOR.md`:

\[
\begin{split}
 \delta_c&=0.46934485869814306749\ldots,\\
 g_c&=\delta_c/2,\qquad
 \kappa_c=0.74977329407992826189\ldots,\\
 R_c&=0.59033235352635579359\ldots,\qquad
 r_c=1.16395357650901095632\ldots .
\end{split}                                                   \tag{21}
\]

These are the scalar comparison data from Liu's
[arXiv:2610.26835v1](https://arxiv.org/html/2610.26835v1), used with
the same qualification as in `MIXED_NUMERATOR.md`. In particular
$\kappa_c<3/4$ is granted in the following optimistic resource check;
Liu's Part II field hypotheses are not transferred to $E$. The actual
analytic theorems (1) and (19) use the original Eisenstein unmarked
moments and its finite-order $7/8$ cap.

At $g=\delta/2$, define

\[
 b_*=\frac{1-g-R}{\delta-g},\qquad
 c_*=\frac{1-g/(3\kappa)-R}
                  {2\delta-2g/(3\kappa)}.                  \tag{22}
\]

For the source's optimized $R$ and $r$ these obey $b_*+c_*=r$.
For example, writing $A=5/6-\delta$ and
$C=\delta(4-2/(3\kappa))/(2(5-2/(3\kappa)))$ gives
$r=1+C/[2(A+C)]$ and $R=1-\delta+A(r-1)$; substitution proves
the identity directly. At (21),

\[
 b_*=0.74569994272429016337\ldots,\qquad
 c_*=0.41825363378472079295\ldots .                          \tag{23}
\]

The triple of dyadic lengths $(0,b_*,c_*)$ is actually present in
(9): take the unit in the first inverse factor. Its second inverse
cutoff is identically one because $b_*<r_c-\alpha$.
The outer product has exponent $b_*$, strictly between $.65$ and $1$,
so it lies inside the remaining middle band.

The supplied marked inverse estimate at a length $b\ge1/2$ gives the
count exponent

\[
             I(b)=1-\delta b-g(1-b).                       \tag{24}
\]

It uses prime length $(1-b)/2$, within the other inverse capacity
constraint. The supplied ordinary fourth moment, with its prime length
$(1-2c)/(6\kappa)$, gives

\[
             P(c)=1-2\delta c-\frac{g}{3\kappa}(1-2c).      \tag{25}
\]

By (22), $I(b_*)=P(c_*)=R_c$. Their unmarked versions are weaker
at this class. The bin pointwise values give
$|M_{b_*}S_{c_*}|^2$ the exponent
$\delta_c(b_*+c_*)=\delta_cr_c$, so the formal combined count and
size reproduce

\[
                        R_c+\delta_cr_c=e_0(r_c).          \tag{26}
\]

This is a check on the supplied upper-bound resources, not a claim
that such rows or simultaneous exact saturations actually exist.

Two further constructions were tested against this class.

First, any fixed higher-order smooth identity follows by expanding
$\prod_j(\delta_1-m_j*1)$, with $\prod_jy_j\ge2D$.
It introduces more short inverse factors and ordinary factors. Splitting
the inverse product length $b_*$ among factors of lengths at most $b_*$
does not contradict any of their individual marked inverse bounds:
the relevant count exponent is decreasing with the inverse length and
is still at least $I(b_*)$. Similarly, splitting the ordinary length
$c_*$ does not strengthen the supplied two-plain-factor moment beyond
(25). A genuinely new joint estimate or coherent cancellation would
be needed; multiplying known individual bounds is insufficient.

Second, the inverse-power envelope in `INVERSE_POWER_COMPONENT.md`
does not remove the class. For every slope $s\ge0$,

\[
 \mathcal E(s)\ge\mathcal R(\delta_c)+s\delta_c
                    \ge R_c+s\delta_c.                    \tag{27}
\]

Thus the formal class is compatible with every supplied inverse-power
moment. For two inverse factors whose lengths sum to $\rho$, Hölder
with exponents $p,q$ gives the envelope
$\mathcal E(p a)/p+\mathcal E(q b)/q$ with $1/p+1/q=1$.
Convexity makes it at least $\mathcal E(\rho)$; no gain follows
from rebalancing those moments alone. The sharper original second moment
is what made the far-tail estimate (15) useful, but at (23) both
inverse lengths are below one and its marked refinement has the exact
contact (26).

For clarity, the further ordinary higher-moment resource tested here
is specifically the unrestricted divisor-bounded full-column sieve,
equation (6) of
`standalone/2026-10-23-structured-moment-gains/fifth-pass/SEXTIC_ROW_PHASE_CANCELLATION.md`
at `c690f96fe6876f945398b3e2779810c563a64743`,
Git blob `3a5d7adcc24ec8907be5c8fd6879d81736d44788`.
For any fixed integer $q\ge3$, the product $S_\psi(N)^q$ has common
divisor-bounded coefficients at length $N^q$. Fix a powerful physical
factor $v$ with $Nv\asymp V$; the normalized squarefree-row estimate
has cost

\[
             U/V+N^q+(UN^q/V)^{2/3}
\]

up to subpower factors. There are $O(V^{1/2+\epsilon})$ such
powerful ideals. Summing $V\le O(U)$ gives the supplied bound

\[
 \sum_u|S_{\psi_u}(N)|^{2q}
      \ll (UN)^\epsilon
              \{U+U^{1/2}N^q+(UN^q)^{2/3}\}.               \tag{28}
\]

The conductor masks and fixed $v$-phase are common column data
within each use of that sieve. For $N=U^n$, its exponent is
$\max(1,1/2+qn,2(1+qn)/3)=\max(1,1/2+qn)$; the last equality follows
by splitting at $qn=1/2$. Since $R_c+\delta_c/2<1$, for every
$s=qn\ge0$ one has
$R_c+\delta_cs\le\max(1,1/2+s)$. Thus this specific supplied
higher-moment envelope also permits the formal class. No lower
bound for the actual moments, or assertion about every possible
higher-moment theorem, is being made.

This analysis is deliberately narrower than an impossibility result.
It identifies the surviving actual middle block and why the tested
factorwise estimates permit its old contact. It does not exclude a
signed correlation estimate for the coherent middle sum, a new moment
for two inverse factors and the ordinary factor, or another arithmetic
argument that rules out the critical class.

## 7. Verification

`check_asymmetric_hb_tail.py` tests the unequal-cutoff convolution
identity with exact rational weights, the scalar bound (18) throughout
rational parameter boxes, the two endpoint identities that prove it for
the full interval, and the exact critical-pair contact formulas.
It checks negative controls for dropping repeated-prime terms and for
an inadmissibly large far-tail saving. All predicates remain active
under `python -O`.

These finite checks do not certify the imported cap, original inverse
moment, smooth head theorem, analytic Mellin shifts, or open hypothesis
(M). The claimed progress is the proved coherent far tail and the
smaller, exact residual band.
