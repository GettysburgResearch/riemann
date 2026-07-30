# T-15103 — Target-pinned diagonal completion and a finite PSD criterion for RH

Claim ID: `T-15103`  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-10`  
Created: 2026-07-30  
Dependencies: the finite CCM special-matrix real-zero theorem; elementary diagonal completion; `L-15101`; the Hardy-strip transform estimate of `T-14301`  
Scope: bypass natural-ground and resolvent selection by pinning the exact Xi target itself  
Related counterexample candidates: none

## 1. Exact finite diagonal completion

Use the finite special-matrix setting of `L-15105`. Thus `D` is diagonal,
`eta` is the boundary vector, `Gamma` is parity, and the Hermitian finite Weil
matrix `Q` satisfies

\[
 [D,Q]=|\beta\rangle\langle\eta|
       -|\eta\rangle\langle\beta|.
 \tag{T-15103.1}
\]

Let `p` be a real even vector such that

\[
 p_i\ne0\quad\hbox{for every coordinate},
 \qquad
 \delta:=\langle\eta,p\rangle\ne0.
 \tag{T-15103.2}
\]

Rescale `p` so that

\[
 \langle\eta,p\rangle=1.
 \tag{T-15103.3}
\]

For any real scalar `c`, define the real diagonal entries

\[
 \boxed{
 r_i(c)=\frac{c\eta_i-(Qp)_i}{p_i}}
 \tag{T-15103.4}
\]

and put

\[
 \boxed{
 T_p(c)=Q+\operatorname{diag}(r_i(c))
       -c|\eta\rangle\langle\eta|.}
 \tag{T-15103.5}
\]

Then:

1. `T_p(c)p=0` exactly;
2. `T_p(c)` commutes with parity;
3. it remains a CCM special matrix:

   \[
   \boxed{
   [D,T_p(c)]
   =|\beta-cD\eta\rangle\langle\eta|
    -|\eta\rangle\langle\beta-cD\eta|.}
   \tag{T-15103.6}
   \]

Therefore, if for one `c`

\[
 \boxed{
 T_p(c)\succeq0,
 \qquad
 \ker T_p(c)=\mathbb Rp,}
 \tag{T-15103.7}
\]

then the imported CCM theorem proves that the Fourier--Mellin transform of `p`
is entire and all its zeros are real.

### Proof

Equation (T-15103.4) gives componentwise

\[
 Qp+\operatorname{diag}(r_i(c))p=c\eta.
\]

Using (T-15103.3), subtracting `c eta eta^T p=c eta` proves `T_p(c)p=0`.
Parity of `Q,p,eta` gives `r_{-i}=r_i`. Diagonal matrices commute with `D`, and
the rank-one commutator is the one computed in `L-15105`, proving
(T-15103.6). The final conclusion is exactly the imported finite special-matrix
theorem. QED.

## 2. Graph-Laplacian sum-of-squares certificate

For `i<j`, define

\[
 \boxed{
 w_{ij}(c)
 =-\bigl(Q_{ij}-c\eta_i\eta_j\bigr)p_ip_j.}
 \tag{T-15103.8}
\]

Because `T_p(c)p=0`, one has the exact identity

\[
 \boxed{
 x^TT_p(c)x
 =\sum_{i<j}w_{ij}(c)
   \left(\frac{x_i}{p_i}-\frac{x_j}{p_j}\right)^2.}
 \tag{T-15103.9}
\]

Consequently:

- if every `w_ij(c)>=0`, then `T_p(c)>=0`;
- if the graph with vertices `i` and edges `w_ij(c)>0` is connected, then
  `ker T_p(c)=span{p}`.

This is an exact rational/interval-checkable SOS proof. It avoids an eigensolver
and does not require interval LDL of a nearly singular full matrix.

### Proof of the identity

Expanding the right side, the mixed term at `(i,j)` is

\[
 2\bigl(Q_{ij}-c\eta_i\eta_j\bigr)x_ix_j,
\]

which is the off-diagonal contribution of `T_p(c)`. The coefficient of `x_i^2`
is

\[
 -\frac1{p_i}\sum_{j\ne i}
  (Q_{ij}-c\eta_i\eta_j)p_j.
\]

The kernel equation `T_p(c)p=0` says that this is exactly the diagonal entry of
`T_p(c)`. This proves (T-15103.9). The kernel statement is the standard connected
weighted-graph argument. QED.

## 3. One-scalar threshold separation

Suppose, as in the CCM coordinate system, every `eta_i` is nonzero. Set

\[
 q_{ij}=\frac{Q_{ij}}{\eta_i\eta_j}.
 \tag{T-15103.10}
\]

The edge condition `w_ij(c)>=0` is equivalent to

\[
 \begin{cases}
 c\ge q_{ij},&p_ip_j>0,\\
 c\le q_{ij},&p_ip_j<0.
 \end{cases}
 \tag{T-15103.11}
\]

Thus a sufficient scalar interval is

\[
 \boxed{
 \max_{p_ip_j>0}q_{ij}
 \le c\le
 \min_{p_ip_j<0}q_{ij}.}
 \tag{T-15103.12}
\]

Empty sides are interpreted as infinite endpoints. Strict inequalities on a
connected edge set give the one-dimensional-kernel gate.

The entire finite target-pinning problem can therefore collapse to comparing
off-diagonal Weil entries against the sign partition of the exact target
coefficients.

This graph condition is sufficient, not necessary. When the interval is empty,
`T_p(c)` may still be PSD for a value of `c`; exact LDL on the complement of `p`
remains the complete finite test.

## 4. Exact Xi-target sequence

Let `K(t)=k(e^t)` be the exact even logarithmic target of `L-15101`, whose
Fourier transform is `Xi`. For a support half-length `a>0`, let

\[
 P_{a,N}K
\]

be its orthogonal projection to the centered Fourier space of frequencies
`|n|<=N`, and transfer its coefficient vector to CCM coordinates through the
exact sign adapter `L-14304`. Denote this real even vector by `p_(a,N)`.

Choose supports and cutoffs

\[
 a_j\to\infty,
 \qquad
 N_j\to\infty
 \tag{T-15103.13}
\]

so that:

1. every coefficient of `p_j=p_(a_j,N_j)` is nonzero;
2. its boundary value `delta_j=<eta_j,p_j>` is nonzero;
3. after restoring the original scalar normalization, the transforms satisfy

   \[
   \widehat{p_j}\longrightarrow\Xi
   \tag{T-15103.14}
   \]

   locally uniformly in `|Im z|<1/2`.

The third item follows from the super-Gaussian support tail of `L-15101`, plus a
cofinal Hardy-weighted Fourier projection tail. Supports hitting a coefficient
or boundary zero can be avoided by a small rational perturbation once
nonvanishing is certified; no universal nonvanishing assertion is made here.

## 5. Finite diagonal-completion criterion for RH

Assume that for every `j` there exists a real `c_j` such that

\[
 T_{p_j}(c_j)\succeq0,
 \qquad
 \ker T_{p_j}(c_j)=\mathbb Rp_j.
 \tag{T-15103.15}
\]

Then every `hat p_j` has only real zeros by Part 1. By (T-15103.14) and Hurwitz's
theorem, `Xi` has no nonreal zero in its open critical strip. Therefore RH is
true.

Equivalently, it is enough to prove the graph-SOS gates

\[
 w_{rs}^{(j)}(c_j)\ge0
 \tag{T-15103.16}
\]

with connected positive-edge graph at a cofinal sequence of exact finite levels.

## 6. Why this changes the positive program

The previous finite-diagonal route required the exact Xi target to become the
natural simple-even ground eigenvector of `Q`. `L-15106` shows why that may be
structurally unrealistic: many localized global-radical directions cluster near
zero.

The present theorem instead:

1. freezes the exact target first;
2. changes only the diagonal of the finite special matrix and one boundary
   rank-one coefficient;
3. preserves the commutator identity responsible for real zeros;
4. reduces the proof to a finite PSD completion;
5. makes convergence to Xi automatic by construction.

No spectral-gap or eigenvector-selection theorem remains.

## 7. Immediate proof-producing program

For exact rational support parameters and finite `N`:

1. produce directed intervals for the finite Weil matrix `Q`;
2. produce directed Fourier coefficients of `K` and the boundary scalar;
3. normalize `p` by the boundary scalar with outward intervals;
4. compute every threshold `q_ij` and the interval in (T-15103.12);
5. if nonempty, choose a rational interior `c` and certify every graph weight;
6. otherwise solve the one-parameter complement-LDL feasibility problem;
7. repeat over increasing `(a,N)` and inspect the sign-partition geometry.

A single failing finite level does not refute the route; the theorem needs a
cofinal passing sequence. A stable empty threshold interval, however, is a
valuable structural obstruction and should be retained.

## Gap audit

- The imported CCM theorem must genuinely cover every PSD special matrix with a
  one-dimensional even kernel, not only the particular natural-ground shift.
  The source lemma appears to have this scope, but this normalization gate must
  be independently reconstructed before promotion.
- Diagonal completion changes the Hilbert metric used in the associated finite
  spectral triple. This is allowed by the finite special-matrix theorem but is
  not the original Weil ground-state model.
- The diagonal entries can become enormous when the boundary value or a target
  coefficient is tiny. Exact interval arithmetic, not condition-number rhetoric,
  decides the finite gate.
- The graph threshold condition may fail because target coefficients change
  sign. Failure of the sufficient condition is not failure of PSD completion.
- No real Weil matrix has yet been replayed through this completion. Therefore
  this theorem is a new exact route, not a completed RH proof.
