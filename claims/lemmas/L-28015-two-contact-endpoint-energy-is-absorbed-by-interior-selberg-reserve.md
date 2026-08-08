# L-28015 — Two-contact endpoint energy is absorbed by the interior Selberg reserve

Claim ID: `L-28015`  
Title: In the exact `b_2` generalized-prime system, the two endpoint contacts are uniformly dominated by the Selberg reserve already present at the two nearest interior carry positions  
Status: **PROPOSED COMPLETE EXACT INEQUALITY PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Parent: PR #302  
Dependencies: `L-28006`, `L-28009`  
Scope: rowwise homogeneous boundary absorption in the exact generalized-prime metric; no claim that arbitrary physical source cross terms diagonalize rowwise

## 1. Exact generalized-prime row

Retain

\[
 \Lambda_2(q)=\Lambda(q)+(\log2)\mathbf1_{q=2^r}
\]

and put

\[
 P_2(n,j)=\sum_q\Lambda_2(q)\chi_{n,q}(j),
\]

\[
 S_2(n,j)
 =\sum_q[\Lambda_2(q)\log q+(\Lambda_2*\Lambda_2)(q)]
  \chi_{n,q}(j).
\]

The exact pointwise Selberg reserve of `L-28009` is

\[
 \boxed{
 \mathcal R_2(n,j)=P_2(n,j)^2-S_2(n,j)\ge0.
 }
\tag{L-28015.1}

At the two endpoint contacts,

\[
 P_2(n,1)=P_2(n,n-1)
 =L_2(n),
\]

where

\[
 \boxed{
 L_2(n)=\log n+v_2(n)\log2.
 }
\tag{L-28015.2}

The normalized energy of the exact two-contact source is therefore

\[
 \boxed{
 \mathcal E_{\rm end}(n)
 ={2L_2(n)^2\over n+1}.
 }
\tag{L-28015.3}

## 2. Explicit reserve at the first interior position

Let `e` and `o` be respectively the even and odd members of `{n-1,n}`, and put

\[
 r=v_2(e),
 \qquad
 L_e=\log e,
 \qquad
 L_o=\log o,
 \qquad
 \ell=\log2.
\]

The explicit `j=2` calculation in `L-28009` is

\[
 \boxed{
 \begin{aligned}
 \mathcal R_2(n,2)
 ={}&2L_e(L_o-2\ell)
  +2(r-2)\ell L_o\\
 &+(r^2-3r+6)\ell^2.
 \end{aligned}}
\tag{L-28015.4

}

and symmetry gives

\[
 \mathcal R_2(n,n-2)=\mathcal R_2(n,2).
\tag{L-28015.5}

The next theorem gives a uniform comparison with the endpoint amplitude.

## 3. Uniform comparison

For every integer `n>=4`,

\[
 \boxed{
 \mathcal R_2(n,2)
 \ge {1\over32}L_2(n)^2.
 }
\tag{L-28015.6}

For `n=4` the stronger finite inequality

\[
 \boxed{
 \mathcal R_2(4,2)
 \ge {1\over16}L_2(4)^2
 }
\tag{L-28015.7}

holds.

### 3.1 The range `n>=16`

First suppose `r>=2`.  The second term of (L-28015.4) is nonnegative, as is the
last term, so

\[
 \mathcal R_2(n,2)
 \ge2L_e(L_o-2\ell).
\tag{L-28015.8}

Since `e,o>=n-1` and `n>=16`,

\[
 n-1\ge {n\over2}\ge n^{3/4},
\]

and

\[
 {n-1\over4}\ge {n\over8}\ge n^{1/4}.
\]

Therefore

\[
 L_e\ge{3\over4}\log n,
 \qquad
 L_o-2\ell\ge{1\over4}\log n.
\]

Hence

\[
 \mathcal R_2(n,2)
 \ge{3\over8}\log^2n.
\tag{L-28015.9}

Also

\[
 v_2(n)\ell\le\log n,
\]

so

\[
 L_2(n)\le2\log n.
\]

Thus

\[
 \mathcal R_2(n,2)
 \ge{3\over32}L_2(n)^2.
\tag{L-28015.10}

Now suppose `r=1`.  Formula (L-28015.4) factors exactly as

\[
 \mathcal R_2(n,2)
 =2(L_o-2\ell)(L_e-\ell).
\tag{L-28015.11}

The first factor is at least `(1/4)log n` as above.  Moreover

\[
 {e\over2}\ge{n-1\over2}\ge{n\over4}\ge n^{1/4},
\]

so `L_e-ell>=(1/4)log n`.  Consequently

\[
 \mathcal R_2(n,2)
 \ge{1\over8}\log^2n
 \ge{1\over32}L_2(n)^2.
\tag{L-28015.12}

This proves (L-28015.6) for `n>=16`.

### 3.2 The finite range

For `4<=n<=15`, substitute the exact logarithmic expression
(L-28015.4).  The standard-library rational interval checker
`X-28004/verify.py` proves

\[
 32\mathcal R_2(n,2)-L_2(n)^2>0
\]

for every row in that range, and also

\[
 16\mathcal R_2(4,2)-L_2(4)^2>0.
\]

The checker evaluates logarithms through the rational `atanh` series with a
rigorous geometric remainder.  No floating-point sign enters the verdict.

Sections 3.1--3.2 prove (L-28015.6)--(L-28015.7).

## 4. Boundary absorption

For `n>=5`, the two positions `2` and `n-2` are distinct.  Define

\[
 \mathcal R_{\rm near}(n)
 ={\mathcal R_2(n,2)+\mathcal R_2(n,n-2)\over n+1}.
\tag{L-28015.13}

Then (L-28015.3), (L-28015.5), and (L-28015.6) give

\[
 \boxed{
 \mathcal E_{\rm end}(n)
 \le32\mathcal R_{\rm near}(n)
 \qquad(n\ge5).
 }
\tag{L-28015.14}

At `n=4`, there is only one distinct interior position.  Equation
(L-28015.7) gives the same conclusion:

\[
 \boxed{
 \mathcal E_{\rm end}(4)
 \le32{\mathcal R_2(4,2)\over5}.
 }
\tag{L-28015.15}

Thus every nontrivial two-contact endpoint row from `n=4` onward is paid by an
explicit reserve which already belongs to the complete generalized Selberg
forcing.  Only the finite rows `n=2,3` have no interior position.

## 5. Homogeneous source consequence

The estimate is quadratic and therefore survives arbitrary scalar row
amplitudes.  If `alpha_n` is any finite scalar family, then

\[
 \boxed{
 \sum_{n\ge4}|\alpha_n|^2\mathcal E_{\rm end}(n)
 \le32\sum_{n\ge4}|\alpha_n|^2\mathcal R_{\rm near}(n).
 }
\tag{L-28015.16

}

This differs essentially from the invalid operation refuted in `R-29002`, where
a quadratic Kummer term and a linear Selberg term were scaled by different
powers of the source amplitude.  Here both sides are already quadratic forms in
the identical row amplitude.

## 6. Role in the reflected proposal

The unweighted `m=1` source was the boundary firewall of `L-26904` and
`L-28013`.  Equations (L-28015.14)--(L-28015.16) show that, after the complete
source-convolved reflected identity has been placed in a direct row ledger, the
endpoint energy is not an uncontrolled extra coordinate: it has an absolute
reserve of its own.

A complete physical block still has source cross terms between row channels.
This lemma may be applied to that block only after the production object emits
the exact row-direct-sum or an explicit congruence preserving (L-28015.16).  It
is not permission to diagonalize an arbitrary source Gram.

## 7. Proof boundary

Closed exactly:

- the explicit `j=2` generalized-prime reserve;
- the uniform bound `R_2(n,2)>=L_2(n)^2/32`;
- exact finite verification of the small rows;
- absorption of every endpoint row `n>=4` by two nearest interior reserves;
- homogeneous scalar-source stability of that absorption.

Open:

- the full source-coupled physical congruence needed to sum cross-row terms;
- the two finite rows `n=2,3` in the block recurrence;
- the lower-scale reflected recurrence and RH.
