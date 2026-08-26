# PR #757 research map: sheaf amplifiers, native reflection, and arithmetic moonshots

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
6. [`FFPS_BOUNDARY_FIELD_PRIMITIVE_RAY_LOCALIZATION.md`](function_field/FFPS_BOUNDARY_FIELD_PRIMITIVE_RAY_LOCALIZATION.md);
7. [`FFPS_BOUNDARY_FIELD_PRIMITIVE_PAIR_LARGE_SIEVE_GATE.md`](function_field/FFPS_BOUNDARY_FIELD_PRIMITIVE_PAIR_LARGE_SIEVE_GATE.md);
8. [`FFPS_MOLLIFIED_GEODESIC_RH_CRITERION.md`](function_field/FFPS_MOLLIFIED_GEODESIC_RH_CRITERION.md);
9. [`QUADRATIC_FAMILY_LOGARITHMIC_DEPTH_ZERO_FIREWALL.md`](function_field/QUADRATIC_FAMILY_LOGARITHMIC_DEPTH_ZERO_FIREWALL.md);
10. [`QUADRATIC_FAMILY_PROFILE_CHI_SQUARE_BRIDGE.md`](function_field/QUADRATIC_FAMILY_PROFILE_CHI_SQUARE_BRIDGE.md);
11. [`QUADRATIC_FAMILY_SQUARECLASS_ENTROPY_COMPRESSION.md`](function_field/QUADRATIC_FAMILY_SQUARECLASS_ENTROPY_COMPRESSION.md);
12. [`FFPS_DERANGEMENT_SELECTOR_TANH_CALIBRATION.md`](function_field/FFPS_DERANGEMENT_SELECTOR_TANH_CALIBRATION.md);
13. [`FFPS_SELECTOR_YOUNG_LATTICE_PROPAGATION_OBSTRUCTION.md`](function_field/FFPS_SELECTOR_YOUNG_LATTICE_PROPAGATION_OBSTRUCTION.md);
14. [`FFPS_TERNARY_UNIVERSAL_NORM_TORSOR.md`](function_field/FFPS_TERNARY_UNIVERSAL_NORM_TORSOR.md);
15. [`GENUS2_SYM12_MASTER_ADAPTER_CONTRADICTION_AUDIT.md`](function_field/GENUS2_SYM12_MASTER_ADAPTER_CONTRADICTION_AUDIT.md);
16. [`SHEAF_AMPLIFIER_RELEASE_AUDIT.md`](SHEAF_AMPLIFIER_RELEASE_AUDIT.md)
   before reusing any claim.

Items 3--7 are the shortest quadratic RH-facing path; item 8 is its native-
reflection continuation. Standalone arithmetic geometry begins at items
9--13. The hard-mask/sheaf path begins at
[`FFPS_MASK_AMPLIFIER_PARETO_FRONTIER.md`](function_field/FFPS_MASK_AMPLIFIER_PARETO_FRONTIER.md).

## Executive verdict

This pass did not prove RH. It did something more useful than accumulating
another family of attractive finite plots:

1. it found an exact, source-faithful fixed-mollified detector which is
   **equivalent to RH** and rewrote it as a native half-divisor reflection
   criterion, then localized its quadratic obstruction beyond every
   prescribed subpower primitive-height cutoff;
2. it proved that the tempting unmollified Jordan premise is
   **unconditionally false** by an explicit `Omega(sqrt(Y))` atomic lower
   bound;
3. it converted the cyclic hard-mask idea into exact projector geometry,
   scalable source candidates, and quantitative conductor/no-go ledgers;
