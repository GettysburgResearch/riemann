# L-15108 — Special positive completion is equivalent to a real-diagonalizable quotient

Claim ID: `L-15108`  
Status: `PROPOSED`  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: finite-dimensional real spectral theorem; the determinant identity used in Connes--van Suijlekom Lemma 5.9  
Scope: arbitrary finite special-matrix completion of one prescribed vector  
Related counterexample candidates: none

## 1. Setup

Let

\[
 D=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)
\]

have distinct real eigenvalues, put

\[
 \eta=(1,\ldots,1)^{\mathsf T},
\]

and let `p` be a nonzero real vector normalized by

\[
 \eta^{\mathsf T}p=1.
\]

Define the rank-one perturbation

\[
 \boxed{
 D_p=D-|Dp\rangle\langle\eta|.}
 \tag{L-15108.1}
\]

Then

\[
 D_pp=0,
\]

so `D_p` induces a well-defined real operator

\[
 \overline D_p:\mathbb R^n/\mathbb Rp
 \longrightarrow
 \mathbb R^n/\mathbb Rp.
 \tag{L-15108.2}
\]

The associated interpolation polynomial is

\[
 \boxed{
 P_p(s)=
 \sum_{i=1}^n p_i
 \prod_{j\ne i}(\lambda_j-s).}
 \tag{L-15108.3}
\]

The matrix determinant lemma gives

\[
 \boxed{
 \det(D_p-sI)=-s\,P_p(s)}
 \tag{L-15108.4}
\]

up to the fixed harmless orientation sign determined by the order of the
`lambda_i`. Consequently `P_p` is the characteristic polynomial of the quotient
operator, up to that nonzero constant factor.

## 2. Exact converse theorem

The following are equivalent.

1. There exists a real symmetric positive semidefinite matrix `Q` such that

   \[
   \ker Q=\mathbb Rp,
   \tag{L-15108.5}
   \]

   and `Q` is special for `D`, meaning that for some real vector `beta`,

   \[
   \boxed{
   DQ-QD=|\beta\rangle\langle\eta|
          -|\eta\rangle\langle\beta|.}
   \tag{L-15108.6}
   \]

2. The quotient operator `\overline D_p` is diagonalizable over `R` and has real
   spectrum.

When these conditions hold, every zero of `P_p` is real. Conversely, if `P_p`
has simple real roots, then condition 2 holds and therefore a positive special
completion exists.

Thus an **arbitrary** special positive completion is not a free route around the
finite real-zero problem: it is exactly a metric realization of the
real-diagonalizable quotient.

## 3. Proof: positive completion implies real quotient spectrum

Assume condition 1. The semidefinite form

\[
 \langle x,y\rangle_Q=x^{\mathsf T}Qy
\]

descends to a positive-definite inner product on the quotient by `Rp`.

Since `Qp=0`, apply (L-15108.6) to `p`. The standard special-matrix calculation
gives

\[
 QDp=-\beta
\]

after the normalization `eta^T p=1` and the parity-orthogonality convention of
the finite theorem. More invariantly, direct expansion shows

\[
 QD_p=D_p^{\mathsf T}Q.
 \tag{L-15108.7}
\]

Therefore `\overline D_p` is selfadjoint in the positive quotient inner product.
The real spectral theorem makes it diagonalizable with real spectrum. Equation
(L-15108.4) then proves that `P_p` is real-rooted.

This is the finite mechanism used in Connes--van Suijlekom Proposition 5.10.

## 4. Proof: real quotient spectrum constructs a special completion

Assume condition 2. Choose a positive-definite real inner product `g` on the
quotient in which `\overline D_p` is selfadjoint: in a real eigenbasis, choose
any positive diagonal weights.

Pull `g` back to `R^n` through the quotient map. The resulting matrix `Q` is real
symmetric, positive semidefinite, and has kernel exactly `Rp`. By construction,

