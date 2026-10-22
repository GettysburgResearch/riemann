# Shake-up pass — global audit, external proof firewall, and dyadic principal-mode pivot

Author: `gpt56-sol`  
Date: 2026-08-08  
Status: **NEW EXACT RESULTS + RESEARCH PIVOT; RH UNPROVED**

## Executive conclusion

This pass deliberately stepped outside the current family of scalar RH-equivalent hinges.  It audited the newest live repository, searched current 2026 literature for a genuine external closure, stress-tested the prime-radix and eta contraction architectures, and re-entered the exact dyadic two-contact source at the physical/carry interface.

The pass does **not** produce an unconditional proof of RH.

It does produce three durable changes to the proof graph:

1. the 2026 preprint claiming `Lambda_dBN=0` is not an external completion: its large-order proof uses a nearest-zero geometric asymptotic for Taylor coefficients of an entire function and later a global real-zero ordering that is circular beyond the verified range;
2. the five-adic residue programme can close its entire current-scale outer four-fifths with **absolute bounded Cycle Debt**, but a source-free five-state contraction is spectrally overstrong because of nonprincipal mod-five characters;
3. on the exact dyadic two-contact system, the balanced physical-to-Selberg reserve loses **no logarithmic power**: an elementary Chebyshev bound upgrades the previous polylogarithmic source transference to one scale-independent constant.

The resulting preferred target is no longer a generic carry contraction.  It is one source-coupled **principal-mode Schur descent** for the dyadic inverse-zeta source.

## 1. Live repository frontier

The newest live graph through PR #323 contains several exact but overlapping endgames:

```text
WSTS <=> RH                         canonical finite weighted shell scalar;
Cycle Debt / dyadic commutator      exact half-scale flow plus paired odd excess;
eta/central cascade                 analytic contraction + finite boundary injections;
five-adic source renewal            exact scaled critical mode + four residue modes;
two-contact Selberg/carry           exact pole-sensitive physical field + positive reserve;
Brownian/aggregate                  independent variance/equality-case programme.
```

The common scope firewalls are now extremely clear:

```text
source-blind contraction            impossible on zeta-zero modes;
source-free prime radix p>2         introduces nonprincipal Dirichlet-L modes;
generic Green norm                  retains the exact prime-ramp scalar;
finite endpoint/rank counting       cannot control coherent Mobius cubes;
absolute positive-part transport    pays a macroscopic square-root cost.
```

A viable proof must preserve the RH-sensitive source all the way through the step that creates strict lower-scale descent.

## 2. External literature audit

### 2.1 Gershon 2026 de Bruijn--Newman claim

The preprint *The De Bruijn-Newman Constant Is Zero* would settle RH if its claimed upper bound `Lambda_dBN<=0` were correct, since Rodgers--Tao prove the opposite inequality.

The manuscript's current all-order closure is not accepted for two independent reasons recorded in

```text
literature/2026-gershon-debruijn-newman-proof-audit.md
```

The first is source-typing: for

\[
g(z)=\sum\gamma_mz^m=\Xi(\sqrt z)
\]

entire, the paper assigns a nearest-zero geometric asymptotic to `gamma_m`.  Cauchy--Hadamard forces

\[
\limsup|\gamma_m|^{1/m}=0,
\]

so a nonzero `rho_1^m` leading term is impossible.  Such a pole expansion belongs to the reciprocal coefficients of `1/g`, not to the Taylor coefficients of `g`.

The second is circularity: the later reciprocal Binet--Cauchy tail orders all required zeros as real negative values `-t_n^2` for arbitrary `n`.  Outside the finite verified-zero range this is precisely the real-zero geometry under dispute.

This does not refute the paper's finite calculations or complementary-minor identity.  It blocks the claimed cofinal closure.

### 2.2 Connes 2026 finite Euler approximants

Connes proves remarkable finite approximants whose zeros lie on the critical line and presents convergence of finite zeros to the zeta zeros as a possible proof strategy.  The convergence is not currently a theorem.  The repository's prolate/CCM branch likewise still has an off-line Xi-cardinal obstruction in the required ground-state interface.  No hidden composition presently supplies the missing convergence theorem.

## 3. New exact theorem on PR #322: bounded outer five-adic debt

The exact five-adic block coefficient is

\[
c_{a,j}=U_X(5a+j)-U_X(5a+5).
\]

For `X=5Y` and `Y<x<=X`, only `mu(1),...,mu(4)` enter the source formula.  The explicit cell expression gives

\[
|U_X'(x)|\le7x^{-3/2}.
\]

Hence, throughout the outer four-fifths,

\[
|c_{a,j}|\le28(5a+j)^{-3/2}.
\]

The legal adjacent-tree commutator with divergence `e_(m+1)-e_m-e_1` has capacity norm

\[
\|E_m\|_\omega\le24\sqrt{m+1}.
\]

Therefore the complete outer residue family has the explicit flow

\[
\mathcal F_X^{out}=\sum c_{a,j}E_{5a+j-1}
\]

and

\[
\boxed{
\mathcal N_\omega(\mathcal F_X^{out})<1344
}
\]

uniformly in `X`.

This is pushed directly to PR #322 as

```text
L-30105-five-adic-outer-residue-commutator-has-bounded-debt.md
```

The result removes every current-scale nonmultiple residue above `X/5`.  It does not close the inner residue automaton.

PR #323 independently shows why a source-free five-state contraction would be the wrong next theorem: the nonzero mod-five residue modes contain nonprincipal Dirichlet-L channels.

## 4. Radix-two principal-mode pivot

Radix two has no nonprincipal character.  The exact zero-safe opposite-parity source is

