# L-34404 — The relative Q=4 innovation is one vector Jordan curvature

Claim ID: `L-34404`  
Title: The radix-four reserve increment and the true compact source-current innovation are the two coordinates of one exact relative Jordan path whose curvature is precisely the positive augmented innovation curvature  
Status: **PROPOSED COMPLETE EXACT VECTOR-JORDAN THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #345 `L-34402`; PR #342 `L-34003/L-34005/L-34006`; PR #339 `L-33802`  
Scope: exact relative vector path and curvature; no upper bound for the innovation and no RH claim

## 1. Q=4 row partition and relative scalar coordinate

For a balanced row

\[
 e=(n,j),\qquad e^+=(4n,4j),
\]

retain the positive Q=4 Jordan row partition

\[
 F_e(\tau)=1+\mathcal L_e(J_{4,\tau}).
\]

PR #345 defines

\[
\boxed{
 H_e(\tau)=\frac{F_{e^+}(\tau)}{F_e(4\tau)}.
}
\tag{L-34404.1}
\]

At the origin,

\[
H_e(0)=1,
\tag{L-34404.2}
\]

\[
\boxed{
 H_e'(0)=E_e
 :=P_4(e^+)-4P_4(e),
}
\tag{L-34404.3}
\]

and

\[
\boxed{
 -\bigl(\log H_e\bigr)''(0)
 =\Delta_4R(e)
 :=R_4(e^+)-16R_4(e).
}
\tag{L-34404.4}
\]

Since `H_e(0)=1`, equation (L-34404.4) is equivalently

\[
\boxed{
 H_e''(0)=E_e^2-\Delta_4R(e).
}
\tag{L-34404.5}
\]

Thus the first coordinate already carries the complete critical-scale deterministic moat.

## 2. Compact source-difference Jordan leg

Retain

\[
 K_{4,\tau}=b_4*J_{4,\tau}.
\]

Define the one-step source difference

\[
\boxed{
 K_{\circ,\tau}
 :=(\varepsilon-\delta_4)*K_{4,\tau}.
}
\tag{L-34404.6}
\]

and evaluate it on the scaled row:

\[
\boxed{
 G_e(\tau)
 :=\mathcal L_{e^+}(K_{\circ,\tau}).
}
\tag{L-34404.7}
\]

At `tau=0`,

\[
 K_{\circ,0}
 =(\varepsilon-\delta_4)*b_4
 =b_\circ,
\]

so

\[
\boxed{G_e(0)=Y_\circ(e).}
\tag{L-34404.8}
\]

Differentiating (L-34404.6) coefficientwise gives

\[
 K_{\circ,\tau}'|_0
 =(\varepsilon-\delta_4)q_4
 =:i_\circ,
\tag{L-34404.9}
\]

where `i_circ` is the actual Q=4 scale-innovation source of PR #342/PR #345, not the own compact current `q_circ` before its delayed bare gauge is removed.

The aligned carry scaling identity gives

\[
 \mathcal L_{e^+}(\delta_4*q_4)
 =\mathcal L_e(q_4).
\]

Hence

\[
\boxed{
 G_e'(0)
 =Q_4^{\rm phys}(e^+)-Q_4^{\rm phys}(e)
 =I_\circ(e).
}
\tag{L-34404.10}
\]

Likewise put

\[
 T_\circ(e)
 :=\mathcal L_{e^+}
   ((\varepsilon-\delta_4)t_4).
\]

Then

\[
\boxed{G_e''(0)=T_\circ(e).}
\tag{L-34404.11}
\]

This is exactly the source second-current coordinate used in the compact innovation ledger.

## 3. The relative vector path

Define

\[
\boxed{
 W_e(\tau)
 =\bigl(H_e(\tau),G_e(\tau)\bigr)
 \in\mathbf R^2
}
\tag{L-34404.12}
\]

for real `tau` in a neighborhood of zero (or in `C^2` with real parts in the curvature below).

Its first three jets are therefore

\[
\boxed{
 W_e(0)=(1,Y_\circ),
}
\tag{L-34404.13}
\]

