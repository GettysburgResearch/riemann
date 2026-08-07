# L-15109 — Bézoutian root-threshold criterion for a special target completion

Claim ID: `L-15109`  
Status: `PROPOSED`  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: `L-15107`, the finite special divided-difference form, and the classical Bézoutian/Hermite inertia theorem  
Scope: CCM boundary vector `eta=(1,...,1)` and simple target roots  
Related counterexample candidates: none

## 1. Polynomial data

Let

\[
 \lambda_1,\ldots,\lambda_n
\]

be distinct real nodes and put

\[
 \Omega(s)=\prod_{j=1}^n(\lambda_j-s),
 \qquad
 \phi_i(s)=\frac{\Omega(s)}{\lambda_i-s}.
 \tag{L-15109.1}
\]

Let the real target satisfy

\[
 p_i\ne0,
 \qquad
 \sum_i p_i=1,
 \tag{L-15109.2}
\]

and define its interpolation polynomial

\[
 \boxed{
 P(s)=\sum_{i=1}^n p_i\phi_i(s).}
 \tag{L-15109.3}
\]

Suppose the finite special matrix has off-diagonal entries

\[
 Q_{ij}=\frac{\beta_i-\beta_j}{\lambda_i-\lambda_j}
 \qquad(i\ne j).
 \tag{L-15109.4}
\]

For the scalar completion `T_p(c)` of `L-15107`, put

\[
 g_i(c)=\beta_i-c\lambda_i
 \tag{L-15109.5}
\]

and define

\[
 \boxed{
 R_c(s)=\sum_{i=1}^n p_i g_i(c)\phi_i(s).}
 \tag{L-15109.6}
\]

The scalar dependence is explicit. With

\[
 R_0(s)=\sum_i p_i\beta_i\phi_i(s),
\]

one has

\[
 \boxed{
 R_c(s)=R_0(s)-c\{sP(s)+\Omega(s)\}.}
 \tag{L-15109.7}
\]

Indeed

\[
 \sum_i p_i\lambda_i\phi_i(s)
 =sP(s)+\sum_i p_i(\lambda_i-s)\phi_i(s)
 =sP(s)+\Omega(s).
\]

## 2. Exact Bézoutian congruence

Define the symmetric polynomial kernel

\[
 \boxed{
 \mathcal B_c(s,t)
 =\frac{P(s)R_c(t)-P(t)R_c(s)}{s-t}.}
 \tag{L-15109.8}
\]

The apparent diagonal singularity is removable. Let

\[
 P_i=P(\lambda_i)=p_i\phi_i(\lambda_i)\ne0.
\]

Then the node-evaluation matrix

\[
 K_c=(\mathcal B_c(\lambda_i,\lambda_j))_{i,j=1}^n
\]

satisfies the exact congruence

\[
 \boxed{
 K_c=-\operatorname{diag}(P_i)\,
       T_p(c)\,
       \operatorname{diag}(P_i).}
 \tag{L-15109.9}
\]

### Off diagonal

For `i!=j`,

\[
 \mathcal B_c(\lambda_i,\lambda_j)
 =P_iP_j\frac{g_j(c)-g_i(c)}{\lambda_i-\lambda_j}
 =-P_iP_j(T_p(c))_{ij}.
\]

### Diagonal

At one node,

\[
 \mathcal B_c(\lambda_i,\lambda_i)
 =P'(\lambda_i)R_c(\lambda_i)
  -P(\lambda_i)R_c'(\lambda_i).
\]

Using

\[
 \phi_j'(\lambda_i)
 =\frac{\phi_i(\lambda_i)}{\lambda_i-\lambda_j}
 \qquad(i\ne j)
\]

and the forced kernel equation `T_p(c)p=0` gives

\[
 \mathcal B_c(\lambda_i,\lambda_i)
 =-P_i^2(T_p(c))_{ii}.
\]

This proves (L-15109.9).

## 3. Root diagonalization

Assume that `P` has `n-1` distinct real roots

\[
 r_1<\cdots<r_{n-1}.
 \tag{L-15109.10}
\]

At those roots,

\[
 \mathcal B_c(r_k,r_l)=0
 \qquad(k\ne l),
\]

and

