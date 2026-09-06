# Corrected mathematical state

This guide is a scoped mathematical extraction of the four review streams, not a new assertion that every source branch passed review. The [decision register](../../../integration/2026-09-06/DECISIONS.json) binds the exact repairs and holds. Full proof texts and their original contexts are retained in [proof-extracts](proof-extracts/README.md). Classical inputs and reviewer-reported executions are not silently turned into new integrator executions.

## 1. A fixed Mellin consumer, not a completed arithmetic estimate

Use the tail convention

\[
\mathcal M f(s)=\int_1^\infty f(x)x^{-s-1}\,dx.
\]

If \(A(X)=\int_1^X f_-(x)\,dx/x=O_\epsilon(X^\epsilon)\) for every positive epsilon, then the transform of the negative part is holomorphic for \(\Re s>0\). On a compact set with minimum real part \(a>0\), take epsilon \(a/2\). The j-th derivative integral over the k-th dyadic block is bounded by a constant times \((k+1)^j2^{-ak/2}\); summation proves locally uniform convergence of every fixed derivative order. Local integrability pays the finite initial interval.

For an eventually nonnegative density with a finite real abscissa c, remove its finite signed head. The remaining logarithmic-coordinate Laplace transform has nonnegative Taylor coefficients when expanded towards the left. An analytic continuation across c would, by Tonelli applied to that Taylor series, give convergence at a smaller real exponent, a contradiction. This is the tail Landau theorem at the exact convention, not the full Mellin integral over all positive x with an uncontrolled small-x portion.

A nonzero analytic multiplier and an analytic additive defect cannot remove a genuine pole. The usual punctured-germ statement follows by division by the multiplier in a small disk. The existing formal predicate `not AnalyticAt` for a total function is weaker: its valid full-neighborhood transfer theorems must not be used as punctured-equality statements without this adapter.

These arguments reconstruct C4-M M1–M4 and the classical inputs used in the previous release. Fixed rows 2 and 3, or the fixed 5:3 scalar, retain their zero-safe algebra. The arithmetic negative-mass premise remains open. Neither a generic consumer nor its formal conditional implementation supplies that premise.

## 2. The two wavelet energies must remain different

Put \(a=X/8\), \(d_n=\mu(n)n^{-1/2}K_0(X/n)\), \(G=\sum d_n\), and \(S(v)=\sum_{n\ge v}d_n\). Finite expansion gives, for tau positive,

\[
\sum_{m,n}d_m\overline{d_n}\min(m,n)^{2\tau}
=a^{2\tau}|G|^2+2\tau\int_a^X|S(v)|^2v^{2\tau-1}\,dv.
\]

At tau one the Cauchy–Poisson energy therefore has boundary term \(a^2|G|^2\), not \(|G|^2\). D-F04 is an actual source mismatch at X=16, where G is nonzero. The old energy criterion survives only by D's separate suffix-field argument; it is not identified with the Poisson energy by renaming it. D-final R15 supplies the corresponding reciprocal-zeta growth and half-plane Hardy adapter for the correctly defined Poisson energy. Its abscissa is an infimum, not a claim of convergence on the boundary.

The compact Abel–Mertens frame and corrected same-kernel Vaughan translation survive. The #719 completed Euler–Beta field has a negative semiprime main and its old equivalence chain is withdrawn. That source is not #730's balanced native tail-pair source. All signed cross-core estimates retain the complete source and carrier cancellation before norms.

## 3. A corrected, nonvacuous conditional order-three Xi theorem

There are two separate results: the informal safe-axis mathematics and the fidelity of its Lean implementation. The latter had an empty input type; this does not refute the former.

Let the pinned entire completion satisfy

\[
\Lambda(s)=\Lambda_0(s)-1/s-1/(1-s).
\]

The correct entire function is

\[
\xi_{\mathrm{ent}}(s)=\tfrac12+\tfrac12s(s-1)\Lambda_0(s).
\]

It equals the usual product away from zero and one and has value one half at both removable endpoints. Define \(F(z)=\xi_{\mathrm{ent}}(1/2+z)\). This centered variable is not the alternative t-coordinate \(\xi_{\mathrm{ent}}(1/2+it)\). The old totalized product is zero at the endpoints; requiring its logarithmic-derivative diagonal to be positive at the half-node makes the old formal source input impossible.

