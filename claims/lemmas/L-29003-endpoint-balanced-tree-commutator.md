# L-29003 — Endpoint contacts are exact balanced-tree commutators

Claim ID: `L-29003`  
Title: The zero-reserve Kummer endpoint row is carry- and entropy-equivalent to the difference of two canonical balanced fragmentation trees  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-r`  
Created: 2026-08-08  
Dependencies: PR #272 `L-27204`; Kummer's identity; finite split-chain algebra  
Scope: exact endpoint routing and Abel ledger; no source-specific asymptotic estimate or RH claim

## 1. Split chains

For an unordered split of an integer `n` into `j` and `n-j`, write

\[
 [n,j],
 \qquad1\le j\le n/2,
\]

and define its node divergence

\[
\boxed{
 \partial[n,j]=e_n-e_j-e_{n-j},
}
\tag{L-29003.1}

with a repeated central child counted twice.

Its carry load at an integer column `q>=2` is

\[
 L_q([n,j])
 =\left\lfloor\frac nq\right\rfloor
  -\left\lfloor\frac jq\right\rfloor
  -\left\lfloor\frac{n-j}{q}\right\rfloor.
\tag{L-29003.2}

Its entropy is

\[
 \mathcal H([n,j])=\log\binom nj.
\tag{L-29003.3}

Both functionals depend only on the divergence: the carry load is the floor
pairing with `partial[n,j]`, while the entropy is the pairing with
`m mapsto log(m!)`.

## 2. Canonical balanced tree

Fix the central split

\[
 s(n)=\lfloor n/2\rfloor
\]

and define recursively

\[
 T_1=0,
 \qquad
\boxed{
 T_n=[n,s(n)]+T_{s(n)}+T_{n-s(n)}.
}
\tag{L-29003.4}

Every edge of `T_n` is `1/3`-balanced and hence `1/4`-balanced.  Induction gives

\[
\boxed{
 \partial T_n=e_n-ne_1.
}
\tag{L-29003.5}

Therefore

\[
\boxed{
 L_q(T_n)=\left\lfloor\frac nq\right\rfloor
 \qquad(q\ge2).
}
\tag{L-29003.6}

The entropy telescopes through factorials:

\[
\boxed{
 \mathcal H(T_n)=\log(n!).
}
\tag{L-29003.7}

Thus a complete balanced tree is an exact carry and entropy realization of one
integer factorial column.

## 3. Endpoint edge as a tree commutator

Define

\[
\boxed{
 D_n=T_n-T_{n-1}
 \qquad(n\ge2).
}
\tag{L-29003.8}

Then

\[
 \partial D_n
 =e_n-e_{n-1}-e_1
 =\partial[n,1].
\tag{L-29003.9}

Consequently

\[
\boxed{
 [n,1]-D_n\in\ker\partial.
}
\tag{L-29003.10}

In the explicit Pascal-cycle basis of PR #272, this difference is a finite
balanced cycle combination.

The carry and entropy identities are

\[
\boxed{
 L_q(D_n)
 =\left\lfloor\frac nq\right\rfloor
  -\left\lfloor\frac{n-1}{q}\right\rfloor
 =\mathbf1_{q\mid n},
}
\tag{L-29003.11}

and

\[
\boxed{
 \mathcal H(D_n)=\log(n!) -\log((n-1)!)=\log n.
}
\tag{L-29003.12}

These are exactly the carry column and entropy of the endpoint split `[n,1]`.
Thus the endpoint-neighbor null direction of `L-29002` is not an alien boundary
object: it is a balanced-tree commutator.

## 4. Abel summation of an endpoint family

Let `c_2,...,c_N` be arbitrary real coefficients.  Replacing every endpoint
edge by its tree commutator gives

\[
\begin{aligned}
 \sum_{n=2}^{N}c_n[n,1]
 &\equiv
 \sum_{n=2}^{N}c_n(T_n-T_{n-1})
 \pmod{\ker\partial}\\
 &=c_NT_N
   +\sum_{n=2}^{N-1}(c_n-c_{n+1})T_n.
\end{aligned}
\tag{L-29003.13}

Therefore

\[
\boxed{
 \sum_{n=2}^{N}c_n[n,1]
 \equiv
 c_NT_N
 +\sum_{n=2}^{N-1}\Delta c_n\,T_n,
 \qquad
 \Delta c_n=c_n-c_{n+1}.
}
\tag{L-29003.14
}

with exact equality of every carry column and the complete entropy objective.

This is the proof-facing endpoint Abel transform.  The current-scale endpoint
family becomes:

- one declared outer tree `c_N T_N`;
- a signed sum of balanced trees weighted only by first coefficient differences.

Every proper descendant of `T_n` lies at scale at most `ceil(n/2)`.

## 5. Positive and bounded-variation consequences

If

\[
 c_n\ge c_{n+1}\ge0,
\]

then every coefficient on the right side of (L-29003.14) is nonnegative.  More
generally the negative balanced-tree mass is bounded exactly by the negative
variation

\[
\boxed{
 \sum_{n=2}^{N-1}(-\Delta c_n)_+\,\|T_n\|,
}
\tag{L-29003.15
}

in any additive edge metric.

In the capacity metric of PR #272, a central tree has a completely explicit
finite cost.  Hence an endpoint source is reduced to one one-dimensional
variation theorem rather than an arbitrary balanced Type-II packet.

## 6. Connection to the prime-annulus boundary

`L-29002` proves that the complete Selberg forcing consumes the whole Kummer
square only on the endpoint neighbors `j=1,n-1`.  The dyadic two-contact source
on PR #269 is supported exactly on those two positions.

Equation (L-29003.14) supplies the missing exact geometric operation:

```text
zero-reserve endpoint source
 -> Pascal-equivalent balanced-tree commutator
 -> one outer endpoint plus first coefficient differences
 -> strict factor-two descendant scales.
```

The remaining arithmetic question is whether the complete prime-annulus source,
after every reflected cross term is assembled, has subpower negative tree
variation.  That is the named theorem in `T-29001`.

## 7. Proof boundary

Closed exactly, subject to review:

- balanced central-tree divergence;
- exact carry load and factorial entropy;
- endpoint/tree commutator identity;
- preservation of every carry column and entropy value;
- coefficient-level Abel transform;
- strict half-scale support of all proper descendants.

Open:

- a source-specific negative-variation bound for the prime-annulus endpoint
  coefficients;
- the recurrence in `T-29001`;
- RH.