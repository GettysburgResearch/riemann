# Signed square-class cancellation with the original compact boundary

23 October 2026. This is a proposed additive result for one precisely
defined component of the source's inverse moment. It proves a bound for
the good quadratic square-class projection with `C=d'=j=1`, good
squarefree rows, no surviving prime marks, and the complete finite Fourier
pairing. Fixed punctures may be absorbed in the fixed set `S`; moving
punctures are excluded.
It does **not** bound the complementary nonsquare correlation or improve
the repository's global zero-free boundary.

Scaling observations for general overlap and powerful rows are not
included in the theorem below.

## 1. Pinned inputs and conventions

The arithmetic source is [OpenAI, pinned paper.tex](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`, Git blob
`268c4e3206d460c617d3d2129742a72b831b3def`, SHA256
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.
The inputs used here are:

* the initial signed expression and its exact common-divisor extraction,
  `eq:initial-formal-component`, `eq:initial-common-extraction`, and
  `eq:initial-outer-arithmetic`;
* the raw completion inversion, `eq:marked-completion-inversion`, with
  no marks in the present component;
* `prop:completed-reflection`, especially `eq:reflection`,
  `eq:reflection-row-phase`, `eq:reflection-cross-prime-phase`, and
  `eq:reflection-kernel`;
* the ordinary finite-order Hecke functional equation recorded in the
  proof of `lem:hecke-strip-growth`.

The complete finite-place identities needed in the proof are established
in [FIXED_CUSP_REINDEXING.md](FIXED_CUSP_REINDEXING.md), SHA256
`b1013b422b11ab743fe797e21c5794d1f342846fe6adb7401bd9d92bc17e970f`.
They use the explicit unconditional theta coefficients in
Dunn--Radziwill, *Bias in cubic Gauss sums: Patterson's conjecture*,
[arXiv:2109.07463v3](https://arxiv.org/html/2109.07463v3), equations
(5.7), (5.13), (5.14), (5.16), and Appendix A, rows 1, 19, and 10.
No conditional assertion about primes from that paper is used.

Work over `E=Q(omega)`, with `lambda=1+2 omega`, and write `q_a=Na`
for absolute ideal norms. Primary generators and residue characters have
the source's conventions. A good ideal is prime to the fixed finite set
`S`; all unqualified ideal sums below are over good primary ideals.
The fixed set includes the primes dividing the finite ray moduli and the
source's modulus `L`. Character powers are zero on nonunits, including
power zero. Write `alpha(a)=a/|a|`, and use the source's normalized cubic
Gauss coefficient `gamma_2(a)` only for squarefree arguments.

Fix a finite-order ray character `nu`, and put

\[
 A(n)=\overline{\alpha(n)}\gamma_2(n)\nu(n).
\tag{1}
\]

All constants below may depend on this fixed finite data and finitely many
smooth seminorms of the chosen tests. They do not depend on the row, the
common divisor, the completion divisors, or `D,H`.

## 2. The original restricted family and the projection being bounded

Let `D>=2`, `1<=H<=D^2`, and `K=D^2/H`. Choose fixed smooth annular tests
`Phi,W`, a smooth kernel `K_init` on the compact set encountered below,
and row weights `omega(R)` with `|omega(R)|<=1`. The basic original family is

\[
\begin{split}
\mathcal I(H,D)=\frac HD
\sum_{R\ {\mathrm{sf}}}&\omega(R)\Phi(q_R/K)
\sum_{\substack{z_1,z_2\ {\mathrm{sf}}\\(z_1,z_2)=1}}
\frac{A(z_1)\overline{A(z_2)}}{\sqrt{q_{z_1}q_{z_2}}}
\chi_{z_1}(R)\overline{\chi_{z_2}(R)}\\
&\quad\times W(q_{z_1}/D)\overline{W(q_{z_2}/D)}
\mathcal K_{\rm init}\!\left(\frac{Hq_R}{q_{z_1}q_{z_2}}\right).
\end{split}
\tag{2}
\]

This is the `C=d'=j=1`, unmarked, good-squarefree-row restriction of the
source's displayed principal-restored nonzero expression, with its outer
bounded arithmetic factor included in `omega`. It does not include the
separately estimated original-origin term, principal-restoration cost,
or raw-ratio complement. The source's subsequent individual `s` dyads
are not imposed here: the complete signed common-divisor sum is retained.

Insert the complete coprimality identity and set `z_i=s n_i`. Exact CRT
gives

\[
 A(sn)\chi_{sn}(R)
 =A(s)\chi_s(R)A(n)\chi_n(R)\chi_n(s)^4
\quad ((s,n)=1),
\tag{3}
\]

so the outer weight is `mu(s)/q_s`, with `(s,R)=1`. The residual `n_i`
are squarefree, prime to `s`, and need not be mutually coprime. Their
zeros are encoded by

\[
 \Psi_{R,s}(n)=\nu(n)\chi_n(R)\chi_n(s)^4.
\tag{4}
\]

After fixing the finitely many ray sectors of `R`, reciprocity writes
(4) in the reflection proposition's form with the **same** fixed character
`Psi_0` in both columns, local exponent one at primes of `R`, and local
exponent four at primes of `s`. The exponent-four reciprocity introduces
no additional moving finite character of `s`. The bounded number of row
sectors can be summed at the end.

Before any separation the complete norm profile is

\[
 F(y_R,y_1,y_2)=\Phi(y_R)W(y_1)\overline{W(y_2)}
 \mathcal K_{\rm init}(y_R/(y_1y_2)),
 \qquad y_R=q_R/K,\quad y_i=q_s q_{n_i}/D.
\tag{5}
\]

Fix once and for all a smooth Fourier separation of this compact
three-coordinate profile, using fixed annular cutoffs. Its coefficients
decay faster than every power of the three mode indices. It produces
annular column tests `V_1,V_2`, a bounded row norm mode, and **no independent
norm twist or cutoff in s**. The proof can therefore be given for one
separated term, uniformly with polynomial loss in its mode indices.
The full object below is the rapidly convergent sum of these terms.

Here is a literal definition of the projected term, including the
otherwise consequential cutoff choice. Define

\[
\begin{split}
 \mathcal T_\Psi(X;V)
 &=\sum_{n\ {\mathrm{sf}},\,b}
 \frac{\gamma_2(n)\overline{\alpha(nb^3)}\Psi(nb^3)}
 {\sqrt{q_n}\,q_b}V(q_nq_b^3/X),\\
 c_\Psi(h)&=\frac{\mu(h)\overline{\alpha(h)}^3\Psi(h)^3}{q_h}.
\end{split}
\tag{6}
\]

There is no coprimality restriction between `n` and `b`. Direct divisor
convolution, or the source's unmarked completion inversion, gives

\[
 \sum_{n\ {\mathrm{sf}}}\frac{\gamma_2(n)\overline{\alpha(n)}\Psi(n)}
 {\sqrt{q_n}}V(q_n/X)
 =\sum_{h\ {\mathrm{sf}}}c_\Psi(h)\mathcal T_\Psi(X/q_h^3;V).
\tag{7}
\]

In the divisor-convolution proof put `b h=c`; the remaining divisor
sum is `sum_(h|c) mu(h)`, and the character zero conventions persist.
In particular, here `(h,Rs)=1` automatically.

If `supp V_i` is contained in `[A_i,B_i]`, choose a fixed smooth `rho`
equal to one on `[0,B_1+B_2]` and zero beyond `2(B_1+B_2)`. Insert

\[
 \rho\!\left(q_s(q_{h_1}^3+q_{h_2}^3)/D\right)
\tag{8}
\]

in the product of (7). This is exact before reflection: a nonzero original
completed column requires `q_s q_(h_i)^3<=B_i D`. When that condition
fails the whole corresponding column is zero, so insertion is exact
also on the zero branches.

For precision define the full reflected coefficient, for each nonzero
`mu` in `lambda^(-4) O`, by the finite source formula

\[
\begin{split}
 \mathfrak R_{R,s}(X,V;\mu)
 =\sum_{h_0\bmod L}\zeta_{h_0;R,s}
 \frac{d_{H(h_0;R,s)}(\mu)\alpha(\mu)
 \vartheta_{h_0;R,s}(\lambda^4\mu)}{\sqrt{q_\mu}}
 \prod_{p\mid Rs}B_p(\lambda^4\mu)
 V^\sharp\!\left(\frac{q_\mu X}{q_{c_F}^2q_R^2q_s^2}\right).
\end{split}
\tag{9}
\]

Every prime is active in this basic exponent-one/exponent-four pattern.
The coefficients, including nonunit and zero `h_0`, are exactly those of
`eq:reflection` and `eq:reflection-row-phase`; none has been replaced by
its absolute value. In particular

\[
 B_p(x)=\chi_p(x)^{-3}\ (p\mid R),\qquad
 B_p(x)=q_p^{-1/2}(-1+q_p1_{p\mid x})\ (p\mid s).
\tag{10}
\]

Use only the following Mellin convention:

\[
 \begin{split}
 V^\sharp(x)&=\frac1{2\pi i}\int
 \widehat V(-u)\mathscr R(u)(K_0x)^{-u}\,du,\\
 \mathscr R(u)&=\prod_\pm
 \frac{\Gamma(1+u\pm1/6)}{\Gamma(1-u\pm1/6)},
 \qquad K_0=(2\pi)^4/27.
 \end{split}
\tag{11}
\]

The transform of a column in (7) therefore has the literal argument

\[
 \frac{q_\mu D}{q_{c_F}^2 q_R^2 q_s^3 q_h^3}.
\tag{12}
\]

On the support of the three theta coefficient functions, write uniquely
`mu=mu_S n b^3`, where `mu_S` contains the unit, the ramified power, and
all other `S`-supported factors, while `n` is good squarefree and `b` is
good. Define

\[
 \mathbf P_\square(h_1,h_2;\mu_1,\mu_2)
 =1_{\,h_1n_1b_1h_2n_2b_2\text{ is a square ideal}}.
\tag{13}
\]

This keeps the complete good quadratic square class, not merely
`n_1=n_2` or `b_1=b_2`. The extracted `S` factors are all retained;
their residual row characters are fixed-ray factors.

For the separated term, let `omega_m(R)` include its row mode and cutoff.
The component being estimated is the following explicit sum:

\[
\begin{split}
\mathcal D_{\square,m}(H,D)=\frac HD
\sum_{R\ {\mathrm{sf}}}\omega_m(R)
\sum_{\substack{s\ {\mathrm{sf}}\\(s,R)=1}}\frac{\mu(s)}{q_s}
\sum_{h_1,h_2\ {\mathrm{sf}}}&c_{\Psi_{R,s}}(h_1)
 \overline{c_{\Psi_{R,s}}(h_2)}
 \rho\!\left(\frac{q_s(q_{h_1}^3+q_{h_2}^3)}D\right)\\
\times\sum_{\mu_1,\mu_2\ne0}&
 \mathbf P_\square(h_1,h_2;\mu_1,\mu_2)
 \mathfrak R_{R,s}\!\left(\frac D{q_s q_{h_1}^3},V_1;\mu_1\right)
 \overline{\mathfrak R_{R,s}\!\left(\frac D{q_s q_{h_2}^3},V_2;\mu_2\right)}.
\end{split}
\tag{14}
\]

The `s,h_1,h_2` sum is finite because of (8), and the reflected sums
converge absolutely. Define `D_square` as the sum of (14) against the
fixed separation coefficients from (5). This definition fixes the tests,
separation, and common cutoff; its constants are controlled by finitely
many of their seminorms. Replacing (13) by one gives exactly (2).
Its complement gives an exact decomposition of (2), but that complement
is not estimated here. Different admissible cutoff choices can redistribute
the projected and complementary pieces, so (14) is not asserted to be a
canonical subsum of the original untransformed expression.

## 3. Theorem

**Reciprocal hypothesis at beta.** Let `2/3<beta<1`. Assume that the fixed
Dedekind zeta function `zeta_E(z)` has no zeros in `Re z>beta`, and that
for every `a>beta` its reciprocal has polynomial growth on each fixed
closed vertical strip in `Re z>=a`. At the pole `z=1` the reciprocal is
understood by its holomorphic continuation. This is a hypothesis only
about this one fixed zeta function; no reciprocal estimate with a moving
conductor is used.

**Theorem.** Under this hypothesis, for each `0<delta<1/5` and each
`epsilon>0`, the component (14), summed as specified above, satisfies

\[
 |\mathcal D_\square(H,D)|
 \ll_{\delta,\epsilon,\beta}
 (DH)^\epsilon
 \left(D^{1-3\delta}H^{2\delta}+D^\beta\right).
\tag{15}
\]

For fixed `c>0`, choosing `delta<1/5` sufficiently close to `1/5` and
then the small exponent loss sufficiently small makes (15) `O(H)` in
`H>=D^(beta+c)`. This is a conclusion only for (14). The original inverse
moment still includes the nonsquare component and the other source rows
and overlap patterns.

## 4. The finite Fourier pair and its principal common-index part

Two exact identities from the fixed-cusp note prevent a hidden finite
character from destroying the signed cancellation. To state them, let
`F_(r,j;u)(mu)` denote the complete sum over `h_0 mod L` after removing the
explicit `B_p`, `alpha(mu)`, and the factors independent of `h_0,mu`.
Keep the kernel's factor `q_(c_F)^(2u)` inside this finite sum.

First, adding a good squarefree radical `s` with local exponent four gives

\[
 F_{sr_0,\boldsymbol j;u}(\mu)
 =\phi(s)^2F_{r_0,\boldsymbol j_0;u}(\mu).
\tag{16}
\]

The exact reindexing is `h_0'=s^2 h_0 mod L`. It preserves `c_F` and
the selected cusp, changes the cusp numerator by multiplication by `s`,
and changes its inverse lower-right residue by `s^(-1)`. The additive
phases agree. In each of the three cusp cases the cusp multiplier changes
by `(c_F/s)_3`; its conjugate change is canceled by the extra exponent-four
local factor `(c_F/s)_3^(-1)`. Finite Fourier inversion contributes
`phi(s)^2`. The identity includes every nonunit and zero Fourier class.
The remaining moving-prime scalar also has modulus one and is independent
of the dual index. Both scalars cancel in the paired columns of (14).
Consequently the full pair has no extra finite character of `s`.

Second, for every good primary `b`, without requiring `(b,mu)=1`,

\[
 F_{r,\boldsymbol j;u}(\mu b^3)
 =|b|\Psi_0(b)^{-3}F_{r,\boldsymbol j;u}(\mu).
\tag{17}
\]

Here the reindexing is `h_0'=b^(-3)h_0`. The cusp multiplier is unchanged,
the additive phase acquires exactly `b^3`, and the finite Fourier weight
is `Psi_0(b)^(-3)`. The theta coefficient acquires `|b|`. The extra
additive factors in the other two cusp coefficient formulas are invariant
because primary `b` satisfies `b^3=1 mod 9` and `mu` lies in
`lambda^(-4)O`. Thus the first raw `h` phase agrees with the conjugate
second good-cube phase, and vice versa. These statements require the full
finite sum; an isolated cusp branch is not sufficient.

After removing the good cubes by (17) and extracting `S` factors, divide
each good squarefree theta coefficient by its common Gauss coefficient.
The remaining coefficient is periodic on a fixed ray group. Expand the
complete pairing in the finitely many characters of that group. For
`n_1=a c,n_2=b c`, with `a,b,c` pairwise coprime and squarefree, cubic CRT
gives

\[
 \gamma_2(ac)\overline{\gamma_2(bc)}
 =\gamma_2(a)\overline{\gamma_2(b)}
   \chi_c(a)^4\overline{\chi_c(b)^4}.
\tag{18}
\]

The angular factors of the common `c` cancel. With `w=u+v`, its series
therefore has the form

\[
 \frac{L_E(1+w,\eta_{a,b})}
 {L_E(2+2w,\eta_{a,b}^2)}
 \times\text{the explicit local removals and Ramanujan factors}.
\tag{19}
\]

The character has conductor norm at most a fixed multiple of `q_(ab)`.
If `ab!=1`, its restriction at each prime of the nonempty disjoint quotient
is a nontrivial cubic character; a fixed `S` character cannot make it
principal. Thus a pole at `w=0` occurs only for `a=b=1` and the principal
fixed-ray part of the **complete** pair. The residue still retains every
pair of `S` sectors and every `h,b` term satisfying (13).

## 5. A common absolute-convergence region and the contour order

Mellin inversion of (8) contributes

\[
 \widehat\rho(\tau)D^\tau q_s^{-\tau}
 (q_{h_1}^3+q_{h_2}^3)^{-\tau}.
\tag{20}
\]

With the inverse Mellin convention (11), the two kernels (12) contribute
the macroscopic factor `Y^w`, `Y=q_R^2/D`. Their literal powers give the
common squarefree exponent `q_c^(-1-w)` and the signed common-divisor
weight

\[
 \mu(s)q_s^{-1+3w-\tau}.
\tag{21}
\]

These signs are dictated by (12); they are not chosen by a desired Euler
factor. Choose a sufficiently small positive `epsilon_0` and begin with

\[
 \Re w=\epsilon_0/4,\qquad \Re\tau=\epsilon_0,
 \qquad \Re(u-v)=0.
\tag{22}
\]

Thus `Re u=Re v=epsilon_0/8`. The common-squarefree series is to the
right of one. Its generic signed-`s` local term has exponent
`1-2 Re w+Re tau>1`, and the parity-filtered `h,b` and unequal-squarefree
series converge absolutely. Equation (22) is a genuine common absolute
region for the Mellin representation of the finite-cutoff expression,
so the starting interchange of sums and integrals is legitimate.

Set `t=u-v`, keep `Re t=0`, and move `w` first to `Re w=-delta`, keeping
`tau` on its positive line. Along this move the generic `s` Euler factors
remain on their absolute side, and the denominator in (19) has real part
at least `2-2delta>1`. The only pole crossed is the principal pole `w=0`.
The first negative numerator gamma pole in (11) is at `-5/6`, whereas
`Re u,Re v>=-delta/2>-1/10`; no gamma pole is crossed. Cube geometric
denominators also stay holomorphic.

Compact column tests give entire Mellin transforms with arbitrary
polynomial decay in vertical strips. They absorb the polynomial gamma,
ordinary Hecke, fixed finite-sector, and reciprocal-zeta growth below.
The same bounds permit the `t` integral and vanishing horizontal edges.
The regular `w` contour retains `Re tau=epsilon_0>0`. **Only the residue
at w=0 is subsequently shifted in tau.** No Mellin--Barnes separation
of `q_(h_1)^3+q_(h_2)^3` across `tau=0` is used.

## 6. Exact residue table and the surviving compact-boundary term

On the principal `w=0` residue, the two good squarefree indices agree.
Fix `h_1,h_2,b_1,b_2` with `h_1h_2b_1b_2` a square. At a good prime
`p` not dividing `R h_1h_2`, put `q=Np` and `e_i=1_(p|b_i)`.
In the residue of the squarefree common-index series the probabilities
of `p`-valuation zero and one are `q/(q+1)` and `1/(q+1)`.
Average the product of the two **unsplit** factors (10) against these
probabilities. This gives exactly

| `(e_1,e_2)` | `d_p(e_1,e_2)` |
|---|---|
| `(0,0)` | `(q^2-q+1)/(q(q+1))` |
| `(1,0)` or `(0,1)` | `-(q-1)/(q(q+1))` |
| `(1,1)` | `(q-1)^2/q` |

For example, the first entry is
`[q/(q+1)]q^(-1)+[1/(q+1)](q-1)^2/q`.
Both `n,b` overlap possibilities are essential to this table. At a prime
of `R`, the natural zeros exclude `n,h,b,s`; this is an exact local
removal, not an averaged squarefree-row density.

The signed `s` series in this residue is consequently

\[
 \mathcal S_{h_1,h_2,b_1,b_2,R}(\tau)
 =\prod_{p\nmid SRh_1h_2}
  (1-d_p(e_1,e_2)q_p^{-1-\tau})
 =\frac{G_{h_1,h_2,b_1,b_2,R}(\tau)}{\zeta_E(1+\tau)}.
\tag{23}
\]

Equation (16) is necessary here: inserting a new fixed character of `s`
would replace the zeta denominator and would not prove the claimed
cancellation. On `Re tau>=-eta`, for fixed `0<eta<1`, generic local
factors of `G` are `1+O(q^(-2+eta))`. Forbidden primes and primes dividing
just one cube variable cost an arbitrary divisor power. A prime dividing
both cube variables costs at most `q^eta` times such a divisor factor.
There is no local denominator zero in this strip, since their magnitudes
are at least `1-q^(-1+eta)`. Therefore

\[
 |G(\tau)|\ll_{\eta,\epsilon_1}
 q_{Rh_1h_2b_1b_2}^{\epsilon_1}
 q_{\operatorname{rad}(\gcd(b_1,b_2))}^{\eta}.
\tag{24}
\]

The Mellin transform of `rho` has just one simple pole, at `tau=0`,
because `rho=1` near zero. The simple zero of `1/zeta_E(1+tau)` cancels
it. Choose `0<eta<1-beta`, with an arbitrarily small fixed margin from
`1-beta`, and move the residue's `tau` contour to `Re tau=-eta`.
The reciprocal hypothesis gives no other pole and supplies polynomial
height control. The factor `D^tau` supplies `D^(-eta)`.

Absolute summation of the remaining `h,b` terms on this new contour is
direct. The phases have modulus one, and

\[
 (q_{h_1}^3+q_{h_2}^3)^\eta
 \le q_{h_1}^{3\eta}+q_{h_2}^{3\eta}.
\tag{25}
\]

Use symmetry to take one summand on the right. The square-class condition
requires every nonconstant local `h_1,h_2,b_1,b_2` configuration to have
even total valuation, at least two. The worst terms involving the
weighted `h` have size `q^(-2+3eta)`. The simultaneous two-cube term,
including (24), is at most `q^(-2+eta)`. The remaining tails are geometric.
The product therefore converges for `eta<1/3`, with room for the small
divisor losses. This is why the theorem assumes `beta>2/3`.

The principal residue for a fixed row is bounded by

\[
 (Dq_R)^\epsilon D^{\beta-1}.
\tag{26}
\]

Small margins in the choice of `eta` are absorbed into `epsilon`.
This term is the retained original compact boundary. It cannot be
discarded by replacing the finite-cutoff expression with an unrestricted
ordered Euler product. In particular, the naive uncut primewise
cancellation on `w=0` does not by itself justify a contour shift: the
uncut common-index and signed-divisor series have no shared absolute
region there. Equations (20)--(23) resolve that ordering issue.

## 7. The regular part and its conductor sum

On `Re u=Re v=-delta/2`, the common-`c` numerator in (19) is at
`Re z=1-delta`. The ordinary finite-order Hecke functional equation,
absolute convergence to the right of one, and strip interpolation give

\[
 |L_E(1-\delta+iT,\eta_{a,b})|
 \ll q_{ab}^{\delta/2+\epsilon_1}(1+|T|)^A.
\tag{27}
\]

One obtains the indicated arbitrary small loss by using the boundary
lines `-epsilon_1` and `1+epsilon_1` in the fixed-field functional
equation from `lem:hecke-strip-growth`. Imprimitive local removals cost
divisor powers. The denominator of (19) is absolutely invertible at
`2-2delta>1`; no moving-character zero-free assertion is being used.

At a prime of `ab`, the square-class constraint forces an odd total
valuation among the `h` and cube factors. Its least decaying absolute
weight, before (27), is

\[
 q^{-1/2+\delta/2}\,q^{-1+3\delta/2}
 =q^{-3/2+2\delta}.
\tag{28}
\]

The first factor is the unequal squarefree index; the second is a minimal
opposite-side cube. A completion divisor only improves this worst
exponent. Including the conductor cost in (27) leaves
`q^(-3/2+5delta/2+epsilon_1)`, summable for `delta<1/5`.

Signed-`s` alternatives at these primes are no worse. If `p|s`, both
completion divisors are excluded, and its weight is
`q^(-1-3delta-Re tau)`; this pays for the possible large Ramanujan
factor. The worst minimal opposite-cube alternative has size
`q^(-3/2-delta-Re tau)` before (27). Outside `ab`, the nonconstant
paired `h,b` terms have size `O(q^(-2+3delta))`, while the generic `s`
term has size `O(q^(-1-2delta-Re tau))`. These Euler majorants are
absolutely summable throughout the stated range. For the principal
common character the continued zeta factor on the regular line is finite
with polynomial vertical growth, and has already had its `w=0` residue
removed in Section 6.

The still-positive `tau` line gives
`|(q_(h_1)^3+q_(h_2)^3)^(-tau)|<=1`. Thus the regular piece for one row
is bounded by

\[
 (Dq_R)^\epsilon (q_R^2/D)^{-\delta}.
\tag{29}
\]

All extracted `S`-supported indices are included in (26) and (29).
Indeed the source bound `|d(mu)|<=27 3^(k/6)|b|` gives the ramified
geometric weight `3^(-k(1/3+Re u))`, `k>=-4`. Each other `S`-supported
cube contributes `q^(-v(1+3 Re u))`. On the regular line these exponents
are `1/3-delta/2>0` and `1-3delta/2>0`; on the residue they are still
larger. Supported squarefree parts have finitely many choices. Fixed
denominators, all three cusp types, and finite ray expansions only affect
the constants and the polynomial mode bounds. This argument keeps their
complete paired coefficients for (16) before taking absolute values.

## 8. Row summation, threshold, and the remaining gap

There are `O(K)` ideals in the fixed row annulus. Summing (26) and (29)
therefore gives the unnormalized bound

\[
 K(DK)^\epsilon
 \left((K^2/D)^{-\delta}+D^{\beta-1}\right).
\tag{30}
\]

Restore the visible original factor `H/D` from (14), use `K=D^2/H`,
and reallocate the arbitrary small losses. This is exactly (15).
The rapidly convergent separation coefficients in (5) absorb the
polynomial mode losses, so the same bound holds for the full original
profile, not just a separable surrogate.

The regular threshold is

\[
 \frac{1-3\delta}{1-2\delta},
\tag{31}
\]

which tends to `2/3` as `delta` tends to `1/5` from below. At
`delta=1/7` it equals `4/5`. For `beta>2/3`, the compact-boundary term
then determines the `H>=D^(beta+c)` threshold in this component.

The complementary terms in (14) have nonsquare good quadratic argument.
They still contain the structured two-column correlation with dual norm
length `N_dual=K^2/D`. The `K+N_dual` quadratic large-sieve bound is an
operator-norm estimate; its `N_dual` term does not disappear merely
because the square-class contribution (13) has been separated. A
functional-equation estimate for the completed theta twist alone is also
insufficient: its conductor scale is `q_R^2`, its central length is
`q_R`, and even a positive mean of order `K` returns the original bound
`(H/D)K=D`, rather than the required `H`.

No estimate for that complementary signed correlation is proved here.
The general `C,d'` overlap patterns, powerful rows, moving punctures,
and prime-mark reassembly also remain outside this theorem. Consequently
this result supplies an explicit signed diagonal gain with its real
boundary term; it does not support a stronger global zero-free region.

## 9. Verification scope

`check_signed_reflection_local.py` checks the local parity/Ramanujan
algebra and the residue table using exact rational arithmetic. It also
checks the numerical exponent identities behind the convergence ranges.
It uses explicit exceptions rather than Python `assert`, and gives the
same report with and without `python -O`.

The checker is supplemental. It does not prove the reflection identity,
the finite-cusp reindexings, the Mellin-contour moves, uniform Hecke
bounds, or any nonsquare or full-row estimate. Those analytic statements
are the proof and pinned inputs above.
