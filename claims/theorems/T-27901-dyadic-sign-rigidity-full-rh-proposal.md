# T-27901 — Dyadic sign rigidity and endpoint domination: a full RH proposal

Claim ID: `T-27901`  
Title: Exact one-crossing of every finite dyadic shell plus one endpoint-prime domination inequality forces WSTS with zero debt and proves RH  
Status: **FULL UNCONDITIONAL PROPOSAL — TWO EXPLICIT SOURCE-SPECIFIC THEOREMS OPEN**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen parent: PR #276 at `a65a02b9463c1cc3a10d0af03ab359a637e357cd`  
Dependencies: `L-27901`--`L-27903`; PR #276 `T-27501`; PR #240; PR #265; PR #274  
Scope: full Riemann Hypothesis; RH is not claimed proved

## 1. Why this is a new full-problem attack

PR #276 identifies Weighted Shell-Tail Stability (`WSTS`) as an exact RH-equivalent theorem. The prior formulation still maximizes over every prime tail and therefore looks like a large family of unrelated arithmetic cuts.

`L-27901` proves that the underlying dyadic continuum shell has exactly one sign change. `L-27902` proves that dyadic subtraction removes the logarithmic floor-error growth. `L-27903` shows that a finite one-crossing theorem collapses the entire WSTS maximum to one total shell scalar.

The proposed proof spine is therefore

```text
continuum shell one-crossing
-> finite shell-crossing rigidity FSCR
-> all weighted tails collapse to the full tail
-> endpoint prime domination EPD
-> exact dyadic shell charge B_X=0
-> WSTS
-> sharp prime ramp
-> square-screw / Landau
-> RH.
```

This attacks a stronger global sign theorem rather than estimating an arbitrary RH-equivalent norm.

## 2. The first open theorem — finite shell-crossing rigidity

For

\[
Y=\lfloor X/2\rfloor,
\]

put

\[
s_X(q)=r_X(q)-\mathbf1_{q\le Y}r_Y(q).
\]

The required theorem is

\[
\boxed{
\exists q_*(X):
\quad
s_X(q)\ge0\ (q\le q_*(X)),
\qquad
s_X(q)\le0\ (q>q_*(X))
}
\tag{FSCR}
\]

for every sufficiently large integer `X`.

This is not an `X`-dimensional sign search. `L-27902` reduces it to:

1. a fixed finite low-coordinate dictionary;
2. a bounded-width collar around
   \[
   q=\theta_*X,
   \qquad
   \theta_*=0.1408520350138\ldots.
   \]

The rest of the finite shell already has the continuum sign by a uniform `O(q^-3/2)` floor estimate.

### Proposed proof mechanisms

- **Exact quotient-cell monotonicity.** In the transition collar, `floor(X/q)=7` and `floor(Y/q)=3`; the residual is an explicit seven-term minus three-term function. Prove it is strictly decreasing in `q` after exact endpoint rounding.
- **Low-coordinate digital recurrence.** For each fixed low `q`, dyadic shell cancellation leaves a convergent complete-lattice expansion with positive leading constant
  \[
  -[\zeta(1/2)+1]\log2\,q^{-1/2}.
  \]
  A fixed interval gate then covers every remaining endpoint.
- **Machine-checkable finite boundary.** The two bounded dictionaries can be certified with rational square-root and logarithm enclosures; finite floating evidence is not promoted.

## 3. The second open theorem — endpoint prime domination

For real `X`, define

\[
\dot b_X(m)
=2\sqrt m(1-\sqrt{m/X})\mathbf1_{m\le X}.
\]

The endpoint residual is

\[
\eta_X(p)=v_p(\dot b_X)-p^{-1/2}.
\]

The proposed global sign theorem is

\[
\boxed{
\sum_{p\le X}(\log p)\eta_X(p)\le0
\qquad(X\ge X_0).
}
\tag{EPD}
\]

By `L-27903`, this says exactly that the ordinary-prime discrepancy

\[
\Delta_X
=J_{\mathbb P,X}(b_X^{(0)})-P_X
\]

is nonincreasing with the endpoint scale.

### Source-specific squarefree-collector route

PR #265 proves that every parabolic endpoint increment is a nonnegative carry-row atom. PR #240 `L-23827` proves that its continuum response is tail-majorized by the critical target increment. PR #274 proves that every positive block between squarefree endpoints is exactly proper-power neutral and has nonnegative logarithmic objective.

The preferred production theorem is therefore:

