# M-23701 — Fail-closed review protocol for the greedy carry–parity proposal

Methodology ID: `M-23701`  
Title: Freeze, replay, mutate, and review the aggregate digital blocker theorem without importing Carry Saturation or RH under another name  
Status: **PROPOSED REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Dependencies: `L-23701`--`L-23703`, `T-23701`  
Scope: independent adversarial review and production certificates

## 1. Freeze rule

A review must record:

```text
repository
PR number
head SHA
base SHA
all imported dependency SHAs
checker source SHA-256
certificate SHA-256
```

Later repairs are new proposals and do not retroactively verify a frozen proof.

## 2. Review the finite algebra first

The reviewer should independently reconstruct:

1. the count of carry-producing `j` values in `L-23701.1`;
2. the Kummer/Legendre identity `G_n=sum Lambda(q) beta_(nq)`;
3. the minimum-ratio greedy recursion;
4. nonnegativity of every residual after one step;
5. complete feasibility `B_X d_X<=w_X`;
6. the entropy lower bound;
7. the prime-ramp contraction;
8. the two binary parity/digit convolution identities.

Failure of one finite identity rejects the corresponding component before DBT
is considered.

## 3. Mandatory mutations

Every checker and proof should include at least:

```text
wrong remainder convention in beta_(nq)
missing q=n diagonal candidate
negative target coordinate
minimizer changed after rounding
residual widened through zero
one prime-power row deleted
one blocker tie reordered
binary parity identity changed at N=4
digit identity changed at N=2
entropy constant strengthened without proof
finite positive ladder promoted to asymptotic DBT
```

The `q=n` row is load bearing because it guarantees that the greedy minimum
exists. Directed intervals meeting a ratio tie must remain unresolved or retain
all possible blockers.

## 4. Exact status labels

Use the following labels separately:

```text
EXACT FINITE ALGEBRA
DIRECTED FINITE CERTIFICATE
EMPIRICAL RECONNAISSANCE
PROPOSED ASYMPTOTIC THEOREM
CONDITIONAL RH DEDUCTION
```

A finite run, regardless of size, does not prove DBT. A midpoint logarithm or
square root is not a proof input. A proposed quotient-layer inequality cannot be
recorded as an exact identity.

## 5. DBT rejection conditions

Reject a proposed proof of DBT if it uses any of the following without a new
proved theorem:

- positivity of the exact triangular inverse `c_X`;
- a generic lower singular-value bound for the parity comb;
- rowwise absolute values before complete quotient-layer grouping;
- deletion of an off-diagonal blocker;
- a fixed outer fraction whose entropy mass loses a positive multiple of
  `sqrt(X)`;
- an error `epsilon sqrt(X)` with fixed `epsilon>0`;
- a finite list of quotient layers;
- a continuum limit without a directed finite-discretization error;
- a reflected Selberg square with the actual carry/slack source omitted;
- a generic Type-II estimate that does not emit the greedy finite object.

## 6. Required proof-producing ledger for DBT

A claimed completion should emit, for every scale block:

```text
all quotient cells
all exact blocker indices
all endpoint ties
all digit layers used
all reflected-square terms
all lower-scale routes
all boundary charges
block entropy mass
block logarithmic mass
cumulative deficit
```

The proof must show that every same-scale charge cancels or is paid by a
nonnegative conditional-variance term. Every uncancelled term must route to a
strictly smaller endpoint or to an explicit polylogarithmic boundary budget.

## 7. First-cell and parity firewalls

A carry proof must reproduce both external scalar firewalls.

### Mertens firewall

Through PR #236's causal ratio transfer, the result must imply

\[
M(D)-M(\lfloor2D/3\rfloor)
=O_\varepsilon(D^{1/2+\varepsilon}).
\]

### Digital firewall

It must preserve

\[
\sum_{m\le N}b_2(m)
\mathbf1_{\{\lfloor N/m\rfloor\text{ odd}\}}=0
\quad(N\ge4)
\]

and

\[
\sum_{m\le N}b_2(m)s_2(\lfloor N/m\rfloor)=-1
\quad(N\ge2).
\]

A proof that does not see these coherent rows has discarded the central
Möbius mode.

## 8. Production recommendation

The first useful production object is not a huge endpoint. It is a complete
symbolic quotient-layer packet for a modest exact `X`, containing:

- the full rational carry matrix;
- directed target weights;
- every greedy residual and blocker;
- an exact base-2 and base-3 carry decomposition;
- a comparison with the exact triangular inverse;
- the entropy and lower-order masses;
- mutation tests.

The reviewer should then demand a symbolic all-`X` quotient-cell identity before
accepting large reconnaissance as evidence for DBT.

## 9. Status boundary

This protocol does not assume DBT and does not claim RH. It is designed so that
a failed aggregate theorem leaves the exact greedy minorant and digital
dictionary reusable.