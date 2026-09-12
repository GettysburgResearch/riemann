# A calibrated connected infinite Ising chain matching theta through degree eight

12 September 2026. **New proposed component theorem, with a directed finite
certificate. This is not a proof of RH or an all-order realization theorem.**
The underlying source quadrature and harmonic-tail arithmetic are explicitly
imported from PR #875 at `be149104721ae7b65b624c100118edfd7b76b69b` and freshly
executed here. Their analytic remainders remain part of the proof dependency.
The construction improves the matched order within the three-term calibrated
infinite-chain family; it does not exceed the degree-fourteen finite and
leading-growth infinite-star constructions in #863/#867.

## 1. Exact source and the statement

Let

\[
\phi(t)=\sum_{n\ge1}(4\pi^2n^4e^{9t/2}-6\pi n^2e^{5t/2})e^{-\pi n^2e^{2t}},
\qquad t\ge0,
\]

with its even Jacobi continuation, and normalize it to a probability density
\(w\). Its characteristic function is \(\Xi(z)/\Xi(0)\). Write
\(\mu_{2r}=\int t^{2r}w(t)dt\) and \(\kappa_{2r}\) for its cumulants.

**Theorem.** There exists \(\epsilon>0\) and analytic positive functions
\(a(q),b(q),c(q),e(q),\tau(q)\), for \(0\le q<\epsilon\), giving the following
Markov sign chain. Its first sign is uniform, all edge correlations are \(q\)
except the edge between sites 26 and 27, whose correlation is \(\tau(q)\).
Its observable weights are

\[
\underbrace{a,\ldots,a}_{25},\quad
\underbrace{b,b,b,b}_{4},\quad c,e,\qquad
a_n(q)=\frac1{2n}+d(q)\frac{\log n}{n^2},\quad n\ge32.
\]

The \(L^2\) limit \(X_q=\sum a_n(q)\sigma_n\) exists. For every
\(0<q<\epsilon\), this is a genuinely connected infinite nearest-neighbor
ferromagnet, with all couplings strictly positive. It has an analytic density,
an entire characteristic function with only real zeros, and

\[
E X_q^{2r}=\mu_{2r}\quad (r=1,2,3,4),
\]

\[
\log E e^{hX_q}=\frac h2\log h-
\frac{1+\log(2\pi)}2h+\frac74\log h+O_q(1),\quad h\to+\infty.
\tag{1}
\]

All odd moments vanish. The law is not theta: after decreasing \(\epsilon\),
its standardized tenth-moment error lies strictly between \(.03\) and \(.04\).
No explicit numerical value of \(\epsilon\) is claimed.

## 2. The calibration and why a finite edge can be changed

Use precisely the calibration in #871/#875:

\[
\ell(q)=\log((1+q)/2),\quad d(q)=7/(8\ell(q)),\quad
r(q)=(1-q)/(1+q),
\]
\[
m_q(u)=\frac{\sinh u}{\sqrt{\sinh^2u+r(q)^2}},\qquad
C(q)=-1+\int_0^1\frac{m_q(u)}u\,du+
\int_1^\infty\frac{m_q(u)-1}u\,du.
\]

Let \(S=\sum_{n\ge32}\log n/n^2\), \(H_{31}=\sum_{n\le31}1/n\), and

\[
A(q)=-\frac{1+\log(2\pi)}2
-\frac{-\log2+C(q)+\gamma}2+\frac{H_{31}}2-d(q)S.
\tag{2}
\]

Impose \(25a+4b+c+e=A(q)\). These functions are holomorphic near zero:
the square root in \(m_q\) has an analytic branch there, its denominator is
uniformly nonzero on the positive real integration axis, and the differentiated
large-\(u\) remainders decay exponentially. The logarithm in \(d(q)\) stays
nonzero. For sufficiently small real \(q\), \(a_n(q)\) is positive, decreasing,
and lies between \(1/(4n)\) and \(1/(2n)\).

