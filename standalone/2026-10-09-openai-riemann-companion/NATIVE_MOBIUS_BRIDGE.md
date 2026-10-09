# Exact ideal-Möbius and native Gram interfaces

Status: proposed elementary component proofs and a conditional analytic consequence, for review.

Scope: exact finite identities for the literal Möbius source; an explicit interface to the existing completed energy and NRC32 coarse covariance; no new cancellation estimate or zero-free region.

Dependencies: classical prime splitting in $\mathbb Q(\sqrt{-3})$; the frozen source files linked below; the conditional summatory hypothesis in Section 5 only.

What was actually run: the accompanying exact integer/Fraction checker, at the default ranges specified in Section 8. No upstream analytic proof, Lean build, or repository-wide validation was replayed.

Smallest remaining analytic gap: an estimate for the complete native signed quadratic form that improves its existing energy exponent, with smoothing, local factors, principal-member extraction, and every complement paid.

All labels beginning **OAI-NB26** belong only to this proposed note. They do not replace inherited claim identifiers. The finite algebra below does not assume the correctness of the imported OpenAI zero-free assertions. The associated [research programme](RESEARCH_PROGRAM.md) describes the proposed analytic work.

## 1. Source contract and notation

The upstream family works with ideals, or their normalized primary generators, in $K=\mathbb Q(\sqrt{-3})$. Its coefficient called $\mu$ is an **ideal** Möbius coefficient. Our native programme uses the ordinary integer Möbius function. The distinction is essential. The two coefficient sequences can nevertheless be connected exactly before attempting an analytic estimate.

Use the quadratic character

$$
\chi(n)=\chi_{-3}(n)=
\begin{cases}
0,&3\mid n,\\
1,&n\equiv1\pmod3,\\
-1,&n\equiv2\pmod3,
\end{cases}
$$

and define the integer norm coefficients

$$
\beta(n)=\sum_{N\mathfrak a=n}\mu_K(\mathfrak a).
$$

The sum includes **all** nonzero integral ideals, including the ramified prime above 3. Defining the coefficients by ideals avoids a unit multiplicity. A translation to primary generators must retain the upstream normalization and restore any excluded local factors.

Write

$$
M(x)=\sum_{n\le x}\mu(n),\qquad
m(x)=\sum_{n\le x}\frac{\mu(n)}n,
$$

$$
w_k=\frac1{k(k+1)},\qquad
E_X=\sum_{k=1}^X w_k M(k)^2,\qquad
u_X=\sum_{k=1}^X w_kM(k),\qquad
F_X=\sum_{k=1}^X m(k)^2.
$$

Here $X$ is a positive integer. These are the literal native source and energies in the frozen [boundary proof][boundary] and [NRC32 proof][nrc32]. This $E_X$ is not a best-approximation error carrying similar notation elsewhere in the repository. The field, primary-generator convention, and sextic-twist family are specified in the [5 October upstream source][oai003].

## 2. Exact coefficient and floor-kernel adapter

### OAI-NB26-L1 — coefficient identity, exact

With Dirichlet convolution denoted by $*$,

$$
\boxed{\quad
\beta=\mu*(\mu\chi),\qquad \mu=\beta*\chi.
\quad}
$$

Equivalently, in the absolutely convergent half-plane $\Re s>1$,

$$
\sum_{n\ge1}\frac{\beta(n)}{n^s}
=\frac1{\zeta_K(s)}
=\frac1{\zeta(s)L(s,\chi)}.
$$

**Proof.** Put $T=p^{-s}$ and inspect each rational prime. Unique factorization of ideals gives the following local polynomials:

| Rational prime | Splitting in $K$ | Local polynomial for $\beta$ | Local factor of $L(s,\chi)$ |
|---|---|---|---|
| $p=3$ | One ramified prime of norm 3 | $1-T$ | $1$ |
| $p\equiv1\pmod3$ | Two primes, each of norm $p$ | $(1-T)^2$ | $(1-T)^{-1}$ |
| $p\equiv2\pmod3$ | One prime of norm $p^2$ | $1-T^2$ | $(1+T)^{-1}$ |

