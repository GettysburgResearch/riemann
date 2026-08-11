# L-90428 — The fourteen-row phase-locked charge has a one-sided variation gate

Claim ID: `L-90428`  
Title: Every suffix of the phase-locked fourteen-row weight is negative, so the complete RH-bearing charge is controlled by one base reserve and one weighted downward variation of the first fifteen carry coefficients  
Status: **PROPOSED COMPLETE EXACT FINITE VARIATION THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: `L-90427`, `T-90421`; finite Abel summation  
Scope: a sufficient one-sign gate; it does not prove that the critical carry inverse satisfies the gate

## 1. Suffix geometry of the finite packet

Let `Y_*(n)` be the row weights from `L-90427.7` and put

\[
S_m=\sum_{n=m}^{15}Y_*(n),
\qquad 2\le m\le15,
\qquad S_{16}=0.
\tag{L-90428.1}
\]

Then

\[
\boxed{S_m<0\qquad(2\le m\le15).}
\tag{L-90428.2}
\]

Indeed every row from eight through fifteen is at most `-4`, so `S_8<=-32`. Adding the successive positive rows gives

```text
S_7 <= -32+3 <0,
S_6 <= -32+3+5 <0,
S_5 <  -32+3+5+8 <0,
S_4 <  -32+3+5+8+12 <0.
```

Rows three and two are negative, so their suffixes remain negative. This deliberately crude argument avoids a decimal table.

Put

\[
\sigma_*=-S_2>0.
\tag{L-90428.3}
\]

## 2. Exact Abel decomposition

For any real sequence `c(2),...,c(15)`, finite summation by parts gives

\[
\boxed{
\sum_{n=2}^{15}Y_*(n)c(n)
 =S_2c(2)+\sum_{m=3}^{15}S_m[c(m)-c(m-1)].
}
\tag{L-90428.4}
\]

Since every `S_m` is negative,

\[
\boxed{
\sum_{n=2}^{15}Y_*(n)c(n)
 \le
 -\sigma_*c(2)
 +\sum_{m=3}^{15}(-S_m)[c(m-1)-c(m)]_+.
}
\tag{L-90428.5}
\]

Define the weighted downward variation

\[
\boxed{
\mathcal V_*(c)
 =\sum_{m=3}^{15}(-S_m)[c(m-1)-c(m)]_+.
}
\tag{L-90428.6}
\]

Then the two scalar inequalities

\[
\boxed{
c(2)\ge0,
\qquad
\mathcal V_*(c)\le\sigma_*c(2)
}
\tag{L-90428.7}
\]

imply

\[
\boxed{
\sum_{n=2}^{15}Y_*(n)c(n)\le0.
}
\tag{L-90428.8}
\]

No sign is required for rows three through fifteen, and no monotonicity is assumed. Only the downward variation that can spend the bottom reserve is charged.

## 3. Phase-Locked Bottom Variation Gate

Apply the theorem to the critical hinge inverse `c_X` of `T-90421`.

> **PBVG.** Cofinally,
> \[
> c_X(2)\ge0,
> \qquad
> \mathcal V_*(c_X)\le\sigma_*c_X(2).
> \tag{L-90428.9}
> \]

Then the phase-locked finite charge satisfies

\[
\mathcal C_*(X)\le0
\tag{L-90428.10}
\]

cofinally.

Because the Mellin transform of `mathcal C_*` has no positive-real singularity but retains every hypothetical open-strip zeta-zero pole, the standard one-sign Landau theorem gives

\[
\boxed{\mathrm{PBVG}\Longrightarrow\mathrm{RH}.}
\tag{L-90428.11}
\]

This is a sufficient theorem, not an equivalence: RH need not imply eventual one-sign of the phase-locked charge.

## 4. Relation to the other finite variation routes

PBVG has the same stable form as the factor-64 occupation theorem, but its state is much smaller:

```text
factor-64 route:
    a long occupation sequence against a fixed signed reward;

phase-locked bottom route:
    fourteen fixed carry coefficients against a fixed signed reward.
```

The phase-locked adjoint has already compressed all rows above fifteen to zero. The remaining proof problem is therefore a cofinal bound for one weighted variation of a fixed finite prefix of the critical inverse.

## 5. Proof boundary

Closed exactly here:

1. negativity of every suffix weight;
2. exact Abel identity;
3. weighted downward-variation bound;
4. PBVG implies eventual one-sign;
5. eventual one-sign implies RH by the zero-safe Mellin consumer.

Open:

1. `c_X(2)>=0` cofinally;
2. the PBVG variation inequality;
3. RH.
