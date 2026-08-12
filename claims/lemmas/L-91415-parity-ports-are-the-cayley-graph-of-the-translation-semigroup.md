# L-91415 — The parity ports are the Cayley graph of the translation semigroup

Claim ID: `L-91415`  
Status: **PROVED EXACT GRAPH REDUCTION; CONNECTION-AWARE GRAPH DOMINATION OPEN**  
Created: 2026-08-12  
Depends on: `L-91414`, corrected `L-91412`  
RH status: **unproved**

## 1. Abstract Cayley graph

Let `T` be a contraction on a Hilbert space and suppose an endpoint pair is
related by

\[
 U=TV.
 \tag{L-91415.1}
\]

Its even and odd ports are

\[
 E=\frac{(I+T)V}{\sqrt2},
 \qquad
 O=\frac{(T-I)V}{\sqrt2}.
 \tag{L-91415.2}
\]

On the range of `I+T`, define the Cayley operator

\[
 \boxed{
 A_T=(I-T)(I+T)^{-1}.
 }
 \tag{L-91415.3}
\]

Then

\[
 \boxed{
 O=-A_TE.
 }
 \tag{L-91415.4}
\]

Thus the favourable/adverse parity comparison is a graph-norm problem for one
canonical operator.  No choice of factorization remains after the Hadamard
rotation.

If `T` is a contraction, `A_T` is accretive wherever defined:

\[
 \Re\langle A_Tx,x\rangle\ge0.
 \tag{L-91415.5}
\]

Accretivity alone does not imply either `E*E <= O*O` or the reverse.

## 2. Translation multiplier

For the unitary translation model with spectral variable `xi`,

\[
 T_u(\xi)=e^{i\xi u},
 \]

one has

\[
 \boxed{
 A_{T_u}(\xi)
 =-i\tan\left(\frac{\xi u}{2}\right).
 }
 \tag{L-91415.6
}
\]

The inverse graph from the odd port back to the even port has multiplier

\[
 i\cot\left(\frac{\xi u}{2}\right).
 \tag{L-91415.7}

\]

and is singular at the no-jump frequencies `xi u in 2 pi Z`.  Conversely the
forward graph is singular at the anti-phase frequencies
`xi u in (2Z+1)pi`.

This explains structurally why both parity orientations occur in the completed
source and why a connection/bridge coordinate is unavoidable.

## 3. Singular short channel

On the short channel of corrected `L-91412`,

\[
 U(u)=S_uf,
 \qquad
 V(u)=f.
\]

The odd port is the genuine Lévy production

\[
 O(u)=\frac{S_uf-f}{\sqrt2},
 \tag{L-91415.8}
\]

while the even port approaches

\[
 E(u)\longrightarrow\sqrt2 f
 \qquad(u\downarrow0).
 \tag{L-91415.9}
\]

The short source measure behaves as `du/(2u)`.  Hence the odd port is square
integrable by the `H1` translation estimate, while the even port is not.  The
finite no-jump coordinates `C,J` and the compensation connection are exactly
the graph completion at the singular endpoint.

After the parity rotation of `L-91414`, the completed short graph is

\[
 \boxed{
 \left(
  \frac{S_uf-f}{\sqrt2},
  \frac{C-J}{\sqrt2}
 \right)
 \quad\text{versus}\quad
 \frac{C+J}{\sqrt2}.
 }
 \tag{L-91415.10}

## 4. Long channel

On `u>kappa`, no Lévy compensation is needed.  The sign of the completed
source reverses the Wick--Green ledger, so the even port is favourable and the
odd graph port is adverse:

\[
 \boxed{
 E_-(u)=\frac{U_-(u)+V_-(u)}{\sqrt2},
 \qquad
 O_-(u)=\frac{U_-(u)-V_-(u)}{\sqrt2}.
 }
 \tag{L-91415.11}

At the plastic-aligned scale this is the opposite side of the parity domain
wall of `L-91414`.

## 5. Cauchy-kernel diagonalization

Let

\[
 r_\eta(t)=\sqrt{2\eta}\,e^{-\eta t}\mathbf1_{t>0},
 \qquad \eta>0.
 \tag{L-91415.12}

For the backward translation used in the physical cross-correlation,

\[
 S_ur_\eta=e^{-\eta u}r_\eta.
 \tag{L-91415.13}

\]

Hence on this one Cauchy vector

\[
 \boxed{
 E_\eta(u)
 =\frac{1+e^{-\eta u}}{\sqrt2}r_\eta,
 \qquad
 O_\eta(u)
 =-\frac{1-e^{-\eta u}}{\sqrt2}r_\eta.
 }
 \tag{L-91415.14}

In particular

\[
 \|O_\eta(u)\|\le\|E_\eta(u)\|
 \qquad(u>0).
 \tag{L-91415.15}

Thus the adverse long odd port is automatically dominated by its favourable
long even partner on the one-node Cauchy subspace.  The remaining one-node
burden lies in the prime even port and the finite completed connection.

This is the bridge from the full CPPD route to the one-node route developed on
the sibling branch.

## 6. Exact sufficient transfer theorem

Let

\[
 \mathcal E_a^{\rm adv}
 =E_{\rm p}\oplus\frac{C+J}{\sqrt2}\oplus O_-
 \tag{L-91415.16}
\]

and let

\[
 \mathcal E_a^{\rm fav}
 =O_{\rm p}\oplus T_{\rm sh}
  \oplus\frac{C-J}{\sqrt2}\oplus E_-
  \oplus\mathcal E_a^{\rm delay,ref,bridge}.
 \tag{L-91415.17}

Suppose the completed connection has a declared positive realization
`G_a` and there is an explicit contraction

\[
 \boxed{
 W_a:\overline{\operatorname{ran}\mathcal E_a^{\rm adv}}
 \longrightarrow
 \mathcal G_a\oplus
 \overline{\operatorname{ran}\mathcal E_a^{\rm fav}}
 }
 \tag{L-91415.18}

such that

\[
 W_a\mathcal E_a^{\rm adv}
 =G_a\oplus\mathcal E_a^{\rm fav}
 \tag{L-91415.19}
\]

in the exact packet normalization.  Then

\[
 \mathcal C_a^\lambda+
 \mathcal P_a^{\rm par}
 \succeq
 \mathcal N_a^{\rm par},
 \tag{L-91415.20}
\]

so CPPD and the corrected fixed-scale RH criterion follow.

The theorem is a direct application of the Douglas factorization lemma after
the explicit source maps have been constructed.  The open problem is the
source-ordered formula for `W_a`; an existential factor obtained from the
unknown target Gram is circular.