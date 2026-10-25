# Internal review of growing-prime coefficients and polynomial marks

Reviewed object: `FRACTIONAL_NATIVE.md`, SHA256
`46c4cc488a463b5ad0606945280f71fd52b4b3a829f0c836422dc44a3c92d379`.
Checker: `check_fractional_prefix.py`, 4,839 bytes, SHA256
`b98cf1a6409062d0566b955cd92a52a8a4bf9fbcf3920b9c7579f7a7265ddaef`.
Remote-commit authentication is a separate publication step.

Reviewer: `native_gain`, a different agent from the author. I did not
author the growing-prime convolution or mark estimates. During review
I identified the family-cap scope error in an earlier Section 7;
the reviewed version corrects it and distinguishes the initial
uncapped calculation from the new capped companion theorem. This is
internal review, not external peer review or formal verification.

## Source and coefficient scope

I fetched `DIRECT_NATIVE_APPLICATION.md` at
`0f07049ff1e8cc7765f6de01b4e176ad627bba4b`, Git blob
`ea1a09486fc77016629f0b4307f668ac8c297953`, and freshly read the
corresponding Xu--Sang v2 ordinary-product input. The reviewed note
retains its nonprincipal-row, natural-zero, fixed-ray, common-profile,
height and residual-scale restrictions. The convolution changes
arithmetic coefficients while leaving that family intact; it does
not insert a huge new conductor into the imported estimate.

## Specific checks

1. The local series ratio (1+zv)/(1+v) gives the full sequence
   (z-1)(-1)^(j-1) at every positive prime-power exponent j.
   Multiplication by 1+v cancels every unwanted nonsquarefree term.
   Deleting repeated powers would be wrong.
2. Complete multiplicativity, including zero values, proves the finite
   vector convolution. The factors psi_u(d)(Nd)^(it) are bounded row
   multipliers. The central normalizations multiply exactly to
   D^(-1/2), and no quotient coprimality is added. All residual scales
   are within the same prescribed bounded-power range or are bounded
   nonempty subunit scales explicitly allowed by the endpoint.
3. The triangle inequality and the positive absolute Euler product
   give precisely the denominator sqrt(Np)-1. The constant need not
   depend on the number or values of the changed primes because all
   of their cost is retained in that product.
4. The prime-ideal count in (10) is valid: degree-one primes give
   O(sqrt(Y)/log(2Y)) by rational prime counting, while higher residue
   degrees and the reciprocal-norm correction cost at most
   O(1+loglog(3Y)). Substitution of the proposed polylogarithmic
   cutoff makes its logarithmic coefficient cost o(log D).
5. For a general anchor z_0 the ratio (14) has coefficient
   (z_p-z_0)(-z_0)^(j-1). Its absolute geometric sum is exactly
   |z_p-z_0|/(sqrt(Np)-|z_0|). Formula (15) correctly retains the
   maximum available anchor estimate over every residual length.
6. Differentiating the finite coefficient identity, rather than an
   inequality, leaves precisely k distinct selected primes. Summing
   their arbitrary positive powers gives k! e_k(r_p), and
   k!e_k<=S_P^k. Independent parameters in disjoint bands give the
   product of the elementary symmetric polynomials. The endpoint's
   derivative and height orders do not grow with k.
7. The binomial polynomial (20) is the finite truncation of the
   derivative of rho^omega. It agrees with the actual damped mark
   whenever omega<=R. The sum of its absolute coefficient costs is
   retained in (21), including all normalizers. At the stated HLC
   scales the logarithm of that finite cost is
   O((log D)^(7/10)loglog D), hence subpower. This statement also
   retains the correct overall sign for differentiation at the
   inverse anchor z_0=-1.
8. The infinite damping remainder is not silently discarded. Its
   factorial tail at the displayed cutoff is subpower, which does
   not automatically beat a fixed-power family loss. The full Euler
   product cost in (23) is explicitly an upper-bound cost, not a
   lower bound for the actual row moment or the truncated divisor
   sum.

## Independent finite reproduction

I ran `python -I check_fractional_prefix.py` successfully. Its exact
rational output records 48,000 integer convolution cases, 15 local
series cases through degree 20, and 11,200 binomial-mark convolution
cases. Its repeated-prime negative control fails as intended at n=25.
These controls test finite coefficient algebra. They do not verify
the imported asymptotic endpoint or an infinite family estimate.

## The corrected capped calculation

I independently checked the algebraic identity (26). It describes
the uncapped optimization. The reviewed version now correctly notes
that the pinned OpenAI theorem supplies a cap for every relevant
finite-order Hecke function, so that this failed uncapped calculation
cannot rule out a capped improvement. The direct proof in
`CAPPED_NATIVE_MOMENT.md` is a separately reviewed object; fractional
analytic continuation is not claimed to establish it here.

## Assessment

I found no gap in Theorems 1 and 2 at the stated imported endpoint
scope. They are actual extensions to growing-prime coefficient sets
and finite polynomial marks, with their costs and quantifiers stated.
They do not prove the full damping-remainder estimate or a new
zero-free region. The cap correction removes an overbroad earlier
negative conclusion and is material to the additional native mean
proved in the companion note.

## Exact remote authentication (2026-10-25)

I independently fetched `FRACTIONAL_NATIVE.md` and `MANIFEST.json` from
`GettysburgResearch/riemann` at the exact final mathematical commit
`5c7f4aa542ea2112b7f95fce984a35dfe454cfd6`, under
`standalone/2026-10-25-hlc-zero-free-transfer/second-pass/`.
For the fetched note, I recomputed both SHA256 and Git blob SHA-1
(including the `blob <byte-length>\0` header), compared the reported
GitHub blob, checked the manifest entry, and compared the local bytes.
All four checks agree:

- Byte length: `18287`.
- SHA256: `46c4cc488a463b5ad0606945280f71fd52b4b3a829f0c836422dc44a3c92d379`.
- Git blob: `39a61be22e833912704a4b02d89d0673ea85455d`.

The manifest itself is 2963 bytes, SHA256
`68f69ad289a722a358b113cdec20db41cf54755bffb2c1bce73cecdf045e3536`,
Git blob `ca948bb86211998ad92e2c147bfb6e9b4b945f8f`; its fetched bytes also match the
local manifest, and its Git blob was independently recomputed.

These are exactly the mathematical bytes reviewed above, also fetched
unchanged at the preceding mathematical commit
`3b47783a7c775bc8133f6601cb9bb97b1b38678a`.

This appendix authenticates this note and its manifest entry. It does
not extend the analytic assessment, authorship independence, imported
source certification, or claim scope stated above.
