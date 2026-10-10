# Moving column exclusions through literal sixth-power row twists

**Status:** proposed source-qualified component theorem. This note supplies the moving original column exclusion missing from the positive two-axis adapter. It preserves every nonzero element row, the fourth-power auxiliary, all overlaps, and every zero-extended local character. It does not estimate a centered signed covariance.

**Inputs and pins:** PR #921, commit 4e6d4aa57ae4cb04d76b2b31279ac367951b469a, especially ARBITRARY_ROW_MOMENTS.md (SHA-256 a12605808006c07f1a413e743545441e0541577367c8ea1bbe09a7fc493cc52a), its Sections 2–8, and CUBE_INVERSE.md; the imported October 5 paper2.tex at OpenAI/math commit adc7f1241b42e322a6451854ab7e4b4c146bf78a, equations theta-local-factors, theta-row-twist, ray-local-transform and the complete reflection scalar. The additional local calculation here uses the actual active exponent-zero factor, rather than its weaker modulus-one bound.

## 1. Exact objects and quantifiers

Work over the Eisenstein field with the same fixed bad set S, primary generators, additive character, normalized cubic Gauss factor, and fixed finite ray character \(\xi\) as in the pinned sources. Put
\[
a_\xi(n)=\alpha(n)^{-1}\gamma_2(n)\xi(n).
\]
All column indices below are primary and outside S. Let \(q_0,f\) be squarefree primary ideals outside S. A general exclusion may be replaced by its radical. Define
\[
\begin{split}
p_{q_0}(A,B;k,f)
={1\over\sqrt{AB}}
\sum_{\substack{an\ {\rm squarefree}\\(an,q_0S)=1}}
a_\xi(an)\chi_{an}(kf^4)
W_1(Na/A)W_2(Nn/B).
\end{split}                                                    \tag{1.1}
\]
Here \(k\) is an arbitrary nonzero element. The fixed smooth tests have compact support in \((0,\infty)\).

Let \(P_{A,B}\) and \(\mathcal C_{A,B}\) be the normalized literal and theta-completed objects of PR #921, ARBITRARY_ROW_MOMENTS.md (1.1). Set
\[
c_{q_0}(A,B;k,f)=\mathcal C_{A,B}(kf^4q_0^6).                  \tag{1.2}
\]
The cube index in (1.2), as well as its squarefree indices, retains its zero extension at \(q_0\).

Fix \(\beta\in(1/2,1]\) and assume the exact uniform angular scalar premise of that note, equation (1.2), for
\[
\mu(g)\eta(g)\alpha(g)^{-3}\chi_s(g)^3
\]
with squarefree \(s\), polynomially bounded moving exclusions, and the specified fixed finite family of \(\eta\). Its counting version is \(\beta=1\); the \(\beta=11/12\) specialization retains the stated imported canonical/angular input. The classical theta and quadratic/cubic upper-sieve inputs in PR #921 are also retained.

Throughout, \(D\ge2\), \(1\le A,B,H,Nq_0,Nf\le D^{C_0}\), with fixed \(C_0\). A nonempty child scale in a fixed bounded interval below one is allowed with constants depending on the test support. Every estimate has a fixed finite smooth-seminorm loss, uniform over these parameters. No uniformity in \(\beta\) as \(\beta\downarrow1/2\) is claimed.

Write
\[
q=q_0/(q_0,f),\qquad Q=Nq,\qquad F=Nf,\qquad
J=FQ,\qquad K=F^{2/3}Q^{1/3},
\qquad \delta={2\beta-2\over3}.                              \tag{1.3}
\]
In particular \(K\le J^{2/3}\). The letter K in (1.3) is an energy multiplier, not the number field.

### Theorem 1.1. Quantitative moving-mask adapter

Uniformly with the preceding quantifiers,
\[
\boxed{
\sum_{k\sim H}|c_{q_0}(A,B;k,f)|^2
\ll D^\epsilon\left[
HA+{JH^2A\over B}\min(A,\sqrt B)^{2\beta-1}
+K\left({H^2A^2\over B}\right)^{2/3}
\right],
}                                                            \tag{1.4}
\]
and
\[
\boxed{
\sum_{k\sim H}|p_{q_0}(A,B;k,f)|^2
\ll D^\epsilon\left[
HA+JH^2AB^\delta+KH^{4/3}A^{4/3}B^\delta
\right].
}                                                            \tag{1.5}
\]
The row annulus contains all nonzero elements. The same bounds hold for sharp balls and fixed Schwartz row profiles. For (1.5), a fixed smooth two-variable test \(V(Na/A,Nn/B)\) is also permitted, with finitely many seminorms.

## 2. The exclusion is exactly a sixth-power twist

