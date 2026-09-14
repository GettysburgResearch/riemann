# L-106442 — A causal inner factor cannot worsen the signed hard-band tail

Claim ID: `L-106442`  
Status: **PROVED EXACT HARDY/TOEPLITZ THEOREM**  
Created: 2026-08-25  
Depends on: `L-105625`, `L-105632`, `L-106440`  
RH status: **not assumed**

Let `V` be inner in the upper half-plane and let `W` be unimodular, with all
Hankel differences below trace class on the declared regularized scope.  Put

\[
S=T_V,
\qquad
U=VW.
\]

Since `V` is analytic,

\[
T_U=ST_W,
\]

and `S` is a causal isometry.

For a unimodular symbol `A`, define the signed Hankel commutator

\[
\mathcal C(A)
 =H_A^*H_A-H_{\overline A}^*H_{\overline A}
 =T_AT_A^*-T_A^*T_A.
\tag{L-106442.1}
\]

Let

\[
Y=H_{\overline W}^*H_{\overline W}\succeq0,
\qquad
Z=H_W^*H_W\succeq0.
\]

Then

\[
T_WT_W^*=I-Y,
\qquad
T_W^*T_W=I-Z.
\]

## 1. Exact product cocycle

Direct substitution gives

\[
\begin{aligned}
\mathcal C(VW)
&=S(I-Y)S^*-(I-Z)\\
&=-P_{K_V}-SYS^*+Z,
\end{aligned}
\]

where

\[
P_{K_V}=I-SS^*
\]

is the model-space projection of `V`.  Since

\[
\mathcal C(W)=Z-Y,
\]

one obtains the exact cocycle

\[
\boxed{
\mathcal C(VW)-\mathcal C(W)
 =-P_{K_V}+Y-SYS^*.
}
\tag{L-106442.2}

Both correction terms have a favorable interpretation:

```text
-P_(K_V):          the topological inner-model contribution;
Y-SYS*:            the causal delay of the favorable Hankel channel.
```

## 2. Hard-band monotonicity

Let `P_H` be the prefix projection onto frequencies `[0,H]` and
`Q_H=I-P_H`.  Causality gives

\[
S^*P_HS\preceq P_H.
\tag{L-106442.3}

Because `Y` is trace class and `S` is an isometry,

\[
\operatorname{tr}(Y-SYS^*)=0.
\]

Therefore

\[
\begin{aligned}
\operatorname{tr}Q_H(Y-SYS^*)Q_H
&=-\operatorname{tr}P_H(Y-SYS^*)P_H\\
&=-\operatorname{tr}Y(P_H-S^*P_HS)\\
&\le0.
\end{aligned}
\tag{L-106442.4}

Taking the localized trace of (L-106442.2) gives

\[
\boxed{
\Delta_H^{\rm out}(VW)
\le
\Delta_H^{\rm out}(W).
}
\tag{L-106442.5}

Thus a source-exact inner factor may be removed from the **outer signed
spectral tail** with no loss and no unspecified Toeplitz commutator.  The
commutator is explicitly nonpositive.

The same proof applies to any projection `P` satisfying

\[
S^*PS\preceq P.
\]

## 3. What does not follow

A general finite source projection inside the hard band need not obey
`S^*PS<=P`.  Consequently (L-106442.5) does not automatically control the
in-band hole `Delta_(H,P)^hole` of `L-106440.9`.  For that term one must prove
source invariance, enlarge to a causal prefix bank, or retain the finite signed
commutator explicitly.

Likewise, the theorem requires an exact factorization `U=VW` with `V` inner.
Norm closeness to a vertical-shift inner function does not supply such a
factorization.

## 4. Xi consequence

Once the safe vertical-shift Xi-prime factor from PR #729 is identified as a
literal left inner factor of the endpoint companion, (L-106442.5) removes it
completely from `OUTASYM106440`.  The outer estimate then concerns only the
unsafe residual divisor.  The remaining bridge is source/divisor exactness,
not a hard-tail product inequality.