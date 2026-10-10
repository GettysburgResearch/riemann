# Independent review of the reunited-divisor support cutoff

**Verdict: PASS, conditional on the explicitly named source inputs.**

The exact finite-cusp reflection and the support cutoff in reunited_cusp_cutoff.md are correct for the byte-bound snapshot below. The smooth insertion of the cutoff before the positive allocations are separated is also valid. Conditional on the previously reviewed angular component estimate, the standard-cusp consequence with row range \(H\le D^{19/24}\) follows.

This review independently checks the new transformation and cutoff. It does not certify the imported paper's global main theorem, replace an audit of the quadratic/cubic large sieves, or prove a full fourth moment, a centered covariance bound, or the generalized \(2k\)-th moment hierarchy.

## 1. Reviewed bytes and dependency boundary

The primary reviewed file is:

| File | Bytes | SHA-256 |
|---|---:|---|
| reunited_cusp_cutoff.md | 18,983 | 89cd204ae66ef615e7d630bf2c1e5524e134b76e30789dce7796a229e53a4340 |

The companion and imported files read in this audit are:

| File | SHA-256 |
|---|---|
| double_reflection_attack.md | b00bcc186dc830daf62341ac2d5cd80c202ceb5af05f09c043725486e8f5588d |
| centered_a2_attack.md | bbc139f956731482fcf9e33645bfe2832b7b7471594d9cbc1f21cd08eaf2ac5a |
| Imported October 5 build/paper2.tex | d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d |
| PR #915 COUPLED_THETA_COMPLETION.md | 602f1e9aede5a6f1fafe08f1b1f0182a1b27103ab740838d793e7a66d753001d |
| PR #915 REFLECTION_SCALAR_AUDIT.md | 630afa6d7e762c8b62017c988b71575b441dca477ec37afb4b2e22059505da77 |

The imported paper is pinned to OpenAI/math commit adc7f1241b42e322a6451854ab7e4b4c146bf78a. The adjacent PR #915 source pin is 9959364671f89b86f3992ec5ed5e19f804eb607b. The checked files contain no control bytes other than line feeds.

The exact-cutoff proof uses only the following imported analytic/arithmetic interfaces: scalar theta automorphy on \(\Gamma(3)\); the stated \(\mathrm{SL}_2(\mathbb Z)\) and \(\mathbb Z+3\mathcal O\) invariances; the three source cusp expansions and their cubic support/coefficient bounds; the source's order-one gamma kernel; and the literal mixed \(j=1,4\) first reflection with its scalar cancellation. Relevant source labels are eq:theta-cusp-representatives, eq:cusp-coefficient-definition, eq:theta-local-factors, eq:reflection, eq:theta-cusp-automorphy, eq:theta-cusp-coordinates, eq:ray-local-transform, and eq:dual-cusp-mellin-series.

The quantitative corollary additionally uses centered_a2_attack.md, Theorem 7.1, at the hash above. That theorem is an explicit previously reviewed input to this audit; its zero-free and sieve arguments are not re-certified here.

## 2. Finite-cusp closure: PASS

Finite index alone would establish a finite collection of functions up to scalar, but would not by itself establish the specific frequency gap \(1/81\). The note supplies the missing explicit reduction.

For an arbitrary \(A\in\mathrm{SL}_2(\mathcal O)\), right multiplication by a unit diagonal matrix makes the upper-left entry \(1\pmod3\) if the lower-left entry is divisible by \(\lambda\), and otherwise makes the lower-left entry \(1\pmod3\). This is possible because all six units of \(\mathcal O\) give distinct representatives of \((\mathcal O/3)^\times\). A subsequent right integral translation kills the upper-right or lower-right residue, respectively. The determinant then supplies the other needed residue.

Consequently the displayed factorization

\[
A=\gamma H T_{-t}D_u^{-1},\qquad \gamma\in\Gamma(3),
\]

is valid, with \(H,t,u\) in fixed finite sets. Choosing actual representatives \(H_\tau\) from the resulting matrices gives the matrix factorization needed in the second reflection.