For every squarefree column n and every element x,
\[
\chi_n(q_0^6)=\mathbf1_{(n,q_0)=1},\qquad
\chi_n(xq_0^6)=\chi_n(x)\mathbf1_{(n,q_0)=1}.                 \tag{2.1}
\]
This follows prime by prime. The sixth power is one on units and remains zero at a nonunit. Therefore
\[
p_{q_0}(A,B;k,f)=P_{A,B}(kf^4q_0^6)
                =P_{A,B}(kf^4q^6).                         \tag{2.2}
\]
The last equality holds because \(p\mid f\) already forces zero at every column containing p, so adding a sixth power at that prime is redundant. The same identity holds for the completed object in (1.2): its cube factor has the literal row character \(\chi_b(k)^3\), and
\[
\chi_b(q_0^6)^3=\mathbf1_{(b,q_0)=1}.
\]
Thus the completion deletes the required cube primes as well. It is not the completion with a missing cube-index mask.

The cube inverse commutes with this exact row replacement. Its inverse coefficient becomes
\[
{\mu(h)\alpha(h)^{-3}\xi(h)^3\chi_h(kf^4q^6)^3\over Nh},
\]
which retains \((h,fq)=1\) by zero extension. The original outer mask remains \((a,h)=1\). No new restriction between h and a reflected theta index is introduced.

## 3. A deleted prime absent from the physical row

Fix \(p\mid q\), let \(q_p=Np\), and first take physical rows with \(p\nmid k\). The reflected local exponent of \(kf^4q^6\) at p is zero, but its original character is the nonunit mask. There are exactly the source's active and inactive alternatives.

The inactive alternative has scalar \(1-q_p^{-1}\), omits p from the reflection denominator, and introduces no frequency factor. The active alternative has a modulus-one local Gauss scalar and
\[
B_{p,0}(x)=q_p^{-1/2}\chi_p(x)^{-2},                       \tag{3.1}
\]
while the squared conductor contributes \(q_p^2\) to the effective theta length.

The exact mixed scalar identity in PR #921 gives exponent \(2j+2=2\) at this active prime, which becomes \(3j=0\) after the outer Gauss factor and row twist are combined. Consequently p introduces no new character in either Möbius scalar, apart from its required exclusion. The fixed bad-ray and reciprocity data still range over the original finite family.

