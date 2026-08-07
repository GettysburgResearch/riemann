# L-23203 — Well-founded reduction of centered packet systems to terminal rows

Claim ID: `L-23203`  
Title: A finite scale/complexity packet dictionary can be eliminated exactly until only strict lower-scale terms and an explicit terminal forcing family remain  
Status: **PROPOSED EXACT COMPOSITION LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-21`  
Created: 2026-08-07  
Issue: #232  
Dependencies: `L-15156`, `L-23201`; elementary induction  
Scope: finite auxiliary-energy systems

## 1. Packet order

Fix an identity order `K`. Let `mathfrak P_K` be a finite packet dictionary.
Every packet type `tau` has:

- a nonnegative energy `E_tau(J)`;
- a complexity rank `c(tau)` in `{0,...,C_K}`;
- a scale destination;
- one of the labels `balanced`, `reduced`, or `terminal`.

The exact dictionaries of `L-15156` and `L-23201` are examples.

Let

\[
M_K(X)=1+\max_{\tau}\max_{0\le J\le X}E_\tau(J).
\tag{L-23203.1}
\]

Assume all coefficients below are nonnegative and have logarithm `o_K(J)` for
fixed `K`.

## 2. Nonterminal row hypotheses

A balanced packet obeys

\[
E_\tau(J)
\le A_\tau(J)
+\sum_h b_{\tau h}(J)
 \max_{u\le(1-\delta_K)J+C_K}E_h(u),
\tag{L-23203.2}
\]

or a tensor analogue whose weighted scale sum is at most `kappa_K<1`.

A reduced-complexity packet obeys

\[
\begin{aligned}
E_\tau(J)\le A_\tau(J)
&+\sum_{c(h)<c(\tau)}
 a_{\tau h}(J)E_h(J+C_K)\\
&+\sum_h b_{\tau h}(J)
 \max_{u\le(1-\delta_K)J+C_K}E_h(u).
\end{aligned}
\tag{L-23203.3}
\]

Here `A_tau` consists only of explicitly declared terminal forcing packets and
finite source terms. No undeclared transition or cutoff row may be placed in
`A_tau`.

## 3. Finite complexity elimination

Order the packet types by increasing complexity. For complexity zero,
(L-23203.3) contains no same-scale packet. Suppose all ranks below `r` have
already been expressed in terms of:

1. terminal forcing at scale `J+O_K(1)`;
2. energies at scale at most `(1-delta_K)J+O_K(1)`;
3. finite source terms.

Substituting those expressions into every rank-`r` row gives the same form. The
number of substitutions is bounded by the finite dictionary size, and a finite
product or sum of `exp(o_K(J))` coefficients remains `exp(o_K(J))`.

Induction therefore proves:

\[
\boxed{
M_K(J)
\le
e^{o_K(J)}
\left[
1+T_K(J)
+\max_{u\le(1-\delta_K)J+O_K(1)}M_K(u)
\right],
}
\tag{L-23203.4}
\]

where `T_K(J)` is the maximum of the complete declared terminal forcing family.

For tensor rows, the same elimination preserves the tensor scale weight
`kappa_K`, because same-scale complexity substitution does not change the
physical scale arguments.

## 4. Terminal forcing theorem

Suppose the terminal family satisfies

\[
\boxed{
T_K(J)
\le
\exp\{(\eta_K+o_K(1))J\}
\left[
1+\max_{u\le(1-\delta_K)J+O_K(1)}M_K(u)
\right].
}
\tag{L-23203.5}
\]

Then (L-23203.4) becomes a closed finite-vector recurrence with coefficient
exponent `eta_K`. The scale-contraction theorem `T-15122` gives

\[
\limsup_{J\to\infty}\frac{\log M_K(J)}J
\le\frac{\eta_K}{\delta_K}
\tag{L-23203.6}
\]

in the linear case, or `eta_K/(1-kappa_K)` in the tensor case.

Thus **only the terminal packet family needs an independent arithmetic
estimate**. Balanced and reduced-complexity rows are bookkeeping once their
declared inequalities have been established.

## 5. Exact review consequence

A claimed proof packet must contain:

```text
complete type dictionary
complexity rank for every type
all same-scale edges
proof that every same-scale edge lowers complexity
all strict-scale destinations
the complete terminal type list
all transition and cutoff residuals
coefficient exponents
```

The checker must reject:

- a cycle among same-scale reduced-complexity rows;
- an undeclared terminal row;
- a same-scale edge with unchanged complexity;
- a lower-scale destination above the declared contraction;
- total variation before signed row recombination.

## 6. Proof boundary

The induction is exact. It does not prove the row inequalities
(L-23203.2)--(L-23203.3), nor the terminal estimate (L-23203.5). Its contribution
is to reduce the broad `CP(K)` obligation of `M-15112` to one explicit terminal
forcing theorem plus a finite acyclicity audit.
