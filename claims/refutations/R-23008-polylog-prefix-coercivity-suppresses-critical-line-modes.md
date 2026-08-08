# R-23008 — Polylogarithmic prefix coercivity suppresses legitimate critical-line modes

Claim ID: `R-23008`  
Title: The finite digital prefix has critical inverse scale `R^(1/2)` at line zeros, so the polylogarithmic `PGC(R)` condition is overstrong  
Status: **EXACT SCOPE REFUTATION AND REPAIR REQUIREMENT**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-08  
Frozen target: PR #236 at `a0d5a627bd2d4e799eddf7c795df77083a3618ff`  
Primary target: `T-23004.7` and the former polylog-conditioned `PGC(R)`  
Scope: refutes that conditioning rate; does not refute critical-order source-specific observability

## 1. The exact digital symbol

Let

\[
c_2(n)=1-v_2(n),
\qquad
C_2(x)=\sum_{n\le x}c_2(n)=s_2(\lfloor x\rfloor),
\]

where `s_2` is the binary digit sum. The Dirichlet series is

\[
\boxed{
\mathcal C_2(s)
 =\sum_{n\ge1}{c_2(n)\over n^s}
 =\zeta(s){1-2^{1-s}\over1-2^{-s}}.
}
\tag{R-23008.1}
\]

For an integer prefix `R>=3`, put

\[
A_R(s)=\sum_{n<R}{c_2(n)\over n^s}.
\tag{R-23008.2}
\]

This is the frequency symbol of the finite delay operator `mathcal A_R` in
`L-23016/T-23004`.

## 2. The prefix is small at every zeta zero

Let `rho=beta+i gamma` be any nontrivial zero of `zeta`. The denominator in
(R-23008.1) does not vanish in the critical strip, so

\[
\mathcal C_2(\rho)=0.
\]

Consequently

\[
A_R(\rho)
 =-\sum_{n\ge R}{c_2(n)\over n^\rho}.
\tag{R-23008.3}
\]

Abel summation and

\[
0\le C_2(x)\le1+{\log x\over\log2}
\]

give, for every fixed `rho` with `beta>0`,

\[
\boxed{
|A_R(\rho)|
 \le C_\rho {1+\log R\over R^\beta}.
}
\tag{R-23008.4}
\]

The same argument bounds every fixed derivative:

\[
|A_R^{(j)}(\rho)|
 \le C_{\rho,j}{(1+\log R)^{j+1}\over R^\beta}.
\tag{R-23008.5}
\]

Thus the digital prefix becomes nearly singular precisely at the zero modes it
is intended to detect.

## 3. Consequence for a pole mode

Let the safe-smoothed dyadic shell transform have a pole of multiplicity `m` at

\[
z_\rho=\rho-\frac12.
\]

Its inverse Laplace expansion contains a nonzero term

\[
e^{z_\rho t}P_{m-1}(t),
\tag{R-23008.6}
\]

where `P_(m-1)` has degree `m-1`. Applying `mathcal A_R` multiplies the top
polynomial coefficient by `A_R(rho)`; if that value vanishes exactly, the
polynomial degree drops and the obstruction below is stronger.

On a long horizon, any source inequality of the form

\[
\|f\|^2
 \le K_R\bigl[D_R(J)+\|\mathcal A_Rf\|^2\bigr]
\tag{R-23008.7}
\]

with a defect `D_R(J)` subexponential in `J` therefore requires

\[
\boxed{
K_R
 \ge c_{\rho,m}
 {R^{2\beta}\over(1+\log R)^{O(m)}}.
}
\tag{R-23008.8}
\]

This holds along every prefix sequence on which the leading multiplier is
nonzero. Exact zeros of the multiplier make a finite `K_R` impossible unless
the corresponding mode is explicitly assigned to the defect channel.

## 4. Why the former polylogarithmic theorem is false

Zeta has nontrivial zeros on the critical line. For such a zero `beta=1/2`,
(R-23008.8) gives the critical lower scale

\[
K_R\ge {R\over(1+\log R)^{O(m)}}.
\tag{R-23008.9}
\]

The former `PGC(R)` required only

\[
K_R\le C(\log R)^A
\]

and provided merely a constant additive defect. That would suppress a genuine
critical-line oscillation whose cumulative energy grows polynomially with the
horizon. It cannot hold for the actual shell source.

Accordingly:

```text
polylog-conditioned finite-prefix PGC(R)    REFUTED
T-23004 deduction from that PGC(R)           NOT AVAILABLE
finite digital recurrence and tail estimate RETAINED
critical-order source-specific theorem       NOT REFUTED
```

## 5. The correct critical threshold

The natural replacement is

\[
\boxed{
K_R=R^{1+o(1)},
}
\tag{R-23008.10}
\]

with an explicit **tempered defect channel** that may contain boundary terms and
critical-line polynomial modes but has zero exponential growth in `J`.

If an off-line zero has `beta>1/2`, then (R-23008.8) requires

\[
K_R\ge R^{2\beta-o(1)},
\]

which is incompatible with (R-23008.10). Hence critical-order observability is
still sufficient for RH, while remaining compatible with the line spectrum.

## 6. Relation to the factor-five transition work

PRs #263 and #269 supply a finite parity-paired reconstruction, confinement of
all potentially negative carry rows to quotient cells `2,3,4`, and an absolute
carry-space Schur reserve. Their still-open physical source-image map is a
candidate mechanism for the corrected critical-order theorem, not for the
refuted polylogarithmic inverse.

A valid production theorem must therefore:

1. retain every independent-frequency cross term;
2. assign all line-spectrum and endpoint terms to a certified tempered channel;
3. prove a source-specific physical-to-carry map with loss `R^(1+o(1))` or
   better;
4. preserve the strict factor-five carry reserve after all collar and
   lower-block charges.

## 7. Proof boundary

Established here:

- the exact digital symbol;
- the Abel tail bound at every zeta zero;
- the necessary critical conditioning scale;
- refutation of the polylogarithmic `PGC(R)` rate;
- the corrected `R^(1+o(1))` threshold.

Not established:

- the corrected source-specific critical-order observability theorem;
- the physical-to-carry transition map;
- RH.
