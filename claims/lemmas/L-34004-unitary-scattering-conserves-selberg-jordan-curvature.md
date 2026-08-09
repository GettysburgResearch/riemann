# L-34004 — Unitary Q=4 scattering conserves the Selberg–Jordan curvature exactly

Claim ID: `L-34004`  
Title: Any parameter-independent unitary colligation conserves `||f'||^2-Re<f,f''>` channel by channel; for the Q=4 Jordan path this is exactly the source-complete augmented Selberg curvature  
Status: **PROPOSED COMPLETE EXACT HILBERT-SPACE LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #325 `L-32406` unitary Q=4 scattering; PR #337 `L-32711`; PR #339 positive Jordan deformation  
Scope: exact curvature conservation; no sign theorem for the terminal state and no RH conclusion

## 1. A unitary curvature identity

Let `H_1,H_2` be Hilbert spaces and let

\[
 U:H_1\oplus H_2\to H_1\oplus H_2
\]

be unitary and independent of a real deformation parameter `tau`.
Suppose

\[
 \binom{x_+(\tau)}{y(\tau)}
 =U\binom{x(\tau)}{u(\tau)}
\tag{L-34004.1}
\]

with twice differentiable Hilbert-valued paths.

For any such path put

\[
\boxed{
 \mathfrak C(f)
 =\|f'(0)\|^2
  -\operatorname{Re}\langle f(0),f''(0)\rangle.
}
\tag{L-34004.2}
\]

Because `U` is parameter independent, differentiation of (L-34004.1) gives the same unitary map on the zeroth, first, and second jets. Hence

\[
 \|x_+'\|^2+\|y'\|^2
 =\|x'\|^2+\|u'\|^2
\]

and

\[
 \operatorname{Re}\langle x_+,x_+''\rangle
 +\operatorname{Re}\langle y,y''\rangle
 =\operatorname{Re}\langle x,x''\rangle
 +\operatorname{Re}\langle u,u''\rangle.
\]

Subtracting gives the exact conservation law

\[
\boxed{
 \mathfrak C(x_+)+\mathfrak C(y)
 =\mathfrak C(x)+\mathfrak C(u).
}
\tag{L-34004.3}
\]

This is distinct from the ordinary second derivative of energy, which contains a plus sign in front of `Re<f,f''>`.

## 2. Q=4 scattering specialization

For Q=4, PR #325 `L-32406` gives the exact slabwise unitary colligation

\[
\binom{x_{k+1}}{y_k}
=
\begin{pmatrix}
1/2&\sqrt3/2\\
-\sqrt3/2&1/2
\end{pmatrix}
\binom{x_k}{u_k}.
\tag{L-34004.4}
\]

Apply the same colligation simultaneously to the complete Q=4 Jordan deformation parameter `tau`. Then for every slab

\[
\boxed{
 \mathfrak C(x_{k+1})+\mathfrak C(y_k)
 =\mathfrak C(x_k)+\mathfrak C(u_k).
}
\tag{L-34004.5}
\]

Summing through a finite block range telescopes the state curvature:

\[
\boxed{
 \sum_{k=0}^{K-1}\mathfrak C(u_k)
 =\sum_{k=0}^{K-1}\mathfrak C(y_k)
  +\mathfrak C(x_K)-\mathfrak C(x_0).
}
\tag{L-34004.6}
\]

For the causal realization `x_0=0`, the last term is just the terminal-state curvature.

## 3. Identification with the row Selberg–Jordan curvature

PR #337 `L-32711` defines on one Q=4 binary carry row

\[
 v_e(\tau)
 =\bigl(1+\mathcal L_e(J_{4,\tau}),\;
        \mathcal L_e(K_{4,\tau})\bigr),
\]

with

\[
 v_e(0)=(1,Y_e),
 \quad
 v_e'(0)=(P_e,Q_e),
 \quad
 v_e''(0)=(S_e,T_e).
\]

Applying (L-34004.2) in `C^2` gives exactly

\[
\boxed{
 \mathfrak C(v_e)
 =P_e^2-S_e+Q_e^2-Y_eT_e
 =R_e+Q_e^2-Y_eT_e
 =\mathcal A_e.
}
\tag{L-34004.7}
\]

By `L-34001`, `Q_e` is the true integer Q=4 physical current. Therefore the source-complete augmented reserve `A_e` is not an ad hoc quadratic correction: it is the unitary-invariant Jordan curvature naturally transported by the Q=4 scattering system.

## 4. Continuous augmented cells

PR #326 `L-32412` proves that continuous carry-position localization at integer physical parent `N` is an exact uniform nonnegative measure on augmented binary rows. The same bilinear identity applies to the zeroth, first, and second Jordan jets.

Consequently the carry-position averaged curvature is the nonnegative row average of the augmented versions of (L-34004.7). No independent-frequency diagonal collapse is required to identify the arithmetic curvature.

## 5. What would close the neutral recurrence

Equations (L-34004.5)--(L-34004.7) show that the coefficient-one neutral state has an exact curvature ledger:

```text
incoming principal Jordan curvature
 = current Q=4 output curvature
   + terminal scattering curvature
   - incoming state curvature.
```

The current-output row curvature is cofinally positive by `L-32711` and the augmented-cell corrections are negligible relative to the Q=4 reserve by `L-32412`.

Therefore a proof that the terminal scattering state has nonnegative curvature, or more generally that its negative curvature is bounded by a fixed finite-delay predecessor ledger, would yield a genuine coefficient-one recurrence without trying to contract the zeta-zero mode.

That terminal-state sign/bound is **not proved here**. Cross terms among the geometrically weighted predecessor inputs must be retained.

## 6. Proof boundary

Closed exactly:

1. unitary conservation of `mathfrak C`;
2. slabwise and finite-prefix Q=4 curvature identities;
3. identification of the row curvature with `R+Q^2-YT`;
4. compatibility with the augmented binary-row placement theorem.

Open:

1. sign or delayed bound for the terminal scattering curvature;
2. the resulting coefficient-one block recurrence;
3. RH.
