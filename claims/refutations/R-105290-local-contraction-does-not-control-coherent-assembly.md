# R-105290 — Local contraction does not control coherent owner assembly

Claim ID: `R-105290`  
Status: **PROVED EXACT FIREWALLS**  
Created: 2026-08-24  
Depends on: `L-105292`; PR #751 `L-106024/L-106027`  
RH status: **unproved**

The sharp local squareclass observation norm

\[
\frac{p-1}{p+1}<1
\]

is an important theorem, but it is not by itself a global ninety-percent
estimate.

## 1. Direct-sum labels can collide physically

Let two source packets occupy orthogonal label spaces and suppose their local
physical images are the same nonzero vector \(v\). Each packet can separately
satisfy an arbitrarily strong contraction estimate. After physical labels are
forgotten, however,

\[
\|v+v\|^2=4\|v\|^2,
\]

whereas the sum of the two individual physical energies is

\[
2\|v\|^2.
\]

The missing factor is the positive cross term

\[
2\operatorname{Re}\langle v,v\rangle.
\]

Thus packetwise contraction cannot be summed after coherent physical
identification unless cross-owner inner products are retained.

## 2. A fixed number of large conductors has no uniform gap

For every fixed integer \(m\),

\[
\sup_{p_1,\ldots,p_m\ {m primes}}
\prod_{j=1}^m\frac{p_j-1}{p_j+1}=1,
\]

because the product tends to one when all \(p_j\to\infty\). Consequently no
fixed finite phase bank can supply a conductor-uniform constant below
\(3579/37000\), or below any other fixed number less than one, from local
occupancy alone.

## 3. Quadratic owner classes may not be merged early

For one conductor \(p\), the two sectors

\[
\kappa_p(P)=+1,\qquad \kappa_p(P)=-1
\]

must remain separate through the square-phase transform. If they are merged
first, the physical residues can occupy all of \(\mathbf F_p^*\); the constant
mode of the full phase Gram then loses the strict contraction. This is the
exact firewall of PR #751 `L-106027`.

## Consequence

A valid global theorem must retain:

```text
owner-conductor labels;
the two quadratic owner sectors;
all positive cross-owner Hankel inner products;
actual-Xi/source exhaustion errors;
near-line Blaschke phase slips.
```

The fixed-constant coherent estimate `HOCH105290` is designed to retain all of
these terms. Dropping any one of them would turn the new ninety-percent cut into
a source-blind local estimate and is not permitted.