4. it proved exact residual/profile algebra and a fixed-`q,j` `M^-2/M^-3`
   odd-notch asymptotic at every fixed depth, exponential local
   anti-concentration, and an `O(M^-2)` whole-layer theorem through a
   genuinely growing logarithmic depth window, then crossed the generic
   residue-entropy wall by an additive `log log M` squareclass window;
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
                     -> high primitive rays -> three-panel PRIMLS target
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
| primitive-ray localization | every fixed admissible beta ray has an explicit `A_(a,b) log X+O(1)` law; all reduced rays of height at most `H` cost `O(H log(2X))`, so for every prescribed `H=X^o(1)` RH is equivalent to the balanced residual above height `H` | cancel the high-height sector; both primitive coordinates exceed `H/16` and the common factor is `<X/H` |
| primitive-pair large-sieve gate | the full residual has an exact five-oriented/three-reciprocal decomposition, a signed one-dimensional Möbius--Gram form, and a biased-Boolean divisor-sieve diagonalization | prove `PRIMLS`, a maximal `L2(d^-1)` square-root-scale bound; the harmonic zero mode and frozen sieve rows show that `d`-averaging alone cannot do it |
| reflection/geodesic form | the same detector is exactly a differentiated native reflection-odd energy; the relative geodesic form differs only by an unconditional `O_epsilon(T)` squared field | obtain arithmetic control of the positive differentiated reflection energy |
| raw complete current | negative Jordan variation is at least `((70+50 sqrt(2))/pi^2)sqrt(Y)+O(log Y)` | none: the raw subpower premise is refuted |
| hard-mask co-design | sharp leverage/leakage Pareto law and bounded-energy anomaly-cancellation theorem | a global varying-place relative complex and signed trace estimate |
| cyclic/abelian geometry | honest torsor endomorphism identity `C-S=Pi_0`; subgroup masks compress many coordinates to fixed selected rank | realize the actual FFPS cleanup functorially with uniform conductor cost |
| universal ternary norm torsor | on every degree pair `(a,b)` over `q=1 mod 6`, the clean physical mask has ranks `48/32/16`, generic selected invariant zero, tame Swan zero, and toric conductor at most `288(a+b)`; root and physical monodromy split | tensor the native owner/Boolean/phase source before norming the exact selector, or use a source-specific/prime-polynomial selector; this packet alone is not `CYSEL` |
| scalable blocks | a native rich-core source has formal leverage `<(4/5)^r`; closed-place supply permits `r` growing with conductor degree | weighted Boolean transfer and joint relative cancellation |
| entropy/conductor | the `r`-th eligible place has degree `exp((1/delta+o(1))r)`; a modewise conductor loss wins only below `theta<delta log(5/4)` | cancel large-degree constituents before paying separate mode costs |
| exact cycle selector | the full `S_d` `d`-cycle indicator has forced absolute semisimple rank mass `2^(d-1)/d`, with equal signed halves; product costs multiply | joint `K_0` cancellation, a weaker source-specific selector, or different descended-orbit geometry |
| derangement-relaxed selector | **exact finite, `2<=d<=10`:** merely vanishing on fixed-point classes still has unique optimum `1_(d)` and mass `2^(d-1)/d` | the all-`d` statement is conjectural; source-specific and joint geometric cancellation remain open |
| selector `tanh` calibration | the natural bounded dual has the exact all-degree `tanh` series; every nonhook has the sharp gap `|b_lambda|/f^lambda<=(d-4)/d`; descent-set-only saturated repairs are rigid; an unrestricted zero-hook lift exists, and even-cycle-only perturbations are globally excluded | solve or refute contractivity on the remaining odd-cycle strata; this does not prove the all-`d` optimum |
| Young-lattice propagation | every real or complex contractive optimal lift must satisfy `Re((-1)^(j-1)X_j)>=2^d/d-C(d,j)` and therefore engage two-row potentials through `d/2-(1/2+o(1))sqrt(d log d)` | this is necessary only; construct a global box-feasible lift or prove that deeper cover constraints make one impossible |
| odd-notch zeros | first boundary is nonzero for all `n>=4`; every fixed depth has an exact `M^-2/M^-3` law; local probabilities are `O_q(sqrt(j)q^-j)`; for fixed `epsilon>0` and sufficiently large `h`, the complete window `j<=(1/2-epsilon)log_q h` is `O_q(M^-2)` | cross the natural CRT-modulus barrier `q^(2j)~h` using a bilinear large sieve, growing monodromy, or another genuinely uniform input |
| profile chi-square bridge | exact profile-weighted Parseval gives `Z<=T(beta+sqrt(beta)D)` and function-field RH bounds `D^2` by an explicit polynomial times `q^(ell_r-M)`; its explicit sufficient condition permits a logarithmic gap to the entropy wall when the discrete `ell_r` satisfies it | `ell_r<=M/2` is the unconditional realized corollary; no near-wall landing is claimed for every `M`, and the logarithmic depth scale remains |
| squareclass entropy compression | the detector factors through exactly `K_r` quadratic signs, replacing `q^ell_r` Fourier modes by `2^K_r`; the complete safe window reaches `r=log_q M+log_q log M+O_q(1)` with total `O_q(M^-2)` | `KRAWLS` must cancel inside degree-wise Krawtchouk orbits to approach the conditional `r=Theta(sqrt M)` scale |
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

