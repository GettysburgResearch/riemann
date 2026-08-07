# T-23201 — Full RH proposal by terminal Selberg–Hankel contraction

Claim ID: `T-23201`  
Title: High-order centered prime packets reduce the full RH problem to a finite terminal Selberg–Hankel certificate family with vanishing scale loss  
Status: **FULL PROPOSAL PENDING INDEPENDENT REVIEW — `STC(K)` OPEN**  
Authoring agent: `gpt56-pro-21`  
Created: 2026-08-07  
Issue: #232  
Base: PR #158 at `9ee33527aef3acbb281ebad367aeb1e51652d006`  
Cross-branch inputs: PR #229 at `1daf03443265ce36cfb6efbd8de1ca9c702de793`; PR #216 at `b76eef1b769584aa9d66d082bfc6634126f986a2`  
Scope: complete proposed proof architecture; RH is not claimed proved

## 1. Global spectral front door

For every integer `K>=2`, use the compact high-order safe window

\[
H_K=H^{[K+1]}
\]

from `L-15155`. Its transform:

- has sufficiently rapid vertical decay;
- has zeros only on the two boundary lines;
- is nonzero throughout the open counterexample strip.

Let

\[
\mathcal B_{J,K}
=
\int_J^{J+1}
\left|
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
H_K(x-\log n)
\right|^2dx.
\tag{T-23201.1}
\]

The reviewed Hardy transfer `L-15151` identifies, for every fixed `K`,

\[
\boxed{
\limsup_{J\to\infty}
\frac{\log(1+\mathcal B_{J,K})}{2J}
=
\Theta_\zeta,
}
\tag{T-23201.2}
\]

where

\[
\Theta_\zeta
=
\sup_{\zeta(\rho)=0}
\left(\Re\rho-\frac12\right).
\]

Thus proving a sequence of upper bounds on the block exponent, with the bound
tending to zero as `K` increases, proves RH.

## 2. Exact finite packet

For endpoint `X=exp(J+O_K(1))`, the exact finite Heath–Brown identity and
dictionary of `L-15156` produce:

- every coefficient tuple;
- exact signed binomial multiplicities;
- a deterministic Type-I/Type-II partition;
- reduced-complexity and terminal Type-I flags;
- all cutoff and transition residuals;
- a finite positive auxiliary-energy vector.

The high-order null quotient of `L-15155` allows a packet companion to be
removed only after exact membership in the declared null space has been
certified. All remaining sources stay in the packet.

All tuple rows sharing a destination are recombined with their exact signs
before any norm.

The fixed-reserve partition `L-15157` permits one number

\[
0<\delta<\frac12
\]

to be chosen independently of `K`. Balanced packets lie below
`(1-delta)J+O_K(1)`, while every Type-I row exposes a complementary packet below
`delta J+O_K(1)`. Thus the linear increasing-order target is `eta_K -> 0`;
there is no artificial `1/K` loss in the scale reserve.

## 3. Reduction to terminal rows

Apply `L-23203` to the finite packet dictionary.

Balanced Type-II rows are routed to strict lower-scale auxiliary energies.
Reduced Type-I rows are eliminated by finite induction on coefficient-word
complexity. After this well-founded elimination, the complete block satisfies

\[
\mathcal B_{J,K}
\le
e^{o_K(J)}
\left[
1+T_K(J)
+\max_{u\le(1-\delta)J+O_K(1)}M_K(u)
\right],
\tag{T-23201.3}
\]

where `T_K(J)` is the maximum over the explicit finite terminal Type-I family.

No packet other than this declared terminal family remains an independent
arithmetic obligation.

## 4. Terminal Selberg–Hankel closure

Assume `STC(K)` of `L-23204` for every terminal packet. Namely, each terminal
kernel admits a source-bound majorization by a finite positive mixture of the
explicit exponential Selberg adjoints, plus a declared lower-scale residual,
and the complete forcing ledger satisfies

\[
T_K(J)
\le
\exp\{(\eta_K+o_K(1))J\}
\left[
1+\max_{u\le(1-\delta)J+O_K(1)}M_K(u)
\right].
\tag{T-23201.4}
\]