For a homogeneous chain of correlation \(q\), #871/#875 prove (1) with these
tail weights and *any* positive finite head of total mass \(A(q)\). The
proof retains the noncommuting transfer matrices by a bounded Perron-vector
comparison, and then applies full Riemann sums to the harmonic and logarithmic
tail corrections. It uses no RH assumption.

Changing just one edge from \(q\) to \(\tau\) preserves (1). Indeed on every
finite prefix containing that edge the exact Radon--Nikodym derivative is

\[
\frac{1+\tau\sigma_{26}\sigma_{27}}{1+q\sigma_{26}\sigma_{27}}.
\tag{3}
\]

For \(0\le q,\tau<1\), it lies between the positive minimum and maximum of
\((1+\tau)/(1+q)\) and \((1-\tau)/(1-q)\). Multiplying by the positive real
integrand \(e^{hX_N}\), integrating, and passing to the complete limit shows
that the two MGFs have a ratio bounded above and below independently of real
\(h\). This proves the preservation of all three coefficients, including the
\(O(1)\) remainder. No mixture of laws or deletion of a covariance is used.

At \(q=0\), the Mellin calculation already supplied in #875 gives

\[
d_0=-\frac7{8\log2},\qquad
A_0=\frac{H_{31}}2-\gamma-\log2-d_0S.
\tag{4}
\]

These are the exact scalar targets used in the accepting computation.

## 3. The new finite inverse problem

At \(q=0\), sites 26 and 27 form one dimer; all other spins are independent.
Let \(\tau=\tanh J\). Its observable is \(b(\sigma_{26}+\sigma_{27})\), whose
even moments are \((1+\tau)(2b)^{2r}/2\). Thus its cumulants are
\(b^{2r}K_r(\tau)\), with

\[
\begin{aligned}
K_1(t)&=2+2t,\\
K_2(t)&=-4-16t-12t^2,\\
K_3(t)&=32+272t+480t^2+240t^3,\\
K_4(t)&=-544-7936t-24192t^2-26880t^3-10080t^4.
\end{aligned}
\tag{5}
\]

They follow from the moment--cumulant recurrence; `test_algebra.py` checks them
against all four configurations, independently of that polynomial derivation.
Let \(c_1,c_2,c_3,c_4=(1,-2,16,-272)\) be the independent-sign cumulants, and
\(T_k=\sum_{n\ge32}(1/(2n)+d_0\log n/n^2)^k\). The five equations are

\[
25a+4b+c+e=A_0,
\]
\[
25a^{2r}+2b^{2r}+c^{2r}+e^{2r}
+b^{2r}K_r(\tau)/c_r
=\kappa_{2r}/c_r-T_{2r},\quad 1\le r\le4.
\tag{6}
\]

The two remaining independent \(b\)-spins are retained, hence the coefficient
2 in (6), while the mass equation counts all four \(b\)-weights.

The exact rational centers are in `certify_dimer.py`; approximately they are

\[
\begin{aligned}
a&=.02243295324256231427575472092255325,\\
b&=.06173395819937378395798769517692535,\\
c&=.11121958141791680469782121451872279,\\
e&=.00260321904240238838084407029067456,\\
\tau&=.04452542381077457922311144103405805.
\end{aligned}
\]

The claimed point is the root in the entire closed infinity-norm box of radius
\(10^{-12}\) around these centers, not their rounded display values.

The checker reconstructs the complete theta moments by #875's analytic-strip
trapezoidal rule, paying both spatial lattices, every omitted theta index,
aliasing, normalizer uncertainty and dyadic rounding. It reconstructs all
\(T_2,T_4,T_6,T_8\) by the signed binomial expansion and Euler--Maclaurin
bounds, including the omitted \(B_6\) boundary term and the entire periodic
remainder. It also reconstructs (4). No predecessor numerical receipt is an
accepting input.

For the exact rational inverse \(R\) of the center Jacobian, on the *whole*
box it verifies

\[
\|R F(x_0)\|_\infty<7.63\cdot10^{-22},\qquad
\sup_{x\text{ in box}}\|I-RDF(x)\|_\infty<1.252\cdot10^{-7}.
\tag{7}
\]