The polynomial for $\beta$ is $(1-T)(1-\chi(p)T)$ in all three cases. This proves $\beta=\mu*(\mu\chi)$ coefficientwise. Multiplication by the displayed local factor of $L(s,\chi)$ leaves $1-T$, proving $\mu=\beta*\chi$. Each fixed coefficient involves finitely many factors, so the coefficient proof needs no analytic continuation. ∎

In particular, $\beta(2)=0$, $\beta(3)=-1$, $\beta(4)=-1$, and $\beta(7)=-2$. The coefficients are not the ordinary $\mu(n)$, are not one-bounded, and need not vanish at rational squares. The elementary bound $|\beta(n)|\le d(n)$ follows from the convolution identity, but it does not preserve the signed cancellation needed below.

### OAI-NB26-L2 — exact local restoration

Let $S$ be a finite set of prime ideals and let $\beta^{(S)}(n)$ denote the same norm sum restricted to ideals coprime to $S$. Define a finitely supported arithmetic function $r_S$ by

$$
\sum_d r_S(d)d^{-s}
=\prod_{\mathfrak p\in S}(1-N\mathfrak p^{-s}).
$$

Then

$$
\beta=r_S*\beta^{(S)},\qquad
\mu=r_S*\beta^{(S)}*\chi.
$$

**Proof.** The restricted ideal Euler product omits exactly the factors in the displayed finite product. Multiplying them back restores the full product. If different prime ideals have the same norm, their factors must both be retained before coefficients of equal norms are combined. ∎

For the commonly occurring condition “prime to 6,” the excluded prime ideals have norms 3 and 4: 3 ramifies and 2 is inert. Therefore, with $\delta_d$ the sequence supported at the integer $d$,

$$
\boxed{\quad
r_{(6)}=(\delta_1-\delta_3)*(\delta_1-\delta_4)
=\delta_1-\delta_3-\delta_4+\delta_{12}.
\quad}
$$

Other upstream exclusions must be restored separately. A fixed finite restoration yields finitely many explicitly rescaled kernels. If the excluded set grows with the analytic parameters, its cardinality, coefficient sizes, and rescalings become additional costs.

### OAI-NB26-L3 — ordinary $M$ as an ideal norm sum, exact

For an integer $r\ge0$,

$$
S_\chi(r):=\sum_{a=1}^r\chi(a)=\mathbf1_{r\equiv1\pmod3}.
$$

Put $\mathcal K(t)=S_\chi(\lfloor t\rfloor)$ for $t\ge0$. For every real $x\ge0$,

$$
\boxed{\quad
M(x)=\sum_{n\le x}\beta(n)\mathcal K(x/n)
=\sum_{j\ge0}
\sum_{x/(3j+2)<n\le x/(3j+1)}\beta(n).
\quad}
$$

Only finitely many inner sums are nonempty.

**Proof.** Each complete block of three character values has sum zero, while the first value in a block is 1. This proves the formula for $S_\chi$. By L1 and finite rearrangement,

$$
M(x)=\sum_{na\le x}\beta(n)\chi(a)
=\sum_{n\le x}\beta(n)S_\chi(\lfloor x/n\rfloor).
$$

The condition $\lfloor x/n\rfloor=3j+1$ is equivalent to
$3j+1\le x/n<3j+2$, which is exactly the strict-left, closed-right interval displayed above. ∎

This is a concrete common arithmetic source for comparison with the upstream ideal sum. It supplies no cancellation estimate by itself. It also uses $\beta(n)$ through $x$, so it does not reconstruct a square-step output using only the old integer prefix through $\sqrt x$. That shorter-source reconstruction is a separate Newton identity in NRC32.

