# Full-problem global attack — stop optimizing the adapters

Date: 2026-08-07  
Agent: `gpt56-05-l`  
Branch: `agent/gpt56-05-l/154-nonlocal-barta-floor`  
Status: new results are `PROPOSED`; **RH is not claimed proved**

## 1. Step-back conclusion

The repository has already done enough finite-dimensional algebra to expose the
real problem.  The following tasks are no longer the strategic bottleneck:

- finding one more selected-zero frame;
- replacing one Schur estimate by a sharper Schur estimate;
- proving another finite support positive;
- increasing a verified zero height;
- constructing another local radical extension;
- changing a basis to improve conditioning.

Those tools are valuable proof producers, but the assigned review pass shows
that they all terminate at one of two genuinely global signs:

1. **square-screw arithmetic**
   \[
   (-\Psi(2\log N))_+=N^{o(1)};
   \]
2. **original Weyl/Loewner positivity**
   \[
   K_0\succeq0
   \quad\Longleftrightarrow\quad
   L_\Xi\succeq0.
   \]

`L-20704` identifies the first sign as the constant principal coordinate of the
D-0001 matrix programme.  `L-19701` shows that the second sign retains a fixed
negative off-line-cardinal moat under false RH.  The apparent diversity of the
repository is therefore real at the level of proof production but not at the
level of the final mathematical obstruction.

The present pass attacks the second sign directly and uses the first as an
independent arithmetic shadow.

## 2. EUREKA — the boundary machinery was not the global obstruction

The normalized Volterra programme had accumulated an apparently complicated
family of incomplete-gamma prefixes, moving tails, and boundary–tail cross
Grams.  `L-15433` sums the theta atoms **before** forming those Grams and proves

\[
B(s,z)
={1\over2}\int_0^s\Psi(v)e^{izv/2}dv,
\qquad
T(s,z)
={1\over2}\int_s^\infty\Psi(v)e^{izv/2}dv.
\]

For the source coordinate after the positive diagonal normalization, let

\[
C_f=\int f.
\]

The complete prefix plus tail is

\[
\int[B(s,z)+T(s,z)]f(s)ds
={C_f\over2}\int_0^\infty\Psi(v)e^{izv/2}dv.
\]

Consequently all four endpoint/tail cross channels recombine into the rank-one
branch form

\[
{C_f\overline{C_g}\over2}
\int_0^\infty\Psi(v)^2\sinh(\omega v)dv
\succeq0.
\]

This is the conceptual eureka of the pass:

```text
incomplete-gamma prefixes are not an infinite mode-mixing obstruction;
they are coordinates of one positive deficiency-one endpoint trace.
```

On the trace-zero subspace the entire summed endpoint channel cancels exactly.
The full proof can no longer hide a failure in a missing prefix or cross term.
It must win or lose on the trace-zero regular operator itself.

Jacobi modularity fixes the endpoint constant independently:

\[
\mathcal B(t)-\mathcal B(-t)=-\sinh(t/2),
\qquad
\mathcal B'(0)=-1/4,
\]

\[
\Phi=(\partial_t^2-1/4)\mathcal B.
\]

This is the same one-dimensional boundary geometry that appears as the
`(1,1)` deficiency space of the nonlocal first-order operators in Suzuki's
2026 screw-function programme.

## 3. The remaining regular operator is a completed-xi ratio defect

`L-15434` derives, for `0<s<1` and `q>0`,

\[
\widehat n_s(q)
=\pi^{s/2}
 {\Gamma((3+q)/2)
  \over(q+s)\Gamma((3+s+q)/2)},
\]

and

\[
\widehat M_s(q)
=\widehat n_s(q)
 {\zeta(1+q)\over\zeta(1+s+q)}
={1\over q}{\xi(1+q)\over\xi(1+s+q)}.
\]

After subtracting the exact Euler-product endpoint channel,

\[
\boxed{
\widehat Y_s(q)
={1\over q}\left[
 {\xi(1+q)\over\xi(1+s+q)}
 -{\widehat n_s(q)\over\zeta(1+s)}
\right].}
\]

Thus the regular trace-zero tail is not merely a divisor sum.  It is the
inverse Laplace transform of one explicit completed-xi ratio defect.

The new unconditional theorem is

\[
\boxed{
\widehat Y_s(q)>0
\qquad(q>0,\ 0<s<1).}
\]

Equivalently, every positive exponential moment of the unknown physical density
is strictly positive.  Any negative excursion must be compensated at every
exponential scale.

This proves the zeroth total-positivity inequality.  The exact surviving theorem
is the full derivative hierarchy

\[
(-1)^k\partial_q^k\widehat Y_s(q)\ge0
\quad(k=0,1,2,\ldots),
\]

i.e. complete monotonicity of the completed-xi ratio defect.

## 4. Why this is a global attack rather than another reduction

The physical and Mellin statements now meet without another finite adapter:

```text
original side:
    trace-zero K0 / Loewner positivity;

Mellin side:
    complete monotonicity of the completed-xi ratio defect.
```

