# L-100162 — Log-interval coarea reduces critical activation debt to three endpoint Euler weights

Status: **PROVED EXACT KERNEL IDENTITY; CRITICAL HALF-ORDER ENDPOINT REMAINS**  
Created: 2026-08-20  
RH status: **unproved**

For the partial-activation correction in `L-100161`, write

\[
d(z)={(\sqrt z-1)^2\over z^{3/2}},\qquad z>1.
\]

Its logarithmic antiderivative is elementary:

\[
\boxed{
\int d(z){dz\over z}
={2\over z}-{2\over\sqrt z}-{2\over3z^{3/2}}+C.
}
\tag{L-100162.1}
\]

Equivalently, for one source integer `n` and endpoint variable `x<n`, putting `z=n/x` gives boundary primitives

\[
\boxed{
2{x\over n}-2{\sqrt x\over\sqrt n}
-{2\over3}{x^{3/2}\over n^{3/2}}.
}
\tag{L-100162.2}
\]

Thus the logarithmic integral of the entire signed upper-ideal correction over any activation interval is an exact linear combination of three endpoint parity sums with Dirichlet exponents

```text
1, 1/2, 3/2.
```

The `1` and `3/2` pieces are supercritical / absolutely convergent after the duplicate-67 Euler factor is inserted. The middle `1/2` term is the unique critical residue. Therefore integrating the activation correction does not eliminate the half-order arithmetic; it localizes it to activation endpoints.

In particular, any proof of subpower logarithmic negative mass based solely on interval integration must still control a half-order endpoint prefix. No interior estimate at exponents `1` and `3/2` can by itself remove that term.

This gives an exact coarea interpretation of the prime-harmonic wall: the continuum debt is supercritical away from activation, and the entire conclusion-producing obstruction is carried by the discrete half-order endpoint sequence.
