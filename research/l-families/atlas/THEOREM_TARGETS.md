# Four theorem nominations from the L-function detector atlas

All statements below are **proposed targets**, not results. They are written to
make the missing arithmetic input explicit and to prevent a finite experiment
from being mistaken for a theorem.

## Target A — function-field trace individualization

Nomination: `FF-XD-TRACE-INDIVIDUALIZATION`
Programmes: #737 and #741.

Let `q` be an odd prime power and give the complete hyperelliptic family
`H_{2g+1}(q)` the uniform measure on monic squarefree polynomials of degree
`2g+1`. Work in the regime of fixed `g` and fixed kernel `K` as `q` tends to
infinity. Derive from one declared reciprocal-L degree kernel a finite
Hermitian statistic

\[
X_D(K)=\sum_{m,n=0}^{2g}K_{mn}H_D(m)\overline{H_D(n)},
\qquad H_D(n)=q^{-n/2}B_D(n),
\]

where `K=K^*` and `K` is the genuine function-field adapter for a selected canonical
`XD` or `HCNC` detector, not the toy lag-one probe.

For `U in USp(2g)`, let `H_U(n)` denote the coefficient of `t^n` in
`det(I-tU)^{-1}` and define

\[
X_U(K)=\sum_{m,n=0}^{2g}K_{mn}H_U(m)\overline{H_U(n)}.
\]

Prove an effective monodromy trace and variance theorem

\[
\frac1{|H_{2g+1}(q)|}\sum_D X_D(K)
=\int_{USp(2g)}X_U(K)\,dU+E_1(q,g,K),
\]

\[
\operatorname{Var}_{D\in H_{2g+1}(q)}X_D(K)
=\operatorname{Var}_{U\in USp(2g)}X_U(K)+E_2(q,g,K),
\]

with explicit errors strong enough to decide whether the required one-sided
bound is density-one or only averaged. Mean and variance control do not imply a
memberwise bound without an additional discrete gap or a pointwise estimate.
Before invoking monodromy, first determine whether the genuine kernel has a
deterministic sign on the `USp(2g)` character image; if it does not, the Haar
model may refute rather than support density-one positivity.

Why this target: the exhaustive `q=5,g=1` result proves that purity plus mean
cancellation cannot perform individualization. The exhaustive `q=3,g=2` result
shows that exact purity and the palindromic functional equation still allow all
three signs for a parity-even toy minor. The missing input must therefore
control the actual kernel's fluctuation or exceptional members, plausibly
through monodromy/sheaf estimates.

Number-field handoff: formulate the corresponding trace/exponential-sum bound
for the same coefficient kernel over integers; do not transfer the conclusion
merely from function-field RH.

## Target B — quadratic-twist excess-rank second moment

Nomination: `TWIST-EXCESS-RANK-L2`
Programmes: #738 and #741.

Fix a source-locked primitive self-dual GL(2) form `f`. For fundamental
discriminants in one explicitly defined root-number subfamily
`D_epsilon(X)`, let

\[
r_d=\operatorname{ord}_{s=1/2}\Lambda(f\otimes\chi_d,s),
\qquad
e_d=r_d-\frac{1-\varepsilon}{2}\in2\mathbf Z_{\ge0}.
\]

First prove the bounded second moment

\[
\sum_{d\in D_\varepsilon(X)}e_d^2
\ll_f |D_\varepsilon(X)|.
\]

The stronger minimalist-rank target is

\[
\frac1{|D_\varepsilon(X)|}\sum_{d\in D_\varepsilon(X)}e_d^2=o(1).
\]

For any fixed positive centered node packet this is exactly equivalent to the
same bound for the average squared parity/full detector correction:

\[
\frac1{|D_\varepsilon(X)|}\sum_d
\|M_d^{\rm parity}-M_d^{\rm full}\|_F^2
=\left(\sum_i x_i^{-2}\right)^2
\frac1{|D_\varepsilon(X)|}\sum_de_d^2.
\]

Why this target: it isolates legitimate rank contamination without depending
on the Loewner/Pick sign convention. It also controls the high-rank tail, which
a mere density-one nonvanishing statement need not do.

## Target C — root-number-split reciprocal-prime wavelet moment

Nomination: `TWIST-RECIPROCAL-PRIME-M2`
Programmes: #738 and #741, with a handoff to #737.

Fix the same `f`, one root-number subfamily, and a compact real prime weight
`w_p(P)` obtained from a declared reciprocal-L wavelet adapter. At good primes
define

\[
W_d(P)=\sum_{p\le P}
w_p(P)\frac{a_p(f)\chi_d(p)}{\sqrt p}.
\]

Prove, uniformly in a nontrivial range `P<=X^theta`, an exact diagonal main term
with a power-saving or otherwise summable off-diagonal error:

