# Independent audit of the incidence and correction reductions

Status: scoped mathematical review; no mathematical defect identified in the reviewed files. No new analytic moment bound is asserted.

## Reviewed bytes

| File | SHA-256 |
|---|---|
| HYPERGRAPH_REDUCTION.md | e22637f2378adf35768d62b1270eb63615cc1c3058faae976e3d28d2f0bf9dac |
| analysis_theta_closure.md | 5655f79355dd5c9a3bc357ed27304354a056b4415e12ed7907de7c969c932e60 |

The first file is under riemann/standalone/2026-10-10-generalized-inverse-moments/; the second is the root scratch research note before placement in the proposed packet. The verdict applies to these exact file bytes and to the native identities and conditional reductions, not to the imported analytic framework or an unproved singleton estimate.

## Hypergraph reduction

The decomposition by exact prime-incidence subset is a bijection. In particular, a prime in three factors is assigned to its one three-element subset rather than separately to three pairwise gcds. The exterior Möbius sign, fixed character, and sextic character all have the correct incidence multiplicity. Character powers divisible by six retain zero extensions.

The support implication \(Nc_i\le bD\), the individual bound \(Nq_I\le bD\), and

\[
NQ\le\prod_I(Nq_I)^{|I|/2}\le(bD)^{k/2}
\]

are correct. The support floor \(X_i\ge1/b\) is sufficient and includes the unit ideal cases. Each source of dependence on the moving exclusion is explicit.

Minkowski and contraction of exterior row factors produce the weight

\[
\prod_I(Nq_I)^{-|I|/2}.
\]

Exactly the two-element incidences have a harmonic sum. Incidences of size at least three have convergent full ideal sums. This gives precisely \(\binom{k}{2}\) powers of a logarithm at the row norm level and \(k(k-1)\) after squaring. Constants can depend on \(k\), which is enough for the claimed fixed-order reduction.

The small-prime restoration statement is sound: restore each fixed removed prime by its finitely many incidence patterns in the original squarefree factors. All resulting norm dilations reduce factor scales, so the rectangular uniformity hypothesis covers them.

## Euler correction and the critical logarithmic transfer

The local identity

\[
\frac{1-\sum_i z_i}{\prod_i(1-z_i)}
=1+\sum_{\mathbf e\ne0}(1-|\operatorname{supp}\mathbf e|)
\mathbf z^{\mathbf e}
\]

has the asserted coefficients. For the inverse correction, the proposed inclusion-exclusion formula counts words with prescribed multiplicities while forbidding each active letter at one distinct designated position. This proves nonnegativity, including single-letter and derangement cases.

At the square-root norm weight \(t=q^{-1/2}\), both exact absolute coefficient generating functions are correct:

\[
C_{\mathrm{abs}}(t)
=2-\frac{1-rt}{(1-t)^r},
\qquad
H_{\mathrm{abs}}(t)
=\frac{(1-t)^r}{1-rt}.
\]

Each equals \(1+\binom r2t^2+O_r(t^3)\). The stipulated small-prime removal guarantees convergence of the inverse series. Every prime in an admissible coefficient tuple has norm at most \(Z=\max_i b_iX_i\), so the finite coefficient sum is bounded by the product of these local absolute majorants over \(Np\le Z\).

The proof of the prime-ideal Mertens upper bound preserves the unit coefficient of \(\log\log Z\). Indeed,

\[
\frac1q-\frac1{q^\sigma}
\le(\sigma-1)\frac{\log q}{q},
\]

and the simple pole of \(\zeta_K(\sigma)\), together with fixed-field Chebyshev and partial summation, gives the stated \(O(1)\) remainder at \(\sigma=1+1/\log Z\). The cubic remainder is summable. Consequently Proposition 4.1's norm loss

\[
(\log(3+Z))^{\binom r2}
\]

is correct in both directions.

The smooth convolution identities preserve the exact test functions and local zeros; only the scales change. Every norm hypothesis is invoked at the same row set and only at nonvanishing smaller scales. No mask has been illicitly discarded from a signed sum.

## Final attempts on weaker high-moment and tail targets

