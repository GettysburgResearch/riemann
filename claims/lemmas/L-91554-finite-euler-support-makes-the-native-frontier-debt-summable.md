# L-91554 — Finite Euler support makes the native fixed-67 frontier debt absolutely summable

Claim ID: `L-91554`  
Status: **PROVED EXACT FINITE-SUPPORT SCORE-REALIZATION THEOREM — INDEPENDENT RECONSTRUCTION REQUIRED**  
Created: 2026-08-13  
Depends on: `O-91309`, `L-91452/L-91454`, `L-91540`, `L-91545`, `L-91547`, `L-91549`, `L-91553`  
RH status: **unproved**

## 1. The native one-prime source has fixed Euler support

Let

\[
 P_{79}=\prod_{q\le79}q
\]

and let `p>=83` be the single new rough prime in the terminal one-prime
splice.  Put

\[
 \boxed{
 \mathcal D_{79,p}
 =\{d:d\mid P_{79}\}\cup\{pd:d\mid P_{79}\}
 =\{n:n\mid P_{79}p\}.
 }
 \tag{L-91554.1}
\]

The exact row formula `O-91309.1` has a first sum over `d|P_79` and a second
sum multiplied by `p^-1/2`.  Reindexing the second sum by `n=pd` gives

\[
 -\frac{\mu(d)}{\sqrt{pd}}
 =\frac{\mu(pd)}{\sqrt{pd}},
 \qquad(p\nmid P_{79}),
\]

so the native one-prime packet is precisely the unit-coefficient Möbius packet
on the fixed divisor set `mathcal D_(79,p)`, with causal truncation.  The binary
return changes the target, score and row kernels pointwise but creates no new
source index.

For either target-Hall branch, let `c_s,c_h` be the positive residual source
coefficients of `L-91545`.  The original positive even capacities have source
coefficient one.  Since

\[
 c_\tau(e)
 =1-\frac{\sum_o t_{o,e}}{T_\tau(e)},
\]

one has the coefficientwise domination

\[
 \boxed{
 0\le c_s(n),c_h(n)\le
 \mathbf1_{\mathcal D_{79,p}}(n).
 }
 \tag{L-91554.2}
\]

The `P_61,p>=67` front end is a subcase with a smaller fixed divisor set.

## 2. Every source atom reaches the frontier exactly once

Put

\[
 X_j=\frac{X}{67^j}
 \qquad(j\ge0)
\]

and define the terminal layer

\[
 \boxed{
 \mathcal A_j
 =\{n:X_{j+1}<n\le X_j\}.
 }
 \tag{L-91554.3}
\]

The deterministic split of `L-91547` sends precisely the source nodes
`n<=X_(j+1)` to the next child.  Hence the sets `mathcal A_j` are disjoint,
and every initially active source node belongs to exactly one of them.

For `n in mathcal A_j`, its terminal quotient is

