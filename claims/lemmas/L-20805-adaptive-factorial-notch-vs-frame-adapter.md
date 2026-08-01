# L-20805 — Adaptive factorial notches beat every subfactorial frame adapter

Claim ID: `L-20805`  
Title: The flat source notch can be scheduled directly from the emitted triangular metric adapter  
Status: `PROVED ASYMPTOTIC ADAPTER THEOREM; JOINT RESIDUAL LMI OPEN`  
Authoring agent: `gpt56-03-s`  
Created: 2026-08-01  
Dependencies: `L-20804`; the exact metric adapter emitted by `T-20501/M-20701`  
Scope: fixed off-line modes after every previously completed frame/graph coordinate change  
Related counterexample candidates: none

## 1. External adapter

Let

\[
 \Lambda_M\ge1
 \tag{L-20805.1}
\]

be the complete production adapter multiplying a one-sided scalar error at the
square level `(N,c)=(M,M^2)`. It may include:

1. the first and conditional frame coordinate maps;
2. the source graph metric;
3. the triangular square-completion metric;
4. any directed basis/assembly comparison already frozen at the finite level.

No asymptotic assumption is initially made on `Lambda_M`.

For an integer `1<=r<=M`, use the flat packet of `L-20804`. For every fixed
complex zero parameter `z`, equations `L-20804.18`--`L-20804.19` give, after
absorbing fixed multiplicity and polynomial factors,

\[
\boxed{
 \Lambda_M\varepsilon_{M,z}^{(r)}
 \le
 C_z\Lambda_M M^2\log M
 \left({C_z\log M\over r}\right)^{4r}
 e^{C r}.}
 \tag{L-20805.2}
\]

The constant `C` includes the complete coefficient/factorial graph charge. This
is the only estimate used below.

## 2. Notch budget

Define

\[
 \mathcal B_M(r)
 =4r\log\left({r\over C_z\log M}\right)-Cr.
 \tag{L-20805.3}
\]

Whenever `r/(log M)->infinity`, (L-20805.2) becomes

\[
 \log(\Lambda_M\varepsilon_{M,z}^{(r)})
 \le
 \log\Lambda_M+O_z(\log M)-\mathcal B_M(r).
 \tag{L-20805.4}
\]

The available budget is increasing for sufficiently large `r`, and at the full
packet degree

\[
 \mathcal B_M(M)
 =4M\log M-4M\log\log M+O(M).
 \tag{L-20805.5}
\]

Thus the finite packet carries a genuinely factorial, rather than polynomial,
fixed-mode moat.

## 3. Subfactorial adapter theorem

Assume

\[
 \boxed{\log\Lambda_M=o(M\log M).}
 \tag{L-20805.6}
\]

Then there is an explicit integer sequence

\[
 \log M\ll r_M\le M
 \tag{L-20805.7}
\]

such that

\[
 \mathcal B_M(r_M)
 \ge2\log\Lambda_M+10\log M.
 \tag{L-20805.8}
\]

For example, take the least integer satisfying (L-20805.8). Equation
(L-20805.4) then yields

\[
\boxed{
 \Lambda_M\varepsilon_{M,z}^{(r_M)}
 \le C_zM^{-9}\Lambda_M^{-1}
 \longrightarrow0.}
 \tag{L-20805.9}
\]

The same sequence works for every fixed finite zero set after increasing the
`10 log M` reserve by a fixed amount.

Hence:

\[
\boxed{
 \log\Lambda_M=o(M\log M)
 \quad\Longrightarrow\quad
 \text{all fixed off-line modes are defeated after the full adapter}.}
 \tag{L-20805.10}
\]

## 4. Exponential adapters and support averaging

A particularly useful production regime is

\[
 \boxed{\log\Lambda_M\le C_0M.}
 \tag{L-20805.11}
\]

Choose

\[
 r_M=\left\lceil K{M\over\log M}\right\rceil
 \tag{L-20805.12}
\]

with `K>C_0/4` after the harmless constants in (L-20805.3) are included. Then

\[
 \mathcal B_M(r_M)=4KM+o(M),
 \tag{L-20805.13}
\]

and every fixed-mode product tends to zero exponentially in `M`.

At the same time,

\[
 r_M={KM\over\log M}
 =o\!\left({M\over\sqrt{\log M}}ight)
 =o\!\left(\sqrt{{M^2\over\log(M^2)}}\right).
 \tag{L-20805.14}
\]

Therefore the whitened support-derivative envelope remains strictly below the
sub-square-root threshold of `L-16226/T-15606`. In this regime the fixed core
and the moving high-frequency support average are compatible in one packet.

## 5. More general growth ledger

Suppose

\[
 \log\Lambda_M=O(M(\log M)^\alpha),
 \qquad 0\le\alpha<1.
 \tag{L-20805.15}
\]

Taking

\[
 r_M=K M(\log M)^{\alpha-1}
 \tag{L-20805.16}
\]

with `K` sufficiently large gives

\[
 \mathcal B_M(r_M)
 =(4K(1-\alpha)+o(1))M(\log M)^\alpha.
 \tag{L-20805.17}
\]

Thus the fixed core is suppressed. Moreover

\[
 r_M=o(M/\sqrt{\log M})
 \tag{L-20805.18}
\]

whenever

\[
 \boxed{\alpha<\frac12.}
 \tag{L-20805.19}
\]

This gives the exact adapter boundary for simultaneous use of the current
support-large-sieve theorem.

If `1/2<=alpha<1`, the factorial packet still defeats every fixed mode, but the
existing support-average derivative threshold requires a separate hard/soft or
multiscale split.

## 6. Slowly growing inner blocks

Let `Z_M` be a finite zero set with

\[
 \max_{z\in Z_M}|z|=H_M,
 \qquad
 \#Z_M\le C H_M\log(2H_M).
 \tag{L-20805.20}
\]

The same proof applies provided

\[
 H_M\log M=o(r_M)
 \tag{L-20805.21}
\]

and the reserve in (L-20805.8) dominates the additional

\[
 O(r_M\log H_M+\log\#Z_M)
 \tag{L-20805.22}
\]

cost. Hence the adaptive packet can remove a growing inner zero block, not only
a fixed finite list.

## 7. Exact remaining implication

The theorem resolves the alternative raised after `L-20802`:

```text
Could the fixed off-line mode survive merely because the frame/metric
factorial costs grow faster than the notch?
```

Under the explicit and auditable condition (L-20805.6), the answer is no. The
notch degree may be selected from the actual emitted `Lambda_M`, and every fixed
mode is smaller than the final metric gate.

It does **not** prove the source Schur scalar because `R-20802` remains
load-bearing. The unresolved estimate is the one joint trial-residual LMI

\[
 \mathscr R_M^*A_{WW,M}^{-1}\mathscr R_M
 \le
 \langle A_Mx_M,x_M\rangle+g_M\varepsilon_M.
 \tag{L-20805.23}
\]

The new result says that no fixed off-line atom and no hidden factorial/frame
cost can obstruct (L-20805.23) once the complete adapter is subfactorial. Any
failure must occur in the moving residual/high-frequency block or in a
superfactorial adapter growth that is visible in the proof artifact.

## 8. Proof boundary

- The theorem is an exact asymptotic consequence of the fully charged estimate
  in `L-20804`.
- It consumes the actual finite adapter, rather than assuming a generic
  polynomial condition number.
- A production pass should emit `log Lambda_M` and the least admissible `r_M`
  from (L-20805.8) at every level.
- No joint residual inequality and no RH proof are claimed here.
