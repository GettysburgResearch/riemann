# L-91883 — One coefficient ledger controls target, score, rows, `q/4q`, detail and `Y_4`

Claim ID: `L-91883`  
Status: **PROVED FORMAL COEFFICIENT-FIDELITY THEOREM; LIVE INPUTS FROZEN**  
Created: 2026-08-16  
Depends on: `L-91882`, `L-93783`, exact linear response maps  
RH status: **unproved**

## 1. Coefficient record

Every positive output record has a single scalar coefficient:

```text
bulk residual:
    tau_K * (2/s) * r_s(e) ds;

anchored residual or bonus:
    tau_K * omega_X;

terminal residual source:
    additionally carries (1-u_(omega,e));

terminal used source:
    carries u_(omega,e) only inside the incidence/bonus identity.
```

No observation is permitted to replace these scalars.

## 2. Target and score

Bulk cancellation is exact because every colour multiplies the same packet.

At an anchored leaf the same `u_(omega,e)` gives target equality, score superordination and every row identity:

\[
T(\nu_\omega)=T(E_\omega)-T(O_\omega),
\]

\[
S(\nu_\omega)=S(E_\omega)-S(O_\omega)+\sigma_\omega,\qquad \sigma_\omega\ge0,
\]

\[
R(\nu_\omega)+B_\omega=R(E_\omega)-R(O_\omega).
\]

The score coordinate is explicitly an inequality with named surplus. No negative Hall-edge score is promoted to a positive target-null packet.

## 3. Every component row

For every `j`, apply the same placement and quantizer to the same coefficient record. Tonelli gives

\[
d_X(j)=\tau_K\left[\sum_\omega\omega_X\left(R_j(\nu_\omega)+B_{\omega,j}\right)+\int_{I_X}\frac2sL(X/s)Q_j(p_s)\,ds\right]
\]

after the single bulk quantizer is expanded.

## 4. Ordinary `q`, ordinary `4q`, then detail

For the total row `d_X`, define

\[
C_q(d_X)=\int C_q(Q_X^{\rm nat}(t,\cdot))\,d\Gamma_X(t).
\]

Evaluate the same formula at `4q`. Only after both totals are formed set

\[
\boxed{\Xi_q(d_X)=C_q(d_X)-2C_{4q}(d_X).}
\tag{L-91883.1}
\]

Thus the coefficient of a source record is identical in target, score, every row, `q`, `4q` and detail.

## 5. Signed comparison and native slack

The retained-cell finite/continuum defect, intrinsic collar and terminal comparison form one signed observation vector `e_X`. Positive thinning and literal omissions supply unused capacity `u_X`. They are separate ledgers.

The frozen all-column theorem gives

\[
e_X(q)\le u_X(q)\qquad(q\ge2).
\]

Define

\[
r_X^{(4)}=u_X-e_X=\Omega_X-\Xi(d_X)\ge0.
\]

Positive radix-four inversion gives the ordinary complement.

## 6. `Y_4` ledger

Only after the complete detail slack is formed, pair it with the native dual:

\[
\boxed{J_\Lambda(X)-\mathcal H(d_X)=\sum_qY_4(q)r_X^{(4)}(q).}
\tag{L-91883.2}
\]

No branch receives a separate `Y_4` price. Hall edges, Lorenz incidences, first-owner labels and placements are audit coordinates, not extra deficit terms.