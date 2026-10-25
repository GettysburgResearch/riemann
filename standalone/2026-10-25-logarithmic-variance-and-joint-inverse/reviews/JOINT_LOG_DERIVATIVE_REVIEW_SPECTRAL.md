# Independent review of the complete logarithmic-derivative moment

Reviewer: `/root/spectral_floor`.
Date: 25 October 2026.
Reviewed object: `third-pass/native/JOINT_LOG_DERIVATIVE.md`.
Exact reviewed file SHA256: `4a1156b0dfafe64eb8f6dbf8f76a597a6a4c09bb6c65308e3dde6868571dcb29`.
Disposition: **PASS for Proposition 1, the exact height and annular decompositions, the paid prime-square upper bound (14), and the stated no-gain implications, relative to the explicitly imported native inverse moment and its scope. No improved zero-free exponent is certified.**

The review independently reconstructs the coefficient identities and moment transfer. It does not re-prove the external physical inverse moment, the imported all-family zero-free cap, or the entire upstream detector framework. The capped-moment source at `5c7f4aa542ea2112b7f95fce984a35dfe454cfd6` was read to check its actual coefficient, mask, bounded-power length, and height/profile scope. This is a review of the file identified above, not of a subsequent integration commit.

## 1. Complete divisor reassembly

The convolution identity has the correct sign:

\[
\mu_E*\Lambda_E=-\mu_E\log N.
\]

