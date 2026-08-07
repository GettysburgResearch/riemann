# L-23701 — Exact Bohr lift of a signed balanced packet

Claim ID: `L-23701`  
Title: A fully recombined balanced Heath–Brown or Möbius packet has an exact multiplicative Bohr polynomial, and its physical block energy is the restriction of the corresponding Hermitian Gram to the prime Kronecker orbit  
Status: **PROPOSED EXACT ALGEBRA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #237  
Frozen inputs: PR #233 at `b64b9878006733e59e9c988de0c5e33242134afb`; PR #235 at `1a86fd1f645d0ca208c0689bf2f0b41ae6448858`; PR #234 at `2d5043070e15fe6be94307381f4023eaa48c17a5`

## 1. Source-bound balanced packet

Fix a packet order `K`, a logarithmic block `J`, and one balanced destination
`tau` after:

1. complete finite Heath–Brown or Möbius-resolvent expansion;
2. divisor expansion of every residual coefficient;
3. direct full-tuple Type-I/Type-II partition;
4. recombination of every tuple with the same destination and product;
5. retention of every cutoff, first-crossing, and transition source.

The resulting finite source is

\[
 d\nu_{K,\tau,J}
 =\sum_{n\in\mathcal N_{K,\tau,J}}a_{K,\tau,J}(n)\,\delta_{\log n},
 \tag{L-23701.1}
\]

where the coefficient `a(n)` is the **net signed coefficient after exact product
collisions have been combined**.  The associated signal and energy are

\[
 Q_{K,\tau,J}(x)
 =\sum_n a(n)H_K(x-\log n),
 \tag{L-23701.2}
\]

and

\[
 E_{K,\tau}(J)=\int_J^{J+1}|Q_{K,\tau,J}(x)|^2dx.
 \tag{L-23701.3}
\]

No rowwise absolute value is permitted in (L-23701.1).

## 2. Multiplicative Bohr lift

Let `P_J` be the finite set of primes dividing at least one active `n`.  Write

\[
 n=\prod_{p\in P_J}p^{v_p(n)}.
\]

On the finite torus

\[
 \mathbb T^{P_J}=\{(z_p)_{p\in P_J}:|z_p|=1\},
\]

define the exact Bohr polynomial

\[
 \boxed{
 \mathcal D_{K,\tau,J}(z)
 =\sum_n a(n)\prod_{p\in P_J}z_p^{v_p(n)}.}
 \tag{L-23701.4}
\]

The prime Kronecker orbit is

\[
 \kappa(t)_p=p^{-it}.
 \tag{L-23701.5}
\]

Therefore

\[
 \boxed{
 \mathcal D_{K,\tau,J}(\kappa(t))
 =\sum_n a(n)n^{-it}.}
 \tag{L-23701.6}
\]

Haar orthogonality on the full torus gives the exact Bohr diagonal

\[
 \boxed{
 \int_{\mathbb T^{P_J}}|\mathcal D(z)|^2dm(z)
 =\sum_n|a(n)|^2.}
 \tag{L-23701.7}
\]

This diagonal is computed **after** product collisions.  The sum of the squares
of the uncombined tuple rows is generally larger and is not an admissible
replacement.

## 3. Exact physical Gram

Put

\[
 K_{J,K}(u,v)
 =\int_J^{J+1}H_K(x-u)\overline{H_K(x-v)}dx.
 \tag{L-23701.8}
\]

Then

\[
 \boxed{
 E_{K,\tau}(J)
 =\sum_{m,n}a(m)\overline{a(n)}
 K_{J,K}(\log m,\log n).}
 \tag{L-23701.9}
\]

Equivalently, with the Fourier convention

\[
 H_K(y)={1\over2\pi}\int_{\mathbb R}\widehat H_K(t)e^{ity}dt,
\]

the physical energy is the Hermitian restriction of the two-frequency Bohr
kernel to the one-parameter orbit (L-23701.5), with the Fourier transform of the
unit block inserted between the two frequencies.  In particular, the correct
analytic object is

\[
 \mathcal D(\kappa(t))\overline{\mathcal D(\kappa(s))},
\]

not `mathcal D(kappa(t))^2`.

## 4. Reflected Selberg compatibility

The reflected Selberg identity on PR #226 produces the same Hermitian
orientation: the product identity at `sigma+it` and `sigma-it`, after subtracting
the two individual identities, contains

\[
 2\left|{\zeta'\over\zeta}(\sigma+it)\right|^2.
\]

After the finite double inverse expansion, its balanced source is therefore a
Hermitian ratio Gram of the form (L-23701.9).  This supplies a valid positive
starting point for a contagion or inverse theorem.  It does not by itself bound
the orbit restriction.

## 5. Exact collision classes

A pair of raw tuples with the same product has the same monomial in
(L-23701.4).  Such tuples must be summed before the reflected square is formed.
The coefficient of the zero ratio in the reflected Laurent polynomial is then
exactly

\[
 \sum_n|a(n)|^2,
 \tag{L-23701.10}
\]

which is the Bohr diagonal.  Any purported proof object whose zero-ratio
coefficient equals the rowwise square sum rather than (L-23701.10) has failed to
retain the signed arithmetic packet.

## 6. Proof boundary

Closed exactly:

- the finite multiplicative Bohr lift;
- the Kronecker-orbit restriction;
- the collision-first Bohr diagonal;
- the physical Hermitian Gram;
- compatibility with the reflected orientation.

Not closed:

- a bound comparing the local orbit Gram with the Bohr/lower-scale energies;
- the contagion theorem `BCT(K)`;
- RH.
