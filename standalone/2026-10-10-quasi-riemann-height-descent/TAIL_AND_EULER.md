# Tail zero criteria and a larger analytic domain for the imported probe

Status: Proposed research component, 2026-10-10. The local algebra and the analytic reductions below have complete proofs. They do not prove a new zero-free half-plane or a height strip tending to the critical line.

Scope: A source-qualified extension of the imported principal Euler correction; exact criteria for a tail bound on zeta zeros; identification of the remaining low-side and noncancellation obligations.

Exact sources or dependencies: OpenAI `math` commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, September 30 manuscript `preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`. The published research import is PR 908 at `31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6`. Root reports that the relevant upstream files are unchanged at October 8 commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`. Standard analytic continuation of nonprincipal unitary Hecke L-functions is an additional dependency wherever explicitly stated. The Gaussian converse uses the classical Hadamard product and the estimate `N(T)=O(T log T)` for zeta zeros.

What was actually run: Direct inspection of the local identities, selected-prime correction, four shared analytic lemmas, and the low bound. Exact rational and polynomial checks are recorded separately in `checks/check_tail_euler.py` and its output: ordinary and optimized Python runs each pass 83 explicit predicates with byte-identical JSON. No Lean kernel build or new zero computation was performed.

Smallest remaining gap: A direct estimate for the same normalized physical probe with exponent strictly smaller than its proposed principal signal, with all high-side hypotheses verified at the new parameters. For a tail theorem, the direct estimate must include exact removal of finite reciprocal poles, or a different genuinely local zero detector with a proved pointwise lower bound.

## 1. What is new here, and what is not

The manuscript's explicit `sigma0 >= 7/8` hypothesis is not the limiting condition of its principal Euler algebra. With the same contours in `w,z`, direct absolute convergence works for any fixed

\[
\alpha>\frac{401}{600}=0.668333\ldots.
\]

The selected-prime correction and its nonzero principal normalization also extend to this region. A further exact factorization isolates a unitary Hecke L-function of angular type `-6`. At the double residue the remaining product is holomorphic and nonzero for `Re s > 1/2`, while the extracted Hecke factor is nonzero by its absolute Euler product for `Re s > 2/3`.

These are larger analytic domains for ingredients of the argument. They are not bounds on the real parts of zeta zeros. The published low estimate has no fixed saving at `7/8`: its exponent is exactly the principal exponent there. A positive high-side margin cannot compensate for that equality.

## 2. Direct extension of the principal Euler region

Use the manuscript's notation, but denote the real lower bound by `alpha` to distinguish it from its angular function `alpha(a)=a/|a|`. Let

\[
\mathcal D_2(\alpha)=\{(s,w,z):\Re s\ge\alpha,
\ \Re w\ge19/20,\ \Re z\ge33/200\}.
\]

### Lemma 2.1: Uniform local bounds

Fix `401/600 < alpha <= 1`. The complete local factors in `paper.tex`, equations `local-P`, `local-H-definition`, and `local-H-defect` (lines 4007–4193), satisfy throughout this region

\[
H_p-1\ll_\alpha Q^{-1-\lambda(\alpha)}\quad(p\nmid u),
\qquad H_p-1\ll_\alpha Q^{-\mu(\alpha)}\quad(p\mid u),
\]

where

\[
\lambda(\alpha)=\min\{6\alpha-401/100,\ \alpha-3/50\}>0,
\qquad
\mu(\alpha)=\min\{\alpha-1/20,\ 3\alpha-3/2\}>0.
\]

The bounds are uniform in imaginary parts and every unit phase. The product `H_eta,u` converges normally locally around every point of this region and is `O_epsilon(q_u^epsilon)`. After a fixed enlargement of the excluded set by primes of norm at most `P0`, its principal member `u=1` satisfies

\[
\sup_{\mathcal D_2(\alpha)}|\mathcal H_{\eta,1}-1|\le1/2.
\]

The choice of `P0` is uniform in the target's unit phases. This changes the fixed excluded set for the proposed new application; it does not change a previously reviewed application.

**Proof.** Put `x_r=Re s`, `w_r=Re w`, `z_r=Re z`. The source gives

\[
V=Q^{-6z},\quad R=a_p^2Q^{4-6s-6z},\quad
D=\eta(p)\overline{\chi_p(u)}Q^{-s},\quad W=\chi_p(u)Q^{-w}.
\]

The only local denominators in the simplified formulas are `1-R,1-V,1-D`. They are uniformly separated from zero here: in particular `|R| <= Q^{301/100-6alpha} < Q^{-1}`. There is no `1-W` denominator in the defect formula.

For a good prime put `E_p=P_p^*+D`. The exact source identities give

\[
H_p-1=\frac{D(V+W-VW)-VW+(1-V)(1-W)E_p}{1-D},
\]

\[
|E_p|\ll Q^{4-6x_r-6z_r}+Q^{1-x_r-w_r-6z_r}.
\]

The following are all potentially largest exponents; products with additional `V` or `W` are smaller.

| Term | Upper exponent of `Q` | Decay beyond `Q^-1` |
|---|---:|---:|
| `DV` | `-alpha-99/100` | `alpha-1/100` |
| `DW` | `-alpha-19/20` | `alpha-1/20` |
| `VW` | `-97/50` | `47/50` |
| first term of `E_p` | `301/100-6alpha` | `6alpha-401/100` |
| second term of `E_p` | `-alpha-47/50` | `alpha-3/50` |

For `alpha <= 1`, the minimum of this final column is the claimed `lambda`.

At a ramified prime `D=W=0`, and `(1-V)P_p^*` is the defect. The term proportional to `(Q-1)Q^{-s-w}` has exponent at most `1/20-alpha`. The complete boundary table in the source gives the following decay exponents; dropping an extra `V` only weakens a bound.

| Ramified contribution | Positive decay exponent |
|---|---:|
| `R` | `6alpha-301/100` |
| strict second family | `alpha-1/20` |
| `J_1` | `alpha+19/20` |
| `J_2` | `3alpha-3/2` |
| first term of `J_3` | `3alpha-21/20` |
| second term of `J_3` | `4alpha-2` |
| `J_4` | `4alpha-31/20` |
| `J_5` | `6alpha-3` |

For `alpha>401/600`, every entry is at least `min(alpha-1/20,3alpha-3/2)`. For example the comparison of `R` with `J_2` is `3alpha-151/100>0`, and the comparison of the second `J_3` entry with `J_2` is `alpha-1/2>0`.

The ideal count `#{a: Na <= X}=O(X)` proves summability of the good-prime majorant. The finitely many factors at primes dividing `u` satisfy the standard divisor-product bound, hence cost `q_u^epsilon`. The same estimates with slightly smaller real lower bounds prove normal convergence on a neighborhood of each boundary point. For `u=1`, the tail sum is `O_alpha(P0^-lambda)`. The inequality `|prod(1+a_p)-1| <= exp(sum |a_p|)-1` gives the fixed contraction after enlarging `P0`. This also proves individual nonvanishing of the retained principal factors. ∎

