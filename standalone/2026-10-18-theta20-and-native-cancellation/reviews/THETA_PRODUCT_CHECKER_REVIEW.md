# Review of the independent degree-20 product and Jacobian checker

**Reviewer:** `/root/critical_coupling`, 2026-10-18.  
**Decision:** accepted at its stated finite rational-center scope. The independent generating-product method and its exact derivative comparison are correct for the fixed graph and active coordinates recorded below.

I did not author the independent checker or the theta packet. I read the complete independent checker, the compared component implementation and its shared arithmetic implementation, the rational parameter input, and the stored normal, optimized and mutation outputs. I reconstructed the finite generating-function and derivative argument. I did not execute a further copy of the already completed calculation.

## Exact objects reviewed

| Object | Bytes | SHA-256 |
|---|---:|---|
| `root/check_theta_product_independent.py` | 5256 | `7ad686d5c9dd25b203c10be8a0e74c293e4e88a7542ed471f08dfdeeeb9d92ba` |
| `root/THETA_PRODUCT_INDEPENDENT.json` | 989 | `a1f1204686adccd12ace4ed93b0f73d202eb775d810280999c85226de12dd93d` |
| `root/THETA_PRODUCT_INDEPENDENT_OPTIMIZED.json` | 989 | `a1f1204686adccd12ace4ed93b0f73d202eb775d810280999c85226de12dd93d` |
| `root/THETA_PRODUCT_MUTATION_STDERR.txt` | 523 | `c18de06d2ee47382e657af5ed4bccf94eab5b57a7a798185c9c72bc6026c4643` |
| `root/THETA_HUB_MUTATION_STDERR.txt` | 531 | `4d9d26f226126458a99f5c357b39c522021d7fb27f0975d42b202d6035ce8310` |
| `theta/parameters20.json` | 4428 | `2bfeb0b5ff376e2fb2b1f3773b726f4679af15dd01af0037ac2b10fa87db8bd4` |
| `theta/connected_blocks.py` | 1515 | `b376526980faf4e98fc9060695befa65e1a1c7c3b1f143b52b3c7dafa7c95978` |
| `theta/tree_core.py` | 3065 | `edab764577f7c4a1553d1dfb3f19b838f536ff48273aba8cf91acb4289a8577a` |

The report's input hashes match the complete files inspected. The normal and optimized reports are byte-identical. This binding is to these input bytes and this specific run; it does not grant a verdict to later changes at the same paths.

## Independent finite construction

The checker works in the exact truncated ring \(\mathbb Q[t]/(t^{21})\). All centers are parsed as `Fraction` values, so their terminating decimal strings specify exact rationals. The multiplicities and active coordinates are independently fixed, then checked against the parameter file:

\[
(256,10,1,\ldots,1),\qquad
(6,0,15,21,3,27,9,12,4,42).
\]

There are 256 single-spin components and 24 dimers, plus their common auxiliary hub: 305 vertices in total. For each component type, its exponential generating polynomial is

\[
P_i(t)=1+\sum_{n=1}^{20}\frac{M_{i,n}}{n!}t^n.
\]

For a dimer, the conditional moments use (p_iA_i^n+(1-p_i)B_i^n); the single-spin type uses (A_0^n). Odd conditional moments carry the exact hub correlation \(\eta=10^{-10}\). This retains the positive orientation of (B_i\) in the conditional odd moments and the full shared-hub dependence.

The checker directly forms \(P(t)=\prod_iP_i(t)^{m_i}\), including every repeated component. Only after that full product does it project to the even part

\[
D(t)=\frac{P(t)+P(-t)}2.
\]

This is the required average over the two hub signs. Projecting individual components to their even parts beforehand would remove hub-induced correlations; that incorrect operation is not used. Polynomial truncation is exact for coefficients through degree 20 because higher degrees cannot contribute to lower ones.

The independently implemented logarithm uses the finite formal series

\[
\log(1+u)=\sum_{j=1}^{20}\frac{(-1)^{j+1}}j u^j
 \pmod{t^{21}},\qquad u(0)=0.
\]

It separately computes the logarithm of the truncated \(\cosh t\) series. Therefore dividing corresponding even coefficients gives \(\kappa_{2r}/c_{2r}\): the factorial factors cancel, and the denominators are the fair-sign cumulants rather than values imported from `tree_core.py`. Multiplying the coefficients of (D\) by (n!\) produces the complete raw moments of orders 0 through 20.

## Complete derivative comparison

For an active coordinate in type (i\), the direct product derivative is

\[
\partial P=m_iP_i^{m_i-1}(\partial P_i)
                 \prod_{j\ne i}P_j^{m_j}.
\]

The prefix/suffix products implement this expression exactly, including the multiplicity factor. The differentiated component moments have the correct (A_i\), (B_i\) and probability derivatives. The recorded active set uses only (A\) coordinates and the (B_1\) coordinate; the unused (B_0,p_0\) entries of the single-spin type remain passive. This review does not claim an arbitrary active-set extension beyond the hard-coded set.

Even projection commutes with differentiation, so the checker obtains \(\partial D\) after forming the full product derivative. Its independently implemented unit-series reciprocal satisfies (D\cdot D^{-1}=1\pmod{t^{21}}\). Multiplication then gives

\[
\partial\log D=(\partial D)D^{-1}.
\]

Dividing the ten even coefficients by those of \(\log\cosh t\) gives the complete derivative column of the normalized cumulant map. The checker compares all ten columns against all ten rows of the author's automatic-differentiation output: all 100 entries are required to agree as exact rationals. No finite differences or numerical tolerances are involved.

The expected values are constructed without using the author's cumulant recurrence, moment-recovery recurrence, fair-sign cumulants, or dual-number arithmetic. The author's `jet` is called only to obtain the values being compared. Thus the two routes are independently implemented at the relevant finite algebraic operations, while intentionally sharing the same rational input graph.

## Stored acceptance and negative controls

The stored successful reports record agreement of all raw orders 0–20, all ten normalized cumulants, and all 100 Jacobian entries. Equality checks raise explicit exceptions and survive optimized Python execution.

The stored derivative-permutation mutation fails at `independent complete Jacobian`. The stored zero-hub-correlation mutation fails earlier at `independent full graph moment map`. These are their intended mathematical equality gates; neither failure comes from the generic final guard that rejects an unexpectedly accepted mutation. In particular, the hub mutation confirms that the tiny positive shared correlation affects the exact finite map and is not simply rounded away.

## Scope and disposition

No discrepancy or algebraic error was found. The checker is a useful independent validation of the full finite graph map and its Jacobian at the declared exact center. It does not validate the original infinite theta source, its moment enclosures, a whole-cube derivative enclosure, the contraction residual, existence or uniqueness of a matching root, the Lee–Yang input, or any unbounded-order limit. Those are separate proof and certificate obligations. This review should accompany the finite-map check with those limits intact.
