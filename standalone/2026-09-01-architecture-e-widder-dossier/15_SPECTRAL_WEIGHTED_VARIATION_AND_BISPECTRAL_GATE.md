# Spectral weighted theta–Darboux theorem and the lattice-Casimir gate

Status: **PROPOSED EXACT THEOREMS; INDEPENDENT REVIEW REQUIRED; THE
COEFFICIENT-RESOLVED TDA SIGN, THE ALL-ORDER E–WIDDER INEQUALITY, AND RH
REMAIN UNPROVED.**

The theta–Darboux/Andreief packet reduces every positive-index Toeplitz minor
of the invariant xi coefficients to

\[
 2^r\int_{\tau_1<\cdots<\tau_r}
 {\cal T}_{H}(\boldsymbol\tau)
 {\cal B}_{N}(\boldsymbol\tau)\,d\boldsymbol\tau,
\]

where

\[
 {\cal T}_{H}(\boldsymbol\tau)
 =\det[(L^{h_p}\Phi)(\tau_\ell)]_{p,\ell=1}^r,
 \qquad
 {\cal B}_{N}(\boldsymbol\tau)
 =\det[b_{n_p}(\tau_\ell)]_{p,\ell=1}^r,
\]

and

\[
 L=D_\tau^2-\frac14,\qquad
 b_n(\tau)=[u^n]\cosh\!\left(\tau\sqrt{u+\frac14}\right).
\]

The original coefficient-resolved sign remains RH-bearing.  This note proves
a substantial weighted variation theorem that holds at every rank: the same
theta–Darboux current pairs strictly positively with every *spectral Slater
determinant*.  It then identifies, exactly, why extracting one coefficient
Slater determinant from that positive cone is the remaining difficulty.

The note also gives a bispectral identity for each literal theta-lattice atom.
It converts the invariant lowering operator into the self-dual radial Mellin
Casimir

\[
 {\cal A}_m=\partial_m(m^2\partial_m).
\]

This isolates the unresolved arithmetic as a lattice-versus-continuum
exterior-current problem rather than a generic source-positivity problem.

## 1. Spectral eigenfunction

Put

\[
 \boxed{
 B(u,\tau)=
 \cosh\!\left(\tau\sqrt{u+\frac14}\right)
 =\sum_{n\ge0}b_n(\tau)u^n.
 }
 \tag{1.1}
\]

Direct differentiation gives

\[
 \boxed{L_\tau B(u,\tau)=uB(u,\tau).}
 \tag{1.2}
\]

Retain the actual full-line normalization

\[
 \mathfrak X(u)
 =\xi_{\rm R}\!\left(\frac12+\sqrt{u+\frac14}\right)
 =2\int_0^\infty\Phi(\tau)B(u,\tau)\,d\tau.
 \tag{1.3}
\]

The theta tail is superexponential.  Both `Phi` and `B` are even in `tau`.
Consequently repeated integration by parts on the half-line has no endpoint
term and, for every integer `h>=0` and every `u>0`,

\[
 \boxed{
 2\int_0^\infty
 (L^h\Phi)(\tau)B(u,\tau)\,d\tau
 =
 u^h\mathfrak X(u).
 }
 \tag{1.4}
\]

No zero information is used in (1.4).

## 2. Strict total positivity of the spectral kernel

The preceding packet proves that

\[
 (\tau,n)\longmapsto b_n(\tau)
\]

is strictly totally positive on
`(0,infinity) x Z_(>=0)`.  The monomial kernel

\[
 (u,n)\longmapsto u^n
\]

is strictly totally positive on the same ordered discrete interface.
Equation (1.1) is their discrete composition.  Cauchy–Binet therefore gives:

### Theorem 2.1

The kernel

\[
 \boxed{(u,\tau)\longmapsto B(u,\tau)}
 \tag{2.1}
\]

is strictly totally positive of infinite order on
`(0,infinity) x (0,infinity)`.