## 3. Exact finite Gram and completed energy

### OAI-NB26-L4 — the native Gram after the adapter, exact

For $1\le k,n\le X$, define

$$
C_X(k,n)=\mathcal K(k/n),\qquad
D_X=\operatorname{diag}(w_1,\ldots,w_X),
$$

$$
G_X=C_X^{\mathsf T}D_XC_X,
\qquad
v_X=C_X^{\mathsf T}(w_1,\ldots,w_X)^{\mathsf T},
\qquad
\boldsymbol\beta_X=(\beta(1),\ldots,\beta(X))^{\mathsf T}.
$$

Then

$$
E_X=\boldsymbol\beta_X^{\mathsf T}G_X\boldsymbol\beta_X,
\qquad
u_X=\boldsymbol\beta_X^{\mathsf T}v_X.
$$

The completed state already used by the boundary programme is exactly

$$
\boxed{\quad
\mathcal A_X:=E_X+2(X+1)u_X^2
=\boldsymbol\beta_X^{\mathsf T}
\bigl[G_X+2(X+1)v_Xv_X^{\mathsf T}\bigr]
\boldsymbol\beta_X.
\quad}
$$

At $X=(Y+1)^2-1$, the factor $2(X+1)$ is the inherited $2(Y+1)^2$ boundary completion. This retains its rank-one term.

**Proof.** L3 says that the vector of actual partial sums is $C_X\boldsymbol\beta_X$. Substitute this vector into the definitions of $E_X$ and $u_X$, then expand the square in the completion. ∎

Two exact entry formulas make the relationship to the repository's max/floor kernels explicit:

$$
G_X(m,n)=
\sum_{r\le X/m}\sum_{s\le X/n}\chi(r)\chi(s)
\left(\frac1{\max(mr,ns)}-\frac1{X+1}\right),
$$

$$
v_X(m)=\sum_{r\le X/m}\chi(r)
\left(\frac1{mr}-\frac1{X+1}\right).
$$

Indeed, expand $C_X(k,m)=\sum_{r\le k/m}\chi(r)$ and use
$\sum_{k=q}^Xw_k=1/q-1/(X+1)$. All sums are finite; no interchange of conditional series occurs.

Alternatively, $C_X(k,m)=1$ exactly on the disjoint integer intervals

$$
m(3j+1)\le k\le m(3j+2)-1.
$$

For each pair $(j,\ell)$, set

$$
L=\max\{m(3j+1),n(3\ell+1)\},\qquad
U=\min\{X,m(3j+2)-1,n(3\ell+2)-1\}.
$$

Its contribution to $G_X(m,n)$ is $1/L-1/(U+1)$ if $L\le U$, and zero otherwise. Summing these contributions gives a second exact rational representation. Positivity of $G_X$ is immediate from its Gram construction. Positivity does not estimate the quadratic form at the signed native vector; replacing that vector by absolute values changes the observable.

### OAI-NB26-L5 — completion and reciprocal energy, exact

The inherited energies obey

$$
\boxed{\quad
F_X=E_X+(X+1)u_X^2,
\qquad
\mathcal A_X=2F_X-E_X,
\qquad
F_X\le\mathcal A_X\le2F_X.
\quad}
$$

**Proof.** Set $u_0=0$. Finite partial summation gives

$$
m(k)=u_k+\frac{M(k)}{k+1},\qquad
u_k-u_{k-1}=\frac{M(k)}{k(k+1)}.
$$

Expanding squares yields the telescoping identity

$$
m(k)^2-\frac{M(k)^2}{k(k+1)}
=(k+1)u_k^2-k u_{k-1}^2.
$$

Sum from 1 to $X$. Nonnegativity of $E_X$ and of $(X+1)u_X^2$ gives the comparison. ∎

