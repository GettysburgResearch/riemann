# L-101102 — Exact SHARP-to-minimal-wavelet derivative bridge

Claim ID: `L-101102`  
Status: **PROVED EXACT KERNEL AND SOURCE IDENTITY**  
Created: 2026-08-21  
Frozen inputs: PR #674 at `9962f7f712adc6b4ad72672ecfeace028ba79bdb`  
RH status: **not assumed**

Let

\[
S_af(y)=f(y/a)
\]

with zero extension below one, let

\[
\mathscr D=(I-\sqrt2S_2)(I-S_2)^2,
\]

and write

\[
D=y{d\over dy}.
\]

Retain the factor-67 box kernel `W`, the SHARP kernel

\[
T(y)=(4\sqrt y-3)\mathbf1_{y\ge1},
\]

and the minimal lower-shell wavelet `K_0` from PR #674.

## Kernel identity

Direct differentiation of the two branches of `W` gives

\[
\boxed{DW=(I-S_{67})T.}
\tag{L-101102.1}
\]

PR #674 proves

\[
\boxed{\mathscr DW=(I-S_{67})K_0.}
\tag{L-101102.2}
\]

Scale shifts commute with `D`. Applying `D` to (L-101102.2) and `mathscr D`
to (L-101102.1) yields

\[
(I-S_{67})(\mathscr DT-DK_0)=0.
\]

The difference is causal and vanishes below one. If `(I-S_67)F=0`, then
`F(y)=F(y/67)`; iteration reaches the zero region. Therefore `F=0`, and

\[
\boxed{\mathscr DT=DK_0.}
\tag{L-101102.3}
\]

## Source identity

Let

\[
h_\beta(X)=\sum_n{\beta(n)\over\sqrt n}T(X/n),
\qquad
G_\beta(X)=\sum_n{\beta(n)\over\sqrt n}K_0(X/n),
\]

and

\[
G_\mu(X)=\sum_n{\mu(n)\over\sqrt n}K_0(X/n).
\]

Finite source convolution commutes with `mathscr D` and `D`. Hence

\[
\mathscr Dh_\beta=DG_\beta.
\]

The duplicate-67 source identity gives

\[
G_\beta=(I-67^{-1/2}S_{67})G_\mu.
\]

Consequently

\[
\boxed{
\mathscr Dh_\beta
=(I-67^{-1/2}S_{67})DG_\mu.
}
\tag{L-101102.4}
\]

Since `I-67^(-1/2)S_67` has a positive finite-endpoint resolvent,

\[
\boxed{
DG_\mu
=\sum_{k\ge0}67^{-k/2}S_{67}^k\mathscr Dh_\beta
}
\tag{L-101102.5}
\]

with only finitely many active terms at each `X`.

## Consequence

CV and XD are not unrelated terminal criteria. The minimal wavelet is the
carrier-annihilating dyadic derivative of the same SHARP source, followed by
one positive factor-67 resolvent.

The bridge does not turn a one-sided bound on `h_beta` into a bound on `G_mu`:
`mathscr D` has signed coefficients and its critical inverse is power-sized. It
identifies the common source-faithful interface that any combined proof must
preserve.
