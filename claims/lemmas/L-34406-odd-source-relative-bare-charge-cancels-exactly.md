# L-34406 — Corrected aligned odd-source relative Jordan curvature

Claim ID: `L-34406`  
Status: **PROPOSED COMPLETE EXACT RELATIVE-CURVATURE THEOREM — CORRECTED AFTER R-90009; INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-09  
Corrected: 2026-08-09 by `gpt56-sol`  
Dependencies: `L-34404`; PR #345 `L-34404` vector-curvature pattern; `R-90009`; `L-90010`  
Scope: exact odd-prime relative state on aligned radix-four rows. The original bare-charge formula and uncentered zero claim were false; the cross-free curvature survives after the exact constant recentering below. No current upper bound or RH conclusion is claimed.

## 1. Odd source and reserve

Put
\[
B_{\rm odd}(s)=\prod_{p\ {m odd}}(1-p^{-s})
=\sum_{n\ge1}b_{\rm odd}(n)n^{-s},
\]
so
\[
b_{\rm odd}(n)=\mu(n)\mathbf1_{2\nmid n}.
\]
Its inverse has generalized-prime sequence
\[
\Lambda_{\rm odd}(n)=\Lambda(n)\mathbf1_{2\nmid n},
\]
and Selberg sequence
\[
C_{\rm odd}=\Lambda_{\rm odd}\log+
\Lambda_{\rm odd}*\Lambda_{\rm odd}.
\]
For one row `e=(n,j)`, write
\[
O(e)=\mathcal L_e(\Lambda_{\rm odd}),
\qquad
S(e)=\mathcal L_e(C_{\rm odd}),
\qquad
R_{\rm odd}(e)=O(e)^2-S(e).
\tag{L-34406.1}
\]
`L-34404` proves on every fixed balanced cone
\[
\Delta_4R_{\rm odd}(e)
:=R_{\rm odd}(4e)-16R_{\rm odd}(e)
=\Theta_\eta(n\log n)>0
\tag{L-34406.2}
\]
cofinally.

## 2. Correct bare-source carry

Since
\[
\mathbf1*b_{\rm odd}=\sum_{r\ge0}\delta_{2^r},
\]
the general prefix/carry identity gives
\[
Y_{\rm odd}(n,j)
=C_2(n)-C_2(j)-C_2(n-j),
\tag{L-34406.3}
\]
where
\[
C_2(0)=0,
\qquad
C_2(x)=1+\lfloor\log_2x\rfloor\quad(x\ge1).
\]
Thus for a nontrivial split `n=j+k`,
\[
\boxed{
Y_{\rm odd}(n,j)
=\lfloor\log_2n\rfloor
-\lfloor\log_2j\rfloor
-\lfloor\log_2k\rfloor-1.
}
\tag{L-34406.4}
\]
In particular
\[
\boxed{
Y_{\rm odd}(4n,4j)=Y_{\rm odd}(n,j)-2.
}
\tag{L-34406.5}
\]
The previous version's formulas
\[
Y_{\rm odd}=\sum_r\chi_{n,2^r}
\]
and
\[
Y_{\rm odd}(4e)=Y_{\rm odd}(e)
\]
were false; `R-90009` records the exact counterexample and correction.

At source level,
\[
(\varepsilon-\delta_4)*b_{\rm odd}
=(\varepsilon+\delta_2)*\mu,
\tag{L-34406.6}
\]
and the carry of `mu` on every nontrivial row is `-1`. Therefore
\[
\boxed{
\mathcal L_{4e}((\varepsilon-\delta_4)*b_{\rm odd})=-2.
}
\tag{L-34406.7}
\]

## 3. Odd Jordan deformation

Define
\[
J_{{\rm odd},\tau}(s)
=\frac{A_{\rm odd}(s-\tau)}{A_{\rm odd}(s)},
\qquad
K_{{\rm odd},\tau}=b_{\rm odd}*J_{{\rm odd},\tau}.
\tag{L-34406.8}
\]
Then
\[
J_0=\varepsilon,
\qquad J_0'=\Lambda_{\rm odd},
\qquad J_0''=C_{\rm odd},
\]
while
\[
K_0=b_{\rm odd},
\qquad K_0'=q_{\rm odd},
\qquad K_0''=t_{\rm odd}.
\]
Write
\[
Q_{\rm odd}(e)=\mathcal L_e(q_{\rm odd}).
\]