This identity is consistent with the states already displayed in the [boundary proof, Section 4][boundary]; no priority claim is made. Its use here is practical: the completed state has the same power exponent as the monotone energy $F_X$. One need not assume that $\mathcal A_X$ itself is monotone when covering a sparse square ladder.

## 4. Exact interface to the unresolved NRC32 coarse covariance

### OAI-NB26-L6 — norm coefficients and old-prefix block means, exact

Let $Y\ge1$, $b=Y+1$, and $B=b^2-1$. For a block of integer cells $I=[a,a+h)\subseteq[b,b^2)$, write

$$
Q_I=\frac1h\sum_{k=a}^{a+h-1}m(k).
$$

Define

$$
T_I(n)=\frac1{hn}
\sum_{r\le(a+h-1)/n}\frac{\chi(r)}r
\bigl[a+h-\max(a,nr)\bigr]_+,
\qquad 1\le n\le B,
$$

where $[t]_+=\max(t,0)$. Then

$$
\boxed{\quad Q_I=\sum_{n\le B}\beta(n)T_I(n).\quad}
$$

In the old integer-prefix coordinates, the same number is

$$
\boxed{\quad
Q_I=2m(Y)-\sum_{r,s\le Y}\mu(r)\mu(s)
\frac{A_{rs}(a+h)-A_{rs}(a)}{hrs},
\quad}
$$

where

$$
A_d(t)=tH_{\lfloor(t-1)/d\rfloor}
-d\lfloor(t-1)/d\rfloor,\qquad H_0=0.
$$

**Proof of the norm-coordinate formula.** L1 gives

$$
m(k)=\sum_{n\le k}\frac{\beta(n)}n
\sum_{r\le k/n}\frac{\chi(r)}r.
$$

For fixed $n,r$, exactly $[a+h-\max(a,nr)]_+$ cells of $I$ satisfy $nr\le k$, with the stated finite bound on $r$. Averaging gives $T_I$.

**Proof of the old-prefix formula.** Put $g=\mu\mathbf1_{n\le Y}$. The finite Newton identity gives $\mu(n)=(2g-\mathbf1*g*g)(n)$ for every $n<b^2$. For $k\ge b$, reciprocal summation therefore gives

$$
m(k)=2m(Y)-\sum_{r,s\le Y}\frac{\mu(r)\mu(s)}{rs}
H_{\lfloor k/(rs)\rfloor}.
$$

For positive integers $d,t$, counting how often $1/j$ occurs proves
$\sum_{k=0}^{t-1}H_{\lfloor k/d\rfloor}=A_d(t)$. Average over the block. This is precisely the [NRC32, Section 5][nrc32] formula, with the term $-d\lfloor(t-1)/d\rfloor$ retained. ∎

For the complete NRC32 cubic mesh,

$$
S_Y=\sum_IhQ_I^2
=\boldsymbol\beta_B^{\mathsf T}
\left(\sum_IhT_IT_I^{\mathsf T}\right)\boldsymbol\beta_B,
$$

$$
F_B-F_Y=S_Y+D_Y,\qquad 0\le D_Y<5/6.
$$

The last bound is the inherited NRC32 mesh theorem, not a new estimate in this note. Orthogonality gives the exact identity for any partition; the cubic choice provides fewer than $10b$ blocks and the constant defect bound. All old-prefix product coincidences, the constant $2m(Y)$, and all coarse cross terms remain. The number of block means is not an arithmetic runtime bound.

The two representations of $Q_I$ serve different purposes. The $\beta$ version identifies the ideal source to which one could try to adapt the upstream analytic machinery. The Newton version identifies the actual old-prefix covariance that must contract. An equality of observables is not a bound transferring information from the shorter prefix.

## 5. Conditional energy exponent from the claimed strip

### OAI-NB26-C1 — explicit conditional consequence

Assume, for some fixed $1/2<\alpha<1$, that

$$
M(x)=O_\epsilon(x^{\alpha+\epsilon})
\quad\text{for every }\epsilon>0.
\tag{H_\alpha}
$$