The finite list of \(H\)'s reduces to the source's three cusp functions. For example, \(T_{u_0}S\) reduces through \(u_0\) modulo \(\mathbb Z+3\mathcal O\), with residues \(0,\omega,-\omega\). The lower translations by \(\lambda\) and \(-\lambda\) reduce through integral lower translations and lower translations by \(3\mathcal O\); the latter have Kubota multiplier \(1\), since their upper-left entry is \(1\). This uses the literal source invariances, not an identification of the three coefficient sequences.

The remaining right factor sends

\[
z\longmapsto u^{-2}z-t,\qquad v\longmapsto v.
\]

It therefore changes a Fourier coefficient by a fixed unit rotation of its index and a unit-modulus translation phase. Both preserve the lattice \(\lambda^{-4}\mathcal O\), coefficient magnitudes, and the source cubic support. Thus every nonzero frequency satisfies

\[
N\ell\ge N(\lambda^{-4})=1/81.
\]

The note also proves the needed absolute convergence: for \(\sigma>1\), the majorant factors into the convergent sums over the ramified valuation, the squarefree \(n\), and the cube index \(b\). This justifies the raw-frequency Dirichlet series on the starting contour.

## 3. Arbitrary periodic multiplier and the second denominator: PASS

Under the source character convention \(e(z)=\breve e(z/\lambda)\), multiplying the mode at \(\ell\) by

\[
e(\lambda^4\ell j/q)
\]

is exactly translation by \(\lambda^3j/q\). Its reduced denominator \(c_j\) divides \(q\); the zero shift is represented by \(0/1\). Thus \(N(c_j)\le Nq\), including the zero-shift term.

For each finite representative, factor

\[
H_\tau g_j=\gamma_j H_{\tau_j},
\qquad \gamma_j\in\Gamma(3).
\]

Then the scalar automorphy law changes the translated function into the cusp function \(F_{\tau_j}\) evaluated at \(g_j^{-1}(z+a_j/c_j,v)\). The inversion matrix is \(g_j\), so its archimedean conductor is \(c_j\). Replacing it by the lower-left entry of \(H_\tau g_j\) would introduce an unjustified moving factor; the note correctly avoids that replacement.

It is not necessary to assume \(P(0)=0\). A constant term in the finite sum of translates is harmless because the next operation is a nonzero horizontal derivative.

## 4. Angular, Mellin, and test normalization: PASS

The pure derivative at the center of the inversion is exactly

\[
\partial_z\{F(z',v')\}\big|_{z=0}
=-\alpha(c_j)^2N(c_j)^{-1}v^{-2}
\partial_{\bar z}F\!\left(-d_j/c_j,\frac1{N(c_j)v}\right).
\]

There is no height-derivative term. Both horizontal derivatives annihilate the constant Fourier modes. The scalar automorphy multiplier is independent of \(z,v\) and contributes no derivative terms.

The Bessel calculation in raw Fourier-index normalization gives

\[
\frac{i}{4(2\pi)^{2s}}
\Gamma(s+1/3)\Gamma(s+2/3)
\sum_{\ell\ne0}d_\tau(\ell)\alpha(\ell)(N\ell)^{-s}.
\]

The opposite derivative has the same scalar and replaces \(\alpha\) by \(\overline\alpha\). After the height substitution the conductor factor is \(N(c_j)^{1-2s}\). Taking the ratio of the two Bessel normalizations and setting \(t=1/2-s\) produces the exact coefficient in the note:

\[
-\widehat P(j)\zeta_j\alpha(c_j)^2,
\]

and the raw-index kernel constant

\[
C_\infty=(2\pi)^4.
\]

The source's kernel instead has \(C_0=(2\pi)^4/27\), because its input coefficients were normalized at \(\ell=\lambda^{-3}nb^3\). The distinction is necessary. Writing the common gamma ratio as \(R_1(t)\),

\[
\widehat{\mathsf JV_*}(s)=
\widehat V_*(-s)R_1(s)C_0^{-s}
\quad(\Re s>-5/6).
\]

It follows on the dual contour \(\Re t=3/4\) that

\[
\widehat{\mathsf JV_*}(-t)R_1(t)C_\infty^{-t}
=\widehat V_*(t)27^{-t}.
\]

Thus the outgoing test is exactly \(V_*(27x)\), not \(V_*(x)\).

