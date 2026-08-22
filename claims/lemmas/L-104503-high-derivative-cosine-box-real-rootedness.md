# L-104503 — Repeated Xi derivatives are real-rooted on every fixed scaled box

Claim ID: `L-104503`  
Status: **PROVED UNCONDITIONALLY FROM THE KI / GUNNS–HUGHES COSINE LIMIT**  
Created: 2026-08-22  
RH status: **not assumed**

Ki proved that there are real sequences `A_n` and `C_n`, with `C_n -> 0`, such
that

\[
G_n(z):=A_n\Xi^{(2n)}(C_nz)
\longrightarrow\cos z
\tag{L-104503.1}
\]

uniformly on compact subsets of `C`.  Gunns and Hughes proved the corresponding
Selberg-class theorem and give explicit scaling sequences.

The zero-theoretic consequence below is not merely a statement about spacing.

## Fixed-box theorem

Let `Omega` be a bounded conjugation-symmetric Jordan domain whose boundary
contains no zero of `cos z`.  Then, for all sufficiently large `n`:

1. `G_n` has exactly the same number of zeros in `Omega` as `cos z`;
2. every such zero is simple and real;
3. each zero lies in an arbitrarily small prescribed disk around one real zero
   of `cos z`.

### Proof

The zeros of `cos z` in `Omega` are finitely many, simple and real.  Choose
pairwise disjoint disks `D_j`, centred at those zeros, invariant under complex
conjugation, and contained in `Omega`.  On each boundary `partial D_j`,
`|cos z|` has a positive minimum.  Uniform convergence in (L-104503.1) and
Rouche's theorem imply that `G_n` has exactly one zero in every `D_j`, counted
with multiplicity.

On the compact complement of the disks, `cos z` is bounded away from zero, so
uniform convergence implies that `G_n` has no zero there.

Finally, `G_n` is real entire.  A nonreal zero in a conjugation-invariant disk
would bring its distinct conjugate, contradicting the fact that the disk
contains exactly one zero counted with multiplicity.  Hence the unique zero is
real, and its multiplicity is one.

This proves the theorem.

## Finite derivative bands

Local uniform convergence permits termwise differentiation.  For every fixed
integer `J>=0`,

\[
G_n^{(j)}(z)
=A_nC_n^j\Xi^{(2n+j)}(C_nz)
\longrightarrow
{d^j\over dz^j}\cos z
\]

uniformly on compact subsets, simultaneously for `0<=j<=J`.

Let `Omega` now be a bounded conjugation-symmetric Jordan domain whose boundary
contains no zero of any of the finitely many functions

\[
\cos^{(j)}z,
\qquad 0\le j\le J.
\]

Applying the fixed-box Rouche argument separately and simultaneously to these
`J+1` compact convergences gives

\[
\boxed{
\begin{aligned}
&\text{for every fixed scaled box satisfying the displayed boundary condition}\
&\text{and every fixed finite derivative depth }J,\text{ all sufficiently high}\
&\text{Xi derivatives }\Xi^{(2n+j)},\ 0\le j\le J,\text{ have only simple real}\
&\text{zeros in }C_n\Omega.
\end{aligned}
}
\tag{L-104503.2}
\]

This is an unconditional finite-depth reverse-Rolle entry theorem.

## Exact limitation

The physical box in the original `t` variable is `C_n Omega`, and `C_n -> 0`.
To control all Xi zeros below a fixed original height `T`, one needs the cosine
approximation on boxes whose scaled width is of order `T/C_n`, which grows with
`n`.

Compact convergence alone does not supply that growing-box uniformity.  No
claim to the contrary is made here.

The remaining high-derivative input for RH is therefore a quantitative
**growing-box cosine theorem**, not another global proportion statement.
