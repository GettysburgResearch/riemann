# FFPS cyclic source realization: the \(2k\)-th-root gauge and hard/soft gate

Status: **exact fixed-fibre source theorem, exact ternary hard/soft control,
and exact Wick firewall**. No varying-conductor moment is proved.

## Start here

The common-order mask in `FFPS_CYCLIC_CHARACTER_MASKS.md` does have an exact
realization on the corrected physical coordinates of live PR #751, but only
after the same kind of owner orientation that repaired the quadratic
checkerboard.

Let \(p\) be prime, let \(2k\mid p-1\), and choose an even multiplicative
character \(\theta_p\) of exact order \(k\). It has a root \(\xi_p\) of exact
order \(2k\), with \(\xi_p^2=\theta_p\). In a fixed owner quadratic sector
\(u_p(\mathbf F_p^\times)^2\), define

\[
 \boxed{
 \epsilon_{p,u_p}(x)=\xi_p(x/u_p)\in\mu_k,
 \qquad x\in u_p(\mathbf F_p^\times)^2.}
\tag{1}
\]

For the source representation \(x=Pc^2\), this is exactly

\[
 \boxed{
 \epsilon_{p,u_p}(Pc^2)
 =\xi_p(P/u_p)\theta_p(c).}
\tag{2}
\]

Thus the value is a function of the physical Kummer coordinate \(Pc^2\), not
of its owner/core presentation. The raw core character \(\theta_p(c)\) is not
physical. The smallest ternary witness is modulo \(7\):

\[
 (P,c)=(1,1),\qquad(P',c')=(4,3),\qquad
 Pc^2=P'c'^2=1.
\]

The two raw order-three values have exponents \(0\) and \(1\), while both
oriented values in (2) have exponent \(0\).

On one live bilateral fibre, put

\[
 X=Pc^2\pmod\rho,\qquad Y=Qd^2\pmod\ell,
\]

and choose exact-order-\(k\) characters on both sides. Then

\[
 \Phi(X,Y)=\epsilon_{\rho,u_\rho}(X)
             \epsilon_{\ell,u_\ell}(Y)\in\mu_k
\tag{3}
\]

is a corrected physical quotient character. Retaining
\(\Phi\in S\), \(|S|=t\), gives exactly the hard cyclic mask of the preceding
packet. Its nonconstant Fourier powers are exactly the live L-106120
double-nonprincipal channels

\[
 (\eta^r,\theta^r),\qquad1\le r<k,
\tag{4}
\]

with roots \((\chi^r,\psi^r)\). This spectral identification does **not**
perform the hard deletion or re-invert the restricted Gram.

The \(k=3,t=2\), \((\ell,\rho)=(7,13)\) control is the decisive small example:

\[
 \boxed{
 L_{\rm hard}={27\over49}
 <L_{\rm full}={9\over14}
 <L_{\rm soft}={135\over182}.}
\tag{5}
\]

The hard mask improves the frame, while the same zero-extended weight is
strictly worse in the complete inverse metric. After Wick normal ordering,
the positive hard inequality still leaves the exact atomic residual

\[
 \boxed{
 {27\over49}(7-1)(13-1)-\left({3\over2}\right)^2
 ={7335\over196}>0.}
\tag{6}
\]

There is an exact signed centered identity using all three rotated hard masks
and the two selected Kummer modes. It cancels literal atoms, but its global
varying-conductor estimate remains open.

The machine-readable entry point is `exact_theorems` in
`ffps_cyclic_source_realization_gate.json`. Sections 2, 4, and 6 are the
shortest proof path.

## 1. Frozen source contract

This packet commit-, blob-, hash-, schema-, and payload-locks both prerequisite
packets:

- `FFPS_CYCLIC_CHARACTER_MASKS.md` and its canonical JSON at
  `5724d30a9ddd91a489312a9d09512587c4c028c1`;
- `FFPS_CHECKERBOARD_SOURCE_BRIDGE.md` and its canonical JSON at
  `09b74682ad6fce3ebfcc5012b246825c0fb5a740`.

It also locks at live PR #751 head
`98af0db6ec7f77d6333a77a3dac53c4698852f43` every claim locked by the
checkerboard bridge. The load-bearing rows are:

| claim | role |
|---|---|
| L-106024 | local sign-pair Gram \(pI-J\) |
| L-106120 | bilateral variables, even characters, and their roots |
| T-106121 | corrected physical coordinates \(Pc^2,Qd^2\) |
| R-106122 | owner/core Kummer coupling |
| R-106123 | varying-conductor positive-sum firewall |
| R-106131 | complete-family atomic cardinality |
| L-106131 | exact Wick additive/Kummer decomposition |
| T-106140 | live WCADD/WCKUM conjunction and summation discipline |

