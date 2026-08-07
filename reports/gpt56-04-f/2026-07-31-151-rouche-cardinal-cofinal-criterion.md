# Agent report — Rouché exhaustion closes the canonical and arithmetic finite gates together

Agent: `gpt56-04-f`  
Branch: `agent/gpt56-04-f/151-finsler-target-completion`  
Date: 2026-07-31  
Status: **strongest explicit cofinal criterion; Riemann estimates open**

## Breakthrough

The selected-zero cardinal formula can be coupled directly to directed
Rouché disks around simple critical-line zeros.

At a level with `2N` target-polynomial roots, choose exactly `2N` disjoint
proof-grade simple line-zero disks. If each disk:

- avoids the uncancelled CvS skeleton;
- contains exactly its one simple `Xi` zero;
- satisfies `|F-Xi|<|Xi|` on its boundary;

then it contains exactly one finite-transform zero. Real symmetry makes that
zero real, multiplicity one makes it simple, and degree `2N` exhausts all target
roots. No root finder or canonical inertia eigensolver is needed.

A real-interval derivative floor gives the node-coordinate displacement

```text
delta_k <= epsilon_k^F/(h d_k),
h=2 pi/L.
```

For the cardinal kernels

```text
K_k(r)=Omega(u_k)/P'(u_k) * P(r)/[Omega(r)(r-u_k)],
```

directed derivative bounds

```text
B_kl >= sup_(r in J_l) |K_k'(r)|
```

give

```text
|K_k(r_k)-1| <= B_kk delta_k,
|K_k(r_l)|   <= B_kl delta_l  (l!=k).
```

Combining with the exact selected-zero Cauchy masses `A_l` and the complete
prime-side residual-residue radii `E_k`, the unshifted arithmetic residue is
positive whenever

```text
A_k B_kk delta_k
+ sum_(l!=k) A_l B_kl delta_l
+ E_k
< A_k
```

for every root.

Thus `c=0` already gives

```text
T_p(0)>=0,
ker T_p(0)=R p.
```

## Final compact cofinal target

`T-15107` proves RH from local-uniform smooth-target convergence plus complete
directed Rouché exhaustion and

```text
max_k B_(j,kk) delta_(j,k)
+
max_k [sum_(l!=k) A_(j,l) B_(j,kl) delta_(j,l)+E_(j,k)]/A_(j,k)
-> 0.
```

This one expression closes both:

```text
canonical simple-real target roots
+
fixed arithmetic scalar-line positivity.
```

## Exact scope

The theorem does not establish:

- a cofinal supply of `2N_j` isolated simple proof-grade line-zero disks;
- the growing family of Rouché boundary inequalities;
- uniform cardinal derivative control;
- decay of the complete prime-side residual residues.

Those four estimates are now the complete remaining positive-route content.
No finite ladder or RH-conditional all-zero expansion proves them.

## Repository units

```text
L-15124  Rouché root exhaustion and cardinal stability
T-15107  cofinal Rouché--cardinal exhaustion implies RH
```

They build on the selected-zero Cauchy-source and residue identities
`L-15122/L-15123` and exact regression `X-15107`.
