# Weighted Hardy repair of the auxiliary operator classification

2026-11-17. Independent derivation by `/root/li_skeptic`; root and equivalences report separate matching reconstructions. This is a mathematical repair of the operator statement inspected in **PAPER-E012**, not a claim about the paper's main zero-free-region results or historical novelty. The exact published endpoint counterexample and source versions are documented in `gallardo_seco_endpoint_skeptic_round4.md` in this directory. No part of the following argument relies on the source's asserted Riesz-basis construction.

## Result, including endpoint

Let `alpha<-1` and `a>0` be fixed, and use the actual coefficient spaces

\[
 D_\gamma=\{f=\sum_{n\ge0}f_nz^n:
                  \sum_{n\ge0}|f_n|^2(n+1)^\gamma<\infty\}.
\]

Set `p=-(alpha+1)/2>0` and

\[
 T_af=f'-\frac{af}{1-z}:D_{\alpha+2}\longrightarrow D_\alpha.
\]

Then:

1. `T_a` is bounded for every `a>0`.
2. If `a>p`, it is a bounded bijection with bounded inverse.
3. If `0<a<p`, it is surjective, has one-dimensional kernel `span{(1-z)^(-a)}`, and has a bounded right inverse.
4. If `a=p`, it is injective with proper dense, nonclosed range. An explicit target outside its range is given below.

In particular, on the source's stated range `alpha in[-3,-2)`, the bounded-bijection condition is **strictly** `a>-(alpha+1)/2`. This proof also covers the slightly broader range `alpha<-1`; that broader scope is an independently proved extension, not a quotation of the source. Constants throughout may depend on the fixed `alpha,a`; no uniformity near the threshold is asserted.

## 1. A weighted Schur estimate and boundedness

For each `q>0` and integer `n>=1`,

\[
 \sum_{k=1}^n k^{q-1}\le C_q n^q,
 \qquad \sum_{k=n}^\infty k^{-q-1}\le C_q n^{-q},
 \quad C_q=1+1/q.
 \tag{H1}
\]

Both estimates follow by separating the first term and comparing with the elementary integral; the stated constants work for all indices, not merely asymptotically.

Write `f=sum_(n>=0)f_nz^n`. Differentiation is bounded `D_(alpha+2)->D_alpha`, since its squared norm is `sum_(n>=1)|f_n|² n^(alpha+2)`, and `n^(alpha+2)` is comparable to `(n+1)^(alpha+2)` uniformly for `n>=1`.

For multiplication by `(1-z)^(-1)`, conjugating the domain and range coefficient norms to ordinary `ell²` gives the positive matrix, indexed by integers `1<=k<=n`,

\[
 A_{nk}=n^{\alpha/2}k^{-(\alpha+2)/2}
       =n^{-p-1/2}k^{p-1/2}.
\]

Use Schur weights `w_n=n^(-1/2)`. By(H1),

\[
 \sum_{k\le n}A_{nk}w_k
 =n^{-p-1/2}\sum_{k\le n}k^{p-1}
 \le C_p w_n,
\]

\[
 \sum_{n\ge k}A_{nk}w_n
 =k^{p-1/2}\sum_{n\ge k}n^{-p-1}
 \le C_p w_k.
\]

Schur's test makes this multiplier bounded, with norm at most `C_p`. Therefore `T_a` is bounded on exactly the displayed domain. Each weighted coefficient space defines holomorphic functions in the disk, since its point evaluations converge by Cauchy–Schwarz against a geometric series. Thus the coefficient construction below produces legitimate analytic functions.

## 2. Exact recurrence and homogeneous solution

For a target `g=sum_(n>=0)b_nz^n`, put

\[
 B_n=b_{n-1}\ (n\ge1),\quad
 P_n=\frac{(a+1)_n}{n!},\quad
 c_n=\frac{(a)_n}{n!},\quad P_0=c_0=1.
\]

For a candidate `f`, let `S_n=sum_(k=0)^n f_k` and `u_n=S_n/P_n`. Taylor coefficient comparison in `T_af=g` is equivalent to

\[
 n f_n-aS_{n-1}=B_n\quad(n\ge1).
\]

The identities `P_n/P_(n-1)=(n+a)/n` and `P_n-P_(n-1)=c_n` yield the exact equivalent recurrence

\[
 u_n-u_{n-1}=\frac{B_n}{nP_n},
 \qquad f_0=u_0,\qquad
 f_n=c_nu_n+\frac{B_n}{n+a}\quad(n\ge1).
 \tag{H2}
\]

Conversely, defining `u_n` by its recurrence and `f_n` by(H2) gives `S_n=P_nu_n` by telescoping, so it solves every coefficient equation. There is no asymptotic replacement in this step.

The only analytic homogeneous solutions are `C(1-z)^(-a)`, either by(H2) or by integrating `((1-z)^af)'=0`. The fixed-parameter gamma-ratio asymptotics give constants `0<m_a<=M_a<infinity` such that for **all** integers `n>=1`,

\[
 m_a n^a\le P_n\le M_a n^a,
 \qquad m_a n^{a-1}\le c_n\le M_a n^{a-1}.
 \tag{H3}
\]

Asymptotics plus the finitely many initial positive ratios prove the global inequalities; no initial-index exception is discarded. Consequently `(1-z)^(-a)` belongs to `D_(alpha+2)` exactly when

\[
 \sum_{n\ge1}n^{2a+\alpha}<\infty,
 \quad\text{that is, }h:=a+(\alpha+1)/2<0.
 \tag{H4}
\]

This proves injectivity for `h>=0` and the one-dimensional kernel assertion for `h<0`.

## 3. Supercritical case: bounded future-tail inverse

Assume `h>0`. Cauchy–Schwarz and(H3) show that

