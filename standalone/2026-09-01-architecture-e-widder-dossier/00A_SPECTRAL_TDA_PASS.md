# Current spectral theta–Darboux pass

Status: **PROPOSED EXACT THEOREMS AND SHARP GAP ISOLATION; INDEPENDENT REVIEW REQUIRED; RH REMAINS UNPROVED.**

This page records the latest proof pass on the weighted theta–Darboux/
Andreief gate.  The full coefficient-resolved gate is RH-equivalent and is
not proved here.  The pass does prove the complete spectral weighted theorem
at every exterior rank, identifies the exact coefficient-extraction
obstruction, and exposes the additional arithmetic structure available from
the literal theta lattice.

Read the complete proof in
[`15_SPECTRAL_WEIGHTED_VARIATION_AND_BISPECTRAL_GATE.md`](15_SPECTRAL_WEIGHTED_VARIATION_AND_BISPECTRAL_GATE.md).

## 1. The theorem proved at every rank

Let

\[
 B(u,\tau)=\cosh\!\left(\tau\sqrt{u+\frac14}\right),
 \qquad L=D_\tau^2-\frac14,
\]

and let

\[
 \mathfrak X(u)=2\int_0^\infty\Phi(\tau)B(u,\tau)d\tau.
\]

For every increasing exponent packet

\[
 H=(h_1<\cdots<h_r)
\]

and every increasing positive spectral packet

\[
 0<u_1<\cdots<u_r,
\]

the exact spectral weighted variation formula is

\[
 \boxed{
 \begin{aligned}
 &2^r\int_{0<\tau_1<\cdots<\tau_r}
 \det[(L^{h_p}\Phi)(\tau_\ell)]_{p,\ell}
 \det[B(u_q,\tau_\ell)]_{q,\ell}
 \,d\boldsymbol\tau\\
 &\qquad=
 \left(\prod_{q=1}^r\mathfrak X(u_q)\right)
 \det[u_q^{h_p}]_{p,q}>0.
 \end{aligned}
 }
 \tag{STDA}
\]

This holds for every finite rank.  Its proof uses only:

1. the eigenfunction identity `L_tau B=uB`;
2. self-adjoint transport of `L` through the even, rapidly decreasing theta
   source;
3. Andreief's continuous Cauchy–Binet identity;
4. positivity of `mathfrak X(u)` on the positive axis;
5. positivity of the generalized Vandermonde.

The spectral kernel `(u,tau)->B(u,tau)` is itself strictly totally positive
of infinite order.  Thus the theta–Darboux current lies in the strict dual
cone of every positive mixture of spectral Slater determinants.

## 2. Relation to the original coefficient gate

Writing

\[
 B(u,\tau)=\sum_{n\ge0}b_n(\tau)u^n,
\]

discrete Cauchy–Binet gives

\[
 \det[B(u_q,\tau_\ell)]
 =\sum_{N}
 \det[u_q^{n_p}]\det[b_{n_p}(\tau_\ell)].
\]

Consequently `(STDA)` expands as

\[
 \boxed{
 \begin{aligned}
 &\left(\prod_q\mathfrak X(u_q)\right)
 \det[u_q^{h_p}]\\
 &\qquad=
 \sum_N
 \det[c_{n_q-h_p}]
 \det[u_q^{n_p}],
 \end{aligned}
 }
 \tag{SCHUR}
\]

where `mathfrak X(u)=sum c_nu^n` and `c_j=0` for `j<0`.
The coefficient-resolved weighted theta–Darboux integral is exactly

\[
 \det[c_{n_q-h_p}].
\]

Thus the remaining theorem is not positivity of the complete spectral
transform.  It is nonnegativity of every individual Schur/alternant
coefficient in `(SCHUR)`.

## 3. A generic extraction shortcut is impossible

Spectral positivity does not imply coefficientwise Schur positivity for a
generic positive-coefficient function.  The exact polynomial

\[
 X(u)=1+u+2u^2
\]

satisfies

\[
 X(u_1)X(u_2)(u_2-u_1)>0
 \qquad(0<u_1<u_2),
\]

but its coefficient minor is

\[
 \det\begin{pmatrix}1&2\\1&1\end{pmatrix}=-1.
\]

Therefore the last extraction step must use the literal Riemann theta
lattice, modularity, or a positive representation-theoretic realization.  It
cannot follow from spectral total positivity alone.

