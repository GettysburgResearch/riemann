# Exact same-characteristic spectroscopy for two marked genus-two traces

**Status:** exact trace-recurrence theorem derived from the two source-locked
all-\(q\) marked-stack theorems. This is no longer a three-field fit.

**Scope:** for each odd prime \(p\), the marked stacks over every extension
\(\mathbf F_{p^n}\), \(n\geq1\). No field, polynomial, curve, cohomology group,
or modular form is enumerated. The replay uses exact integers only.

**Sources:** the proved `chi_(0,3)` and `chi_(2,2)` packets at commits
`65eb68fe1` and `65f4c7dc0`. Their LF-normalized file hashes, canonical
payloads, schemas, and full commits are locked in the JSON.

## 1. Why this is a different evidence type

The guarded cohomology experiment refused to name a Frobenius spectrum from
values at \(q=3,5,7\): every polynomial can be changed by

\[
 (q-3)(q-5)(q-7)Q(q)
\]

without changing those observations. The first same-characteristic holdout
\(q=3^2=9\) already sees the basic ambiguity factor as \(48\).

The two later character-sum proofs change the situation. They give trace
formulas for **every** odd prime power, hence in particular a complete
\(p,p^2,p^3,\ldots\) tower at each fixed characteristic. The recurrence below
is therefore a theorem-derived holdout test, not interpolation.

## 2. The `chi_(0,3)` tower

The marked trace is

\[
 T_{0,3}(q)=q^4-2q-1.
\]

At \(q=p^n\),

\[
 T_n=(p^4)^n-2p^n-1.
\tag{1}
\]

Thus its trace-level virtual spectrum has eigenvalues
\((p^4,p,1)\), with signed multiplicities \((1,-2,-1)\). The three roots are
distinct, so the minimal characteristic polynomial is

\[
 (X-p^4)(X-p)(X-1).
\]

Equivalently,

\[
 \boxed{
 T_{n+3}=(1+p+p^4)T_{n+2}
 -(p+p^4+p^5)T_{n+1}+p^5T_n.}
\tag{2}
\]

## 3. The `chi_(2,2)` tower

Here

\[
 T_{2,2}(q)=2q^3-q^2-2q-2,
\]

so

\[
 T_n=2(p^3)^n-(p^2)^n-2p^n-2.
\tag{3}
\]

The virtual signed Tate spectrum is

\[
 (p^3,2),\quad(p^2,-1),\quad(p,-2),\quad(1,-2),
\]

and all four eigenvalues occur. Therefore the minimal polynomial is

\[
 (X-p^3)(X-p^2)(X-p)(X-1),
\]

giving

\[
\boxed{
\begin{aligned}
T_{n+4}={}&(1+p+p^2+p^3)T_{n+3}\\
&-(p+p^2+2p^3+p^4+p^5)T_{n+2}\\
&+(p^3+p^4+p^5+p^6)T_{n+1}-p^6T_n.
\end{aligned}}
\tag{4}
\]

## 4. Exact automated recovery and minimality

For \(p=3,5,7\), the replay uses the first \(2r\) tower values to recover the
order-\(r\) recurrence by exact rational linear algebra, then predicts four
untouched values. Every prediction agrees exactly.

Minimality is also certified rather than assumed. For a tower

\[
 s_n=\sum_{j=1}^r m_j\lambda_j^n,
\]

the leading \(r\)-by-\(r\) Hankel determinant is

\[
 \det H_r
 =\left(\prod_jm_j\lambda_j\right)
  \prod_{i<j}(\lambda_j-\lambda_i)^2.
\]

It is nonzero in every control, while \(\det H_{r+1}=0\). Hence the orders
three and four are exact; no shorter linear recurrence can generate these
towers.

This is the useful core of automated cohomological spectroscopy: a nominated
spectrum, an exact recurrence, a minimality certificate, and genuine
same-characteristic holdouts.

## 5. Cohomological firewall

Equations (1)--(4) prove equality of the **virtual compactly supported trace
sequences** with signed Tate power sums. Negative multiplicities are natural
in an alternating Euler trace. They are not negative dimensions of an
individual cohomology group.

The result does not by itself prove that every individual \(H_c^i\) is Tate,
an isomorphism of motives or Galois representations, or the absence of
canceling non-Tate pieces between cohomological degrees. It does not identify
a Siegel eigenform, transfer to number fields, or imply RH/GRH.

## Replay

```text
python -B research/l-families/atlas/function_field/genus2_exact_frobenius_tower_spectroscopy.py --check
python -B -O research/l-families/atlas/function_field/genus2_exact_frobenius_tower_spectroscopy.py --check
python -B -m unittest tests.test_genus2_exact_frobenius_tower_spectroscopy
python -B -O -m unittest tests.test_genus2_exact_frobenius_tower_spectroscopy
```
