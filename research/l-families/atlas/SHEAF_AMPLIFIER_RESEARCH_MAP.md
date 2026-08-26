# PR #757 research map: sheaf amplifiers, native reflection, and two arithmetic moonshots

Status: **release-candidate exploratory mathematics; no proof of RH or GRH**

Branch: `codex/l-function-sheaf-amplifier`

Frozen parent: PR #756 at
`6e4609dfe1b073f1eb58445fdd1d7164dbc450d6`.

Programmes touched:
[#736](https://github.com/gfreund123/riemann/issues/736),
[#737](https://github.com/gfreund123/riemann/issues/737), and
[#741](https://github.com/gfreund123/riemann/issues/741)

## Start here

For a five-minute digest, read in this order:

1. [`SHEAF_AMPLIFIER_FIVE_MINUTE_HANDOFF.md`](SHEAF_AMPLIFIER_FIVE_MINUTE_HANDOFF.md);
2. this map, especially the result table below;
3. [`FFPS_MOLLIFIED_BETA_RH_EQUIVALENCE.md`](function_field/FFPS_MOLLIFIED_BETA_RH_EQUIVALENCE.md);
4. [`FFPS_MOLLIFIED_BETA_BOUNDARY_SHELL_IDENTITY.md`](function_field/FFPS_MOLLIFIED_BETA_BOUNDARY_SHELL_IDENTITY.md);
5. [`FFPS_BOUNDARY_FIELD_NEAR_CORRELATION_CRITERION.md`](function_field/FFPS_BOUNDARY_FIELD_NEAR_CORRELATION_CRITERION.md);
6. [`FFPS_MOLLIFIED_GEODESIC_RH_CRITERION.md`](function_field/FFPS_MOLLIFIED_GEODESIC_RH_CRITERION.md);
7. [`QUADRATIC_FAMILY_FIXED_DEPTH_TRACE_ZERO_DENSITY.md`](function_field/QUADRATIC_FAMILY_FIXED_DEPTH_TRACE_ZERO_DENSITY.md);
8. [`GENUS2_SYM12_MASTER_ADAPTER_CONTRADICTION_AUDIT.md`](function_field/GENUS2_SYM12_MASTER_ADAPTER_CONTRADICTION_AUDIT.md);
9. [`SHEAF_AMPLIFIER_RELEASE_AUDIT.md`](SHEAF_AMPLIFIER_RELEASE_AUDIT.md)
   before reusing any claim.

Items 3--5 are the shortest quadratic RH-facing path; item 6 is its native-
reflection continuation. Standalone arithmetic geometry begins at items
7--8. The hard-mask/sheaf path begins at
[`FFPS_MASK_AMPLIFIER_PARETO_FRONTIER.md`](function_field/FFPS_MASK_AMPLIFIER_PARETO_FRONTIER.md).

## Executive verdict

This pass did not prove RH. It did something more useful than accumulating
another family of attractive finite plots:

1. it found an exact, source-faithful fixed-mollified detector which is
   **equivalent to RH** and rewrote it as a native half-divisor reflection
   criterion;
2. it proved that the tempting unmollified Jordan premise is
   **unconditionally false** by an explicit `Omega(sqrt(Y))` atomic lower
   bound;
3. it converted the cyclic hard-mask idea into exact projector geometry,
   scalable source candidates, and quantitative conductor/no-go ledgers;
4. it proved exact residual/profile algebra and a fixed-`q,j` `M^-2/M^-3`
   odd-notch asymptotic at every fixed depth, then proved exponential local
   anti-concentration across that depth tower;
5. it found a separate full-rational-place supersingular law; and
6. it audited the genus-two `Sym^12` stack from raw arithmetic to ambient
   semisimplified cohomology: the exact `p=3,5,7` residual has one formal
   one-Tate repair in the displayed carrier ledger, while actual Galois
   realization and any all-`q` correction remain open.

The main conceptual change is that there are now two distinct RH-facing
architectures:

```text
hard physical restriction -> relative sheaf projector -> global trace bound
                         -> signed principal extraction -> RH consumer

complete beta source -> compact boundary field -> ratio-16 beta Gram form
                     -> subpower off-diagonal estimate <=> RH
```

The first is a family-amplification research programme. The second is already
an exact RH criterion, but its one-sided reflection estimate is still as hard
as RH. They should not be blended into one vague “family estimate.”

## Result table

| Lane | Strongest exact result | What remains open |
|---|---|---|
| native analytic detector | for every fixed `epsilon>0`, mollified beta negative mass is equivalent to RH | prove the estimate without assuming RH |
| boundary primitive | the mollified detector is an exact first difference of the boundary field `G` built from compact-BV `K_bd`; signed mass is one terminal shell, and one-sided mass of `G` is itself RH-equivalent | boundary telescoping cannot control Jordan mass; cross-odd-index cancellation remains open |
| boundary near-correlation | prefix `L2` energy is RH-equivalent and is exactly a positive Gram sum over beta pairs with ratio in `[1/16,16]`; the diagonal is explicitly logarithmic | prove the signed off-diagonal compact-ratio correlation is subpower |
| reflection/geodesic form | the same detector is exactly a differentiated native reflection-odd energy; the relative geodesic form differs only by an unconditional `O_epsilon(T)` squared field | obtain arithmetic control of the positive differentiated reflection energy |
| raw complete current | negative Jordan variation is at least `((70+50 sqrt(2))/pi^2)sqrt(Y)+O(log Y)` | none: the raw subpower premise is refuted |
| hard-mask co-design | sharp leverage/leakage Pareto law and bounded-energy anomaly-cancellation theorem | a global varying-place relative complex and signed trace estimate |
| cyclic/abelian geometry | honest torsor endomorphism identity `C-S=Pi_0`; subgroup masks compress many coordinates to fixed selected rank | realize the actual FFPS cleanup functorially with uniform conductor cost |
| scalable blocks | a native rich-core source has formal leverage `<(4/5)^r`; closed-place supply permits `r` growing with conductor degree | weighted Boolean transfer and joint relative cancellation |
| entropy/conductor | the `r`-th eligible place has degree `exp((1/delta+o(1))r)`; a modewise conductor loss wins only below `theta<delta log(5/4)` | cancel large-degree constituents before paying separate mode costs |
| exact cycle selector | the full `S_d` `d`-cycle indicator has forced absolute semisimple rank mass `2^(d-1)/d`, with equal signed halves; product costs multiply | joint `K_0` cancellation, a weaker source-specific selector, or different descended-orbit geometry |
| derangement-relaxed selector | **exact finite, `2<=d<=10`:** merely vanishing on fixed-point classes still has unique optimum `1_(d)` and mass `2^(d-1)/d` | the all-`d` statement is conjectural; source-specific and joint geometric cancellation remain open |
| odd-notch zeros | first boundary is nonzero for all `n>=4`; every fixed depth has exact residual/profile algebra and a fixed-`q,j` `M^-2/M^-3` asymptotic; local channel probabilities are `O_q(sqrt(j)q^-j)` | the stable range, `O_(q,j)(M^-4)` remainder, and complementary growing-depth layers are not uniform in `j` |
| full rational aperture | auxiliary curve `y^2=x-x^q` gives an exact even generating series and all odd family correlations vanish | relate this saturation law to more general marked-place selectors |
| genus-two `Sym^12` | arithmetic/stack adapter and semisimplified `G=0` survive; Shmakov's displayed branch misses raw rows by exactly `-p` at `p=3,5,7`, with a unique formal repair inside the displayed carrier ledger | realize or refute that carrier in actual compact-support Galois cohomology; three rows prove no all-`q` correction |
| finite numerical control | through `Y=2^18`, both the mollified current and compact boundary field show near-logarithmic variation while the raw atomic comparator grows like `sqrt(Y)`; the first-difference cross-check is `2.13e-13` absolute | no asymptotic is inferred; test structural decompositions, not larger brute-force ranges |

## 1. The canonical RH-facing route

### 1.1 Raw Jordan variation is the wrong target

For the complete duplicate-`67` source

\[
 \beta(n)=\mu(n)-1_{67\mid n}\mu(n/67),
\]

let

\[
 \nu_{\rm ext}
 =\sum_{n\ge1}{\beta(n)\over\sqrt n}\,\tau_nK_{\rm ext}.
\]

The extra-notched kernel has dyadic atomic coefficients

\[
 (5,-10-10\sqrt2,15+20\sqrt2,-20-10\sqrt2,10).
\]

After every possible `2`-adic collision is grouped, the six coefficients have
positive and negative mass exactly `50+35 sqrt(2)` each. Unique `2`-adic
factorization prevents cross-group cancellation, so

\[
 \nu_{\rm ext}^-([1,Y])
 \ge (50+35\sqrt2)
 \sum_{\substack{m\le Y/32\\m\ \mathrm{odd}}}
 {\lvert\beta(m)\rvert\over\sqrt m}
 \gg\sqrt Y.
\]

Read [`FFPS_COMPLETE_BETA_ATOMIC_VARIATION_FIREWALL.md`](function_field/FFPS_COMPLETE_BETA_ATOMIC_VARIATION_FIREWALL.md). The old implication
“raw subpower Jordan variation implies RH” remains logically valid, but its
premise is false and must not be advertised as an open strategy.

### 1.2 Fixed mollification is exactly RH-equivalent

Fix one `epsilon>0`, let `eta_epsilon` be the positive causal log box, and
put

\[
 h_\varepsilon=\eta_\varepsilon*\nu_{\rm ext}.
\]

Then

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \int_0^T\lvert h_\varepsilon(t)\rvert\,dt=e^{o(T)}
 \Longleftrightarrow
 \int_0^T(h_\varepsilon(t))_-\,dt=e^{o(T)}.}
\]

The forward implication uses the classical RH Mertens bound, normalized beta
summation, and one compact-BV summation step. The reverse implication is the
zero-safe Mellin--Landau argument: every off-line zeta zero creates an
uncancelled pole in `Re(s)>0`, while one-sided subpower mass makes the
positive and negative Laplace transforms holomorphic there.

This is a calibration theorem, not a proof. It tells future work exactly how
strong the remaining arithmetic estimate is: proving it proves RH.

### 1.3 The compact boundary primitive removes the box parameter

Because `K_ext` has total mass zero, it has a compact-BV causal primitive
`K_bd`. Define

\[
 G(t)=\sum_{n\ge1}{\beta(n)\over\sqrt n}K_{\rm bd}(t-\log n).
\]

Then, for every fixed `epsilon>0`,

\[
 \boxed{h_\varepsilon={G-\tau_\varepsilon G\over\varepsilon}.}
\]

Its signed mass is exactly one terminal shell, and

\[
 \int_0^T\lvert h_\varepsilon\rvert
 =2\int_0^T(h_\varepsilon)_-
 +{1\over\varepsilon}\int_{T-\varepsilon}^TG.
\]

This explains the scout's nearly `2:1` absolute/negative masses exactly; it
does not explain their apparent logarithmic growth. More importantly,

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \int_0^T\lvert G(t)\rvert\,dt=e^{o(T)}
 \Longleftrightarrow
 \int_0^T(G(t))_-\,dt=e^{o(T)}.}
