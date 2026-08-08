# R-23705 — Generic digit variance does not force greedy saturation

Claim ID: `R-23705`  
Title: Carry and digit identities alone do not control the final greedy slack; the logarithmic target must enter through a source-specific inequality  
Status: **EXACT FINITE SCOPE REFUTATION / REVIEW CORRECTION**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Dependencies: `L-23701`, `L-23703`, `L-23705`  
Scope: generic target-independent uses of carry martingales or parity identities

## 1. The tempting but invalid inference

The carry matrix has an exact base-`p` digit interpretation, and the binary
Euler-aligned source has exact parity and digit convolution identities. It is
tempting to infer that a positive conditional-variance argument must force the
minimum-ratio greedy algorithm to saturate all columns, or at least leave only a
small amount of slack, for every nonnegative decreasing target.

That inference is false. The carry and digit identities are properties of the
matrix; final slack depends on the source target.

## 2. Exact rational control

Take `X=9` and the nonnegative decreasing target

\[
\begin{array}{c|cccccccc}
q&2&3&4&5&6&7&8&9\\ \hline
w(q)&91/100&41/50&33/50&33/50&63/100&11/20&53/100&0.
\end{array}
\tag{R-23705.1}
\]

Run the exact backward minimum-ratio algorithm of `L-23701`. It gives

\[
\begin{array}{c|cccccccc}
n&2&3&4&5&6&7&8&9\\ \hline
d(n)&651/500&133/125&0&111/250&101/250&8/35&477/700&0,
\end{array}
\tag{R-23705.2}
\]

with blocker map

\[
\begin{array}{c|cccccccc}
n&2&3&4&5&6&7&8&9\\ \hline
q_X(n)&2&3&4&4&6&7&8&9.
\end{array}
\tag{R-23705.3}
\]

Thus row `n=5` is blocked by the off-diagonal column `q=4`.

The final residual is

\[
\boxed{
 s(5)=29/500,}
\tag{R-23705.4}
\]

and every other final column slack is zero. All arithmetic is rational.

## 3. What survives in the control

The following matrix identities remain exact in this example:

- the carry-count formula for every `beta_(nq)`;
- the Kummer/Legendre digit decomposition on every prime-power column;
- the binary parity convolution;
- the binary digit convolution;
- nonnegativity of every greedy coefficient and residual.

Nevertheless the total final slack is strictly positive.

Therefore a proof of the Greedy Slack Theorem cannot consist solely of:

```text
carry rows are conditional digit variances
+ parity boundary identities
+ positivity of the residual
=> small final slack.
```

It must use the special logarithmic square-root target

\[
w_X(q)=q^{-1/2}\log(X/q)
\]

in a quantitative, source-specific way.

## 4. Consequence for the eight-step DBT outline

The exact quotient-layer, Möbius-affine, and digit identities remain valuable.
But the phrase

```text
pay the internal cell by conditional variance
```

is not yet a theorem. To close DBT it must produce an inequality whose left side
is the total slack `Sigma_X` of `L-23705`, and whose right side consists only of:

1. nonnegative reflected-square terms;
2. explicitly telescoping digit endpoints;
3. strictly smaller-scale slack ledgers;
4. a polylogarithmic boundary budget.

Likewise, the global reflected Selberg identity cannot be inserted as if it were
one physical quotient layer. The local two-frequency source map and every cross
term must be written before its positive square can pay a blocker.

## 5. Status boundary

Refuted:

- a target-independent implication from carry/digit martingale structure to
  zero or polylogarithmic greedy slack;
- treating “conditional variance pays the cell” as an automatic consequence of
  Kummer's theorem.

Not refuted:

- polylogarithmic slack for the actual logarithmic target;
- DBT;
- a source-specific quotient-layer/reflected-Selberg proof;
- RH.