\[
\boxed{
 W_e'(0)=(E_e,I_\circ),
}
\tag{L-34404.14}
\]

and

\[
\boxed{
 W_e''(0)
 =(E_e^2-\Delta_4R,\;T_\circ).
}
\tag{L-34404.15}
\]

No term in these formulas is introduced for bookkeeping: both coordinates are explicit finite Jordan/source objects.

## 4. Exact curvature identity

For a twice differentiable Hilbert-valued path define

\[
 \mathfrak C(W)
 =\|W'(0)\|^2
  -\operatorname{Re}\langle W(0),W''(0)\rangle.
\tag{L-34404.16}
\]

Insert (L-34404.13)--(L-34404.15):

\[
\begin{aligned}
\mathfrak C(W_e)
&=E_e^2+I_\circ^2
 -\left[E_e^2-\Delta_4R+Y_\circ T_\circ\right]\\
&=\boxed{
 \Delta_4R(e)+I_\circ(e)^2-Y_\circ(e)T_\circ(e).
}
\end{aligned}
\tag{L-34404.17}
\]

Thus

\[
\boxed{
 \mathfrak C(W_e)=\mathcal A_\circ(e),
}
\tag{L-34404.18}
\]

where `A_circ` is exactly the positive augmented one-step innovation curvature of PR #342.

This explains why the reserve increment, current square, and second-current/bare-source cross always occur together: they are the three pieces of one vector Jordan curvature.

## 5. Cofinal positivity and scale

PR #342 proves uniformly on the quarter-balanced cone, outside a finite base,

\[
\Delta_4R=\Theta(n\log n),
\]

\[
Y_\circ T_\circ=O(n),
\]

and hence

\[
\boxed{
 \mathfrak C(W_e)
 =\mathcal A_\circ(e)
 \ge I_\circ(e)^2+\frac12\Delta_4R(e)>0.
}
\tag{L-34404.19}
\]

The positivity is therefore the curvature sign of one relative path, not an inequality obtained by separately paying three source terms.

## 6. Interaction with the scalar two-parameter no-go

`L-34403` constructs the natural positive Q=4-to-compact two-parameter scalar Jordan partition and proves that its source coordinate is flat at `tau=0`; consequently its scalar negative log-Hessian is indefinite whenever the four-adic carry is active.

The present theorem identifies the missing coordinate: the source-convolved leg `G_e`.  It supplies the nontrivial source zeroth, first, and second jets

\[
Y_\circ,\quad I_\circ,\quad T_\circ
\]

which cannot appear in the scalar partition.

Therefore the correct final Schur/Fisher object is necessarily vector/Hermitian and must act on `W_e` or an equivalent source-complete Gram.

## 7. What remains

The formerly vague task

```text
construct a two-parameter source-complete state containing
Delta_4R and I_circ
```

is now closed at exact one-parameter vector scope: both quantities are jets of `W_e`, and `A_circ` is its exact curvature.

A conclusion-producing theorem still has to give an **upper/dissipative** law for this positive curvature, for example a fixed-delay estimate whose iteration implies

\[
 I_\circ(e)^2=O(n\log^A n).
\]

Positivity of `A_circ` alone is not such an upper bound.

The preferred next attack is therefore:

```text
find a parameter-independent colligation/frame for the relative vector W_e,
or a relative Gram whose Schur complement is A_circ,
so that curvature conservation yields a coefficient-one delayed recurrence.
```

This is strictly narrower than the prior scalar innovation-domination formulation.

## 8. Proof boundary

Closed exactly here:

1. relative Q=4 Jordan ratio coordinate;
2. compact source-difference Jordan leg;
3. exact first three jets of both coordinates;
4. identification of the true aligned current innovation `I_circ`;
5. exact vector curvature identity `C(W)=A_circ`;
6. compatibility with the cofinal critical-scale moat and lower-order source cross.

Still open:

1. a dissipative colligation/relative Gram for `W_e`;
2. an upper fixed-delay recurrence for `A_circ`;
3. subpower pole-current energy;
4. RH.
