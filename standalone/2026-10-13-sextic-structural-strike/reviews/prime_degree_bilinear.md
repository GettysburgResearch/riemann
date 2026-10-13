# Independent review of the prime-degree and distinct-column manuscript

**Reviewer:** the bilinear-conductor subagent. I did not author the manuscript under review. This is a same-team adversarial mathematical reconstruction, not external acceptance, a proof-assistant certificate, or an independent proof of the named classical inputs.

**Final verdict:** no load-bearing defect found after the two scope corrections described below. The numbered finite inequality, signed prime-sector lower bound, deformation results, and prime-rooting identities are supported by the stated arguments. They do not refute the original composite-column Möbius moment or its complete singleton core.

## 1. Exact versions and correction history

The initial target was `pass3_native_attack.md`, SHA256

`f80d42fd162a207889b1e858c2b28660bb5fdfed9011d58991f373f4f709e0bf`.

The final reviewed target is the revised `pass3_native_attack.md`, 22,934 bytes, SHA256

`2290ce3d8d24f832259b3d701607beb125ceb5111f86b39d82be200eea1c27fb`.

The author retained the original as `pass3_native_attack_f80d42_original.md`. I read the full original and then checked the exact two-hunk revision, `pass3_native_scope_fix.diff`, SHA256

`3d2509e992c9a7d3fb9b1e76a7c9a71f2623518b7d66a73af78a24e5d971e09f`.

The review identified two prose claims needing correction:

1. Section 3 originally referred to a “connected tuple restriction,” although the proved selector is the removal of every repeated column. A connected incidence restriction could exclude the disjoint prime tuples entirely. The revision now states precisely that removing every repeated column does not eliminate the coherent spikes.
2. Section 6 allowed an arbitrary fixed twist `nu` but identified its `m = 1` piece with the untwisted polynomial (1.2). The revision restricts that exact identification to `nu = 1`, retains `nu(p)` in the general identity, and disclaims the same lower bound for arbitrary fixed twists.

Both corrections are present in the final hash. No numbered theorem, displayed formula, exponent, or proof of an estimate changed.

For the original source scope I reread the native covariance in PR #927's `SMALL_W_CORE_AUDIT.md` and the family statement in PR #913's `MOMENT_OBSTRUCTIONS.md`. The latter was also fetched directly through GitHub at commit `6498d6cc2eded03159c7332b25fd224ad07f89c1`, Git blob `a3bfa63cb6398d6b1ced163602f32a5fb052bf75`. Its fixed finite-order twist, fixed smooth test, original nonunit zeros, and all nonzero element rows agree with the distinctions made in the revised manuscript.

The classical analytic inputs are the fixed-field ideal count and prime ideal theorem, and the local simple pole of the Dedekind zeta function at one. The primary Burgin source cited in the manuscript was already opened in my separate resonance review. No moving-field prime theorem, moving-modulus prime theorem, RH assumption, or new zero-free half-plane is used here.

## 2. The finite signed inequality is valid globally

The ordered all-distinct Hermitian polynomial is real because exchanging its two groups of `k` slots conjugates each term and preserves its indexing set. It is not termwise nonnegative, and the proof correctly avoids assuming that it is.

The partition formula (2.6) is the exact inclusion-exclusion needed for all `2k` indices to be distinct. Fixing an assignment with equality partition `rho`, its coefficient is the sum of the displayed partition Möbius factors over partitions refining `rho`. This sum factors over equality blocks. On a block of size greater than one, it vanishes by the signed permutation-cycle identity; on a singleton it is one. Thus precisely the all-distinct assignments survive. This also verifies the signs and the factorial coefficients.

For every nonsingleton block, the bound

\[
|p_{r,s}|\le\sum_j|b_j|^{r+s}\le V
\]

uses only `r+s >= 2` and `|b_j| <= 1`. Singleton blocks give `B` or its conjugate. If a nontrivial partition has `j` nonsingleton blocks and `t` singleton blocks, then `2j+t <= 2k` and `t <= 2k-2`. With `U=1+V` and `y=|B|/sqrt(U)`, its unsigned contribution is at most `U^k y^t`.

For `0 < eta <= 1` and every such `t`,

\[
y^t\le\eta y^{2k}+\eta^{-(k-1)}
\]

follows by splitting at `y=1` and `y=eta^(-1/2)`. The sum of the absolute partition coefficients over all nontrivial partitions is `(2k)!-1`: partitions with cyclic order on each block are precisely permutations. Taking `eta=delta/((2k)!-1)` gives the displayed explicit constant

\[
C_{k,\delta}=((2k)!-1)^k\delta^{1-k}.
\]

This proves the absolute difference estimate and hence the real lower bound. The argument covers `k=1`, empty all-distinct sums, and vectors with zero coordinates. It makes no assumption on the number of coordinates relative to `2k`.

The weighted row corollary then follows by summation. Its negative allowance is bounded by

\[
C_{k,\delta}(1+V_0)^k\sum_u w(u)
\ll H(1+V_0)^k.
\]