The ray packet sharpens where that strength lives.  After writing every
nonzero pair uniquely on a reduced beta ray `a/b`, including all exceptional
`67` valuations, one ray has an explicit harmonic formula and

\[
 \mathcal Q_{a,b}(X)=A_{a,b}\log X+O_{a,b}(1).
\]

Moreover, the aggregate of all reduced rays with height at most `H` is
`O(H log(2X))` absolutely.  Hence for every prescribed `H(X)=X^o(1)`, RH is
equivalent to the residual above height `H(X)`.  Compact ratio support then
forces both reduced coordinates above `H/16` and the common factor below
`X/H`.  Thus no finite, polylogarithmic, or other prescribed subpower family
of rational resonances is the obstruction.  Read
[`FFPS_BOUNDARY_FIELD_PRIMITIVE_RAY_LOCALIZATION.md`](function_field/FFPS_BOUNDARY_FIELD_PRIMITIVE_RAY_LOCALIZATION.md).

### 1.5 The residual is a five-channel Möbius large-sieve problem

Dyadically shell the remaining primitive height and expose the common
squarefree factor.  An exact finite interchange turns every shell into five
oriented exceptional-`67` panels—three after reciprocity—of the form

\[
 \sum_{d\le D}{1\over d}\,
 \mathcal P_{\alpha,\gamma}(d;H,U_d),
\]

where `P` is a square-root-normalized two-dimensional Möbius correlation over
coprime primitive pairs, with `(ab,d)=1` and the moving prefix endpoint
`U_d` retained exactly.  A maximal square mean

\[
 \sum_{d\le D}{1\over d}
 \sup_{H\le U\le2H}|\mathcal P_{\alpha,\gamma}(d;H,U)|^2
 \ll_\varepsilon (2DH)^\varepsilon
\]

for the three reciprocal panels implies RH by weighted Cauchy and summation
over `O(log X)` shells.  This `PRIMLS` statement is open and intentionally
stronger than RH; unlike the assembled Gram criterion, it is a recognizable
averaged Chowla/large-sieve target at the random-sign scale.  Read
[`FFPS_BOUNDARY_FIELD_PRIMITIVE_PAIR_LARGE_SIEVE_GATE.md`](function_field/FFPS_BOUNDARY_FIELD_PRIMITIVE_PAIR_LARGE_SIEVE_GATE.md).

Two exact normal forms prevent a misleading next move.  Rectangle
differencing and coprimality Möbius inversion express each panel as a signed
`k^-1` sum of one-dimensional boundary-field Gram inner products.  On every
finite squarefree divisor cube, the `d^-1`-weighted family has an exact
biased-Boolean Parseval transform.  Its zero frequency is the harmonic panel
mean, and primes larger than the shell produce identical sieve rows.  Thus
abstract orthogonality in the common-factor label cannot prove `PRIMLS`; the
mean and the nonzero Boolean modes both require Möbius-pair cancellation.

### 1.6 Native half-divisor reflection removes the Boolean adapter

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

### 1.7 Lightweight scout

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

