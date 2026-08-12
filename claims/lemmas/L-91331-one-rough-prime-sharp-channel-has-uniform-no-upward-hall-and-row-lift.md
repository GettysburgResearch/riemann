# L-91331 — One rough prime sends SHARP into a uniformly Hall-positive effective channel

Claim ID: `L-91331`  
Status: **PROPOSED COMPLETE EXACT ONE-PRIME RESET PROJECTION — ALL-GENERATION IDENTIFICATION OPEN**  
Created: 2026-08-12  
Depends on exact paths:

- `claims/lemmas/L-91327-rough-euler-semigroup-has-a-positive-four-state-linear-dilation.md`;
- `claims/lemmas/L-91322-normalized-component-row-monotonicity-lifts-the-parity-shadow-exactly.md`;
- `claims/lemmas/L-91328-p61-forcing-has-a-uniform-one-rough-prime-margin.md`.

RH status: **unproved**

## 1. Effective channel after one rough prime

Use the diagonal modes

\[
 X=L-R,\qquad Y=L-2R,
\]

so that

\[
 \Psi=L+2R=4X-3Y=3U_{4/3},
 \qquad U_a=aX-Y.
\]

For one rough prime `p`, put

\[
 A_p=1-p^{-1},\qquad B_p=1-p^{-1/2}.
\]

The exact rough action is

\[
 X\mapsto A_pX,\qquad Y\mapsto B_pY.
\]

Consequently

\[
\boxed{
 \Psi_p
 =4A_pX-3B_pY
 =3B_pU_{a_p},
 \qquad
 a_p=\frac{4A_p}{3B_p}
     =\frac43(1+p^{-1/2}).
}
\tag{L-91331.1}
\]

For every `p>=67`,

\[
 \boxed{
 \frac43<a_p<\frac32,
 }
\tag{L-91331.2}
\]

because `sqrt(p)>8`.

Thus the state presented after one new least rough prime is not an arbitrary
point of the four-state cone. It is one ordinary Möbius channel in a fixed
compact parameter interval.

## 2. Uniform no-upward Hall theorem

For a squarefree atom `n<=x`, let

\[
 w_a(x,n)=\frac{a\sqrt x}{n}-\frac1{\sqrt n}.
\]

For every active odd threshold `t`, define

\[
 \mathcal H_{a,t}(x)
 =\sum_{\substack{e\le t\\\mu(e)=1}}w_a(x,e)
  -\sum_{\substack{o\le t\\\mu(o)=-1}}w_a(x,o).
\tag{L-91331.3}
\]

For fixed `x,t`, this is affine in `a`. Therefore its minimum over
`4/3<=a<=3/2` occurs at one of the two endpoints.

The directed checker `X-91118` evaluates both endpoint parameters on every
activation-cell endpoint and every active odd threshold throughout

\[
 1\le x\le c_0^{-1}.
\]

It proves

\[
 \boxed{
 \mathcal H_{4/3,t}(x)>\frac15,
 \qquad
 \mathcal H_{3/2,t}(x)>\frac1{10}.
 }
\tag{L-91331.4}
\]

Hence, uniformly for the complete parameter interval,

\[
 \boxed{
 \mathcal H_{a,t}(x)>\frac1{10}
 \qquad
 \left(\frac43\le a\le\frac32\right).
 }
\tag{L-91331.5}
\]

Hall's theorem supplies a positive transport from odd to even squarefree mass
with support

\[
 \boxed{e\le o.}
\tag{L-91331.6}
\]

In particular this applies to every effective one-prime parameter `a_p`.

## 3. Direct exact-row lift

`L-91330` proves that for every `a>=1` the normalized component-row profile

\[
 \mathcal Q_{n,a}(Y)=\frac{Q_Y(n)}{a\sqrt Y-1}
\]

is strictly increasing on the entire reset window. Therefore every Hall edge
`e<=o` satisfies

\[
 \mathcal Q_{n,a}(x/e)-\mathcal Q_{n,a}(x/o)\ge0.
\]

Using

\[
 k^{-1/2}Q_{x/k}(n)
 =w_a(x,k)\mathcal Q_{n,a}(x/k),
\]

the one-prime Hall transport lifts directly to every exact finite component row.
After multiplication by `3B_p>0`, the row is precisely the effective SHARP row
in (L-91331.1).

Thus every one-prime transition admits a source-faithful, no-upward, positive
row projection with a fixed Hall reserve exceeding `1/10`.

## 4. What this closes

The review's live four-state frontier required a local projection after rough
propagation. The theorem proves that projection whenever the incoming state is
exactly the one-new-least-prime SHARP state. It also strengthens `L-91328`, which
certifies only the scalar one-prime forcing margin.

The remaining all-generation theorem is now the compatibility statement:

> prove that the least-prime source decomposition presents each contracted child
> to the next reset exactly in the effective form (L-91331.1), with the unmatched
> even residual becoming the next source state, all target shares charged once,
> and the score recurrence retaining coefficient one.

This identification is not supplied by scalar one-prime positivity alone.

## 5. Proof boundary

```text
one-prime SHARP effective-channel identity       EXACT
parameter interval 4/3<a_p<3/2                  EXACT
uniform no-upward Hall margin >1/10              DIRECTED EXACT
exact finite-row Hall lift                       PROPOSED COMPLETE
one-prime reset projection                       PROPOSED COMPLETE
least-prime all-generation child identification  OPEN / RH-BEARING
coefficient-one score/capacity recursion          OPEN
Riemann Hypothesis                               UNPROVEN
```