The following barriers are independent of the local algebra above.

### Fixed moment information plus a pointwise estimate has a linear excess

Suppose an array satisfies

\[
\sum_{u\in U_D}|A_u|^{2K}\ll H D^K,
\qquad |A_u|\ll D^{B_0},
\qquad B_0>1/2.
\]

For \(k\ge K\), these inputs give only

\[
\sum_{u\in U_D}|A_u|^{2k}
\ll H D^{K+2(k-K)B_0}
=H D^{k+(2B_0-1)(k-K)}.
\]

The excess \(e_k=(2B_0-1)(k-K)\) is linear in \(k\), so it cannot satisfy the sufficient cofinal criterion \(e_k=o(k)\).

This is a sharp obstruction to deductions using only those norm bounds. Set

\[
R\asymp H D^{K(1-2B_0)}
\]

entries equal to \(D^{B_0}\), and all other entries to zero, whenever the exponent of \(R\) is positive. Every moment of order \(2j\) with \(j\le K\) is at most its diagonal size, whereas the higher moments attain the displayed interpolation exponent. To make this model also allow at least \(D^{h/6+o(1)}\) repeated principal entries, it suffices that

\[
K(2B_0-1)\le5h/6.
\]

This is exactly the finite-moment extraction boundary. Thus generic moment interpolation and the already-known replica multiplicity leave room for precisely the obstruction that the new arithmetic theorem must exclude. These are synthetic arrays, not asserted realizations of the arithmetic family.

An explicit specialization avoids every integer-count issue: take

\[
B_K=\frac12+\frac{5h}{12K},
\qquad R=\lfloor D^{h/6}\rfloor.
\]

For fixed \(0<h\le11/10\) and \(K\ge1\), this has \(1/2<B_K<1\), positive row count tending to infinity, and \(R\le H\). Assign those \(R\) entries magnitude \(D^{B_K}\). The \(2K\)-th moment has exponent exactly \(K+h\), all moments of order \(2j\), \(j\le K\), satisfy their diagonal upper exponents, and the higher moments have excess

\[
e_k=\frac{5h}{6K}(k-K).
\]

The chosen \(R\) also exceeds the prime-replica count by a logarithmic factor, up to its fixed constant, for sufficiently large \(D\). No model with fewer than one row is invoked. If one wants a strict gap below the extraction boundary, decrease \(B_K\) by any fixed sufficiently small positive amount and increase the row count accordingly.

For the imported uniform exponent \(B_0=7/8\), \(K=1\), and \(h\) near one, the example has \(R\asymp D^{h-3/4}\), about \(D^{1/4}\). This exceeds the \(D^{h/6}\) replica multiplicity and gives \(e_k=3(k-1)/4\). The same conclusion applies if the small geometric constant improvement is used instead: the slope remains strictly positive.

### The second-moment tail bound has the old extraction threshold

Markov's inequality from \(\sum|A_u|^2\ll HD\) gives at threshold \(D^\alpha\)

\[
\#\{|A_u|>D^\alpha\}
\ll D^{h+1-2\alpha}.
\]

To force fewer than \(D^{h/6}/\log D\) bad rows requires

\[
\alpha>\frac12+\frac{5h}{12}.
\]

The synthetic array above shows why adding only the pointwise cap does not improve this below that cap. A new large-value estimate must use arithmetic correlation, rather than a rearrangement of the existing norm information.

### A linear growth of the admissible row exponent defeats cofinality

A diagonal moment theorem first becoming available at \(H=D^{h_k}\) with \(h_k\asymp k\) does not meet the weakened criterion. Even with \(e_k=0\), extraction gives the residual gap \(5h_k/(12k)\), bounded away from zero. Collapsing \(k\) factors to a length-\(D^k\) coefficient and applying a theorem requiring a comparable row range therefore cannot prove GRH through this route. A successful new argument needs both \(e_k=o(k)\) and \(h_k=o(k)\), or a genuinely stronger amplification or tail statement.

These failures do not rule out an arithmetic proof. They identify the precise extra information absent from interpolation, multiplicity counting, and the existing large-length estimates.
