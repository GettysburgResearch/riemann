# Route 1: a source-exact nuclear determinant and a marked positivity obstruction

Status: complete mathematical arguments supplied, **PROPOSED / INDEPENDENT REVIEW REQUIRED**.
Scope: an unconditional scalar determinant construction; two unconditional obstructions to stronger marked constructions; no positive scalar operator and no RH proof.
Sources: PR #785 at `9a965c26fd3e0310736829689db1734bcb5c3ec4`, especially the theta–Fock and spectral theta–Darboux notes. The new arguments do not assume their open positivity gates.
What was run: exact finite companion, covariance, and cumulant controls in `../code/verify.py`.
Smallest remaining gap: a genuinely positive **scalar** realization, or a direct all-order sign theorem for the scalar coefficients. A positive realization preserving the natural occupation labels is impossible.

The packet-local IDs below deliberately do not enter the repository-wide numerical claim namespace. Standard Fredholm, covariance, and generating-function tools are credited; external novelty is not established.

## R1.1. Normalization and the actual source

Let

\[
 \xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
 F(u)=\xi\!\left(\tfrac12+\sqrt{u+\tfrac14}\right),\qquad
 f(u)=F(u)/F(0)=\sum_{n\ge0}a_nu^n.
\]

The square root causes no multivaluedness: the functional equation makes the centered xi function even. Here `F(0)=xi(1)=1/2` and `a_0=1`.

Set, for `tau>=0`,

\[
 g(\tau)=e^{\tau/2}\sum_{m\ge1}e^{-\pi m^2e^{2\tau}},\quad
 \Phi(\tau)=(\partial_\tau^2-\tfrac14)g(\tau)
 =\sum_{m\ge1}(4\pi^2m^4e^{9\tau/2}-6\pi m^2e^{5\tau/2})e^{-\pi m^2e^{2\tau}}.
\]

Every summand is positive because `pi*m^2*exp(2tau)>3/2`. The theta identities give

\[
 F(u)=2\int_0^\infty\Phi(\tau)\cosh\!\left(\tau\sqrt{u+\tfrac14}\right)d\tau.
 \tag{1}
\]

These are the actual full-source conventions of the parent, not a positive replacement. In particular, define the probability measure

\[
 d\nu(\tau)=4\Phi(\tau)\cosh(\tau/2)d\tau.
 \tag{2}
\]

The half-integer cosine product yields

\[
 f(u)=\int\prod_{j\ge0}(1+u\lambda_j(\tau))d\nu(\tau),\qquad
 \lambda_j(\tau)=\frac1{\tfrac14+\pi^2(j+\tfrac12)^2/\tau^2}.
 \tag{3}
\]

For fixed `tau`, the product converges locally uniformly, and `sum_j lambda_j(tau)<infinity`. The integrals in (1)–(3) converge normally on compact `u` sets. For example, the product of absolute factors is bounded by the same positive product at `|u|`, and the superexponential theta tail makes that integrable.

## R1.2. Explicit scalar trace-class realization without zeros

**Theorem.** The actual `f` has a source-coefficient-defined trace-class operator `C` on `ell^2(N_0)` with

\[
 \det(I+uC)=f(u),\qquad u\in\mathbb C.
 \tag{4}
\]

No xi zeros enter the construction. This operator is not positive, and its construction also works for many entire counterfeits.

Define rational shift weights and their products by

\[
 w_n=\frac1{(n+1)\lceil\sqrt{n+1}\rceil},\quad
 B_0=1,\quad B_n=\prod_{j=0}^{n-1}w_j,
 \qquad S e_n=w_ne_{n+1}.
\]

Define

\[
 v_n=(-1)^n a_{n+1}/B_n,\qquad C=S+|e_0\rangle\langle v|.
 \tag{5}
\]

The `a_n` and `v_n` are real. In a complex-coefficient generalization, conjugate the entries of `v` in (5) so that its row functional has the prescribed coefficients.

### Proof of trace class

From (1), with `r=sqrt(|u|+1/4)`, an elementary Gamma-integral bound gives

