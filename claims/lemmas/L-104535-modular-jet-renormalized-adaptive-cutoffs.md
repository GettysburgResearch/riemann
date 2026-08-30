# L-104535 — Modular jet-renormalized adaptive theta cutoffs

Claim ID: `L-104535`  
Status: **PROVED EXACT APPROXIMATION THEOREM**  
Created: 2026-08-23  
Depends on: `L-104531--L-104533`, `R-104518`  
RH status: **not assumed**

`R-104518` shows that a raw finite theta-orbit sum retains a spurious third-
order cusp at the modular fixed point and therefore has an eventually negative
Laguerre tail.  This theorem removes that artifact to arbitrary finite order
without altering the complete conclusion-facing source.

## 1. Omitted modular jets

Let

\[
G_N=\sum_{n\le N}g_n,
\qquad
j_{N,r}=G_N^{(2r+1)}(0+)
\qquad(r\ge1).
\]

The complete source `g=u^2 Phi` is smooth and even, so

\[
\boxed{
j_{N,r}=-\sum_{n>N}g_n^{(2r+1)}(0+).}
\tag{L-104535.1}
\]

For every fixed `R`, the explicit theta tail gives

\[
\boxed{
|j_{N,r}|\le C_RN^{C_R}e^{-\pi N^2}
\qquad(1\le r\le R).
}
\tag{L-104535.2}
\]

## 2. Exact jet correction

Choose once and for all an even cutoff `chi in C_c^infinity(R)` which equals
one on a neighbourhood of zero. Define

\[
\psi_r(u)=\frac{|u|^{2r+1}}{(2r+1)!}\chi(u).
\]

On the positive half-line, the only nonzero odd derivative of `psi_r` at zero
through any fixed finite order is

\[
\psi_r^{(2r+1)}(0+)=1.
\]

For `R>=1`, put

\[
\boxed{
\widetilde G_{N,R}(u)
=G_N(u)-\sum_{r=1}^{R}j_{N,r}\psi_r(u).
}
\tag{L-104535.3}
\]

Then

\[
\boxed{
\widetilde G_{N,R}^{(2r+1)}(0+)=0
\qquad(1\le r\le R).
}
\tag{L-104535.4}
\]

Thus the even extension is smooth through order `2R+1` at the modular fixed
point.

## 3. Strong approximation remains exponential

Every correction coefficient is an omitted theta-tail jet. Consequently, for
every fixed pair `J,R`,

\[
\boxed{
\|(1+|u|)^J(\widetilde G_{N,R}-g)\|_{L^1(du)}
\le C_{J,R}N^{C_{J,R}}e^{-\pi N^2}.
}
\tag{L-104535.5}
\]

The same estimate holds for every fixed number of distributional derivatives
up to the matched order. Therefore the Fourier transforms and the corresponding
Laguerre profiles differ uniformly by an explicit exponentially small error.

## 4. Artificial high-frequency tail is postponed

Let

\[
\widetilde F_{N,R}=\widehat{\widetilde G_{N,R}}.
\]

Repeated integration by parts gives

\[
\boxed{
\widetilde F_{N,R}(t)=O_{N,R}(|t|^{-2R-4}).
}
\tag{L-104535.6}
\]

If the next unmatched odd jet is nonzero, its Laguerre profile is again
negative at sufficiently large height.  Hence a fixed finite `R` is still not
a global proof.  The point is quantitative: the spurious `t^{-4}` mode of the
raw cutoff has been removed, and the alias can be pushed to arbitrary order.

## 5. Fail-closed adaptive certification criterion

Let

\[
\widetilde\Lambda_{N,R}(t)
=(\widetilde F_{N,R}'(t))^2
-\widetilde F_{N,R}(t)\widetilde F_{N,R}''(t).
\]

For every finite `T`, a directed proof of

\[
\widetilde\mu_{N,R,T}
=\min_{|t|\le T}\widetilde\Lambda_{N,R}(t)>0
\]

combined with the explicit comparison error from (L-104535.5) proves

\[
\mathcal L_2(t)>0
\qquad(|t|\le T)
\]

whenever the margin exceeds that error.

A cofinal proof may therefore choose

\[
N=N(T)\to\infty,
\qquad
R=R(T)\to\infty
\]

and certify overlapping intervals.  It may not hold either parameter fixed
while sending `T` to infinity.

## 6. Preferred implementation

The cleanest implementation is actually to evaluate the complete carrier-
subtracted Jacobi mother `B` of `L-104534` on a central modular neighbourhood,
and to use the theta-orbit expansion only in the tails.  The jet-matched
construction proves that this hybrid protocol has a finite algebraic surrogate
with an explicit error ledger.

This theorem advances the cofinal route from a false fixed-cutoff proposal to
a source-faithful adaptive certification theorem. It does not supply the
required cofinal directed margins.