# R-34402 — The odd relative second current is not the standard Selberg carry

Claim ID: `R-34402`  
Title: The repair identity `T_odd(4e)-T_odd(e)=S_odd(4e)+S_odd(2e)` uses the wrong prefix level  
Status: **EXACT FALSE-CLAIM CERTIFICATE AND SOURCE-ORDER CORRECTION**  
Authoring/review agent: `gpt56-sol`  
Created: 2026-08-10  
Dependencies: PR #349 `R-34401/L-34407`; the atomized carry identity  
Scope: exact arithmetic source typing; no RH conclusion

## 1. The carry identity has one mandatory divisor convolution

For an arithmetic sequence `f`, write

\[
\mathcal L_{n,j}(f)
=\sum_{q\ge1}f(q)
\left(
\left\lfloor\frac nq\right\rfloor
-\left\lfloor\frac jq\right\rfloor
-\left\lfloor\frac{n-j}q\right\rfloor
\right).
\]

If

\[
P_f(X)=\sum_{m\le X}f(m),
\]

then divisor switching gives

\[
\boxed{
\mathcal L_{n,j}(f)
=P_{\mathbf1*f}(n)
-P_{\mathbf1*f}(j)
-P_{\mathbf1*f}(n-j).
}
\tag{R-34402.1}
\]

The ordinary prefix of `f` is not enough.  The convolution `1*f` is load bearing.

## 2. Apply this to the odd source second current

Retain

\[
b_{\rm odd}(n)=\mu(n)\mathbf1_{n\text{ odd}},
\]

\[
C_{\rm odd}
=\Lambda_{\rm odd}\log
 +\Lambda_{\rm odd}*\Lambda_{\rm odd},
\]

and

\[
t_{\rm odd}=b_{\rm odd}*C_{\rm odd}.
\]

The correct source identity from PR #349 is

\[
\mathbf1*b_{\rm odd}
=\sum_{a\ge0}\delta_{2^a}.
\tag{R-34402.2}
\]

Therefore

\[
\boxed{
\mathbf1*t_{\rm odd}
=\sum_{a\ge0}\delta_{2^a}*C_{\rm odd}.
}
\tag{R-34402.3}
\]

Define the **ordinary** prefix of the Selberg coefficient sequence

\[
H_C(X)=\sum_{m\le X}C_{\rm odd}(m).
\tag{R-34402.4}
\]

Equations (R-34402.1)--(R-34402.3) give

\[
P_{\mathbf1*t_{\rm odd}}(X)
=\sum_{a\ge0}H_C\!\left(\left\lfloor\frac X{2^a}\right\rfloor\right).
\tag{R-34402.5}
\]

Consequently, if

\[
\mathcal D_C(n,j)
:=H_C(n)-H_C(j)-H_C(n-j),
\tag{R-34402.6}
\]

then exact dyadic index shifting gives

\[
\boxed{
T_{\rm odd}(4e)-T_{\rm odd}(e)
=\mathcal D_C(4e)+\mathcal D_C(2e).
}
\tag{R-34402.7}
\]

This is the correct relative second-current identity.

## 3. Why `D_C` is not `S_odd`

The standard odd Selberg carry is

\[
S_{\rm odd}(e)=\mathcal L_e(C_{\rm odd}).
\]

By (R-34402.1), it is the additive defect of the prefix of

\[
\mathbf1*C_{\rm odd},
\]

not of `C_odd` itself.  In fact the generalized Selberg identity gives

\[
(\mathbf1*C_{\rm odd})(m)
=\log^2\operatorname{odd}(m),
\]

so

\[
S_{\rm odd}(n,j)
=\sum_{m\le n}\log^2\operatorname{odd}(m)
 -\sum_{m\le j}\log^2\operatorname{odd}(m)
 -\sum_{m\le n-j}\log^2\operatorname{odd}(m).
\tag{R-34402.8}
\]

That is a different prefix level from (R-34402.4).

Thus the displayed equality in current `L-34407.3`, and hence `L-34407.12`, is false.

## 4. Exact smallest counterexample

Take

\[
e=(2,1),\qquad 2e=(4,2),\qquad4e=(8,4).
\]

Put

\[
a=\log3,\qquad b=\log5,\qquad c=\log7.
\]

Below eight, the nonzero odd Selberg coefficients are

\[
C_{\rm odd}(3)=a^2,
\quad
C_{\rm odd}(5)=b^2,
\quad
C_{\rm odd}(7)=c^2.
\]

Hence

\[
H_C(2)=0,
\quad H_C(4)=a^2,
\quad H_C(8)=a^2+b^2+c^2.
\]

The correct identity (R-34402.7) gives

\[
\begin{aligned}
T_{\rm odd}(8,4)-T_{\rm odd}(2,1)
&=\mathcal D_C(8,4)+\mathcal D_C(4,2)\\
&=(b^2+c^2-a^2)+a^2\\
&=\boxed{b^2+c^2}.
\end{aligned}
\tag{R-34402.9}
\]

On the other hand, direct carry evaluation gives

\[
S_{\rm odd}(8,4)=b^2+c^2,
\qquad
S_{\rm odd}(4,2)=a^2,
\]

and therefore

\[
\boxed{
S_{\rm odd}(8,4)+S_{\rm odd}(4,2)
=a^2+b^2+c^2
\ne b^2+c^2.
}
\tag{R-34402.10}
\]

The discrepancy is exactly `(log 3)^2>0`.

## 5. Consequence for PR #349

The following current claims are false as written:

```text
L-34407.3:
    ordinary prefix of C_odd equals the Selberg carry prefix;

L-34407.12:
    T_odd(4e)-T_odd(e)=S_odd(4e)+S_odd(2e);

L-34407.17:
    repaired curvature contains exactly
    2S_odd(4e)+2S_odd(2e).
```

The earlier correction

\[
Y_{\rm odd}(4e)-Y_{\rm odd}(e)=-2
\]

remains correct.  The curvature must instead retain

\[
2\mathcal D_C(4e)+2\mathcal D_C(2e).
\]

`L-34408` proves the exact corrected formula and a cofinal positivity theorem for this boundary on fixed balanced cones.

## 6. Proof boundary

Established exactly:

1. the mandatory `1*f` prefix in the carry identity;
2. the correct dyadic relative second-current formula;
3. the distinction between `D_C` and the standard Selberg carry;
4. the explicit counterexample at `e=(2,1)`.

Not claimed here:

1. all-row positivity of `D_C`;
2. an upper/dissipative recurrence;
3. RH.
