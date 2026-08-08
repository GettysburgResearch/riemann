# T-27901 — Dyadic sign rigidity and endpoint domination: a full RH proposal

Claim ID: `T-27901`  
Title: Cofinal one-crossing of every finite dyadic shell reduces WSTS to one endpoint-prime domination inequality  
Status: **FULL CONDITIONAL PROPOSAL — ONE EXPLICIT SOURCE-SPECIFIC THEOREM OPEN**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen parent: PR #276 at `a65a02b9463c1cc3a10d0af03ab359a637e357cd`  
Dependencies: `L-27901`--`L-27904`; PR #276 `T-27501`; PR #240; PR #265; PR #274  
Scope: full Riemann Hypothesis; RH is not claimed proved

## 1. New full-problem spine

PR #276 identifies Weighted Shell-Tail Stability (`WSTS`) as an exact RH-equivalent theorem. The prior formulation maximizes over every prime tail and therefore presents the final arithmetic burden as a large family of cuts.

The new work proves, subject to independent review:

```text
continuum shell one-crossing             L-27901;
uniform O(q^-3/2) shell floor error      L-27902;
one-crossing collapse of WSTS tails      L-27903;
cofinal finite shell-crossing rigidity   L-27904.
```

The complete proposed proof spine is now

```text
cofinal finite dyadic one-crossing
-> every WSTS tail collapses to the full tail
-> endpoint prime domination EPD
-> exact dyadic shell charge B_X=0
-> WSTS
-> sharp prime ramp
-> square-screw / Landau
-> RH.
```

Thus only one source-specific arithmetic sign theorem remains.

## 2. Cofinal finite shell-crossing is supplied

For

\[
Y=\lfloor X/2\rfloor,
\qquad
s_X(q)=r_X(q)-\mathbf1_{q\le Y}r_Y(q),
\]

`L-27904` proves that, for every sufficiently large `X`, there is a threshold `q_*(X)` such that

\[
\boxed{
s_X(q)>0\quad(q<q_*(X)),
\qquad
s_X(q)\le0\quad(q\ge q_*(X)).}
\tag{T-27901.1}
\]

Moreover

\[
\boxed{
{q_*(X)\over X}\longrightarrow
\theta_*=0.1408520350138\ldots.}
\tag{T-27901.2}
\]

The proof has four independent parts:

1. the normalized continuum moat
   \[
   \sqrt\theta D(\theta)
   \to-(\zeta(1/2)+1)\log2>0
   \]
   controls every nonfixed low-ratio coordinate;
2. every fixed coordinate has a strictly positive Hurwitz-zeta limit;
3. the exact finite shell is strictly decreasing throughout quotient cell seven;
4. the upper reciprocal cells have a strict negative moat, and the outermost cell is elementary.

Finite reconnaissance is not used to complete the cofinal theorem.

## 3. Exact collapse of WSTS

Since `log p>0`, the weighted prime shell has the same one-crossing order as `s_X(p)`. Every tail sum first decreases while negative terms are added and then increases while positive terms are added. Therefore