Useful exact instances are:

| `alpha` | Good-prime defect | Ramified-prime defect |
|---|---:|---:|
| `3/4` | `O(Q^-149/100)` | `O(Q^-7/10)` |
| `4/5` | `O(Q^-87/50)` | `O(Q^-3/4)` |
| `437/500 = 7/8-1/1000` | `O(Q^-907/500)` | `O(Q^-103/125)` |
| `7/8` | `O(Q^-363/200)` | `O(Q^-33/40)` |

The last row reproduces the source's bounds exactly.

### Lemma 2.2: The selected-prime correction extends as well

Retain the manuscript's fixed finite slot system and its exact, quotient-free selected-tuple correction (`paper.tex` lines 8684–8771). On `D_2(alpha)` this full correction is holomorphic and obeys the required all-height polynomial majorant. On the principal row,

\[
\mathcal B_p=-1+O_\alpha(Q^{-\nu(\alpha)}),
\quad
\nu(\alpha)=\min\{\alpha,99/100,5\alpha-301/100,47/50\}>0.
\]

Moreover, on each fixed real box,

\[
|\mathfrak H_{\eta,1,Z}(s,w,z)|\ll Z^{\ell\Re z}.
\]

**Proof.** The formula for the selected factor `G_p` has only the denominators `1-R,1-V,1-D`, all controlled by Lemma 2.1. The full correction is a finite sum of selected products `G_p` times normally convergent unselected products `H_p`; it uses no division by a vanishing `H_p`. Thus it is holomorphic. On a fixed real box each selected factor is `O(Q^B)` for a fixed `B`, uniformly in heights, so ideal counting in the finite slots gives the same all-height majorant as in the source.

For `u=1`, the exact cancellation identity at `paper.tex` line 8808 yields

\[
|G_p+H_p|\ll
Q^{-x_r}+Q^{-6z_r}+Q^{4-5x_r-6z_r}+Q^{1-w_r-6z_r}.
\]

In the extended box the four positive decay exponents are precisely the entries defining `nu`. The lower bound on `H_p` from Lemma 2.1 permits division for this principal row, giving the approximation. In particular `G_p=O(1)`. The positive majorant for an unselected product stays bounded. Each slot contributes `sum_{p asymp P_i}|W_i(Q/P_i)| Q^{z_r-1}=O(P_i^{z_r})`; multiplication gives `Z^{ell z_r}`. ∎

