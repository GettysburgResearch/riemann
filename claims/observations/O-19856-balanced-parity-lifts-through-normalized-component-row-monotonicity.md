# O-19856 — The balanced/reset programme now has an exact finite parity-to-row lift

Claim ID: `O-19856`  
Status: **RESEARCH SYNTHESIS — SOURCE THEOREMS ON PR #399 PENDING INDEPENDENT REVIEW**  
Created: 2026-08-12  
RH status: **unproved**

## 1. New finite-window chain

The factor-54 branch now contains the following exact proposed chain:

```text
L-91315
    unique mass-and-score-neutral balanced ray;

L-91320
    balanced Hall transport has support e<=o;
    transport edges lift to nonnegative interval seeds;

L-91321
    each interval seed admits a positive butterfly factorisation
    up to one explicit positive upper-boundary atom;

L-91322
    stronger route: reserve-normalized exact component rows are increasing,
    so the Hall transport lifts directly to every exact finite row.
```

The final step avoids the conditioning and baseline-compatibility problem of
the butterfly inverse.

## 2. Exact normalized row profile

For the retained positive component row `Q_Y(n)`, put

\[
 \mathcal Q_n(Y)=\frac{Q_Y(n)}{\sqrt Y-1}.
\]

On every activation cell,

\[
 2Y(\sqrt Y-1)^2\mathcal Q_n'(Y)
 =M_{n,N}(Y),
 \qquad
 M_{n,N}'(Y)=-\frac{Q_Y(n)}{2\sqrt Y}\le0.
\]

The directed replay `X-91109` checks the right endpoint of all 1,431 cells and
proves `M_(n,N)>1/20` throughout the reset window.  Hence `mathcal Q_n` is
strictly increasing.

## 3. Hall transport becomes row positivity

The exact finite equality row is

\[
 c_x(n)=\sum_k\mu(k)k^{-1/2}Q_{x/k}(n).
\]

Since

\[
 k^{-1/2}Q_{x/k}(n)
 =w_1(x,k)\mathcal Q_n(x/k),
\]

the reserve Hall transport with `e<=o` gives

\[
\begin{aligned}
 c_x(n)={}&
 \sum_{e,o}\pi_R(e,o)
 [\mathcal Q_n(x/e)-\mathcal Q_n(x/o)]\\
 &+\sum_e r_e\mathcal Q_n(x/e)
 \ge0.
\end{aligned}
\]

This is a source-faithful divisor lift at the actual row level.  It does not use
the false finite-seed/Volterra identification refuted by `R-91102`.

## 4. Architectural consequence

The finite small-prime interface is no longer the main obstacle:

```text
finite parity cancellation              closed;
finite divisor destinations              closed;
exact component-row positivity           closed;
finite/continuum mismatch and collars    separately paid;
terminal annulus                          separately paid.
```

The remaining arithmetic theorem is genuinely recursive:

> compose the exact positive finite-row lift over every rough-prime generation,
> while preserving coefficient-one score, nonnegative endpoint weights,
> complete radix-four capacity, and the balanced decaying boundary port.

This is the factor-54 analogue of the fixed-observation problem on the Suzuki
and Brownian routes: the local positive reservoir and local observation are now
explicit, but the all-generation conservative colligation remains open.

## 5. Status

```text
finite normalized component-row monotonicity     PROPOSED COMPLETE / DIRECTED
Hall-to-exact-row lift                            PROPOSED COMPLETE EXACT
rough-generation conservative composition         OPEN / RH-BEARING
Riemann Hypothesis                                UNPROVED
```
