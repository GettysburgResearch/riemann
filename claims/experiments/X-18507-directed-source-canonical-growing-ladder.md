# X-18507 — Directed source-canonical growing D-0001 ladder

Claim ID: `X-18507`  
Status: `DIRECTED FINITE LADDER — ALL RETAINED LEVELS CERTIFIED; COFINAL CLAIM NOT PROVED`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-01  
Dependencies: `D-0001`; `L-18512`; `T-18504`  

## Exact production object

In the unnormalised even basis

\[
b_0=e_0,
\qquad b_k=e_{-k}+e_k,
\]

the metric is

\[
G_N=\operatorname{diag}(1,2,\ldots,2).
\]

The source functional, its metric representer, and an exact basis of its kernel
are

\[
\ell_N(x)=x_0+2\sum_{k=1}^N x_k,
\qquad
Q_W=(1,\ldots,1)^T,
\qquad
Q_E^{(k)}=-2e_0+e_k.
\]

Thus

\[
G_W=1+2N,
\qquad
G_E=2I_N+4\mathbf 1\mathbf 1^T.
\]

For every retained support the producer includes every prime power `q <= c`,
the complete cutoff-free pole block, and the complete archimedean block. It
emits

\[
Q_W,P_W,E_W,Z_W,C,X_N,\mathscr R_N,G_W,
\qquad
\mathscr R_N=Z_W-CX_N.
\]

The independent exact consumer proves

\[
C-hG_E\succ0
\]

and then the direct residual-shorting LMI

\[
\mathscr D_N-mG_W\succ0.
\]

## Directed result

At 384 and 512 MPFR bits, with higher-precision interval containment, the nine
levels

\[
(10,2),(20,3),(50,4),(100,5),(200,6),
(500,7),(1000,8),(2000,9),(5000,10)
\]

all satisfy

\[
\boxed{
\Delta_{c,N}
=
\left[G_W^{-1/2}\mathscr D_NG_W^{-1/2}\right]_-
=0.
}
\]

The normalized directed floors range from approximately

\[
0.08251754261
\]

to

\[
0.02213524967.
\]

All retained classifications are

```text
CERTIFIED_DELTA_ZERO_SOURCE_CANONICAL_DIRECT_BLOCK.
```

The retained summary SHA-256 is

```text
5cb0bda48a65ec6ee896ca37d8e9920ea2ed7349bac66b2cdd935c087364c26c.
```

## Proof boundary

This experiment proves nine exact finite signs. It does not prove an unbounded
sequence, and its source-canonical split has not been identified with the
spectral deficit-canonical augmentation of `L-18901`. In particular, no
statement

\[
\|\Delta_{\lambda,N(\lambda)}\|\to0
\]

or RH conclusion follows solely from this finite ladder.
