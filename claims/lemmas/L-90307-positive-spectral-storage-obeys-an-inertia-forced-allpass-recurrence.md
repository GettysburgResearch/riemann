# L-90307 — Positive spectral storage obeys an inertia-forced all-pass recurrence

Claim ID: `L-90307`  
Title: The polarized all-pass telescope is an exact matrix conservation law on channel curvatures; replacing scalar energy by positive spectral mass yields a coefficient-one storage recurrence whose only losses are the negative masses of the current output and state  
Status: **PROPOSED COMPLETE EXACT MATRIX/STATE-SPACE LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Dependencies: PR #339 `L-33804`; `L-90305`, `L-90306`  
Scope: exact finite-channel matrix conservation and Lyapunov recurrence; source identification with the corrected Q2/Q4 state remains a separate arithmetic interface

## 1. Channel curvature matrix

Let

\[
V_\tau=(v_{1,\tau},\ldots,v_{r,\tau})
\]

be a twice differentiable analytic path of `r` physical block fields.  On a logarithmic block `I`, define its Hermitian channel curvature matrix by

\[
\boxed{
[K_I(V)]_{ab}
=\langle\dot v_a,\dot v_b\rangle_I
 -\frac12\left(
   \langle v_a,\ddot v_b\rangle_I
  +\langle\ddot v_a,v_b\rangle_I
 \right).
}
\tag{L-90307.1}
\]

Its trace is the scalar curvature of the direct-sum physical vector:

\[
\operatorname{tr}K_I(V)
=\sum_{a=1}^r\mathfrak C_I(v_a).
\tag{L-90307.2}
\]

For a Hermitian matrix `H`, put

\[
p(H)=\operatorname{tr}H_+,
\qquad
\delta(H)=\operatorname{tr}H_-.
\tag{L-90307.3}
\]

Then

\[
\operatorname{tr}H=p(H)-\delta(H).
\]

The variational formulas are

\[
\boxed{
 p(H)=\max_{0\preceq P\preceq I}\operatorname{tr}(PH),
 \qquad
 \delta(H)=\max_{0\preceq P\preceq I}-\operatorname{tr}(PH).
}
\tag{L-90307.4}
\]

Consequently both `p` and `delta` are subadditive on Hermitian sums.

## 2. The all-pass telescope holds entrywise

Let `phi(D),R(D)` be the parameter-independent all-pass output/state operators of PR #339 `L-33804`, with delay `L`.  That theorem proves the physical identity in polarized bilinear form, not merely on a diagonal energy.

Apply its bilinear identity to every pair of channel paths `(v_a,v_b)` and differentiate in the imaginary Jordan direction.  One gets, entry by entry,