More explicitly, whenever

\[
 0<u_1<\cdots<u_r,
 \qquad
 0<\tau_1<\cdots<\tau_r,
\]

one has

\[
 \boxed{
 {\cal S}_{\mathbf u}(\boldsymbol\tau)
 :=
 \det[B(u_q,\tau_\ell)]_{q,\ell=1}^r>0.
 }
 \tag{2.2}
\]

Strictness follows already from the intermediate index set
`(0,1,...,r-1)`.

## 3. Spectral weighted theta–Darboux variation theorem

Let

\[
 H=(h_1<\cdots<h_r)
\]

be any increasing tuple of nonnegative integers and define

\[
 {\cal T}_H(\boldsymbol\tau)
 =
 \det[(L^{h_p}\Phi)(\tau_\ell)]_{p,\ell=1}^r.
 \tag{3.1}
\]

### Theorem 3.1 — spectral TDA

For every increasing positive spectral packet
`0<u_1<...<u_r`,

\[
 \boxed{
 \begin{aligned}
 &2^r\int_{0<\tau_1<\cdots<\tau_r}
 {\cal T}_H(\boldsymbol\tau)
 {\cal S}_{\mathbf u}(\boldsymbol\tau)
 \,d\boldsymbol\tau\\
 &\qquad\qquad=
 \left(\prod_{q=1}^r\mathfrak X(u_q)\right)
 \det[u_q^{h_p}]_{p,q=1}^r
 >0.
 \end{aligned}
 }
 \tag{3.2}
\]

#### Proof

Andreief's continuous Cauchy–Binet identity and (1.4) give

\[
 \begin{aligned}
 &2^r\int_{\tau_1<\cdots<\tau_r}
 \det[(L^{h_p}\Phi)(\tau_\ell)]
 \det[B(u_q,\tau_\ell)]\,d\boldsymbol\tau\\
 &\qquad=
 \det\left[
 2\int_0^\infty
 (L^{h_p}\Phi)(\tau)B(u_q,\tau)\,d\tau
 \right]_{p,q}\\
 &\qquad=
 \det[u_q^{h_p}\mathfrak X(u_q)]_{p,q}.
 \end{aligned}
\]

Factor `mathfrak X(u_q)` from column `q`.  The actual positive theta
representation gives `mathfrak X(u_q)>0`.  The remaining generalized
Vandermonde determinant is strictly positive for increasing positive nodes
and increasing integer exponents.  This proves (3.2). `square`

### Corollary 3.2 — positive dual cone

Let `nu` be any nonzero positive measure on the ordered positive spectral
chamber for which the following integrals converge.  Then

\[
 G_\nu(\boldsymbol\tau)
 =
 \int {\cal S}_{\mathbf u}(\boldsymbol\tau)\,d\nu(\mathbf u)
\]

is pointwise positive and

\[
 \boxed{
 \int_{\tau_1<\cdots<\tau_r}
 {\cal T}_H(\boldsymbol\tau)
 G_\nu(\boldsymbol\tau)\,d\boldsymbol\tau>0.
 }
 \tag{3.3}
\]

Thus the actual theta–Darboux current belongs to the strict dual cone of the
entire spectral-Slater cone at every exterior rank.

This is a genuine weighted variation theorem.  It does not assert the false,
unnecessarily strong statement that `T_H` is pointwise nonnegative.

## 4. Exact Schur-generating identity

Expanding the spectral determinant by discrete Cauchy–Binet gives

\[
 \boxed{
 {\cal S}_{\mathbf u}(\boldsymbol\tau)
 =
 \sum_{0\le n_1<\cdots<n_r}
 \det[u_q^{n_p}]_{q,p=1}^r
 {\cal B}_N(\boldsymbol\tau).
 }
 \tag{4.1}
\]

Pairing (4.1) with the source current and using Theorem 3.1 yields