For `alpha=3/4`, `nu=37/50`; for `alpha=4/5`, `nu=4/5`; for `alpha=437/500`, `nu=437/500`. At the principal normalization, a slot error relative to its nonzero prime sum is therefore `O(P_i^-nu)`, subject to the same prime-sum lower bound used by the original source. The exponent remains positive at each candidate.

## 3. Extracting the leading Euler factor

There is a stronger exact algebraic result than merely moving a rectangular boundary.

Let `A(a)=a/|a|` be the manuscript's angular function. Since every unit of `Q(sqrt(-3))` has sixth power one and the class number is one,

\[
\chi_\eta((a))=\overline{A(a)}^{\,6}\eta((a))^6
\]

is a well-defined unitary Hecke character, independent of the chosen ideal generator. It has angular type `-6`; it is not a finite-order character. The source's exact definition `a_p=bar(alpha(p))^3 eta(p)^3` gives `a_p^2=chi_eta(p)`.

### Lemma 3.1: Exact factorization at the double residue

For `u=1,w=1,z=1/6`, write `t=Q^-1`, `D=eta(p)Q^-s`, and `R=chi_eta(p)Q^{3-6s}`. Then

\[
P_p^*=\frac{(1+t)(R-D)}{1-R},
\qquad
H_p=\frac{1-t^2}{1-R}
\left(1+\frac{t(D-R)}{1-D}\right).
\tag{3.1}
\]

Consequently, first in absolute convergence and then wherever continued,

\[
H_\eta(s)=
\frac{L_F^S(6s-3,\chi_\eta)}{\zeta_F^S(2)}K_\eta(s),
\tag{3.2}
\]

\[
K_\eta(s)=\prod_{p\notin S}
\left(1+
\frac{\eta(p)Q^{-s-1}-\chi_\eta(p)Q^{2-6s}}
 {1-\eta(p)Q^{-s}}\right).
\tag{3.3}
\]

The product `K_eta` converges normally and is nowhere zero for `Re s>1/2`.

**Proof.** Substitute `V=W=t` into the complete `j=0` formula. Its bracket becomes `(1+t)(R-D)`. Adding its `t=0` contribution `(1+t)/(1-t)` gives (3.1); Euler multiplication gives (3.2).

For `Re s >= a > 1/2`, each `K_p-1` is `O_a(Q^{-a-1}+Q^{2-6a})`, a summable prime majorant. Its numerator after writing it over `1-D` is

\[
1-(1-t)D-tR.
\]

For `Re s >= 1/2`, `|D|<=Q^-1/2` and `|R|<=1`. Thus

\[
|(1-t)D+tR|
\le (1-Q^{-1})Q^{-1/2}+Q^{-1}<1.
\]

For the strict inequality put `y=Q^-1/2`, so its left side is `y+y^2-y^3`, and
`1-y-y^2+y^3=(1-y)^2(1+y)>0` for `0<y<1`. No local factor vanishes. A normally convergent product with summable defects and no vanishing local factors is nowhere zero. ∎

**Consequences and precise limitation.** For `Re s>2/3`, the extracted `L`-function is nonzero by absolute Euler convergence, since `Re(6s-3)>1`. Thus `H_eta` is nonzero there. The required standard entire continuation of this angular Hecke L-function follows from the global continuation theorem in Bjorn Poonen's *Tate's Thesis* notes, Theorem 5.22, p. 38; its exceptional norm-character components cannot have angular type `-6`. With that explicitly external input, (3.2) makes `H_eta` holomorphic for `Re s>1/2`. Its zeros in that domain are exactly the zeros of `L_F^S(6s-3,chi_eta)`, with the same multiplicities. There is no justification here for deleting that factor from the principal signal or assuming that it cannot cancel a target zero. The imported theorem for finite-order targets does not cover this angular character.

The constant `1/ζ_F^S(2)` in (3.2) is essential. The defect exponents at the exact residue, before extraction, require `6 Re s-3>1`, so the natural absolute-convergence floor there is `2/3`, not the slightly larger rectangular floor `401/600`.

Poonen's theorem is stated for the product including archimedean factors. Passing to the finite Euler product divides by the gamma factor, whose reciprocal is entire; deleting the fixed finite set `S` multiplies by finitely many entire local factors. Thus the stated continuation applies to the precise incomplete finite Euler product in (3.2).

### Lemma 3.2: Exact extraction on the full principal rectangle

