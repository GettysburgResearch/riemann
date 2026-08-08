# T-32401 — Critical-neutral capped-boundary route toward RH

Claim ID: `T-32401`  
Title: Contract the affine-log transverse core, carry the zeta-neutral mode at coefficient one, and reduce RH to one capped-boundary scale recurrence  
Status: **FULL CONDITIONAL GLOBAL PROPOSAL — ONE SOURCE-SPECIFIC COEFFICIENT-ONE CAP RECURRENCE OPEN**  
Authoring agent: `gpt56-pro-09-s`  
Created: 2026-08-08  
Dependencies: `L-32401`, `L-32402`; PR #316 `L-30901/L-30902/T-30901`; PR #323 zero-mode firewall; PR #272 Cycle-Debt consumer  
Scope: corrected global architecture after the strict-contraction and terminal-atomic refutations; RH is not claimed proved

## 1. Why the previous closing targets were too strong

The live repository has now proved two complementary facts.

First, source-blind strict contraction of the complete critical eta state is impossible: at every zeta zero the critical eta multiplier is exactly one.

Second, strict contraction is unnecessary. A coefficient-one recurrence with a fixed dyadic scale drop already gives polynomial energy and hence the subexponential pole bound required for RH.

The proof target should therefore be critical, not subcritical:

```text
principal dyadic mode        carried losslessly;
transverse analytic bank     strictly contracted;
fresh cutoff boundary        paid by explicit polylog debt;
propagated cap channel       nonexpansive under scale descent.
```

## 2. Exact decomposition of every fresh boundary

At every analytic depth, the fresh boundary has the form

\[
 h_{a,X,s}(x)
 =x^{-s}\log\!\left(\min\{2^a(x-1)+1,X\}\right).
\]

`L-32401` proves exactly

