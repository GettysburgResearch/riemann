# Discrete derivative moments, resonance, and universality

The twenty primary records span 2003–2026. Nineteen have local primary PDFs. The Springer and Math-Net records establish Fujii's identity, but attempted full-text routes did not return a PDF. The journal year governs published citations. Each SHA-256 identifies the accessed manifestation.

## The two-point twist in the factorial-array constant

Let \(\rho=\tfrac12+i\gamma\) under RH and put \(Q(s)=2^{1-s}-1\). Then
\[
 |Q(\rho)|^2=3-2\sqrt2\cos(\gamma\log 2).
\]
The numerator in the factorial-array constant therefore contains a derivative-weighted ordinate twist. The Landau–Gonek formula concerns the unweighted sum \(\sum x^\rho\).

Heap–Li–Zhao's unconditional [Theorem 5](../sources/classical63_derivative_moments/hlz2022print.pdf) evaluates
\[
 F_T(\alpha,\beta)=\sum_{0<\gamma\le T}
 \zeta(\rho+\alpha)\zeta(1-\rho+\beta)\,
 Q(\rho)\overline Q(1-\rho).
\]
Here \(\overline Q\) conjugates the coefficients. The polynomial can have length \(T^\theta\) for fixed \(\theta<1/2\), with submultiplicative-in-modulus and divisor/log-bounded coefficients. The real coefficients \((-1,2)\) on \(\{1,2\}\) meet these bounds with the usual convention that the \((\log n)^C\) bound applies for \(n\ge2\) and the coefficient at \(1\) is bounded. With a literal \((\log 1)^C=0\) condition, submultiplicativity would exclude every nonzero sequence.

