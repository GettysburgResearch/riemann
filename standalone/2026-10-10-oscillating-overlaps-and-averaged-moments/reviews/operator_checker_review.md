# Independent finite operator-checker review

**Reviewer:** amplification subagent.  
**Verdict:** PASS within the finite scope below. No infinite operator, moment, or zero-free theorem is certified by this computation.

## Frozen source and reproduced results

Reviewed source: /workspace/scratch/5b23d9b20a3a/attack2_operator_check.py

SHA-256:

da375b646729871e48130d9179b2153e97f3735502d60b274c1c170385e40332

I inspected the complete source and independently ran both commands in /workspace/scratch/5b23d9b20a3a:

- python3 attack2_operator_check.py
- python3 -O attack2_operator_check.py

Both exited with status zero and reported PASS with **5,988 active assertions** and **311 ideals of norm at most 512**. The counts include repeated embedding and unit-invariance checks; they are not 5,988 distinct arithmetic objects.

Captured normal output: /workspace/scratch/5b23d9b20a3a/attack2_amp_operator_normal.json  
Captured optimized output: /workspace/scratch/5b23d9b20a3a/attack2_amp_operator_optimized.json

Both output files have the identical SHA-256:

9a5ed4b551e6ed1d3c35d7c8dbf6ae16bd3dadf627bc32bd56814d5ef485b13d

A byte comparison also returned equality. The checker uses an explicit require function that raises ArithmeticError on failure. Its checks are not Python assert statements, so optimization does not remove them. Only the standard library is imported.

## Independent arithmetic audit

The two coordinate conventions in the source are different and are both correct.

For C6, the generator is \(\zeta_6\), satisfying \(\zeta_6^2=\zeta_6-1\). Hence

\[
(a+b\zeta_6)(c+d\zeta_6)
=(ac-bd)+(ad+bc+bd)\zeta_6,
\]

\[
\overline{a+b\zeta_6}=(a+b)-b\zeta_6,\qquad
N(a+b\zeta_6)=a^2+ab+b^2.
\]

These are exactly the implemented multiplication, conjugation, norm, and conjugate-over-norm inverse. All coordinates used in the checks are rational fractions; no floating-point rounding enters.

For the Eisenstein lattice, the generator is \(\omega\), satisfying \(\omega^2+\omega+1=0\). The implemented formulas are

\[
(a+b\omega)(c+d\omega)
=(ac-bd)+(ad+bc-bd)\omega,\qquad
N(a+b\omega)=a^2-ab+b^2.
\]

The six listed units are precisely \(1,\omega,\omega^2,-1,-\omega,-\omega^2\). Taking the lexicographically least associate therefore gives one representative per nonzero principal ideal. In the Eisenstein ring every ideal is principal; no ideal classes are omitted. Every nonzero associate orbit has six elements.

The lattice box covers the full norm disk: since

\[
a^2-ab+b^2\ge\frac12(a^2+b^2),
\]

norm at most \(B\) implies \(|a|,|b|\le\sqrt{2B}\). The chosen radius is larger than that bound.

The comparison count is independently computed from rational-prime factorization. A split prime \(\ell\equiv1\pmod3\) contributes \(e+1\) ideals at exponent \(e\); an inert prime \(\ell\equiv2\pmod3\) requires an even exponent and then contributes one; the ramified prime 3 contributes one at every exponent. The implementation agrees with these cases. It checks the lattice count at each individual norm \(1,\ldots,512\), not just the final total.

## Exact masks and coefficient checks

The maps \(\omega\mapsto2\pmod7\) and \(\omega\mapsto3\pmod{13}\) respect the Eisenstein relation, since \(2^2+2+1=7\) and \(3^2+3+1=13\). Their kernels are the actual prime ideals \((7,\omega-2)\) and \((13,\omega-3)\), of norms 7 and 13. Testing \(a+b\omega\) by \(a+bw\equiv0\pmod\ell\) therefore tests divisibility by the indicated prime ideal. The unit-invariance checks correctly confirm that this property is independent of the chosen associate.

For all 11 declared cutoffs and \(0\le e_7,e_{13}\le4\), the checker compares the independently enumerated mask count with

\[
J\!\left(\left\lfloor
\frac{Y}{7^{1_{e_7>0}}13^{1_{e_{13}>0}}}
\right\rfloor\right).
\]

This is the correct radical dependence for geometric removal coefficients, including coefficients whose prime-power degree greatly exceeds the base cutoff. The subsequent mean-coefficient equality checks exact accumulation in C6 using the prescribed sixth-root phases.

The local inverse test covers \(q=3,7,13,19\), each of the six unit phases and the zero phase, and all convolution degrees \(0,\ldots,16\). I checked that its formulas are the local mean coefficients \(q^{-1}\eta^j\) and inverse coefficients

\[
-q^{-1}\eta^j(1-q^{-1})^{j-1}\qquad(j\ge1).
\]

The 476 exact convolution checks authenticate the claimed inverse identity to those finite orders.

## Finite Gram matrices and limits of the result

The Gram computations use the three real Mellin modes \(\sigma=1,2,3\), the two selected prime responses, and actual enumerated ideal bases. Equivalently, they use a completely multiplicative coefficient function supported on those two primes. They do **not** evaluate all local factors of a fixed finite-order Hecke character.

The response construction, conjugation convention, and recursive determinant formula are correct. The checker verifies Hermitian symmetry and nonnegative leading minors. At each tested cutoff \(Y\ge13\), all three leading minors are strictly positive, giving positive definiteness by Sylvester's criterion. The displayed full determinants vanish for \(Y=1,7\), as expected when fewer response types are present. Positive semidefiniteness at those smaller cutoffs also follows directly from the verified Gram construction; the source does not claim that checking only leading nonnegative minors would certify an arbitrary Hermitian matrix as positive semidefinite.

The computation covers two prime-ideal masks, four local inverse norm parameters through degree 16, and the displayed finite base cutoffs. It does not establish absolute Euler-product convergence, a uniform inverse bound as \(Y\) grows, arbitrary-mode separation, weighted coercivity on an infinite function space, a Möbius moment estimate, or an \(L\)-function zero-free region. Those require the separate mathematical proofs.

The source and mathematical proof note were left unchanged.