\[
\boxed{
\mathcal B_X
=\left[
\sum_{p\le X}(\log p)s_X(p)
\right]_+.}
\tag{T-27901.3}

Define the ordinary-prime discrepancy

\[
\boxed{
\Delta_X
=J_{\mathbb P,X}(b_X^{(0)})-P_X.}
\tag{T-27901.4}

The exact ordinary-prime dual identity gives

\[
\boxed{
\mathcal B_X
=[\Delta_X-\Delta_{\lfloor X/2\rfloor}]_+.}
\tag{T-27901.5}

Thus the maximum over all WSTS tails has been eliminated. The final scalar is one dyadic increment of one global discrepancy.

## 4. Sole remaining theorem — Endpoint Prime Domination

For real `X`, define the endpoint source

\[
\boxed{
\dot b_X(m)
=2\sqrt m(1-\sqrt{m/X})\mathbf1_{m\le X}.}
\tag{T-27901.6}

Put

\[
\eta_X(p)=v_p(\dot b_X)-p^{-1/2}.
\tag{T-27901.7}

The entering endpoint has zero coefficient, so differentiation introduces no omitted atom. Hence

\[
\boxed{
\partial_{\log X}\Delta_X
=\sum_{p\le X}(\log p)\eta_X(p).}
\tag{T-27901.8}

The sole new theorem required is

\[
\boxed{
\mathrm{EPD}:\qquad
\sum_{p\le X}(\log p)
 [v_p(\dot b_X)-p^{-1/2}]
\le0
\qquad(X\ge X_0).}
\tag{T-27901.9}

Equivalently, `Delta_X` is eventually nonincreasing.

## 5. Preferred construction — Endpoint Squarefree Collector

Three exact inputs point to a concrete proof of EPD:

1. PR #265 proves every parabolic endpoint increment is a nonnegative carry-row atom;
2. PR #240 `L-23827` proves the continuum endpoint response is tail-majorized by the critical target increment;
3. PR #274 proves positive constant blocks between squarefree endpoints are exactly neutral on every proper prime power and have nonnegative logarithmic objective.

The proposed production theorem is:

> **Endpoint Squarefree Collector (`ESC`).** For every sufficiently large `X`, lift the monotone continuum coupling of the endpoint atom to nonnegative squarefree incidence blocks so that every ordinary-prime endpoint residual is nonpositive, every proper-prime-power response is exactly zero, and the physical objective does not decrease.

`ESC` implies `EPD` immediately.

Its exact Farkas dual uses

\[
Y_y(n)=\sum_{p\mid n}y_p,
\qquad y_p\ge0,
\]

monotone on the declared squarefree collector graph. A valid proof must show

\[
\sum_{p\le X}y_p\eta_X(p)\le0
\]

for every such potential. The logarithmic ray `y_p=log p` remains admissible and is the mandatory RH firewall.

## 6. Alternative physical route

The endpoint source may instead be inserted into PR #241's independent-frequency normal block and PR #263's parity-paired inverse-zeta frame. The carry sector may pay transverse rows, but PR #269 `R-26902` requires the endpoint/bottom-charge commutator to remain in the physical channel before the carry-window zeta factor cancels the RH pole.

Because finite one-crossing is now supplied, the required physical boundary Schur complement has only one scalar consumer: (T-27901.9).

## 7. Conditional completion

Assume `EPD`. Then `Delta_X` is nonincreasing, so (T-27901.5) gives

\[
\boxed{
\mathcal B_X=0}
\tag{T-27901.10}

for every sufficiently large `X`.

This is stronger than WSTS. PR #276 then yields

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
\mathrm{EPD}\Longrightarrow\mathrm{RH}.}
\tag{T-27901.11}

The weaker dyadic statement

\[
[\Delta_X-\Delta_{\lfloor X/2\rfloor}]_+
=O_\varepsilon(X^\varepsilon)
\tag{T-27901.12}
\]

also suffices and is exactly WSTS after `L-27904`.

## 8. Discovery evidence and its boundary

The committed replay checks all integer coordinates through `20,000` and all prime coordinates through `200,000`. A separate optimized scan through `10^7` found:

```text
one-crossing violations                 0
positive weighted-tail violations       0
crossing ratio at X=10^7                 0.1408523
```

The finite data are retained only as mutation tests. They do not prove EPD or RH.

## 9. Mandatory adversarial tests

Reject a claimed completion if it:

1. uses finite sign scans instead of checking `L-27904`;
2. reverses the Hurwitz-zeta monotonicity or eta-series sign;
3. loses the odd-endpoint ratio `floor(X/2)/X`;
4. replaces EPD by the unweighted prime queue refuted on PR #274;
5. uses a squarefree collector with a proper prime-power divisor;
6. deletes the logarithmic dual ray;
7. takes a positive part before complete dyadic shell subtraction;
8. loses the dyadic or `2/3` first-cell mutation;
9. claims RH while EPD or its dyadic weakening remains assumed.

## 10. Exact status

```text
continuum dyadic one-crossing                PROPOSED COMPLETE
uniform shell floor-error sharpening         PROPOSED COMPLETE
cofinal finite shell-crossing rigidity        PROPOSED COMPLETE
one-crossing collapse of WSTS tails           PROPOSED COMPLETE
endpoint derivative identity                  PROPOSED COMPLETE
endpoint squarefree collector / EPD            OPEN / RH-BEARING
EPD -> WSTS with zero debt -> RH               PROPOSED COMPLETE
Riemann Hypothesis                             UNPROVED
```

This is a full, sharply reviewable proposal with one explicit remaining theorem. It is not represented as an unconditional proof of RH.
