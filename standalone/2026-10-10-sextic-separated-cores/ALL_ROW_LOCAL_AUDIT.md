# Active local factors and the extension to all coupled theta rows

Status: source-conditional local and norm adapter, independently derived
from the exact formulas listed below. The earlier proposed obstruction
from inactive exponent-zero primes is incorrect: such a prime is absent
from both the first reflection denominator and the second reflection
period. This note proves the resulting uniform support extension and
records the summable all-row norm adapter. It does not prove the moving
inner-conductor/auxiliary A2 adapter or a fourth-moment target.

Sources:

- OpenAI/math commit adc7f1241b42e322a6451854ab7e4b4c146bf78a,
  preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex.
  Local SHA-256:
  d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d.
  The exact inputs are eq:theta-local-factors, eq:reflection,
  eq:theta-row-twist, eq:ray-fourier, eq:ray-local-transform,
  the displayed full scalar following eq:dual-cusp-mellin-series,
  and lem:reflection-uniformity. These are at source lines 1730–1848,
  1973–2088, 2988–3020, 3207–3278, and 3413–3449.
- PR #920, commit 2edc467ef4dea4aa685219ac6a558a158b88768d,
  standalone/2026-10-10-theta-support-descent/ALL_CUSP_REFLECTION.md,
  Theorem 4.1. Git blob 979c54bb310fe8ec48d83d4ac118ca6a97144ff6.
  Its support theorem applies to every finite periodic multiplier,
  not only primitive characters or multipliers bounded by one.
- The same commit, RAMANUJAN_SUPPORT_PRUNING.md, Git blob
  fae954cda842026d9f9edeabf1e5cdb4c0ed9e5c,
  gives the squarefree-row version of the grouped calculation.
- The local norm calculation uses precisely the two-sieve estimate and
  the angular reciprocal input stated in Sections 4–6 of the companion
  PRUNED_COUPLED_MEAN_SQUARE.md. Its author is preparing the all-row
  theorem separately. The present calculation does not replace an
  independent review of those analytic inputs.

## 1. Local exponents, amplitudes, and inactive primes

Consider the literal coupled family
\[
\mathcal C_{A,B}(k)=\frac1{\sqrt A}\sum_{a}^{*}
 \overline{\alpha(a)}\gamma_2(a)\xi(a)\chi_a(k)
 W_1(Na/A)\,T(B;k,a).
\tag{1.1}
\]
The outer ideal is squarefree; all character powers keep their original
nonunit zeros. A surviving outer term necessarily has \((a,k)=1\).
Thus a prime of \(a\) never overlaps any prime of the row, regardless
of the row valuation. At a good prime the inner local exponent is
\[
j_p\equiv v_p(k)+4\mathbf1_{p\mid a}\pmod6.
\tag{1.2}
\]
Consequently every prime of \(a\) has \(j_p=4\). At a prime of \(k\)
one simply has \(j_p\equiv v_p(k)\pmod6\).

Write \(q=Np\), and let \(x=\lambda^4\ell\) be the integral reflected
frequency. The complete local data are:

| Row exponent modulo 6 | Active reflected factor | Its pointwise magnitude bound | Inactive branch |
|---|---|---|---|
| 1 | \(\chi_p(x)^3\) | \(1\) | none |
| 2 | \(\chi_p(x)^2\) | \(1\) | none |
| 3 | \(\chi_p(x)\) | \(1\) | none |
| 4 | \(q^{-1/2}(-1+q\mathbf1_{p\mid x})\) | \(q^{1/2}\) | none |
| 5 | \(\chi_p(x)^5\) | \(1\) | none |
| 0 | \(q^{-1/2}\chi_p(x)^4\) | \(q^{-1/2}\) | scalar \(1-q^{-1}\) |

Every active prime appears once in the first reduced denominator.
Every displayed active factor is periodic modulo \(p\). An inactive
prime contributes only the scalar in the last column; there is no
remaining frequency mask at that prime.

