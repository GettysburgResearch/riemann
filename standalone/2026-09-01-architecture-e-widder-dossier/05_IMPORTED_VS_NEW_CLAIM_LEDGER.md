# Imported versus new claim ledger

Status: **LOCAL REVIEW LEDGER ONLY.  THESE ARE NOT CANONICAL REPOSITORY CLAIM IDS.**

This ledger is intended to make dependency and novelty review mechanical.  `IMPORTED` means the dossier relies on a result already present at a frozen source head without upgrading its status.  `PROPOSED_NEW` means a proof is supplied in this packet or its immediate predecessor work and requires independent review.  `OPEN_EQUIVALENT` means the statement is explicitly RH-equivalent and remains unproved.  `FIREWALL` means a counterexample or logical obstruction is supplied or imported.

## 1. Source results

| Local label | Statement | Status | Exact provenance | Notes |
|---|---|---|---|---|
| `EW-I-001` | Raw Xi companion Schur/inner behavior for one fixed `lambda>0` is RH-equivalent after removable cancellation. | `IMPORTED` | PR #765 `8f01064df805624c045877655893c324a220975d` | Endpoint criterion, not a sign mechanism. |
| `EW-I-002` | Fixed-calibration companion and finite joint-polynomial transport certificates hold at the declared panels. | `IMPORTED` | PR #765 same head | Finite only; eighteen reviewed transport points remain unresolved. |
| `EW-I-003` | Actual-Xi odd-current, double-scaling, saddle and radial-semigroup asymptotics hold in their declared regimes. | `IMPORTED` | PR #765 same head | Local/universal asymptotics do not imply RH. |
| `EW-F-001` | Positive smooth kernels with the exact Xi tail and the local asymptotics can still have nonreal zeros. | `FIREWALL` | PR #765 same head | Blocks generic positive-kernel descent. |
| `EW-I-004` | The minimum-energy positive source quotient is `(pi H^{-1} pi^*)^{-1}` with the stated coherence properties. | `IMPORTED` | PR #766 `17c7624a0bd56c5356d00278b2a846d2efdbdccc` | Source quotient, not scalar averaging. |
| `EW-F-002` | Proper native level-one positive theta-source quotients have reflected real off-central zeros for every `j>=1`, even `k>=96j`. | `FIREWALL` | PR #766 same head | Refutes positive-source-only Architecture A. |
| `EW-I-005` | The ternary coefficient cube has the explicit self-dual Chow-base minimal resolution and actual top relation. | `IMPORTED` | PR #769 `f36576faf7853a56bd1f64edd29c4df662cae849` | Supplies duality and an alternating Tor character. |
| `EW-F-003` | Euler/Tor trace cancellation need not imply vanishing of the underlying resolution or a polarization. | `FIREWALL` | PR #769 and related #781 packets | Blocks purity from Euler characteristic alone. |
| `EW-I-006` | Native source quotienting, principal recombination and ratio-mask gauge inversion can incur factorial or power losses. | `IMPORTED` | PR #770 `9421846721cd788ab01615c8b6d459d9de849df7` | Source metric must be retained. |
| `EW-I-007` | The selected twenty-row physical minor has singular infinite-horizon limit; separate full-support rows give finite source faithfulness. | `IMPORTED` | PR #770 same head | Finite nonsingularity is not stable cofinal inversion. |
| `EW-I-008` | Segre defect self-duality and deformation-spectrum reciprocity are exact; purity is a separate temperedness inequality. | `IMPORTED` | PR #781 `ea282c4e73ecd2d8cad44587da5ffa135df67e98` | Functional equation versus purity separation. |
| `EW-F-004` | Arithmetic Epstein/theta objects can have certified off-critical real and complex zeros. | `FIREWALL` | PR #781 same head | Refutes generic arithmetic wall protection. |
| `EW-I-009` | Low-order safe-line Hausdorff/Pick/Stieltjes transforms and finite Xi Pick results survive with their integrated fixes. | `IMPORTED` | `main@6dda8b5125457ed936330229f8c9eb6491728e76` | Complete all-order sign remains RH-equivalent. |

## 2. Review deductions

