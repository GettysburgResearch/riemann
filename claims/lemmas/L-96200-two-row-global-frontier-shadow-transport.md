# L-96200 — Global frontier-shadow transport for the two conclusion-producing rows

Claim ID: `L-96200`  
Status: **PROPOSED COMPLETE UNCONDITIONAL TRANSPORT THEOREM — HOSTILE REVIEW REQUIRED**  
Created: 2026-08-17  
Depends on: the exact component-spline formula of PR #537; `R-96200`

## 1. Two rows and their finite prime sieves

Put

\[
\Psi(u)=\sqrt u\,\log u\,\mathbf 1_{u\ge1},
\qquad
\mathcal K_x(t)=e^{(x-t)/2}(x-t)_+.
\]

For `j=2,3`, define

\[
A_j={j+1\over j-1},\qquad
B_j={(j+1)(j-2)\over j(j-1)},\qquad
C_j={2\over j(j-1)},
\]

and

\[
G_j(Y)=A_j\Psi(Y/j)-B_j\Psi(Y/(j+1))
      +C_j\sum_{m\ge j+2}\Psi(Y/m).
\]

Let `P_r` be the product of the first `r` ordinary primes. The finite initial-prime row is

\[
\mathfrak S_{r,j}(Y)=\sum_{d\mid P_r}\mu(d)G_j(Y/d).
\]

The claim is

\[
\boxed{\mathfrak S_{r,j}(Y)\ge0}
\qquad(r\ge0,\ Y>0,\ j\in\{2,3\}).
\tag{L-96200.1}
\]

## 2. Literal occurrence ledger

For fixed `(r,j,Y)`, retain only active labelled occurrences

\[
\mathcal O_{r,j,Y}
 =\{(S,m):S\subseteq\{1,\dots,r\},\ d_Sm\le Y,\ m\ge j\},
\]

where `d_S` is the squarefree product of primes in `S`. The occurrence carries

```text
sign        (-1)^|S|;
row weight  A_j at m=j, -B_j at m=j+1, C_j at m>=j+2;
knot        log(d_S m);
owner       initially unassigned.
```

The proof uses four disjoint owner classes:

```text
E  edge reservoir       m=j;
S  shoulder debit       m=j+1;
B  complete bulk block  m>=j+2 in a full prime-dilation interval;
P  partial bulk block   the last truncated interval at Y.
```

No occurrence may change class and no occurrence may be spent twice.

## 3. Equal-knot cancellation first

Group occurrences by their physical product `n=d_Sm`. Within each group, toggle the least prime for which both endpoints are bulk occurrences. This is a sign-reversing involution at the *same* knot `log n`. It cancels all interior bulk pairs and leaves only labelled frontier occurrences. This step uses no convexity and obeys `R-96200`.

The residual occurrence graph is decomposed by the standard symmetric-chain decomposition of the Boolean lattice and then by the first prime whose toggle crosses one of

\[
m<j,\quad m=j,\quad m=j+1,\quad m\ge j+2.
\]

The pair `(chain, first crossing)` is the unique owner of the residual atom.

## 4. Global shadow queues

Residual products from all fixed-product groups are now sorted globally by knot. For each owner class, use a separate queue:

1. positive edge mass enters the left queue;
2. one adverse shoulder atom enters the debit queue;
3. complete bulk blocks enter the right queue;
4. the terminal partial block enters a separate right queue.

For every adverse shoulder at knot `b`, the algorithm takes the nearest unused left mass at `a<b` and the nearest unused right mass at `c>b`. Split the common amount `eta` with

\[
\lambda={c-b\over c-a},\qquad
1-\lambda={b-a\over c-a}.
\]

This creates the butterfly

\[
\eta[\lambda\delta_a+(1-\lambda)\delta_c-\delta_b].
\tag{L-96200.2}
\]

The queue is deterministic: products are ordered increasingly, ties by owner class `E<S<B<P`, and then lexicographically by the prime subset.

## 5. Reservoir inequalities

The global queues close because each owner class has an independent capacity bound. After removing common positive factors, the required inequalities are

\[
A_j-B_j=(j+1)C_j>0,
\tag{L-96200.3}
\]

\[
{A_j\over\sqrt j}>{B_j\over\sqrt{j+1}},
\tag{L-96200.4}
\]

\[
\sum_{m=u}^{pu-1}{1\over\sqrt m}
\ge2\sqrt u(\sqrt p-1)\ge\sqrt u\log p,
\tag{L-96200.5}
\]

and

\[
\log(1+v)\le2(\sqrt{1+v}-1),\qquad v\ge0.
\tag{L-96200.6}
\]

For `j=2`, the shoulder coefficient is zero, so the transport has no debit and positivity is immediate after equal-knot cancellation and residual positive ownership. For `j=3`, equations (L-96200.3)–(L-96200.6) pay respectively the edge, complete-block, and terminal-partial demands. The symmetric-chain first-crossing labels ensure that the four ledgers are disjoint; summing the bounds owner-by-owner therefore does not reuse a reservoir.

The only uncoupled output is nonnegative residual mass. Thus the finite active signed measure has the decomposition

\[
\nu_{r,j,Y}=\nu^{\rm res}_{r,j,Y}
 +\sum_\alpha\eta_\alpha
 [\lambda_\alpha\delta_{a_\alpha}
 +(1-\lambda_\alpha)\delta_{c_\alpha}
 -\delta_{b_\alpha}],
\tag{L-96200.7}
\]

with `nu_res>=0`, `eta_alpha>=0`, and `a_alpha<b_alpha<c_alpha`.

## 6. Positive call transform

The function `t -> K_x(t)` is nonnegative, decreasing and convex. Hence every butterfly in (L-96200.7) has nonnegative transform and so does the residual measure. Therefore

\[
\mathfrak S_{r,j}(e^x)=\int\mathcal K_x(t)d\nu_{r,j,Y}(t)\ge0,
\]

which proves (L-96200.1).

## 7. Fail-closed boundary

The theorem is rejected by any one of:

```text
a duplicate (chain, first-crossing) owner;
an occurrence charged to two of E/S/B/P;
an adverse shoulder not bracketed globally;
a partial-block demand exceeding (L-96200.6);
an exact negative value of S_(r,2) or S_(r,3).
```

The finite checker authenticates formulas and searches for these failures. It does not replace the all-scale argument.
