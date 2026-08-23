# Sharp low-order Xi descent through Bezoutian pivots and a boundary Loewner kernel

Date: 2026-08-23  
Dedicated branch: `research/gpt56-pro/105200-xi-natural-scale-residue-coherence`  
Scientific status: **RH unproved**

## Remote publication audit

Before this continuation, PR #724 was read back remotely at exact head

```text
82ba4bdb824868dcf26d5d2f2d38b1e2af2d8631
```

and `L-105212` was fetched at that exact commit with blob

```text
eb148e8e15728ee29a20d0f760f5a659fde8683f
```

The complete changed-file inventory was also read from GitHub. The present
continuation is committed on the same branch and PR.

## Binding correction

The preceding `ESDE105212` condition is overstrong. The exact polynomial

\[
p(x)=x^5/5-7x^3-10x^2+8/5
\]

has five simple real zeros and all four critical residues negative, yet

\[
R(1-\mathfrak C)={946907\over459983}>2.
\]

Thus near-constant residues are not necessary for real-rootedness. The sharp
real-critical statement is the pointwise sign `rho_c<=0`.

## Exact finite theorem

For a real polynomial,

\[
\mathscr B_p(x,y)
={1\over n}p'(x)p'(y)
-
\sum_{p'(c)=0}
\rho_c{p'(x)\over x-c}{p'(y)\over y-c}.
\]

This is a congruence diagonalization. Therefore

\[
\operatorname{ind}_-(\mathscr B_p)
=\#\{c:\rho_c>0\}
={N_{\rm nr}(p)\over2}.
\]

At the critical points themselves the Bezoutian matrix is diagonal. A positive
residue is exactly one negative Hermite--Biehler pivot.

## Exact entire-window decomposition

For an entire real function in one bounded regular window,

\[
{F\over F'}
=H_{F,\Omega}
+
\sum_{F'(c)=0}{\rho_c\over z-c},
\]

where `H_(F,Omega)` is the boundary Cauchy integral. Consequently,

\[
\mathscr B_F
=\mathscr R_{F,\Omega}
-
\sum_c\rho_cq_c\otimes q_c,
\]

with

\[
\mathscr R_{F,\Omega}(x,y)
=F'(x)F'(y){H(x)-H(y)\over x-y}.
\]

The boundary remainder vanishes on real critical-point rows and columns. It
cannot mask a positive residue. The two PR #720 last-defect alternatives are
therefore exact orthogonal coordinates:

```text
PRES event     negative diagonal residue pivot;
HARG event     negative square of one boundary Loewner kernel.
```

## New unconditional fixed-low-order geometry

The Bezoutian itself is the chord average

\[
\mathscr B_F(x,y)
=\int_0^1\Gamma_F((1-t)x+ty,tx+(1-t)y)dt
\]

of polarized Laguerre phase numerators. For `F=Xi^(k)`, its center average is

\[
\int_\mathbb R\mathscr B_F(m+h/2,m-h/2)dm
=4\pi\int_\mathbb R
u^{2k+2}\varphi(u)^2{\sin(hu)\over hu}du.
\]

This is strictly positive on an explicit short-chord interval. The remaining
problem is fixed-center/all-packet localization, not absence of mean source
orientation.

## Sharp frontier

The new conditional theorem is

```text
PRES105220:
  every real critical residue at the last defective level is nonpositive;

BRP105220:
  the entire-window boundary Cauchy function has a PSD all-packet Loewner
  kernel under the exact Xi exhaustion, with no nonreal critical correction.
```

Then

\[
\mathrm{PRES105220}\wedge\mathrm{BRP105220}\Longrightarrow RH.
\]

Neither gate is proved. Packet-size-three actual-Xi Pick positivity does not
bootstrap abstractly to `BRP105220`; an exact four-by-four separator is frozen
in `R-105203`.

## Replay

```text
PASS_X_105220_BEZOUTIAN_BOUNDARY_DECOMPOSITION
```

The exact rational/Sturm replay performs 182 checks and explicitly records:

```text
esde105212_canonical = false
pres105220_proved     = false
brp105220_proved      = false
rh_established        = false
```