| Local label | Statement | Status | Proof/source | Notes |
|---|---|---|---|---|
| `EW-R-001` | Architecture A is false in scalar positive-source form and survives only as two-variable polarized positivity. | `PROPOSED_NEW` | `01_FROZEN_SOURCE_REVIEW.md` | Direct consequence of `EW-F-002`. |
| `EW-R-002` | Architecture B is the strongest exact endpoint, provided its index counts distinct zero locations. | `PROPOSED_NEW` | review plus `EW-N-002` below | Multiplicity caveat is load-bearing. |
| `EW-R-003` | Architecture C lacks a protected arithmetic invariant in the reviewed data. | `PROPOSED_NEW` | `01_FROZEN_SOURCE_REVIEW.md` | Epstein firewall. |
| `EW-R-004` | Architecture D supplies duality but lacks a polarized realization and purity theorem. | `PROPOSED_NEW` | review of #769/#781 | Near-term algebraic programme, long route to RH. |
| `EW-R-005` | Architecture E is the shortest coherent synthesis of the reviewed source and endpoint structures. | `PROPOSED_NEW` | `01_FROZEN_SOURCE_REVIEW.md` | Strategic assessment, not a theorem of external priority. |

## 3. Source–Hermite–Stieltjes theorems

| Local label | Statement | Status | Proof/source | Review sensitivity |
|---|---|---|---|---|
| `EW-N-001` | The generalized-Schur kernel of `Theta_lambda` is a positive diagonal congruence of the Xi Hermite–Bezout kernel. | `PROPOSED_NEW` | `02_SOURCE_HERMITE_STIELTJES_CLOSURE.md`, Section 2; predecessor PR #784 | Check normalization and removable cancellations. |
| `EW-N-002` | `sq_-(B_X)` equals the number of distinct upper-half-plane Xi zero locations. | `PROPOSED_NEW` | same, Section 3; related PR #783 | Check feature independence and infinite exhaustion. |
| `EW-N-003` | The explicit source kernel `A_Phi` has double Fourier transform `B_X`. | `PROPOSED_NEW` | same, Sections 4–5 | Check factor, transport equation and boundary terms. |
| `EW-N-004` | `A_Phi=4K_0` for the current zero-frequency Weyl kernel. | `PROPOSED_NEW` | same, Section 6; predecessor PR #784 | Factor-four normalization. |
| `EW-N-005` | The safe Euler-axis Pick kernel is the imaginary-axis restriction of `B_X`. | `PROPOSED_NEW` | same, Section 7 | Functional-equation derivative signs. |
| `EW-N-006` | RH is equivalent to `p(t)=F(sqrt(t))/sqrt(t)` being Stieltjes. | `PROPOSED_NEW` | same, Section 8 | Check converse analytic continuation. |
| `EW-N-007` | A positive Stieltjes measure gives the exact two-channel Gram factorization of the safe Pick kernel. | `PROPOSED_NEW` | same, Section 9 | Elementary algebra. |
| `EW-N-008` | `H[x]=L_{tp}[t]-D_xL_p[t]D_x`. | `PROPOSED_NEW` | same, Section 10; predecessor PR #784 | Check diagonal convention. |
| `EW-N-009` | RH is equivalent to accretivity of the explicit gamma-plus-prime-shift operator on all finite exponential polynomials. | `PROPOSED_NEW` | same, Section 11 | Relies on all-order safe Pick equivalence. |
| `EW-N-010` | On the positive quadrant, `A_Phi={H_Phi,{M,H_Phi}}`. | `PROPOSED_NEW` | same, Section 12 | Anticommutator, not square. |

## 4. E–Widder endpoint

