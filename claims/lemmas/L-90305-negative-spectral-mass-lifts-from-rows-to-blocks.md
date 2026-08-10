# L-90305 — Negative spectral mass lifts from rows to complete finite blocks

Claim ID: `L-90305`  
Title: The trace of the negative part is convex, decreases under contraction, and admits an exact Toeplitz-compression bound; consequently the zero-bare Q4 row defect of `L-90304` remains lower order after complete balanced-row and finite-filter block assembly  
Status: **PROPOSED COMPLETE EXACT OPERATOR LEMMA + COFINAL Q4 BLOCK APPLICATION — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Dependencies: `L-90304`; finite-dimensional spectral theorem; exact physical/carry block identifications on PRs #341 and #346  
Scope: negative-mass bookkeeping through positive integration, direct sums, contractions, and Toeplitz compression; it does not by itself establish the final delayed-state orientation or RH

## 1. Negative spectral mass and its variational formula

For a finite-dimensional Hermitian matrix `H`, write

\[
H=H_+-H_-,\qquad H_\pm\succeq0,\qquad H_+H_-=0,
\]

and put

\[
\boxed{\delta(H)=\operatorname{tr}H_-.}
\tag{L-90305.1}
\]

Then

\[
\boxed{
\delta(H)
=\max_{0\preceq P\preceq I}-\operatorname{tr}(PH).
}
\tag{L-90305.2}
\]

Indeed, in an eigenbasis of `H`, for every positive contraction `P`,

\[
-\operatorname{tr}(PH)
\le \sum_{\lambda_i(H)<0}(-\lambda_i(H)),
\]

and equality is attained by the spectral projection onto the negative eigenspace.

Formula (L-90305.2) is the load-bearing interface.  It is the trace-mass analogue of the inertia monotonicity used in Claude's finite-compression argument, and it does not require the matrices being combined to commute.

## 2. Convexity and positive integration

Let `H_1,...,H_m` be Hermitian and let `a_j>=0`.  From (L-90305.2),

\[
\begin{aligned}
\delta\!\left(\sum_j a_jH_j\right)
&=\max_{0\preceq P\preceq I}
  \sum_j a_j[-\operatorname{tr}(PH_j)]\\
&\le\sum_j a_j
  \max_{0\preceq P\preceq I}[-\operatorname{tr}(PH_j)].
\end{aligned}
\]

Therefore

\[
\boxed{
\delta\!\left(\sum_j a_jH_j\right)
\le\sum_j a_j\delta(H_j).
}
\tag{L-90305.3}
\]

The same proof, by approximation with positive simple functions, gives the Bochner-integral form: if `omega -> H(omega)` is an integrable Hermitian matrix field on a positive measure space,

\[
\boxed{
\delta\!\left(\int H(\omega)\,d\mu(\omega)\right)
\le\int\delta(H(\omega))\,d\mu(\omega).
}
\tag{L-90305.4}
\]

No termwise diagonalisation and no sign condition on the off-diagonal entries is used.

## 3. Contractions cannot amplify negative mass beyond their squared norm

Let `A` be a linear map and suppose

\[
AA^*\preceq qI,
\qquad q\ge0.
\tag{L-90305.5}
\]

Then

\[
\boxed{
\delta(A^*HA)\le q\,\delta(H).
}
\tag{L-90305.6}
\]

### Proof

For `0<=P<=I`,

\[
0\preceq APA^*\preceq AA^*\preceq qI.
\]

Hence, by (L-90305.2),

\[
\begin{aligned}
-\operatorname{tr}(PA^*HA)
&=-\operatorname{tr}(APA^*H)\\
&\le q\,\delta(H).
\end{aligned}
\]

Taking the maximum over `P` proves (L-90305.6).

Thus neither a source synthesis nor a Hilbert-space compression can create a large negative trace mass from a small one.  This is stronger than an inertia-count statement and is exactly the quantity consumed by `L-90301`.

## 4. Matrix-valued Toeplitz compression retains every filter cross term

Let

\[
K:\mathbb T\longrightarrow\operatorname{Herm}_r
\]

be integrable.  Let `M_K` be multiplication by `K` on

\[
L^2(\mathbb T;\mathbb C^r),
\]

and let `P_N` be the orthogonal projection onto any `N` consecutive Fourier modes.  Define the finite block Toeplitz matrix

\[
T_N(K)=P_NM_KP_N.
\tag{L-90305.7}
\]

Then

\[
\boxed{
\delta(T_N(K))
\le
N\int_{\mathbb T}\delta(K(e^{i\theta}))\,
       \frac{d\theta}{2\pi}.
}
\tag{L-90305.8}
\]

### Proof

Pointwise,

\[
K=K_+-K_-.
\]

Consequently

\[
T_N(K)=T_N(K_+)-T_N(K_-),
\qquad T_N(K_\pm)\succeq0.
\]

For every positive contraction `P` on the finite Fourier block,

