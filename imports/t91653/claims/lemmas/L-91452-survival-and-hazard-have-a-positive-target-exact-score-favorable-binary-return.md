# L-91452 — Survival and hazard have a positive target-exact, score-favorable binary canonical return

Claim ID: `L-91452`  
Status: **PROVED EXACT TWO-BRANCH LEDGER / CANONICAL-RETURN THEOREM**  
Created: 2026-08-12  
Depends on: `L-91335`–`L-91338`, `R-91307`  
RH status: **unproved**

## 1. One rough prime

Let

\[
 r=p^{-1/2},
 \qquad
 A=1-r^2,
 \qquad
 B=1-r,
 \qquad
 d=A-B=r(1-r)>0.
\tag{L-91452.1}
\]

Retain the positive survival return of `L-91338`,

\[
 C_p=
 \begin{pmatrix}
  A&2d/3\\
  0&(4B-A)/3
 \end{pmatrix},
\tag{L-91452.2}
\]

and define the positive hazard return

\[
\boxed{
 H_p=
 \begin{pmatrix}
  r^2&0\\
  0&r
 \end{pmatrix}.
}
\tag{L-91452.3}
\]

Both matrices are entrywise nonnegative for every prime `p`.

Write

\[
 t=(1,2),
 \qquad
 s=(2,1)
\tag{L-91452.4}
\]

for the SHARP target and endpoint-score rows.

## 2. Hazard target and the minimal physical score subsidy

The hidden least-prime hazard multipliers are

\[
 a=r^2,
 \qquad
 b=r.
\]

For a positive parent state `u=(L,R)^T`, the exact hidden hazard ledgers are

\[
 T_h=r^2L+2rR,
 \qquad
 S_h=r^2(2L+R).
\tag{L-91452.5}
\]

`R-91307` proves that these two numbers need not come from a positive physical
state. The matrix `H_p` preserves the target exactly and returns the hazard to
the positive state

\[
 H_pu=(r^2L,rR)^T.
\]

Its score is

\[
 sH_pu=2r^2L+rR
 =S_h+dR.
\tag{L-91452.6}
\]

Thus the exact score subsidy required for positive canonical return is

\[
\boxed{
 \Delta_p(u)=dR=r(1-r)R\ge0.
}
\tag{L-91452.7}
\]

On the pure reserve ray this is minimal: the hidden hazard target is `2rR`, so
any positive physical return has score at least `rR`, whereas the hidden score
is only `r^2R`.

## 3. Exact binary target partition

`L-91338` gives

\[
 tC_p=(A,2B),
 \qquad
 sC_p=(2A,A).
\tag{L-91452.8}
\]

The hazard matrix gives

\[
 tH_p=(r^2,2r),
 \qquad
 sH_p=(2r^2,r).
\tag{L-91452.9}
\]

Since `A+r^2=1` and `B+r=1`,

\[
\boxed{
 t(C_p+H_p)=t.
}
\tag{L-91452.10}
\]

Therefore every positive parent target splits exactly into one positive
survival target and one positive hazard-child target:

\[
\boxed{
 t u=tC_pu+tH_pu.
}
\tag{L-91452.11}
\]

There is no parent overdraw.

## 4. Score is favorable

Since

\[
 A+r=1+d,
\]

one has

\[
\boxed{
 s(C_p+H_p)=s+(0,d).
}
\tag{L-91452.12}
\]

Consequently

\[
\boxed{
 sC_pu+sH_pu=su+dR\ge su.
}
\tag{L-91452.13}
\]

The positive hazard subsidy is paid exactly by favorable local score. It is not
an inherited multiplicative debt.

Equivalently, for the signed loss `ell(u)=tu-su`,

\[
\boxed{
 \ell(C_pu)+\ell(H_pu)
 =\ell(u)-dR
 \le\ell(u).
}
\tag{L-91452.14}
\]

## 5. Sequential least-prime telescope

Let

\[
 p_1<p_2<\cdots<p_k
\]

be the ordered active rough primes. Put

\[
 S_0=I_2,
 \qquad
 S_j=C_{p_j}S_{j-1},
\]

and let the `j`-th hazard child be

\[
 Z_j=H_{p_j}S_{j-1}.
\tag{L-91452.15}
\]

Every matrix `S_j,Z_j` is nonnegative. Repeated use of
(L-91452.10) gives the exact target telescope

\[
\boxed{
 t=tS_k+\sum_{j=1}^ktZ_j.
}
\tag{L-91452.16}
\]

Hence, for every `u>=0`,

\[
\boxed{
 tu=tS_ku+\sum_{j=1}^ktZ_ju
}
\tag{L-91452.17}
\]

as a positive partition. The final survival packet and all least-prime hazard
children spend the target exactly once.

The score telescope is

\[
\boxed{
 sS_ku+\sum_{j=1}^ksZ_ju
 =su+\sum_{j=1}^kd_{p_j}(S_{j-1}u)_R
 \ge su.
}
\tag{L-91452.18}
\]

Thus the complete ordered rough-prime split is score-favorable.

## 6. Subprobability weights

If `tu>0`, define

\[
 \theta_\infty=\frac{tS_ku}{tu},
 \qquad
 \theta_j=\frac{tZ_ju}{tu}.
\]

Then

\[
\boxed{
 \theta_\infty+\sum_{j=1}^k\theta_j=1,
 \qquad
 \theta_\infty,\theta_j\ge0.
}
\tag{L-91452.19}
\]

Every nontrivial hazard packet with `p_j>=67` is placed at endpoint `x/p_j`,
strictly inside the next factor-54 scale. The final survival packet has no active
rough prime and belongs to the finite forcing/frontier channel.

Equation (L-91452.19) is the exact physical two-ledger replacement for the
blocked naive hazard normalization of `R-91307` and the independently
overdrawn one-prime children of `R-91305`.

## 7. Target-null correction

The total controlled split differs from the identity by

\[
\boxed{
 C_p+H_p-I_2
 =\frac d3
 \begin{pmatrix}
  0&2\\
  0&-1
 \end{pmatrix}.
}
\tag{L-91452.20}
\]

This correction lies in the kernel of the target row and improves the score:

\[
 t(C_p+H_p-I_2)=0,
 \qquad
 s(C_p+H_p-I_2)=(0,d).
\tag{L-91452.21}
\]

It is one third of the minimal SHARP-preserving positive completion isolated in
`L-91319`; hence it lies within the resident common innovation/endpoint-port
budget of `L-91333/L-91334`.

## 8. Remaining physical-row theorem

The theorem closes the state-level target partition, the hazard canonical
return, and the common score coefficient. To finish the factor-54 proof one
must lift the binary matrices `C_p,H_p` through the exact positive finite rows
of `L-91340/L-91341` and the affine child map, proving columnwise ordinary and
radix-four feasibility after the colors are summed and quantized once.

Because `C_p,H_p` are positive and the target identity is exact, this is now a
positive-functor/source-typing problem; no signed hazard state remains.

```text
positive survival return C_p                       EXACT
positive hazard return H_p                         EXACT
minimal hazard score subsidy                       EXACT
target-exact binary split                          EXACT
score-favorable binary split                       EXACT
ordered least-prime target telescope               EXACT
subprobability target weights                      EXACT
factor-54 placement of hazard children             EXACT
physical ordinary/radix-four row lift              OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVEN
```