Then `L-23203` yields a closed finite-vector recurrence, and `T-15122` gives

\[
\boxed{
2\Theta_\zeta
\le
\frac{\eta_K}{\delta}
}
\tag{T-23201.5}
\]

in the linear case, or

\[
2\Theta_\zeta
\le
\frac{\eta_K}{1-\kappa_K}
\tag{T-23201.6}
\]

for the tensor recurrence.

Because `delta` is fixed and positive, it is enough to prove `STC(K)` for an
unbounded sequence of orders with

\[
\boxed{
\eta_K\longrightarrow0.
}
\tag{T-23201.7}
\]

The tensor alternative still requires
`eta_K/(1-kappa_K) -> 0`. Under either condition,

\[
\Theta_\zeta=0.
\]

Functional-equation symmetry gives

\[
\boxed{\mathrm{RH}.}
\tag{T-23201.8}
\]

## 5. Scalar Möbius audit

The proposal is not permitted to hide the scalar arithmetic difficulty inside
a generic operator norm.

`L-23003/T-23002` prove that the first critical Farey cell is

\[
\left(\frac{i}{2\pi}+\frac1{2\pi^2}\right)
\left[M(D)-M(2D/3)\right],
\tag{T-23201.9}
\]

and square-root control of this one row is RH-equivalent.

`L-23201` supplies the exact finite Möbius resolvent packet, while `L-23202`
shows that every high-order geometric difference of the same Mertens increment
retains the full RH exponent.

Therefore every claimed `STC(K)` packet must include a mutation proving that its
terminal closure implies the corresponding high-order Mertens bound. This
prevents recurrence coefficients or positive adjoints from silently deleting
the coherent first-cell mode.

## 6. Why this proposal is narrower than `CP(K)`

The prior proposal `M-15112` grouped all unresolved analytic work under
`CP(K)`. The present proposal separates it into:

1. **finite exact algebra and acyclicity**, already reviewable;
2. **balanced and reduced packet routing**, a finite list of normal-form
   inequalities;
3. **one terminal certificate family `STC(K)`**, the sole independent
   arithmetic hinge.

A reviewer need not re-audit the full repository or every auxiliary packet.
The decisive questions are:

- Does every same-scale edge reduce complexity?
- Is every terminal row declared?
- Does the positive Hankel mixture dominate the actual terminal kernel?
- Is the Selberg forcing ledger source bound with the correct signs?
- Does the residual route to a genuinely lower scale?
- Does the coefficient exponent `eta_K` tend to zero?
- Does the certificate control the first-cell Mertens mutation?

## 7. Proof-producing form

For each order `K`, a finite proof object contains:

```text
safe-window and normalization digests
complete Heath-Brown tuple manifest
signed destination packets
complexity DAG and terminal list
all null companions and transition residuals
terminal kernels
positive exponential weights and exponents
Hankel Gram/Loewner certificates
Selberg forcing and linear-reserve intervals
lower-scale residual routes
eta_K, fixed delta, or kappa_K
first-cell Mertens mutation
```

A standard-library consumer can verify every finite algebraic and Loewner gate.
The all-order conclusion additionally requires a symbolic rate theorem or an
unbounded proof-producing family; finitely many passing orders do not imply RH.

## 8. Exact status

```text
safe Hardy front door                         PROPOSED / inherited
high-order null quotient                      PROPOSED EXACT
finite Heath-Brown packet                     PROPOSED EXACT
fixed-reserve packet partition                PROPOSED EXACT
finite Möbius resolvent                       PROPOSED EXACT
high-order Mertens equivalence                PROPOSED EXACT
well-founded terminal reduction               PROPOSED EXACT
positive Selberg-Hankel adapter                PROPOSED EXACT
STC(K) construction with eta_K -> 0           OPEN
Riemann Hypothesis                            UNPROVED
```

This is a full proposal with one explicitly named arithmetic certificate family.
It is not a completed proof of `STC(K)` or RH.