\]

Thus one integration removes both the box parameter and the raw atoms without
losing zero detection. Exact dyadic compression leaves a compact odd-fibre
kernel with polynomial

\[
 (1-z)^2(1-\sqrt2z)^2(1-z/\sqrt2).
\]

Its constant coefficient is one, so finite telescoping does not annihilate an
independent odd fibre. An explicit compact countermodel proves signed
boundary telescoping alone cannot bound either Jordan side.

### 1.4 The primitive isolates one compact-ratio beta correlation

For the finite prefix

\[
 G_X(t)=\sum_{n\le X}{\beta(n)\over\sqrt n}
 K_{\rm bd}(t-\log n),
\]

let `R` be the autocorrelation of `K_bd`. Exact finite Fubini gives

\[
 \mathcal E(X)=\int_{\mathbf R}|G_X|^2
 =\sum_{m,n\le X}{\beta(m)\beta(n)\over\sqrt{mn}}
 \mathcal R\!\left(\log{m\over n}\right).
\]

Because `K_bd` is supported in `[0,4log2]`, only ratios
`1/16<=m/n<=16` occur. Causality and Cauchy--Schwarz, together with the
locked boundary-field theorem, prove

\[
 \boxed{\mathrm{RH}\Longleftrightarrow\mathcal E(X)=X^{o(1)}.}
\]

