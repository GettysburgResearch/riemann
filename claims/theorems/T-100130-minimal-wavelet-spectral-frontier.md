# T-100130 — Minimal-wavelet spectral frontier and positive-kernel firewall

Claim ID: `T-100130`  
Status: **EXACT SPECTRAL CHARACTERIZATION; RH UNPROVED**  
Created: 2026-08-20  
Frozen base: PR #674 at `714efd9f837b5349e5295c5064237375ee69798e`  
RH status: **unproved**

Let `Q_X` be the exact Cauchy--Poisson square of the ordinary-Möbius compact
kernel `K_0` from PR #674 and put

\[
\mathscr E(Y)=\int_1^YQ_X{dX\over X^3}.
\]

Then `L-100130/L-100131` prove

\[
\boxed{
\mathscr E(Y)=Y^{o(1)}\iff RH.
}
\tag{T-100130.1}
\]

More generally,

\[
\mathscr E(Y)=O_\epsilon(Y^{2\theta+\epsilon})
\quad\Longrightarrow\quad
\Re\rho\le\frac12+\theta
\]

for every nontrivial zeta zero.

The `MWOC99910` integral satisfies

\[
\mathrm{MWOC}(Y)^2
\le64\log Y\,\mathscr E(Y).
\]

Thus RH implies `MWOC99910`; PR #674 proves the converse. The final Hardy
packing is therefore exactly RH-equivalent. It cannot be supplied by a
diagonal bound, a generic labelled-source collapse, or an estimate valid for
arbitrary coefficient packets.

`R-100130` additionally proves that the positive floor-kernel criterion of
T-100120 cancels the zeta detector identically:

\[
\sum_m\mu(m)K_Q(N/m)=\sum_{j\le N}q_j,
\]

and its transform is `Q(s)/s`. It is not an RH criterion.

## Correct conclusion graph

```text
minimal compact ordinary-Mobius kernel       exact
Poisson/Hardy tail identity                  exact
Mellin transform                             exact
wavelet L2 abscissa = Theta+1/2              proved
critical cumulative energy subpower <=> RH  proved
MWOC99910 <=> RH                             proved across PR #674 + this packet
positive floor-kernel escape                 refuted: zeta cancels
new unconditional RH proof                   not obtained
Riemann Hypothesis                           unproved
```

The shortest honest remaining objective is the signed ordinary-Möbius
cross-core estimate itself. This packet closes the analytic and normalization
interfaces and prevents a tautologically positive transform from being
mistaken for that estimate.