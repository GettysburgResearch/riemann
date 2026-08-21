# L-23604 — First-cell Mertens firewall and scale-contraction closure

Claim ID: `L-23604`  
Title: The Brion-localized balanced recurrence retains the exact first Farey cell and implies the square-root Mertens bound  
Status: **PROPOSED FULL-PROOF COMPOSITION PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-final-02`  
Created: 2026-08-07  
Dependencies: `L-23601`--`L-23603`; PR #229 first-cell identity; PR #233 `L-23202/L-23207/T-23202`; the classical Mertens criterion  
Scope: finite packet mutation and final global implication

## 1. Exact first-cell projection

For integer `D`, PR #229 proves

\[
 B_{D,1}
 =\left(\frac{i}{2\pi}+\frac1{2\pi^2}\right)
  \left[M(D)-M(\lfloor2D/3\rfloor)\right].
\tag{L-23604.1}
\]

Let

\[
 c=\frac23,
 \qquad
 \Delta_c=I-T_c,
 \qquad
 (T_cF)(x)=F(cx).
\tag{L-23604.2}
\]

The complete packet manifest in `L-23601` is required to export a linear
projection

\[
 \Pi_{\rm cell}:
 \text{balanced source}\longrightarrow
 \mathbb C\cdot\Delta_cM
\tag{L-23604.3}
\]

with the coefficient in (L-23604.1).  This is not inferred from an aggregate
operator estimate: every tuple, residue chain, cutoff, and parity row appearing
in the cell is contracted explicitly.

The projection commutes with:

1. signed destination recombination;
2. cumulative-prefix coordinate change;
3. polyhedral subdivision;
4. the Brianchon--Gram identity;
5. geometric finite differences in the outer cutoff.

Therefore applying `Delta_c^(m-1)` to the first-cell coordinate gives exactly

\[
 G_m(D)=\Delta_c^mM(D)
\tag{L-23604.4}
\]

with all floors retained.

## 2. Mutation theorem

The denominator cancellations in `L-23603` are identities in the complete
source algebra.  Applying `Pi_cell` to the localized vertex formula therefore
gives the same unmatched-denominator bound.  For every fixed order `K`, the
first-cell mutation satisfies

\[
 \boxed{
 \frac{|G_K(D)|^2}{D}
 \le
 D^{\theta_K+o_K(1)},}
\tag{L-23604.5}
\]

where the conservative exponent supplied by the full scale recurrence is

\[
 \boxed{
 \theta_K\le
 \frac{2g_0}{\delta K}
 =\frac{100}{K}.}
\tag{L-23604.6}
\]

The factor two deliberately absorbs passage between block energy and a scalar
cell amplitude.  A sharper source normalization may replace `100/K` by
`10/K`, but no sharper factor is used in the full proposal.

Equivalently,

\[
 \boxed{
 |G_K(D)|
 \ll_{K,\varepsilon}
 D^{1/2+50/K+\varepsilon}.}
\tag{L-23604.7}
\]

The implied constant may depend arbitrarily on fixed `K`.  This is harmless,
because `K` is chosen only after the target exponent `epsilon` is fixed.

## 3. Derivation from the balanced recurrence

Let

\[
 M_K(X)=1+\max_{\tau}\max_{0\le J\le X}E_{K,\tau}(J).
\tag{L-23604.8}
\]

`L-23603` gives, for fixed `K`,

\[
 M_K(J)
 \le
 \exp\{(g_0/K+o_K(1))J\}
 \left[1+M_K((1-\delta)J+C_K)\right].
\tag{L-23604.9}
\]

Iterating until the argument is bounded yields

\[
 \begin{aligned}
 \log M_K(J)
 &\le
 \left(\frac{g_0}{K}+o_K(1)\right)
 J\sum_{r\ge0}(1-\delta)^r+O_K(1)\\
 &\le
 \left(\frac{g_0}{\delta K}+o_K(1)\right)J.
\end{aligned}
\tag{L-23604.10}
\]

Thus every balanced energy has exponential coefficient tending to zero.  The
Type-I and terminal families are already exponentially smaller by the inherited
high-order Euler theorem.  Consequently the complete safe prime signal has
subexponential block energy.

The mutation (L-23604.5) is the scalar audit of this iteration.  It must be
obtained from the same proof object, not appended as a separate assumption.

## 4. Exact geometric inversion

`L-23202` proves the pointwise finite identity

\[
 M(x)=
 \sum_{j\ge0}{K+j-1\choose j}
 G_K(c^jx),
\tag{L-23604.11}
\]

where the sum terminates once `c^jx<1`.

Insert (L-23604.7).  For every fixed `K` and `epsilon>0`,

\[
 \begin{aligned}
 |M(x)|
 &\ll_{K,\varepsilon}
 x^{1/2+50/K+\varepsilon}
 \sum_{j\ge0}{K+j-1\choose j}
 c^{j(1/2+50/K+\varepsilon)}\\
 &\ll_{K,\varepsilon}
 x^{1/2+50/K+\varepsilon}.
\end{aligned}
\tag{L-23604.12}

Given an arbitrary `eta>0`, choose one fixed

\[
 K>100/\eta
\tag{L-23604.13}
\]

and then take `epsilon<eta/2`.  Equation (L-23604.12) gives

\[
 \boxed{
 M(x)=O_\eta(x^{1/2+\eta}).}
\tag{L-23604.14}
\]

The classical Mertens criterion now implies RH.

## 5. Alternative prime-signal closure

The same conclusion may be reached without isolating the cell.  The safe
prime-signal rightmost-zero theorem converts subexponential complete block
energy into

\[
 \Theta_\zeta=0,
\tag{L-23604.15}
\]

and hence RH.  The first-cell path is retained because it is the sharper
arithmetic firewall: it shows that the proof really controls the coherent
Möbius shell rather than only an aggregate positive energy.

## 6. Noncoprime and odd--odd controls

The first-cell producer must include the corrections that invalidated the old
Farey proof.  In particular it must preserve:

- lattice step `(q/g,v/g)` with `g=(q,v)`;
- the noncoprime control `q=v=5,r=5`;
- the odd--odd cotangent residue;
- every reduced-frequency multiplicity;
- the exact coefficient multiplying the Mertens increment.

The Brion proposal does not reuse the rejected determinant cancellation
`r=av-bq`.  These terms enter the source manifest and are consumed only by the
complete signed valuation.

## 7. Fail-closed verification

A proof object for (L-23604.5) must bind:

```text
source balanced-packet digest,
first-cell projection matrix,
all residue-chain and parity rows,
polytope and vertex-cone digests,
numerator/denominator cancellations,
scale destinations,
energy-to-cell adapter,
and the exact geometric-difference inversion.
```

The checker must reject if:

- the first-cell projection is absent or zero;
- the coefficient differs from (L-23604.1);
- one geometric difference uses a rounded rather than floored cutoff;
- a lower-scale destination exceeds the reserve;
- `K` varies with `x` inside one asymptotic bound;
- finite numerical agreement is substituted for (L-23604.7).

## 8. Proof boundary

The first-cell identity, geometric inversion, and final Mertens implication are
already established.  The proposed content is that the complete Brion-localized
balanced certificate exports the mutation bound (L-23604.5) with the same
vanishing rate as the full recurrence.

Subject to that source-level compatibility and `L-23603`, the displayed chain
proves RH.