These assertions follow directly from the source's finite Fourier
coefficients:
\[
C_{p,0}(h)=
\begin{cases}
-q^{-1},&h\ne0,\\
1-q^{-1},&h=0.
\end{cases}
\tag{1.3}
\]
Activity is the condition \(h\ne0\), not the condition \(j_p\ne0\).
After the local transform, the active exponent-zero factor is
\(q^{-1/2}\chi_p(x)^{-2}\); the inactive Fourier coefficient has no
local transformed factor at all. In particular a sixth-power row
prime may be inactive, but does not then produce an uncancelled
period cost.

## 2. The full outer scalar has the same quadratic row twist

This subsection checks phase dependence, rather than just absolute
amplitudes. Fix an active row product
\[
R_k=\prod_{\substack{p\mid k\\p\ {\rm active}}}p,
\qquad c=c_0aR_k.
\]
The source's full scalar includes
\[
\overline{\alpha(c)}^2
\prod_{p\ {\rm active}}\chi_p(\sigma_p)^{-2}\omega_{p,j_p},
\quad
\sigma_p=\lambda^2c/p,\quad
\epsilon_p=-((\lambda^3c/p)\sigma_p)^{-1}.
\tag{2.1}
\]
Up to factors independent of the other good primes of \(c\), the
dependence of the \(p\)-factor on \(c/p\) is
\[
\chi_p(c/p)^{\,2j_p+2}.
\tag{2.2}
\]
For \(j_p\ne0,4\), this follows from the exponent
\(-2+2(j_p+2)=2j_p+2\) in
\(\chi_p(\sigma_p)^{-2}\chi_p(\epsilon_p)^{-j_p-2}\).
For \(j_p=0\), the same computation gives exponent \(2\).
For \(j_p=4\), the source has \(\omega_{p,4}=\gamma_4(p)\)
and exponent \(-2\equiv4\equiv2j_p+2\pmod6\).

At outer primes \(p\mid a\), the factors depending on \(R_k\)
therefore give \(\chi_a(R_k)^{-2}\). At active row primes the
dependence on \(a\), using even-power sextic reciprocity, gives
\[
\chi_a\!\left(\prod_{p\mid R_k}p^{2j_p+2}\right).
\]
Their product is
\[
\chi_a\!\left(\prod_{p\mid R_k}p^{2j_p}\right)=\chi_a(k)^2.
\tag{2.3}
\]
The equality holds on the surviving \((a,k)=1\) support; inactive
primes have row exponent zero modulo six and supply no missing
phase. Multiplying the original exterior \(\chi_a(k)\) gives
\(\chi_a(k)^3\).

The interactions among primes of \(a\), together with its original
\(\gamma_2(a)\), cancel exactly as in the squarefree-row coupled
calculation: the \(\gamma_2(p)\gamma_4(p)\) factors and their CRT
cross factors cancel. The angular dependence on \(a\) is
\(\overline{\alpha(a)}^3\), from the original coefficient and
\(\overline{\alpha(c)}^2\). Everything else is a fixed-ray factor,
a bounded row scalar, or a factor depending only on the chosen
row-prime branches.

If \(k=u_0sv^2\), with \(s\) squarefree, then the quadratic twist
must be read with its zeros:
\[
\chi_a(k)^3
=\chi_a(u_0)^3\chi_a(s)^3\mathbf1_{(a,v)=1}.
\tag{2.4}
\]
It is generally incorrect to replace it by the bare twist in \(s\).
The moving exclusion at \(v\) remains in the outer factor and in
the negative-allocation reciprocal series.

## 3. Exact support pruning for every row

