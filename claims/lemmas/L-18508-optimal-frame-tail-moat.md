# L-18508 — The exact frame–tail moat and the optimal threshold

Claim ID: `L-18508`  
Title: The full-complement zero frame gives the visible Schur floor directly, and the requested threshold exists exactly when one scalar moat is positive  
Status: `PROVED FINITE ALGEBRA; COFINAL ARITHMETIC MOAT OPEN`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-01  
Dependencies: `L-18507`; the harmonic certified-zero lower form; elementary interval arithmetic  
Scope: the inequality `epsilon < B_T+beta < Sigma` and the visible Schur block  
Related candidates: none

## 1. Setting

Fix one support and suppress the support index. Let

\[
 U=R\oplus_{G_C}W,
 \qquad W=R^{\perp_{G_C}}\cap U,
\]

where `U` is the actual complete harmonic low packet. Let `Z` be a finite
proof-grade set of simple critical-line zeros and suppose

\[
 K_Z^C|_W\succeq \sigma_Z^2 G_C|_W,
 \qquad \sigma_Z^2>0.                                    \tag{L-18508.1}
\]

Let `K_T^C` be a larger selected-zero Gram containing `K_Z^C`, let `B_T>=0`
be the complete one-sided omitted-zero budget in the harmonic lower form, and
assume

\[
 S_U\succeq K_T^C-B_TG_C.                                \tag{L-18508.2}
\]

Finally let `epsilon>=0` be a certified radical evaluation endpoint,

\[
 K_T^C|_R\preceq \epsilon G_C|_R.                        \tag{L-18508.3}
\]

## 2. Direct visible Schur floor

Since `K_T^C>=K_Z^C`, restricting (L-18508.2) to `W` gives immediately

\[
 \boxed{
 S_U|_W\succeq(\sigma_Z^2-B_T)G_C|_W.}                  \tag{L-18508.4}
\]

Thus the selected-zero eigenvalue count and the principal-angle estimate are
not needed to prove the visible Schur floor once `L-18507` has framed the
**actual** complement `W`.

In the original three-block coordinates,

\[
 \boxed{
 B_V-Z^*C^{-1}Z
 \succeq(\sigma_Z^2-B_T)G_V.}                            \tag{L-18508.5}
\]

Consequently the exact visible gate is simply

\[
 \boxed{B_T<\sigma_Z^2.}                                 \tag{L-18508.6}
\]

The radical endpoint `epsilon` is still useful for count saturation and may
enter the radical-row rate, but it is not required for (L-18508.4).

## 3. Exact solution of the requested scalar interval

Fix nonnegative numbers `epsilon,B` and a positive frame endpoint `sigma`.
There exists a number `beta>0` satisfying

\[
 \epsilon<B+\beta<\sigma                                 \tag{L-18508.7}
\]

if and only if

\[
 \boxed{\max\{\epsilon,B\}<\sigma.}                      \tag{L-18508.8}
\]

Indeed the admissible interval for `beta` is

\[
 \max\{0,\epsilon-B\}<\beta<\sigma-B.                   \tag{L-18508.9}
\]

It is nonempty exactly under (L-18508.8).

### Positive visible margin

If one also requires `beta>epsilon`, so that the counted transfer itself has
strict visible floor `beta-epsilon`, then such a `beta` exists exactly when

\[
 \boxed{B+\epsilon<\sigma.}                              \tag{L-18508.10}
\]

The midpoint choice

\[
 \beta_*
 =\frac{\epsilon+\sigma-B}{2}                            \tag{L-18508.11}
\]

gives

\[
 \beta_*-\epsilon
 =\frac{\sigma-B-\epsilon}{2}>0.                         \tag{L-18508.12}
\]

### The Gaussian schedule `epsilon<=beta/2`

The stronger condition used in the harmonic three-block schedule,

\[
 \epsilon\le\frac{\beta}{2},
 \qquad B+\beta<\sigma,                                  \tag{L-18508.13}
\]

is feasible if and only if

\[
 \boxed{B+2\epsilon<\sigma.}                             \tag{L-18508.14}
\]

Under (L-18508.14), the exact midpoint of the interval
`[2epsilon,sigma-B]` is

\[
 \boxed{
 \beta_{\rm G}
 =\epsilon+\frac{\sigma-B}{2}.}                          \tag{L-18508.15}
\]

It satisfies

\[
 2\epsilon\le\beta_{\rm G}<\sigma-B,                    \tag{L-18508.16}
\]

\[
 B+\beta_{\rm G}
 =\frac{\sigma+B+2\epsilon}{2}<\sigma,                  \tag{L-18508.17}
\]

and

\[
 \boxed{
 \beta_{\rm G}-\epsilon
 =\frac{\sigma-B}{2}.}                                   \tag{L-18508.18}
\]

Hence no threshold search is needed after the three directed endpoints have
been certified.

## 4. The optimized proof-facing scalar

For one support define

\[
 \boxed{
 \mathfrak M
 =\sup_{(T,Z)}
   \bigl(\sigma_Z^2-B_T\bigr),}                          \tag{L-18508.19}
\]

where the supremum runs over compatible finite proof-grade simple-line-zero
blocks `Z`, complete selected blocks through `T`, and their source-bound
one-sided omitted-zero budgets.

Equation (L-18508.4) shows that `mathfrak M` is the best visible lower floor
obtainable from the selected-zero-plus-one-sided-tail interface. More precisely,
for every `m<mathfrak M` there is a finite proof object with

\[
 S_U|_W\succeq mG_C|_W.                                  \tag{L-18508.20}
\]

The strong Gaussian threshold schedule exists exactly when

\[
 \boxed{\mathfrak M>2\epsilon.}                          \tag{L-18508.21}
\]

Indeed choose a finite block with
`\sigma_Z^2-B_T>2epsilon` and apply (L-18508.15). Conversely, any finite block
satisfying (L-18508.13) has
`\sigma_Z^2-B_T>2epsilon`.

The weaker displayed inequality in the user request is equivalent to positivity
of

\[
 \sup_{(T,Z)}
 \left[\sigma_Z^2-\max\{B_T,\epsilon\}\right].           \tag{L-18508.22}
\]

## 5. Direct three-block bypass

If `mathfrak M>0`, one may bypass the selected-zero count completely:
choose any `0<beta_vis<mathfrak M` and use

\[
 B_V-Z^*C^{-1}Z\succeq\beta_{\rm vis}G_V.                \tag{L-18508.23}
\]

The triangular radical-row theorem then consumes its own compression and cross
rates. In this direct formulation `epsilon` is not a visible-block hypothesis.
The quantitative target is strictly smaller:

\[
 \boxed{\mathfrak M>0}                                   \tag{L-18508.24}
\]

plus the already-declared radical-row rates relative to the chosen
`beta_vis`.

## 6. Proof boundary

- All equivalences and threshold formulas above are exact.
- `L-18507` proves only that some `sigma_Z^2` is positive at each finite support.
- Neither qualitative uniqueness nor finite dimensionality proves
  `mathfrak M>0` cofinally.
- Under a hypothetical off-line zero, the selected-real-zero frame can be
  overwhelmed by the complete signed residual; this is the fixed negative
  alternative isolated by the Xi-cardinal defect theorems.
- Therefore (L-18508.21) or even (L-18508.24) remains the RH-bearing arithmetic
  statement. No RH proof is claimed here.
