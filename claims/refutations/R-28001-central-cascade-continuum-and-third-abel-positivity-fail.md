# R-28001 — The single-channel continuum cascade and fixed third-Abel repair fail

Claim ID: `R-28001`  
Title: Boundary knots destroy the claimed all-stage continuum positivity, and the third cumulative producer kernel has an exact negative row  
Status: **PROPOSED EXACT REFUTATION / SCOPE CORRECTION PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen targets:

```text
PR #280 head 6a2195f4c173dfc3db1ac42596dce58706062b28
PR #279 head d5fb54844711a0ecad6805298f749d07e9c2fcf4
```

Scope: refutes the all-stage positivity claim in `L-27702.7` and the cofinal third-kernel positivity proposed in `L-27801.12`; it does not refute the exact central residual identity, the two-pass packing theorem, the exact signed finite saturation, or RH.

## 1. The continuum operator

Extend

\[
W(x)=x^{-1/2}\log(1/x)
\]

by zero for `x>1`, and put

\[
(\mathcal Tf)(x)
=\sum_{k\ge1}\bigl[f(2kx)-f((2k+1)x)\bigr].
\tag{R-28001.1}
\]

The sum is finite at every positive `x`.  Its dilation coefficient is

\[
c(n)=
\begin{cases}
1,&n\text{ even},\\
-1,&n\ge3\text{ odd},\\
0,&n=1.
\end{cases}
\tag{R-28001.2}
\]

Hence

\[
\mathcal T^jW(x)
=\sum_{n\le1/x}c^{*j}(n)W(nx).
\tag{R-28001.3}
\]

## 2. Exact loss of monotonicity at the second iterate

For `n<=8`, the second Dirichlet-convolution power is

\[
c^{*2}(4)=1,
\qquad
c^{*2}(6)=-2,
\qquad
c^{*2}(8)=2,
\]

and the `n=8` term vanishes at `x=1/8` because `W(1)=0`. Thus

\[
\begin{aligned}
(\mathcal T^2W)(1/7)
&=\sqrt7\left[
\frac12\log\frac74
-\frac2{\sqrt6}\log\frac76
\right],\\
(\mathcal T^2W)(1/8)
&=\sqrt8\left[
\frac12\log2
-\frac2{\sqrt6}\log\frac43
\right].
\end{aligned}
\tag{R-28001.4}
\]

The exact directed rational checker `X-28001` proves

\[
\boxed{
(\mathcal T^2W)(1/7)-(\mathcal T^2W)(1/8)>\frac9{100}.
}
\tag{R-28001.5}
\]

Since `1/8<1/7`, the second iterate increases on this pair. It is not decreasing.

Therefore the inference

```text
D^m W >= 0
and D commutes with dilations
=> D^m T^j W >= 0 for every m,j
```

is invalid for the compactly stopped source.

## 3. Exact negativity at the third iterate

For `n<=16`, the only nonzero third-convolution coefficients contributing at `x=1/16` are

\[
c^{*3}(8)=1,
\qquad
c^{*3}(12)=-3,
\qquad
c^{*3}(16)=3,
\]

and again the endpoint term vanishes. Hence

\[
\boxed{
(\mathcal T^3W)(1/16)
=\sqrt2\log2-2\sqrt3\log\frac43.
}
\tag{R-28001.6}
\]

The exact interval replay proves

\[
\boxed{
(\mathcal T^3W)(1/16)<-\frac1{100}.
}
\tag{R-28001.7}
\]

Thus the continuum cascade does not merely lose monotonicity: it loses nonnegativity at the third iterate.

## 4. Where the proof lost the terms

The zero extension is continuous at `x=1` because `W(1)=0`, but its first derivative has a jump:

\[
W'(1)=-1.
\]

The second and higher distributional derivatives therefore contain an endpoint atom. Under the dilations in `mathcal T`, that atom propagates to every reciprocal knot `x=1/n`.

The identity

\[
D\mathcal T f=\mathcal TDf
\]

is valid only away from the moving support boundaries unless those atomic terms are included. Iterating the smooth formula drops exactly the knot ledger responsible for (R-28001.5)--(R-28001.7).

## 5. The fixed third-Abel repair also fails

Let the binary--ternary producer of PR #279 act on the third cumulative target

\[
w_Q^{(3)}(q)=\binom{Q-q+2}{2}\mathbf1_{q\le Q}.
\]

At the exact finite endpoint

\[
Q=X=520,
\qquad n=15,
\]

the standard-library `Fraction` reconstruction gives

\[
\boxed{
A_{w_{520}^{(3)}}(15)=-\frac{91}{256}.
}
\tag{R-28001.8}
\]

Therefore the proposed cofinal claim

\[
S_X(n,Q)\ge0
\]

for the third cumulative producer kernel is false. The finite scan through `Q<=80` did not reach the first retained mutation.

This refutes a fixed third-Abel ambient positivity theorem. It does not refute positivity of the actual critical producer, which remains a stronger source-specific statement.

## 6. Surviving scope

The following claims are not contradicted here:

1. the exact central carry pattern and residual formula of `L-27701`;
2. monotonicity of the first critical residual;
3. the unconditional two-stage nonnegative packing and its `3.624...` constant;
4. the exact support-halving signed finite saturation;
5. a future source-specific cycle repair or parity-paired boundary theorem;
6. RH.

The following claims must be withdrawn or rewritten:

```text
all continuum iterates are nonnegative and decreasing;
only the one-step lattice commutator obstructs the finite cascade;
third cumulative producer positivity is a valid cofinal repair.
```

## 7. Review mutation

Any future cascade proof must replay all three exact controls:

```text
T^2 W(1/7)-T^2 W(1/8) > 9/100;
T^3 W(1/16) < -1/100;
third-Abel producer A_(Q=520)(n=15) = -91/256.
```

A proof which differentiates through the stopped dilation sum without the reciprocal-knot atoms fails this mutation.