\[
\boxed{
K_I(V)-K_I(\phi V)
=K_I(RV)-K_{I-L}(RV).
}
\tag{L-90307.5}

(The closing bracket in the tag is typographical only.)

Equivalently,

\[
\boxed{
K_I(\phi V)+K_I(RV)
=K_I(V)+K_{I-L}(RV).
}
\tag{L-90307.6}

Thus the lossless block state law is an equality of complete Hermitian curvature matrices.  All channel cross terms are retained.

## 3. Principal positive-mass recurrence

From (L-90307.5),

\[
K_I(\phi V)
=K_I(V)+K_{I-L}(RV)-K_I(RV).
\]

Using subadditivity of `p` and `p(-H)=delta(H)`,

\[
\boxed{
 p(K_I(\phi V))
 \le p(K_I(V))
    +p(K_{I-L}(RV))
    +\delta(K_I(RV)).
}
\tag{L-90307.7}

This is a matrix-strengthened version of `L-90306.12`.  It controls every output-channel Rayleigh quotient, not only the trace:

\[
\boxed{
 c^*K_I(\phi V)c
 \le \|c\|^2\,p(K_I(\phi V))
}
\tag{L-90307.8}

for all channel vectors `c` whenever the left side is nonnegative.

In particular an RH-sensitive current square occupying one diagonal channel is bounded by the right side of (L-90307.7).

## 4. Total positive spectral storage

For Hermitian `A,B`,

\[
\begin{aligned}
 p(A)+p(B)
 &=\operatorname{tr}(A+B)+\delta(A)+\delta(B)\\
 &=p(A+B)-\delta(A+B)+\delta(A)+\delta(B)\\
 &\le p(A+B)+\delta(A)+\delta(B).
\end{aligned}
\]

Hence

\[
\boxed{
 p(A)+p(B)
 \le p(A+B)+\delta(A)+\delta(B).
}
\tag{L-90307.9}

Apply this to the two outgoing matrices in (L-90307.6), then use subadditivity on the incoming side:

\[
\boxed{
\begin{aligned}
&p(K_I(\phi V))+p(K_I(RV))\\
&\quad\le
 p(K_I(V))+p(K_{I-L}(RV))
 +\delta(K_I(\phi V))
 +\delta(K_I(RV)).
\end{aligned}}
\tag{L-90307.10}

This is the exact inertia-forced storage recurrence.  If the output of one stage is the principal input of the next, define

\[
\mathscr E_I
=p(K_I(\text{principal}))+p(K_I(\text{stored state})).
\tag{L-90307.11}
\]

Then every lossless stage contributes coefficient one to `mathscr E`; the only forcing is the negative spectral mass of the current output and state.

## 5. Q=4 normalization and finite cascades

For Q=4, `E_4=2phi`, so

\[
p(K_I(E_4V))=4p(K_I(\phi V)),
\qquad
\delta(K_I(E_4V))=4\delta(K_I(\phi V)).
\]

Divide the principal output by the critical gain four.  Equations (L-90307.7) and (L-90307.10) retain coefficient one.

For a finite cascade, apply (L-90307.6) stage by stage and add the exact matrix identities.  Internal channel curvatures cancel before `p` or `delta` is taken.  Only after this cancellation apply (L-90307.9).  Therefore an `m`-stage cascade obeys

\[
\boxed{
\mathscr E_{\rm out}(I)
\le
\mathscr E_{\rm in}(I)
+\mathscr E_{\rm stored}(I-\text{declared delays})
+\sum_{j=1}^m
 \left[\delta(K_{j,\rm out})+\delta(K_{j,\rm state})\right].
}
\tag{L-90307.12}

No multiplicative loss depending on the number of stages appears.

## 6. Insert the zero-bare Q4 defect

`L-90304` proves for the source carrying the genuine compact innovation that, rowwise on every fixed balanced cone,

\[
\delta(K)=O_\eta(n/\log n).
\]

`L-90305` lifts this through the complete positive carry-position measure, independent-frequency block, Toeplitz filters, and contractive syntheses, giving in critical normalization

\[
\delta(K_I)=O_\eta(1/\log n).
\tag{L-90307.13}
\]

Thus every occurrence of that corrected source as either output or stored state in (L-90307.12) contributes only lower-order forcing.  For a fixed Q2/Q4 cascade the sum remains `O_eta(1/log n)` per block.

This proves that neither:

1. noncommuting rowwise bad directions;
2. filter cross terms;
3. the current-block all-pass state;
4. a finite number of cascade stages

can restore an RH-scale loss after `L-90304`.

## 7. Remaining source interface

To turn (L-90307.12) into the final QIDR recurrence, one must identify in one block metric:

```text
principal input/output path;
zero-bare compact relative path;
Q2 low-pass/root states;
Q4 two-stage state;
strictly delayed derivative gauges;
fixed physical collars.
```

The existing repository gives exact formulas for each item separately.  The remaining task is to substitute them into (L-90307.6), cancel the internal states, and verify that every nonprincipal term is either one of the declared predecessor states or a fixed/polylogarithmic forcing channel.

The dissipative orientation and the spectral Lyapunov functional are no longer open.

## 8. Proof boundary

Closed exactly here:

1. the channel-matrix all-pass curvature identity;
2. positive/negative spectral-mass variational formulas;
3. principal positive-mass recurrence;
4. total positive-storage recurrence;
5. coefficient-one finite-cascade composition;
6. lower-order insertion of the zero-bare Q4 defect.

Still open:

1. explicit substitution of the corrected Q2/Q4 source dictionary into the matrix conservation law;
2. routing of all fixed collars and differentiated finite gauges;
3. the final globally iterated QIDR statement;
4. RH.
