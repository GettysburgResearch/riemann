# L-99991 — Closed phase symbol of the symmetric Hasse boundary and exact neutral-mode annihilation

Claim ID: `L-99991`  
Status: **PROVED EXACT FOURIER/PRODUCT IDENTITY; PHASE PACKING OPEN**  
Created: 2026-08-20  
Depends on: `L-99990`  
RH status: **unproved**

Use the notation of `L-99990`. Put

\[
z_h(\gamma)=p_h^{i\gamma}
\]

and, for \(i\in B\),

\[
B_i^\pm(t,\gamma)
=
\prod_{h\ne i}
\left[
1-a_ht\pm a_h(1-t)z_h(\gamma)
\right].
\tag{L-99991.1}
\]

For the exponential test potential \(\Phi_\gamma(P)=P^{i\gamma}\), the Fourier
symbol of the odd-boundary functional is

\[
\boxed{
\mathscr S_B(\gamma)
=
\frac12\sum_i a_i(1-z_i(\gamma))
\int_0^1
\left[B_i^+(t,\gamma)-B_i^-(t,\gamma)\right]dt.
}
\tag{L-99991.2}
\]

## Proof

For fixed \(i,t\), expansion of \(B_i^\pm\) gives

\[
\prod_{h\ne i}
[1-a_ht\pm a_h(1-t)z_h]
=
\sum_{A\subseteq B\setminus\{i\}}
(\pm1)^{|A|}w(A)(1-t)^{|A|}
z_A
\prod_{h\notin A\cup\{i\}}(1-a_ht).
\]

Taking half the difference selects odd \(A\). Multiplication by
\(a_i(1-z_i)\) is exactly the Fourier transform of
\(\Phi(P_A)-\Phi(p_iP_A)\). Integrating in \(t\) gives (L-99991.2).

## Neutral-mode cancellation

Every summand contains \(1-z_i(\gamma)\), hence

\[
\boxed{\mathscr S_B(0)=0.}
\tag{L-99991.3}
\]

The logarithmic derivative at the origin is explicit:

\[
\mathscr S_B'(0)
=
-\frac i2\sum_i a_i\log p_i
\int_0^1
[B_i^+(t,0)-B_i^-(t,0)]dt.
\tag{L-99991.4}
\]

Thus the order-\(1/\log\log Y\) neutral residual of independent cube matching
is annihilated before physical collapse. What remains is genuinely nonzero
phase.

For the Cauchy density

\[
P_\tau(\gamma)=\frac{\tau}{\pi(\tau^2+\gamma^2)}
\]

one also has the exact edge gap

\[
\boxed{
\int_{\mathbb R}|1-p^{i\gamma}|^2P_\tau(\gamma)d\gamma
=
2(1-p^{-\tau}).
}
\tag{L-99991.5}
\]

At \(\tau=1\) this is at least one for every prime label. Therefore no positive
boundary mass is phase-invisible after Cauchy averaging.

## Remaining theorem

For the fixed zero-safe box potential, bandwise Fourier/Stieltjes inversion
turns the complete cross-core boundary into the symbol (L-99991.2). The
remaining theorem `PSCP99990` is a source-specific subpower estimate for that
nonzero-phase integral after the native \(1/p\) normalization and physical
half-order observation.

This is not `HTOC99810` or `DGOC99810`: PR #671 proves those root-containing
positive squares RH-equivalent. Here the neutral root is removed algebraically
by \(1-z_i\) before the phase packing estimate.
