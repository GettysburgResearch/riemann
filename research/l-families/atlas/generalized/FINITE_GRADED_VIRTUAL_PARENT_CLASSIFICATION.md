# Finite graded virtual parents: exact classification and formal escape

Status: **proposed exact local representation theorem; classical Segre,
Eulerian and symmetric-power algebra, with no novelty or global claim**.

Scope: nonnegative integer coefficient powers and finite-dimensional complex
algebraic representations of `GL_n`; universal formal character identities.

Exact source: `3c6dd97bb497d5b25c00883362fd2fff4d5f6af6`, with primitive
objects in [the source manifest](finite_graded_virtual_parent_classification.sources.json).

What is replayed: exact differential and frozen finite-difference numerators,
Sturm negative/simple-root counts, integer Euler transforms and independent
truncated product reconstruction, and rational matrix exception controls.

Smallest remaining burden: independent frozen-SHA review of this proposed
packet. An analytic or global infinite-graded parent is not constructed.

## 1. The exact question

Let `V=C^n`, with integers `n>=1` and `k>=0`, and put

\[
 h_r(A)=\operatorname{Tr}(\operatorname{Sym}^r A),\qquad
 F_{n,k}(A,T)=\sum_{r\ge0}h_r(A)^kT^r.
\tag{1.1}
\]

The power `k=0` is the polynomial convention `x^0=1`, including `x=0`.
It is not a limiting logarithmic power.

A **finite graded virtual parent** means classes
`R_1,...,R_D` in `K_0(Rep_alg(GL_n(C)))`, each a finite virtual difference,
such that

\[
 F_{n,k}(A,T)=\prod_{d=1}^D\det(1-T^dR_d(A))^{-1}.
\tag{1.2}
\]

For `R=[R_+]-[R_-]`, its factor means
`det(1-T^d R_-(A))/det(1-T^d R_+(A))`. The classes and `D` may depend on
`n,k`, but not on `A`. Equality is required for every `A in GL_n(C)`, or
coefficientwise on a Zariski-dense set of such matrices. These two versions
have the same classification.

### Theorem GLO764.FINITE_GRADED_VIRTUAL_PARENT_IFF

A finite graded virtual parent exists **if and only if**

\[
 \boxed{n=1\quad\text{or}\quad k\in\{0,1\}
        \quad\text{or}\quad(n,k)=(2,2).}
\tag{1.3}
\]

This strengthens the frozen **single-grade** obstruction: allowing arbitrary
finitely many positive grades admits precisely one further chamber, `(2,2)`.
It does not classify a factorization at one special matrix. Arbitrary extra
Frobenius operators, freely chosen scalar eigenvalues, coefficients singular
at the identity, matrix-coefficient resolvents, and regularized determinants
are outside (1.2). A group representation necessarily sends the identity to
the identity; that requirement is decisive below.

## 2. Identity numerator and a native strict interlacing proof

Write `a=n-1`. The frozen source proves

\[
 F_{n,k}(I_n,T)=\frac{H_{n,k}(T)}{(1-T)^{ka+1}},\qquad
 H_{n,k}(0)=1,\quad H_{n,k}(1)=\frac{(ka)!}{(a!)^k}>0.
\tag{2.1}
\]

For `n,k>=2`, `H` is the multiset Eulerian polynomial for `k` letters each
repeated `a` times, equivalently the diagonal Segre algebra's `h`-polynomial.

### Theorem GLO764.SEGRE_IDENTITY_NUMERATOR_SIMPLE_NEGATIVE_ROOTS

For integers `n,k>=2`, `H_{n,k}` has degree `a(k-1)` and exactly that many
distinct simple negative roots.

This is a special case of classical multiset-Eulerian root theory. The
following proof is included independently of the literature.

Let `D_T=T d/dT`. Coefficientwise,

\[
 \mathcal B_a=\prod_{j=1}^a\frac{D_T+j}{j},\qquad
 \mathcal B_a(T^r)=\binom{r+a}{a}T^r.
\tag{2.2}
\]

Applying `B_a` exactly `k` times to `1/(1-T)` gives (2.1). If before one
step the series is `H/(1-T)^d`, then the step indexed by `j` gives