After the outer positive allocation, the frequency is
\[
x=u_\theta\lambda^{m+4}e n_S n_0(f_1b')^3,
\]
where the outer allocation \(a=ef_1g\) is coprime to p. Here \(f_1\) is an allocation label, distinct from the auxiliary f. Equation (3.1) separates as a fixed phase times
\[
q_p^{-1/2}\chi_p(e)^{-2}\chi_p(n_0)^{-2}
\mathbf1_{p\nmid b'}.                                     \tag{3.2}
\]
Every zero in (3.2) is retained. The factors in e and \(n_0\) are separate bounded coefficients permitted by the quadratic–cubic norm. Freezing the full cube index leaves its indicator intact. The scalar variables g and h acquire no theta-column dependence.

Relative to the block before p is inserted, the two exact amplitude/length pairs are

| Branch | Squared amplitude | Effective length |
|---|---:|---:|
| Inactive | \((1-q_p^{-1})^2\) | \(1\) |
| Active | \(q_p^{-1}\) | \(q_p^2\) |

Apply these to the three nonnegative block monomials \(H_0E,Y,(EY)^{2/3}\). Minkowski over the two branches gives local costs bounded by
\[
\begin{aligned}
\bigl(1-q_p^{-1}+q_p^{-1/2}\bigr)^2&\ll1,\\
\bigl(1-q_p^{-1}+q_p^{1/2}\bigr)^2&\ll q_p,\\
\bigl(1-q_p^{-1}+q_p^{1/6}\bigr)^2&\ll q_p^{1/3}.
\end{aligned}                                               \tag{3.3}
\]
Thus the deleted-prime costs are \(1,q_p,q_p^{1/3}\), with no pointwise-conductor estimate added to the angular scalar premise.

## 4. Physical rows that already contain a deleted prime

Now let \(p\mid q\) and \(v_p(k)=\nu\ge1\). Adding \(q^6\) changes neither the local exponent modulo six nor the original zero mask. We therefore use the same local row branches as the unshifted all-row proof, fixing this physical valuation and removing p from the variable squarefree row.

The squared amplitude can be bounded by
\[
q_p^{\mathbf1_{\nu\equiv4\ (6)}},
\]
with the active/inactive squared branch factor
\[
4^{\mathbf1_{\nu\equiv0\ (6)}}.
\]
The physical row height is divided by \(q_p^\nu\), not by the artificial sixth power. The active radical contributes at most p to the denominator. The three valuation sums are consequently bounded by
\[
\begin{aligned}
\sum_{\nu\ge1}4^{\mathbf1_{\nu\equiv0\ (6)}}
q_p^{\mathbf1_{\nu\equiv4\ (6)}-\nu}&\ll q_p^{-1},\\
\sum_{\nu\ge1}4^{\mathbf1_{\nu\equiv0\ (6)}}
q_p^{\mathbf1_{\nu\equiv4\ (6)}+2-2\nu}&\ll1,\\
\sum_{\nu\ge1}4^{\mathbf1_{\nu\equiv0\ (6)}}
q_p^{\mathbf1_{\nu\equiv4\ (6)}+4/3-4\nu/3}&\ll1.
\end{aligned}                                               \tag{4.1}
\]
These are six geometric progressions. Their largest exponents occur at \(\nu=1\), giving respectively \(-1,0,0\); the exceptional amplitude at \(\nu=4,10,\ldots\) and branch factor at \(\nu=6,12,\ldots\) are present in (4.1).

The sectors with distinct physical valuations are disjoint, so their energies add. Combining (4.1) with (3.3) gives the same costs \(O(1),O(q_p),O(q_p^{1/3})\), including all physical row overlaps with the deleted prime.

At primes of f, use the already proved three-way exponent-four reindexing of PR #921, Corollary 7.2. It gives \(1,Np,(Np)^{2/3}\), including all positive physical valuations. The sets of primes of f and q are disjoint by (1.3). All other repeated row primes have the convergent Euler weights proved in that note; bad-prime powers are geometric and the six unit rows remain included.

## 5. Global composition and the inverse

Multiplying the local costs gives precisely \(1,J,K\). The fixed per-prime branch constants cost
\[
C^{\omega(fq)}\ll_\eta (FQ)^\eta,
\]
which is absorbed in \(D^\epsilon\) after the preliminary exponents are chosen. No uniformly bounded Euler product is asserted for these branch constants.

The exact second-reflection cutoffs in PR #921 apply to the substituted row, hence remain
\[
G^2\ll B,\qquad G^2Z^3\ll B
\]
for the completion and its cube inverse. They are inserted into the reunited sums before any positive allocation is separated. The inactive/active expansion at a deleted prime does not change the scalar variables in either cutoff.

The complete-cusp block estimates therefore become
\[
D^\epsilon G^{2\beta-2}
[H_0E+JY+K(EY)^{2/3}]
\]
and
\[
D^\epsilon G^{2\beta-2}Z^{2\beta-2}
[H_0E+JY+K(EY)^{2/3}],
\]
with the unshifted effective lengths used to define Y. Each local reindexing has already been absorbed into the displayed energy multiplier. The powers of g, h and the common-divisor corrections are unchanged.

In particular, the three norm costs used to separate the two Möbius scalars remain
\[
(Nd)^{-\beta-1/2},\quad (Nj)^{-\beta-1/2},\quad
(N\ell)^{-2\beta}.
\]
They are summable for \(\beta>1/2\). The shared label \(\ell\) may still intersect the remaining positive variable. Every scalar exclusion now additionally contains q, exactly as supplied by the row substitution.

The same \(E,F_1,G\) optimization as in PR #921 proves (1.4); the same \(E,F_1,G,Z\) optimization proves (1.5). Here \(F_1\) denotes the allocation scale. Thus the additional deleted-prime costs are attached to the existing three energy terms without changing their scale powers.

All transformations occur on full theta sums before truncation. Ratios and smooth partitions are rescaled with their effective lengths, as in the pinned proof. Polynomial bounds on \(q_0,f\) preserve the fixed finite seminorm order and all polynomial conductor ceilings.

## 6. General tests and row profiles

For a fixed compactly supported smooth two-variable V, choose one-variable cutoffs equal to one on its support and apply Mellin inversion in both normalized coordinates. Its Mellin transform decreases faster than any prescribed polynomial in the two imaginary variables, by repeated integration by parts. The one-variable tests multiplied by the Mellin phases have seminorms bounded polynomially in those variables. Minkowski and absolute integration of the rapidly decreasing transform therefore transfer (1.5) to V. No arithmetic column coefficient is changed. Swapping the two axes is legitimate for the literal polynomial, with the transposed test.

Sharp norm balls follow by summing inward annuli: the three row powers are \(H,H^2,H^{4/3}\). For a fixed Schwartz row weight, the annulus \(2^jH\le Nk<2^{j+1}H\) is estimated with reference \(D_j=2^jD\), leaving \(A,B,q_0,f\) fixed. A common fixed polynomial ceiling still applies. The preliminary loss \(2^{j\epsilon_0}\) and the largest row power \(2^{2j}\) are absorbed by decay of order \(M>2+\epsilon_0\). This proves the stated profiles without applying a fixed-D estimate beyond its parameter range.

## 7. Meaning and limit

The new result is a uniform positive norm for the actual original exclusion and fourth-power auxiliary, with costs
\[
\boxed{
J=Nf\,N(q_0/(q_0,f)),\qquad
K=(Nf)^{2/3}N(q_0/(q_0,f))^{1/3}.
}
\]
It includes all overlaps among physical rows, the auxiliary, and the deleted primes. It is not inferred by treating column deletion as a contraction of a character-sum norm.

The companion A2 note uses this exact dependence when a correction enlarges both the exclusion and the auxiliary. The signed first-Poisson covariance still has independently corrected columns and its original coupled kernel. Theorem 1.1 alone supplies no bound for that centered form or the full moment hierarchy.
