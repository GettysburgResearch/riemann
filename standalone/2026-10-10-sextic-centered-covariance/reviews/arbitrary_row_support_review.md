# Independent review of the arbitrary-row support extension

**Verdict: PASS at the stated source-conditional scope.** The exact reunited negative-divisor cutoff extends to every nonzero Eisenstein row. The proof preserves the literal zeros at primes whose positive row valuation is divisible by six. It requires neither a squarefree-row Gauss cancellation nor a uniform norm bound for the varying periodic row multiplier. This verdict concerns exact support only.

## 1. Frozen source and inspected inputs

Reviewed file: ARBITRARY_ROW_SUPPORT.md, SHA-256

f859936fb555de1afd0215fa74e89ce10b8afa1b9a193e4d355be3da3f542dd5.

I read the complete file and compared it with the October 5 paper2.tex at OpenAI math pin adc7f1241b42e322a6451854ab7e4b4c146bf78a. The inspected formulas and derivations were:

- eq:theta-row-twist and its fixed bad-prime/unit discussion;
- eq:theta-local-factors and Proposition lem:reflection;
- eq:ray-fourier and the reduced-denominator argument immediately following it;
- eq:ray-additive-crt, eq:ray-local-transform, and the displayed full scalar \(C\);
- the source kernel eq:theta-weight.

The generic finite-cusp reflection and kernel composition are retained as the separately reviewed input reunited_cusp_cutoff.md, SHA-256 89cd204ae66ef615e7d630bf2c1e5524e134b76e30789dce7796a229e53a4340, Lemmas 1.1–2.2. This audit verifies the new arbitrary-row adapter to that input; it does not re-establish the imported automorphy theorem.

## 2. Arbitrary valuations and the fixed initial family

The outer factor \(\chi_a(k)\) makes every \((a,k)>1\) contribution zero before reflection. On the remaining support, all primes of the squarefree outer divisor \(a\) have local exponent four, independently of the row exponents. Thus their active status is valid even for a nonsquarefree row.

At a good row prime with positive valuation divisible by six, reducing the exponent modulo six produces

\[
\chi_p^0(n)=\mathbf1_{p\nmid n}.
\]

This is exactly the source convention. The character is not replaced by the constant function one. Raising its value to the third power in the cube part of \(T\) preserves the same zero.

The source explicitly places the unit, fixed-bad-prime, and good-prime reciprocity factors into a fixed finite family \(\Psi_0\). The note's explanation of this interface is correct. There are six row units. Bad-prime exponents can be reduced modulo six on the initial support because both original theta indices are already coprime to the fixed bad set. Their finitely many fixed-numerator characters have a common fixed ray period. Good-prime exponent reduction is accompanied by the separate nonunit masks above.

It follows that arbitrarily large row valuations do not enlarge the common bad modulus or the finite \(c_0\)-family. No exclusion of bad primes from the reflected theta support is made.

## 3. Active branches, periodicity, and scalar dependence

The source's finite Fourier coefficients satisfy

\[
C_{p,0}(0)=1-(Np)^{-1},\qquad
C_{p,0}(h)=-(Np)^{-1}\quad(h\ne0),
\]

whereas \(C_{p,j}(0)=0\) for \(j\ne0\). Thus only exponent-zero row primes can be inactive. An inactive prime contributes its zero-frequency scalar; an active exponent-zero prime contributes

\[
B_{p,0}(x)=(Np)^{-1/2}\chi_p(x)^{-2},
\]

with the additional unit factor in the source scalar. These two branches retain the original mask. The absence of an inactive prime from the second periodic multiplier is not deletion of a zero condition.

Let \(r\) be the active good row radical in a fixed branch. Since all primes of \(a\) are active and \((a,k)=1\), the first reduced denominator is \(c=c_0ra\), up to a unit. The source's full scalar and the remaining fixed ray data are independent of the Fourier index after that branch is chosen. Their dependence on \(k,a\) is permissible: the proof freezes them before expanding the outer-divisor Ramanujan product.

Only factors belonging to \(a\) are reunited. The row factors, including any row exponent-four Ramanujan factors, remain in

\[
\mathcal B_{\mathcal R}(x)=\prod_{p\in\mathcal R}B_{p,j_p}(x).
\]

Every factor is periodic modulo \(p\). For a fixed factorization \(a=hg\), the resulting full multiplier is periodic modulo \(Mrh\), where \(M\) is fixed. The source additive CRT formula gives a fixed finite period for \(\psi\); the chosen bad-prime projection adds only another fixed period.

Some row factors may be large, and the number of first branches may grow with \(k\). Neither property affects the exact support argument: it applies the finite Fourier reflection separately to each fixed multiplier and does not take an absolute-value estimate for the resulting family.

## 4. Raw kernel constants and the uniform support bound

The first raw-frequency scale is

\[
X=\frac{N(c_0)^2(Nr)^2(Nh)^2(Ng)^2}{B}.
\]

For the second finite Fourier reflection, each reduced denominator divides \(Mrh\), hence \(N(c_j)\le N(M)NrNh\). The generic reflection uses the reduced translating denominator \(c_j\); no denominator from the product of the cusp matrix with that translating matrix is substituted.

The source transform has scale constant \((2\pi)^4/27\), whereas the generic raw-frequency transform has scale constant \((2\pi)^4\). Their proved composition is therefore

\[
\mathsf J_0(\mathsf JV_*)(y)=V_*(27y).
\]

This factor \(27\) is retained correctly. The common nonzero frequency gap is \(N\ell'\ge1/81\). Consequently every outgoing argument is at least

\[
27\frac{N\ell'X}{N(c_j)^2}
\ge \frac{N(c_0)^2}{3N(M)^2}\frac{(Ng)^2}{B}.
\]

Both the active row radical and the positive divisor cancel. The finite \(c_0\)-family has a positive minimum norm, so the displayed constant

\[
C_*=\frac{3N(M)^2\,\sup\operatorname{supp}V_*}
{\min_{c_0}N(c_0)^2}
\]

is independent of the row, all its valuations, and the number of active branches.

For \((Ng)^2>C_*B\), every outgoing test is strictly beyond its support. The differentiated constant modes are zero, and the already proved composition uses its pole-free Mellin strip. Thus each branch vanishes exactly before any estimate of its scalar or finite Fourier coefficients is needed.

The argument includes units, rows supported entirely on the bad set, and rows with arbitrarily many good prime powers. It places no upper bound on \(Nk\).

## 5. Final scope

The smooth cutoff may be inserted into the reunited expression for every nonzero row, then followed by the positive \(e/f\) allocation or theta norm decompositions. The proof does not assert that an individual unmodified \(e,f,g\) summand vanishes.

The mixed row factors are retained without a uniform mean-square estimate. Accordingly this addendum does not extend the numerical squarefree-row ranges \(D^{3/4}\), \(D^{19/24}\), or the later cube-free range to arbitrary rows. It also supplies no centered covariance estimate or generalized moment theorem.

No source changes or numerical tests were made in this review. The exact support extension passes with no mathematical repair requested.