\[
 \boxed{
 \mathcal B_c(r_k,r_k)
 =P'(r_k)R_c(r_k).}
 \tag{L-15109.11}
\]

Evaluation at the simple roots is an isomorphism on polynomials of degree at
most `n-2`. Therefore the nonzero inertia of the Bézoutian is the inertia of

\[
 \operatorname{diag}
 \bigl(P'(r_k)R_c(r_k)\bigr)_{k=1}^{n-1}.
 \tag{L-15109.12}
\]

Combining this with (L-15109.9) proves

\[
 \boxed{
 T_p(c)\succeq0,
 \quad
 \ker T_p(c)=\mathbb Rp
 }
 \tag{L-15109.13}
\]

if and only if

\[
 \boxed{
 P'(r_k)R_c(r_k)<0
 \qquad(1\le k<n).}
 \tag{L-15109.14}
\]

This is a complete scalar test once the target roots are simple and real.

Conversely, a passing completion makes the quotient rank-one operator
selfadjoint in a positive metric, so `P` has real semisimple roots. Thus a target
with a certified nonreal root cannot pass any scalar completion.

## 4. One threshold per target root

At a target root, (L-15109.7) becomes

\[
 R_c(r_k)=R_0(r_k)-c\Omega(r_k).
 \tag{L-15109.15}
\]

Define

\[
 c_k=\frac{R_0(r_k)}{\Omega(r_k)},
 \qquad
 \sigma_k=P'(r_k)\Omega(r_k).
 \tag{L-15109.16}
\]

Since no target root equals a node, `Omega(r_k)!=0`. Condition (L-15109.14) is

\[
 \sigma_k(c_k-c)<0.
\]

Hence

\[
 \boxed{
 \begin{cases}
 c>c_k,&\sigma_k>0,\\
 c<c_k,&\sigma_k<0.
 \end{cases}}
 \tag{L-15109.17}
\]

The exact feasible interval is therefore

\[
 \boxed{
 \max_{\sigma_k>0}c_k
 <c<
 \min_{\sigma_k<0}c_k.}
 \tag{L-15109.18}
\]

Empty sides are interpreted as infinite. This root-threshold interval is the
Bézoutian form of the complete Finsler interval in `L-15107`.

## 5. Proof-producing finite audit

At one exact target level:

1. form the rational/algebraic polynomial `P`;
2. use a Sturm sequence to prove that it has `n-1` simple real roots and isolate
   each root in a disjoint rational interval;
3. enclose `R_0/Omega` and the sign of `P' Omega` on every root interval;
4. prove strict separation in (L-15109.18);
5. choose a rational interior `c`;
6. independently replay exact/directed complement LDL from `L-15107`.

If Sturm finds a nonreal pair, the finite target itself is unsuitable and no
completion search is necessary. If the roots are all real but the threshold
interval is empty, the target has a real-zero transform but the restricted
one-scalar arithmetic metric does not certify it.

## 6. Relation to arbitrary special completion

`L-15108` says that an arbitrary positive special metric exists exactly when
the target quotient is real-diagonalizable. In the simple-root case this means
exactly that `P` is real-rooted.

The present lemma adds the arithmetic restriction: the particular source
polynomial `R_0`, shifted only by the scalar family

\[
 R_0-c(sP+\Omega),
\]

must have the correct alternating Bézoutian signs at every target root.

Thus the finite audit separates three logically different outcomes:

1. `P` has a nonreal root: the target fails;
2. `P` is real-rooted but (L-15109.18) is empty: arbitrary completion exists,
   but the one-scalar Weil completion fails;
3. the interval is nonempty: exact rational completion and real-zero transfer.

## 7. Repeated-root boundary

When `P` has repeated real roots, simple evaluation no longer diagonalizes the
Bézoutian. A confluent Hermite matrix using derivatives at repeated roots is
required. A repeated but semisimple quotient eigenvalue may still admit a
positive special metric.

No repeated-root case is silently promoted by this lemma. Production may avoid
it by a certified small rational support perturbation, or handle it with a
separate confluent theorem.

## 8. Positive RH handoff

For the exact Hermite-radical target sequence, a cofinal proof can now be split
into two scalar-algebraic layers:

1. prove the finite interpolation polynomials `P_j` are simple and real-rooted;
2. prove the source thresholds in (L-15109.18) remain strictly separated.

Together with local-uniform convergence to `Xi`, this implies RH by `T-15104`.

The first layer alone is already a real-rooted-approximation proof of RH; the
second supplies the arithmetic Weil metric and an independent certificate.
Therefore the root criterion is primarily a diagnostic and proof-checking
interface, not a claim that the global difficulty has disappeared.

## Gap audit

1. The lemma uses the exact CCM sign and node orientation. Reversing `Omega` or
   the denominator in (L-15109.8) reverses every sign.
2. Target coefficients and node values must be exact or directed; ordinary
   polynomial roots are reconnaissance only.
3. The simple-root assumption is essential to the diagonal form
   (L-15109.12).
4. A nonempty midpoint interval is not a proof until all algebraic root
   enclosures and the final LDL replay are directed.
5. Cofinal real-rootedness and threshold separation are not proved here.
