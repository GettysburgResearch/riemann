# L-93882 — A block-diagonal whole-cell realization preserves the exact hybrid marginal

Claim ID: `L-93882`  
Status: **PROPOSED COMPLETE POSITIVE-REALIZATION THEOREM**  
Depends on: `L-93880`, `L-93881`, the positive martingale quantizer  
RH status: **unproved at this claim**

## 1. Two source sectors

Let

\[
\mathscr H_X^{\rm src}
=
\mathscr H_{X,\mathrm{anc}}^{\rm src}
\oplus
\mathscr H_{X,\mathrm{bulk}}^{\rm src}.
\]

The anchored sector already consists of finite positive physical rows. The bulk
sector is the positive Volterra measure from `L-93880`.

Define

\[
\boxed{
\mathcal Q_X^{\rm hyb}
=
I_{\rm anc}\oplus\mathcal Q_X^{\rm Bsp}.
}
\tag{L-93882.1}
\]

Thus the anchored rows are never requantized.

## 2. Whole-cell support

Use only complete integer cells

\[
I_X=[K+2,X-W-2],
\qquad
K=\lfloor X/67\rfloor+1,\quad W=10000.
\]

There is no partial lower cell, activation cell, or upper cell. The bulk
rank-one coefficients are Borel on each quotient cell. The anchored leaf
coefficients are finite algebraic/min expressions on each activation cell.
Their one-sided knot values are irrelevant to the integral.

## 3. Positive bulk quantizer

For a bulk endpoint `s`, the B-spline weights satisfy

\[
q_U(s)\ge0,\qquad
\sum_Uq_U(s)=1,\qquad
\sum_Ur_Uq_U(s)=r(s).
\]

Consequently the endpoint masses

\[
M_U=\int\lambda(s)a(s)q_U(s)\,ds
\]

are nonnegative and preserve the two parabolic modes exactly.

The bulk row discrepancy is supported only on the moving width-three strip.
There is no bulk error below `K`.

## 4. Exact label preservation

The quantizer acts on the endpoint coordinate and is blind to:

```text
Möbius residual label;
anchored/bulk label;
rough first owner;
Target-Lorenz cutoff;
current-only row bonus.
```

Every output atom retains all labels. Since its weights sum to one, an input
source occurrence has exactly one unit of outgoing ownership.

## 5. Physical row

Let `d_X^0` be the observation of

\[
\mathcal Q_X^{\rm hyb}
(\Sigma_{X,\mathrm{anc}}\oplus\Sigma_{X,\mathrm{bulk}}).
\]

Then

\[
\boxed{d_X^0\ge0}
\tag{L-93882.2}
\]

coefficientwise.

The exact native row is

\[
\boxed{
c_X=d_X^{0,\mathrm{ideal}}+\mathcal R E_X^I
      +o_X^{\rm bot}+o_X^{\rm top},
}
\tag{L-93882.3}
\]

where `E_X^I` is signed observation data and the omissions are literal positive
source restrictions. Equation (L-93882.3) is a typed accounting identity, not
a claim that the signed error is a source packet.

## 6. One scalar thinning

Put

\[
\tau_K=\frac{\sqrt K}{\sqrt K+130},
\qquad
d_X=\tau_K d_X^0.
\tag{L-93882.4}
\]

All labels and all current/child colours are scaled together. No recursive
family is exported; every actual child response is already an internal colour
of `d_X`.

## 7. No auxiliary Schur port

The realization consists only of:

```text
positive source restriction;
positive finite Target-Lorenz row compilation;
positive B-spline Markov pushforward;
one scalar thinning;
capacity comparison against the signed observation defect.
```

No state completion or Schur complement is invoked. Therefore the auxiliary
matrix demand and reserve are both exactly zero.

## 8. Boundary

```text
anchored quantizer                         IDENTITY
bulk quantizer                            POSITIVE MARTINGALE
partial cells                             ABSENT
source ownership                          EXACT
physical row positivity                   EXACT
signed defect                             OBSERVATION ONLY
exported children                         EMPTY
matrix port                               ZERO
capacity feasibility                      L-93883
```
