# L-90227 — Claude's Zeta23 theorem gives a local Pontryagin-index budget for every Weil compression

Claim ID: `L-90227`  
Status: **IMPORTED-THEOREM COROLLARY / PROPOSED COMPLETE EXACT BRIDGE — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: Claude, *More than two thirds of the zeros of the Riemann zeta function lie on the critical line*, Theorem D; exact Weil cardinal block `L-15613`; inertia under pullback  
External formal artifact: `https://github.com/anthropics/zeta-23-lean`  
Scope: asymptotic local index and dimension budget; no exclusion of the residual off-line sector and no RH conclusion

## 1. Imported constant

Put

\[
 c_1^*
 =\frac{\sqrt2\tan(1/\sqrt2)}
 {1+(1/\sqrt2)\tan(1/\sqrt2)},
\]

and

\[
 \boxed{
 c_{\rm MT}=2-\frac1{c_1^*}
 =\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2}
 =0.672500703679\ldots .
 }
 \tag{L-90227.1}
\]

Claude's Theorem D proves, unconditionally,

\[
 N^s_0(T,2T)\ge(c_{\rm MT}-o(1))N(T,2T),
 \tag{L-90227.2}
\]

where the left side counts simple critical-line zeros and the right side counts
all nontrivial zeros with multiplicity.

The paper also proves the same lower bound for distinct critical-line zeros and
the lower bound

\[
 N_d(T,2T)\ge
 \left(\frac{1+c_{\rm MT}}2-o(1)\right)N(T,2T).
\]

Only (L-90227.2) is needed below.

## 2. Off-line pair budget

Let `p_T` be the number of distinct functional-equation pairs

\[
 \{\rho,1-\overline\rho\}
\]

with ordinate in `(T,2T]` and real part different from `1/2`. Every such pair
uses at least two units of the multiplicity count, while every simple on-line
zero uses one. Therefore

\[
 N(T,2T)\ge N^s_0(T,2T)+2p_T.
\]

Combining with (L-90227.2) gives

\[
 \boxed{
 p_T\le
 \left(\frac{1-c_{\rm MT}}2+o(1)\right)N(T,2T)
 =\left(0.163749648160\ldots+o(1)\right)N(T,2T).
 }
 \tag{L-90227.3}
\]

Thus Claude's `67.25%` theorem is equivalently a `16.375%` asymptotic upper
budget for local off-line hyperbolic planes.

## 3. Exact Weil-block interpretation

Let `V_T` be any finite-dimensional test space and let its zero-evaluation map
on a height window be

\[
 A_T:V_T\longrightarrow
 \mathbb C^{s_T}\oplus
 \bigoplus_{j=1}^{p_T}\mathbb C^2.
\]

In the exact centered Weil normalization of `L-15613`, the zero-coordinate
form is an orthogonal direct sum of

```text
one positive coordinate for every on-line zero;
one block m_j [[0,1],[1,0]] for every off-line pair.
```

Write the pullback as

\[
 W_T^{\rm loc}=P_T+Q_T,
 \qquad P_T\succeq0.
\]

Inertia under pullback gives

\[
 \boxed{
 n_+(Q_T)\le p_T,
 \qquad
 n_-(Q_T)\le p_T.
 }
 \tag{L-90227.4}
\]

Because adding a positive semidefinite form cannot increase the negative
index,

\[
 \boxed{
 n_-(W_T^{\rm loc})\le p_T.
 }
 \tag{L-90227.5}
\]

Combining (L-90227.3)--(L-90227.5),

\[
 \boxed{
 n_-(W_T^{\rm loc})
 \le(0.163749648160\ldots+o(1))N(T,2T).
 }
 \tag{L-90227.6}
\]

This applies to every coefficient realization of the same finite test space;
no orthogonality or independence of the evaluation vectors is required.

## 4. Tail-stable finite compression

Suppose a finite matrix `G_T` decomposes as

\[
 G_T=W_T^{\rm loc}+E_T,
 \qquad \|E_T\|_{\rm op}\le\theta_T.
\]

Let `n_{<-theta_T}(G_T)` count eigenvalues strictly below `-theta_T`. Weyl's
inequality gives

\[
 n_{<-\theta_T}(G_T)\le n_-(W_T^{\rm loc}).
\]

Hence

\[
 \boxed{
 n_{<-\theta_T}(G_T)
 \le(0.163749648160\ldots+o(1))N(T,2T).
 }
 \tag{L-90227.7}
\]

For Claude's critical-density Gabor family the coefficient dimension is
`d=(1+o(1))N(T,2T)`. Thus at least

\[
 (0.836250351839\ldots-o(1))N(T,2T)
\]

coefficient directions are not below the certified negative tail threshold.
This is the operator-language form of the paper's `83.625%` distinct-zero
constant.

## 5. Repository connection

The zero-side block in Claude's proof is exactly the block already resident in
`L-15613`:

```text
critical-line cardinal       -> positive coordinate;
off-line cardinal pair       -> one hyperbolic plane;
finite test compression       -> pullback of those blocks.
```

Claude's new contribution relative to that repository geometry is the global
rank--trace/Frobenius estimate and its unconditional prime-side evaluation.
It supplies a quantitative cofinal dimension budget for PRs #179, #186, and
#199, but it does not remove the residual off-line cardinal block.

## 6. Proof boundary

Imported:

- Claude's unconditional optimal-window bound (L-90227.2).

Proved here from that theorem and the resident exact block geometry:

- the off-line-pair budget (L-90227.3);
- the local positive/negative-index bounds;
- the tail-stable thresholded negative-index bound;
- the exact identification with the repository's Xi-cardinal defect.

Not proved:

- `p_T=0`;
- a vanishing negative-index theorem;
- positivity of a complete Weil form;
- RH.