Fix a first-reflection branch, including \(c_0\), its cusp, its
fixed additive character \(\psi\), and an active subset \(R_k\).
Keep the outer \(a\)-Ramanujan factor complete:
\[
\prod_{p\mid a}B_{p,4}(x)
=\frac1{\sqrt{Na}}\sum_{dg=a}\mu_K(g)Nd\,\mathbf1_{d\mid x}.
\tag{3.1}
\]
For a fixed \(d,g\), the entire reflected frequency sum has the
finite periodic multiplier
\[
F(x)=\psi(x)\prod_{p\mid R_k}B_{p,j_p}(x)\mathbf1_{d\mid x}.
\tag{3.2}
\]
Choose a fixed bad-prime modulus \(M\) containing the periods of
the finitely many \(\psi\). A period of (3.2) is
\[
q_2=MR_kd.
\tag{3.3}
\]
There is no factor from an inactive row prime. The first reflected
raw norm scale is
\[
X_{\rm ref}=\frac{(Nc_0)^2(Na)^2(NR_k)^2}{B}.
\]
Consequently
\[
\frac{X_{\rm ref}}{(Nq_2)^2}
=\frac{(Nc_0)^2(Ng)^2}{B(NM)^2}.
\tag{3.4}
\]
Theorem 4.1 of ALL_CUSP_REFLECTION applies to (3.2) without any
amplitude restriction. If the original weight is supported in
\([u,R_W]\), the full frequency sum is zero whenever
\[
\boxed{(Ng)^2>
\frac{3R_W(NM)^2}{(Nc_0)^2}\,B.}
\tag{3.5}
\]
There are finitely many fixed-ray/cusp choices, so one constant
\(C_S\) gives the uniform cutoff \(Ng\le C_S\sqrt B\) for every
row \(k\), not only squarefree rows.

This statement is about the complete projected frequency sum.
It is used before splitting cube indices, ramified valuations,
or frequency dyads. It asserts no vanishing for an individual
truncated piece and no reduction of the conductor after all
Ramanujan terms are reunited.

## 4. Summable repeated-row adapter for the coupled norm

The local data also remove the proposed obstacle to the norm
argument. The precise bookkeeping is as follows.

First suppose the row is primary and prime to \(S\). Write uniquely
\[
k=sv^2,\qquad s=t k_0,\qquad
t=(s,\operatorname{rad}v),\qquad (k_0,v)=1.
\tag{4.1}
\]
The ideals \(s,t,k_0\) are squarefree; \(v\) is unrestricted.
For fixed \(v,t\), the variable \(k_0\) is a squarefree row with
\[
Nk_0\le H'=\frac{H}{Nt\,(Nv)^2}.
\tag{4.2}
\]
Empty ranges are omitted. Let \(r_v\mid\operatorname{rad}v\)
be the active row primes in \(v\), and put
\[
R=Nr_v\le Nv,\qquad
Q_4=\prod_{\substack{p\mid v\\j_p=4}}Np.
\tag{4.3}
\]
Each prime of \(k_0\) is active with exponent one and produces the
same quadratic variable row factor used in the original two-sieve
lemma. The extra primes in \(v\) are fixed coefficient data.