Then

$$
E_X,F_X,\mathcal A_X=O_\epsilon(X^{2\alpha-1+\epsilon}).
$$

**Proof.** Choose the input loss small enough that $\alpha+\epsilon<1$. The summatory bound gives convergence of the Möbius Dirichlet series at 1. Its value is zero, obtained by approaching 1 from the right in $1/\zeta(s)$. Partial summation gives

$$
m(x)=\frac{M(x)}x-\int_x^\infty\frac{M(t)}{t^2}\,dt
=O_\epsilon(x^{\alpha-1+\epsilon}).
$$

Summing the resulting powers bounds $F_X$, and directly summing $M(k)^2/[k(k+1)]$ bounds $E_X$. L5 bounds $\mathcal A_X$. Rename the small losses. ∎

| Explicit summatory input | Conditional exponent of $E_X,F_X,\mathcal A_X$ |
|---|---|
| $M(x)\ll_\epsilon x^{7/8+\epsilon}$ | $3/4$ |
| $M(x)\ll_\epsilon x^{11/12+\epsilon}$ | $5/6$ |
| $M(x)\ll_\epsilon x^{1/2+\epsilon}$ | Arbitrarily small positive exponent |

The [base conditional bridge][base-bridges] explains the reciprocal-zeta growth and summation interface when starting from an all-height zero-free half-plane. This note does not treat the imported strip as established. The exact algebra in Sections 2–4 is unconditional; this section is explicitly conditional on $H_\alpha$.

## 6. Where smooth analytic estimates still fail to meet this exact kernel

The adapter specifies the source and kernel; it does not prove that the kernel lies in an upstream theorem's uniformly bounded smooth class. On a range $n\asymp D$, the ratio $x/n$ crosses roughly $x/D$ possible integer boundaries. The interval at index $j$ has length

$$
\frac{x}{3j+1}-\frac{x}{3j+2}
=\frac{x}{(3j+1)(3j+2)}.
$$

Both the number of pieces and the shortest relevant intervals depend on the scale. An assertion for one fixed smooth radial weight does not automatically handle this growing discontinuous family. Smoothing at width $\eta$ can make derivatives cost powers of $\eta^{-1}$; summing many pieces or applying Cauchy–Schwarz can consume an analytic saving. In addition, an estimate for a twisted ideal source must be uniform in every extra character, conductor, and height introduced by the decomposition.

There is a precise norm in which a proposed smoothing must be paid. For a vector $z=(z_1,\ldots,z_X)$, define

$$
\|z\|_{\mathrm{comp},X}^2
=\sum_{k=1}^Xw_k|z_k|^2
+2(X+1)\left|\sum_{k=1}^Xw_kz_k\right|^2.
$$

If $\widetilde C_X$ is a proposed smooth replacement and $R_X=C_X-\widetilde C_X$, then the triangle inequality gives the exact requirement

$$
\sqrt{\mathcal A_X}
\le \|\widetilde C_X\boldsymbol\beta_X\|_{\mathrm{comp},X}
+\|R_X\boldsymbol\beta_X\|_{\mathrm{comp},X}.
$$

The second term contains the completed boundary correction as well as the physical energy error. For the NRC32 target, the corresponding error norm is $\sum_Ih|\Delta Q_I|^2$. An estimate for one component without these terms does not bound the literal target.

The required next theorem must therefore state the smooth decomposition, its parameter-dependent seminorms, local restoration, exact endpoint treatment, surviving signed source, and a total error smaller than the proposed gain. This note leaves that theorem open.

## 7. Existing limitations that this adapter does not remove

The [base comparison][base-comparison] already identifies two decisive restrictions.

First, the fully assembled MHB32 inequality sends an input energy exponent $\kappa$ to

$$
\Phi(\kappa)=\frac{191+82\kappa}{273},\qquad
\Phi(\kappa)-\kappa=\frac{191(1-\kappa)}{273}.
$$

