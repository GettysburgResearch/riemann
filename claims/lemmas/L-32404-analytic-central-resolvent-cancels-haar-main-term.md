# L-32404 — Analytic central resolvent cancels the Haar main term exactly

Claim ID: `L-32404`  
Title: The infinite shifted central cascade contributes exactly `-log X + log(2)/zeta(1/2)` to the critical Haar bottom telescope, so all nonconstant RH-bearing behavior is finite-cutoff boundary behavior  
Status: **PROPOSED COMPLETE EXACT/ANALYTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-s`  
Created: 2026-08-08  
Dependencies: `L-32403`; PR #286 `L-28401` strict analytic-bank contraction  
Scope: exact infinite analytic resolvent; no bound for the finite-cutoff correction and no RH claim

## 1. Bottom functional

Retain the critical Haar source `nu_2` from `L-32403` and define

\[
\boxed{
 \mathcal B(f)
 =-(1+\sqrt2)f(2)+\sqrt2 f(3)+\sqrt2 f(4).
}
\tag{L-32404.1}

Let `mathscr C` be the infinite shifted central operator

\[
 (\mathscr C f)(q)
 =\sum_{k\ge1}
 [f(2kq-1)-f((2k+1)q)].
\tag{L-32404.2}

For

\[
 p_s(q)=q^{-s},
\]

PR #286 proves that the complete Dirichlet–Taylor expansion of `mathscr C` is strictly contracting in its coefficient norm for every real `s>=1/2`.

## 2. Resolvent identity

Initially for real `s>1`, all sums below are absolutely convergent. Applying the finite central carry identity to longer and longer truncations, or directly summing the absolutely convergent first differences, gives

\[
\boxed{
 \mathcal B(p_s)
 =\langle\nu_2,(I-\mathscr C)p_s\rangle_{q\ge2}.
}
\tag{L-32404.3}

Iterating and using the analytic-bank decay gives

\[
\begin{aligned}
 \sum_{a\ge0}\mathcal B(\mathscr C^a p_s)
 &=\langle\nu_2,p_s\rangle_{q\ge2}\\
 &=\sum_{q\ge2}{\nu_2(q)\over q^s}.
\end{aligned}
\]

By `L-32403`,

\[
\boxed{
 S(s):=
 \sum_{a\ge0}\mathcal B(\mathscr C^a p_s)
 ={1-2^{1/2-s}\over\zeta(s)}-1.
}
\tag{L-32404.4}

The coefficient-bank contraction of `L-28401` supplies locally uniform convergence down to every real `s>=1/2`, so (L-32404.4) continues to that boundary by the same analytic representation.

## 3. Critical value

At `s=1/2`,

\[
1-2^{1/2-s}=0.
\]

Since `zeta(1/2)` is finite and nonzero,

\[
\boxed{S(1/2)=-1.}
\tag{L-32404.5}

Thus the pure critical power contributes exactly one negative unit through the complete infinite central resolvent.

## 4. Logarithmic companion

Because `mathscr C` is independent of the Mellin exponent,

\[
 \partial_s\mathscr C^a p_s
 =\mathscr C^a\partial_s p_s.
\]

The logarithmic companion is

\[
 q^{-s}\log q=-\partial_s p_s(q).
\]

Differentiating (L-32404.4) at `s=1/2` gives

\[
\boxed{
 S'(1/2)
 ={\log2\over\zeta(1/2)}.
}
\tag{L-32404.6}

Indeed the numerator in (L-32404.4) vanishes at `1/2`, so the derivative of `1/zeta` does not contribute.

## 5. Exact cancellation of the `log X` main term

Define the **uncut** critical logarithmic profile

\[
 w_X^\infty(q)
 =q^{-1/2}\log(X/q)
 =\log X\,p_{1/2}(q)
   +\left.\partial_s p_s(q)\right|_{s=1/2}.
\tag{L-32404.7}

Equations (L-32404.5)--(L-32404.6) imply

\[
\boxed{
\sum_{a\ge0}
 \mathcal B(\mathscr C^a w_X^\infty)
 =-\log X+{\log2\over\zeta(1/2)}.
}
\tag{L-32404.8}

The full Haar Riesz shell of `L-32403` contains the unit coordinate

\[
\nu_2(1)w_X(1)=\log X.
\]

Therefore the complete infinite analytic model is exactly the constant

\[
\boxed{
 \log X+
 \sum_{a\ge0}
 \mathcal B(\mathscr C^a w_X^\infty)
 ={\log2\over\zeta(1/2)}.
}
\tag{L-32404.9]

(The closing bracket in the tag is typographical only.)

No asymptotic estimate is used: the large logarithmic main term cancels identically.

## 6. Consequence for the full problem

Let `r_a^(X)` denote the exact **finite stopped** central cascade of `L-32403`, and let

\[
 u_a^{(X)}=\mathscr C^a w_X^\infty
\]

be the infinite analytic cascade. Then (L-32403.18) and (L-32404.9) give the exact structural decomposition

\[
\boxed{
 \mathcal H_2(X)
 -{\log2\over\zeta(1/2)}
 =\sum_a
 \mathcal B\bigl(r_a^{(X)}-u_a^{(X)}\bigr),
}
\tag{L-32404.10}

where the finite side terminates and the analytic side is absolutely/resolvent summable in the `L-28401` bank. Equivalently, all `X`-dependent arithmetic difficulty lies in the complete finite-cutoff boundary Duhamel correction.

Thus the critical dyadic Riesz-shell criterion is no longer a cancellation between a size-`log X` unit term and an opaque `O(log X)` bottom ledger. The entire analytic `log X` cancellation is closed exactly. A proof only has to control the net cutoff correction in (L-32404.10).

## 7. New scalar completion target

A sufficient theorem is

\[
\boxed{
 \sum_a
 \mathcal B\bigl(r_a^{(X)}-u_a^{(X)}\bigr)
 =X^{o(1)}.
}
\tag{HBC}

Together with (L-32404.9), this gives `HDS` of `L-32403`, hence RH.

`HBC` is a scalar boundary theorem. It does not require a norm estimate for every propagated state. The complete boundary must still be retained before the bottom functional is applied.

## 8. Proof boundary

Established here, subject to review:

1. the exact analytic central resolvent in the critical Haar source;
2. `S(1/2)=-1`;
3. `S'(1/2)=log(2)/zeta(1/2)`;
4. exact cancellation of the `log X` unit term;
5. reduction of all nonconstant arithmetic behavior to the finite-cutoff boundary correction.

Not established:

1. `HBC`;
2. `HDS`;
3. RH.