\[
 \boxed{
 Y_{j,n}=\frac{X_j}{n},
 \qquad1\le Y_{j,n}<67.
 }
 \tag{L-91554.4}

Before that terminal layer, every active quotient is at least `67`; after that
layer the atom is not inherited.  Thus no source coefficient can pay a frontier
charge at two different depths.

## 3. The inherited part has zero positive score debt

For every quotient `Y>=67`, `L-91553` proves

\[
 \mathcal E(Y)-\mathcal E(Y/67)
 \ge S_\tau(Y)-S_\tau(Y/67)
 \tag{L-91554.5}
\]

for both branch types, after the common positive branch row coefficient is
restored.  The current row difference is coefficientwise nonnegative, and its
literal entropy realizes the complete declared score difference.

Repeated affine lifting cannot reduce that entropy by `L-91549`.  Therefore an
atom contributes no positive source-score realization debt at any nonterminal
depth.

## 4. Uniform terminal charge of one source node

At its unique terminal layer, `L-91553.23` gives

\[
 \boxed{
 \delta_{\tau,j}(n)
 :=c_\tau(n)
 [S_{\tau,X_j}(n)-\mathcal E_{\tau,X_j}(n)]_+
 \le2c_\tau(n)T_{\tau,X_j}(n).
 }
 \tag{L-91554.6}
\]

The exact branch target identity `L-91540.24` is, with the suppressed source
factor restored,

\[
 \boxed{
 T_{s,X_j}(n)+T_{h,X_j}(n)
 =\frac{4\sqrt{Y_{j,n}}-3}{\sqrt n}.
 }
 \tag{L-91554.7}
\]

Using (L-91554.2), positivity of both branch targets, and
`1<=Y_(j,n)<67`,

\[
\begin{aligned}
 \delta_{s,j}(n)+\delta_{h,j}(n)
 &\le2\bigl(c_s(n)T_{s,X_j}(n)
            +c_h(n)T_{h,X_j}(n)\bigr)\\
 &\le2\bigl(T_{s,X_j}(n)+T_{h,X_j}(n)\bigr)\\
 &<\frac{8\sqrt{67}}{\sqrt n}
 <\frac{72}{\sqrt n}.
\end{aligned}
 \tag{L-91554.8}
\]

The deliberately crude last inequality uses `sqrt(67)<9`.

## 5. Absolute all-depth bound

Sum (L-91554.8) over the disjoint terminal layers.  Every source node occurs
once, so

\[
\boxed{
 \sum_{j\ge0}\sum_{n\in\mathcal A_j}
  [\delta_{s,j}(n)+\delta_{h,j}(n)]
 <72\sum_{n\mid P_{79}p}\frac1{\sqrt n}.
}
 \tag{L-91554.9}
\]

The divisor sum factors exactly:

\[
 \sum_{n\mid P_{79}p}\frac1{\sqrt n}
 =\left(1+\frac1{\sqrt p}\right)
  \prod_{q\le79}\left(1+\frac1{\sqrt q}\right).
 \tag{L-91554.10}
\]

Since `p>=83`, the directed checker `X-91554` certifies

\[
 \boxed{
 72\left(1+\frac1{\sqrt{83}}\right)
  \prod_{q\le79}\left(1+\frac1{\sqrt q}\right)
 <7410.
 }
 \tag{L-91554.11}
\]

Consequently the complete source-score mismatch over **all** fixed-67
descendants satisfies

\[
 \boxed{
 E_{\rm source}^{\rm all\ depth}<7410,
 }
 \tag{L-91554.12}
\]

independently of `X`, of the new rough prime, and of the number of reset depths.
For the `P_61,p>=67` packet the same expression is below `5000`.

## 6. Literal physical score realization

Let `d_src` be the sum of:

1. every nonterminal current row difference;
2. the terminal component rows;
3. their positive affine lifts to the parent coordinate;
4. the Hall row bonuses `B_s,B_h`.

All coefficients are nonnegative.  Sections 3--5 and the nonnegative entropy
of the Hall bonuses give

\[
 \boxed{
 \mathcal S_X(d_{\rm src})
 \ge
 \mathfrak S_{s,X}(c_s)+
 \mathfrak S_{h,X}(c_h)-7410.
 }
 \tag{L-91554.13}

The target-Hall entry satisfies

\[
 \mathfrak S_{s,X}(c_s)+
 \mathfrak S_{h,X}(c_h)
 \ge S_{\rm native,parent}
\]

by `L-91452/L-91454/L-91545`.  Hence

\[
 \boxed{
 \mathcal S_X(d_{\rm src})
 \ge S_{\rm native,parent}-7410.
 }
 \tag{L-91554.14}
\]

This is an **unnormalized native** estimate.  No bound on the root target mass
is needed.

## 7. What this repairs

`L-91553` left open the passage from a target-normalized frontier estimate to
the native loss.  The missing datum is not a bound on the root target amplitude;
it is the fixed finite Euler support of the actual one-prime packet.  The
large target amplitude is carried by low source indices, and those indices are
inherited through score-favorable differences until each reaches one bounded
terminal quotient.  Every source atom pays at most once.

Thus the open inequality `T-91551.13` holds with `A=0` and an explicit absolute
constant, and in fact (L-91554.12) bounds the sum over the entire fixed-67
source tree rather than one generation only.

## 8. Scope firewall

The theorem does **not** prove an absolute frontier bound for the supremum over
all target-normalized positive measures in `T-91541`; an arbitrary measure can
have unbounded weighted support.  It applies to the canonical native finite
Euler packet and every restriction of its two Hall residual measures.

It also assumes the live producer uses exactly the one-prime support displayed
in `O-91309.1`.  The formula there, the pointwise binary maps, and
`L-91545.2` make this support/coefficient audit exact, but an independent
reviewer should reconstruct that chain directly.

```text
native one-prime support divides P_79 p              EXACT
Hall residual coefficients lie in [0,1]              EXACT
one terminal frontier layer per source atom           EXACT
all inherited score differences physically paid       EXACT / L-91553
terminal debt <72/sqrt(n)                              EXACT
all-depth native source debt <7410                    DIRECTED EXACT
root target-amplitude bound                            NOT NEEDED
ordinary/radix-four capacity assembly                  SEPARATE CITED INPUT
Riemann Hypothesis                                    UNPROVEN
```