For the scalar relative coordinate put
\[
F_e(\tau)=1+\mathcal L_e(J_{{\rm odd},\tau}),
\]
\[
H_e^{(4)}(\tau)=\frac{F_{4e}(\tau)}{F_e(4\tau)}.
\tag{L-34406.9}
\]
Then
\[
H_e^{(4)}(0)=1
\]
and the standard Jordan calculation gives
\[
\boxed{
-\bigl(\log H_e^{(4)}\bigr)''(0)
=\Delta_4R_{\rm odd}(e).
}
\tag{L-34406.10}
\]

## 4. Correctly centered source-difference leg

The uncentered source difference has base value `-2`, not zero. Define instead
\[
\boxed{
\widetilde G_e^{(4)}(\tau)
=2+
\mathcal L_{4e}
\bigl((\varepsilon-\delta_4)*K_{{\rm odd},\tau}\bigr).
}
\tag{L-34406.11}
\]
By (L-34406.7),
\[
\boxed{
\widetilde G_e^{(4)}(0)=0.
}
\tag{L-34406.12}
\]
The constant `2` has zero derivatives, hence
\[
\boxed{
(\widetilde G_e^{(4)})'(0)
=Q_{\rm odd}(4e)-Q_{\rm odd}(e)
=:I_{\rm odd}^{(4)}(e).
}
\tag{L-34406.13}
\]
The second derivative is unchanged but does not enter the curvature because the zeroth source coordinate vanishes.

Put
\[
\widetilde W_e^{(4)}(\tau)
=\bigl(H_e^{(4)}(\tau),\widetilde G_e^{(4)}(\tau)\bigr).
\]
For
\[
\mathfrak C(W)=\|W'(0)\|^2-
\operatorname{Re}\langle W(0),W''(0)\rangle,
\]
we obtain the exact corrected identity
\[
\boxed{
\mathfrak C(\widetilde W_e^{(4)})
=\Delta_4R_{\rm odd}(e)
+|I_{\rm odd}^{(4)}(e)|^2.
}
\tag{L-34406.14}
\]
Thus the desired absence of a bare-times-second-current cross is real, but it comes from an **explicit constant centering**, not from scale-four invariance of the odd bare carry.

## 5. Scale two is the finer state

`L-90010` proves the stronger scale-two decomposition
\[
\Delta_2R_{\rm odd}(e)
=R_{\rm odd}(2e)-4R_{\rm odd}(e)
=\Theta_\eta(n\log n)>0
\tag{L-34406.15}
\]
cofinally, together with the centered cross-free state
\[
\mathfrak C(W_e^{(2)})
=\Delta_2R_{\rm odd}(e)
+|Q_{\rm odd}(2e)-Q_{\rm odd}(e)|^2.
\tag{L-34406.16}
\]
Moreover
\[
\boxed{
\Delta_4R_{\rm odd}(e)
=\Delta_2R_{\rm odd}(2e)+4\Delta_2R_{\rm odd}(e).
}
\tag{L-34406.17}
\]
Thus the scale-four state in this file is best viewed as the two-step aggregate of the finer doubling ledger.

## 6. Relation to the compact source

The compact source still factors exactly as
\[
B_\circ(s)=T(2^{-s})B_{\rm odd}(s),
\qquad
T(z)=(1-z)(1-4z^2),
\tag{L-34406.18}
\]
so
\[
q_\circ=Tq_{\rm odd}+T'b_{\rm odd}.
\tag{L-34406.19}
\]
`L-90010` resolves this on a fully aligned dyadic chain into two scale-two current innovations plus an explicit logarithmic bare gauge. This is the preferred recurrence coordinate after the present correction.

## 7. Boundary

Corrected and retained:

```text
odd-prime reserve and its scale-four critical moat
the positive odd Jordan deformation
cross-free scale-four vector curvature after +2 centering
compact source factorization over the odd carrier
```

Removed as false:

```text
Y_odd = sum of dyadic carry columns
Y_odd >= 0
Y_odd(4e)=Y_odd(e)
uncentered source-difference leg has zero base value
```

Strengthened in `L-90010`:

```text
fresh critical moat at every doubling
cross-free centered scale-two vector state
exact compact-current two-tap routing through scale-two innovations
```

Still open:

```text
upper/dissipative law for the centered relative curvature
lossless coefficient-one two-state recurrence
subpower current energy
RH
```