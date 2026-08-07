# O-23701 — Carry firewalls and failed shortcuts

Claim ID: `O-23701`  
Status: `PROPOSED OBSERVATION / SCOPE BOUNDARY`

## 1. Square-root prefix firewall

For the exact Green tail of `L-23701`, define the arithmetic coefficient

\[
R_m(n)
 =m\mu(n/m)\mathbf1_{m|n}
 +\sum_{\substack{\ell|n\\\ell>m}}\mu(n/\ell).
\tag{O-23701.1}
\]

Then

\[
r_{X,m}=m(m-1)s_{X,m}
 =\sum_{n\le X}\frac{R_m(n)}{\sqrt n}\log\frac Xn.
\tag{O-23701.2}
\]

Writing

\[
A_m(t)=\sum_{n\le t}\frac{R_m(n)}{\sqrt n},
\tag{O-23701.3}
\]

partial summation gives

\[
\boxed{r_{X,m}=\int_m^X A_m(t)\frac{dt}{t}.}
\tag{O-23701.4}
\]

Thus a proof that every `A_m(t)>=0` would imply the weaker exact-tail positivity
`s_(X,m)>=0`. This is a crisp scalar target, but its Dirichlet series contains
`1/zeta`; it must not be described as a routine divisor estimate.

## 2. Exact coefficient total variation is not a bypass

Because

\[
G_n=\frac n2+O(\log n),
\]

one might try to prove only

\[
\sum_n|c_X(n)|\log n=X^{o(1)}.
\]

But the exact inverse contains the full reciprocal-zeta channel. A bound strong
enough to force the critical prime-ramp cancellation is another form of the
RH-bearing theorem unless it exploits additional positive structure. The phase
frame instead builds its certificate from coefficients already proved
nonnegative.

## 3. A single unphased geometric ladder loses a fixed constant

Take the complete outer block at endpoints `X,X/5,X/5^2,...` and keep the four
bands tied to one common weight at each endpoint. The continuum spill estimate
produces a valid scalar renewal, and a linearly growing weight sequence improves
it, but the critical entropy mass stops at a fixed fraction of `4` (the natural
continuum calculation gives `15/16`).

A fixed fractional loss is fatal. This is why `T-23701` splits the four quotient
bands and retains the phase `log T mod log5`.

The `15/16` calculation is a warm-up, not a theorem used by the proposal.

## 4. Generic smooth densities are insufficient

Replacing the exact outer atoms by a smooth scale density makes the continuum
operator easy to estimate, but a generic approximation error of size `eta`
loses `eta sqrt X`. Taking `eta` merely to zero is not enough; the error must be
`X^{o(1)}` in absolute size.

The critical Mellin conservation in `L-23704` is designed precisely to avoid a
relative-error proof.

## 5. Tail positivity alone does not give the main term

Even if one proves `s_(X,m)>=0` for the exact inverse, the identity

\[
P_X=s_{X,2}\log2+\sum_{m\ge3}s_{X,m}L_m
\]

still needs a lower bound with the exact constant `4`. Positivity prevents
cancellation but does not itself determine the total critical mass.

The phase-frame theorem combines positivity and near-saturation in one finite
certificate.

## 6. Relationship to the balanced Möbius core

The first Farey cell and the fixed-ratio Mertens shell show that any method which
estimates the actual Möbius vector by an unsigned operator norm has already lost
the problem. The carry frame does something different:

- it never estimates a Möbius shell absolutely;
- it changes the dual basis to average binomial rows;
- all prime-power weights become nonnegative by Legendre/Kummer;
- the remaining signed Möbius information is confined to proving positivity of
  the four outer atoms, where only `mu(1),...,mu(4)` occur;
- the global task becomes positive phase renewal.

This is the proposed mechanism by which the elementary route could genuinely
evade generic BTP rather than rename it.