It worsens every seed $0\le\kappa<1$; at $3/4$ it gives $505/546$. The exact adapter does not change this exponent budget.

Second, CAP36 combined with $H_{7/8}$ gives an improved bounded-phase **difference** estimate,

$$
\|A_\tau-U_\tau\|^2
\ll_\epsilon H^4\tau^2Y^{5/4+\epsilon}
$$

under all its observation, support, anchoring, and $|\tau|\le1$ hypotheses. At output scale $X\asymp Y^2$, the exponent is $5/8$. Neither observable is bounded by that difference estimate. Existing dephasing uses a much larger phase range and does not cheaply extract the principal native member. These are the full conditions and limitations in [CONDITIONAL_BRIDGES.md, Sections 3–4][base-bridges].

Nor does the fact that L4 is a positive Gram provide the missing signed negative-mass or covariance upper bound. The boundary source already contains large positive least-prime sectors. They must cancel against other sectors before any positive-part budget is taken. An analytic transport must preserve that ordering.

## 8. Exact finite validation

Run:

```bash
python3 checks/check_native_mobius_bridge.py
```

The default run passed using exact integers and `fractions.Fraction` throughout. It checked:

| Check | Complete finite range actually run |
|---|---|
| Ordinary $\mu$ sieve versus independent norm Euler polynomials; both convolutions; local restoration; reciprocal adapter; completed-energy identities and monotonicity of $F$ | Every prefix through 512 |
| Floor identity and strict-left/closed-right interval formula | 1,539 values: $x=k,k+1/2,k+2/3$ for every $0\le k\le512$ |
| Gram entries from direct cells, signed max formula, and interval intersections; physical and completed quadratic forms | Every $1\le X\le24$, all 4,900 entries |
| Actual reciprocal block means versus norm-coefficient means versus old-prefix Newton means; exact square-step energy and mesh defect | Every $1\le Y\le12$, all 169 mesh blocks |

The checker also preserves explicit rejected shortcuts: an unrestored source coprime to 6 gives 0 in the floor sum at $x=3$, whereas $M(3)=-1$; replacing $\beta$ by $|\beta|$ gives 3 at $x=4$, whereas $M(4)=-1$; and $\beta(7)=-2$ excludes a one-bounded coefficient assumption.

These are algebra regressions and endpoint checks, not finite evidence for a new asymptotic cancellation estimate. The proofs in this note establish the identities; the checker exercises their implementation and guards against specific normalization errors. It does not independently verify the upstream papers or inherited analytic packets.

## Frozen sources

- [OpenAI family 003, 5 October manuscript][oai003], upstream commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`.
- [Boundary execution proof][boundary], source commit `72ad9bc0fecf52769d62942a8ad307efe46847ce`.
- [NRC32 proof][nrc32], source commit `0f82df3bf1d0bc669a1bbca09f8404b77c6fecde`.
- [Base conditional bridges][base-bridges] and [base repository comparison][base-comparison], PR #908 source commit `31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6`.

[oai003]: https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex
[boundary]: https://github.com/GettysburgResearch/riemann/blob/72ad9bc0fecf52769d62942a8ad307efe46847ce/standalone/2026-09-19-sylvester-boundary-execution/PROOF.md
[nrc32]: https://github.com/GettysburgResearch/riemann/blob/0f82df3bf1d0bc669a1bbca09f8404b77c6fecde/standalone/2026-09-21-native-covariance-compression/PROOF.md
[base-bridges]: https://github.com/GettysburgResearch/riemann/blob/31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6/standalone/2026-10-07-openai-quasi-riemann-import/CONDITIONAL_BRIDGES.md
[base-comparison]: https://github.com/GettysburgResearch/riemann/blob/31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6/standalone/2026-10-07-openai-quasi-riemann-import/REPO_COMPARISON.md