\[
 \sum_{k\ge1}\frac{|B_k|}{kP_k}
 \le C_a\left(\sum|B_k|^2 k^\alpha\right)^{1/2}
          \left(\sum k^{-2h-1}\right)^{1/2}<\infty.
\]

Choose

\[
 u_0=-\sum_{k\ge1}\frac{B_k}{kP_k},\qquad
 u_n=-\sum_{k>n}\frac{B_k}{kP_k}.
 \tag{H5}
\]

The constant coefficient `f_0=u_0` is a bounded linear functional of `g` in `D_alpha`. It remains to control `c_nu_n` in the domain norm. After conjugating the coefficient weights to `ell²`, (H3) bounds the absolute matrix entries by a fixed constant times

\[
 H^{(+)}_{nk}=n^{h-1/2}k^{-h-1/2}1_{k>n},
 \qquad n,k\ge1.
\]

For `w_n=n^(-1/2)`,

\[
 \sum_{k>n}H^{(+)}_{nk}w_k
 =n^{h-1/2}\sum_{k>n}k^{-h-1}
 \le h^{-1}w_n,
\]

\[
 \sum_{n<k}H^{(+)}_{nk}w_n
 =k^{-h-1/2}\sum_{n<k}n^{h-1}
 \le C_h w_k.
\]

Hence Schur's test bounds this tail operator by `sqrt(C_h/h)`, apart from the fixed(H3) constants. The direct term `B_n/(n+a)` in(H2) is bounded into the domain since `n/(n+a)<=1`, with only the harmless equivalence between `n` and `n+1` in the weights. Thus the constructed `f` belongs to `D_(alpha+2)` and satisfies `||f||_(alpha+2)<=C_(alpha,a)||g||_alpha`. The exact recurrence proves `T_af=g`; injectivity from(H4) proves this is the unique bounded inverse.

## 4. Subcritical case: bounded past-prefix right inverse

Assume `h<0`, and write `q=-h>0`. Choose `u_0=0` and

\[
 u_n=\sum_{k=1}^n\frac{B_k}{kP_k}.
 \tag{H6}
\]

The conjugated matrix for `c_nu_n` is bounded by a fixed multiple of

\[
 H^{(-)}_{nk}=n^{-q-1/2}k^{q-1/2}1_{k\le n}.
\]

By(H1), both weighted Schur sums with `w_n=n^(-1/2)` are at most `C_q` times the corresponding weight. The direct term in(H2) is again bounded. Therefore(H6) gives a bounded right inverse for every target `g`. The homogeneous solutions in(H4) show its kernel has exactly dimension one. No bounded-bijection claim is made in this case.

## 5. Critical case: an explicit target outside the range

Now assume `h=0`, equivalently `alpha=-2a-1`. Set, for `n>=0`,

\[
 b_n=\frac{(n+1)P_{n+1}}{(n+2)\log(n+2)}.
 \tag{H7}
\]

These positive coefficients have polynomial growth and define a holomorphic disk function. By(H3), `b_n=O((n+1)^a/log(n+2))`, so

\[
 \sum|b_n|^2(n+1)^\alpha
 \ll\sum\frac1{(n+1)\log^2(n+2)}<\infty.
\]

Any analytic preimage must satisfy the exact(H2) recurrence, now giving

\[
 u_n=u_0+\sum_{j=2}^{n+1}\frac1{j\log j}.
\]

Its real part tends to positive infinity for every complex choice of `u_0`. Since `c_n>0` and the direct term in(H2) is also positive real for this target, eventually `|f_n|>=c_n`. But(H3) implies

\[
 \sum_{n\ge1}|f_n|^2(n+1)^{\alpha+2}
 \ge C\sum_{n\text{ large}}n^{2a+\alpha}
 =C\sum_{n\text{ large}}n^{-1}=\infty.
\]

Thus no analytic preimage lies in the stated domain. At `a=1,alpha=-3`, (H7) is precisely the elementary target `b_n=(n+1)/log(n+2)` in the independent source review.

The range is nevertheless dense. For a polynomial `q`,

\[
 T_a[(1-z)q]=(1-z)q'-(a+1)q.
\]

On polynomials of degree at most `m`, this is triangular with nonzero diagonal entries `-(a+j+1)`, `0<=j<=m`. Therefore every polynomial is the image of an element of `(1-z)P`, which is contained in the domain. Polynomials are dense in `D_alpha` by coefficient truncation. The range is proper by(H7), hence dense and nonclosed; injectivity was proved in(H4).

As another exact diagnostic, the truncated homogeneous series `sum_(n=0)^K c_nz^n` has domain norm squared comparable to `log K` and image norm squared bounded at `h=0`. This agrees with the failure of a bounded inverse onto a closed range.

## 6. Optional invertible multiplier and fair interpretation

If `M_h` is a bounded invertible multiplier on the target, composition `T_(a,h)=M_hT_a` has precisely the same injectivity, surjectivity and closed-range classification. The source's bounded analytic `h` bounded away from zero has this property for its negative `alpha`: the equivalent weighted Bergman integral norm follows from `B(n+1,-alpha)` being comparable to `(n+1)^alpha`; both `h` and `1/h` are bounded multipliers in that integral norm. Thus the optional multiplier does not repair equality.

The verified contradiction is anchored to the **printed inclusive endpoint** of auxiliary Proposition5.1 in both inspected versions. The strict replacement and complete classification above are independently written repairs using elementary weighted Hardy estimates. They do not by themselves decide how to repair any later closure equivalence: a dense nonclosed injective operator need not transfer norm-closure equivalences through its inverse. That downstream question must be checked separately. No author was contacted, and no public claim about the paper as a whole is made.