For the principal row, with arbitrary `w,z` and the same `D,V,W,R`, direct simplification gives

\[
(1-R)H_p=1+
\frac{D(V+W-VW)-VW-(Q-1)DWV(1-W)
-R\{Q^{-1}(1-W)+W^2(1-V)\}}{1-D}.
\tag{3.4}
\]

Therefore `H_eta,1(s,w,z)` has the extracted factor

\[
L_F^S(6s+6z-4,\chi_\eta).
\]

The remaining Euler product converges normally on `D_2(alpha)` for every fixed `301/600 < alpha <= 1`. Its good-prime defect has exponent

\[
O(Q^{-1-\kappa(\alpha)}),\qquad
\kappa(\alpha)=\min\{\alpha-3/50,\ 6\alpha-301/100\}>0.
\]

**Proof.** Multiply the source formula for `P_p` by `(1-R)(1-V)(1-W)/(1-D)` and collect the terms with `R`. Their coefficient is `-Q^-1(1-W)-W^2(1-V)`, giving (3.4). In its numerator the potentially largest exponents are those of `DV,DW,VW,QDWV,R/Q,RW^2`. The first four have excess decay at least `alpha-3/50`; the last two have excess decay `6alpha-301/100` and `6alpha-211/100`. The asserted minimum follows. Normal convergence is the same majorant argument as in Lemma 2.1. ∎

At `alpha=51/100`, `kappa=1/20`. This is a concrete continuation mechanism close to `1/2`, provided the angular Hecke factor is analytically continued. It does not by itself prove nonvanishing of that factor.

For selected tuples one may analogously set `Gtilde_p=(1-R)G_p`. Removing the common extracted Euler factor leaves a finite sum of products of `Gtilde_p` and the unselected factors in (3.4). Thus the local singular denominator `1-R` is removable at the level of the extracted representation. Claiming the original all-height majorant in this wider region would additionally require the stated angular-Hecke vertical-growth input; no such bound is silently inherited from the finite-order family theorem.

### A conditional common-family observation

Suppose a larger class of target characters were closed under `eta -> bar(A)^6 eta^6`, and let `beta_*` be the supremum of zero real parts for that class. At a target extremal zero the auxiliary argument has real part approximately `6 beta_*-3`. This is larger than `beta_*` when `beta_*>3/5`. Under the closed-family hypotheses, that proves noncancellation near the common extremum without separately proving RH for the auxiliary factor.

This is an exact conditional inequality, not an extension of the existing theorem. Iterating the character map starting from angular weight zero gives weights `0,-6,-42,-258,...`; the source uses finite fixed ray families and cannot simply be declared to include this orbit. A reviewable extension would have to rebuild that family input and its uniformity.

## 4. Where the published `7/8` barrier actually remains

The four shared lemmas at source lines 5811, 6024, 6178, and 6345 explicitly state `sigma0 in [7/8,1)`. Reusing their statements below `7/8` is invalid. Their proofs nevertheless show the following precise division of responsibilities.

| Shared ingredient | Relevant condition in its proof | What changes below `7/8` |
|---|---|---|
| Fixed-bin contour | `D_1(epsilon0)`, floor `a>=51/100`, `a<=beta_*` | The displayed contour inequalities do not use `7/8`; retain the same buffered zero hypotheses and choose positive margins. |
| Retained integral exponent | Addition of outside Mellin powers | `C(sigma0)+E_sigma0` is independent of `sigma0`; the reference level alone carries no analytic gain. |
| Principal residue extraction | Holomorphy and bounds in the principal rectangle; nonzero normalized signal | Lemmas 2.1–2.2 supply the needed rectangular domain for any fixed `alpha>401/600`. |
| Small outer rows | Line `(beta_*+e,1/2,17/50)` in `D_1(epsilon0)` | Replace the source's convenient `epsilon0=3/8` by a fixed `0<epsilon0<alpha-1/2`; the selected-prime upper estimates remain valid. |
| Large outer rows | Fixed line `(2,2,v)`, `v>2` | This does not depend on the proposed endpoint. |

For the small selected-prime bound, the good-prime errors have exponents `-x_r,-51/25,49/25-5x_r,-77/50`, all bounded above by zero for `x_r>401/600`. After the ramified terms are multiplied by `Q^{x_r}`, the boundary exponents are
`-1/2, 3/2-2x_r, 2-3x_r, 3-5x_r`; every one is at most `1/2` already for `x_r>=1/2`. Thus the source's `G_p=O(1)` off `u` and `G_p=O(Q^{1/2})` on `u` have room. The conductor-deficit argument and row envelope still need to be instantiated with their exact unchanged hypotheses.

By contrast, the published low estimate is