Both inverse identities are checked entrywise: 50 rational equalities.
The strict inequality \(\beta+L10^{-12}<10^{-12}\) makes
\(x\mapsto x-RF(x)\) a contraction of the box into itself. Banach proves one
exact root and uniqueness within the box. All its weights and \(\tau\) are
strictly positive, and \(\tau<1\). Because \(L<1\), the exact Jacobian at the
root is also nonsingular. Independent meshes 1/128 and 1/160 of the *same*
backend certify the same box; this is not an independent implementation.

## 4. A reusable analytic lemma for every fixed cumulant order

**Lemma (gap divisibility).** Fix a number \(k\) of spin occurrences, allowing
repeated indices, in a symmetric Markov sign chain. Group their distinct
ordered sites as \(i_1<\cdots<i_d\), and write
\(v_j=\prod_{i_j\le n<i_{j+1}}r_n\), where \(r_n\) is the edge correlation.
Their joint cumulant is a polynomial in the \(v_j\), divisible by
\(v_1\cdots v_{d-1}\). If \(|r_n|\le r_*<1\), then

\[
|\operatorname{cum}(\sigma_{n_1},\ldots,\sigma_{n_k})|
\le B_k r_*^{\max n_j-\min n_j},
\quad B_k=\sum_{\pi\in\mathcal P_k}(|\pi|-1)!.
\tag{8}
\]

For \(d=1\), the product is empty and the same bound holds.

*Proof.* Every even Markov product moment is a monomial in the \(v_j\), while
every odd moment is zero. The partition formula for a cumulant therefore
produces a polynomial whose coefficient absolute sum is at most \(B_k\).
Set any \(v_j=0\). For real correlations this cuts the chain into two
independent nonempty collections, so their joint cumulant vanishes. A polynomial
identity on the real correlation cube is an identity over the complex
variables; therefore each \(v_j\) divides the polynomial. After cancellation,
every surviving monomial contains all \(v_j\) at least once. Its remaining
powers have modulus at most one. This proves (8).

Consequently, if weights depend holomorphically on finitely many parameters
and are locally uniformly \(O(1/n)\), every fixed even observable cumulant
has an absolutely, locally uniformly convergent spin-cumulant series.
For fixed ordered gaps, Holder bounds the translation sum of products of
\(2r\) weights by \(\sum_n|a_n|^{2r}\). The sum over positive gaps is bounded
by products of geometric series from (8); repetitions give only finitely many
multiplicity patterns. Normal convergence proves holomorphy.

This argument works at order eight and above without assuming a special
sixth-cumulant formula. It proves analytic regularity, not solvability of an
inverse problem at arbitrary orders.

## 5. Continue the certified seed to a connected infinite chain

Apply the lemma near the exact root to the family with all ordinary edge
correlations \(q\) and the distinguished edge correlation \(\tau\). Shrink
the complex parameter neighborhood so that all correlations have modulus
at most some fixed \(r_*<1\). The moment constraints through eight and the
mass constraint (2) are then holomorphic. Their Jacobian in
\((a,b,c,e,\tau)\) is nonsingular at \(q=0\), by (7). The analytic
implicit-function theorem supplies the five analytic head/edge parameters.
Continuity preserves positivity and \(\tau<1\) for sufficiently small \(q>0\).

For these real parameters, the covariance of two spins is the product of
correlations along their connecting path. Hence

\[
\operatorname{Var}\!\left(\sum u_n\sigma_n\right)
\le\frac{1+r_*}{1-r_*}\sum u_n^2.
\tag{9}
\]

This constructs the actual complete \(L^2\) observable. The finite weighted
Lee--Yang theorem applies to every finite marginal. Its paired entire product
implies

\[
\frac{E X_N^{2j}}{(2j)!}\le\frac{(\operatorname{Var}X_N/2)^j}{j!}.
\tag{10}
\]

Uniform variances give uniform exponential integrability and local uniform
entire convergence. Hurwitz proves real-zero geometry for the full limit,
which is nonzero at zero. Conditioning on the even spins gives conditionally
independent odd spins with biases bounded away from one; applying this to odd
indices in \([|t|,2|t|]\) yields exponential decay of the characteristic
function and an analytic density, exactly as in #871/#875. The finite special
edge does not affect that remote block argument. Equations (2)--(3) give (1).

