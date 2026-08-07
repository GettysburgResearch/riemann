# O-9513 — Terminal endpoint dimension and the balanced Möbius firewall

Observation ID: `O-9513`  
Title: True terminal lattice rows are unconditionally Euler-small; any terminal face retaining the fixed-log Möbius source is already RH-bearing  
Status: **REVIEW OBSERVATION / MANDATORY MUTATION FOR `L-9517`**  
Authoring/review agent: `gpt56-pro`  
Created: 2026-08-07  
Related claims: `L-9517`, `L-9518`, `L-15159`, PR #235 `L-15451`, corrected PR #233 `L-23205/L-23206`

## 1. Two different meanings of “terminal”

There are two mathematically different objects that the frozen proposal treats
under the same label.

### Complete-lattice terminal row

After every Möbius or residual divisor sign has been frozen into one short
prefix `A`, the remaining large variable has coefficient

\[
P(\log n)
\]

and runs over the complete positive-integer lattice selected only by a compact
window:

\[
\sum_{n\ge1}
\frac{P(\log n)}{\sqrt{An}}
H_K(x-\log(An)).
\tag{O-9513.1}
\]

The high-order half-pole moments annihilate the continuous integral, and one
Euler remainder gives

\[
O_K(e^{-x/2}\operatorname{poly}(x)).
\]

Summing the short prefixes under a fixed reserve still gives exponential
decay. This terminal family is unconditional and contains no Mertens problem.

### Arithmetic terminal boundary

If the coefficient of the final long variable still contains `mu`, `r_V`, or a
signed Möbius recombination, Abel summation produces its summatory function.
The boundary is then Mertens-like.

High-order null moments for continuous polynomial densities do not estimate
that summatory function.

The two objects must not be conflated.

## 2. Explicit growing-dimensional terminal geometry

Let

\[
X=e^J,
\qquad
V=X^{1/K},
\qquad
\delta=\frac15.
\]

In one expanded resolvent row, write

\[
r_V(n_i)
=
-\sum_{\substack{d_i m_i=n_i\\d_i\le V}}\mu(d_i).
\]

Take

\[
j_K=\left\lfloor\frac K5\right\rfloor-1.
\]

Choose `j_K` short residual factors with

\[
V<n_i\le cV
\]

for a fixed `c>1`. Their product has logarithmic exponent

\[
\frac{j_K}{K}+o(1)<\frac15.
\]

One additional unrestricted variable fills the remaining scale, so it has
exponent

\[
1-\frac{j_K}{K}+o(1)>\frac45.
\]

This is a terminal configuration under the fixed reserve.

After summing the long variable, the endpoint face remains parametrized by the
short divisor coordinates

\[
d_1,\ldots,d_{j_K}.
\]

Thus terminal geometry permits

\[
\boxed{j_K=\Omega(K)}
\]

free short divisor coordinates.

This is not a proof that complete signed recombination cannot cancel the face.
It is an exact mutation showing that the claimed absolute bound cannot follow
from terminal scale geometry alone.

`X-9515` checks the exponent geometry for increasing `K`.

## 3. What complete recombination can do

The finite resolvent identity may recombine many expanded divisor faces back
into the scalar coefficient `mu(n)`.

That reduces the visible factorization dimension, but it does not estimate the
coefficient.

At the level of summatory functions, the recombined boundary becomes a Mertens
quantity. In the fixed-ratio hierarchy this is

\[
G_K(D)=\Delta_{2/3}^K M(D).
\]

For every fixed `K`,

\[
G_K(D)=O_\varepsilon(D^{1/2+\varepsilon})
\]

is equivalent to RH by exact geometric inversion.

Therefore there are only two possible outcomes:

```text
expanded source coordinates retained:
    growing-dimensional terminal faces must be controlled;

coordinates fully recombined:
    an RH-equivalent Mertens boundary must be controlled.
```

An endpoint-coordinate count does not solve both sides of this dichotomy.

## 4. The fixed-log Möbius slice cannot disappear into an easy terminal family

The exact Heath–Brown decoder gives, for fixed logarithmic variable `q_0`,

\[
\text{packet coefficient}
=
\mu(m)\log q_0.
\]

In the Gram Hilbert space, if this fixed slice is divided into a finite packet
family,

\[
h_{\mu,q_0}
=
\sum_{\tau=1}^{R_K}h_{K,\tau},
\]

then

\[
\max_\tau\|h_{K,\tau}\|^2
\ge
\frac{\|h_{\mu,q_0}\|^2}{R_K^2}.
\tag{O-9513.2}
\]

For fixed `K`, `R_K` does not affect the block exponential exponent.

Suppose the true complete-lattice terminal family has exponentially decaying
energy. Then, writing

\[
h_{\mu,q_0}
=
h_{\mathrm{term}}
+
\sum_{\tau\in\mathfrak B_K}h_\tau,
\]

one has

\[
\boxed{
\max_{\tau\in\mathfrak B_K}\|h_\tau\|^2
\ge
\frac{
\left(
\|h_{\mu,q_0}\|-\|h_{\mathrm{term}}\|
\right)_+^2
}{
|\mathfrak B_K|^2
}.
}
\tag{O-9513.3}
\]

Hence, after terminal Euler closure, at least one balanced packet retains the
full positive Möbius/rightmost-zero exponent.

This is why the corrected PRs #158, #233, and #235 leave `BTP(K)` open.

## 5. Consequence for `L-9517`

The two claims

```text
all genuine terminal rows are closed by complete-lattice Euler cancellation
```

and

```text
the q_0=2 RH-bearing Möbius slice is a terminal packet
```

cannot both be used without an exact decoder explaining the distinction.

If the `q_0=2` slice really lands in the terminal family, the terminal estimate
is already an RH-equivalent arithmetic theorem and does not follow from
endpoint counting.

If terminal means the complete-lattice normal form, then its energy is
unconditionally small and the `q_0=2` obstruction remains in the balanced
sector.

The corrected frontier is therefore:

\[
\boxed{
\text{complete-lattice terminal closure}
+
\text{signed balanced Möbius-bearing packet contraction}.
}
\]

## 6. Required production artifacts

A future terminal or balanced proposal should emit:

```text
exact fixed-q_0 tuple manifest
terminal/balanced destination of every tuple
signed recombination table
all cutoff and first-crossing faces
the packet vector in the physical normal Gram
an exact map to G_K if G_K is claimed
a coercive inequality, not only an identity
```

The first mutation should be the family in Section 2. The second should be the
fixed-`q_0=2` Hilbert-space lower bound (O-9513.3).

## 7. Status

```text
terminal face absolute dimension C_*              NOT ESTABLISHED
growing-dimensional pre-recombination family      EXPLICIT
complete-lattice terminal Euler closure            AVAILABLE
packet-level map to high-order Mertens difference  NOT SUPPLIED
balanced Möbius-bearing theorem                    OPEN
RH                                                  UNPROVED
```
