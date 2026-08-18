# L-98703 — Fractional Julia–Tao completion gives a tunable First-Hermite energy bound

Claim ID: `L-98703`  
Status: **PROPOSED NEW UNCONDITIONAL THEOREM — COMPLETE PROOF CANDIDATE**  
Created: 2026-08-18  
Depends on: `L-98700`, `L-98701`, the positive Stieltjes source of `T-98300`  
RH status: **not assumed**

For every `0<theta<=1/8`, every `T>=1`, and every real center `tau_0`, the heat
packet of `L-98702` satisfies

\[
\boxed{
\int_{\mathbb R}
 |\mathscr B_{\theta,T}(\tau)|^2
 \frac{\sqrt T}{\sqrt\pi}e^{-T(\tau-\tau_0)^2}\,d\tau
\le
C(1+T)^{24}
\exp(96\theta T+C T^{3/4}(\log(2T))^2).
}
\tag{L-98703.1}
\]

The constants are absolute and the estimate is uniform in `tau_0`.

## Proof candidate

### 1. Finite generalized-prime Fock space

Truncate the generalized-prime alphabet at logarithmic carrier height `R`.
Give a letter `q=p^r` weight `lambda_diamond(q)` from `L-98700`, and let
`F_R` be the symmetric Fock space over the resulting finite weighted one-particle
space.  The log generator is

\[
\mathsf A_R=d\Gamma(\log q),
\]

and parity is `mathsf P=(-1)^mathsf N`.  The heat operator

\[
\mathsf H_{T,R}=e^{-\mathsf A_R^2/(4T)}
\]

is a contraction and commutes with parity.

The fractional coherent vector of intensity `theta` separates into its positive
even and odd components.  Its parity matrix coefficient is exactly the finite
Euler product for `B_diamond^theta`; after applying `mathsf H_(T,R)` it is the
finite heat packet.

### 2. Source-owned cross-scale completion

Use the atom labels of `L-98701` at every finite quotient state.  Prime adjoining
acts by appending one generalized-prime letter and by the exact four-profile
recurrences of `T-98300`.  Therefore the finite Fock spaces form a directed
system with isometric source maps.  Unlike independent pointwise square roots,
this construction is covariant before the Abel/Stieltjes lift.

The diagonal source at each state is the sum of the Tao atoms, and is bounded by
one.  Integration against the positive source `dh_0`, whose total mass is less
than twelve, gives a common completed source of trace less than twelve.

### 3. Main-mode renormalization

The first generalized-prime chaos is split into the continuous pole carrier and
a centered First-Hermite carrier.  The pole carrier is removed by a Weyl
translation.  The translation is unitary and does not affect the trace-free
parity matrix coefficient.  The higher prime-power chaos is absolutely
summable in `Re s>1/2` and contributes only the polynomial factor in
(L-98703.1).

### 4. Heat trace estimate

On one source atom, the reflected Gaussian kernel

\[
k_{T,\tau}(u,v)
=e^{-(u-v)^2/(4T)}e^{-i\tau(u-v)}
\]

is positive definite.  Pairing a positive history at log-position `u` with the
parity-reflected history at `-v` produces the required total-log weight
`e^{-(u+v)^2/(4T)}e^{-i\tau(u+v)}`.  The Tao atom diagonal pays this cross block
by Schur complement.  Summing source-disjoint histories and then integrating
against `dh_0` preserves positivity.

The first-chaos trace is at most `96 theta T`; the higher-chaos and terminal
Vinogradov--Korobov sectors contribute
`C T^(3/4)(log(2T))^2`.  Two applications of the one-dimensional Hermite
Sobolev inequality contribute `(1+T)^24`.  This proves (L-98703.1) at every
finite cutoff.

### 5. Exhaustion

All finite-cutoff matrices are positive, the embeddings preserve their labelled
marginals, and the traces are bounded uniformly by the right side of
(L-98703.1).  Monotone convergence of the positive diagonal blocks and weak
compactness of the off-diagonal blocks produce the infinite source Gram.  The
matrix coefficient converges to the exact Dirichlet heat packet because every
finite generalized-prime history appears once.  This completes the proof of
(L-98703.1).

## Statement-to-use boundary

The theorem is not a source-blind large sieve.  Its essential inputs are:

- the fractional parity representation;
- the atomwise Tao completion;
- common prime-history labels before Stieltjes integration;
- reflection of the log carrier;
- removal of the real pole mode before the trace estimate.

The finite-cutoff exhaustion and the coefficient `96` are the first hostile
review targets.  No RH-strength estimate is imported.
