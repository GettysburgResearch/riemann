# T-23202 — Corrected full RH proposal by terminal Euler closure and balanced Type-II contraction

Claim ID: `T-23202`  
Title: Exact high-order prime packets, corrected Type-I reduction, and one signed balanced Type-II theorem imply RH  
Status: **FULL CORRECTED PROPOSAL PENDING INDEPENDENT REVIEW — `BTP(K)` OPEN**  
Authoring agent: `gpt56-pro-21`  
Created: 2026-08-07  
Issue: #232  
Base: PR #158 at `9ee33527aef3acbb281ebad367aeb1e51652d006`  
Scope: complete conditional proof architecture; RH is not claimed proved

## 1. Safe global front door

For every integer `K>=6`, let

\[
H_K=H^{[K+1]}
\]

be the compact high-order safe window of PR #158.  Its transform has boundary
zeros of the required order, sufficient vertical decay, and no zero in the open
counterexample strip.

Define the complete von-Mangoldt block energy

\[
\mathcal B_{J,K}
=
\int_J^{J+1}
\left|
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
H_K(x-\log n)
\right|^2dx.
\tag{T-23202.1}
\]

The inherited safe-filter Hardy transfer gives, for every fixed `K`,

\[
\boxed{
\limsup_{J\to\infty}
\frac{\log(1+\mathcal B_{J,K})}{2J}
=
\Theta_\zeta,
}
\tag{T-23202.2}
\]

where

\[
\Theta_\zeta
=
\sup_{\zeta(\rho)=0}
\left(\Re\rho-\frac12\right).
\]

The prime-only and full-von-Mangoldt normal energies have the same polynomial
and subexponential status by the bridge on PR #158.

## 2. Exact finite packet

At endpoint `X=exp(J+O_K(1))`, the exact finite Heath--Brown identity supplies:

- every coefficient tuple and multiplicity;
- exact signed binomial and Möbius coefficients;
- a deterministic first-crossing partition;
- every cutoff and transition source;
- a finite auxiliary-energy dictionary.

All rows with the same destination are recombined with their exact signs before
any norm.  A null companion may be removed only after exact membership in the
high-order null space has been certified.

The finite Möbius resolvent `L-23201` supplies an independent scalar packet for
the same inverse-zeta obstruction, while `L-23202` records the RH-equivalent
fixed-ratio Mertens hierarchy.

## 3. Corrected fixed reserve

Fix

\[
\boxed{
\delta=\frac15
}
\tag{T-23202.3}
\]

and use `K>=6`.  The first-crossing theorem gives a strict logarithmic reserve.
The stronger condition `delta<1/3` permits the internal Type-I reduction of
`L-23206`.

Every exact packet row is routed, after signed source recombination, into one of
three classes:

1. a balanced Type-II destination whose two complete factor groups lie below
   `(1-delta)J+O_K(1)`;
2. a same-scale Type-I destination of strictly lower integer complexity;
3. a one-variable terminal lattice row.

Finite induction eliminates the second class without a same-scale cycle.

## 4. Terminal Type-I closure

At complexity one, the large variable is unrestricted.  All truncated Möbius
and first-crossing conditions lie in a small prefix

\[
A\le e^{\delta J+O_K(1)}.
\]

The terminal source has the exact lattice form of `L-23205`.  The high-order
half-pole moments annihilate the continuous main term, and one Euler remainder
gives

\[
\boxed{
E_{K,\mathrm{term}}(J)
\le
\exp\left[-\left(\frac35-o_K(1)\right)J\right].
}
\tag{T-23202.4}
\]

Thus every terminal and terminal-transition row has coefficient exponent zero.
No packet-to-global-Selberg identification is used.

## 5. Remaining balanced vector

Let `mathfrak B_K` be the complete finite balanced destination dictionary and
let `E_(K,tau)(J)` be the exact normal-Gram energies of `L-23207`.  Exact source
routing and Gram Cauchy--Schwarz give

