# L-100411 — Free labelled phase packing is polylogarithmic; the sole loss is physical half-order collapse

Claim ID: `L-100411`  
Status: **PROVED FREE-PACKET BOUND + EXACT REMAINING INTERFACE**  
Created: 2026-08-20  
Depends on: `L-100410`  
RH status: **unproved**

Use the notation of `L-100410` and put

\[
A=\sum_i a_i,
\qquad
\Pi=\prod_i(1+a_i).
\]

For \(|\eta|\le1\),

\[
|1-a_it+\eta a_i(1-t)z_i|\le1+a_i.
\]

The area formula therefore gives

\[
\boxed{
|\mathscr S_B(\gamma)|
\le
\frac{\Pi A}{2}
\sum_i a_i|1-p_i^{i\gamma}|.
}
\]

For the Cauchy phase law

\[
P_\tau(\gamma)
=
\frac{\tau}{\pi(\tau^2+\gamma^2)},
\]

one has

\[
\int_{\mathbb R}|1-p^{i\gamma}|^2P_\tau(\gamma)d\gamma
=
2(1-p^{-\tau}).
\]

Weighted Cauchy--Schwarz now yields

\[
\boxed{
\int_{\mathbb R}
|\mathscr S_B(\gamma)|^2P_\tau(\gamma)d\gamma
\le
\frac12\Pi^2A^4.
}
\]

At the literal normalized-box activities

\[
a_p=\frac1p
\]

with one extra labelled \(67\),

\[
A=O(\log\log Y),
\qquad
\Pi=O(\log Y).
\]

Hence the complete free labelled phase packet is polylogarithmic.

## The exact half-order wall

The conclusion-facing physical observation is not the free labelled packet.
Same-product physical collapse changes the effective critical activity from

\[
p^{-1}
\]

to the half-order scale

\[
p^{-1/2}.
\]

At that point the preceding Euler-product bound loses its summability.  This is
the sole remaining interface:

```text
PHPC100410:
the physical collapse operator, restricted to the root-free phase-Hasse
range, has subpower norm on every fixed zero-safe shell.
```

`PHPC100410` is strictly narrower than the root-containing HTOC/DGOC squares,
but it is not proved by the free estimate above.  A source-blind cluster can
still amplify a diagonal packet, so the physical source/provenance restriction
must remain visible.
