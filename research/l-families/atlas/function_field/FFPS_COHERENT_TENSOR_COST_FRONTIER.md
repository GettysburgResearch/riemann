# The conductor cost of coherent FFPS tensor contraction

**Status:** exact finite budget theorem plus a classical primorial
asymptotic. The formal local tensor is analyzed; the open global FFPS moments
and principal-member individualization are not claimed.

**Frozen source:** corrected PR #751 target `T-106121 / FFPS106121` at
`37d9df4b9b4fb9a8277de6ec1f77278dbbe5b0f2`, through the source-locked
principal-leverage theorem.

**Computation:** 13 exact rational prefix rows, five target thresholds, and
an exhaustive 256-subset regression on the first eight odd primes. The
public checker refuses beyond 4,096 subsets or prime 127. No conductor
family, character family, L-function, or zero is enumerated.

## 1. Exact finite optimization

For distinct marked odd-prime phase coordinates, write

\[
 M=\prod_{p\in S}p,
 \qquad
 L(M)=\prod_{p\in S}{p-1\over p+1}.
\tag{1}
\]

Here \(L(M)\) is the squared principal leverage of the coherent local tensor.
The factor

\[
 f(p)={p-1\over p+1}
\]

is strictly increasing in \(p\), while every \(f(p)<1\). These two elementary
facts solve the conductor-budget problem exactly.

Let \(r_1=3,r_2=5,\ldots\) be the odd primes and
\(P_k=\prod_{i\leq k}r_i\). Then:

- among every \(k\)-prime tensor, \(\{r_1,\ldots,r_k\}\) uniquely minimizes
  both conductor and leverage;
- if \(P_k\leq X<P_{k+1}\), no \((k+1)\)-prime tensor fits under \(X\), and
  the first \(k\) odd primes uniquely minimize leverage among **all**
  tensors with \(M\leq X\).

Thus the optimal finite design is not a numerical knapsack: it is always the
odd-prime prefix.

The first few exact frontier points are

| marked primes | minimal \(M\) | optimal \(L(M)\) |
|---:|---:|---:|
| \(3\) | \(3\) | \(1/2\) |
| \(3,5\) | \(15\) | \(1/3\) |
| \(3,5,7\) | \(105\) | \(1/4\) |
| through \(11\) | \(1155\) | \(5/24\) |
| through \(13\) | \(15015\) | \(5/28\) |
| through \(19\) | \(4849845\) | \(1/7\) |

In particular, achieving \(L\leq1/5\) already needs \(M=15015\), rather
than the much smaller fourth prefix. The JSON gives the exact first point
with \(L\leq1/10\) as well.

## 2. Translation from prime cutoff to conductor

The source packet proves, by an exact finite Mertens factorization followed
by the classical Mertens product theorem, that for

\[
 M_x=\prod_{3\leq p\leq x}p
\]

one has

\[
 L(M_x)
 \sim {3\zeta(2)e^{-2\gamma}\over(\log x)^2}.
\tag{2}
\]

The prime number theorem gives

\[
 \log M_x=\vartheta(x)-\log2\sim x.
\]

Hence the conductor-scale frontier is

\[
 \boxed{
 L(M_x)
 \sim {3\zeta(2)e^{-2\gamma}\over(\log\log M_x)^2}.}
\tag{3}
\]

This is the critical scale change. The contraction is inverse-square
logarithmic in the prime cutoff but only inverse-square **log-log** in the
squarefree conductor cost.

Formally, reaching a small target \(\varepsilon\) on the optimal frontier
requires

\[
 \log\log M
 \sim\sqrt{{3\zeta(2)e^{-2\gamma}\over\varepsilon}}.
\]

Thus the conductor grows double-exponentially in the inverse square root of
the desired leverage, at this local-factor scale.

## 3. What this says about individualization

The result has a positive and a negative face.

Positively, coherent-before-square assembly really does contract, and the
exact cheapest design is now known. No search over marked-prime panels is
needed.

Negatively, for every fixed \(\delta>0\),

\[
 M_x^\delta L(M_x)\longrightarrow\infty.
\]

So the local tensor factor alone cannot supply an \(M^{-\delta}\) saving. If
an average-to-individual argument loses a polynomial-size character family,
this phase leverage cannot pay that loss by itself.

That is a local-operator obstruction, not a global impossibility theorem.
Arithmetic cancellation beyond the Gram factor, cross-prime Fourier or
incidence structure, a signed amplifier applied before squaring, or a
rigidity theorem could still change the scale. The packet does not prove that
every formal tensor is realized source-faithfully in `FFPS106121`, nor does it
prove the mixed/double global moments, RH, or GRH.

## Replay

```text
python -B research/l-families/atlas/function_field/ffps_coherent_tensor_cost_frontier.py --check
python -B -O research/l-families/atlas/function_field/ffps_coherent_tensor_cost_frontier.py --check
python -B -m unittest tests.test_ffps_coherent_tensor_cost_frontier
python -B -O -m unittest tests.test_ffps_coherent_tensor_cost_frontier
```