\[
 \frac{Q(T)}{(1-T)^{d+1}},\qquad
 Q=\frac{[j+(d-j)T]H+T(1-T)H'}j.
\tag{2.3}
\]

In the first cycle, before step `j`, `d=j` and `H=1`, so `Q=1`. In any
later cycle, let `i>=1` be the number of complete previous cycles. Immediately
before step `1<=j<=a`, induction gives

\[
 d=ia+j,\quad m=\deg H=(i-1)a+j-1,\quad q=d-j=ia,
 \qquad q-m=a-j+1>0.
\tag{2.4}
\]

Suppose `H` has positive leading coefficient, `H(0)>0`, and simple roots
`r_1<...<r_m<0`. The coefficient of `T^(m+1)` in `Q` is `(q-m)/j` times
the leading coefficient of `H`, so it is positive. At each root,

\[
 Q(r_s)=\frac{r_s(1-r_s)}j H'(r_s).
\tag{2.5}
\]

These nonzero signs alternate. There is one zero of `Q` between every
adjacent pair, one between `r_m` and `0` since `Q(r_m)<0<Q(0)`, and one
to the left of `r_1` since the leading sign at negative infinity is opposite
to `Q(r_1)`. Thus `Q` has `m+1` distinct negative zeros; its degree is
`m+1`, so these exhaust its roots and are simple. When `m=0`, (2.3) is
`H(0)(1+qT/j)` and has the same conclusion directly. Its constant term
remains positive. Induction proves the theorem, including the exact degree.
Since `H(1)>0`, the denominator in (2.1) is not cancelled. No finite root
census is used in this proof.

## 3. Necessity of the classification

At the identity, every factor in (1.2) becomes

\[
 (1-T^d)^{-\dim R_d}.
\tag{3.1}
\]

Consequently all finite zeros and poles of the reduced rational expression
are roots of unity. Cancellation cannot create a zero elsewhere. If
`n,k>=2` and `a(k-1)>=2`, the numerator in (2.1) has at least two distinct
negative zeros. At most one can be a root of unity, namely `-1`. This
contradicts (3.1). The only remaining positive degree is `a(k-1)=1`, which
forces `(n,k)=(2,2)`.

For equality only on a Zariski-dense set, each formal coefficient of both
sides is a regular function on `GL_n`. Coefficientwise equality extends to
the identity, so the same obstruction applies. This argument does not
evaluate a rational expression at a singular non-group parameter.

### Independent coefficient-only obstruction

The frozen source also gives

\[
 q=\deg H=(k-1)a,\qquad A_1=[T]H=(a+1)^k-ka-1.
\tag{3.2}
\]

If all roots of `H` were roots of unity, `H(0)=1` would imply
`|A_1|=|sum_roots 1/root|<=q`. But

\[
 A_1-q=(a+1)^k-1-(2k-1)a>0
\tag{3.3}
\]

except when `a=1,k=2`. For `k=2` the difference is `a(a-1)`; for `k>=3`
the quadratic binomial term already exceeds `(k-1)a`, since `a>=1`.
This independently proves necessity from degree and first numerator
coefficient, without the root theorem.

## 4. Every constructive exception

For `k=0`, take `R_1=1`; for `k=1`, take `R_1=V`; and for `n=1`, take
the one-dimensional character `R_1=V^(tensor k)`. All higher grades vanish.

For `(n,k)=(2,2)`, let `delta=det A`. Then universally

\[
 \boxed{
 F_{2,2}(A,T)
 =\frac{1+\delta T}{\det(1-T\operatorname{Sym}^2 A)}
 =\frac{1-\delta^2T^2}{\det(1-T(A\otimes A))}.}
\tag{4.1}
\]

Thus take `R_1=V tensor V`, `R_2=-(det V)^2`, and `R_d=0` for `d>2`.
At distinct nonzero eigenvalues `alpha,beta`, the formula follows by summing
the three geometric terms in
`h_r(A)^2=[(alpha^(r+1)-beta^(r+1))/(alpha-beta)]^2`.
Both formal coefficients are regular on `GL_2`, so density extends the
identity to repeated eigenvalues and nondiagonalizable matrices. Equivalently
`V tensor V=Sym^2 V direct-sum det V`, which explains the second equality.
No determinant-one restriction is imposed.

## 5. The unique formal infinite-graded escape

Put `R=K_0(Rep_alg(GL_n(C)))`. For a virtual class `W` define

\[
 \sigma_t(W)=\sum_{r\ge0}[\operatorname{Sym}^r W]t^r,
 \qquad \sigma_t(U-W)=\sigma_t(U)/\sigma_t(W).
\tag{5.1}
\]

This is the usual symmetric-power operation extended multiplicatively to
the representation ring; it starts `1+Wt+...`.

### Theorem GLO764.UNIQUE_FORMAL_GRADED_VIRTUAL_ESCAPE

For every `n>=1,k>=0`, there is a unique sequence of finite virtual classes
`W_d in R` such that

\[
 \boxed{
 \sum_{r\ge0}[\operatorname{Sym}^r V]^{\otimes k}T^r
 =\prod_{d\ge1}\sigma_{T^d}(W_d).}
\tag{5.2}
\]

The product exists in the **T-adic formal** ring: any coefficient uses only
finitely many grades. Recursively, after grades below `d` have been removed,
the residual has the form `1+W_d T^d+O(T^(d+1))`. Multiplying by
`sigma_(T^d)(W_d)^(-1)` removes precisely that coefficient. This both
constructs the sequence and proves its uniqueness, without division in `R`.
Each character evaluation of (5.2) is the formal determinant product.

The first two classes are

\[
 W_1=V^{\otimes k},\qquad
 W_2=(\operatorname{Sym}^2 V)^{\otimes k}
       -\operatorname{Sym}^2(V^{\otimes k}).
\tag{5.3}
\]

Regrouping the two tensor copies, the overall flip is the product of the
factor flips. Consequently the frozen quadratic decomposition gives

\[
 \boxed{
 W_2=-\bigoplus_{\substack{S\subseteq\{1,\ldots,k\}\\
                          |S|\ge2,\ |S|\ {\rm even}}}
 \left(\bigotimes_{j\in S}\Lambda^2V\right)
 \otimes\left(\bigotimes_{j\notin S}\operatorname{Sym}^2V\right).}
\tag{5.4}
\]

For `n,k>=2`, this is the negative of a nonzero actual representation,
the quadratic relation module of the diagonal Segre presentation. In
particular

\[
 \dim W_2=-\Delta_{n,k}
 =\binom{n+1}{2}^k-\binom{n^k+1}{2}<0.
\tag{5.5}
\]

Indeed multiplication from `Sym^2(V tensor ... tensor V)` onto the degree-two
Segre piece is the projection onto the empty-`S` summand. Every other even
summand is killed, giving exactly the relation module in (5.4).

Hence no all-effective graded parent, finite **or infinite**, can reproduce
(5.2) in that chamber: uniqueness already forces a negative second grade.
The three elementary chambers have only `W_1`, while `(2,2)` has precisely
the two classes in Section 4. In every other chamber, infinitely many
`W_d` are nonzero, since a finite list would contradict Theorem (1.3).

This is not a construction of a topological vector space, convergent
determinant, completed trace, Frobenius object or global Euler product. No
analytic convergence or primewise compatibility is claimed.

### Scalar dimensions and the Euler transform

Writing `f_r=binom(r+n-1,n-1)^k`, `w_d=dim W_d`, and
`B(T)=T F'(T)/F(T)=sum_(m>=1)b_m T^m`, the exact recursions are

\[
 b_m=mf_m-\sum_{j=1}^{m-1}b_j f_{m-j},\qquad
 b_m=\sum_{d\mid m}d w_d,\qquad
 w_m=\frac1m\sum_{d\mid m}\mu(d)b_{m/d}.
\tag{5.6}
\]

The resulting integers obey `F(I,T)=product_(d>=1)(1-T^d)^(-w_d)`.
For `(2,2)`, `(w_1,w_2,w_3,... )=(4,-1,0,...)`. Negative dimensions or
a finite computed tail do not identify all virtual classes: dimension has
a kernel. The theorem of infinite nonzero representation grades follows
from (1.3), not from extrapolating a scalar list.

## 6. Exact computation, authentication, and hostile boundaries

The default rectangle is `1<=n<=4`, `0<=k<=4`, with Euler dimensions through
grade `12`. Hard maxima are `n,k<=5`, grade `16`. All public replay helpers
reject Boolean, floating, oversized, or malformed inputs before arithmetic.
Sturm arithmetic is rational, with no numerical roots or tolerances.

The differential numerator is compared to the frozen producer's independent
finite-difference routine, including its vanishing tail. Each nonconstant
numerator is checked by a rational Sturm chain: gcd with its derivative is
constant, all roots lie in `(-infinity,0)`, and no root is zero. The scalar
Euler transform is checked against a separate triangular binomial-factor
elimination and full truncated product reconstruction. Neither method uses
the root theorem. The second-grade dimension and its even-subset expansion
are checked independently. Rational rank-two controls include repeated
eigenvalues and Jordan matrices and compute `det(1-T(A tensor A))` directly
by permutation expansion.

Caps bound the enumerated scalar rows, polynomial degrees, grades, matrix
sizes and rational input bits. The additional exclusive work cap bounds
named coefficient-update loops, not CPU time, RAM or bit complexity. It is
checked before source authentication or the census; fixed hard maxima remain
binding even with a larger requested cap.

Explicitly, for one row put `e=k(n-1)`, `d=e+1`,
`q=0` if `n=1` or `k=0` and otherwise `q=(n-1)(k-1)`, and let `L` be the
requested grade. The declared row bound is

\[
 4e(q+2)+8(q+2)^3+10(L+1)^3
 +\sum_{j=0}^{2d+3}(\min(j,d)+1)+32.
\tag{6.1}
\]

The terms respectively cover differential coefficient updates, Sturm
division/normalization/sign checks, the two Euler constructions plus product
reconstruction, frozen finite-difference summands, and scalar bookkeeping.
An additional `50000` covers the five fixed matrix controls. The hard-max
rectangle has bound `1669660`, strictly below the default cap `5000000`.

Three frozen primitive files are authenticated by exact commit/blob and
LF-normalized SHA-256, with matching current bytes. The imported finite-
difference producer is authenticated **before** import. The typed manifest
must equal its compiled contract. The fixture binds note, producer, tests
and manifest via LF-normalized hashes, and binds its remaining payload by
canonical SHA-256. Its complete file is bound by the frozen Git commit.
Acceptance requires exact canonical JSON equality with recomputation, not
merely internally consistent hashes. Normal and optimized Python use the
same checks; no scientific validation uses `assert`.

```text
python -B research/l-families/atlas/generalized/finite_graded_virtual_parent_classification.py --check
python -B -O research/l-families/atlas/generalized/finite_graded_virtual_parent_classification.py --check
python -B -m unittest tests.test_finite_graded_virtual_parent_classification
python -B -O -m unittest tests.test_finite_graded_virtual_parent_classification
```

The infinite interlacing theorem, generic representation quantifier and
formal-ring recursion are proved in prose; the bounded census does not
machine-prove them or any analytic/global statement. RH and GRH remain open.

## 7. Established literature and programme meaning

The numerator and quadratic relations are classical Segre algebra:
Marcel Morales, [*Segre embeddings, Hilbert series and Newcomb's problem*](https://arxiv.org/pdf/1306.6910),
Theorem 6 identifies the multiset-Eulerian numerator, Corollary 1 gives its
degree, and Corollary 4 gives the number of quadratic relations, exactly
`Delta_(n,k)` in the equal-factor case. The relevant sections of the paper
were read; it is a literature comparison, not a machine-authenticated input.

Simple negative zeros belong to Rodica Simion's established multiset
Eulerian theory: [*A multiindexed Sturm sequence of polynomials and
unimodality of certain combinatorial sequences*](https://doi.org/10.1016/0097-3165(84)90075-X),
JCTA 36 (1984), 15--22. The publisher's metadata/abstract was checked;
the full article was not obtained. The elementary proof in Section 2 is
self-contained. The graded symmetric-power product is ordinary formal
lambda-ring/plethystic algebra, not a new analytic regularization.

The programme contribution is the exact **finite-graded representation
boundary** beyond the frozen single-grade no-go, together with the precise
formal escape and its obligatory negative relation module. It closes a
finite-parent alternative; it does not prove that an infinite categorical
parent has any L-function, completion, automorphic or RH-facing meaning.
