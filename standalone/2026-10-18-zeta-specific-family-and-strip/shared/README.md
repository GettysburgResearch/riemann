# Ordinary-zeta extraction from a quadratic field family

**Status: proposed component theorems, awaiting independent review.** This
packet proves explicit arithmetic extraction and residual identities. It does
not improve a zero-free strip or prove RH. No proposed quasi-RH theorem is a
dependency.

The family consists of the actual imaginary quadratic fields of fundamental
discriminant \(d=-8u\), with \(u\) odd and squarefree in \((Q,2Q]\). Every
Dedekind zeta function in the family is \(\zeta(s)L(s,\chi_d)\), so every
hypothetical ordinary zeta zero remains in every member. The construction
avoids asking for GRH for each additional Dirichlet factor.

## Proved components

- **The mean inverse source is ordinary Möbius.** If
  \(a_d=\mu*(\mu\chi_d)\), \(A_d(x)=\sum_{n\le x}a_d(n)\), and
  \(M(x)=\sum_{n\le x}\mu(n)\), then
  \(\lim_{Q\to\infty}\mathbb E_Q A_d(x)=M(x)\). The coefficients \(a_d\)
  are the full inverse Dedekind coefficients, with ramification included.

- **The complete critical energy is captured quantitatively.** Write
  \(E_\sigma(B;T)=\int_1^T|B(x)|^2x^{-2\sigma}dx/x\) and
  \(g(m)=\prod_{p\mid m}p/(p+1)\). For \(1/2\le\sigma\le1\),

  \[
  \mathbb E_QE_\sigma(A_d;T)
  =\sum_{\substack{m\le T\\m\text{ odd squarefree}}}
       g(m)m^{-2\sigma}E_\sigma(M;T/m)
   +O(Q^{-1/2}T^{5/2-2\sigma}\log(2T)).
  \]

  The main term lies between the ordinary energy and a constant multiple of
  it for \(\sigma>1/2\); at \(\sigma=1/2\), the upper factor is at most
  \(1+\log T\). Taking \(Q(T)\ge T^{3+\delta}\) makes the critical
  additive error vanish. If the signed sources are averaged before squaring,
  \(Q(T)\ge T^{3/2+\delta}\) already suffices. These give ordinary-RH
  criteria with the classical RH-to-Mertens converse; no auxiliary GRH is
  required and no new upper cancellation estimate is proved.

- **The full-product residual has an exact positive decomposition.** For the
  triangular inverse mollifier
  \(\mathcal M_{d,X}(s)=\sum_{mn\le X}\mu(m)\mu(n)\chi_d(n)(mn)^{-s}\),
  the limiting residual is an explicitly corrected ordinary Möbius bias plus
  a sum of nonnegative variance terms. All square aliases and ramified primes
  are retained. The complete formulas are (4.3)–(4.6) of [PROOF.md](PROOF.md).

- **The mean correction has a bounded inverse.** Its causal dilation kernel
  and inverse are absolutely summable whenever \(\Re s>1/2\), with bounds
  independent of the cutoff horizon. Power-decay estimates transfer in both
  directions without exponent loss in the stated range. Formula (5.5) gives
  an explicit analytic mollifier whose mean after multiplication by the full
  auxiliary L-factor is exactly the ordinary Möbius mollifier.

## Analytic domain and open problem

The full residual formula is proved for the limiting **actual arithmetic
family** at every fixed mollifier length \(X\) and \(\Re s>3/4\), excluding
the pole \(s=1\). A detailed approximate-functional-equation proof is included.
The analogous random Euler identity holds for \(\Re s>1/2\). The wider random
domain is not silently transferred to actual full L-values. The native
critical-energy identities above are actual arithmetic statements and have no
such domain gap.

At an ordinary zeta zero the full residual remains exactly 1 for every finite
family and mollifier. A complete bound strictly below 1 would exclude that
zero. **This strict-residual estimate and the required ordinary Möbius
cancellation remain open.** Enlarging the family does not remove the
explicit scalar bias or its positive variance.

## Reproduce the bounded checks

```bash
python check_shared_factor.py --output check_report.json
python -O check_shared_factor.py
```

The checker uses only the Python standard library and exact integer/Fraction
arithmetic, including complex rational Euler variables. It checks actual-field
inverse coefficients, finite ramified probability models, covariance and
critical energy, all terms in the residual decomposition, and the explicit
inverse correction. A small actual-discriminant table is clearly labeled as
finite observations. It does not certify infinite analytic claims or RH.

The relation to fixed-field PRs #996 and #998, their exact source commits,
all imported classical inputs, and the remaining gaps are recorded in
[PROOF.md](PROOF.md).