The contour extension to the noncompact input \(\mathsf JV_*\) is legitimate. Moving the coefficient-series variable from \(5/4\) to \(-1/4\) keeps its smoothing Mellin argument in \([-3/4,3/4]\), to the right of the first possible pole at \(-5/6\). The differentiated theta Mellin integral is entire by exponential decay at both ends after cusp inversion. The source strip-growth argument and rapid Mellin decay justify the contour shift. No constant-mode or polar residue has been omitted.

## 5. Reunited arithmetic expression and standard projection: PASS

The elementary identity

\[
\prod_{p\mid a}(Np)^{-1/2}
[-1+Np\,\mathbf1_{p\mid x}]
=\sum_{hg=a}\mu(g)\sqrt{Nh/Ng}\,\mathbf1_{h\mid x}
\]

holds for every \(x\). In particular the negative term does not impose \((g,x)=1\). Keeping every positive choice inside \(h\) produces the full divisibility condition \(h\mid x\), with no squarefree/cube-part asymmetry.

Combining this identity with PR #915's full scalar cancellation gives the note's raw-index scale

\[
X=\frac{N(c_0)^2(Nk)^2(Nh)^2(Ng)^2}{B}
\]

and multiplier

\[
P_{k,h}(x)=\psi(x)\chi_k(x)^3\mathbf1_{h\mid x}\Pi(x).
\]

The first-reflection branch data have been fixed by the prescribed finite ray split. The additive character \(\psi\) has a fixed finite period supported on \(S\). After including the period of \(\Pi\), the entire multiplier is periodic modulo \(Mkh\), with \(M\) fixed. The complementary divisor \(g\) has disappeared from this modulus. The original branch assumes \((k,hg)=1\); all other pairs were already zero in the coupled expression.

The proposed standard-face projection is exact:

\[
\Pi_{\mathrm{std}}(x)=
\mathbf1_{x\equiv\lambda\pmod{\lambda^3}}
\prod_{\substack{p\in S\\p\nmid\lambda}}\mathbf1_{p\nmid x}.
\]

On the source support \(\ell=u\lambda^mnb^3\), the congruence forces \(m=-3\). Dividing by \(\lambda\) gives \(u\,nb^3\equiv1\pmod3\). Since \(n,b\) are primary, their product is \(1\pmod3\), and the distinct unit residues force \(u=1\). The remaining masks are exactly \((nb,S)=1\). Conversely every index on the stated standard face satisfies this projection. No condition involving \(g\) is inserted.

## 6. Exact cutoff and order of operations: PASS

After the second reflection the compact test is evaluated at