\[
 \log\max_{|u|\le R}|F(u)|=O(\sqrt R\log(R+2)).
 \tag{6}
\]

Indeed `Phi(tau)<=C exp(9tau/2-pi exp(2tau))` for `tau>=0`; substitute `x=exp(2tau)` and bound the resulting integral by a Gamma integral. Cauchy's bound on the radius `R=n^{5/3}` consequently gives

\[
 \log|a_n|\le-\tfrac53n\log n+o(n\log n).
\]

A zero coefficient only strengthens this bound. Since

\[
 2^{-n}(n!)^{-3/2}\le B_n\le(n!)^{-3/2},
\]

we obtain `log|v_n|<=-(1/6)n log n+o(n log n)`. Thus `v` is square summable, with a superpolynomial tail. Also `sum_n w_n<infinity`, so `S` is trace class and the second term of (5) is rank one.

### Proof of the determinant identity

Let `P_N` project onto `e_0,...,e_(N-1)`, and let `C_N=P_N C P_N` on that space. Its shift part is nilpotent. The finite rank-one determinant identity gives

\[
 \det(I+uC_N)
 =1+u\sum_{j=0}^{N-1}v_j(-u)^jB_j
 =\sum_{j=0}^{N}a_ju^j.
 \tag{7}
\]

Moreover,

\[
 \|C-C_N\|_1
 \le\sum_{n\ge N-1}w_n+
       \left(\sum_{n\ge N}|v_n|^2\right)^{1/2}\longrightarrow0.
 \tag{8}
\]

Here `C_N` is extended by zero outside its range. Trace-norm continuity of the Fredholm determinant, or directly its absolutely convergent exterior-power expansion, passes (7) to (4). This proves the theorem.

The construction genuinely supplies a nuclear scalar determinant, but it does not explain why a positive realization should exist. It is a useful source-exact test object, not a spectral proof of RH.

## R1.3. This companion cannot be made positive by diagonal reweighting

For `x=e_1-e_2`, the rank-one row in (5) has zero pairing with `x`, and

\[
 \langle x,Cx\rangle=-w_1=-\tfrac14,\qquad
 \frac{\langle x,Cx\rangle}{\|x\|^2}=-\tfrac18.
 \tag{9}
\]

This holds for the actual xi coefficients, independently of their values. Thus `C` is not positive or accretive. In fact no strictly positive diagonal metric `G=diag(g_n)` can make it self-adjoint: the `(2,1)` entry of `GC` is `g_2 w_1`, whereas the same entry of `C^*G` is zero.

A general non-diagonal similarity has not been constructed. Its existence should not be assumed equivalent to RH: diagonalizability and bounded conditioning can impose additional obligations, particularly at multiple zeros. The scalar positive-determinant target remains distinct from a demand to symmetrize this particular companion.

## R1.4. The actual theta mixture cannot preserve its mode labels in a positive determinant

For distinct modes `i,j`, (3) defines the marked two-variable polynomial

\[
 Z_{ij}(x,y)=1+A_i x+A_j y+C_{ij}xy,
\]

where `A_i=E_nu lambda_i` and `C_ij=E_nu(lambda_i lambda_j)`.

**Theorem.** For the actual measure (2),

\[
 C_{ij}>A_iA_j.
 \tag{10}
\]

Consequently no positive Hermitian operator can reproduce these marked singleton and two-mode coefficients as its principal minors.

**Proof.** Each `lambda_j(tau)` is strictly increasing on `(0,infinity)`, and `nu` has positive density there. Hence

\[
 C_{ij}-A_iA_j
 =\tfrac12\iint
 (\lambda_i(t)-\lambda_i(s))
 (\lambda_j(t)-\lambda_j(s))d\nu(t)d\nu(s)>0.
\]

But a Hermitian matrix with diagonals `A_i,A_j` has two-mode principal minor `A_iA_j-|K_ij|^2<=A_iA_j`. This contradicts (10). The argument rules out even arbitrary Hermitian off-diagonal entries in that marked two-mode block. QED.