\[
|J_{\mathrm{II},\eta}(Z)|\ll_{\eta,\epsilon}Z^{3/16+\epsilon},
\qquad C_{\mathrm{II}}(s)=s-11/16.
\]

The source explicitly records at lines 8642–8648

\[
C_{\mathrm{II}}(7/8)=3/16=l_x/2+b/12.
\]

Hence its saving relative to the principal exponent is exactly `beta_*-7/8`. For `beta_*<7/8`, the unchanged low bound is larger than the principal scale. There is no fixed endpoint gain from an open endpoint or from high-side slack alone.

Changing the geometry is a legitimate different route. Its admissibility must include the physical low estimate, the exact same high identity and normalizer, all slot-length/Gram/row-norm hypotheses, and a compact-domain high exponent certificate. Verifying strict inequalities for a final affine envelope alone does not verify that the input estimates remain available. The separate [completed geometric proof](GEOMETRY_PERTURBATION.md) now carries out that construction at `ell=1/6+1/40000` and the endpoint `7/8-1/160000`, conditional on its explicitly listed imported analytic machinery. Its new adapters received a scoped independent source review. The saturation statement above concerns only the fixed published geometry.

## 5. The exact meaning of a height strip tending to `1/2`

Let `ZetaZeros` be the nontrivial zeros of zeta, with multiplicities irrelevant to the following supremum. Define

\[
B(T)=\sup\bigl(\{1/2\}\cup
\{\Re\rho:\rho\in\mathrm{ZetaZeros},\ |\Im\rho|\ge T\}\bigr),
\qquad B_\infty=\lim_{T\to\infty}B(T).
\]

The limit exists because `B(T)` is decreasing and lies in `[1/2,1]`.

### Lemma 5.1: Equivalent tail formulations

The following are equivalent.

1. `B_infty=1/2`.
2. For every `a>1/2`, there are only finitely many zeros with `Re rho>a`.
3. For every `epsilon>0`, all sufficiently high zeros satisfy `Re rho<=1/2+epsilon`.
4. There is a nonnegative decreasing function `delta(T)->0` such that all nontrivial zeros satisfy `|Re rho-1/2|<=delta(|Im rho|)` after any fixed finite initial range is included in the definition of `delta`.

**Proof.** The equivalence of 1 and 3 follows directly from the definition of a decreasing tail supremum. A bounded-height closed portion of the critical strip contains only finitely many zeros, since zeta is meromorphic and its zeros are isolated; this gives 2 iff 3. The functional equation pairs `beta+i gamma` with `1-beta+i gamma`. Hence the upper bound controls both sides. One can take `delta(T)=B(T)-1/2` for 1 implies 4; 4 implies 3 immediately. ∎

This theorem concerns a tail supremum, not an average zero density. As a statement about locations it allows finite exceptions, and also infinitely many off-line zeros whose distances from the line tend to zero. It does not itself assert that every zero is on the line. A further zero-replication or rigidity theorem would be required to convert it into RH; none is supplied by the imported proof or by this report.

The distinction between a fixed zeta function and an entire character family is substantial. For one fixed target, a bounded-height set is finite. Across unbounded conductors, a common bounded-height set of zeros need not be finite. A family proof cannot perform one finite low-pole subtraction for all targets without a separate conductor/height argument.

## 6. Exact pole subtraction and a Gaussian criterion

### Lemma 6.1: The meromorphic criterion

For fixed `a>1/2`, there are finitely many zeta zeros in `Re s>a` if and only if a finite sum of principal parts `P_a(s)` makes

\[
1/\zeta(s)-P_a(s)
\]

holomorphic in `Re s>a`.

**Proof.** Subtract the Laurent principal part at every pole of `1/zeta` in that half-plane. Conversely, subtracting a rational function with finitely many poles cannot remove any other pole. A zero of multiplicity `m` gives a pole of order `m`; its highest Laurent coefficient is nonzero. ∎

For a simple zero `rho`, its principal part is `1/(zeta'(rho)(s-rho))`. Multiple zeros require all principal-part coefficients. A numerical list of ordinates alone does not supply this subtraction, and it does not preserve an arithmetic source identity automatically.

Fix `H>0` and `tau` real. Define

\[
W_H(u)=\frac{H}{2\sqrt\pi}\exp\left[-\frac{H^2(\log u)^2}{4}\right],
\quad W_{\tau,H}(u)=u^{-i\tau}W_H(u),
\]

\[
S_{\tau,H}(x)=\sum_{n\ge1}\mu(n)W_{\tau,H}(n/x),
\qquad E_{\tau,H}(s)=e^{(s-i\tau)^2/H^2}.
\]

