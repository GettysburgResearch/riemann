# L-30201 — Relative Pascal replacement and the exact divisor-source commutator

Claim ID: `L-30201`  
Title: A central/sibling switch realizes one divisor dipole relative to an incoming central edge; an absolute divisor atom is realized by an adjacent central-tree commutator  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: PR #272 `L-27207`; PR #294 central/sibling carry identity  
Scope: the correct source and flow coordinates needed to repair PR #301

## 1. Carry-flow notation

For a split `[n,j]`, write

\[
 \partial[n,j]=e_n-e_j-e_{n-j}
\]

and

\[
 \chi_{n,j}(q)
 =\left\lfloor\frac nq\right\rfloor
  -\left\lfloor\frac jq\right\rfloor
  -\left\lfloor\frac{n-j}{q}\right\rfloor.
\]

The carry load of a flow is the floor transform of its node divergence.

At parent `4k`, set

\[
 C_k=[4k,2k],
 \qquad
 S_k=[4k,2k-1].
\tag{L-30201.1}
\]

Then

\[
\boxed{
 L_q(S_k-C_k)
 =\mathbf1_{q\mid2k}-\mathbf1_{q\mid2k+1}.
}
\tag{L-30201.2}

## 2. Exact relative replacement

Let `A>=B>=0`. If an incoming flow contains the central edge `A C_k`, replace it by

\[
\boxed{
 \mathcal R_k(A,B)=(A-B)C_k+B S_k.
}
\tag{L-30201.3}

All new edge coefficients are nonnegative and

\[
\boxed{
 \mathcal R_k(A,B)-A C_k
 =B(S_k-C_k).
}
\tag{L-30201.4}

Consequently the carry-load change is exactly

\[
\boxed{
 L_q(\mathcal R_k(A,B))-A\chi_{C_k}(q)
 =B\left(\mathbf1_{q\mid2k}-\mathbf1_{q\mid2k+1}\right).
}
\tag{L-30201.5}

The replacement creates no negative flow coefficient. It is an exact affine
operation on a flow which already contains the declared central capacity.

## 3. Absolute divisor atoms use adjacent tree commutators

Let `T_n` be the complete central halving tree rooted at `n`, normalized by

\[
 \partial T_n=e_n-n e_1.
\]

Put

\[
 \mathcal E_h=T_{h+1}-T_h.
\tag{L-30201.6}

Then

\[
 \partial\mathcal E_h=e_{h+1}-e_h-e_1.
\]

For every carry column `q>=2`, the bottom atom is invisible and therefore

\[
\boxed{
 L_q(\mathcal E_h)
 =\left\lfloor\frac{h+1}{q}\right\rfloor
  -\left\lfloor\frac hq\right\rfloor
 =\mathbf1_{q\mid h+1}.
}
\tag{L-30201.7}

Thus the formal divisor-source atom `e_m` is represented in flow space by the
signed adjacent commutator

\[
\boxed{e_m\longleftrightarrow\mathcal E_{m-1}.}
\tag{L-30201.8}

For a paired source

\[
 A e_{2k}-B e_{2k+1},
\]

one exact flow representative is

\[
\boxed{
 A\mathcal E_{2k-1}-B\mathcal E_{2k}.
}
\tag{L-30201.9}

Using the Pascal identity, the dipole part satisfies

\[
\boxed{
 \mathcal E_{2k-1}-\mathcal E_{2k}
 \equiv S_k-C_k
}
\tag{L-30201.10}

modulo a zero-divergence Pascal cycle; the two flows have the same complete
carry vector. Hence

\[
\boxed{
 A\mathcal E_{2k-1}-B\mathcal E_{2k}
 \equiv
 (A-B)\mathcal E_{2k-1}+B(S_k-C_k).
}
\tag{L-30201.11}

This is the correct absolute source identity. It is signed because the residual
source is an adjacent commutator and the switch is relative.

## 4. Why the distinction matters

There are two valid but different statements:

```text
relative statement:
  A C_k is present
  -> replace by (A-B)C_k+B S_k with zero new negative debt;

absolute statement:
  A e_(2k)-B e_(2k+1)
  -> (A-B)E_(2k-1)+B(S_k-C_k), a signed flow.
```

The first is stronger for a cascade but requires an incoming-capacity manifest.
The second is unconditional but does not by itself prove zero cycle debt.

A proof may pass from the absolute to the relative statement only by exhibiting
where the central edge `A C_k` occurs in the already constructed lower-scale
flow. The coefficient inequality `A>=B` is necessary but not sufficient for
that source binding.

## 5. Exact endpoint consequence

At a finite cutoff the odd tail may begin one index before the shifted-even
tail. That unmatched odd atom cannot enter (L-30201.3). It must be placed in the
explicit collar or paired with an actual previously included central edge. The
index inequality alone does not provide such an edge.

## 6. Proof boundary

Closed exactly:

1. the relative nonnegative replacement;
2. its complete carry-column change;
3. the adjacent-tree representation of one divisor atom;
4. the exact signed flow for a paired divisor source;
5. the source-coordinate distinction needed by a DCD proof.

Open:

1. an all-generation manifest of incoming central capacities;
2. exact treatment of every finite cutoff collar in that manifest;
3. a corrected DCD recurrence;
4. RH.