The combined main term is \(J(\alpha,\beta,T)+I(\alpha,\beta,T)+I(\beta,\alpha,T)\), with \(J\) in (5) and \(I\) in (24). The error is uniform \(O_A(T(\log T)^{-A})\) for sufficiently small complex shifts of size \(O(1/\log T)\). The uniform bound on regular points and the holomorphy of the finite sum imply local boundedness at apparent poles of the meromorphic main term, giving a removable extension for the combined expression. The two Cauchy formulas on circles of radius a sufficiently small fixed multiple of \(1/\log T\) give an error \(O_A(T(\log T)^{-A+2})\) after double differentiation. On RH the resulting derivative of \(F_T\) at zero is exactly
\[
 \sum_{0<\gamma\le T} |\zeta'(\rho)|^2 |2^{1-\rho}-1|^2.
\]
Zeros can be counted with their multiplicities because any multiple zero has \(\zeta'(\rho)=0\). Before imposing RH the differentiation yields the mixed reflected derivative sum. The arithmetic main term remains in differentiable form and its remainder constants are asymptotic.

For convergence alone, [Gonek 1984, Corollary 1, p.124](../sources/classical63_lfunctions/gonek1984.pdf) suffices. At \(\mu=\nu=1,\alpha=0\), its coefficient is \(1/3-2(1/8)=1/12\) relative to \(T/(2\pi)\). On RH it gives
\[
 \sum_{0<\gamma\le T}|\zeta'(\tfrac12+i\gamma)|^2
 =\frac{T(\log T)^4}{24\pi}+O(T(\log T)^3).
\]
Since \(|Q(\rho)|\le1+\sqrt2\), partial summation bounds the positive-ordinate weighted tail with denominator \(|\rho|^2\) by \(O((\log Y)^4/Y)\) for \(Y\ge3\). Conjugation gives the same negative-ordinate tail. The additional logarithm in the raw sum comes from \(N(T)\sim T\log T/(2\pi)\). An earlier draft gave the normalized moment’s log power in the raw sum and tail. The unconditional finite Arb enclosures for the factorial-array error use a different tail bound.

## Full reading of Heap–Radziwiłł–Soundararajan

All ten pages of [arXiv:1901.08423v1](../sources/classical63_derivative_moments/hrs2019.pdf) were read, including the proof chain in §§2–6. The unconditional Theorem 1 gives
\[
 \int_T^{2T}|\zeta(1/2+it)|^{2k}\,dt\ll T(\log T)^{k^2},
 \qquad T\ge10,\quad 0\le k\le2 .
\]

Sections 2–4 divide primes into intervals with smaller successive logarithmic scales and write \(\mathcal P_j(s)=\sum_{T_{j-1}\le p<T_j}p^{-s}\). Each \(\exp(\alpha\mathcal P_j(s))\) is modeled by its Taylor polynomial cut off at \(500\mathcal P_j(1)\). On the set where every prime block is moderate, weighted Young's inequality reduces the moment to squared truncated polynomials at parameter \(k\) and a fourth moment of \(\zeta\) weighted by the polynomials at \(k-2\). For the first exceptional block \(v\), a high even power with half-exponent \(\lceil50\mathcal P_v(1)\rceil\) suppresses the contribution. The factorials in the resulting mean squares make the exceptional terms summable.

Sections 5–6 use the Bettin–Bui–Li–Radziwiłł twisted fourth moment for short Dirichlet polynomials. At each prime the first-order Euler factor contributes \(4(k-2)+(k-2)^2=k^2-4\), which combines with the fourth-moment scale \((\log T)^4\). The reduction includes the endpoints \(k=0,2\). The imported fourth-moment theorem was identified in the proof and was outside the independent proof check. The theorem averages over a continuous interval of heights. Kirila's discrete theorem at zeros uses a different shifted upper-bound argument.

## Full reading of Lee–Pańkowski

All seven pages of [arXiv:2502.15364v1](../sources/classical63_derivative_moments/lee_pankowski2025.pdf) were read. The theorem statements and relevant proof passages were compared with the [2025 publisher PDF](../sources/classical63_derivative_moments/lp2025print.pdf).

Let \(D=\overline D_r(s_0)\) lie strictly in \(1/2<\Re s<1\) and put \(a=\Re s_0-r\). For the scope supported by the logarithm-based proofs, require \(f\) to be continuous and nonvanishing on \(D\) and holomorphic in its interior. Given every fixed \(\epsilon>0\), take \(H=(\log T)^B\) and measure the shifts \(T\le\tau\le T+H\) with \(\max_D|\zeta(s+i\tau)-f(s)|<\epsilon\). Theorem 1.1 uses RH and \(B>2/(2a-1)\) for a positive lower limit of the proportion. Theorem 1.2 uses \(B>4/(2a-1)\) unconditionally for a positive upper limit of the proportion along selected blocks.

Both inspected versions omit nonvanishing from the statements although §§2.4 and 3 take \(\log f\). The literal RH theorem is false for \(f(s)=s-s_0\) on any such disc of radius \(r>0\). With \(\epsilon<r\), Rouché's theorem would force a zero of \(\zeta(s+i\tau)\) inside the disc, contrary to RH. The records use the nonvanishing condition required by the proof.

The argument approximates \(\log\zeta\) by a short prime-power sum of length \(Y=(\log T)^A\), \(A<B\). Kronecker–Weyl gives a positive proportion of shifts matching finitely many prime phases, including over growing short intervals. Mean-square estimates control the remaining prime tail, and a disc mean-value inequality converts area estimates on a larger disc to a uniform bound on \(D\). One can choose a larger radius strictly inside the strip that leaves room for the strict inequality in the exponent. Choosing the truncation sufficiently large makes the normalized phase-tube error small, after which the finite phase tolerance can be fixed. Exponentiation gives the approximation to \(f\).

For the unconditional subsequence, the zero-density step uses Ingham's \(N(\sigma,T)\ll T^{3(1-\sigma)/(2-\sigma)}(\log T)^5\). The displayed bound (3) in both inspected sources omits \(1-\sigma\) from the numerator. For the short-product estimate on these blocks, choosing the zero-free boundary midway between \(1/2\) and the left edge of the disc uses the weaker error exponent \(1+A(1/4-a/2)\), up to an arbitrarily small loss and with \(a\) replaced by the enlarged disc's left edge when needed. This gives the stronger unconditional threshold on \(B\). The reading verifies the omission and checks the argument's inputs and threshold arithmetic. It imports standard zero-density, prime-phase density and logarithmic approximation tools.

## Other distinctions used in the records

- Ng's 2007 linear derivative twist and Benli–Elma–Ng's 2024 one-shift formula can give \(\sum_\rho\zeta'(\rho)X(\rho)Y(1-\rho)\). The latter identifies the inherited large-sieve error from Conrey–Ghosh–Gonek and corrects minor main-term errors in Ng's Theorem 1.3. The Heap–Li–Zhao two-shift formula above yields a product of derivatives.
- Ng 2004 bounds the fourth moment above and below at the predicted order under RH. Milinovich 2010 gives upper bounds for positive integer moments with a \((\log T)^\epsilon\) loss under RH. Kirila 2020 removes that loss for fixed real \(k>0\), while Gao's 2021 preprint treats the matching lower bound for real \(k\ge0\) under RH. These are order-of-magnitude statements.
- Theorem 3 of Ng 2008 gives very small \(|\zeta'(\rho)|\) on RH. It divides into infinitely many multiple zeros, when the result is immediate, and eventual simplicity, when the resonator uses reciprocal derivatives. A bound for an individual small value does not estimate the average of inverse powers. Heap–Li–Zhao Theorem 1 takes RH and simplicity of every zero as hypotheses for the negative-moment result.
- The pointwise derivative consequence of Lindelöf uses \(r=1/\log(2+|t|)\). Phragmén–Lindelöf extends the critical-line bound to the right. The functional equation on the left half of this shrinking disc changes the bound by a bounded factor. Cauchy's formula then incurs \(j!r^{-j}\), which can be absorbed by reducing the initial Lindelöf exponent for each fixed \(j\). This gives \(|\zeta^{(j)}(1/2+it)|\ll_{j,\epsilon}(1+|t|)^\epsilon\). Simm–Wei's Theorems 1.8–1.9 evaluate right-of-line integral moments with the height limit first for fixed \(\sigma>1/2\). The fourth moment is unconditional and higher integer moments there use Lindelöf.
- The recorded resonance results specify the long interval \([T^\beta,T]\) and Soundararajan's dyadic interval \([T,2T]\). Yang's derivative extrema are at unconstrained heights. Christ–Kalpokas sample generalized Gram points where the functional-equation phase is prescribed. Hughes–Pearce-Crump's 2025 conjectural recipe treats integer mixed moments, including the complex square \(\zeta'(\rho)^2\), which differs from the absolute square.

The recorded resonance bounds are historical statements from their original papers.

The [fixed-polynomial main-term computation](../audits/adversarial_reviews/prime_array63_hlz_classical_independent.md) uses both source terms to obtain the weighted coefficient \(k-1\) for \(Q_k(s)=k^{1-s}-1\), with the polarized coefficient \(\gcd(k,l)-1\).
