# L-102601 — The logarithmic phase connection has only one critical chaos

Claim ID: `L-102601`  
Status: **PROVED EXACT EXPANSION AND POLYLOGARITHMIC TAIL**  
Created: 2026-08-22  
Depends on: `L-102600`  
RH status: **not assumed**

For one labelled Euler factor

\[
e_p(\vartheta)=I-r_pe^{-i\vartheta}U_p,
\qquad r_p=p^{-1/2},
\]

work on any finite physical horizon, so every shift is nilpotent on the
restricted source.  Then

\[
\boxed{
-i(\partial_\vartheta e_p)e_p^{-1}
=
\frac{r_pe^{-i\vartheta}U_p}
{I-r_pe^{-i\vartheta}U_p}
=
\sum_{k\ge1}
r_p^ke^{-ik\vartheta}U_{p^k}.
}
\tag{L-102601.1}
\]

For the complete labelled product the logarithmic phase connection is the sum
of these one-prime connections.

## 1. Critical first chaos

The \(k=1\) term is

\[
p^{-1/2}e^{-i\vartheta}U_p.
\]

After greatest-owner projection and preceding-prefix completion it is exactly
the atom in `L-102600`.  It is therefore the only phase chaos which can meet the
moving completion transfer at critical half-order.

## 2. Higher prime powers

After physical collapse, let \(f\) lie in any Hilbert space on which all
multiplicative shifts are isometries.  For a horizon \(Y\), the higher-power
connection satisfies

\[
\begin{aligned}
\left\|
\sum_{\substack{p^k\le Y\\k\ge2}}
(\log p)p^{-k/2}U_{p^k}f
\right\|
&\le
\left[
\sum_{p\le\sqrt Y}
\frac{\log p}{p(1-p^{-1/2})}
\right]\|f\|\\
&\ll \log(2Y)\|f\|.
\end{aligned}
\tag{L-102601.2}
\]

The last estimate follows from the elementary Chebyshev bound

\[
\sum_{p\le x}\frac{\log p}{p}\ll\log(2x).
\]

Without the logarithmic weight, the same argument gives
\(O(\log\log(3Y))\).

Thus every phase-current prime power \(p^k\), \(k\ge2\), has only
polylogarithmic physical cost.  The unique critical obstruction is the
first-chaos owner/transfer current of `L-102600`.
