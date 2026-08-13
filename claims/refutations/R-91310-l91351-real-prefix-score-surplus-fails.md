# R-91310 — The `P_79` real-prefix score surplus used by `L-91351` is false

Claim ID: `R-91310`  
Status: **EXACT SCALAR COUNTEREXAMPLE — DIRECT-ROW PROPOSAL REQUIRES A PHYSICAL-ENTROPY REPAIR**  
Created: 2026-08-13  
Frozen main under review: `d688cc7cb73eea9e50f10352a50516ab2c4f4625`  
Depends on: `L-91345-p79-one-prime-splice-has-a-monotone-two-ledger-kernel-and-large-prefix-reserve.md`; `L-91351-p79-one-prime-splice-is-a-terminal-child-plus-positive-arithmetic-row.md`  
RH status: **unproved**

## 1. The assertion under audit

Put

\[
 P=P_{79}=\prod_{q\le79}q,
 \qquad
 A_P(x)=\sum_{\substack{d\mid P\\d\le x}}\frac{\mu(d)}d.
\]

For `p>=83`, `1<=y<83`, and `x=py`, `L-91351.10` correctly gives

\[
 \mathfrak S_{Pp}(x)-\mathfrak T_{Pp}(x)
 =\sqrt{x}\left[A_P(x)-\frac1pA_P(y)\right].
 \tag{R-91310.1}
\]

The next line of that proof promotes the active-threshold estimate from
`L-91345` to the pointwise assertion

\[
 A_P(x)>\frac1{25}\qquad(x\ge83).
 \tag{R-91310.2}
\]

That promotion is invalid. The theorem in `L-91345` controls the Hall prefix
only at its declared odd squarefree demand thresholds. It does not control the
entire real step function between those thresholds.

## 2. Exact witness

Take

\[
 p=83,
 \qquad y=1,
 \qquad x=83.
\]

The complete exact divisor prefix is

\[
 \boxed{
 A_P(83)
 =-
 \frac{1401629533229069216211617003}
 {107254825578022430263302818471}
 <0.
 }
 \tag{R-91310.3}
\]

Since `A_P(1)=1`,

\[
\boxed{
 A_P(83)-\frac1{83}A_P(1)
 =-
 \frac{223590076836035175208867029720}
 {8902150522975861711854133933093}
 <0.
}
\tag{R-91310.4}
\]

Therefore the claimed favorable scalar orientation is reversed:

\[
\boxed{
 \mathfrak S_{P\cdot83}(83)-\mathfrak T_{P\cdot83}(83)
 <0.
}
\tag{R-91310.5}
\]

Numerically, only for orientation,

\[
 \mathfrak S_{P\cdot83}(83)-\mathfrak T_{P\cdot83}(83)
 \approx-0.2288213998081811.
\]

No floating-point sign decision is involved in (R-91310.5).

## 3. Why the active-threshold certificate does not apply

`L-91345` defines

\[
 A_0(t)
 =\sum_{e\le t,\mu(e)=1}\frac1e
 -\sum_{o\le t,\mu(o)=-1}\frac1o
\]

at an odd squarefree divisor demand threshold `t`. Its retained minimum for the
large-threshold gate occurs at `t=105`, where the prefix is positive. The real
step function before that threshold is different. In particular, the complete
prefix at `x=83` is the negative rational number (R-91310.3).

Thus

```text
active odd Hall thresholds t>=83         controlled by L-91345;
all real x>=83                            not controlled;
x=83                                     exact negative witness.
```

## 4. Consequence for the direct-row composition

The following parts of `L-91351` survive this counterexample:

```text
exact Euler target split;
exact Euler row split;
inherited residual-row positivity, conditional on L-91346;
positivity of the residual target and residual score separately;
terminal-child coefficient p^(-1/2).
```

The following advertised inference does not survive:

```text
residual source score > residual source target
-> current arithmetic residual has nonpositive physical loss.
```

The premise is false at `(p,y)=(83,1)`, and source score is not automatically
the literal entropy of the positive component row.

## 5. Repair direction

The correct quantity is the physical component-row entropy

\[
 \sum_{j\ge2}D_{Pp}(py;j)G_j,
\]

not the scalar source label `mathfrak S_(Pp)(py)`. The companion theorem
`L-91352` computes that entropy exactly and proves the stronger inequality

\[
 \sum_{j\ge2}D_{Pp}(py;j)G_j
 >\frac43\sqrt{py}
 >\mathfrak T_{Pp}(py),\mathfrak S_{Pp}(py).
\]

Accordingly, this refutation removes one false scalar sentence while leaving a
potentially stronger physical repair.

```text
L-91351.10 exact first-moment identity             VALID
L-91351 pointwise A_P(x)>1/25 for all x>=83        FALSE
L-91351.11 strict scalar score-over-target surplus FALSE
T-91304 scalar favorable-loss justification         INVALID AS WRITTEN
physical component-entropy repair                    PROPOSED IN L-91352
Riemann Hypothesis                                  UNPROVEN
```