\[
-\operatorname{tr}(PT_N(K))
\le\operatorname{tr}(PT_N(K_-))
\le\operatorname{tr}T_N(K_-).
\]

The diagonal Fourier coefficient gives

\[
\operatorname{tr}T_N(K_-)
=N\int_{\mathbb T}\operatorname{tr}K_-(e^{i\theta})
  \frac{d\theta}{2\pi}.
\]

Now use (L-90305.2).

Equation (L-90305.8) is important for the present repository: it does **not** discard convolution/filter cross terms.  They remain inside the exact matrix symbol before the negative part is taken.  The estimate is therefore compatible with the finite-delay Toeplitz consequences of PR #346 and with the independent-frequency physical blocks of PR #341.

## 5. Direct-integral curvature matrices

Let

\[
V(\tau,\omega)\in\mathbb C^r
\]

be twice differentiable in `tau` and square-integrable in `omega`.  Regard

\[
\mathcal V(\tau)=V(\tau,\cdot)
\]

as a vector in the Hilbert direct integral.  Its channel curvature matrix is

\[
\mathbf K_{\mathcal V}
=\langle\mathcal V',\mathcal V'\rangle
 -\frac12\left(
  \langle\mathcal V,\mathcal V''\rangle
 +\langle\mathcal V'',\mathcal V\rangle
 \right),
\tag{L-90305.9}
\]

where the brackets are taken entrywise in the channel indices.  Fubini gives exactly

\[
\boxed{
\mathbf K_{\mathcal V}
=\int K_{V(\cdot,\omega)}\,d\mu(\omega).
}
\tag{L-90305.10}
\]

Therefore

\[
\boxed{
\delta(\mathbf K_{\mathcal V})
\le
\int\delta(K_{V(\cdot,\omega)})\,d\mu(\omega).
}
\tag{L-90305.11}
\]

This is the exact row-to-physical-block lift needed after the prefix/carry identity: differentiation, source convolution, carry-position integration, and channel curvature all commute before the negative mass is estimated.

## 6. Apply to the zero-bare Q4 balanced row bank

Fix `0<eta<1/2`.  For a sufficiently large integer parent `n`, let

\[
J_{n,\eta}
=\{j\in\mathbb Z:\eta n\le j\le(1-\eta)n\}.
\]

For each `j in J_(n,eta)`, let `K_(n,j)` be the exact zero-bare relative Q4 curvature matrix of `L-90304`.  That theorem gives uniformly

\[
\delta(K_{n,j})
\le C_\eta\frac{n}{\log n}.
\tag{L-90305.12}
\]

Define the normalized finite carry-position block

\[
\overline K_{n,\eta}
=\frac1n\sum_{j\in J_{n,\eta}}K_{n,j}.
\tag{L-90305.13}
\]

Then (L-90305.3) yields

\[
\boxed{
\delta(\overline K_{n,\eta})
\le C'_\eta\frac{n}{\log n}.
}
\tag{L-90305.14}
\]

After the square-root critical normalization by the parent size,

\[
\widehat K_{n,\eta}=\frac1n\overline K_{n,\eta},
\]

we obtain

\[
\boxed{
\delta(\widehat K_{n,\eta})
\le\frac{C'_\eta}{\log n}.
}
\tag{L-90305.15}
\]

The same conclusion holds for any positive quadrature or carry-position measure of total mass `O(1)`, and for every finite Toeplitz/filter compression of that block by Sections 3--4.

Thus the passage

```text
pointwise balanced carry rows
  -> complete carry-position Gram
  -> independent-frequency physical block
  -> finite-delay filter bank
```

cannot turn the `O(n/log n)` row defect of `L-90304` into an RH-scale obstruction.  In the critically normalized block it remains `O(1/log n)`.

## 7. Exact remaining boundary

This lemma closes the spectral-accumulation concern in QIDR:

```text
rowwise negative mass lower order
  DOES remain lower order after positive block integration;

filter cross terms
  ARE retained by the Toeplitz compression inequality;

finite Hilbert compression
  DOES NOT amplify the bad trace mass.
```

What it does not supply is the final signed identity placing the corrected Q2/Q4 principal state, the zero-bare relative source, the terminal all-pass return, finite collars, and every delayed gauge in one common block metric with coefficient one.  That is now an exact source/state assembly problem, not an uncontrolled accumulation of rowwise indefinite directions.

## 8. Proof boundary

Closed exactly here:

1. the variational formula for negative trace mass;
2. convexity under positive sums and integration;
3. contraction monotonicity;
4. the matrix-valued finite Toeplitz compression bound;
5. direct-integral curvature assembly;
6. inheritance of the `O(n/log n)` Q4 row defect by complete balanced blocks;
7. critically normalized block defect `O(1/log n)`.

Still open:

1. one source-complete coefficient-one delayed-state identity in a common Hilbert metric;
2. iteration of that identity into the global pole-energy recurrence;
3. RH.