\[
\omega_2(n)
=\mu(n)-{3\over2}{\bf1}_{2\mid n}\mu(n/2)
 +{1\over2}{\bf1}_{4\mid n}\mu(n/4),
\]

with transform

\[
{(1-2^{-s})(1-2^{-s-1})\over\zeta(s)}.
\]

The same source already has:

```text
compact factor-four carry dipole;
positive inverse coefficients;
positive generalized-prime weights;
finite binary digital forcing;
exact annular physical-to-carry isometry;
strict generalized-prime carry reserve;
strict half-scale source-change identity;
positive half-scale generalized-Selberg defect.
```

The synthesis is recorded in

```text
O-32401-dyadic-principal-mode-is-the-unique-prime-radix-source-without-extra-l-functions.md
```

The remaining proposed theorem is `PMSD`: combine the source-change and Selberg-defect lower families in one Schur elimination, without charging either separately by absolute convolution.

## 5. New exact theorem: no logarithmic transference loss in the balanced interior

For the simpler exact two-contact system

\[
A_2={\zeta\over1-2^{-s}},
\qquad
B_2=A_2^{-1},
\]

let `Q_2(n,j)` be the RH-sensitive inverse-source carry field, `P_2(n,j)` the nonnegative generalized-prime Kummer field, and

\[
R_2=P_2^2-S_2
\]

the explicit source-matched Selberg reserve.

PR #302 had proved

\[
|Q_2|^2\le C_\eta\log^2n\,R_2
\]

on a fixed balanced interior cone.  The logarithmic loss came only from the crude bound `Psi_2(x)<<x log x`.

The elementary central-binomial estimate gives

\[
\psi(2m)-\psi(m)\le2m\log2.
\]

Dyadic summation yields

\[
\psi(x)\le4x\log2,
\]

and therefore the generalized Chebyshev function satisfies the convenient global bound

\[
\Psi_2(x)\le4x.
\]

The exact Jensen formula then gives

\[
|Q_2(n,j)|\le8n.
\]

On a fixed balanced cone,

\[
P_2(n,j)\ge\eta n\log2
\]

and for all sufficiently large `n`

\[
R_2(n,j)\ge{1\over2}P_2(n,j)^2.
\]

Consequently

\[
\boxed{
|Q_2(n,j)|^2\le C_\eta R_2(n,j)
}
\]

with one constant independent of `n`; finitely many small interior rows are absorbed into the constant because their reserve is strictly positive.

This is pushed as

```text
L-32402-absolute-balanced-two-contact-physical-to-selberg-reserve.md
```

The endpoint-neighbor rows remain explicitly separate and are already absorbed by nearest interior reserve rows on PR #302.  Hence no growing physical/carry condition number survives at current scale.

## 6. What this changes

The prior proof graph could plausibly blame the failure to close the dyadic route on an ever-growing physical-to-carry transference constant.  That explanation is now removed.

The surviving arithmetic mechanism is narrower:

```text
current RH-sensitive principal block
+ proper-divisor source-change family
+ proper-divisor Selberg-defect family
+ finite endpoint/bottom charge
-> one source-coupled Schur elimination
-> half-scale recurrence.
```

The lower families share the same positive inverse coefficients and the same divisor descent.  They must be combined before absolute values are taken.

## 7. New production target — PMSD

The source-coupled Principal-Mode Schur Descent certificate should prove

\[
E_W(M)
\le C(1+\log M)^A
 +\sum_\beta\theta_\beta E_W(M_\beta),
\]

with

\[
M_\beta\le M/2,
\qquad
\sum_\beta\theta_\beta\le1.
\]

The certificate must expose:

```text
current inverse-zeta source W;
positive generalized-prime source;
all proper-divisor source-change rows;
all proper-divisor Selberg-defect rows;
independent-frequency reflected cross terms;
current Selberg reserve;
endpoint-neighbor absorption;
finite bottom rows;
all exact half-scale destinations.
```

A proof may not estimate the positive inverse coefficients absolutely: their critical mass is exactly where the inverse-zeta obstruction lives.

## 8. Stress tests performed during this pass

Several tempting closures were explicitly rejected during the work:

- pure central fragmentation looked positive in a scratch implementation but the correct recurrence has finite negative mutations; no such claim is retained;
- generic floor-atomic classification of Cycle-Debt duals is false already in finite balanced cones;
- a source-free five-adic contraction is spectrally overstrong;
- the 2026 claimed `Lambda_dBN=0` proof does not survive the all-order source audit;
- current-scale physical reserve alone is not a lower-scale recurrence.

## 9. Exact status

```text
external claimed RH proof imported                 NO
five-adic outer current-scale residue               CLOSED with O(1) debt
five-adic inner/source-character recurrence         OPEN
radix-two spectral scope                            EXACTLY PREFERRED
balanced two-contact physical transference          CLOSED with absolute constant
endpoint two-contact absorption                     IMPORTED CLOSED
principal-mode source-change half-scale identity    IMPORTED CLOSED EXACTLY
positive Selberg-defect half-scale identity          IMPORTED CLOSED EXACTLY
PMSD source-coupled Schur descent                    OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVED
```

## 10. Recommendation

The next serious proof pass should not return to WSTS, AWTO, Greedy Slack, generic eta contraction, or source-free radix-five renewal as the primary theorem.

Construct the explicit finite block matrix for one annular dyadic `PMSD` step, with the current `W` coordinate and the complete proper-divisor source/defect bank, and compute its Schur complement symbolically.  The current-scale geometry is now sufficiently closed that a failure will be visible as one concrete lower-block charge rather than another abstract equivalence.