### 2.5 The minimal varying-degree physical torsor is now explicit

Assume `q=1 mod 6` and fix place degrees `(a,b)`. Universal etale root
algebras and their norms canonically lift one order-six base-field character
to every irreducible residue field. Four scalar norm-orientation covers and
one cubic torsor then realize the clean ternary physical mask over the full
degree shells. The physical ranks are

\[
 48\quad\text{(regular)},\qquad
 32\quad\text{(selected)},\qquad
 16\quad\text{(relative)}.
\]

The generic selected invariant is zero by a boundary valuation; resonance is
exactly the condition that the orientation monomial be a cube. All toric
ramification is tame, the support has `6(a+b)` divisors after splitting, and
the rank-times-support conductor bound is `288(a+b)`. Moreover the generic
finite quotient is the direct product

\[
 (S_a\times S_b)\times(C_2^4\times C_3).
\]

Thus the physical norm/Kummer factor is bounded-rank and linear-cost, while a
termwise exact irreducibility tensor still incurs
`2^(a+b-2)/(ab)` before the physical dimension. The direct-product theorem
rules out cancellation internal to this positive physical representation. It
does **not** rule out cancellation after the native virtual
owner/Boolean/incidence tensor, a weaker source-specific selector, or a
prime-polynomial trace formula. Read
[`FFPS_TERNARY_UNIVERSAL_NORM_TORSOR.md`](function_field/FFPS_TERNARY_UNIVERSAL_NORM_TORSOR.md).

### 2.6 Exact irreducibility selectors cannot be rank-optimized away

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

### 2.7 The derangement relaxation is no cheaper through degree ten

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

### 2.8 The natural all-degree dual is exactly a hyperbolic tangent

The finite dual certificates have an exact structural calibration.  If

\[
 b_{d,\lambda}=\sum_{T\in\operatorname{SYT}(\lambda)}(-1)^{\operatorname{des}(T)},
 \qquad
 \mathcal A(t)=\sum_{r\ge1}{2^{r-1}\over r}p_rt^r,
\]

then, in every degree,

\[
 \sum_{d\ge1,\lambda\vdash d}b_{d,\lambda}s_\lambda t^d
 =\tanh \mathcal A(t).
\]

This bounded Schur spectrum saturates every hook with the signs required by
the exact-cycle primal candidate.  On a cycle type with `ell` parts its
class transform is exactly
`[x^ell]tanh(x) ell! 2^(d-ell)`.  Even cycle counts vanish, while the first
forbidden derangement residual occurs at `(2,2,2)` in degree six.

The nonhook slack is now quantitative and sharp in every degree:

\[
 { |b_{d,\lambda}|\over f^\lambda}\le {d-4\over d}.
\]

This follows from the Adin--Reiner--Roichman cyclic-descent extension; the
families `(d-2,2)` and their transposes attain equality.  There is also a
rigidity no-go: every unit-disk tableau weight depending only on the descent
set and saturating the hooks is forced to equal `(-1)^|Des|` on every subset.
It therefore reproduces the same `tanh` certificate and cannot cancel the
odd-cycle residual from degree six onward.

The zero-hook correction exists algebraically in every degree: the
`p_1=0` image of the nonhook Schur span is exactly the hyperplane with zero
`p_d` coordinate.  This is still not the missing all-degree proof.  It
reduces the optimal-value statement exactly to choosing such a correction
for `[t^d](tanh(A)-A)` while staying in every remaining nonhook dimension
box; strict interior is additionally sufficient for uniqueness.
One infinite escape space is closed completely: adding any nonzero class
function supported on noncycle derangements with an even number of cycles
strictly increases the weighted rank mass.  Thus any cheaper all-degree
selector would have to engage an odd cycle-count stratum `ell>=3`, exactly
where the nonlinear `tanh` tail lives.
Read
[`FFPS_DERANGEMENT_SELECTOR_TANH_CALIBRATION.md`](function_field/FFPS_DERANGEMENT_SELECTOR_TANH_CALIBRATION.md).