The diagonal contribution is explicit:

\[
 \mathcal D(X)=\mathcal R(0)\sum_{n\le X}{\beta(n)^2\over n}
 ={2379\,\mathcal R(0)\over2278\zeta(2)}\log X+O(1).
\]

Therefore RH is equivalent to the **absolute value** of one signed off-
diagonal compact-ratio beta correlation being `X^o(1)`. This is the requested
quadratic/prime-shell localization. It remains RH-strength, but it interfaces
directly with the relative-projector and bilinear family lanes.

### 1.5 Native half-divisor reflection removes the Boolean adapter

The frozen half-divisor source `lambda` satisfies `lambda*lambda=beta`. Let
`F_1` be its positive spline field and `I_1=F_1*_M F_1`. With

\[
 \mathcal D_{\rm out}=5D^4-6D^3+\tfrac14D^2+\tfrac34D,
\]

the complete mollified density is exactly

\[
 h_\varepsilon=\eta_\varepsilon*\mathcal D_{\rm out}I_1.
\]

After a causal finite-horizon `L^2` fence, define the reflection-odd energy

\[
 \mathcal O_{1,R}(x)
 =\left\|{f_{1,R}-f_{1,R}(x-\cdot)\over2}\right\|_2^2.
\]

For every `R>T`, on `[0,T]`,

