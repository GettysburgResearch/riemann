# L-32305 — The aligned Q=4 innovation is prime-free and reserve-dominated

Claim ID: `L-32305`  
Title: On aligned quarter-balanced integer rows the one-step Q=4 innovation is an explicit factorial/base-four expression of size `O(log n)`, hence its square is eventually smaller than the radix-four reserve increment  
Status: **PROPOSED COMPLETE COFINAL SCALAR THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #345 `L-34401`; PR #337 `L-32706`; PR #342 `L-34005`  
Scope: aligned integer carry rows only; does not prove the independent-frequency physical block or RH

## 1. Exact aligned innovation formula

Let `L=log 4`, `n=j+k`, and retain PR #345's compact source

\[
 b_\circ=(\varepsilon-\delta_4)*b_4,
\]

own compact current

\[
 q_\circ=-b_\circ\log,
\]

and actual innovation current

\[
 i_\circ=q_\circ-L\delta_4*b_4.
\]

PR #345 proves

\[
\mathbf1*q_\circ
=(\varepsilon-4\delta_4)*\Lambda+4L\delta_4.
\]

Its ordinary prefix is

\[
G_\circ(X)=\psi(X)-4\psi(\lfloor X/4\rfloor)+4L\mathbf1_{X\ge4}.
\]

At the aligned row `(4n,4j)`, all three arguments are multiples of four. Hence the carry/prefix identity gives

\[
\begin{aligned}
\mathcal L_{4n,4j}(q_\circ)
={}&[\psi(4n)-\psi(4j)-\psi(4k)]\\
&-4[\psi(n)-\psi(j)-\psi(k)]-4L.
\end{aligned}
\]

By Kummer's ordinary von-Mangoldt identity,

\[
\psi(n)-\psi(j)-\psi(k)=\log\binom nj.
\]

Therefore

\[
\boxed{
\mathcal L_{4n,4j}(q_\circ)
=\log\frac{\binom{4n}{4j}}{\binom nj^4}-4L.
}
\tag{L-32305.1}
\]

The delayed bare gauge scales exactly:

\[
\mathcal L_{4n,4j}(\delta_4*b_4)
=\mathcal L_{n,j}(b_4)
=Y_4(n,j).
\]

Thus the true innovation of PR #345 is

\[
\boxed{
I_\circ(n,j)
=\log\frac{\binom{4n}{4j}}{\binom nj^4}
 -4\log4-(\log4)Y_4(n,j).
}
\tag{L-32305.2}
\]

No prime or Mobius coefficient remains in this aligned coordinate.

## 2. The factorial ratio is logarithmic

There is a direct combinatorial injection

```text
choose j objects independently from each of four disjoint n-blocks
    -> choose 4j objects from a 4n-set,
```

so

\[
\binom{4n}{4j}\ge\binom nj^4.
\]

PR #342 `L-34002` proves the complementary elementary bound

\[
\frac{\binom{4n}{4j}}{\binom nj^4}\le(n+1)^4.
\]

Hence

\[
\boxed{
0\le
\log\frac{\binom{4n}{4j}}{\binom nj^4}
\le4\log(n+1).
}
\tag{L-32305.3}
\]

## 3. The bare Q=4 gauge is logarithmic

PR #337 gives exactly

\[
Y_4(n,j)
=3[\lfloor\log_4j\rfloor+\lfloor\log_4k\rfloor-\lfloor\log_4n\rfloor]-1.
\]

Since each floor lies between zero and `floor(log_4 n)`,

\[
\boxed{
|Y_4(n,j)|\le3\lfloor\log_4n\rfloor+1.
}
\tag{L-32305.4}
\]

Combining (L-32305.2)--(L-32305.4), and using `log(n+1)<=log(2n)` and `log4=2log2`, gives for every `n>=2`

\[
\begin{aligned}
|I_\circ(n,j)|
&\le4\log(n+1)+4\log4+(\log4)|Y_4|\\
&\le7\log n+14\log2\\
&\le\boxed{21\log n}.
\end{aligned}
\tag{L-32305.5}
\]

Thus the aligned innovation is deterministically logarithmic.

## 4. Domination by the critical reserve increment

PR #342 `L-34005` proves uniformly on the quarter-balanced cone, for

\[
n\ge N_0:=12005^2,
\]

that

\[
\boxed{
\Delta_4R(n,j)\ge(\log2)n\log n.
}
\tag{L-32305.6}
\]

On the same range,

\[
I_\circ(n,j)^2\le441\log^2n.
\]

Use the elementary inequalities

\[
\log2>\frac12,
\qquad
\log n\le\sqrt n,
\]

and `sqrt(n)>=12005>882`. Then

\[
441\log^2n
\le441\sqrt n\log n
<\frac12n\log n
<(\log2)n\log n.
\]

Therefore

\[
\boxed{
|I_\circ(n,j)|^2<\Delta_4R(n,j)
}
\tag{L-32305.7}
\]

for every quarter-balanced aligned row with `n>=N_0`.

This proves PR #345's scalar innovation-square domination with the absolute constant `C=1` outside an explicit finite base.

## 5. Consequence for the scalar recurrence

PR #345 gives

\[
|U(4n,4j)|^2
\le|U(n,j)|^2+\frac{|I_\circ(n,j)|^2}{3n},
\qquad
U(n,j)=\frac{Q_4^{\rm phys}(n,j)}{\sqrt n}.
\]

Combining with (L-32305.7) and the upper bound `Delta_4R<480n log(2n)` gives

\[
\boxed{
|U(4n,4j)|^2
\le|U(n,j)|^2+160\log(2n)
}
\tag{L-32305.8}
\]

cofinally on every aligned quarter-balanced radix-four chain. Iteration gives only `O(log^2 X)` scalar forcing.

## 6. Essential scope firewall

Equation (L-32305.2) shows something just as important as the bound: the aligned innovation is **prime-free**. Therefore this scalar row cannot by itself be the all-zero pole frame.

The RH-sensitive proof must retain the independent carry-position variable or the independent Fourier pair before the square. PR #241's two-frequency block and the source-convolved Q4 assembly remain the correct physical scope.

Accordingly, (L-32305.7) closes the aligned scalar arithmetic estimate but does **not** prove the missing Hermitian source placement or RH.

## 7. Proof boundary

Closed here:

- exact prime-free aligned innovation formula;
- logarithmic factorial-ratio bound;
- logarithmic bare-gauge bound;
- `|I|<=21 log n`;
- cofinal `I^2<Delta_4R` with explicit threshold;
- scalar coefficient-one `O(log^2 X)` recurrence.

Open:

- the complete independent-frequency Q4 source-convolved block placement;
- continuous carry-position polarization;
- RH.