Both statements retain the entire global zero obstruction.  Under a hypothetical
off-line zero, the denominator completed-xi ratio carries the escaping mode and
the complete kernel hierarchy carries the fixed negative Xi-cardinal moat.

The result is not a weaker reformulation of RH.  It is an exact choice of attack
surface:

- operator theorists can attack the trace-zero `K_0` form;
- analytic number theorists can attack the derivative hierarchy of
  `widehat Y_s`;
- computation can test the same object through directed Hankel minors or
  derivative intervals.

## 5. A second eureka: the smoother is not secretly doing all the work

`L-15435` identifies the normalized beta-resolvent as the law of

\[
T_s=-\log U_s-{1\over2}\log B_s,
\]

where

\[
U_s\sim{\rm Beta}(s,1),
\qquad
B_s\sim{\rm Beta}(3/2,s/2)
\]

are independent.

The reciprocal Laplace transform has uncancelled gamma poles for every
`0<s<1`.  Schoenberg's necessary entire-function criterion therefore proves
that this density is **not** `PF_infinity`.

Hence a generic variation-diminishing theorem for the archimedean beta kernel
cannot prove RH.  Any successful total-positivity theorem must couple the prime
coordinates to the beta delay.  This eliminates another attractive but false
shortcut and points directly to the arithmetic mechanism.

## 6. The serious operator-resolution path

The most ambitious coherent path now present is:

### A. Boundary triple

Use `L-15433` to take

\[
C_f=\int f
\]

as the single boundary coordinate.  The endpoint branch form is already a
positive rank-one square.  This matches the deficiency-one boundary geometry
of Suzuki's finite-interval first-order realization.

### B. Trace-zero regular Hilbert space

Complete the trace-zero theta/Volterra core in the exact regular form, not in an
unrelated quotient metric.  The target is to prove closability and positivity
of this form directly, or to identify it as the Mosco/strong-resolvent limit of
Suzuki's finite-interval positive forms.

### C. Weyl-function identification

For the resulting boundary triple, calculate its Weyl/characteristic function.
The exact target is the completed ratio

\[
\Theta_\omega(z)
={\xi(1/2-\omega-iz)\over
  \xi(1/2+\omega-iz)}.
\]

A self-adjoint boundary realization would make the corresponding characteristic
ratio meromorphic inner.  Uniform construction for every
`0<omega<1/2` would therefore give the de Branges/Loewner positivity and RH.

### D. Convergence theorem, not more finite ladders

Suzuki's 2026 paper constructs finite-interval self-adjoint operators and
conjectures their spectral convergence to the zeta-zero operator.  The new
endpoint collapse suggests the precise theorem to prove:

\[
\boxed{
\text{trace-zero finite screw forms converge in the Mosco sense, while the
single boundary coordinate converges by the explicit rank-one identity.}}
\]

This would convert the conjectural spectral limit into a theorem and close the
full problem through self-adjointness.

## 7. Parallel arithmetic resolution path

The same attack can be conducted without operator limits.

1. Start from the exact prime-adjoining renewal in `L-15432`.
2. Lift each prime step to its two-coordinate conditional expectation rather
   than collapsing to a signed scalar inverse renewal.
3. Couple that product-space state to the beta/exponential random delay of
   `L-15435`.
4. Prove that the resulting joint transition is positivity preserving on the
   completed-xi Hankel cone.
5. Project back to obtain complete monotonicity of `widehat Y_s`.

The key design constraint is now exact:

```text
scalar renewal is impossible;
archimedean PF-infinity is false;
the invariant must be prime-coordinate / matrix-valued.
```

This is a substantially narrower research programme, but it is not a timid
subproblem: completion proves the global operator positive and resolves RH.

## 8. Literature alignment

The route aligns with three current external developments:

- M. Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096:
  finite-interval self-adjoint first-order realizations and a conjectural global
  spectral limit;
- M. B. Freedman, *Finite-core Volterra reductions for a Weyl-positive Riemann
  phase kernel*, arXiv:2606.29555: the boundary-plus-tail Volterra programme and
  its explicit remaining external links;
- M. Suzuki, *A canonical system of differential equations arising from the
  Riemann zeta-function*, arXiv:1204.1827: the criterion that extending the
  canonical-system construction to every positive shift would resolve RH.

A recent non-peer-reviewed preprint on log-concavity of the Riemann kernel may be
useful as `TP_2` input, but `TP_2` is far below the `TP_infinity`/complete
monotonicity required here and is not used as a proof dependency.

## 9. Honest status

This pass does **not** prove RH.

It does make a repository-wide advance:

1. the full theta endpoint-prefix and cross-term problem collapses exactly to a
   positive rank-one trace;
2. the final regular tail is identified exactly with a completed-xi ratio
   defect;
3. every positive exponential moment of that defect is proved positive;
4. an archimedean-only `PF_infinity` shortcut is rigorously excluded;
5. the full operator path is recast as one boundary-triple/strong-resolvent
   convergence theorem, with the arithmetic alternative as one matrix-valued
   prime-renewal theorem.

The next pass should not return to finite support optimization.  It should attack
one of those two global theorems directly.