\[
 \boxed{
 h_\varepsilon(t)
 =-2\eta_\varepsilon*\mathcal D_{\rm out}\mathcal O_{1,R}(t).}
\]

Hence RH is equivalent to subpower **positive** mass of the differentiated
reflection-odd energy. The continuous half-divisor geodesic gives a relative
native-minus-squared reflection form; its squared endpoint has only
`O_epsilon(T)` absolute mass, so the two criteria are equivalent.

This route is source-exact and bypasses the open Boolean completion statement
`NATCOMP-MOLL106150`. Its smallest burden is now sharply stated, but not
solved.

### 1.6 Lightweight scout

The bounded scout uses at most `2^18` beta coefficients and two log meshes.
For `epsilon=(log 2)/2`, the fine panel reports:

| `Y` | mollified negative mass | absolute mass | raw atomic lower bound |
|---:|---:|---:|---:|
| `2^10` | `209.085` | `422.792` | `448.094` |
| `2^14` | `287.634` | `580.765` | `1858.573` |
| `2^18` | `367.255` | `733.561` | `7408.856` |

The finite-window slopes are about `19.32` and `38.38` per doubling. This
suggests logarithmic-scale cancellation and motivates an exact boundary-shell
analysis. It is floating-point finite data, not asymptotic evidence for RH.

The independently audited compact-field scout evaluates `G` itself on the
same three horizons:

| `Y` | boundary-field negative mass | absolute mass | signed mass |
|---:|---:|---:|---:|
| `2^10` | `60.661` | `122.349` | `1.028` |
| `2^14` | `80.520` | `161.465` | `0.425` |
| `2^18` | `102.449` | `203.051` | `-1.848` |

