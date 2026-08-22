# L-102505 — Squared-core physical collapse is polylogarithmic

Claim ID: `L-102505`  
Status: **PROVED UNCONDITIONALLY**  
Created: 2026-08-22  
Depends on: `L-102500--L-102503`; finite Euler squaring  
RH status: **not assumed**

Let `H` be any Hilbert space carrying the multiplicative shifts `U_(p^2)` as
isometries, and let `f in H`. For a finite labelled prime set `P`, define the
squared-core packet

\[
\mathscr C_Pf
=
\prod_{p\in P}(I-p^{-1}U_{p^2})f.
\tag{L-102505.1}
\]

The two labelled copies of `67` are kept as separate coordinates.

## 1. Vector-valued Hardy realization

Define the `H`-valued polydisc polynomial

\[
G(z)=
\sum_{S\subseteq P}
(-1)^{|S|}
\left(\prod_{p\in S}p^{-1/2}\right)
U_{(\prod_{p\in S}p)^2}f\,z^S.
\tag{L-102505.2}
\]

Its Hardy norm is

\[
\boxed{
\|G\|_{H^2(\mathbb T^P;H)}^2
=
\prod_{p\in P}(1+p^{-1})\,\|f\|_H^2.
}
\tag{L-102505.3}
\]

Evaluate at the interior point

\[
z_p=p^{-1/2}.
\]

Then

\[
G((p^{-1/2})_p)=\mathscr C_Pf.
\]

The vector-valued reproducing-kernel estimate gives

\[
\begin{aligned}
\|\mathscr C_Pf\|_H^2
&\le
\prod_{p\in P}(1-p^{-1})^{-1}
\|G\|_{H^2}^2\\
&=
\boxed{
\prod_{p\in P}\frac{1+p^{-1}}{1-p^{-1}}\,\|f\|_H^2.
}
\end{aligned}
\tag{L-102505.4}
\]

## 2. Polylogarithmic cost

Mertens' prime-product theorem implies

\[
\boxed{
\prod_{p\le Z}\frac{1+p^{-1}}{1-p^{-1}}
\ll (\log(2Z))^2.
}
\tag{L-102505.5}
\]

The extra labelled `67` contributes only one fixed additional factor.
Therefore

\[
\boxed{
\|\mathscr C_Zf\|_H
\ll \log(2Z)\,\|f\|_H.
}
\tag{L-102505.6}
\]

This estimate is uniform in the number of squared primes and requires no
source sign cancellation.

## 3. Simultaneous CV/XD application

The channel operators

\[
A=\partial_u,
\qquad
B=\frac12(\partial_u+\tfrac32)
\]

commute with every `U_(p^2)`. Hence (L-102505.6) applies simultaneously to the
common mother, the smoothed-CV channel, and the same-`K1` XD channel.

Thus physical labelled-to-unlabelled collapse of the **entire squared
small-prime core** has only polylogarithmic cost.

## Exact remaining scope

The theorem does not control a unique unsquared largest-prime owner or the
moving-cutoff transfer atom. Those are not interior polydisc evaluations at
summable activity. Consequently `AR-OCC102500` is reduced to the literal
unsquared owner/collar sector rather than the full core.