The elementary Gaussian integral gives

\[
\int_0^\infty W_{\tau,H}(u)u^{s-1}\,du=E_{\tau,H}(s).
\]

Consequently, for `Re s>1`,

\[
\int_0^\infty S_{\tau,H}(x)x^{-s-1}\,dx
=\frac{E_{\tau,H}(s)}{\zeta(s)}=:G(s).
\tag{6.1}
\]

Every interchange is absolute: with `sigma=Re s>1`, the sum of absolute integrals is `zeta(sigma)` times a finite Gaussian moment. For every `N>0`, `S(x)=O_N(x^N)` as `x->0`, by the rapid multiplicative decay of `W` and, for example, a bound `|W(u)|<=C_A u^-A` with `A>max(N,1)` on `u>=1`.

Let `P` be any finite set of nontrivial zeros. At `rho in P`, write the principal part of `G` as

\[
\sum_{j=1}^{m_\rho}\frac{c_{\rho,j}}{(s-\rho)^j}.
\]

For `x>=1` define the exact residue correction

\[
R_P(x)=\sum_{\rho\in P}\sum_{j=1}^{m_\rho}
c_{\rho,j}\frac{x^\rho(\log x)^{j-1}}{(j-1)!}.
\tag{6.2}
\]

Equivalently, each summand in `rho` is `Res_{s=rho}(x^s G(s))`. This is the principal part of the **weighted** reciprocal `G`, not just that of `1/zeta`.

### Proposition 6.2: A fully global certificate after finite subtraction

If, for some `a>1/2`,

\[
S_{\tau,H}(x)-R_P(x)=O(x^a)\qquad(x\to\infty),
\tag{6.3}
\]

then every zero in `Re s>a` belongs to `P`. In particular, if all members of `P` have `|Im rho|<T`, there is no zero with `Re rho>a` and `|Im rho|>=T`.

**Proof.** For `Re s` sufficiently large,

\[
G(s)-\sum_{\rho\in P}\sum_j\frac{c_{\rho,j}}{(s-\rho)^j}
=\int_0^1 S(x)x^{-s-1}\,dx
+\int_1^\infty(S(x)-R_P(x))x^{-s-1}\,dx.
\]

Here `int_1^infty x^{rho-s-1}(log x)^{j-1} dx=(j-1)!/(s-rho)^j`. The first integral is entire, using the small-`x` bounds; the second is holomorphic for `Re s>a`, including its differentiated integrals on compact subsets. The right side therefore continues the weighted reciprocal minus the specified principal parts to that half-plane. The Gaussian multiplier is entire and nowhere zero, so an unselected zeta zero there would remain a pole, a contradiction. ∎

The cutoff at `x=1` matters. Subtracting `R_P(x)` also as `x->0` generally destroys the small-`x` estimate and the entire first integral. A smooth cutoff is possible, but its exact Mellin correction must then be included.

### Proposition 6.3: Equivalence with a smoothed remainder, allowing arbitrary small losses

For fixed `a>1/2`, the following are equivalent:

* There are only finitely many zeros in `Re s>a`.
* There is a finite set `P` such that for every `epsilon>0`,
  `S_tau,H(x)-R_P(x)=O_epsilon(x^{a+epsilon})`.

It suffices to fix one `tau` and one `H>0`; constants may depend on them and on `P`.

**Proof of the forward implication.** Let `P` be all zeros in `Re s>a`. Fix `epsilon>0` and choose `c` in `(a,a+epsilon/2)` avoiding the finitely many real parts of zeros in `P`. Start with the absolutely convergent inverse Mellin integral on a line to the right of one and move it to `Re s=c`. Only the finite members of `P` with real part greater than `c` are crossed.

For completeness, Gaussian decay justifies the shift without assuming that holomorphy alone bounds a reciprocal. The classical Hadamard product for zeta, the estimate `N(r)=O(r log r)`, and distance at least `c-a` from every high zero give, uniformly on the fixed real strip at sufficiently large heights,

\[
|1/\zeta(\sigma+it)|\le
\exp\bigl(C(1+|t|)\log^2(3+|t|)\bigr).
\]

To verify the estimate, split the canonical product at `|rho|=2r`, `r=2+|s|`. In the inner part bound `log(|rho|/|s-rho|)` by `log(2r/d)` and sum `|s/rho|`; these cost `O(r log^2 r)`. In the outer part use `log((1-z)e^z)=O(|z|^2)` for `|z|<=1/2` and `sum_{|rho|>2r}|rho|^-2=O(log r/r)`. Gamma and elementary prefactors have smaller logarithmic growth on the fixed strip. Finitely many low zeros affect only a constant or compact-height exclusions. The negative quadratic in `E_tau,H` dominates this bound, so horizontal integrals vanish and the new vertical integral is `O(x^c)`.