### 2.9 Contractive repairs must propagate almost to the equator

Suppose an all-degree correction actually attains the conjectured optimum and
stays in every Schur dimension box. Divisibility of its `p_1`-free residual
gives a unique predecessor potential `X_(d-1)`. On the two-row chain, write
`X_j=[s_(d-1-j,j)]X_(d-1)`. Hook saturation and the neighboring two-row boxes
then telescope to the exact signed lower bound

\[
 \operatorname{Re}\!\left((-1)^{j-1}X_j\right)
 \ge {2^d\over d}-{d\choose j}.
\]

Hence every such lift has nonzero potentials in forced alternating
half-planes through

\[
 m_d={d\over2}-\left({1\over2}+o(1)\right)\sqrt{d\log d}.
\]

This eliminates bounded-depth, fixed-width, and near-hook repair formulae in
one stroke. For real lifts the half-planes become signs. It is only a
necessary condition: the off-chain Young-lattice constraints may permit or
forbid the required global extension. Read
[`FFPS_SELECTOR_YOUNG_LATTICE_PROPAGATION_OBSTRUCTION.md`](function_field/FFPS_SELECTOR_YOUNG_LATTICE_PROPAGATION_OBSTRUCTION.md).

### 2.10 Firewalls that must be retained

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
absolutely summable. By itself this does **not** permit summing the conductor
layers: `h>=5j+2`, the
`O_(q,j)(h^-4)` remainder, and complementary growing-depth profiles still
lack uniform control. Read
[`QUADRATIC_FAMILY_LOCAL_DELTA_TOWER_ANTICONCENTRATION.md`](function_field/QUADRATIC_FAMILY_LOCAL_DELTA_TOWER_ANTICONCENTRATION.md).

### 3.6 A whole growing logarithmic window is now controlled

The fixed-depth remainder can be bypassed completely.  Mark one least-degree
prime `R` of degree `d=h-j`, freeze the rough complement, and condition the
full detector modulo the product `A_r` of primes through `r=2j+1`.  Exact CRT
independence, top-channel anti-concentration, the normalized
prime-polynomial progression theorem, and the rough-complement bound give

\[
 {Z_{q,h,j}\over q^M}
 \le {\beta_r\over d^2}
 \left(1+(\ell_r+1)q^{\ell_r-d/2}\right),
 \qquad \ell_r=\deg A_r.
\]

If `ell_(2J+1)<=(h-J)/4`, summing every complete layer through `J` gives
`O_q(M^-2)`.  In particular, for each fixed `epsilon>0` and all sufficiently
large `h`, every `J<=(1/2-epsilon)log_q h` is safe.  This is a genuine
growing-depth conductor theorem, not formal coefficient summability.  Its
natural stopping point `q^(2j)~h` motivates the profile-averaged bridge in
the next subsection.  Read
[`QUADRATIC_FAMILY_LOGARITHMIC_DEPTH_ZERO_FIREWALL.md`](function_field/QUADRATIC_FAMILY_LOGARITHMIC_DEPTH_ZERO_FIREWALL.md).

### 3.7 Profile averaging exposes a conditional entropy-wall gate

Conditioning one complement is not the final word.  Stratify the full layer
by factor-degree profile and let `D_j` be the profile-weighted relative
chi-square discrepancy of the conductor residues modulo `A_r`.  Two exact
Cauchy steps and Parseval give

\[
 Z_{q,h,j}\le T_j(\beta_r+\sqrt{\beta_r}\,\mathfrak D_j).
\]

Because `d>r` permits at most five irreducible factors, Newton identities
reduce every profile Fourier coefficient to at most five prime sums.
Function-field RH for the corresponding Dirichlet characters then proves

\[
 \mathfrak D_j^2
 \le 614400M^{11}(\ell_r+1)^{10}q^{\ell_r-M}.
\]

Consequently the layer retains the sharp bound
`Z/q^M<=2 beta_r/d^2` whenever

