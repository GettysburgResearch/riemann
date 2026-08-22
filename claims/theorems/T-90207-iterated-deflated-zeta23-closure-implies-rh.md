# T-90207 — Residual stability of the Claude Zeta23 certificate would imply RH by geometric deflation

Claim ID: `T-90207`  
Status: **FULL CONDITIONAL PROPOSAL — ONE RESIDUAL MOMENT-STABILITY THEOREM OPEN; INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: Claude Zeta23 rank--trace seam; exact positive line-zero deflation `L-15614`; geometric exhaustion `L-90229`  
Scope: cofinal dyadic zero packets plus a finite low-height verification; RH is not claimed

## 1. Exact residual Weil form

Fix a large dyadic height window

\[
 I_T=(T,2T]
\]

and let `W_(T,0)` be the corresponding localized Weil form, including the
declared far-zero tail treatment.

At stage `j`, let `D_(T,<j)` be the union of the previously selected simple
critical-line zeros and define the exact positively deflated form

\[
 W_{T,j}
 =W_{T,0}
 -\sum_{\gamma\in D_{T,<j}}
   u_\gamma u_\gamma^*.
 \tag{T-90207.1}
\]

By `L-15614`, the removed coordinates become exact radicals and every residual
line-zero or off-line cardinal block is unchanged.

Let `N_(T,j)` be the residual zero multiplicity in the window.

## 2. The missing residual Zeta23 closure

> **Iterated Deflated Zeta23 stability (`IDZ23`).** There is a quantity
> `eta(T)->0` such that, for every sufficiently large `T` and every stage
> `j` with `N_(T,j)>0`, one can construct a finite compression `G_(T,j)` of
> `W_(T,j)` satisfying the same zero-side block/tail hypotheses as Claude's
> compression and
> \[
> \operatorname{tr}G_{T,j}
> \ge(1-\eta(T))N_{T,j},
> \tag{IDZ23.1}
> \]
> \[
> \|G_{T,j}\|_F^2
> \le\left(\frac1{c_1^*}+\eta(T)\right)N_{T,j},
> \tag{IDZ23.2}
> \]
> with the complete tail and normalization loss bounded by
> `eta(T)N_(T,j)`, uniformly for all
> \[
> 0\le j\le C\log N(T,2T)
> \]
> for one fixed sufficiently large `C`.

Here

\[
 c_1^*
 =\frac{\sqrt2\tan(1/\sqrt2)}
 {1+(1/\sqrt2)\tan(1/\sqrt2)}.
\]

The original Claude theorem proves the stage `j=0`. `IDZ23` asks for stability
under exact selected-line-zero deflation.

## 3. One residual stage

Let `s_(T,j)` be the number of residual simple critical-line zeros. Claude's
multiplicity-aware rank--trace argument, applied to `G_(T,j)`, gives

\[
 s_{T,j}
 \ge4\operatorname{tr}G_{T,j}
   -\|G_{T,j}\|_F^2
   -2N_{T,j}
   -\eta(T)N_{T,j}.
\]

Using (IDZ23.1)--(IDZ23.2),

\[
\begin{aligned}
 s_{T,j}
 &\ge
 \left[
 4(1-\eta(T))
 -\left(\frac1{c_1^*}+\eta(T)\right)
 -2-\eta(T)
 \right]N_{T,j}\\
 &=\left(c_{\rm MT}-6\eta(T)\right)N_{T,j},
\end{aligned}
 \tag{T-90207.2}
\]

where

\[
 c_{\rm MT}=2-\frac1{c_1^*}=0.672500703679\ldots .
\]

For large `T`, take `eta(T)<=c_MT/12`. Then

\[
 \boxed{
 s_{T,j}\ge\frac{c_{\rm MT}}2N_{T,j}.
 }
 \tag{T-90207.3}
\]

Choose that many residual simple line zeros and deflate them.

## 4. Geometric exhaustion

Equation (T-90207.3) and `L-90229` give

\[
 N_{T,j+1}
 \le\left(1-\frac{c_{\rm MT}}2\right)N_{T,j}.
\]

After

\[
 K_T>
 \frac{\log N(T,2T)}
 {-\log(1-c_{\rm MT}/2)}
 \tag{T-90207.4}
\]

stages, the residual count is a nonnegative integer strictly below one.
Therefore

\[
 \boxed{N_{T,K_T}=0.}
 \tag{T-90207.5}
\]

Every zero in `(T,2T]` was a simple critical-line coordinate selected at some
stage. In particular there was no off-line pair.

The required number of stages is `O(log T)`, within the uniform range demanded
by `IDZ23`.

## 5. RH conclusion

Assume `IDZ23` for every sufficiently large dyadic height window. Then every
sufficiently high nontrivial zeta zero lies on the critical line.

Add a proof-grade finite verification of RH below the resulting height
threshold. Functional-equation symmetry then gives

\[
 \boxed{\mathrm{IDZ23}+\text{finite low-height verification}
 \Longrightarrow\mathrm{RH}.}
 \tag{T-90207.6}
\]

## 6. Why this is a genuine use of Claude's theorem

A one-shot rank proportion tolerates a sparse off-line sector. Iteration removes
the certified positive sector and forces the same theorem to act on the
residual. A single off-line pair cannot hide through `O(log N)` geometric
peelings.

This route does not amplify the pair's index and therefore does not violate
`L-90228`. It repeatedly removes positive coordinates until any residual pair
would be the whole packet.

## 7. Exact missing analytic quantity

For one deflation matrix `P_j>=0`,

\[
 G_{j+1}=G_j-P_j,
\]

so

\[
 \operatorname{tr}G_{j+1}
 =\operatorname{tr}G_j-\operatorname{tr}P_j,
\]

and

\[
 \|G_{j+1}\|_F^2
 =\|G_j\|_F^2+\|P_j\|_F^2
  -2\operatorname{tr}(G_jP_j).
 \tag{T-90207.7}
\]

The first stage does not control the cross term

\[
 \operatorname{tr}(G_jP_j).
\]

A production proof of `IDZ23` must show that a large proof-grade line-zero
block can be selected so that the deflated trace and Frobenius ratio retain the
Zeta23 bound, uniformly through `O(log T)` stages.

This is precisely a selected-zero-kernel / weighted-deficit stability theorem,
connecting to PRs #163, #179, and #186.

## 8. Stronger but simpler sufficient forms

Any one of the following would imply `IDZ23`:

1. **Deflated prime-side replay:** an explicit-formula evaluation of
   `tr G_(T,j)` and `tr G_(T,j)^2` with the bounds above after every selected
   deflation.
2. **Cross-term domination:** a selection theorem giving
   \[
   2\operatorname{tr}(G_jP_j)
   \ge\|P_j\|_F^2
     +\frac1{c_1^*}\operatorname{tr}P_j
     -o(N_{T,j}).
   \]
3. **Kernel moment stability:** the evaluation-kernel compression after
   positive deflation has normalized second trace at most `c_1^{*-1}+o(1)`.
4. **Exact recursive carrier frame:** a source-complete Gabor/carrier subspace
   for the residual zero packet with the original Poisson and
   Montgomery--Vaughan moment laws.

None is proved here.

## 9. Proof boundary

Closed exactly:

- the residual positive-deflation algebra;
- one-stage deduction from residual moments;
- geometric `O(log N)` exhaustion;
- the conditional implication to RH.

Open:

- `IDZ23` beyond stage zero;
- uniform selected-line-block moment stability;
- RH.
