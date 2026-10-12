# Complete absolute tail norms from native logarithmic moments

Status: proposed elementary source transport lemma, pending independent review.
Scope: complete paired tail beyond a real cutoff `R` in a complete zero strip
`|Im rho|<=A`; every zero and every multiplicity is retained. Native moment
bindings can replace a coarse all-height zero-count bound in subsequent
transport budgets. This gives no new zero-free range and no RH conclusion.
Exact dependencies: the complete genus-zero paired product in THEOREM.md,
a complete finite census, and an actual-source enclosure of the indicated
logarithmic Taylor coefficients. Finite candidates alone do not supply the
census or the native moments.
What was actually run: existing native Taylor binding of `t_1`, separately
qualified in TAYLOR_TAIL_BINDING.md. No larger slab is certified by this lemma.
Smallest remaining gap: independent analytic review and any new native
parameter-family certificate that uses the stronger budgets.

## 1. A positive projection bounds the complete absolute norm

Let `R>0` and `A>=0`. For the paired representatives of the complete tail,
define

\[
t_k=\sum_{\operatorname{Re}\rho>R}\frac{m_\rho}{\rho^{2k}},\qquad
S_{2k}=\sum_{\operatorname{Re}\rho>R}\frac{m_\rho}{|\rho|^{2k}},
\quad k\ge1.
\tag{MN1}
\]

Nonreal conjugates are both present, real roots have their full multiplicity,
and the omitted negative representatives are exactly the opposite partners.
All sums converge absolutely. Suppose

\[
2k\arctan(A/R)<\pi/2,\qquad
c_k=\cos(2k\arctan(A/R))>0.
\tag{MN2}
\]

Every representative `rho=gamma+i eta` has `gamma>R` and `|eta|<=A`, hence
`|arg rho|<=arctan(A/R)`. The cosine is decreasing on `[0,pi/2]`, so

\[
\operatorname{Re}(\rho^{-2k})
=|\rho|^{-2k}\cos(2k\arg\rho)\ge c_k|\rho|^{-2k}.
\tag{MN3}
\]

Complete conjugation makes `t_k` real. Summing (MN3) gives the exact norm
transport

\[
0<c_kS_{2k}\le t_k,\qquad S_{2k}\le t_k/c_k.
\tag{MN4}
\]

Strict positivity assumes a nonempty tail, as follows for this source from
its infinite zero set and a finite central census. Neither an unknown
nonreal quartet nor a zero multiplicity is dropped. The real part of the
complete moment controls the entire absolute norm because the complete
strip puts every summand in the same acute sector.

For `ell>=k`, `|rho|>R` further gives

\[
S_{2\ell}\le R^{-2(\ell-k)}S_{2k}
\le\frac{t_k}{c_kR^{2(\ell-k)}}.
\tag{MN5}
\]

An authenticated directed upper bound `t_k<=U_k` may replace `t_k` on the
right. This controls every higher absolute inverse-power norm, without
an additional all-height counting estimate.

## 2. Exact low-order constants and native coefficient binding

The first three constants have rational forms for rational `R,A`:

\[
\begin{aligned}
c_1&=\frac{R^2-A^2}{R^2+A^2},\\
c_2&=\frac{R^4-6R^2A^2+A^4}{(R^2+A^2)^2},\\
c_3&=\frac{R^6-15R^4A^2+15R^2A^4-A^6}{(R^2+A^2)^3}.
\end{aligned}
\tag{MN6}
\]

The simple sufficient guard `R>2kA` ensures (MN2), since
`2k arctan(A/R)<2kA/R<1<pi/2`. For actual `R=8192,A=1/2`, all three
guards are immediate. In particular the existing native `a_1=t_1` binding
implies `S_2<=a_1_upper/c_1`, approximately `0.00015879044`, compared with
the separately source-qualified coarse-count bound of approximately `0.002325`.
The decimals describe the improvement only; acceptance uses the exact
rational upper endpoint and exact `c_1`.

The complete native coefficient identity is

\[
t_k=-k[z^{2k}]\log(\Xi(z)/\Xi(0))
-\sum_{0<\gamma\le R}\gamma^{-2k}.
\tag{MN7}
\]

The actual Gamma/zeta series supplies the first term, and a complete simple
real census supplies the second. Root intervals must be narrow enough to
resolve the difference; ordinary floating-point subtraction is not a
certificate. Higher coefficients can require refinement of low census roots.
The inherited FLINT historical finite-count input remains explicit whenever
that census is used. This lemma does not independently authenticate either
that historical computation or the analytic complete-product identity.
