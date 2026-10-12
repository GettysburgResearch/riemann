# A sharper positive sector with only fourteen complementary dimensions

Status: PROPOSED_EXACT refinement; exact checker replay passes; independent
review pending.  Scope: the complete L=1 source-positive sector and its residual
enclosure, not the effective sign.  Source and domain: the same literal kernel,
primitive and inherited O1-O4 Fourier/coupling contract specified in
`CODIMENSION_18_COERCIVITY.md`.  No quasi-RH result or source-zero information
is used.  What was run: `check_codimension14.py`, normal Python and Python -O,
identical receipts; all acceptance uses explicit raises and exact arithmetic.

## Statement

Replace the 15 sine constraints in the preceding theorem by just the 11
constraints sin(j*pi*t), 1<=j<=11, keeping e^(+/-t/2) and cosh(3t/2).
The resulting V_14 has exactly codimension 14 and obeys

\[
q(h,h)\ge\frac65\|\phi_h'\|_2^2
 +\tau_2\left|\int_0^1\sinh(3t/2)h(t)dt\right|^2,
\qquad h\in V_{14}.
\tag{R1}
\]

Its newly defined 14-by-14 effective matrix consequently has

\[
U-(15/8)R\preceq S\preceq U,
\tag{R2}
\]

with Pi projecting off {1, cos(j*pi*t):1<=j<=11, sinh(3t/2)}.  U and R must
be formed afresh for this space; previous numerical matrices are not its entries.

## Exact all-frequency supporting line

Set x=omega², P(x)=(x+1/4)²/(x+9/4), alpha=13/10 and C=710.  The checker
proves rational enclosures

\[
\gamma<289/500,\quad \pi<3927/1250,\quad
\log2<1733/2500,\quad \log\pi<1431/1250,
\]

whose sum gives Omega(0)>-43/8.  Here gamma<H_1024-10log2 and the positive
atanh log series are used.  The pi enclosure follows from the exact Machin
identity pi=16atan(1/5)-4atan(1/239), with alternating rational series; it also
gives pi>31415/10000.  The rational comparison sqrt2>707/500 then yields
q_2=log2/sqrt2<491/1000.  The digamma partial fractions give

\[
V_2(\omega)>v_{14}(x):=-43/8-491/500+
\sum_{k=0}^{256}\frac{16x}{(4k+1)((4k+1)^2+4x)}.
\]

Both P and v_14 increase.  Using exactly the sign-aware endpoint product
enclosure explained in the preceding proof, but downward floors at scale
2^100, the checker covers all 4096 cells [a,a+1], 0<=a<=4095, and proves

\[
P(x)v_{14}(x)\ge(13/10)x-710\qquad(0\le x\le4096).
\]

The smallest strict cell margin exceeds 2.68, on [1418,1419].  At x=4096
the rational lower v_lo exceeds alpha, and C>(7/4)v_lo.  For every larger
x, P(x)>=x-7/4 and v_14(x)>=v_lo therefore give

\[
P(x)v_{14}(x)\ge v_{\rm lo}(x-7/4)
\ge\alpha x-C.
\]

This encloses the entire unbounded frequency domain, not a finite mesh alone.
No cosine-phase estimate is needed; only cos<=1 was used.

## Coercivity and residual coefficient

The exact source/primitive Fourier identity implies

\[
q_2(h,h)\ge b\bigl((13/10)\|\phi'\|_2^2-710\|\phi\|_2^2\bigr).
\]

Eleven removed sine modes give ||phi||²<=||phi'||²/(12²*pi²).  The checked
rational inequality is

\[
\frac32\left(\frac{13}{10}-
 \frac{710}{144(31415/10000)^2}\right)>\frac65.
\]

The exact full source beyond the first prime cusp adds the nonnegative sinh
moment after the cosh constraint, proving R1.  All clamped endpoint, continuity,
Riesz-completion and residual-Gram arguments are identical in form for the
changed finite subspace, with b²/(6/5)=15/8, proving R2.

The arithmetic lemma is deliberately stronger than needed for the old
codimension-18 theorem.  This refinement establishes a smaller finite positive
sector complement; it does not prove a new effective sign or certify any
sampled matrix.  The whole-window lower certificate remains the next task.
