# T-107000 — Near-quadratic Nyquist compression of the native beta RH criterion

Claim ID: `T-107000`  
Status: **UNCONDITIONAL THEOREM / RH-EQUIVALENT FINITE-RANK CRITERION**  
Created: 2026-08-27  
Base: PR #758 at `070be728e8d434bfb72645e23f9894acf920d3c0`  
RH status: **unproved**

Fix any \(\ell,\varepsilon>0\) and integer \(r\ge1\). The logarithmic box
cascade in `L-107000` produces one fixed compact smooth source-faithful beta
detector \(B_{r,\log}\). For every fixed \(A>0\), define \(P_X\),
\(t_{k,X}\), and \(K_A(X)\) as in `L-107001`.

Then

\[
\boxed{
\mathrm{RH}
\Longleftrightarrow
\frac1{P_X}
\sum_{|k|\le K_A(X)}
\left|
\widehat B_{r,\log}(it_{k,X})
\sum_{n\le X}
\frac{\beta(n)}{n^{1/2+it_{k,X}}}
\right|^2
=
X^{o(1)}.
}
\tag{T-107000.1}
\]

The discarded lattice tail is \(O_A(X^{-A})\), and

\[
\boxed{
2K_A(X)+1
=
O_A\!\left(
(\log X)^2
[\log\log(e^eX)]^2
\right).
}
\tag{T-107000.2}
\]

Equivalently, RH is characterized by the norm of one native beta vector in a
deterministic feature space of almost-quadratic polylogarithmic dimension.

## What is unconditional

```text
compact C-infinity probability smoother             PROVED
zero-free right-half-plane Laplace product           PROVED
near-exponential Fourier envelope                    PROVED
every-power tail beyond log X (loglog X)^2           PROVED
exact global Nyquist identity                        PROVED
almost-quadratic finite-rank truncation               PROVED
preservation of the individual-zeta beta source      PROVED
equivalence of the finite-rank criterion with RH      PROVED
the finite-rank norm bound itself                     OPEN / RH-EQUIVALENT
Riemann Hypothesis                                    UNPROVED
```

## Why this is a genuine reset

The theorem bypasses the completed-source, owner-pair, QPTI, Hodge and
family-individualization lineages. It acts directly on

\[
\beta=(\delta_1-\delta_{67})*\mu
\]

and the fixed individual-zeta Mellin--Landau detector. The only remaining
problem is arithmetic cancellation in a deterministic feature space of
dimension

\[
(\log X)^{2+o(1)},
\]

rather than an unbounded continuum of frequencies or a source-blind physical
collapse.

## Next exact target

Define `NBV107000` to be the estimate

\[
\left\|
\sum_{n\le X}
\frac{\beta(n)}{\sqrt n}\mathbf v_X(n)
\right\|^2
=
X^{o(1)}.
\]

Then

\[
\boxed{
\mathrm{NBV}_{107000}
\Longleftrightarrow
\mathrm{RH}.
}

A serious next attack should work on the native multiplicative phase vectors
\(\mathbf v_X(n)\) themselves: blockwise hyperbola decomposition, signed
Möbius discrepancy on the logarithmic circle, or a source-faithful
large-sieve theorem. It must not infer smallness merely from the low rank.