Its finite-window slopes are about `5.14` and `10.16` per doubling. Direct
first differencing recovers the mollified density with maximum absolute error
`2.13e-13` and relative error `1.05e-15`. This validates the implementation
of the exact boundary identity; it still supplies no asymptotic estimate.

## 2. Hard masks, relative projectors, and conductor cost

### 2.1 Exact Pareto frontier

For retained quotient density `rho=t/k`, put `u=k/t-1`. If `A=Q/N` and
`B=P/N`, then the sharp restricted leverage and total selected Fourier mass
are

\[
 L(u)={(1+u)^2\over A+Bu},
 \qquad
 \sum_{r=1}^{k-1}\lvert\gamma_r\rvert^2=u.
\]

Uniform hard weights uniquely minimize both quantities. Signed or complex
dual weights on the same support cannot secretly improve the tradeoff. A
principal amplitude can be cancelled by selected modes with minimum energy
`|P_0|^2/u`, which stays bounded at the large-panel optimum. Thus formal
leverage is not individualization.

### 2.2 Fixed-fibre sheafification and its resonance

The ternary mask becomes two faithful cubic Kummer lines on the oriented
physical squareclasses. On a geometrically integral stratum `Z`, an invariant
appears exactly when

\[
 R_XR_Y^\varepsilon\in K(Z)^{\times3}.
\]

The generic physical torus passes, but compensating resonances and double
physical collisions do not. Wick removal deletes the literal diagonal, not
every resonant stratum. This is the exact reason a fixed-fibre Deligne slogan
is not yet `CYSEL`.

### 2.3 Relative projector is honest geometry

On every genuine cyclic torsor, the hard and selected operators satisfy

\[
 \boxed{\mathsf C_S-\mathsf S_S=\Pi_0}
\]

as honest endomorphisms of the regular local system. Any common equivariant
cleanup functor preserves the identity. The theorem extends to every finite
abelian mask. If the retained set is a subgroup coset of index `h`, selected
Fourier support has only `h-1` lines. In particular, the global parity
checkerboard on `C_2^d` has exactly one selected line despite exponentially
many coordinates.

This is the best geometric mechanism in the mask lane. The missing theorem is
not local Fourier algebra; it is construction of one global varying-place
physical torsor/correspondence on which every source cleanup is common and
whose pushed-forward complexity is uniform enough.

### 2.4 Scalable source and the entropy/conductor threshold

Inside one native clean source atom, selecting the first `r` eligible prime
divisors on each side gives `2r` phases before one common square. Every
nontrivial `C_2^r` mode remains bilateral, and

\[
 L_r<(4/5)^r.
\]

There is a one-characteristic closed-place analogue. If eligible places have
degree-density

\[
 \delta=1\quad(q=1\bmod4),
 \qquad
 \delta=1/2\quad(q=3\bmod4),
\]

the `r`-th smallest eligible factor has typical degree

\[
 d_{(r)}=\exp((1/\delta+o(1))r).
\]

A separate trace theorem losing `d_(r)^theta` can beat the leverage only if

\[
 \boxed{\theta<\delta\log(5/4).}
\]

Square-root conductor loss therefore fails badly. The plausible escape is a
joint relative complex in which high-degree constituents cancel before a
modewise conductor bill is paid.

### 2.5 Exact irreducibility selectors cannot be rank-optimized away

The universal root-incidence packet used the exact `d`-cycle selector

\[
 q_d={1\over d}\Lambda_{-1}(\mathrm{Std}_d).
\]

Character orthogonality and Murnaghan--Nakayama give its unique irreducible
expansion

\[
 q_d={1\over d}\sum_{k=0}^{d-1}(-1)^k
 \chi_{(d-k,1^k)}.
\]

Therefore every exact characteristic-zero semisimple `S_d` presentation has
forced absolute rank mass

\[
 {2^{d-1}\over d},
\]