Indeed the derivative of \(1/\zeta_E(s)\) is both the Dirichlet series of \(-\mu_E(n)\log Nn\) and the product \((1/\zeta_E(s))(-\zeta_E'(s)/\zeta_E(s))\). This comparison is justified in the absolute half-plane and then gives a finite coefficient identity.

The literal zero-extended character is completely multiplicative, with modulus at most one. Multiplication by \(\psi_u(n)(Nn)^{iv}\) therefore preserves this identity, including every original zero and any common puncture. The equality is not relying on restoration of deleted Euler factors. The height must be the same in the two factors, as the note states.

At total norm \(Nn\), the profile in (3) depends only on \(Nn/Y\), with no independent divisor cutoff. Consequently the identity gives

\[
\mathcal J_u(Y;W)
=-\log Y\,M_u(Y;W)-M_u(Y;W\log)
\]

with exactly the displayed normalization \(Y^{-1/2}\). Multiplication by \(\log x\) is bounded on the fixed compact annular profile class. Applying the native moment twice and using the squared triangle inequality proves (5), with only logarithmic losses. The capped version uses the same unchanged coefficient and profile operations, so it follows with the exact imported dependencies of that capped estimate.

The reverse adapter (5a) also checks: using the profile \(W(x)/\log(Yx)\), the complete coefficient \(-\mu_E(n)\log Nn\) cancels its denominator. For sufficiently large \(Y\), that denominator is bounded away from zero on the fixed support, and each fixed-order profile seminorm is \(O(1/\log Y)\). Thus the complete-convolution moment is a genuine bound at total length, but it carries the same native norm information, up to logarithms. It is not an improved moment exponent by itself.

## 2. Unequal incoming heights

For a squarefree \(n\), only the prime terms with exponent one contribute; \(\mu_E(n/p)=-\mu_E(n)\), giving (8). If \(n=p^a b\), \(a\ge2\), with \(b\) squarefree and prime to \(p\), exactly the terms with prime-power exponents \(a\) and \(a-1\) survive. Their signs are opposite, giving (9). If two primes have exponent at least two, removing a single prime power leaves another square, so every term vanishes.

The coefficient error (10) follows from
\(|e^{i\Delta y}-1|\le|\Delta|\,|y|\). For a squarefree coefficient it is bounded by
\(|\Delta|\sum_{p\mid n}(\log Np)^2\le|\Delta|(\log Nn)^2\). For the one-heavy-prime case the phase difference in (9) is at most \(|\Delta|\log Np\), giving an even smaller bound after the von Mangoldt factor. This verifies the stated exact defect without asserting that a coefficientwise error is small in the native second moment.

## 3. One prime annulus and the square correction

Opening the annular product, the squarefree part has \(d=n/p\), with Möbius coefficient \(-\mu_E(n)\). Its profile is exactly
\(W(Nn/(NpD))V(Np/L)\), giving the minus sign and all normalization factors in (11).

Every nonsquarefree product has the unique form \(n=p^2b\), where \(d=pb\), \(b\) is squarefree, and \((p,b)=1\). Its coefficient is \(-\mu_E(b)\), its character factor is \(\psi_u(p^2)\psi_u(b)\), and its height factor is \((Np)^{2iv}(Nb)^{iv}\). These are exactly the terms in (12). No additional nonsquarefree patterns occur because the inverse factor is squarefree and the second factor is one prime.

Putting \(X_p=D/Np\) converts the inner sum into \(X_p^{1/2}M_u^{(p)}(X_p;W)\). Combined with \((DL)^{-1/2}\), the coefficient is exactly \((L Np)^{-1/2}\), as stated. On the support of \(V\), \(Np\asymp L\). Elementary ideal counting bounds the sum of the absolute scalar coefficients by \(O(\log(2L))\); no character averaging in \(p\) is needed for this step.

The single-prime deletion expansion (13) was checked directly. Opening its right side, the normalization \((X/(Np)^k)^{-1/2}\) cancels \((Np)^{-k/2}\), and the height factors combine to the original total norm. The coefficient of a term with a positive \(p\)-valuation cancels between its two possible nonzero Möbius contributions. Only the terms prime to \(p\) remain. If the source already vanishes at \(p\), all terms with \(k\ge1\) are zero, so the original mask is preserved.

For scales at least one, Minkowski and the imported native moment give an inner row norm bounded by

\[
(UDL)^{\epsilon}
(1+|v|)^{A/2}p_J(W)
\left(\sqrt U+U^{1/12}X_p^{5/12}\right),
\]

after a harmless adjustment of \(\epsilon\). The two geometric sums are uniformly convergent: their factors include respectively \((Np)^{-k/2}\) and \((Np)^{-11k/12}\). The row-dependent character phases have modulus at most one, so they cause no hidden moment assumption.

A small proof-completeness issue in the initially read version was repaired in the final reviewed file. A residual scale below one can still meet a fixed annular support whose upper endpoint exceeds one. The repaired text handles such bounded nonzero scales by direct bounded-norm counting, giving \(O_W(U)\); only the smaller unsupported scales vanish. This fits the \(U\) term in (14) and avoids applying an estimate stated for \(Y\ge1\) outside its domain.

A second use of Minkowski over \(p\), the \(O(\log(2L))\) coefficient sum, and \(X_p\asymp D/L\) now give precisely

\[
\sum_u w(u)|\mathcal E_u|^2
\ll (UDL)^\epsilon(1+|v|)^A p_J(W)^2p_J(V)^2
\left[U+U^{1/6}(D/L)^{5/6}\right].
\]

The bounded-power range and source-uniformity hypotheses are stated in the note. For \(D/L\le U\), the second term is at most \(U\), so the asserted row-size moment follows. This is an actual source-dependent upper bound for the square correction. It is not an upper bound for the squarefree annular main term (11).

## 4. Separation of actual estimates from no-gain observations

The weight left on the squarefree part depends on the factorization of \(n\). Its nonnegativity or boundedness does not make it a common norm-smooth profile. The note correctly avoids transferring the native coefficient estimate to that new weight. The Gram-matrix example is only a logical counterexample to such an inference, not a claimed counterexample in the actual Hecke family.

The same-bin feedback inequality (16) is exact under its stated hypotheses: the maximum defining \(E(\lambda)\) contains the target term \(R_i+w_i(\lambda)\). Consequently division by a saturated lower bound for that same weight cannot improve \(R_i\). Refining labels or applying Hölder to bounds derived solely from the same pointwise exponents does not remove the target term. This is a no-gain statement about the specified information, not a prohibition on new signed arithmetic inequalities.

The complete convolution remains a signed sum of all divisor-length pieces. A large selected annular product need not supply a comparably large complete convolution. That missing lower bound is clearly distinguished from Proposition 1's proved upper moment and (14)'s proved correction estimate. Neither identity is described as closing the detector at a better zero-free exponent.

## 5. Limits and verdict

The principal algebraic and analytic claims listed in the disposition pass at the exact file hash above. The source inverse moment is explicitly imported rather than independently certified here. The review does not authenticate the full derivation of the critical detector class in Section 7 or the applicability of every literature comparison there; those statements remain attached to the exact upstream source and the author's separate checks.

The established new content is a complete-convolution adapter, exact defects explaining its scope, and a paid upper bound for the prime-square correction. The adapter is reversible and therefore supplies no new exponent on its own. No all-scale annular lower-coupling estimate, improved native coefficient exponent beyond the imported capped theorem, or smaller zero-free region follows from this review.