\[
\boxed{
 h_{a,X,s}=u_{a,s}-c_{a,X,s},
}
\tag{T-32401.1}

where

\[
 u_{a,s}(x)
 =x^{-s}\log(2^a(x-1)+1)
\]

has the uniformly summable inverse-power expansion

\[
\begin{aligned}
 u_{a,s}(x)
 ={}&a\log2\,x^{-s}+x^{-s}\log x\\
 &-\sum_{\ell\ge1}
 {\left(1-2^{-a}\right)^\ell\over\ell}
 x^{-s-\ell},
\end{aligned}
\]

and the power-tail coefficient norm at radius `1/4` is at most `log(4/3)`.

Thus `u_(a,s)` belongs to PR #286's existing `6/7` Dirichlet–Taylor contraction bank. Only

\[
\boxed{
 c_{a,X,s}(x)
 =x^{-s}
 \log{2^a(x-1)+1\over X}
 \mathbf1_{x\ge1+(X-1)/2^a}
}
\tag{T-32401.2}

remains in the critical boundary state.

## 3. Fresh cap injection is already controlled

PR #316 `L-30902` proves that the complete fresh boundary at every depth has native weighted first-difference debt

\[
 O((1+\log X)^2)
\]

at the critical exponent and `O(1+log X)` for faster powers, uniformly in depth.

Since the uncapped core is now separately assigned to the strictly contracting analytic bank, this theorem is more than enough for every **new** cap injected by finite support. The only remaining issue is subsequent propagation and recombination of already-created cap states.

## 4. Sole theorem — Critical-Neutral Cap Recurrence (`CNCR`)

Let `D_cap(J)` be the cycle-optimized native weighted first-difference debt of the complete cap state at logarithmic endpoint scale `J`, after:

1. all cap terms with the same current destination are recombined;
2. every uncapped affine-log component is removed through `L-32401` and sent to the `6/7` analytic bank;
3. all Pascal-cycle corrections are applied before a negative part or norm;
4. every current-scale cutoff crossing and endpoint atom is retained.

The proposed **Critical-Neutral Cap Recurrence** is

\[
\boxed{
 D_{\rm cap}(J)
 \le C(1+J)^A
 +D_{\rm cap}(J-\log2+O(J^{-1})).
}
\tag{CNCR}

A cleaner sufficient finite-endpoint form is

\[
\boxed{
 D_{\rm cap}(2Y)
 \le D_{\rm cap}(Y)+C\log^A(2Y).
}
\tag{T-32401.3}

The coefficient is deliberately **one**. A strict coefficient below one is neither required nor compatible with the complete critical zero mode.

A production proof must bind the `O(J^-1)` endpoint perturbation or use the exact integer half-scale map; it may not conceal it in asymptotic notation.

## 5. Conditional completion

Assume `CNCR`. Iterating over at most `O(log X)` dyadic scales gives

\[
\boxed{
D_{\rm cap}(X)=O(\log^{A+1}X).
}
\tag{T-32401.4}

The complete analytic core contributes a convergent geometric series by the `6/7` reserve. Every fresh boundary contributes only a polynomial logarithmic injection by PR #316. Therefore the exact balanced cascade has polylogarithmic Cycle Debt.

PR #272 then yields the sharp complete prime-power ramp

\[
\sum_{p^k\le X}
{\Lambda(p^k)\over\sqrt{p^k}}
\log{X\over p^k}
=4\sqrt X+X^{o(1)}.
\tag{T-32401.5}

The reviewed square-screw/Landau consumer excludes every zeta zero with real part greater than one half. Functional-equation symmetry gives RH.

Equivalently, the atomized Nyman/carry route of PR #297 obtains polynomial local energy and its vector-valued pole criterion gives the same conclusion.

Thus

\[
\boxed{
\mathrm{CNCR}\Longrightarrow\mathrm{RH}.
}
\tag{T-32401.6}

## 6. Spectral sharpness

At a zeta zero `rho`, `L-32402` gives

\[
\beta*e^{(\rho-1/2)t}=e^{(\rho-1/2)t}.
\]

Under endpoint doubling, the same mode is multiplied by

\[
2^{\rho-1/2}.
\]

Therefore

```text
Re rho = 1/2     critical scale factor = 1;
Re rho > 1/2     scale factor > 1.
```

`CNCR` is therefore tuned to the exact spectral threshold. It permits the known critical-line modes without damping them and forbids the exponential scale growth which an off-line zero would force.

This is why the proposal does not seek another source-blind contraction theorem.

## 7. Relation to the current repository alternatives

### PR #316 / CBVR

`CNCR` is a strict reduction of the state space proposed by `CBVR`: `L-32401` removes the entire uncapped affine-log bank from the unknown recurrence.

### PR #323

The zero-mode firewall becomes a design principle rather than a no-go: preserve the principal mode with coefficient one.

### PR #297 / CISR

The atomized Hermitian matrix remains an independent consumer. A `CNCR` certificate gives the required polynomial local energy without requiring a diagonal-to-source Selberg lift.

### PR #321 transition cone

Cycle/collector/parity moves remain permitted inside the cap-state optimization; their role is to make the coefficient-one inequality source complete, not to produce an artificial strict contraction.

## 8. Mandatory rejection tests

Reject a claimed `CNCR` proof if it:

```text
uses a strict source-blind eta contraction on the complete zeta mode;
uses the refuted terminal atomic source norm;
propagates the uncapped affine-log core as an unknown boundary state;
drops a cutoff cap or endpoint crossing;
takes absolute values before same-destination cap recombination;
drops Pascal-cycle freedom;
produces a coefficient larger than one at the dyadic scale;
uses a five-adic residue contraction without the nonprincipal character modes;
fails the 2/3 Mertens or bottom-charge mutation;
promotes finite numerical behavior to CNCR.
```

## 9. Exact status

```text
all-depth affine-log core factorization       PROPOSED COMPLETE
uniform analytic-core coefficient budget      PROPOSED COMPLETE
6/7 contraction of uncapped core              IMPORTED / PROPOSED COMPLETE
critical eta zero-mode neutrality             PROPOSED COMPLETE
coefficient-one scale threshold               PROPOSED COMPLETE
fresh boundary polylog debt                    IMPORTED / PROPOSED COMPLETE
CNCR propagated cap recurrence                 OPEN / RH-BEARING
CNCR -> Cycle Debt / atomized energy -> RH     COMPLETE CONDITIONAL
Riemann Hypothesis                             UNPROVED
```

This is a full-problem proposal at the correct critical scale. It is not represented as an unconditional proof until `CNCR` is constructed.