The source is unbounded and has no nonzero Gaussian convolution factor:
\(\log M(h)/h\to\infty\), whereas \(\log M(h)=o(h^2)\).

## 6. The complete tenth-moment separation

The polynomial recurrence also gives \(K_5\), recorded in the certificate.
The independent sign cumulant is \(c_5=7936\). Every tail weight is between
zero and \(1/(2n)\), so the *entire* tenth power tail obeys

\[
0<T_{10}<\frac1{2^{10}}\sum_{n\ge32}n^{-10}
\le\frac1{2^{10}\,9\,31^9}.
\]

Evaluate
\(7936(25a^{10}+2b^{10}+c^{10}+e^{10}+T_{10})+b^{10}K_5(\tau)\)
over the whole root box and subtract the freshly reconstructed native tenth
cumulant. Since every lower cumulant matches exactly, this is also the raw
tenth-moment difference. Dividing by the fixed native \(\mu_2^5\) gives

\[
.03321148056<\frac{E X_0^{10}-\mu_{10}}{\mu_2^5}<.03321163717.
\tag{11}
\]

Holomorphic regularity includes degree ten. Thus (11), with the wider interval
\((.03,.04)\), persists after decreasing the positive \(q\)-neighborhood.
The new chain is demonstrably not theta; no claim of global target crossing,
uniform conditioning in the order, or RH follows.

## 7. What the calculation adds

The successful change was chosen using a compensated edge derivative, not by
discarding a constraint. At an independent seed, an edge between weights
\(u,v\) changes the log-MGF by \(\tanh(uh)\tanh(vh)\) to first order.
Let the head constraint vector consist of its mass and the normalized
cumulants through six. If \(J\) is its Jacobian and \(j_8\) the next row, put
\(\lambda=j_8J^{-1}\). Then the compensated normalized eighth-cumulant
derivative is \(d_4-\lambda\cdot(0,d_1,d_2,d_3)\), where

\[
\begin{aligned}
d_1&=2uv,\\
d_2&=4uv(u^2+v^2),\\
d_3&=6uv(u^4+v^4)+5u^3v^3,\\
d_4&=8uv(u^6+v^6)+\frac{112}{17}u^3v^3(u^2+v^2).
\end{aligned}
\]

At the exact rational center of #875, the resulting *raw* eighth-cumulant
derivative for a \(bb\) edge is positive, approximately \(7.9770\cdot10^{-7}\).
That center calculation was a scout, not a native-root certificate. Equations
(6)--(7) are the subsequent directed target certificate, so the new theorem
does not depend on trusting the rounded derivative or extrapolating it.

## References and reproducibility

- [#875 pinned ISING.md](https://github.com/GettysburgResearch/riemann/blob/be149104721ae7b65b624c100118edfd7b76b69b/standalone/2026-09-12-astra-collision-chain-flow/ISING.md)
  and its NUMERICS.md: source, complete arithmetic remainders, calibration.
- [#871 pinned PROOF.md](https://github.com/GettysburgResearch/riemann/blob/43a9eea85e20202370cae4b6ffa1a2c30fc3cfc3/standalone/2026-09-12-astra-connected-theta-chain/PROOF.md): bounded Perron reduction and three-term growth.
- [Newman--Wu, 2019](https://arxiv.org/abs/1901.06596), equation (21) and the
  following weighted statement: the finite Lee--Yang import. Definition 15,
  Theorem 16 and equations (27)--(28) give the broader weak-closure context.

Run `python -B extract_predecessor.py` only to reproduce the read-only pinned
extraction, then `python -B certify_dimer.py`, `python -B certify_dimer.py
--mesh 160 --output dimer-certificate-mesh160.json`, and
`python -B test_algebra.py`. The two complete certificates and all four
independent finite algebra tests passed. The initial failed run detected an
integer-division coercion in the center Jacobian's constant row; converting
that row to exact rationals corrected it before any accepting result.
