# Review of the uniform prime and sector consequences

Date: 2026-10-20. Reviewer: Type-I subagent, independently of the author
of ../uniform/FULL_FAMILY_CONSEQUENCES.md.

Reviewed SHA256:
4d2c4476e3235cb9e1bfa3557134b8ec2eed71dc18004eed0ed67e2f6369a159.
The uniform reciprocal premise was previously reviewed in
REVIEW_UNIFORM.md. This review is conditional on the same common
zero-free boundary for the full family of actual unitary characters.

**Verdict:** no outstanding issue was found in the deductions.
No edit was needed. These are classical analytic consequences of
the stated common boundary; they do not prove that boundary anew.

For a pure norm twist, let \(\rho=1+i\tau\) and
\[
 F_\chi(s)=\frac{s-\rho}{s+1-i\tau}L(s,\chi).
\]
If \(h_\chi=\log F_\chi\), then exactly
\[
 -\frac{L'}L(s,\chi)-\frac1{s-\rho}
       =-h_\chi'(s)-\frac1{s+1-i\tau}.
\]
Thus equation (3) has the correct pole and rational-term signs.
Cauchy's formula on a smaller fixed-gap disk applies to the
uniform logarithm bound. Its arbitrary small conductor exponent
is available for \(h_\chi'\), as required.

Put \(C_0=\mathcal C(\chi,0)\), \(n=[F:\mathbb Q]\). The explicit
conductor satisfies
\[
 \mathcal C(\chi,t)\ll_F C_0(1+|t|)^n.
\]
Choose \(T\asymp x^2 C_0^2\), with a fixed sufficiently large
constant. Then \(T\) exceeds twice the possible \(|\tau|\), since
\(|\tau|\ll_F C_0\). Both horizontal edges consequently stay away
from the translated pole. On the rectangle, an internal exponent
\(\varepsilon'\) costs at most
\[
 C_0^{(1+2n)\varepsilon'}x^{2n\varepsilon'}.
\]
Choose \(\varepsilon'\) after the requested final epsilon and the
left-line gap. The logarithmic integration factors are absorbed in
the remaining allowance. The vertical and horizontal contributions
then have the claimed \(C_0^\epsilon x^{\beta+\epsilon}\) bound.
The explicitly separated rational pole term has smaller integral
size and the sole residue \(x^{1+i\tau}/(1+i\tau)\).

The norm-grouped Dirichlet coefficients are uniformly bounded by
\(d_n(m)\log m\). Half-integer Perron therefore has the claimed
truncation bound. Replacing the half integer by the original \(x\)
does not change the set of integer norms, and the derivative of
the principal main term is \(x^{i\tau}\), of modulus one.
This confirms the uniformity in arbitrarily large norm twists.

Over \(E=\mathbb Q(\omega)\), every ideal prime to \(3\) has a
unique primary generator; their products remain primary.
Thus \(\alpha(\mathfrak a)=c/|c|\) is multiplicative and is a
unitary Hecke character with fixed finite conductor. For every
nonzero integer \(k\), \(\alpha^k\) has nonzero angular type and
is not a pure norm character. Its conductor is \(O((3+|k|)^2)\).
The full-family premise is essential here, including the first
positive and negative harmonics.

Removing prime powers costs \(O_E(x^{1/2}\log^2x)\), uniformly in
the harmonic, since all character values have modulus at most one.
The upper and lower trigonometric approximations of an arc have
constant-term error \(O(1/H)\) and coefficients
\(O(1/|k|+1/H)=O(1/|k|)\) for \(1\le |k|\le H\).
Applying them to the positive prime weights gives precisely
\[
 x/H+x^{\beta+\varepsilon'}H^{2\varepsilon'}\log(2H).
\]
For \(H\asymp x^{1-\beta}\), the second exponent is
\(\beta+(3-2\beta)\varepsilon'\); taking the internal epsilon
small proves the requested uniform \(x^{\beta+\epsilon}\) error.

Partial summation is uniform in the same fixed arc at every
intermediate norm and gives the stated unweighted formula.
For arcs of length at least \(x^{\beta-1+\delta}\), choose the
final epsilon smaller than \(\delta\). The error divided by the
main term tends to zero, even after its factor \(\log x\).
The resulting shrinking-sector asymptotic and its displayed
numerical exponent are therefore consistent with the premise.