All residue, character-root, metric, and Wick algebra closes before those
sources are inspected.

## 2. The exact \(2k\)-th-root orientation

Write \(p-1=2m\). An exact-order-\(k\) character on
\(\mathbf F_p^\times/\{\pm1\}\) exists exactly when \(k\mid m\), equivalently
\(2k\mid p-1\). Its lift \(\theta_p\) to \(\mathbf F_p^\times\) is even.

The character group of \(\mathbf F_p^\times\) is cyclic of order \(2m\).
Every even character is a square in that group. To track the exact order
without confusing the ambient exponent, take the unique character subgroup
of order \(2k\) and a generator \(\gamma\). An exact-order-\(k\) character is

\[
 \theta_p=\gamma^{2a},\qquad(a,k)=1.
\]

Its two roots in that subgroup are \(\gamma^a\) and
\(\gamma^{a+k}\). At least one of \(a,a+k\) is coprime to \(2k\), so at
least one root has exact order \(2k\). Call it \(\xi_p\). The other square
root in the full character group is \(\xi_p\kappa_p\).

Since \(x/u_p\) is a square,

\[
 (\xi_p\kappa_p)(x/u_p)=\xi_p(x/u_p).
\]

So (1) is independent of the choice between the two roots. Equation (2)
follows multiplicatively:

\[
 \xi_p(Pc^2/u_p)=\xi_p(P/u_p)\xi_p(c)^2
 =\xi_p(P/u_p)\theta_p(c).
\]

This identity proves physical-collapse invariance without selecting a source
presentation. The producer exhausts only the tiny \(p=7,13\), \(k=3\)
controls, in both owner quadratic sectors: on every physical fibre the
oriented exponent is a singleton, while the raw core exponent mixes on some
fibre. Each oriented value occurs equally often.

There is also a finite-field formula after a primitive \(k\)-th-root alignment.
If \(x/u_p=g^{2a}\), then

\[
 \epsilon_{p,u_p}(x)=\zeta_k^a.
\tag{7}
\]

Equivalently, \((x/u_p)^{(p-1)/(2k)}\) is the corresponding element of
\(\mu_k(\mathbf F_p)\). Aligning these finite-field root groups with one
abstract \(\mu_k\) is a choice when \(k>2\).

## 3. Gauge dependence is exactly quotient relabelling