Subtracting all of `R_P`, rather than just the crossed residues, leaves finitely many additional terms `x^rho` times polynomials in `log x` with `Re rho<c`. These are `O_epsilon(x^{a+epsilon})`. This proves the forward implication.

Conversely, Proposition 6.2 with every positive `epsilon` excludes every zero with real part greater than `a` outside the finite set: given such a zero, choose `epsilon<Re rho-a`. ∎

Combining Propositions 6.2–6.3 with Lemma 5.1 gives an exact analytic reformulation of `B_infty=1/2`. It does not estimate the arithmetic sum. Proving the remainder bound is the missing theorem, not a corollary of introducing the smoothing.

## 7. Why twisting and height averaging do not remove individual zeros

### 7.1 A fixed pure twist preserves the global summatory exponent

For `M(x)=sum_{n<=x}mu(n)` and `M_t(x)=sum_{n<=x}mu(n)n^{-it}`, partial summation gives

\[
M_t(x)=x^{-it}M(x)+it\int_1^x M(u)u^{-it-1}\,du.
\]

For every fixed `t` and `a>0`, `M(x)=O(x^a)` implies `M_t(x)=O_t(x^a)`. Applying the same identity to recover `M` from `M_t` proves the converse. The factor in the bound may grow with `|t|`, but the global exponent is unchanged. Thus proving an all-`x` improved exponent for one fixed pure twist is already a global result, not a localized high-zero result.

### 7.2 A Gaussian attenuates a low pole; it does not annihilate it

For a simple zero `rho=beta+i gamma`, its exact contribution to (6.2) is