\[
 q^{M-\ell_r-r}\ge
 1228800M^{11}(\ell_r+1)^{10}.
\]

The displayed condition permits `ell_r=M-O(r+log M)`, within a logarithmic
gap of the full residue-space entropy wall, and then gives `O_q(M^-2)`.  It
does not say that the discrete `ell_r` lands there for every `M`; the
unconditional realized corollary is `ell_r<=M/2` for sufficiently large `M`.
The method crosses the first CRT transition but does not create a
superlogarithmic depth window:
`ell_r=Theta_q(q^r)` still forces
`J=(1/2)log_q M+O_q(1)`.  The next theorem must use the special detector-zero
sets more economically than full residue equidistribution.  Read
[`QUADRATIC_FAMILY_PROFILE_CHI_SQUARE_BRIDGE.md`](function_field/QUADRATIC_FAMILY_PROFILE_CHI_SQUARE_BRIDGE.md).

### 3.8 The detector's squareclass quotient crosses the generic wall

The full unit residue contains much more information than the notch uses.
Let `K_r=sum_(e<=r)I_q(e)` be the number of small primes.  The detector
factors exactly through their quadratic signs, so Parseval needs only the
`2^K_r` quadratic conductor characters.  The profile argument sharpens to

\[
 \mathfrak Q_j^2
 \le 614400M^{11}(\ell_r+1)^{10}2^{K_r}q^{-M}.
\]

In particular `2^(2K_r)<=q^M` implies the explicit gate for all sufficiently
large `M`.  Since

\[
 K_r={q^{r+1}\over(q-1)r}(1+O_q(r^{-1})),
\]

the terminal safe scale is

\[
 r=\log_qM+\log_q\log M+O_q(1),
\]

and every earlier layer still sums to `O_q(M^-2)`.  This is an unbounded
additive extension beyond the generic `ell_r<M` wall, not a mesoscopic
window.  Degree-wise permutation invariance compresses the exact remaining
Fourier space to Krawtchouk orbits, but triangle-bounding their constituent
characters recovers `2^K_r` exactly.  The open normalized orbit estimate
`KRAWLS` would conditionally reach `r=Theta(sqrt M)`.
Read
[`QUADRATIC_FAMILY_SQUARECLASS_ENTROPY_COMPRESSION.md`](function_field/QUADRATIC_FAMILY_SQUARECLASS_ENTROPY_COMPRESSION.md).

### 3.9 Depth and full-aperture laws

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

Start from the new universal ternary norm torsor and tensor it with the actual
Boolean/owner/phase source before separate absolute values or exact-cycle
rank masses are taken. Determine whether the complete virtual cone cancels
the hook selector, or replace it by a prime-polynomial trace formula. This
targets the source and entropy/conductor obstructions directly; another
fixed-fibre Kummer example would not.

### Highest standalone arithmetic-geometry bet

Resolve the `Sym^12` realization arrow by comparing the nonregular
Eisenstein Galois filtration, not by fitting more unrelated primes. A
same-characteristic tower or direct boundary cohomology computation would be
more informative than a fourth small prime.

### Ambitious discovery lanes

1. Build a renormalization flow for the native reflection current in a small
   basis of boundary-shell correlations, retaining early-prime memory.
2. Prove `KRAWLS` or another detector-specific small-ball theorem on the
   squareclass quotient.  The exact `2^K_r` compression already crosses the
   generic residue wall by `log log M`; constituent-wise estimates recover
   that entire entropy and cannot reach the conditional `sqrt M` scale.
3. Use quotient-subgroup masks beyond parity to keep selected rank fixed
   while varying conductor geometry; classify when relative projectors
   descend over nonsplit base fields.
4. Automate cohomological conjecture generation only after the exact adapter,
   representation channel, and Galois normalization are locked.
5. Solve or disprove the selector's contractive primitive lift; its full
   forbidden class transform and almost-half-depth propagation law are now
   explicit, so more finite LP degrees are lower priority than a global
   Young-lattice extension or impossibility theorem.

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