| Local label | Statement | Status | Proof/source | Review sensitivity |
|---|---|---|---|---|
| `EW-W-001` | There is a unique entire `mathfrak X` with `mathfrak X(s(s-1))=xi_R(s)`, of order at most `1/2`. | `PROPOSED_NEW` | `03_E_WIDDER_SCALAR_ENDPOINT.md`, Section 1 | Even-entire descent and order conversion. |
| `EW-W-002` | `q(u)=2 mathfrak X'(u)/mathfrak X(u)` is positive for every `u>0`. | `PROPOSED_NEW` | same, Sections 1–2 | Uses positivity of the actual theta kernel. |
| `EW-W-003` | RH implies `q(u)=2 sum m_gamma/(u+gamma^2+1/4)`. | `PROPOSED_NEW` | same, Section 4 | Genus-zero product and multiplicities. |
| `EW-W-004` | RH is equivalent to `(-1)^{k-1}D^{2k-1}[u^kq(u)]>=0` for every `u>0,k>=1`. | `PROPOSED_NEW` using `CLASSICAL IMPORT` | same, Sections 3–6; Widder/Sokal theorem | Central theorem of this dossier. |
| `EW-W-005` | The Widder functional equals an explicit archimedean reserve minus an absolutely convergent von Mangoldt sum at `s>1`. | `PROPOSED_NEW` | same, Sections 7–8 | Check `2/u` cancellation and differentiated convergence. |
| `EW-W-006` | False RH produces a finite strict certificate at integer `k`, rational `u`, and finite directed prime cutoff. | `PROPOSED_NEW` | same, Section 11 | Requires strict continuity and tail enclosure. |
| `EW-W-OPEN` | The E–Widder source inequality `(EW)` holds for all `u>0,k>=1`. | `OPEN_EQUIVALENT` | `03_E_WIDDER_SCALAR_ENDPOINT.md`, Section 9 | Proving this proves RH. |

## 5. Firewalls proved or imported in the successor work

| Local label | Statement | Status | Proof/source | Consequence |
|---|---|---|---|---|
| `EW-F-005` | `||K||<=1` and `CE=I` do not imply `||CKE||<=1` under non-isometric compression. | `FIREWALL` | `04_FIREWALLS_AND_SCOPE.md`, Section 5 | Volterra scalar contraction is insufficient. |
| `EW-F-006` | Positive sums of `PF_infinity` kernels need not be `PF_infinity`. | `FIREWALL` | same, Section 6; predecessor PR #784 | Termwise theta total positivity cannot be summed. |
| `EW-F-007` | Pointwise Wigner positivity is not a viable target for the non-Gaussian Riemann kernel. | `FIREWALL` | same, Section 4; Hudson theorem | Positivity must be nonlocal. |
| `EW-F-008` | Fixed finite Pick/Loewner order does not imply the all-order Stieltjes hierarchy. | `FIREWALL` | same, Section 11 | New all-order recurrence required. |
| `EW-F-009` | Direct absolute Euler generating sums stop at the boundary before the RH-detecting annulus. | `FIREWALL` | same, Section 12; imported safe-line square-root transform | E–Widder avoids the annulus but not the sign. |
| `EW-F-010` | Replacing `L_k` by absolute values erases the load-bearing signed interference. | `FIREWALL` | same, Section 13 | Preserve the signed source before estimates. |

## 6. Classical imports

The following are used as named classical inputs, not claimed new:

1. the Riemann xi functional equation and its positive theta Fourier representation;
2. standard zero-counting sufficient for genus-zero convergence in the invariant coordinate;
3. canonical-product logarithmic derivative identities;
4. the Hermite–Biehler/de Branges and generalized-Schur kernel framework;
5. the Bernstein–Hausdorff–Widder theorem;
6. Widder's 1938 characterization of Stieltjes functions, in the reduced form `F_{k-1,k}>=0`;
7. the cut-plane analytic characterization of Stieltjes functions;
8. the Euler formula for `xi'/xi` on `Re(s)>1`;
9. Hudson's theorem for pure-state Wigner positivity;
10. standard operator-monotone/Stieltjes and complete-Bernstein correspondences where invoked.

Every final proof should pin exact editions/theorem numbers before external publication.

## 7. Explicit nonclaims

This ledger does not claim:

- an unconditional proof of `(EW)`;
- RH or GRH;
- an external novelty or priority determination;
- that predecessor proposed claims have passed canonical integration review;
- a new zero-free region;
- a certified off-line zero of the Riemann zeta function;
- that finite symbolic checks prove any continuum positivity theorem.

The purpose of the ledger is to prevent accidental promotion, hidden imports and circular restatement.