\[
\frac{x^\rho}{\zeta'(\rho)}
 e^{(\rho-i\tau)^2/H^2},
\]

whose modulus is

\[
\frac{x^\beta}{|\zeta'(\rho)|}
\exp\left(\frac{\beta^2-(\gamma-\tau)^2}{H^2}\right).
\]

For fixed `tau,H`, its coefficient is never zero. If `beta>a`, it eventually exceeds every fixed multiple of `x^a`, however far `gamma` is from `tau`. With several poles the phases can cancel at particular `x`; Proposition 6.2 handles the global obstruction without assuming pointwise dominance of any one residue.

For low poles `|gamma|<=T0` and a center with `|tau|>=T0+D`, attenuation can hide a term of exponent at most `theta` on a finite range of `x`. A sufficient comparison is

\[
D^2/H^2\ \gtrsim\ (\theta-a)\log x+\log C,
\]

with the fixed coefficient, the `beta^2/H^2` term, and multiplicity powers of `log x` included in `C` or explicitly retained. The inequality cannot hold for every `x` with fixed `D,H` when `theta>a`. Varying the kernel with `x` requires a new identity and uniform derivative/seminorm estimates; it is not the fixed transform in Proposition 6.2.

### 7.3 A uniform band for an arbitrarily translated family would already imply the full line bound

Suppose a function family is closed under every vertical translation `F(s)->F(s+iv)`, and one common function `delta(|t|)->0` bounds all its zeros. If `F` has a zero with real part `beta`, choose translations that move its ordinate to arbitrarily large absolute values while preserving `beta`. Then `|beta-1/2|<=delta(T)` for arbitrarily large `T`, forcing `beta=1/2`.

The imported finite-order character family is not closed under arbitrary norm twists. In a family enlarged to contain them, the analytic conductor records the shift; relabeling a zero cannot make its conductor disappear. Any proposed height theorem must state whether its thresholds depend on the target or on its archimedean twist.

Ordinary Voronin universality gives approximation of nonvanishing holomorphic targets on admissible compact sets. It therefore does not supply zero replication for a target disk containing an off-line zeta zero. A hypothetical sufficiently close approximation to such a target on the disk boundary would indeed reproduce a zero by Rouché's theorem; the missing premise is precisely the approximation of that vanishing target. See the primary paper of Lamzouri–Lester–Radziwill below for a precise nonvanishing hypothesis and an effective version.

### 7.4 Small averages need a detector lower bound

An averaged upper bound does not imply that every member is small, and a signed spectral average can cancel. Even a nonnegative average can miss a narrow spike without a lower bound on its width. To use a mean-square height estimate to exclude a single zero, one must prove that the zero forces a definite contribution to that very mean square, with explicit dependence on distance from the line, multiplicity, height and any localization parameters. Neither Gaussian localization nor a zero-density estimate alone supplies such a detector.

A valid elementary special case illustrates the missing distinction. For a fixed finite exponential sum `P(y)=sum_j a_j exp(i gamma_j y)` with distinct real frequencies,

\[
\lim_{Y\to\infty}\frac1Y\int_0^Y|P(y)|^2\,dy=\sum_j|a_j|^2.
\]

The proof expands the square; each off-diagonal integral divided by `Y` tends to zero. Thus a nonzero finite collection of rightmost pole terms cannot remain exponentially smaller at all logarithmic scales. The averaging variable is `y=log x` for a fixed finite set of residues. Passing to infinitely many poles, a moving height window, or a moving family requires additional uniform bounds; this finite calculation does not justify that passage.

## 8. A precise next target for a quantitative height band

Here is a theorem-shaped target with complete quantifiers. Let `a(T)=1/2+delta(T)` where `delta(T)>0` decreases to zero. For each sufficiently large `T`, let `P_T` consist of a finite collection of zeros of height strictly less than `T`, including their exact weighted principal parts. If for one fixed `H>0` and any chosen finite real center `tau_T`,

\[
S_{\tau_T,H}(x)-R_{P_T}(x)=O_T(x^{a(T)})
\quad\text{for every sufficiently large }x,
\tag{8.1}
\]

then all zeros of height at least `T` satisfy `Re rho<=a(T)`. The functional equation gives the symmetric band. Constants and the starting `x` may depend on `T`; the exponent and the exclusion of all high zeros follow from Proposition 6.2. With arbitrary small exponent losses, the same conclusion follows by intersecting the resulting half-planes.

Equation (8.1) is a useful exact reduction because it separates low-height exceptions from the tail. It is also a strong arithmetic assertion: the nonzero Gaussian sees every unremoved pole. Centering it at one height does not reduce the assertion to one window.

For the imported arithmetic probe, the analogous plan would subtract the exact residues of its actual principal multiplier times `1/L`. The direct and high representations would both have to be modified with the same subtraction. For the native signed Mellin/Landau route in this repository, finite residue subtraction similarly changes the signed source and any negative-mass accounting. These are possible points of composition, not inherited estimates.

The shortest credible sequence is therefore:

1. Record Lemmas 2.1–2.2 and the exact factorization as separately reviewed local analytic improvements.
2. Obtain an admissible geometry or a stronger direct physical estimate whose low exponent beats a specified endpoint below `7/8`.
3. Rebuild the high exponent certificate at that geometry, retaining its all-height and principal-noncancellation conditions.
4. For a tail program, prove a source-level counterpart of (8.1) with exact finite pole corrections. If one instead uses a finite height window and finite range of `x`, supply a separate quantitative detector theorem explaining how that finite information excludes a zero in the window.

The first item has concrete proved components here. The companion [geometric deduction](GEOMETRY_PERTURBATION.md) completes items 2–3 for a small rational improvement, relative to the listed imported inputs. The tail estimate and the stronger native off-diagonal bound remain open. No positive-density assertion or finite zero census supplies either missing estimate.

## Source locations and primary references

* [Pinned September 30 manuscript](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex): angular definition line 575; local parameters 3859–3867; complete six-row identity 4007–4035; defect and convergence bounds 4142–4193; principal normalization 5520–5534; high-data domain 5568–5667; shared analytic lemmas 5808–5920, 6020–6163, 6174–6300, 6341 onward; low exponent equality 8640–8648; selected quotient-free correction 8684–8771; local cancellation 8808; principal selected bounds 9051–9092.
* [NIST DLMF §25.2, especially 25.2.12](https://dlmf.nist.gov/25.2): the classical product over nontrivial zeros used in the Gaussian converse; the proof above additionally names the classical zero-count estimate it needs.
* [NIST DLMF §25.4](https://dlmf.nist.gov/25.4) and [§25.10](https://dlmf.nist.gov/25.10): reflection and zero symmetry.
* Bjorn Poonen, [Tate's Thesis notes](https://math.mit.edu/~poonen/786/notes.pdf), Theorem 5.22, p. 38: global continuation of Hecke L-functions across character components, with only the exceptional norm-character poles. The angular-type condition is what is used here; the theorem and its normalization were directly checked in this pass.
* S. M. Voronin, [Theorem on the universality of the Riemann zeta-function](https://www.mathnet.ru/eng/im2037), 1975. Bibliographic primary record; the attempted original PDF retrieval failed in this pass.
* Y. Lamzouri, S. Lester, M. Radziwill, [An effective universality theorem for the Riemann zeta-function](https://arxiv.org/abs/1611.10325v2), 2016, abstract and theorem setup: explicitly requires a nonvanishing approximation target. No strong-recurrence equivalence is used as a premise here.
