# T-104500 — Xi Riccati–Pick edge-defect cascade

Claim ID: `T-104500`  
Status: **UNCONDITIONAL REVERSE-ROLLE THEOREMS + EXACT CONDITIONAL RH CASCADE**  
Created: 2026-08-22  
Base programme: PR #714 at `d1a9fea34aa0620a5cb2da41061518638ab8b219`  
RH status: **unproved**

## 1. What is now unconditional

The following parts of Levinson's reverse-Rolle intuition are exact facts.

### Real conservation

For a generic real polynomial,

\[
N_{\rm nr}(p)-N_{\rm nr}(p')
=2E(p),
\]

where `E(p)` is the number of positive minima and negative maxima.  Iterating,

\[
N_{\rm nr}(p)
=2\sum_jE(p^{(j)}).
\]

On a finite real interval, the exact count is the adjacent-critical-value edge
identity of `L-104500`, with two explicit boundary defects.

### Complex transport

For a real entire function on one conjugation-symmetric domain,

\[
\boxed{
O(F_k)
=O(F_{k+1})
 +2E_k+B_{k,-}+B_{k,+}+W_k-1.
}
\tag{T-104500.1}
\]

Here `O` counts off-real zeros, `E_k` counts wrong extrema, and `W_k` is the
argument-principle winding of `F_k/F_(k+1)`.  Iteration gives an exact integer
ledger for the whole derivative ladder.

### Riccati–Pick dynamics

With

\[
h_k=-F_{k+1}/F_k,
\]

one has

\[
\mathcal L_k=F_k^2h_k',
\qquad
h_{k+1}=h_k-h_k'/h_k.
\]

Wrong extrema are exactly negative diagonal nodes of the derivative-ratio Pick
kernel, equivalently positive residues of `F_k/F_(k+1)`.

### High-derivative entry

Ki's cosine limit, and its Selberg-class extension by Gunns and Hughes, imply
unconditionally that every sufficiently high Xi derivative has only simple
real zeros on any fixed **scaled** compact box.  The same holds simultaneously
for every fixed finite band of subsequent derivatives.

These four statements turn the qualitative reverse-Rolle picture into an
exact local transport theory.

## 2. Integer-rigidity closure theorem

Let

\[
F_k=\Xi^{(k)}.
\]

For a height `T`, choose a conjugation-symmetric rectangle `Omega_T` containing
the complete critical strip in the `t`-plane up to real height `T`, with
boundary avoiding zeros of all derivatives under consideration.

Suppose that for some order `r=r(T)`:

1. **High-derivative entry**
   \[
   O_{\Omega_T}(F_r)=0.
   \tag{T-104500.2}
   \]

2. **Cumulative Riccati–Pick edge charge**
   \[
   \boxed{
   \mathfrak C_r(T)
   :=
   2\sum_{k=0}^{r-1}E_k(T)
   +\sum_{k=0}^{r-1}
    \bigl(B_{k,-}(T)+B_{k,+}(T)+W_k(T)-1\bigr)
   <2.
   }
   \tag{T-104500.3}
   \]

By `L-104501`,

\[
O_{\Omega_T}(\Xi)=\mathfrak C_r(T).
\]

The left side is a nonnegative even integer because nonreal zeros occur in
conjugate pairs.  Hence (T-104500.3) forces

\[
O_{\Omega_T}(\Xi)=0.
\]

If (T-104500.2)--(T-104500.3) hold for arbitrarily large `T`, then every zero
of `Xi` is real and RH follows.

This is the exact reverse-Rolle closure theorem:

\[
\boxed{
\mathrm{GBOX104500}
\ \wedge\ 
\mathrm{RPCH104500}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-104500.4}
\]

## 3. The two remaining estimates

### GBOX104500 — growing-box high-derivative entry

The proved compact cosine theorem must be made quantitative on the expanding
scaled rectangles

\[
C_n^{-1}\Omega_T.
\]

A sufficient form is a Rouche-safe approximation to `cos z` on the union of:

```text
small circles around every cosine zero in the expanding rectangle;
the complementary zero-free region;
the horizontal and vertical outer boundaries.
```

This is substantially stronger than fixed-compact convergence but is a
concrete saddle-point theorem for the positive Fourier kernel of Xi.

### RPCH104500 — cumulative Riccati–Pick charge below two

One must prove

\[
\mathfrak C_{r(T)}(T)<2.
\]

This target is local and integer-valued.  It allows cancellation between
wrong-extremum and winding terms, so it is weaker than requiring every
derivative ratio to be globally Pick.

The natural proof data are:

```text
negative spectral mass of the derivative-ratio Pick kernels;
adjacent critical-value edge signs;
argument variation of F_k/F_(k+1) on the common rectangle;
explicit multiplicity and boundary ledgers.
```

The repository's actual-Xi Pick positivity through order three is a useful
finite local input, but it is not reused at several derivative levels and is
not extrapolated to all orders.

## 4. How Levinson–Conrey concentration enters legally

A proportion tending to one does not imply (T-104500.2).  It becomes useful
only in a quantified growing-order theorem strong enough that

\[
(\text{exceptional proportion})
\times
(\text{total zero count below }T)
<2.
\]

At that point the exceptional count is an even integer and must vanish.  This
is the correct integer-rigidity upgrade of a density theorem.

## 5. Exact scientific boundary

```text
unit-cost one-point reverse Rolle             FALSE
factor-two real defect conservation           PROVED EXACT
complex winding transport                     PROVED EXACT
Riccati derivative-ladder recursion           PROVED EXACT
fixed-scaled-box high-derivative real zeros    PROVED
finite-depth scaled derivative cascade         PROVED
GBOX104500 growing-box entry                   OPEN
RPCH104500 cumulative charge <2                OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVEN
```

No global zero percentage, finite Pick order, numerical zero census or
unquantified `O(1)` boundary term is promoted to a proof of either open gate.
