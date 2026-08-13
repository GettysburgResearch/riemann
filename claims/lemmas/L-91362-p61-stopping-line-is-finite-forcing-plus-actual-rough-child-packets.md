# L-91362 — The `P_61` stopping line is one finite forcing plus actual source-disjoint rough child packets

Claim ID: `L-91362`  
Status: **PROVED EXACT POSITIVE SOURCE-TREE DECOMPOSITION**  
Created: 2026-08-13  
Depends on: paired least-prime recursion `L-91333/L-91402`; same-index functor `L-91361`  
RH status: **unproved**

## 1. Paired source packet

For a fixed parameter `a>=1`, let

\[
 \mathbf P_j^{(a)}(X)
 =\bigl(E_j^{(a)}(X),O_j^{(a)}(X)\bigr)
\]

be the positive paired squarefree source whose prime factors are at least the `j`-th prime.  Retain the exact least-prime recursion

\[
\boxed{
 \mathbf P_j^{(a)}(X)
 =\binom{a\sqrt X-1}{0}
 +\sum_{k\ge j,\ p_k\le X}
 p_k^{-1/2}S\,
 \mathbf P_{k+1}^{(a)}(X/p_k),
}
\tag{L-91362.1
}

where `S` swaps the parity coordinates.  Every summand is a positive measure and every squarefree source atom appears once.

## 2. Expand through all primes at most `61`

Put

\[
 P_{61}=\prod_{q\le61}q
\]

and let `m` be the index of the next prime `67`.  Finite iteration of (L-91362.1) gives

\[
\boxed{
 \mathbf P_1^{(a)}(X)
 =\sum_{d\mid P_{61}}
 d^{-1/2}S^{\omega(d)}
 \mathbf P_m^{(a)}(X/d).
}
\tag{L-91362.2
}

Insert the least-prime recursion once at every term.  The result is

\[
\boxed{
 \mathbf P_1^{(a)}(X)
 =\mathbf F_{61}^{(a)}(X)
 +\sum_{d\mid P_{61}}
  \sum_{\substack{p\ge67\\dp\le X}}
  (dp)^{-1/2}S^{\omega(d)+1}
  \mathbf P_{p+}^{(a)}(X/(dp)),
}
\tag{L-91362.3
}

where

\[
\boxed{
 \mathbf F_{61}^{(a)}(X)
 =\sum_{d\mid P_{61}}
 d^{-1/2}S^{\omega(d)}
 \binom{a\sqrt{X/d}-1}{0}
 \mathbf1_{d\le X}.
}
\tag{L-91362.4
}

The first term is the complete finite Boolean forcing through `61`.  The other terms are the **actual paired rough child packets**, not scalar copies of one preferred native packet.

## 3. Source disjointness and contraction

Unique factorization assigns every squarefree source atom either to the finite forcing or to the unique pair `(d,p)` consisting of its complete small-prime part and its least rough prime.  Thus (L-91362.3) is coefficientwise source-disjoint.

Every nontrivial child endpoint satisfies

\[
\boxed{
 Y_{d,p}=X/(dp)\le X/67<c_0X.
}
\tag{L-91362.5
}

Taking any positive additive source mass gives

\[
\boxed{
 m(\mathbf F_{61}^{(a)})
 +\sum_{d,p}m(P_{d,p})
 =m(\mathbf P_1^{(a)}).
}
\tag{L-91362.6
}

In particular, the total child mass is substochastic.

## 4. Exact row and physical-capacity decomposition

Apply the retained component-row map to (L-91362.3).  At a child source node `n`, the corresponding parent node is `dpn`, and

\[
 (dpn)^{-1/2}Q_{X/(dpn)}
 =(dp)^{-1/2}n^{-1/2}Q_{Y_{d,p}/n}.
\]

Therefore `L-91361` gives the exact same-index row identity

\[
\boxed{
 R_X(\mathbf P_1^{(a)})
 =R_X(\mathbf F_{61}^{(a)})
 +\sum_{d,p}(dp)^{-1/2}
  R_{Y_{d,p}}(P_{d,p}).
}
\tag{L-91362.7
}

Applying any linear ordinary column, radix-four detail column, boundary-port coordinate, or literal entropy score preserves the same identity.  Consequently the parent target/capacity is spent once.

No affine row-index map, fractional child column, or branchwise quantizer is present.

## 5. The two SHARP labels

Apply (L-91362.3) separately to the fixed balanced and reserve paired labels used by the factor-54 source split, then add the two positive direct sums.  Their source atoms remain disjoint because the channel label is part of the source type.

Every finite-forcing producer may therefore act separately on the two complete labelled packets.  Every rough child retains its actual paired type and is passed unchanged to the next generation.

## 6. Proof boundary

```text
P_61 finite-block expansion                    EXACT
finite forcing plus actual rough children      EXACT
source disjointness and mass equality          EXACT
factor-67 endpoint contraction                 EXACT
same-index row/capacity/score decomposition    EXACT
hidden hazard normalization                    NOT USED
finite-forcing positive producer               OPEN / LOAD-BEARING
packet-envelope iteration                      AVAILABLE
Riemann Hypothesis                             UNPROVEN
```