Replace the sector representative by \(u'_p=u_pr^2\). Then

\[
 \boxed{
 \epsilon_{p,u'_p}(x)
 =\theta_p(r)^{-1}\epsilon_{p,u_p}(x).}
\tag{8}
\]

This multiplier is constant throughout the owner sector. In a bilateral
product, changing either sector representative therefore rotates every value
of \(\Phi\) by one fixed element of \(\mu_k\). It carries the labelled retained
set \(S\) to a translate. Cardinality, Gram denominator, sharp weight, and
leverage are unchanged.

For \(k=2\), this was merely a swap of the plus/minus labels. For \(k>2\), it
is a cyclic rotation. Replacing a primitive character by
\(\theta_p^a\), \((a,k)=1\), applies the automorphism \(z\mapsto z^a\).
Consequently:

- each fixed choice produces a legitimate physical hard mask;
- the full orbit of masks is gauge-stable;
- a labelled higher-order mask is not canonical without character, root-group
  alignment, sector, and retained-set conventions.

The two square roots of one fixed \(\theta_p\) do not add another dependence:
they agree in (1).

## 4. Exact identification with the live L-106120 channels

Use live notation. On the \(\ell\)-side,

\[
 Y=Qd^2,\qquad\eta=\chi^2,
\]

and on the \(\rho\)-side,

\[
 X=Pc^2,\qquad\theta=\psi^2.
\]

Choose \(\eta,\theta\) of one common exact order \(k\) and roots
\(\chi,\psi\) of exact order \(2k\). Then

\[
\begin{aligned}
 \epsilon_{\ell,u_\ell}(Y)
 &=\chi(Q/u_\ell)\eta(d),\\
 \epsilon_{\rho,u_\rho}(X)
 &=\psi(P/u_\rho)\theta(c).
\end{aligned}
\tag{9}
\]

Therefore \(\Phi\) differs from the coefficient of the L-106120 member

\[
 \chi(Q)\eta(d)\psi(P)\theta(c)
\tag{10}
\]

only by the fixed sector scalar
\([\chi(u_\ell)\psi(u_\rho)]^{-1}\). More generally,
\(\Phi^r\) is, up to the corresponding fixed scalar, the member indexed by
\((\eta^r,\theta^r)\), with roots \((\chi^r,\psi^r)\).

Exact common order is load-bearing. For every \(1\le r<k\), both
\(\eta^r\) and \(\theta^r\) remain nonprincipal. If \(k\) is composite their
orders may fall, but neither becomes principal. Hence every nonconstant
Fourier mode of the hard mask lies in the double-nonprincipal part of the
existing Kummer family.

This proves spectral containment, not analytic control. In particular:

- WCKUM106140 is a signed global sum over all normal-ordered nonprincipal
  channels; membership does not bound a selected weighted subcombination;
- a soft character estimate acts in the complete frame;
- it does not delete source atoms before squaring and does not create
  \(G_A^{-1}\).

## 5. The exact ternary hard/soft separation

Take

\[
 (\ell,\rho)=(7,13),\qquad k=3,\qquad S=\{1,\zeta_3\},\qquad t=2.
\]

The local physical square cosets have sizes \(3\) and \(6\). Each product
quotient value occurs six times, so the hard support has \(12\) of the
\(18\) coordinates. With

\[
 G=(7I_3-J_3)\otimes(13I_6-J_6),
\]

every restricted row sum is \(49\), and

\[
 \mathbf1_A^*G_A\mathbf1_A=588.
\]

The unique sharp retained weight is \(3/2\), and

\[
 L_{\rm hard}={18^2\over588}={27\over49}.
\]

The complete constant-mode leverage is

\[
 L_{\rm full}={18\over(3+1)(6+1)}={9\over14}.
\]

Evaluating the same zero-extended weight in the complete inverse metric keeps
its nonconstant Fourier energy:

\[
\begin{aligned}
 L_{\rm soft}
 &= {N\over Q}+{N(1-\rho_S)\over\rho_S P},\\
 \rho_S&={2\over3},\quad N=18,\quad Q=28,\quad P=91,\\
 L_{\rm soft}&={9\over14}+{9\over91}={135\over182}.
\end{aligned}
\tag{11}
\]

This proves (5). The hard improvement is real, and the complete-frame soft
surrogate moves in the opposite direction.

## 6. The Wick obstruction and the centered repair

Let

\[
 O_j={k\over t}\sum_{\Phi\in\zeta_k^jS}z_\omega,
 \qquad0\le j<k,
\tag{12}
\]

and write

\[
 c_r={1\over t}\sum_{s\in S}s^{-r},
 \qquad
 H_r=\sum_\omega\Phi(\omega)^r z_\omega.
\tag{13}
\]

The Fourier expansion of the hard observation has constant coefficient one.
Parseval gives

\[
 \sum_{r=1}^{k-1}|c_r|^2={k\over t}-1.
\tag{14}
\]

Each retained atom contributes \((k/t)^2|z_\omega|^2\) to \(|O_j|^2\),
while its complete two-phase diagonal is
\((\ell-1)(\rho-1)|z_\omega|^2\). Thus the normal-ordered hard inequality
contains

\[
 \left[L_{k,t}(\ell-1)(\rho-1)-\left({k\over t}\right)^2\right]D_j.
\tag{15}
\]

In fact the obstruction is universal, not merely a ternary accident. For a
\(d\)-prime tensor set

\[
 A={Q\over N},\qquad B={P\over N},\qquad
 D_0=\prod_i(p_i-1)=2^dN,\qquad \varrho={t\over k}.
\]

Then

\[
 L={1\over A\varrho^2+B\varrho(1-\varrho)},\qquad
 R_{\rm atom}=LD_0-\varrho^{-2}.
\]

The two exact density thresholds are

\[
 \varrho_{\rm atom}={B\over D_0-A+B},\qquad
 \varrho_{\rm imp}={A\over B-A},
\tag{15a}
\]

where \(R_{\rm atom}>0\) exactly above the first threshold, and strict leverage
improvement occurs exactly above the second. Their ordering reduces to

\[
 \varrho_{\rm imp}>\varrho_{\rm atom}
 \Longleftrightarrow
 AD_0>(B-A)^2
 \Longleftrightarrow
 2^dQN^2>(P-Q)^2.
\tag{15b}
\]

The last inequality holds for every eligible distinct-prime panel. For
\(d=1\), writing \(m=(p-1)/2\), its difference is
\(m^2(2m+1)>0\). For \(d\ge2\), it is enough to prove the stronger
\(P^2<2^dQN^2\). The factor ratio is

\[
 r(m)={(2m+1)^2\over2m^2(m+1)}.
\]

It is strictly decreasing for \(m\ge2\), since

\[
 {d\over dm}\log r(m)
 ={4\over2m+1}-{2\over m}-{1\over m+1}<0.
\]

Every eligible local dimension is at least two, and distinct primes permit
\(m=2\) at most once. Without \(m=2\), every factor is at most
\(r(3)=49/72<1\). If \(m=2\) occurs, pair it with one other factor:

\[
 r(2)r(3)={25\over24}{49\over72}={1225\over1728}<1.
\]

All remaining factors are below one. Consequently,

\[
 \boxed{\text{every hard cyclic mask that improves leverage has }R_{\rm atom}>0.}
\tag{15c}
\]

At the ternary control this residual is the exact positive value (6). The hard
gain can therefore never by itself pay the complete-family atomic cardinality
of R-106131.

Literal atoms do cancel in a signed cyclic identity. Put

\[
 P=\sum_\omega z_\omega,\qquad
 D=\sum_\omega|z_\omega|^2,\qquad
 D_j=\sum_{\Phi(\omega)\in\zeta_k^jS}|z_\omega|^2,
\]

and define

\[
\begin{aligned}
 P^\circ&=|P|^2-D,\\
 O_j^\circ&=|O_j|^2-(k/t)^2D_j,\\
 H_r^\circ&=|H_r|^2-D.
\end{aligned}
\]

Fourier orthogonality across the \(k\) rotated masks and (14) give

\[
 \boxed{
 P^\circ={1\over k}\sum_{j=0}^{k-1}O_j^\circ
 -\sum_{r=1}^{k-1}|c_r|^2H_r^\circ.}
\tag{16}
\]

For \(k=3,S=\{1,\zeta_3\}\),
\(|c_1|^2=|c_2|^2=1/4\), so

\[
 \boxed{
 P^\circ={O_0^\circ+O_1^\circ+O_2^\circ\over3}
 -{H_1^\circ+H_2^\circ\over4}.}
\tag{17}
\]

The producer verifies (17) with exact rational coefficients on all 18 control
coordinates. Both \(H_1,H_2\) are the selected L-106120
double-nonprincipal channels. Their individual Gauss weight is

\[
 {2\ell\over\ell-1}{2\rho\over\rho-1}={91\over18}<9,
\]

The value \(91/36\) is the bounded external Gauss-weight diagnostic

\[
 \sum_{r=1}^2|c_r|^2
 {2\ell\over\ell-1}{2\rho\over\rho-1}={91\over36}.
\]

It is **not** the literal atomic coefficient in (17): the \(H_r^\circ\) there
are unweighted, so that coefficient is
\(|c_1|^2+|c_2|^2=1/2\). If (17) is rewritten in terms of externally weighted
L-106120 channels, its coefficients are divided by the same Gauss weight and
the literal value remains \(1/2\). The bounded diagnostic is
conductor-independent on the fixed fibre. The off-atomic global moments are
not proved.

Equation (16) is the honest algebraic next coordinate: a signed, globally
recombined estimate for all rotated conditioned currents and their selected
Kummer modes. Taking absolute values separately for each conductor fibre is
still forbidden by R-106123 and T-106140.

## 7. Exact boundary

Proved exactly here:

- every fixed exact-order-\(k\) quotient character has a \(2k\)-th-root
  physical orientation on one fixed owner sector;
- the orientation is invariant under all source presentations of \(Pc^2\);
- root choice disappears, while sector gauge rotates quotient labels and a
  primitive-character change applies a quotient automorphism;
- every nonconstant mask mode is an explicit live L-106120
  double-nonprincipal channel;
- the exact \(k=3,t=2,(7,13)\) hard gain, complete-frame soft loss, and
  positive Wick residual;
- the all-panel theorem that every leverage-improving cyclic mask leaves a
  strictly positive Wick atomic residual;
- the all-\(k\) centered identity (16) and exact ternary control (17).

Not proved:

- a canonical \(k>2\) mask independent of character and alignment choices;
- permission to delete source atoms in the full varying-owner/conductor FFPS
  assembly;
- a global estimate for the rotated conditioned currents or selected Kummer
  modes;
- WCADD106140, WCKUM106140, BCI102990, RH, or GRH;
- any external novelty claim.

The result is therefore a **source-realization theorem and analytic gate**, not
a closure of the RH-bearing moment.

## 8. Reproduction

The producer uses exact integers and `Fraction`. It inspects only \(180\)
owner/core presentations for the invariance controls, two small presentations
for the raw-collapse witness, and an 18-coordinate Gram. It performs no
prime, conductor, L-function, curve, or zero sweep. Source bytes, git objects,
residue atoms, matrix cells, exact operations, packet size, and wall time are
capped and fail closed.

~~~powershell
python research/l-families/atlas/function_field/ffps_cyclic_source_realization_gate.py --check
python -O research/l-families/atlas/function_field/ffps_cyclic_source_realization_gate.py --check
python -m pytest -q tests/test_ffps_cyclic_source_realization_gate.py
python -O -m pytest -q tests/test_ffps_cyclic_source_realization_gate.py
python -m ruff check research/l-families/atlas/function_field/ffps_cyclic_source_realization_gate.py tests/test_ffps_cyclic_source_realization_gate.py
~~~

Regenerate the canonical JSON only by omitting `--check` from the first
command.