\[
27\frac{N\ell'\,N(c_0)^2(Nk)^2(Nh)^2(Ng)^2}
{B\,N(c_j)^2}.
\]

Using \(N(c_j)\le N(M)NkNh\) and \(N\ell'\ge1/81\), this is at least

\[
\frac{N(c_0)^2}{3N(M)^2}\frac{(Ng)^2}{B}.
\]

The constant

\[
C_*=\frac{3N(M)^2v_1}{\min_{c_0}N(c_0)^2},
\qquad v_1=\sup\operatorname{supp}V_*,
\]

therefore proves exact vanishing whenever \((Ng)^2>C_*B\). The strict inequality correctly handles the support endpoint. The finite Fourier expansion may have many terms, but each resulting test is zero. No bound for its growing coefficient norm is needed.

This proves the cutoff for each reunited \((h,g)\) block, at every source cusp and after a fixed periodic projection. It does not prove vanishing for an individual separated \((e,f,g)\) block.

The subsequent smooth insertion is valid precisely in the order stated: insert a function equal to one for \(Ng\le\sqrt{C_*B}\) into each reunited block, then separate the positive allocations. The difference is supported on already vanishing reunited blocks. Reversing this order would require an additional argument that the note does not assume.

On every nonempty smooth \(g\)-dyad the inserted test has uniform rescaled derivative bounds. These remain uniform after \(g=dg'\), with scale \(G/Nd\). Thus the modified components fall under the previously reviewed smooth component theorem and have \(G\ll\sqrt B\).

## 7. Quantitative standard-cusp consequence: PASS with the stated extra input

Assume the component bound from centered_a2_attack.md, Theorem 7.1:

\[
D^\epsilon G^{2\beta-2}
[HE+Y+(EY)^{2/3}],
\qquad
Y=\frac{H^2EG^2}{BF},
\quad EFG\asymp A.
\]

At \(A=B=D\), with \(1/2<\beta\le1\), the exact restriction \(G\ll D^{1/2}\) gives

\[
G^{2\beta-2}HE\ll HD,
\]

\[
G^{2\beta-2}Y
\asymp \frac{H^2G^{2\beta-1}}{F^2}
\ll H^2D^{\beta-1/2},
\]

and

\[
G^{2\beta-2}(EY)^{2/3}
\ll H^{4/3}D^{2/3}.
\]

Minkowski over the logarithmic number of smooth allocation blocks and the fixed ray branches costs a subpower. Consequently

\[
\sum_{k\sim H}^*|\mathcal C^{(0)}_{D,D}(k)|^2
\ll D^\epsilon
[HD+H^2D^{\beta-1/2}+H^{4/3}D^{2/3}].
\]

For \(\beta=11/12\), the second exponent is \(5/12\), and the binding restriction is \(2\log_D H+5/12\le2\). Hence \(H\le D^{19/24}\) is correct. The other two terms permit \(H\le D\). The stated general range \(H\le D^{(5-2\beta)/4}\) is also correct for \(1/2<\beta\le1\).

## 8. Independent finite-checker inspection and rerun

I inspected the implementation of checks/check_support_algebra.py and reran it with both ordinary Python and Python's optimization flag, -O. Both executions returned exit status zero, the same JSON bytes, and PASS on 11,134 predicates. The predicates use exact integer and rational arithmetic and explicit failure checks; optimization does not remove them.

| Checked artifact | Bytes | SHA-256 |
|---|---:|---|
| checks/check_support_algebra.py | 7,141 | fb8770897cd7ec6d15411e8070b3b418b3b6439d0b2c4e2f658f4d97b2dcf00c |
| support_cutoff_algebra_audit.json | 872 | 6362787d64e65271d1555fe4b34e73fde1eb55ed02556a8e4aecd0782a1193ad |

The exhaustive matrix check covers all 648 matrices in \(\mathrm{SL}_2(\mathcal O/(3))\), using the actual six Eisenstein units. It verifies the normalization, prescribed reduced cusp residues, and \(\Gamma(3)\) remainder. The projection check covers 8,262 cases with all units, valuations \(m=-4,\ldots,12\), and nontrivial primary lifts. The local product check covers 81 complete divisibility profiles over four prime norms, including negative allocations at divisibility points. The exponent check computes exact maxima on the four vertices of the allocation polygon for four specified rational \(\beta\)'s, including \(11/12\).

These checks corroborate the finite algebra in the proof. The projection beyond the tested valuation range and the exponent formula for all \(1/2<\beta\le1\) follow from the analytic review's elementary proofs, rather than from those finite samples. The checker does not establish theta automorphy, the Mellin contour argument, exact infinite-sum cancellation, or a moment asymptotic.

## 9. Explicit limitations of this verdict

- The exact cutoff is valid for the complete theta frequency sum in a reunited block. A norm truncation of \(n\) or \(b\) before the second reflection would generally destroy the identity.
- The cutoff includes all source cusps. The quantitative \(19/24\) corollary in this reviewed file uses the separate standard-cusp Gauss-factorization estimate. An extension of that estimate to all cusps requires its own proof and review.
- Squarefree primary rows and the original coprime mixed branch are retained. This review supplies no estimate for arbitrary rows or new overlapping local-exponent configurations.
- No quantitative bound for a growing Fourier/scattering matrix is proved or required for the exact-zero statement.
- No new argument here bounds the centered sesquilinear family after the product-column diagonal is subtracted, inverts the entire completion family at the initial fourth-moment scales, or reaches the original adverse dual range.
- The imported main theorem and the full generalized moment hierarchy remain outside this verdict. The result certified here is the source-conditional exact support cutoff, plus its explicitly conditional standard-face corollary.

No unresolved mathematical defect was found in the frozen cutoff snapshot. Any further mathematical change should be reviewed against its new hash.