To see the latter statement with every mask retained, make the
outer allocation \(a=efg\), then set the reflected indices
\(n=en'\), \(b=fb'\). The outer zero convention implies that
\(e,f,g\) all avoid \(v\). At a prime \(p\mid v\), the reflected
argument is a fixed unit times
\[
e\,n'\,(fb')^3.
\]
When \(j_p\ne4\), the extra \(B_{p,j_p}\) factor separates into
unit characters of \(e,f\), and a factor of \(n',b'\). When
\(j_p=4\), its divisibility indicator is exactly
\(\mathbf1_{p\mid n'b'}\), independent of \(e,f,g\). Thus after
freezing \(b'\), the extra factors are bounded separate coefficient
vectors for the two-sieve estimate, with total magnitude at most
\(\sqrt{Q_4}\). They introduce no new dependence on \(g\).
The original variable-row mask at \(k_0\) stays in the sieve.

The scalar calculation in Section 2 gives the negative allocation
the same infinity-type \(-3\) Möbius coefficient and quadratic
variable-row twist as before. Its fixed moving exclusions now
include \(v\) and \(t\), along with \(e,f\) and any permitted
original outer mask. The stated conductor-uniform angular
reciprocal input and the convergent moving-\(e\) operator in the
companion note therefore have exactly the same domain.

The reflected length in that calculation becomes
\[
Y=\frac{(H'R)^2EG^2}{BF},
\qquad EFG\asymp A,\quad
G\ll T:=\min(A,\sqrt B).
\tag{4.4}
\]
The sieve still has row length \(H'\); only the reflected length
has acquired \(R^2\). Repeating its separated-kernel estimate
therefore gives, for every fixed \(\sigma>11/12\), the block
envelope
\[
\boxed{
D^\epsilon Q_4\left[
H'A+\frac{(H'R)^2A}{B}T^{2\sigma-1}
+\left(\frac{(H'R)^2A^2}{B}\right)^{2/3}
\right].
}
\tag{4.5}
\]
This formula preserves the literal outer coefficient. Without
the angular reciprocal input the exponent of \(T\) is one, and
the original arbitrary bounded outer-multiplier scope is retained.
The common smooth-kernel separation precedes both sieve and
Mellin norm estimates, as in the companion proof.

It remains to sum the physical row strata. They are disjoint,
so this is a sum of their squared norms, not a Minkowski sum of
rows. The finitely many active choices and choices of \(t\) cost
a fixed divisor function of \(v\). Using \(R\le Nv\), the first
two terms in (4.5) have a summation weight at most
\[
\frac{Q_4}{(Nv)^2},
\]
and the third has weight at most \(Q_4/(Nv)^{4/3}\).
At a prime with \(m=v_p(v)\) and \(\delta=\mathbf1_{p\mid t}\),
\[
j_p\equiv2m+\delta\pmod6.
\]
The case \(j_p=4\) requires \(\delta=0\) and
\(m\equiv2\pmod3\), hence \(m\ge2\). Therefore an upper bound
for \(Q_4\) is \(\prod_{p^2\mid v}Np\). For each
\(\alpha\in\{2,4/3\}\), the corresponding local sum, even with a
fixed divisor weight, is
\[
1+O(q^{-\alpha})
+\sum_{m\ge2}O((m+1)^Cq^{1-\alpha m})
=1+O(q^{-\min(\alpha,\,2\alpha-1)}).
\tag{4.6}
\]
For \(\alpha=4/3\), the first possible costs are \(q^{-4/3}\)
and \(q^{-5/3}\); both are summable over prime ideals. The case
\(\alpha=2\) is stronger. There is a positive convergence margin
for any small powers used to absorb divisor-bounded branch counts.

Units supply a fixed factor. The \(S\)-supported part of a general
row changes the fixed ray data only through exponents modulo six;
its height reduction contributes convergent finite-prime geometric
sums to all three terms. Thus all nonzero element rows are included.

With the exact analytic inputs of the companion squarefree proof,
this proves the same uniform all-row envelope:
\[
\boxed{
\sum_{0<Nk\le H}|\mathcal C_{A,B}(k)|^2
\ll_\epsilon D^\epsilon\left[
HA+\frac{H^2A}{B}\min(A,\sqrt B)^{5/6}
+\left(\frac{H^2A^2}{B}\right)^{2/3}
\right].
}
\tag{4.7}
\]
The exponent \(5/6\) uses a fixed positive margin above \(11/12\),
chosen in terms of the final epsilon, exactly as in the squarefree
theorem. No bound on the endpoint line itself is asserted. The
same proof keeps a polynomial-sized original mask \((a,h)=1\).
The weaker version replaces \(5/6\) by \(1\) and tolerates the
stated arbitrary bounded outer multiplier.

## 5. What has and has not been supplied

The local audit establishes a support and norm extension for the
literal coupled family, with the companion proof's analytic inputs.
The inactive-branch denominator obstruction must not be repeated.
The nonunit mask at the square part of the row is necessary and
has been retained; a sixth-power row is never discarded.

This does not establish the different mixed family with a moving
inner exclusion \(q\), a moving additional auxiliary \(f\), or
their possible overlaps from the A2 projection. It does not
estimate the centered signed covariance produced by that projection.
Those interfaces require their own exact scalar and norm argument.
The all-row result alone therefore supplies no fourth-moment
extraction or new zero-free boundary.
