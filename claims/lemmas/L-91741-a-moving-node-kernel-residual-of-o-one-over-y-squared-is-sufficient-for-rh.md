# L-91741 — A moving-node kernel residual of o(1/Y^2) is sufficient for RH

Claim ID: `L-91741`  
Status: **EXACT CONDITIONAL KERNEL-RATE THEOREM**  
Created: 2026-08-13  
Depends on: `L-91720/L-91721`, `L-91740`  
RH status: **unproved**

## 1. One-node residual

At one moving node `eta`, suppose the canonical completed source lock gives

\[
A(\eta)
=
C(\eta)
+
H(\eta)
+
E(\eta),
\tag{L-91741.1}
\]

where

```text
A  arithmetic source;
C  critical plus stable output;
H  hyperbolic crossed-zero port;
E  auxiliary port;
```

and all four scalar quantities are nonnegative.

Put

\[
r(\eta)=A(\eta)-C(\eta)=H(\eta)+E(\eta).
\tag{L-91741.2}
\]

Then

\[
0\le H(\eta)\le r(\eta).
\]

## 2. Entropy conversion

The annular Clark entropy is

\[
\Lambda^{\rm ann}(\eta)
=
\log(1+2\eta H(\eta)).
\]

Therefore

\[
\boxed{
\Lambda^{\rm ann}(\eta)
\le
\log(1+2\eta r(\eta)).
}
\tag{L-91741.3}
\]

This converts a canonical kernel residual bound into the entropy bound needed
by the moving-node moat theorem.

## 3. Exact finite threshold

For a depth-height box `delta<=x<=b`, `|y|<=Y`, choose

\[
\eta_*=\sqrt{b^2+Y^2}
\]

and let

\[
m_*
=
\frac{2\delta}
{\sqrt{b^2+Y^2}+b}.
\]

If

\[
\boxed{
r(\eta_*)
<
\frac{e^{m_*}-1}{2\eta_*},
}
\tag{L-91741.4}
\]

then the box contains no crossed zero.

Indeed (L-91741.3) makes the total annular entropy strictly smaller than the
charge forced by one zero.

## 4. Cofinal rate

For fixed `delta,b`,

\[
\frac{e^{m_*}-1}{2\eta_*}
=
\frac{\delta}{Y^2}
+O_{\delta,b}(Y^{-3}).
\]

Hence

\[
\boxed{
r(\eta_*(Y))=o(Y^{-2})
}
\tag{L-91741.5}
\]

excludes every fixed off-line zero in the box.

If the canonical kernel residual has this rate on every dyadic annulus, RH
follows.

## 5. Significance

The conclusion-producing target is now a positive-kernel estimate at a single
moving node:

```text
arithmetic source kernel
minus critical/stable kernel
    = o(1/Y^2).
```

The stronger entropy target `o(1/Y)` is recovered automatically.