This is stronger than the generic observation that mixtures need not be determinantal: it applies to the literal theta source. It does **not** refute an unmarked scalar determinant after setting every fugacity equal. Scalar coefficient matching aggregates many principal minors and need not preserve the original mode labels.

## R1.5. Independent obstruction in the parent's vacuum/forced-bit representation

The split-theta representation used by the parent is

\[
 F(v)=\tfrac12+2v\int_0^\infty g(\tau)
                  \cosh(\tau\sqrt{v+1/4})d\tau,\qquad v>0.
\]

Its count law has vacuum probability `w_0=1/(2F(v))`, and otherwise contains one forced occupation `I_*` plus the conditional Bernoulli modes. For an ordinary occupation `I_j`, write `b_j=E I_j>0`. Since `I_j=1` forces `I_*=1`,

\[
 \operatorname{Cov}(I_*,I_j)=w_0b_j>0.
 \tag{11}
\]

Every determinantal occupation process in those same orthogonal modes has covariance `-|K_*j|^2<=0`. Thus the vacuum and forced-bit labels alone already obstruct a source-mark-preserving quasi-free reduction. This is independent of the monotonicity argument above.

### Quantitative correction cost

Suppose desired singleton probabilities are `a,b` and desired pair probability is `c>ab`. If all three are approximated within absolute error `epsilon` by a determinantal process, then necessarily

\[
 c-\epsilon\le(a+\epsilon)(b+\epsilon),
\]

so

\[
 \epsilon\ge
 \frac{\sqrt{(1+a+b)^2+4(c-ab)}-(1+a+b)}2>0.
 \tag{12}
\]

This is a lower bound, not a claim of optimal attainable approximation. It prevents a vanishing-error marked identification from concealing the covariance mismatch.

## R1.6. The ordinary direct-integral determinant is not available

A nonzero decomposable operator over a nonatomic base is not compact whenever one fixed fiber direction is bounded below on a positive-measure set. To see this, split that set into countably many disjoint positive-measure subsets and use their normalized indicators in the fixed direction. Their images remain orthogonal with norms bounded below.

In the parent's split-theta direct integral the forced mode has eigenvalue one throughout the continuous component. The direct-integral operator is therefore not even compact, hence not trace class. Its **ordinary Hilbert-space Fredholm determinant is not defined**.

An exponential integral of fiber logarithmic determinants belongs to a differently specified trace/determinant formalism; it is not the ordinary Fredholm determinant of that nonatomic direct integral. This is a forward clarification of the parent note's direct-integral wording, not a modification of its frozen source or a refutation of its scalar gate.

## R1.7. The scalar mixture debt is explicit

Let `T_k(tau)=sum_j lambda_j(tau)^k`, and define scalar cycle quantities by

\[
 \log f(u)=\sum_{k\ge1}(-1)^{k-1}s_k u^k/k.
\]

Differentiation of (3) at zero is justified by the theta tail and gives

\[
 s_1=E T_1,\qquad
 s_2=E T_2-\operatorname{Var}(T_1),
 \tag{13}
\]

\[
 s_3=E T_3-\tfrac32\operatorname{Cov}(T_1,T_2)
                  +\tfrac12\kappa_3(T_1).
 \tag{14}
\]

These follow by expanding `log E exp(u T_1-u^2 T_2/2+u^3 T_3/3+...)`. They isolate the latent-selector corrections. In a positive scalar realization, `s_k=Tr(K^k)`; the fiberwise positive traces alone do not prove this because the covariance/cumulant debts remain.

## R1.8. What would finish this route

A positive trace-class `K` with `det(I+uK)=f(u)` would put every zero of `F` on the negative real axis. Equation (1) makes `F(u)>0` on `u>=-1/4`, so every such zero has `u<-1/4`, forcing `s=1/2+it` and proving RH.

The pass closes the **unrestricted nuclear determinant construction**, refutes **marked** positive collapse, and identifies explicit scalar mixing debts. It does not close positivity. The surviving research target must permit a genuinely nonlocal reorganization of modes while proving the scalar exterior-character identity exactly. Neither a direct integral nor a diagonal metric repair can supply it.
