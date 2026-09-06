# L-91038 — Suzuki's normalized tangent gives the scalar Cauchy commutator

Claim ID: `L-91038`  
Status: **EXACT SCALAR OPERATOR IDENTITY; FULL-KERNEL REDUCTION REFUTED BY `R-91010`**  
Created: 2026-08-12  
Corrected: 2026-08-12  
Depends on: `L-91035`, `L-91037`, `R-91009`, `R-91010`, main `L-91023`  
RH status: **unproved**

## 1. Suzuki orientation

Use

\[
 \Theta_a(z)
 =\frac{\xi(1/2-a-iz)}{\xi(1/2+a-iz)}.
\]

For safe `a>=1/2`, this is meromorphic inner unconditionally.  On the real
axis put

\[
 q_a(x)=-i\Theta_a(x)^{-1}\partial_x\Theta_a(x).
\]

Functional-equation symmetry gives

\[
 q_a(x)=2\Re\frac{\xi'}{\xi}
 \left(\frac12+a-ix\right).
\]

## 2. Normalized radial tangent

Define

\[
 B_a(x)
 =-i\partial_a[a^{-1}\log\Theta_a(x)].
\]

Then

\[
 \partial_xB_a(x)=\partial_a[q_a(x)/a]
\]

and the scalar Cauchy soft count is

\[
 \boxed{
 \mathcal N_x(a)
 =-\frac{a^3}{4}\partial_xB_a(x).
 }
 \tag{L-91038.1}
\]

In Mellin spectral coordinates Suzuki's completed Hankel operator is

\[
 \mathsf S_a=M_{\Theta_a}\mathsf R.
\]

Its normalized tangent is the self-adjoint multiplication operator

\[
 \mathsf B_a=M_{B_a(x)}.
\]

With `P=-i partial_x`,

\[
 \boxed{
 M_{\mathcal N(a)}
 =-\frac{a^3}{4}i[\mathsf P,\mathsf B_a].
 }
 \tag{L-91038.2}
\]

This is an exact Mourre-type identity for the **scalar diagonal**.

## 3. Source split

From

\[
 \Theta_a=\Gamma_aQ_a
\]

one gets

\[
 \mathsf B_a
 =\mathsf B_a^{\Gamma,\mathrm{pole}}
  +\mathsf B_a^{\rm J}.
\]

On a safe line, `L-91037` factors the normalized Jordan radial derivative as
one positive first-chaos Gram.  The gamma/pole term is explicit.  Their
completed recombination gives the scalar tangent symbol `B_a`.

## 4. Exact firewall

`R-91010` proves that the multiplication operator in `(L-91038.2)` is not the
fully polarized delayed screw kernel.

For one synthetic real zero, the true carrier kernel is

\[
 \Psi_a(\gamma-x)\overline{\Psi_a(\gamma-y)},
\]

which is generically nonzero for `x!=y`.  The multiplication surrogate has
off-diagonal distribution kernel zero.  Therefore the complete carrier,
delay, orientation and bridge Gram cannot be replaced by `(L-91038.2)`.

The earlier statement that CDFHTI was equivalent to a positive factorization
of this single commutator was false.

## 5. Correct use

The scalar commutator remains useful for:

```text
diagonal estimates;
pointwise Cauchy gates;
normalization checks;
identifying the radial source derivative;
constructing necessary scalar tests of a full colligation.
```

The actual conclusion-producing operator is

\[
 (\mathcal A_a^{\rm del})^*
 \mathfrak Q_\zeta
 \mathcal A_a^{\rm del},
\]

where `A_a^del` synthesizes arbitrary finite superpositions of delayed causal,
anti-causal and bridge tests.  `T-91008` is corrected accordingly.

## 6. Exact boundary

```text
Suzuki amplitude involution                         IMPORTED PROVED
normalized tangent multiplier                       EXACT
scalar Cauchy soft count = tangent commutator        EXACT
commutator = full delayed screw Gram                 FALSE
safe Jordan scalar tangent = positive first chaos   EXACT
full source-ordered delayed Gram factorization       OPEN / RH-EQUIVALENT
Riemann Hypothesis                                   UNPROVED
```