\[
\delta_{\varepsilon,X}(p)
=\frac1{|D_\varepsilon(X)|}
\sum_{d\in D_\varepsilon(X)}\chi_d(p)^2,
\]

\[
\frac1{|D_\varepsilon(X)|}\sum_{d\in D_\varepsilon(X)}W_d(P)^2
=\sum_{p\le P}w_p(P)^2\frac{a_p(f)^2}{p}
\delta_{\varepsilon,X}(p)
+O_{f,w}(E(X,P)),
\]

where bad primes, the fundamental-discriminant condition, and the root-number
restriction are all explicit. Away from special primes the unconditioned local
density is asymptotic to `p/(p+1)`, not `1`; the root-number restriction may
change it and must be computed. The error `E(X,P)` must be strong enough for the
intended compact detector limit.

Why this target: the Phase-0 table shows that raw GL(1) unit amplitude does not
survive degree two. This moment uses the correct unitary GL(2) coefficient and
asks quadratic-character orthogonality to supply the family law. The analogous
function-field theorem should be attacked first by exact character sums and
monodromy, providing a formula—not a transfer claim—for the number-field target.

The exact conductor-coprime precursor now computes the complete raw Gram and
centered covariance matrices for the fixed `11.a2` prime packet at
`X=256,512,1024,2048`, both pooled and in the sourced root-number cohorts
`epsilon_d=sign(d)*(d/11)`. The root-sign counts at the largest window are
568/574. Its pooled weighted radical correction to `E(W_d^2)` is nonmonotone,
and the root-cohort second-moment difference also changes sign across the four
windows. The off-diagonal root-cohort Gram-contrast RMS decreases from
`0.108858` to `0.039862`, but `sqrt(N)` times that RMS stays of order one and
the maximizing pair moves. This is why the target asks for a weighted, uniform
estimate rather than extrapolating an unweighted finite RMS or fitted rate.

## Target D — genus-two higher moments and effective USp(4) equidistribution

Nomination: `FF-GENUS2-TOY-MINOR-HIGHER-MOMENTS`
Programmes: #737 and #741.

For odd prime powers `q`, let `H_5(q)` be the uniform family of monic
squarefree quintics and write

\[
P_D(u)=1+a_Du+b_Du^2+qa_Du^3+q^2u^4,
\qquad
\frac1{P_D(u)}=\sum_{n\ge0}B_D(n)u^n.
\]

The exact algebraic lemma

\[
B_D(1)B_D(3)-B_D(2)^2=qa_D^2-b_D^2
\]

and the following first-moment formula are now proved in the bound DRAFT
research note:

\[
\frac1{|H_5(q)|}\sum_{D\in H_5(q)}
\frac{qa_D^2-b_D^2}{q^2}
=-\left(1-\frac1q\right)^2+\frac{q+1}{q^5}
\longrightarrow-1.
\]

The remaining target begins at moment two. Put

\[
F(U)=(\operatorname{Tr}U)^2-e_2(U)^2,
\qquad U\in USp(4).
\]

For each fixed `m>=2`, prove an effective formula

\[
\frac1{|H_5(q)|}\sum_{D\in H_5(q)}
\left(\frac{qa_D^2-b_D^2}{q^2}\right)^m
=\int_{USp(4)}F(U)^m\,dU+E_m(q),
\qquad E_m(q)\longrightarrow0,
\]

uniformly for `m` in any range needed by the chosen detector. Ideally expose
the conductor and representation dependence in an explicit square-root-scale
or better error, or derive exact rational functions in `q` for the first few
fixed moments. The normalization uses `P_D(t/sqrt(q))=det(I-tU)`, so
`a_D/sqrt(q)=-Tr(U)` and `b_D/q=e_2(U)`. Since
`Lambda^2 Std` is `1 + V_(omega_2)`, character orthogonality gives the proved
first Haar mean `-1`. Exact `C_2` Weyl constant terms give the next five targets

```text
m=2,3,4,5,6: 3, -11, 56, -374, 3117.
```

Why this target: the first moment no longer needs nomination. Its exact
squarefree-sieve proof shows that low moments can expose structure more sharply
than a three-field fit. The higher moments now test whether the full
hyperelliptic family approaches the compact-group law, not merely whether one
average has the right limit. A proof should decompose `F^m` into `USp(4)`
characters or evaluate the corresponding finite-field correlations, with an
effective error. This target remains about a toy coefficient minor; it does
not rename that minor as `XD`, `HCNC`, or a Pick/Loewner theorem.

## Falsification and promotion rules

For each nomination, a future computation should retain:

- the exact family definition and root-number split;
- the completed and local normalization fingerprints;
- a frozen detector contract before the final scan;
- explicit exceptional members and negative controls;
- source/coverage hashes and a compact replay;
- separate labels for memberwise, family-average, and density-one conclusions.

No target becomes a theorem node from numerical fit alone.
