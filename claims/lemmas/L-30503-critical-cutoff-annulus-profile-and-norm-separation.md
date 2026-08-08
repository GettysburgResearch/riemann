# L-30503 — Activation firewall for the unqualified analytic boundary

Claim ID: `L-30503`  
Title: Extending every stopped layer into the analytic bulk before its first active row creates a different macroscopic boundary; the activation threshold `Y>=2q-1` is load bearing  
Status: **EXACT SCOPE CORRECTION / MUTATION ANALYSIS — NOT THE PRODUCTION BOUNDARY**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Corrected: 2026-08-08 after comparison with the exact active-layer formula in `L-30501`  
Frozen target: PR #304 at `78b75fc17e27334a9950018528c1c6e083d74820`  
Dependencies: `L-30501`; PR #286 `L-28401/L-28402`; elementary eta/Hasse series  
Scope: adversarial mutation showing why source activation cannot be omitted

## 1. Two different analytic splits

Put

\[
 p(q)=q^{-1/2},
 \qquad
 w_X(q)=q^{-1/2}\log(X/q)\mathbf1_{q\le X}.
\]

The **production** stopped-power decomposition activates the analytic central output at column `q` only for endpoint layers

\[
 Y\ge2q-1.
\]

Accordingly, `L-30501` proves that its actual first aggregate boundary is

\[
 \boxed{
 b_X(q)=
 \log\frac{X}{2q-1}\,\mathscr Cp(q)
 -\mathscr C_Xw_X(q).
 }
 \tag{L-30503.1}
\]

A tempting but invalid shortcut is to extend every layer with `Y>=q` into the analytic bulk.  That produces instead

\[
 \boxed{
 Q_X^{\rm all}(q)=
 \log\frac Xq\,\mathscr Cp(q)
 -\mathscr C_Xw_X(q).
 }
 \tag{L-30503.2}
\]

The two differ by the explicit positive analytic channel

\[
 \boxed{
 Q_X^{\rm all}(q)-b_X(q)
 =
 \log\frac{2q-1}{q}\,\mathscr Cp(q).
 }
 \tag{L-30503.3}
\]

Thus `Q_X^all` is **not** the production boundary.  It is the exact mutation obtained by ignoring the first-active-row condition.

## 2. Annular profile of the mutation

Let

\[
 f_X(x)=x^{-1/2}\log(X/x)
\]

on the analytic continuation beyond `X`.  The quantity in (L-30503.2) is equivalently the omitted-tail expression

\[
 Q_X^{\rm all}(q)
 =
 \sum_{2kq-1>X}f_X(2kq-1)
 -\sum_{(2k+1)q>X}f_X((2k+1)q).
 \tag{L-30503.4}
\]

For

\[
 \frac{2X}{5}\le q\le\frac{4X}{9},
 \qquad r=\frac Xq\in\left[\frac94,\frac52\right],
\]

the first omitted odd and shifted-even indices are respectively `1` and `2`. Hence

\[
 \sqrt q\,Q_X^{\rm all}(q)
 =-\phi_r(3)
 +\sum_{k\ge2}[\phi_r(2k-1/q)-\phi_r(2k+1)],
 \tag{L-30503.5}
\]

where `phi_r(x)=x^(-1/2)log(r/x)`.

Uniformly on the annulus,

\[
 \boxed{
 \sqrt q\,Q_X^{\rm all}(q)=H(r)+O(1/q),
 }
 \tag{L-30503.6}
\]

with

\[
 H(r)=P(1/2)\log r+P'(1/2),
 \qquad
 P(s)=1-\eta(s)-2^{-s}.
 \tag{L-30503.7}
\]

The elementary derivative majorant makes the error at most `6/q`.

## 3. Directed mutation moat

`X-30502` uses the globally convergent Hasse series and rational square-root/logarithm enclosures to prove

\[
 P(1/2)<0,
 \qquad
 H(5/2)>\frac1{1000}.
 \tag{L-30503.8}
\]

Therefore the **unqualified mutation** has a positive macroscopic annulus and its isolated divisor-source atomic norm is linear.

This does not supply an additional contradiction beyond `L-30501`, because the mutation is not the actual stopped-power boundary.  Instead it proves a fail-closed review rule:

\[
 \boxed{
 \text{every source manifest must enforce }Y\ge2q-1
 \text{ before inserting the analytic bulk.}
 }
 \tag{L-30503.9}
\]

Deleting that activation condition changes both the sign and the annular constant of the boundary.

## 4. Norm-separation observation

On every fixed ratio cell, `Q_X^all` is a `C^1` profile at scale `X^{-1/2}`. Consequently

\[
 \sum_{q\text{ in the cell}}
 \sqrt q\,|Q_X^{\rm all}(q+1)-Q_X^{\rm all}(q)|=O(1),
 \tag{L-30503.10}
\]

even though its isolated divisor-source value norm is `Omega(X)`.

The same methodological warning applies to the true boundary of `L-30501`: atomic source conversion can destroy cancellations present in the central-flow coordinate.  The production repair must use the activated coupled flow in `L-30502`, not the mutation (L-30503.2).

## 5. Proof boundary

Closed here:

1. the exact difference between activated and unqualified analytic splits;
2. the annular eta profile of the unqualified mutation;
3. a directed positive margin for that mutation;
4. the activation firewall and norm-separation warning.

Not claimed:

1. that `Q_X^all` is the PR #304 production boundary;
2. an additional refutation beyond `L-30501`;
3. a cycle-debt estimate or RH.