\[
 \boxed{
 \begin{aligned}
 &\left(\prod_{q=1}^r\mathfrak X(u_q)\right)
 \det[u_q^{h_p}]_{p,q=1}^r\\
 &\quad=
 \sum_N
 \det[c_{n_q-h_p}]_{p,q=1}^r
 \det[u_q^{n_p}]_{q,p=1}^r.
 \end{aligned}
 }
 \tag{4.2}
\]

Here `c_j=0` for `j<0`.  Formula (4.2) is the complete Schur/alternant
generating identity for the weighted theta–Darboux integrals.  In particular,

\[
 \boxed{
 2^r\int_{\tau_1<\cdots<\tau_r}
 {\cal T}_H(\boldsymbol\tau)
 {\cal B}_N(\boldsymbol\tau)\,d\boldsymbol\tau
 =
 \det[c_{n_q-h_p}]_{p,q=1}^r.
 }
 \tag{4.3}
\]

The desired coefficient-resolved TDA theorem is precisely coefficientwise
nonnegativity in the alternant expansion (4.2).

## 5. Why spectral positivity does not finish coefficient extraction

Theorem 3.1 proves positivity of the whole left side of (4.2) on every
positive spectral chamber.  Positivity of an antisymmetric function after
division by its generalized Vandermonde does not, in general, force all of
its Schur coefficients to be nonnegative.

There is an exact two-variable firewall.  Take

\[
 X(u)=1+u+2u^2>0\qquad(u>0)
\]

and `H=(0,1)`.  Then for `0<u_1<u_2`,

\[
 \det\begin{pmatrix}
 X(u_1)&X(u_2)\\
 u_1X(u_1)&u_2X(u_2)
 \end{pmatrix}
 =
 X(u_1)X(u_2)(u_2-u_1)>0.
 \tag{5.1}
\]

But the alternant coefficient indexed by `N=(1,2)` is

\[
 \det\begin{pmatrix}c_1&c_2\\c_0&c_1\end{pmatrix}
 =1-2=-1.
 \tag{5.2}
\]

Therefore no generic positive coefficient-extraction functional from the
spectral-Slater cone can prove (4.3).  The remaining step must use the
specific theta lattice, the modular relation, or an additional
representation-theoretic positivity structure.  This prevents the spectral
theorem from being silently promoted to RH.

## 6. Literal theta atoms and the Mellin Casimir

For a continuous positive lattice variable `m`, define

\[
 g(m,\tau)
 =
 \exp\!\left(\frac\tau2-\pi m^2e^{2\tau}\right)
 \tag{6.1}
\]

and put

\[
 M=m\partial_m,
 \qquad
 {\cal A}=M(M+1)=\partial_m(m^2\partial_m).
 \tag{6.2}
\]

Since

\[
 \partial_\tau g=(M+\tfrac12)g,
\]

one obtains the exact bispectral identity

\[
 \boxed{
 L_\tau g
 =
 (D_\tau^2-\tfrac14)g
 =
 M(M+1)g
 =
 {\cal A}_m g.
 }
 \tag{6.3}
\]

The full-line normalization of the actual Riemann kernel is

\[
 \Phi(\tau)
 =
 \sum_{m\ge1}L_\tau g(m,\tau).
\]

Consequently, for every `h>=0`,

\[
 \boxed{
 L_\tau^h\Phi(\tau)
 =
 \sum_{m\ge1}{\cal A}_m^{h+1}g(m,\tau).
 }
 \tag{6.4}
\]

The operator `A` is a divergence-form radial Sturm operator.  For every
function in the displayed Gaussian ladder,