\[
\mathcal B_{J,K}
\le
e^{o_K(J)}
\left[
1+
\sum_{\tau\in\mathfrak B_K}E_{K,\tau}(J)
+
\max_{u\le(1-\delta)J+O_K(1)}M_K(u)
ight],
\tag{T-23202.5}
\]

where the exponentially decaying terminal family has been absorbed into the
source term.

The only independent arithmetic estimate still required is the
source-specific balanced packet theorem `BTP(K)`.

## 6. Conditional balanced contraction

Assume that, for an unbounded sequence of orders, every balanced type satisfies

\[
E_{K,\tau}(J)
\le
\exp\{(\varepsilon_K+o_K(1))J\}
\left[
1+
\max_{\upsilon\in\mathfrak B_K}
\max_{u\le(1-\delta)J+O_K(1)}
E_{K,\upsilon}(u)
\right]
\tag{T-23202.6}
\]

and

\[
\boxed{
\varepsilon_K\longrightarrow0.
}
\tag{T-23202.7}
\]

The tensor alternative is allowed if its scale weight `kappa_K<1` and

\[
\varepsilon_K/(1-\kappa_K)\to0.
\tag{T-23202.8}
\]

Equations (T-23202.4)--(T-23202.6) give a complete finite-vector recurrence.
The scale-contraction theorem of PR #158 yields

\[
2\Theta_\zeta
\le
\frac{\varepsilon_K}{\delta}
=5\varepsilon_K
\tag{T-23202.9}
\]

in the linear case.  Letting `K` increase gives

\[
\Theta_\zeta=0.
\]

Functional-equation symmetry therefore proves

\[
\boxed{\mathrm{RH}.}
\tag{T-23202.10}
\]

## 7. Scalar Möbius firewall

The first positive critical Farey cell is exactly

\[
\left(\frac{i}{2\pi}+\frac1{2\pi^2}\right)
\left[M(D)-M(\lfloor2D/3\rfloor)\right],
\]

and `L-23202` proves that every fixed finite geometric difference retains the
full Mertens/RH exponent.

This is not presented as a machine decoder from an arbitrary balanced packet.
It is a proof firewall: any derivation of `BTP(K)` that replaces the actual
signed vector by a generic operator norm, deletes coherent low rows, or takes
rowwise absolute values has lost an RH-equivalent scalar and must be rejected.

## 8. Role of the Selberg--Hankel adjoint

The scalar positive adjoint of `L-23204` remains a useful candidate mechanism.
It may enter a proof of `BTP(K)` only after an explicit packet source map or a
coupled packet Selberg equation has been constructed with every cross term.
The aggregate centered-prime Selberg equation alone does not control the sum of
packet self-energies and is not a dependency of this theorem.

## 9. Review-efficient proof object

For each order, a production object contains:

```text
safe-window and normalization digests
complete Heath--Brown tuple manifest
signed destination recombination
corrected Type-I complexity DAG
terminal unrestricted-lattice records
Euler moment and remainder ledger
complete balanced packet list
factor intervals and boundary sources
normal-Gram source contractions
BTP linear/tensor recurrence
coefficient exponent epsilon_K
strict scale destinations
```

The all-order conclusion additionally requires a symbolic rate theorem or an
unbounded proof-producing family.  Finitely many passing orders do not imply RH.

## 10. Exact status

```text
safe Hardy transfer                         inherited / proposed
exact finite packet                         inherited / proposed exact
finite Möbius resolvent                     retained exact algebra
high-order Mertens equivalence              retained with notation fixes
corrected Type-I complexity reduction       proposed complete
terminal Euler closure                      proposed complete
balanced packet definition/certificate      proposed exact interface
BTP(K) construction                         open
vanishing balanced rate                     open
Riemann Hypothesis                          unproved
```

This is a complete corrected proposal with one explicitly named arithmetic
hinge.  It does not prove `BTP(K)` or RH.