This step is what turns a large positive moment on selected rows into a lower bound for the **complete signed** distinct-column sum. It controls the possible negative contribution from every other row, rather than silently discarding those rows.

## 3. The actual prime-sector lower bound has the claimed power range

The coefficients in the selected prime polynomial are the literal native values `mu_K(p)=-1`, multiplied by the prescribed nonnegative smooth profile. Thus `|b_p(u)| <= 1`, and the literal character zeros only reduce the variance. The uniform variance upper bound is the stated `V_D`.

For the fixed nonzero profile, the prime ideal theorem gives

\[
L_D\asymp D/\log D,
\qquad V_D\ll D/\log D.
\]

The exact value of the first asymptotic constant is not essential; its positivity follows from the nonnegative nonzero profile. The source's fixed finite excluded set does not affect the order of these counts.

Let `Y=H^(1/6)` and take a prime ideal `r` with `Y/2 < Nr <= Y`. The Eisenstein field is a principal ideal domain, so a generator supplies the element row `r^6`. Distinct prime ideals yield distinct rows: equality of their sixth powers would imply equality of their principal ideals. Multiplication of a generator by a unit does not change its sixth power. The row norm is `(Nr)^6 <= H`, so the stated sharp or majorant weight is at least one.

At this row the residue symbols are exactly one at every other column prime and exactly zero at the copying prime. Hence

\[
|P_{r^6}(D)|=L_D-W(Nr/D)\ge L_D-1.
\]

No coprimality assumption has replaced the zero, and no comparison between `Y` and `D` is needed. In particular the formula remains valid for the larger values of `h` allowed when `k` is large.

There are `gg H^(1/6)/log H` such rows. The ordinary prime moment is nonnegative, so their contribution yields

\[
\sum_{u\ne0}w_H(u)|P_u(D)|^{2k}
\gg \frac{D^{2k+h/6}}{(\log D)^{2k+1}}.
\]

Applying the weighted finite inequality with `delta=1/2` gives a lower bound for the entire signed prime sector, with possible negative error

\[
O\!\left(\frac{D^{k+h}}{(\log D)^k}\right).
\]

The difference between the two powers of `D` is `k-5h/6`. If `0<h<6k/5`, this positive power dominates the extra logarithms. The error is eventually smaller than a fixed fraction of the positive lower bound. The claimed lower bound therefore holds for every sufficiently large scale, rather than merely along a subsequence.

It exceeds `H D^(k+epsilon)` for every fixed `epsilon` strictly smaller than that power gap. There is no assertion of endpoint control at `h=6k/5`.

## 4. The prime selector is genuinely additional source information

Every tuple retained in the prime-sector theorem has `2k` different prime ideals. Consequently its columns are pairwise coprime and each occurring prime has signed multiplicity `+1` or `-1`. It is an actual all-singleton tuple with no repeated-column diagonal.

However, the theorem retains only prime ideal columns. The original fixed-profile Möbius polynomial also has squarefree composite columns. An estimate for its complete signed singleton sector is not required to survive deleting all those composites. The revised manuscript repeatedly makes this distinction and does not transfer its prime-selector lower bound to the native sum.

The statement that primality cannot be encoded by a permitted polynomially bounded exclusion also has a direct elementary justification. Choose a fixed interval on which the profile is positive. For large `D`, choose two fixed proportional intervals of prime norms near `sqrt(D)` whose pairwise products lie in that positive interval times `D`. The prime ideal theorem supplies arbitrarily many primes in each interval. An exclusion ideal of norm at most `D^C` can contain only `O_C(1)` of those prime factors. Distinct unexcluded primes can therefore be chosen from the intervals, leaving an unexcluded squarefree composite column in the profile. Thus such exclusions cannot implement the exact prime selector. A finite-order twist is nonzero on its good ideals and cannot supply this deletion either.

A fixed smooth profile also cannot itself decide primality across all scales: positive values of its argument occur for both prime and composite ideal norms after rescaling. The distinction is an arithmetic column selection, not a permissible relabeling of the original fixed data.

The result correctly rules out methods that would prove a diagonal-size bound for every such selected sector and then sum their absolute bounds. It does not prove that every conceivable decomposition by prime degree fails; a successful decomposition could retain the necessary signed coupling between degrees.

## 5. The deformation proof requires only a local analytic obstruction

For `|z+1|<1/2`, the factorization in the absolute half-plane is valid. The correction product cancels the linear prime terms and has normally convergent logarithms near one after finitely many primes are separated. Its factors at one are nonzero because `|z|<3/2` and every prime norm is at least two. The omitted finite-prime factors are also nonzero there.

The local simple pole of `zeta_K` therefore gives

\[
F_z(s)=(s-1)^{-z}U_z(s),\qquad U_z(1)\ne0,
\]

on a slit neighborhood. Within the stated disk, `z=-1` is the only value for which `-z` is a nonnegative integer. If a nonzero holomorphic extension existed for another `z`, its integer zero order at one would equal

\[
\lim_{s\downarrow1}(s-1)F_z'(s)/F_z(s)=-z,
\]

which is impossible. The local argument makes no assertion that a fractional power of the zeta function is single-valued across a larger zero-containing domain.