with positive and negative masses `2^(d-2)/d` each for `d>1`. Independent
place selectors multiply these costs. Since the selected place degree itself
grows exponentially in block rank, expanding this selector and bounding its
constituents separately is far worse than the power-conductor ledger.

This closes the search for a cheaper **exact full-`S_d` character
presentation**. It does not rule out assembling the zero class before paying
rank, selecting only the factorization information seen by the native source,
using an approximate filter, or changing from universal roots to descended
closed-orbit atoms.

### 2.6 The derangement relaxation is no cheaper through degree ten

A strictly weaker optimization asks only that `Q((d))=1` and that `Q` vanish
on conjugacy classes with a fixed point; its values on all other derangement
classes are free. Equivalently,

\[
 \operatorname{Res}^{S_d}_{S_{d-1}}Q=0.
\]

Exact rational primal-dual certificates prove that for every `2<=d<=10`

\[
 \min\sum_{\lambda\vdash d}f^\lambda|a_\lambda|
 ={2^{d-1}\over d},
\]

uniquely at the exact cycle indicator. This is an **exact finite theorem**,
not an all-degree result. The same statement for every `d` is a conjecture;
the simplest hook-predecessor-only dual ansatz already fails at `d=8`, even
though an interior Young-lattice certificate exists there. Read
[`FFPS_DERANGEMENT_SELECTOR_FINITE_L1_OPTIMIZATION.md`](function_field/FFPS_DERANGEMENT_SELECTOR_FINITE_L1_OPTIMIZATION.md).

### 2.7 Firewalls that must be retained

- Ambient density of rich cores does not transfer automatically through the
  cutoff-dependent Boolean/owner source.
- The half-source free diagonal has a genuine power saving, but near-collision
  and reflection correlations remain.
- The normalized selected-energy rank is quadratic in block rank, not linear.
- Positive semidefinite atom-free replacements cannot reproduce the required
  signed cancellation.
- Complete-frame soft weighting does not emulate hard physical deletion.
- The signed identities `P=A-K=C-S` already give scalar principal extraction
  once both members of one pair are controlled; positive averages still need
  a separate domination or rigidity theorem.

## 3. Closed-place notch mathematics

These are zeros of a **family correlation sum**, never zeros of an individual
L-function.

### 3.1 First boundary extinction

At the odd notch `M=2n-1`, put `h=floor(n/2)`. The support-forced stratum has
minimum factor degree greater than `h`. On the first boundary, with `m_h`
degree-`h` factors,

\[
 S_{n,Q}=m_hD_{n-2h}.
\]

For even `n` this is positive. For odd `n>=5`, `D_1` is a sum of an odd
number of nonzero signs and cannot vanish. Hence every first-boundary zero
disappears for `n>=4`; `n=3` is the unique exceptional family degree.

### 3.2 Second boundary through third order

For odd `n=2h+1`, `M=4h+1`, the first accidental layer outside the support
and first-boundary regions reduces to one exterior-cubic condition. Its local
probability is the exact finite Rademacher law

\[
 \delta_q=\Pr\left(
 S_3+S_1S_2+{S_1^3+(2-3q)S_1\over6}=0\right).
\]

The full second-boundary density is

\[
 {Z^{(2)}_{q,h}\over q^M-q^{M-1}}
 ={\delta_q\over1-q^{-1}}
 \left\{
 {16(1+\log2)\over3M^2}
 +{32(11+5\log2)\over9M^3}
 +O_q(M^{-4})
 \right\}.
\]

This closes the “additional trace-zero layer” question at its first
nontrivial boundary: it is `M^-2`, so it does **not** add another `c/M` term
to the support-forced leading density.

### 3.3 Third boundary and the first mixed channel

For the next layer, `n=2h+1`, `M=4h+1`, and minimum factor degree `h-2`, the
raw detector collapses exactly to

\[
 S_{n,Q}=m_{h-2}D_5+m_{h-1}D_3+m_hD_1.
\]