> **Endpoint Squarefree Collector (`ESC`).** For every sufficiently large `X`, lift the monotone continuum coupling of the endpoint atom to nonnegative squarefree incidence blocks so that every ordinary-prime endpoint residual is nonpositive, every proper-prime-power response is exactly zero, and the physical objective does not decrease.

`ESC` implies `EPD` immediately by the ordinary-prime dual identity.

The exact dual review surface is a strongly additive potential

\[
Y_y(n)=\sum_{p\mid n}y_p,
\qquad y_p\ge0,
\]

monotone on the declared squarefree collector graph. A valid proof must establish

\[
\sum_{p\le X}y_p\eta_X(p)\le0
\]

for every such potential. The logarithmic ray `y_p=log p` is retained; it is the equality-facing RH firewall, not deleted by the transport.

### Reflected boundary route

An alternative is to insert the endpoint source into PR #241's independent-frequency normal block and PR #263's parity-paired inverse-zeta frame. The carry-window sector may pay transverse rows, but PR #269 `R-26902` requires the endpoint/bottom-charge commutator to remain in the physical channel before the zeta factor cancels.

The one-crossing theorem reduces the required physical Schur complement to the single total endpoint scalar in `EPD`.

## 4. Exact deduction from FSCR and EPD

Assume `FSCR`. `L-27903` gives

\[
\mathcal B_X
=[\Delta_X-\Delta_{\lfloor X/2\rfloor}]_+.
\tag{T-27901.1}
\]

Assume also `EPD`. Then `Delta_X` is nonincreasing, so

\[
\boxed{\mathcal B_X=0}
\tag{T-27901.2}
\]

for every sufficiently large `X`.

This is strictly stronger than WSTS. PR #276 then gives

\[
\mathcal B_X=0
\Longrightarrow
P_X\ge4\sqrt X-X^{o(1)}
\Longrightarrow
\mathrm{RH}.
\]

Hence

\[
\boxed{
\mathrm{FSCR}+\mathrm{EPD}
\Longrightarrow
\mathrm{RH}.}
\tag{T-27901.3}
\]

## 5. Weaker accepted completion

A proof need not establish exact eventual nonpositivity. It is sufficient to prove `FSCR` and

\[
[\Delta_X-\Delta_{\lfloor X/2\rfloor}]_+
=O_\varepsilon(X^\varepsilon).
\tag{T-27901.4}
\]

This is already WSTS. The exact sign version is preferred because it matches all current finite evidence and exposes a concrete falsifiable theorem.

## 6. Discovery evidence and its strict boundary

The committed standard-library replay checks:

```text
all integer coordinates through X=20,000;
all prime coordinates through X=200,000;
one sign change in every checked shell;
no positive weighted prime tail;
crossing ratio converging to theta_*.
```

A separate optimized floating reconnaissance through `X=10^7` found:

```text
one-crossing violations                 0
positive weighted-tail violations       0
crossing ratio at X=10^7                 0.1408523
```

This evidence motivates `FSCR+EPD`; it certifies neither theorem.

## 7. Mandatory adversarial tests

Reject a claimed completion if it:

1. infers finite one-crossing from the continuum theorem without the two bounded gates;
2. uses the old `O(q^-3/2 log(X/q))` error after dyadic cancellation but fails to prove the sharpened shell estimate;
3. checks only prime coordinates when claiming `FSCR` for all integer columns;
4. replaces `EPD` by unweighted prime-tail charge, which has the density drift refuted on PR #274;
5. uses squarefree collectors but leaks into a proper prime power;
6. deletes the logarithmic dual ray;
7. takes a positive part before the complete dyadic shell subtraction;
8. promotes the `10^7` reconnaissance to a cofinal theorem;
9. loses the `2/3` first-cell Mertens mutation;
10. claims RH while either `FSCR` or the endpoint scalar remains assumed.

## 8. Exact status

```text
continuum dyadic one-crossing                PROPOSED COMPLETE
uniform shell floor-error sharpening         PROPOSED COMPLETE
finite sign problem -> two bounded gates      PROPOSED COMPLETE REDUCTION
one-crossing collapse of WSTS tails           PROPOSED COMPLETE
endpoint derivative identity                  PROPOSED COMPLETE
finite shell-crossing rigidity FSCR            OPEN
endpoint squarefree collector / EPD            OPEN / RH-BEARING
FSCR + EPD -> WSTS -> RH                       PROPOSED COMPLETE
Riemann Hypothesis                             UNPROVED
```

This is an ambitious full-problem proposal, not an unconditional proof. It should be reviewed first at `L-27901`, then at the two exact production gates `FSCR` and `ESC/EPD`.
