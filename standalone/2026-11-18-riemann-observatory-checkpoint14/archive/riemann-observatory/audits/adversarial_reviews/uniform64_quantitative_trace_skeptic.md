# Independent audit of the quantitative reciprocal power-trace test

18 November 2026. The proposed uniform finite cutoff holds. For fixed integers \(q\ge1\) and \(d\ge1\), put
\[
D=\max\{d,\tbinom d2\},\quad
A=(q+1)(2q+1)^{D-1},\quad n_0=4dA,\quad B=n_0\,6^{\lfloor d/2\rfloor}.
\]
For any monic integral polynomial of degree \(d\) with nonzero roots whose multiset is invariant under \(\alpha\mapsto q/\alpha\), all roots have modulus \(\sqrt q\) if and only if
\[
\sum_j \alpha_j^{n_0k}\le d q^{n_0k/2}
\quad\text{for every }1\le k\le 6^{\lfloor d/2\rfloor}.
\]
Conjugation invariance is automatic for integral coefficients. All comparisons in this version are exact integers and the test uses the stated finite progression rather than every exponent through \(B\). [Cutoff proof audited](positivity64_quantitative_trace_test.md)

## Algebraic gap and possible degeneracies

Normalize \(z_j=\alpha_j/\sqrt q\), with the positive real square root. Inversion guarantees \(R=\max_j|z_j|>1\) if at least one modulus is unequal to 1. Choose a maximal \(\alpha\) and put \(\beta=\alpha\bar\alpha=qR^2\). Both factors are integral over \(\mathbb Z\) whether or not \(P\) is irreducible. Any embedding of \(\mathbb Q(\beta)\) into \(\mathbb C\) extends to an automorphism of the splitting field of \(P\), which is normal and separable over \(\mathbb Q\). It follows that the image of \(\beta\) is a product of roots of \(P\) with modulus at most \(\beta\). This argument does not require the embedding to commute with complex conjugation. If \(\alpha\) is real then the product is the square of one root and there are at most \(d\) distinct possibilities. If \(\alpha\) is nonreal then its two factors are distinct and remain distinct under automorphisms, so there are at most \(\binom d2\) unordered product possibilities. Repetitions in \(P\) can only decrease both counts.

For \(q<\beta<q+1\), every other image \(\beta'\) satisfies \(|\beta'-q|\le |\beta'|+q\le\beta+q<2q+1\). The norm of \(\beta-q\) is a nonzero integer, so
\[
1\le|\operatorname{Norm}_{\mathbb Q(\beta)/\mathbb Q}(\beta-q)|
 \le(\beta-q)(2q+1)^{D-1}.
\]
If the degree is one the product over other embeddings is empty, and the same bound applies. For \(\beta\ge q+1\) the gap is at least 1 and needs no norm estimate. Thus in both cases
\[
\log R=\frac12\log(\beta/q)\ge
\frac{1}{2(q+1)(2q+1)^{D-1}}=\frac1{2A}.
\]
For the first case integrate \(1/(q+u)\ge1/(q+1)\) from \(0\) to \(\beta-q\); for the second integrate over \(0\le u\le1\). The integer \(n_0=4dA\) is even and \(n_0\log R\ge 2d>\log(2d)\). The smaller formula \(2(1+\lfloor A\log(2d)\rfloor)\) also works, since its value is strictly greater than \(2A\log(2d)\), even if the argument of the floor is an integer. The all-integer choice avoids needing to evaluate that floor.

The case \(d=1\) is vacuous on the off-circle side, since the sole normalized root must equal its inverse and has modulus 1. Such an integral polynomial exists only if \(q\) is a perfect square. The norm calculation also permits \(q=1\), and roots of either real sign are handled by the even exponents. The proof does not require squarefreeness, distinct real roots, or an initial trace inequality. Reciprocity remains essential for inferring an outer root from an arbitrary off-circle root. The substitution for a different radius \(\sqrt{q^w}\) requires \(q^w\) to be a positive integer, as it is for a nonnegative integer weight \(w\).

## Finite phase recurrence and strict violation

Select a phase \(\theta_j\) modulo one from each distinct nonreal conjugate root pair, so their number \(m\) is at most \(\lfloor d/2\rfloor\). Put \(v_j=n_0\theta_j\) and partition the torus into \(6^m\) half-open boxes of side \(1/6\). Among the \(6^m+1\) points \(0,v,\dots,6^m v\) two lie in the same box, so their positive index difference \(1\le k\le6^m\) gives \(\|kv_j\|_{\mathbb R/\mathbb Z}<1/6\) in every coordinate. The strict inequality follows from half-open endpoints and works even when some coordinates are rational or zero. In the empty case choose \(k=1\). At \(n=n_0k\), both phases of every nonreal pair have cosine \(>1/2\), and each real root has cosine 1, including a negative real root. The entire multiset then gives
\[
s_n=\sum_j |z_j|^n\cos(2\pi n\theta_j)>
  \tfrac12\sum_j |z_j|^n\ge\tfrac12 R^n>d.
\]
This is a single positive trace witness, and it necessarily occurs in the claimed progression. Real coefficients ensure \(s_n\) is real. The duality relation \(s_{-n}=s_n\) then makes the test polynomial \(1-X^n\) have trace form \(2d-2s_n<0\). If all roots lie on the circle, the triangle inequality instead gives \(|s_n|\le d\) for every power. The phase recurrence asserts neither a prime-index witness nor an efficient bound as a function of the degree.

## Exact implementation and finite controls

Root isolation and floating phase estimation are unnecessary. For \(P(X)=X^d+a_1X^{d-1}+\cdots+a_d\), let \(C\) be its integral companion matrix and \(J=C^{n_0}\), computed by exact integer matrix exponentiation. Compare \(\operatorname{tr}(J^k)\) to \(d(q^{n_0/2})^k\), iterating both by multiplication, for \(k=1,\dots,6^{\lfloor d/2\rfloor}\). Matrix triangularization over \(\mathbb C\) shows that traces of powers count eigenvalues with their algebraic multiplicities regardless of Jordan blocks. Newton identities yield the same integer traces. Input reciprocity can be checked exactly if needed: with \(a_d=P(0)\ne0\), test the polynomial identity \(X^dP(q/X)=a_d P(X)\). Indeed both polynomials then have the same roots with multiplicities, and their leading coefficients agree. The identity is also necessary under the reciprocal hypothesis. This validation step prevents silently applying the test to a nonreciprocal collection of roots strictly inside the disk.

An independent exact Newton replay found the first progression term already violating the bound for \(q=1,\ P=X^2-3X+1\) at \(n_0=48\) and for \(q=4,\ P=X^2-5X+4\) at \(n_0=360\). It passed all progression tests for \(q=1,\ P=X^2+1\), for \(q=1,\ P=X-1\), and for \(q=4,\ P=X+2\). These are finite controls on arithmetic and parity. The algebraic gap and pigeonhole argument prove the uniform statement.