\[
 QD_p=D_p^{\mathsf T}Q.
 \tag{L-15108.8}
\]

Substitute `D_p=D-Dp\,\eta^T` into (L-15108.8). With

\[
 g_0=QDp,
\]

one obtains

\[
 DQ-QD
 =
 \eta g_0^{\mathsf T}-g_0\eta^{\mathsf T}.
\]

Taking

\[
 \beta=-g_0
\]

gives exactly (L-15108.6). Since `D` has simple spectrum, its off-diagonal
entries satisfy

\[
 Q_{ij}=
 \frac{\beta_i-\beta_j}{\lambda_i-\lambda_j},
 \qquad i\ne j,
 \tag{L-15108.9}
\]

while the diagonal entries are unrestricted. Thus `Q` is precisely of the
finite special form.

## 5. Parity refinement

Assume the nodes are symmetric,

\[
 \lambda_{-i}=-\lambda_i,
\]

and inversion `Gamma` satisfies

\[
 \Gamma D=-D\Gamma,
 \qquad
 \Gamma p=p,
 \qquad
 \Gamma\eta=\eta.
\]

Then `D_p` anticommutes with `Gamma`. If the quotient is real-diagonalizable,
choose equal positive metric weights on the `lambda` and `-lambda` eigenspaces
and a `Gamma`-invariant positive metric on the zero eigenspace modulo `p`.
The constructed `Q` then commutes with `Gamma`, so the completion meets the even
finite theorem.

## 6. Relation to the scalar pencil of L-15107

`L-15108` allows every special vector `beta` and every diagonal. Its existence is
equivalent to the target interpolation polynomial already having the required
real-zero property.

By contrast, `L-15107` starts from the arithmetic Weil matrix and permits only

\[
 \beta\longmapsto\beta-cD\eta
\]

together with the forced target-pinning diagonal. This one-scalar subfamily is
strictly smaller. Its Finsler criterion is therefore a noncircular sufficient
test that can, in principle, be proved from arithmetic structure without first
knowing the target polynomial is real-rooted.

This distinction is essential:

- **arbitrary special completion:** exact reformulation of finite real-rootedness;
- **one-scalar Weil completion:** stronger structured condition, exactly decided
  by `L-15107`;
- **edgewise nonnegative graph weights:** still stronger, only a convenient
  sufficient certificate.

## 7. Direct finite alternative

For an exact rational target `p`, equation (L-15108.3) has rational coefficients.
A Sturm sequence can certify directly that all its roots are real. This is a
valid finite proof route and can serve as an independent check of any completed
matrix.

It does not solve the cofinal problem: one still needs a sequence of such exact
real-rooted targets converging locally uniformly to `Xi`. But it removes the
special-matrix producer from the finite trust boundary.

## 8. Gap audit

1. Real roots with multiplicity do not by themselves guarantee that the quotient
   operator is diagonalizable. The clean converse from polynomial roots uses
   simple roots, or else a separate semisimplicity certificate.
2. The existence theorem constructs some special matrix, not necessarily the
   arithmetic Weil matrix or the one-scalar completion of `L-15107`.
3. Parity must be built into the quotient metric; it is not automatic from an
   arbitrary eigenbasis.
4. Equation (L-15108.4) must use the exact node and sign convention of the finite
   theorem.
5. A finite real-rooted interpolation polynomial is not RH. Cofinal
   locally-uniform convergence to `Xi` remains mandatory.
6. This lemma does not claim that the Hermite target quotients are
   real-diagonalizable.

## 9. Suggested next attack

Use a three-way finite audit at each small Hermite level:

1. exact Sturm root count for `P_p`;
2. exact `L-15107` scalar-completion search;
3. if the polynomial is real-rooted but the scalar pencil fails, construct an
   arbitrary special metric from the quotient eigenbasis.

This separates failure of the target itself from failure of the restricted
arithmetic completion ansatz.
