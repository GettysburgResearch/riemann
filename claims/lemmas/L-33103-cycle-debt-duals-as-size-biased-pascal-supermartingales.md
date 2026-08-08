# L-33103 — Cycle-Debt duals are size-biased Pascal supermartingales

Claim ID: `L-33103`  
Title: The bounded-superadditive dual cone becomes a bounded-drift supermartingale cone under the exact size-biased Pascal child chain  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Issue: #331  
Dependencies: PR #272 `L-27205`; `L-33102`  
Scope: exact finite dual/probability bridge; no cofinal estimate and no RH conclusion

## 1. Cycle-Debt dual

Fix an allowed balanced split

\[
n=j+(n-j).
\]

PR #272's optimized Cycle-Debt dual uses real potentials `F` satisfying

\[
\boxed{
0\le
F(n)-F(j)-F(n-j)
\le \omega_{n,j},
}
\tag{L-33103.1}
\]

where

\[
\omega_{n,j}
=
\sum_{q=2}^{n}\frac{\chi_{n,j}(q)}{\sqrt q}>0.
\]

The lower inequality is balanced superadditivity; the upper inequality is the capacity normalization.

## 2. Normalize by conserved parent mass

Put

\[
f(n)=\frac{F(n)}n
\qquad(n\ge1).
\]

For the fixed split, choose a child by following a uniformly selected unit of parent mass. Thus

\[
K=
\begin{cases}
 j,&\text{with probability }j/n,\\
 n-j,&\text{with probability }(n-j)/n.
\end{cases}
\]

Then

\[
\begin{aligned}
\mathbb E[f(K)\mid n,j]
&=\frac jn\frac{F(j)}j
 +\frac{n-j}{n}\frac{F(n-j)}{n-j}\\
&=\frac{F(j)+F(n-j)}n.
\end{aligned}
\]

Consequently (L-33103.1) is exactly

\[
\boxed{
0\le
f(n)-\mathbb E[f(K)\mid n,j]
\le\frac{\omega_{n,j}}n.
}
\tag{L-33103.2}

Thus every Cycle-Debt dual potential becomes a supermartingale observable under every allowed size-biased split, with an explicit capacity drift.

## 3. Uniform split and the finite Beta state

Now choose `J` uniformly from `0,...,n` and then choose the size-biased child. `L-33102` proves that the resulting child satisfies

\[
\mathbb P(K=k)=\frac{2k}{n(n+1)},
\qquad1\le k\le n.
\tag{L-33103.3}

Averaging (L-33103.2) over `J` gives

\[
\boxed{
0\le
f(n)-\mathbb E[f(K)\mid n]
\le
\frac1{n(n+1)}
\sum_{j=0}^{n}\omega_{n,j}.
}
\tag{L-33103.4}

If only a fixed balanced subwindow is permitted, the same identity holds after conditioning `J` to that subwindow and renormalizing its uniform law.

## 4. Elementary drift bound

For every split,

\[
\omega_{n,j}
\le
\sum_{q=2}^{n}q^{-1/2}
<2\sqrt n.
\]

Therefore

\[
\boxed{
0\le
f(n)-\mathbb E[f(K)\mid n]
<\frac{2}{\sqrt n}.
}
\tag{L-33103.5}

The bound is deliberately crude but uniform and source free. It shows that every normalized dual obstruction becomes asymptotically harmonic for the exact finite Pascal child chain.

## 5. Two-step Gamma scaling state

Apply two independent uniform size-biased splits. In the scaling limit the two child fractions converge to independent `Beta(2,1)` variables `U,V`; `L-33102` identifies

\[
G=-4\log(UV)
\sim\operatorname{Gamma}(2,1/2).
\]

Thus the same two-step fragmentation state which produces the sharp Gamma law is precisely the Markov chain on which every normalized Cycle-Debt dual is asymptotically superharmonic.

This is the dual reason `L-33101` is relevant to the finite carry cone rather than merely a probability curiosity.

## 6. Exact critical-mode firewall

The supermartingale drift does **not** by itself prove Cycle Debt is small. The critical correction

\[
f(n)=c-dn^{-1/2}
\]

has scale

\[
n^{-1/2}
\]

and the `Beta(2,1)` child law satisfies

\[
\mathbb E[V^{-1/2}]
=\int_0^1 2v^{1/2}dv
=\frac43.
\]

Hence

\[
f(n)-\mathbb E f(nV)
=\frac d{3\sqrt n}
\]

when `d>0`, exactly at the capacity-drift scale. The dangerous square-root mode is therefore *not* removed by generic harmonicity. A valid completion must control its source pairing, not merely prove compactness of normalized duals.

This is the dual analogue of the eta zero-mode firewall on PR #323.

## 7. Consequence for the Martingale Pascal Lift

The finite lift can now be reviewed equivalently from either side:

### Primal
Construct state-resolved Pascal cycles which realize the centered carry-to-Gamma martingale with subpower negative capacity debt.

### Dual
Prove that every bounded-drift size-biased Pascal supermartingale satisfying (L-33103.2) pairs with the actual Möbius divergence by at most `X^o(1)` after the linear conserved mode is removed.

The second formulation exposes the exact remaining arithmetic obstruction. It also prevents a false conclusion from the continuum convex-order theorem alone.

## 8. Proof boundary

Established here:

1. exact equivalence between balanced superadditivity and size-biased supermartingale drift;
2. exact capacity upper drift;
3. exact finite `2k/[n(n+1)]` child law;
4. uniform `O(n^-1/2)` drift;
5. the square-root critical-mode mutation.

Open:

1. a source-specific bound for the critical dual pairing;
2. the cofinal finite Martingale Pascal Lift;
3. RH.