\[
 \int_0^\infty {\cal A}F(m)\,dm
 =
 [m^2F'(m)]_0^\infty=0.
 \tag{6.5}
\]

Thus (6.4) may equally be written as the exact lattice defect

\[
 \boxed{
 L^h\Phi(\tau)
 =
 \left(\sum_{m\ge1}-\int_0^\infty dm\right)
 {\cal A}^{h+1}g(m,\tau).
 }
 \tag{6.6}
\]

The continuum term is literally zero, but retaining it identifies the
arithmetic origin of the source current.

Under the Fourier transform in `m`,

\[
 M\longmapsto -M-1.
\]

Hence

\[
 M(M+1)\longmapsto(-M-1)(-M)=M(M+1).
 \tag{6.7}
\]

The Casimir is Fourier self-dual.  This is the operator-level reason the
literal lattice current is compatible with theta inversion and the evenness
of `Phi`.

## 7. The sharpened remaining theorem

The original coefficient TDA gate can now be stated as a source-specific
Schur-extraction theorem.

### Theta lattice Schur-extraction gate `TLSE`

For every increasing exponent packet `H` and every increasing coefficient
packet `N` in the nonnegative Toeplitz range, prove that the coefficient of
the alternant `det[u_q^(n_p)]` in

\[
 \left(\prod_q\mathfrak X(u_q)\right)\det[u_q^{h_p}]
\]

is nonnegative, using the lattice-Casimir representation (6.6).

Equivalently, prove

\[
 \boxed{
 \int_{\tau_1<\cdots<\tau_r}
 {\cal T}_H(\boldsymbol\tau)
 {\cal B}_N(\boldsymbol\tau)\,d\boldsymbol\tau\ge0.
 }
 \tag{TLSE}
\]

Theorem 3.1 pays this inequality for every positive mixture of complete
spectral Slaters.  Formula (5.2) proves that passage to an individual Schur
coefficient is not a generic consequence of that spectral positivity.
Equation (6.6) identifies the additional structure available only for the
Riemann source: a Fourier-self-dual radial-Casimir lattice defect.

A completion proof should now target one of the following precise mechanisms:

1. a multidimensional Poisson/Andreief formula turning `TLSE` into a sum of
   nonintersecting radial-heat squares;
2. a canonical-basis realization in which the lattice-Casimir alternant
   coefficient is a positive trace rather than an Euler characteristic;
3. a variation theorem for the lattice defect under every strictly
   totally-positive Schur test;
4. a source-built positive contraction whose exterior character realizes
   all coefficients in (4.2) simultaneously.

Any complete version proves the coefficient PF-infinity theorem, the
all-order E–Widder inequality, and RH.

## 8. Exact status

```text
strict TP of the full spectral kernel B(u,tau)       PROPOSED COMPLETE / REVIEW
spectral weighted theta-Darboux theorem              PROPOSED COMPLETE / REVIEW
positive duality for all spectral-Slater mixtures   PROPOSED COMPLETE / REVIEW
Schur/alternant generating identity                  PROPOSED COMPLETE / REVIEW
generic positive-extraction shortcut                 REFUTED EXACTLY
theta-mode bispectral Casimir identity               PROPOSED COMPLETE / REVIEW
Fourier self-duality of the Casimir                  PROPOSED COMPLETE / REVIEW
coefficient-resolved theta-Darboux sign TLSE          OPEN / RH-EQUIVALENT
all-order E-Widder source inequality                 OPEN / RH-EQUIVALENT
Riemann Hypothesis                                   UNPROVED
```

## 9. Review checklist

1. the half-line factors in (1.3)--(1.4);
2. the strict composition argument for Theorem 2.1;
3. the ordered-chamber normalization in Andreief;
4. the orientation of the two generalized Vandermonde determinants;
5. normal convergence in the Cauchy–Binet expansion (4.1);
6. the index orientation in (4.2)--(4.3);
7. the exact counterexample (5.1)--(5.2);
8. the identity `D_tau=M+1/2` on one literal theta atom;
9. the divergence-form boundary cancellation in (6.5);
10. Fourier conjugation of `M` and self-duality of `M(M+1)`.