Parity forces `m_h` even; the only positive such profile contributes
`D_5+2D_1` only at `M^-4`. Put

\[
 \delta_{5,q}=\Pr(D_5=0),\qquad
 \delta_{53,q}=\Pr(D_5+D_3=0).
\]

Both are positive for every odd prime power, and

\[
 {Z^{(3)}_{q,h}\over q^M}
 ={\delta_{5,q}(1+\log2)\over3h^2}
 +{\delta_{5,q}(5+2\log2)/6+\delta_{53,q}/2\over h^3}
 +O_q(h^{-4}).
\]

Thus a second fixed-depth layer also begins at `M^-2`; its first genuinely
mixed Frobenius channel appears at `M^-3`. The repetition points toward a
fixed-depth tower rather than isolated exceptional formulas.

### 3.4 All fixed depths

The residual/profile algebra is exact, and the density asymptotic uses the
standard fixed-modulus prime-polynomial progression theorem. For fixed
`j>=1`, `h>=5j+2`, and minimum factor degree `h-j`, put

\[
 \delta_{j,s,q}=\Pr(D_{2j+1}+D_{2j+1-2s}=0),
 \qquad
 \delta_{j,0,q}=\Pr(D_{2j+1}=0).
\]

The residual and parity laws are

\[
 S_{n,Q}=\sum_{s=0}^{j}m_{h-j+s}D_{2j+1-2s},
 \qquad \delta_{j,j,q}=0,
\]

and the complete fixed-depth density through third order is

\[
\begin{aligned}
 {Z^{(j)}_{q,h}\over q^M}
={}&{\delta_{j,0,q}(1+\log2)\over3h^2}\\
&+{1\over h^3}\left\{
 {\delta_{j,0,q}((2j-1)(7+4\log2)+9)\over36}
 +{1\over2}\sum_{s=1}^{j}\delta_{j,s,q}
 \right\}
 +O_{q,j}(h^{-4}).
\end{aligned}
\]

The `j=1,2` specializations recover both predecessor packets exactly. Every
fixed depth is only `O(M^-2)`. Therefore a new `c/M` population, if one
exists, must use a depth range growing with `M`.

### 3.5 Local anti-concentration makes the coefficient tower summable

Let `r=2j+1` and `N=I_q(r)`. The top-degree Rademacher sum occurs with
coefficient one in every local channel. Conditioning on all lower-degree
signs and applying the exact maximal-atom bound gives, uniformly in
`0<=s<=j`,

\[
 \delta_{j,s,q}\le N^{-1/2}
 \le {3\over\sqrt{2q}}\sqrt j\,q^{-j},
 \qquad \delta_{j,j,q}=0.
\]

Consequently

\[
 \sum_{s=0}^{j}\delta_{j,s,q}
 =O_q(j^{3/2}q^{-j}),
\]

and the displayed fixed-depth `M^-2` and `M^-3` coefficient towers are
absolutely summable. This is genuine progress on the aggregate question, but
it does **not** permit summing the conductor layers: `h>=5j+2`, the
`O_(q,j)(h^-4)` remainder, and complementary growing-depth profiles still
lack uniform control. Read
[`QUADRATIC_FAMILY_LOCAL_DELTA_TOWER_ANTICONCENTRATION.md`](function_field/QUADRATIC_FAMILY_LOCAL_DELTA_TOWER_ANTICONCENTRATION.md).

### 3.6 Depth and full-aperture laws

Every exact minimum-degree layer satisfies

\[
 B_q(M,d)\le {q^M\over d^2}.
\]

Thus a new `q^M/M` population cannot hide in only `o(M)` proportional-depth
layers. Separately, marking every rational place produces the auxiliary
supersingular curve

\[
 y^2=x-x^q,
 \qquad P_q(u)=(1+s_qqu^2)^{(q-1)/2},
\]