## 4. The source-specific structure now isolated

For one continuous theta mode define

\[
 g(m,\tau)=e^{\tau/2-\pi m^2e^{2\tau}},
 \qquad M=m\partial_m,
 \qquad {\cal A}=M(M+1)=\partial_m(m^2\partial_m).
\]

Then

\[
 \boxed{
 (D_\tau^2-1/4)g={\cal A}_mg.
 }
\]

The actual source satisfies

\[
 \boxed{
 L^h\Phi(\tau)
 =\sum_{m\ge1}{\cal A}^{h+1}g(m,\tau)
 =\left(\sum_{m\ge1}-\int_0^\infty dm\right)
   {\cal A}^{h+1}g(m,\tau).
 }
\]

The continuum term vanishes by the divergence form of `A`.  Under Fourier
transform in `m`, `M` maps to `-M-1`, so the Casimir `M(M+1)` is invariant.
The arithmetic current is therefore a Fourier-self-dual radial-Casimir
*lattice defect*.

This is the extra structure absent from the generic counterexample.

## 5. Coefficientwise range already covered

The branch's imported Schoenberg-sector theorem, using the repository's
locked finite-height zero verification, gives the invariant coefficient
sequence the `PF_m` property through

\[
 m=9{,}419{,}999{,}999{,}999.
\]

Consequently the original coefficient-resolved theta–Darboux integral is
already nonnegative for every admissible packet of exterior rank at most that
integer.  The new theorem `(STDA)` has no rank bound but applies to the full
spectral-Slater cone rather than to each coefficient Slater separately.

These two regions are complementary:

```text
coefficient tests: all packets through rank 9.42e12;
spectral tests:    all packets at every finite rank;
remaining gate:    coefficient extraction at unbounded rank.
```

The external zero verification is imported and was not rerun in this pass.

## 6. Sharpened gate

The exact remaining statement is the **theta-lattice Schur-extraction gate**
`TLSE`:

> Use the Fourier-self-dual lattice-Casimir representation to prove that every
> alternant coefficient in `(SCHUR)` is nonnegative.

Equivalently, prove for every admissible `H,N`

\[
 \int_{\tau_1<\cdots<\tau_r}
 \det[(L^{h_p}\Phi)(\tau_\ell)]
 \det[b_{n_q}(\tau_\ell)]
 \,d\boldsymbol\tau\ge0.
\]

A successful proof must supply one of the following source-specific
mechanisms:

1. multidimensional Poisson/Andreief conversion to nonintersecting radial
   heat squares;
2. a canonical positive basis in which the lattice-Casimir coefficient is a
   trace rather than an Euler characteristic;
3. a variation theorem for the lattice defect against every strictly-TP
   Schur test;
4. one positive contraction realizing all coefficients simultaneously.

Any complete form proves the coefficient `PF_infinity` theorem, the all-order
E–Widder inequality, and RH.

## 7. Bounded verification

The new standard-library checker is

[`verify_spectral_weighted_variation.py`](verify_spectral_weighted_variation.py).

The authoring run passed:

```text
PASS_SPECTRAL_WEIGHTED_VARIATION_EXACT_CHECKS
spectral_cauchy_binet=8
generalized_vandermonde=3
spectral_extraction_firewall=2
bispectral_casimir=4
source_mode_ladder=4
total=21
COEFFICIENT_RESOLVED_TDA_SIGN_OPEN
RH_UNPROVED
```

The checks authenticate bounded rational algebra only.  They do not certify
the infinite Andreief passage, the imported sector theorem, `TLSE`, or RH.

## 8. Current boundary

```text
spectral kernel B(u,tau) is STP_infinity             PROPOSED COMPLETE / REVIEW
spectral weighted theta-Darboux theorem, all ranks   PROPOSED COMPLETE / REVIEW
Schur/alternant generating identity                  PROPOSED COMPLETE / REVIEW
generic spectral-to-coefficient shortcut             REFUTED EXACTLY
lattice-Casimir bispectral identity                   PROPOSED COMPLETE / REVIEW
coefficient TDA through imported sector rank          IMPORTED + EXACT BRIDGE
unbounded coefficient-resolved TLSE                   OPEN / RH-EQUIVALENT
all-order E-Widder inequality                         OPEN / RH-EQUIVALENT
Riemann Hypothesis                                    UNPROVED
```