Suppose that the smoothed scalar sum were `O(D^(1-eta))` for some positive `eta`. Its Mellin integral is holomorphic in `Re s>1-eta`: there is no lower-end convergence issue because the compactly supported norm profile makes the sum vanish below a fixed positive scale. In `Re s>1`, absolute convergence permits termwise integration, producing `W_hat(s)F_z(s)`. The factor `W_hat(1)` is positive and is nonzero in a neighborhood. Dividing by it would give the impossible holomorphic extension. Proposition 4.1 follows.

The tangent coefficient is also computed correctly. Differentiation in `z` at `-1` produces `-mu_K(n) omega_K(n)`. Its Dirichlet series has the product of the simple zero of `F_-1` and a prime sum equal to `log zeta_K(s)` plus an analytic remainder. The resulting nonzero `(s-1) log(s-1)` term is nonremovable. The sign of the tangent coefficient does not affect the obstruction. Weighting by `log Nn` instead differentiates in `s`, so the stated local distinction is valid.

## 6. The deformation survives arithmetic row averaging in the stated limsup sense

The coefficient bound `|a_z(n)| <<_(z,epsilon) (Nn)^epsilon` is the standard fixed-base divisor bound and is uniform in the moving copying prime. Deleting its multiples changes the scalar sum by at most

\[
O\!\left(D^\epsilon(D/Nr+1)\right).
\]

This follows by writing `n=rm` and applying ideal counting after taking absolute values. When `Nr>bD`, the difference is exactly zero. With `Nr` in `[D^(h/6)/2,D^(h/6)]`, the displayed deletion loss has the two powers stated in (4.8).

Failure of every scalar power-saving bound gives arbitrarily large scales with `|A_z(D)|>D^(1-eta)`. Choose `eta` and `epsilon` so that both `eta+epsilon<h/6` and `eta+epsilon<1`. The deletion loss is then negligible compared with that large value, uniformly over all copying primes. Their number gives the lower moment along those scales, and taking a limsup followed by arbitrarily small `eta` proves (4.7).

The distinction between all sufficiently large scales in Theorem 3.1 and a limsup in Proposition 4.2 is correctly maintained. For the deformation no unproved asymptotic formula for the scalar sum is assumed.

These deformed coefficients are not silently identified with the original Möbius family. For arbitrary `z` in the disk they are divisor bounded; on the unit-circle portion they are bounded in modulus by one. Arbitrarily small unit-circle rotations away from `-1` already suffice for the claimed failure of a coefficient-insensitive arithmetic comparison. No lower bound for the undeformed value `z=-1` follows from this reasoning.

## 7. The independent-residue comparison and the source-preserving identity

The independent sixth-root model keeps a tuple only if every prime's signed multiplicity is divisible by six. Every occurring prime must then occur at least twice, including the order-six aliases at larger `k`. The physical product budget bounds the radical norm by `O(D^k)`, and the fixed incidence assignment count gives `O(D^(k+epsilon))` surviving tuples. Taking absolute coefficient values is legitimate after this exact expectation. When `k<6`, the signed multiplicity range forces exact balance at each prime, so arbitrary primewise phase rotations leave the moment unchanged. At `k>=6`, the value can change but the same counting upper bound still holds. These statements agree with the manuscript's scope.

The prime-rooting identity is also exact. Every supported nonunit squarefree ideal `n` appears once for every prime `p` dividing it, with `m=n/p`. The condition `(m,p)=1` is required and is present. The coefficient is the original `mu_K(n) xi_u(n)`, including zero cases, and its total weight is

\[
\sum_{p\mid n}\frac{\log Np}{\log Nn}=1.
\]

The support excludes the unit ideal and keeps the logarithmic denominator positive. All sums are finite. Multiplying the identity by `conjugate(A_u)|A_u|^(2k-2)` gives the stated nonlinear pairing after summing the permitted nonnegative row weights. This is an algebraic identity for the actual native test, not a new arbitrary-test norm estimate.

The final prose now correctly identifies the untwisted `m=1` contribution with (1.2) only when `nu=1`. The remaining terms retain its composite completion. Estimating this signed pairing at diagonal size is expressly left open.

## 8. Review conclusion and validation boundary

The significant new obstruction is a lower bound for a **complete signed all-distinct prime-column contribution**, with the original coefficient on every retained column. The finite partition inequality controls all other rows' possible negative contribution, so this is stronger than observing a positive spike on a selected row. The additional column selector is nevertheless essential, and the revised manuscript preserves that boundary.

The deformation establishes a separate instability of a larger coefficient class using only local behavior near the zeta pole. The prime-rooting identity retains the missing composite terms but does not yet estimate their cancellation.

I reconstructed these arguments symbolically, checked the source quantifiers, and verified the exact corrective diff. I did not rerun the author's finite diagnostic or treat its output as a proof of the asymptotic theorems. The classical prime ideal theorem and ideal-counting inputs remain named inputs. No remaining mandatory correction was identified in final hash `2290ce3d8d24f832259b3d701607beb125ceb5111f86b39d82be200eea1c27fb`.