so the complete generating series is even and every odd-degree full-place
correlation vanishes. This is geometric saturation, not the exterior-notch
alias alone.

## 4. Genus-two `Sym^12`

The master audit checked the full arithmetic/stack chain:

- groupoid denominator `q(q-1)`;
- `r_D(12)=q^6 chi_(12,0)(U_D)`;
- reciprocal preclosure, repeated cubic, quartic, and `Q_1=3q-9` rows;
- ordered `Y_0(2) x A_1` decomposable boundary;
- ambient trace identity; and
- exact semisimplified stable/general vanishing `G=0`.

All survive. Directly from raw stored `T_(12,0)` rows and the locked
inventory, the residual against Shmakov's displayed `2-4L` branch is exactly

\[
 -3,-5,-7
\]

at `p=3,5,7`. Within the displayed carrier ledger, the unique formal repair
is an additional

\[
 [5,1]\otimes\mathbb L
\]

in the weight-16 Fricke-positive degree-three block, changing `2-4L` to
`2-5L`.

The first unproved arrow is precisely:

\[
 \text{displayed associated-graded Tate ledger}
 \longrightarrow
 \text{actual compact-support Galois Euler class}.
\]

Three trace rows force the one-Tate correction at those primes; they do not
prove an all-`q` motivic identity. This is the next specialist target.

## 5. What to pursue next

### Highest direct-RH bet

Attack the compact-ratio beta correlation or native reflection criterion, not
the refuted raw measure. The exact quadratic target is now

\[
 \sum_{\substack{m,n\le X\\m\ne n\\1/16\le m/n\le16}}
 {\beta(m)\beta(n)\over\sqrt{mn}}
 \mathcal R\!\left(\log{m\over n}\right).
\]

Its subpower bound is exactly RH-equivalent. The useful next move is a
prime-incidence or `beta=lambda*lambda` decomposition which preserves the
assembled signed Gram form and interfaces with relative projectors.

### Highest family/sheaf bet

Construct the varying-closed-place **relative** complex implementing
`C-S=Pi_0` before separate absolute values are taken. Track the actual
Boolean/owner source and cleanup functors, then determine whether the large
place-degree constituents cancel in the cone. This directly targets the
entropy/conductor obstruction rather than adding more fixed-fibre examples.

### Highest standalone arithmetic-geometry bet

Resolve the `Sym^12` realization arrow by comparing the nonregular
Eisenstein Galois filtration, not by fitting more unrelated primes. A
same-characteristic tower or direct boundary cohomology computation would be
more informative than a fourth small prime.

### Ambitious discovery lanes

1. Build a renormalization flow for the native reflection current in a small
   basis of boundary-shell correlations, retaining early-prime memory.
2. Prove growing-depth uniformity for the notch profile expansion and its
   remainder; local channel anti-concentration already makes the displayed
   fixed-depth coefficient tower absolutely summable.
3. Use quotient-subgroup masks beyond parity to keep selected rank fixed
   while varying conductor geometry; classify when relative projectors
   descend over nonsplit base fields.
4. Automate cohomological conjecture generation only after the exact adapter,
   representation channel, and Galois normalization are locked.

## 6. Proof and computation contract

- Exact, exact-finite, imported, formal, conditional, and conjectural claims
  remain separate.
- No finite trend is promoted to an asymptotic statement.
- A fixed-fibre trace-sheaf bound is not called conductor-uniform `CYSEL`.
- A hard-mask leverage gain is not called principal individualization.
- A formal Tate constituent is not called an actual Galois cohomology class.
- A detector zero is not an individual L-function zero.
- No local factor identity is promoted to a motive or global Euler product.
- The pass uses exact algebra and bounded replays; the two coupled
  floating-point scouts stop at `2^18` and enumerate no zero, curve, or
  conductor family.

Every proof-bearing packet has a canonical JSON artifact, bounded replay,
normal and optimized tests, and explicit source locks. The release audit
records the final replay set and any residual provenance caveats.
