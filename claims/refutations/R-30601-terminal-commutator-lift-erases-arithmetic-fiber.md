# R-30601 — The quotient-only terminal commutator lift erases the arithmetic fiber

Claim ID: `R-30601`  
Title: PR #304's terminal map realizes divisor atoms at `2k,2k+1`, not the actual dilated atoms at `2kq_0,(2k+1)q_0`  
Status: **EXACT REFUTATION OF THE LOAD-BEARING SOURCE MAP IN `L-30402/T-30401`**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #306  
Dependencies: PR #303 `L-30201`; PR #304 `L-30402`; exact carry algebra  
Scope: the source-to-flow map used by the proposed terminal closure; no statement about RH itself

## 1. Adjacent-tree commutators

Let `T_n` be the complete central halving tree and put

\[
E_h=T_{h+1}-T_h.
\]

The exact carry load is

\[
\boxed{
L_q(E_h)=\mathbf 1_{q\mid h+1}.
}
\tag{R-30601.1}
\]

Consequently a divisor atom at the **actual integer node** `m` is represented by

\[
\boxed{e_m\longleftrightarrow E_{m-1}.}
\tag{R-30601.2}
\]

The node label cannot be divided by an external arithmetic fiber without an explicit dilation of the flow.

## 2. The source used in PR #304

For a fixed arithmetic fiber `q_0`, quotient index `k`, and exponent `s`, the shifted cutoff coefficients are

\[
A_k(q_0,s)=\frac{(2kq_0-1)^{-s}}{2k},
\qquad
B_k(q_0,s)=\frac{((2k+1)q_0)^{-s}}{2k+1}.
\tag{R-30601.3}
\]

`L-30402.8` treats their paired source as

\[
A_k e_{2k}-B_k e_{2k+1}
\]

and realizes it by `E_(2k-1),E_(2k)` plus a relative sibling switch.

That source has carry image

\[
A_k\mathbf1_{q\mid2k}-B_k\mathbf1_{q\mid2k+1}.
\tag{R-30601.4}
\]

The actual cutoff fiber is dilated by `q_0`. Its divisor source is

\[
\boxed{
A_k e_{2kq_0}-B_k e_{(2k+1)q_0},
}
\tag{R-30601.5}
\]

with carry image

\[
\boxed{
A_k\mathbf1_{q\mid2kq_0}
-B_k\mathbf1_{q\mid(2k+1)q_0}.
}
\tag{R-30601.6}
\]

The correct absolute adjacent-tree representative is therefore

\[
\boxed{
A_kE_{2kq_0-1}-B_kE_{(2k+1)q_0-1}.
}
\tag{R-30601.7}
\]

A dilation operator, together with its capacity scaling, is indispensable.

## 3. Minimal rational witness

Take

\[
q_0=5,
\qquad k=1,
\qquad s=1.
\]

Then

\[
A=\frac1{18},
\qquad
B=\frac1{45}.
\]

At the carry column `q=5`, the quotient-only flow has load

\[
A\mathbf1_{5\mid2}-B\mathbf1_{5\mid3}=0.
\]

The actual dilated source has load

\[
A\mathbf1_{5\mid10}-B\mathbf1_{5\mid15}
=A-B
=\boxed{\frac1{30}}.
\tag{R-30601.8}
\]

Thus the flow checked in `X-30401` does not replay this actual arithmetic fiber.

The verifier on PR #304 makes the loss visible: its expected source row tests divisibility of `2k` and `2k+1`; the loop variable `q0` enters only the numerical coefficient.

## 4. Capacity scaling after the correction

The adjacent-tree bound gives

\[
\|E_{m-1}\|_{\omega,1}\le24\sqrt m.
\]

For the corrected source (R-30601.7), at the critical exponent `s=1/2`,

\[
\begin{aligned}
\sqrt{2kq_0}\,A_k(q_0,1/2)&\asymp\frac1{2k},\\
\sqrt{(2k+1)q_0}\,B_k(q_0,1/2)&=\frac1{2k+1}.
\end{aligned}
\tag{R-30601.9}
\]

The `k`-sum is harmonic, but the outer factor `q_0^{-1/2}` claimed in `L-30402.10--.11` is cancelled by the square-root capacity of the dilated node.

Therefore the estimate

\[
Cq_0^{-1/2}(1+\log K)
\]

is not a bound for the actual dilated adjacent-tree flow. Any cross-fiber summation must be proved anew in a source coordinate retaining `q_0`.

## 5. Consequence

The chain

```text
finite Euler/Peano fiber
-> quotient-only source at 2k,2k+1
-> q0^(-1/2) logarithmic commutator debt
-> polylog total Cycle Debt
```

is unavailable.

This refutes the load-bearing source map in the frozen PR #304 proposal. It does not refute:

- the exact undilated commutator identity;
- the `24 sqrt(m)` capacity bound;
- the analytic `6/7` contraction;
- the possibility of a different source-complete optimized flow;
- RH.

## 6. Required repair

A valid replacement must retain one of the following exactly:

1. the dilated node labels `2kq_0,(2k+1)q_0` and pay their true capacity;
2. a complete fiber congruence proving that a quotient-space flow is transported to physical integer nodes, including the norm scaling;
3. a bandwise flow which recombines all `q_0` fibers before measuring negative capacity.

The third option is developed in `L-30601`.