The replacement source must allow empty, finite and countably infinite off-line spectra. Index actual distinct locations bijectively, attach analytic multiplicities as weights, and keep the selected critical reserve out of the other-critical list. An injective coding from each index set into Nat supplies a fixed exhaustion. An injective map from Nat into the off-line spectrum does not: it forces infinitely many off-line locations.

Here is the precise conditional paper theorem reconstructed by C4-X and separately checked in this integration. Fix H at least 1024, a selected critical location \(0<\gamma_0\le H/2\) of multiplicity \(m_0\ge1\), other critical locations \(\gamma_j>0\), and off-line representatives \(0<a_i<1/2,b_i>H\), all with positive integral multiplicity. Assume complete zero correspondence for an even real entire F of order less than two with F(0) nonzero, and

\[
\sum_j m_j/\gamma_j^2<\infty,
\qquad \sum_i m_i/b_i^2\le2(\log H+1)/H.
\]

Set \(r_0=\gamma_0^2,c_i=b_i^2-a_i^2,B_i=2a_ib_i\), and

\[
R(t)=2/(t+r_0),\quad q_i(t)=\frac{4m_i(t+c_i)}{(t+c_i)^2+B_i^2},\quad
p(t)=m_0R(t)+\sum_j\frac{2m_j}{t+\gamma_j^2}+\sum_iq_i(t).
\]

Evenness writes F(z)=G(z squared), where G has order less than one. Its complete genus-zero Hadamard product and locally uniform derivative bounds give

\[
p(t)=F'(\sqrt t)/(\sqrt t F(\sqrt t)),\quad t>0,
\]

with C2 convergence through every t at least zero. In particular the source is defined across t=1/4; no unjustified continuation of a sign is used.

Put \(d_i=c_i-r_0\), \(\kappa_i=B_i^2/d_i^2\), and \(\epsilon_i=2m_i\kappa_i/(1-\kappa_i)\). The source geometry gives \(\epsilon_i\le9m_i/b_i^2\). The shares are independent of t, and their total is at most \(297/512\), leaving at least \(215/512\) of one reserve unit.

For \(E(f)=ff''-2(f')^2\), the exact one-orbit calculation gives

\[
q_i+\epsilon_iR>0,\qquad E(q_i+\epsilon_iR)\ge0.
\]

For positive functions, writing \(A=\sum f_i\) and \(u_i=f_i'/f_i\),

\[
E(A)=A\sum_i E(f_i)/f_i+2\sum_{i<j}f_if_j(u_i-u_j)^2.
\]

Combine every paid off-line term with the unused reserve, the residual \((m_0-1)R\), and all other critical terms. The shares cancel exactly at every finite prefix, including both derivatives. C2 convergence yields \(p>0\) and \(E(p)\ge0\). Direct source differentiation also gives \(p'<0,(tp)'>0,(tp)''<0\); hence \(1/p\) is concave.

For positive x_i, let \(t_i=x_i^2\) and

\[
K_{ij}=\frac{x_ip(t_i)+x_jp(t_j)}{x_i+x_j}.
\]

The exact two-node determinant is strictly positive at distinct nodes. For three distinct nodes the determinant factors as

\[
\frac{p(t_1)p(t_2)p(t_3)\prod_{i<j}(t_j-t_i)^2}
{\prod_{i<j}(x_i+x_j)^2}
\,[t_1,t_2,t_3](1/p)\,[t_1,t_2,t_3](tp)\ge0.
\]

The positive two-node pivot and scalar Schur complement prove PSD. Repeated nodes are the pullback of the distinct-node matrix under coefficient summation, not an assertion about confluent derivative kernels. Thus every packet of size at most three is PSD under the stated source hypotheses.

For actual xi the finite-height theorem, low reserve, complete zero correspondence, growth and all-height counting bound must still be attached to their reviewed sources. No zero census was rerun. The paper repair is accepted at this conditional scope; a complete corrected Lean input construction, compilation, comparator and axiom audit are not supplied by this integration. Order four and above remain open. Finite models with far off-line quartets satisfy the hypotheses, so the argument has not encoded RH in an empty-spectrum premise.

## 4. Finite-window Schur elimination is not a sign certificate

The #792 two-proof operator scope, independently reviewed in C4-O, keeps the whole arithmetic kernel, including its cusps and tail. Energy continuity supplies Riesz representatives in the completion of the positive subspace; they need not belong to the original L2 space. The effective matrix \(S_L=C-\operatorname{Gram}_q(g_i)\) controls full-window positivity and negative index, not an unrestricted nullity identity.

Finite Galerkin matrices approach S from above. Positive upper approximations alone do not prove S nonnegative. For exact trial corrections, the full cross-term residual matrices give

\[
U-3R\preceq S_L\preceq U,
\qquad U-(15/8)R\preceq S_1\preceq U
\]

in the separately specified L=1 subspace. A certified nonnegative lower matrix would establish that window. None is supplied here. Sampled positive minima are not continuum enclosures, and a single fixed window is not the required unbounded sequence of windows.

The #793 pass7 corrected Euler/Dickman norm theorem is at the classical line Re(s)=1 on its stated PNT/Mertens inputs. It does not provide corrected-product local boundedness throughout Re(s)>1/2. Neither the correction's positive density nor finite source agreement proves contraction below one.

## 5. The fixed P61 theorem has replacement evidence

For P the product of the eighteen primes through 61, let

\[
q=6\mathbf1-6\delta_1+9\delta_2-3\delta_4,
\quad H_x(n)=\min(\log4,\log(x/n))_+,
\quad A(x)=\sum_nq(n)H_x(n)/\sqrt n.
\]

Let F and M be its signed and unsigned divisor sums over P, with weight \(d^{-1/2}\). D4 R25 supplies a new complete proof/evidence chain for

\[
0\le F(x)\le M(x)\ (1\le x<67),
\qquad M(x)/42\le F(x)\le M(x)/8\ (x\ge67).
\]

The old 1/40 bound remains false. The old printed singleton for C0 was not an enclosure; preserving its bytes does not preserve its certification status. D's replacement uses directed MPFR primitives followed by integer intervals, 1,999,994 finite inequalities through one million, the compact analytic error bound, all 262,144 divisors, and both endpoints of every relevant tail slab plus the final infinite slab. This is reviewer-executed replacement evidence, not a new integrator execution of the whole campaign. The integration independently reconstructs the finite coefficient formulas through n=200 and preserves the full D4 source, outputs and runtime limitations.

The theorem is fixed-P61. Neither growing-prime uniformity nor the dynamic critical Bellman block follows from it. D3's actual-source weighted-variation proof and D-final's Stieltjes/Hardy adapters remain explicit analytic dependencies.

## 6. Structural and certificate boundaries

B's corrected HPL convention is \(p\delta(1+h\delta)^{-1}i\) when \(dh+hd=1-ip\). Higher-page differentials also require lower-component zigzags. The finite arity cutoff, support and Euler identities retain their actual Chow-table/N3 dependencies; a virtual character does not identify each genuine module.

Generic degree laws are not universal specialization laws. The torsion entry threshold is not blanket persistence: the a=0, R=2, m=6 example has discriminant 16. A leading divisor-renewal resonance is not exact finite-weight cancellation. The native growing Poincare precision assertions and Epstein complete directed contours remain held. A pointwise Stieltjes-density asymptotic at infinitely many square-root spikes is replaced by the proved integrated statement, not silently retained.

A's corrected finite seven-point certificate and analytic adapters are kept separate from C's refutation of the old X105560 wrapper. The 269 expression has the corrected decimal 0.6730085279277797613...; its use as a simple-zero proportion retains all analytic input and normalization requirements. No public-priority claim follows from this integration.

In the old main audit, every D-F01–18 correction remains binding. These include point-spectrum versus spectrum, all versus leading principal minors, correctly signed Farkas alternatives, rational-data certificate assumptions, real-part jump dissipation, the 2pi Fredholm normalization, four-sector Q4 ownership, signed Hilbert cancellation, activation-aware gauges, net poles, and the negative elementary prime atom. None is a counterexample to RH. The exact repaired statement, not a broad negative slogan, is the reusable result.
