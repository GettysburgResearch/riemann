# Bounded-order Hecke twist balls and simultaneous relative fields

**Status.** The conductor count below is elementary, with fixed field and fixed order. Its applications import the explicitly source-qualified uniform moving-twist density/detector estimates, reciprocity and profile matching in [the moving-twist note](../2026-10-29-moving-unitary-twist-density/README.md), [the growing cubic note](../2026-10-29-growing-ray-relative-cubics.md), and [the growing quartic note](../2026-10-29-growing-ray-relative-quartics.md). This is not an individual zero-free half-plane or an exhaustive priority claim.

## Conductor-ball and fixed-conductor bounds

Let K be any fixed number field, m≥1 a fixed integer, and Q≥2. The number of primitive finite-order K-Hecke characters ν with \(\nu^m=1\) and \(N\mathfrak f_\nu\le Q\) satisfies
\[
 N_{K,m}(Q)\ll_{K,m,\epsilon}Q^{1+\epsilon}.\tag{1}
\]
Moreover, for each fixed integral ideal \(\mathfrak f\), the number of such characters whose conductor divides \(\mathfrak f\) is
\[
 \ll_{K,m,\epsilon}(N\mathfrak f)^\epsilon.\tag{2}
\]
The same bounds include all possible finite-order archimedean components. No uniformity in K or m is claimed.

**Proof.** For each finite place \(\mathfrak p\nmid m\), the principal-unit group is pro-p and has no nontrivial continuous character of order dividing m. Thus a local m-torsion character is tame, its conductor exponent is at most 1, and its restriction to the residue-unit group has at most m choices. At the finitely many places above rational primes dividing m, the quotient \(K_\mathfrak p^\times/(K_\mathfrak p^\times)^m\) is finite, so there are finitely many local m-torsion characters and their conductor exponents are bounded by a constant depending only on K,m. A finite-order character at a complex place is trivial; at a real place it has one of the two sign choices.

Fix all local inertia data at the finite ramified places and all real signs. Two global characters with the same data differ by a finite-order character unramified at every finite place, with a fixed allowed sign pattern; there are only finitely many, bounded by the narrow class-group size. It follows that, for fixed \(\mathfrak f\), the number is \(O_{K,m}(m^{\omega(\mathfrak f)})\), up to a fixed wild/sign factor. The standard ideal-divisor bound gives (2). Summing (2) over the \(O_K(Q)\) integral ideals of norm at most Q gives (1). This argument counts primitive characters by their primitive conductor; extra redundant Euler deletions are not allowed as part of the conductor. ∎

If H/K is finite abelian of exponent dividing m, and its conductor ideal has norm ≤Q, all characters of \(\operatorname{Gal}(H/K)\) have order dividing m and conductor dividing that single ideal. Hence
\[
 [H:K]\ll_{K,m,\epsilon}Q^\epsilon.\tag{3}
\]
The conductor-ball bound (1), of order \(Q^{1+\epsilon}\), is needed to make an exceptional set work simultaneously for *all* such H; the sharper fixed-conductor bound (3) controls field fibers for each H.

## Uniform union and compositum transfer

Suppose a source theorem gives, uniformly for each common primitive unitary twist ν with \(N\mathfrak f_\nu\le X^\kappa\), at most \(O(X^{E+\epsilon})\) bad labels in a specified \(\asymp X\)-sized family, with one common height power \(\tau>0\). For finitely many fixed character powers and all finite-order ν of order dividing a fixed m, (1) and a union bound give a **single** exceptional set of size
\[
 O_{K,m,\epsilon}(X^{E+\kappa+\epsilon}).\tag{4}
\]
The common τ and constants must be uniform before this union. Local ramification cancellation and all original zero masks remain in the moving-twist theorem; primitive inducing characters are used in (4). Any pole-bearing rows must be included in the source theorem's exception count, as in the cited moving-twist note.

Let the labels define cyclic degree-n class fields \(L_u/K\), with n fixed and \(\gg X\) distinct labels up to \(O_n(1)\) fibers. Suppose the density estimate covers all nontrivial powers \(\chi_u^j\), \(1\le j<n\), and their admissible twists. For every finite abelian H/K of exponent dividing m and conductor norm ≤\(X^\kappa\), put \(M=L_uH\). The fibre-product character argument in the linked growing-ray notes gives
\[
 \frac{\zeta_M(s)}{\zeta_H(s)}=
 \prod_{\psi\in\widehat{\operatorname{Gal}(M/K)}\setminus\widehat{\operatorname{Gal}(H/K)}}L_K(s,\psi),\tag{5}
\]
where each factor is a primitive character represented by some \(\chi_u^j\nu\) with j nonzero and ν a character of H/K. A character of the fibre-product subgroup extends to the finite abelian direct product. This remains true when \(L_u\cap H\ne K\); if \(L_u\subset H\), the quotient is 1. Every factor in (5) is nonprincipal, and omitted S-Euler factors do not vanish in \(\Re s>0\).

For each fixed admissible H, (3) gives \([M:K]\le n[H:K]\ll X^\epsilon\). A finite abelian group has at most its order many characters and hence cyclic degree-n subextensions, so each M has \(X^\epsilon\) label fibers. Consequently the source labels give \(\gg X^{1-\epsilon}\) distinct composita for each H, and at most (4) of them are exceptional. If \(E+\kappa<1\), their exceptional proportion tends to zero after choosing the losses. The **same** exceptional label set works for every H in the bounded-exponent conductor ball; H may vary with X. This is a family statement and does not enumerate all extensions of H.

## Cubic example at the candidate boundary

Let \(K=\mathbb Q(\zeta_{12})\), \(\theta=4369347/5000000\), and fix \(\kappa=1/10\) and any m. Restrict the good cubic FHL labels to squarefree ideals with norms in a fixed annulus \(\asymp X\), and omit any trivial label. The cited sixth-moment moving detector gives, per ν,
\[
 E=\frac{5045224}{9391959}=0.53718548\ldots,\qquad
 E+\kappa=\frac{59844199}{93919590}=0.63718548\ldots.\tag{6}
\]
The source proof uses \(h=630653/2500000\), \(t=20000000/9391959<5/2\), and the ordinary sixth moment when the inverse witness is short; its fixed losses and common τ are chosen as in the growing cubic note. Conjugation covers the second cubic power in the same two-sided height window. Therefore, for each fixed ε>0 and sufficiently small common τ>0, all but \(O(X^{59844199/93919590+\epsilon})\) labels have the following property **simultaneously for every** abelian H/K of exponent dividing m and conductor norm ≤\(X^{1/10}\): the relative quotient \(\zeta_{L_uH}/\zeta_H\) is zero-free in \(\Re s\ge\theta\), \(|\Im s|\le X^\tau\). For each H there are \(\gg X^{1-\epsilon}\) distinct composita and at most that many exceptional labels, giving density one.

The comparison is source-specific. [Khale–O'Kuhn–Panidapu–Sun–Zhang, Lemma 3.3](https://arxiv.org/abs/2008.09677) combined with the general conductor/collision count in the growing cubic note gives the weaker exponent
\[
 \frac{32118079}{43693470}=0.735077\ldots\tag{7}
\]
at this κ, after shrinking the height power. If \(\gcd(m,3)=1\), however, \(\nu\) is uniquely recovered from \((\chi_u^j\nu)^3=\nu^3\); then that named theorem gives the stronger \(13874366/21846735=0.635077\ldots\). Thus (6) is not an improvement over that comparator in the coprime-order case. This comparison is not exhaustive.

## Quartic example at 4/5

Let \(K=\mathbb Q(i)\), \(\kappa=1/10\), and use **squarefree** good quartic FHL labels in an annulus \(Nu\asymp X\). There are \(\gg X\) distinct primitive labels, and at most two define the same cyclic quartic field. The moving quartic source at \(\sigma=4/5\) gives \(R_4=35/52\) per ν, while the moving quadratic sieve/detector gives \(R_2=1/2\) for \(\chi_u^2\); since all u lie in the top annulus, no small-core height split is needed. Union over the bounded-order conductor ball gives the common exception exponent
\[
 \frac{35}{52}+\frac1{10}=\frac{201}{260}=0.7730769\ldots.\tag{8}
\]
Hence, under the cited uniform source inputs, a single set of \(O(X^{201/260+\epsilon})\) exceptional squarefree labels suffices for all abelian H/K of exponent dividing m and conductor norm ≤\(X^{1/10}\). Outside it, every \(\zeta_{L_uH}/\zeta_H\) is zero-free in \(\Re s\ge4/5\), \(|\Im s|\le X^\tau\). For each H, there are \(\gg X^{1-\epsilon}\) distinct composita and a density-one good subfamily.

At \(\sigma=4/5\), the conductor exponent in the named Khale et al. Lemma 3.3 is \(2\min\{3/(2-\sigma),2/\sigma\}(1-\sigma)=1\). The general conductor/collision comparison therefore gives \(1/10+11/10=6/5\), weaker than (8). This is a comparison to that named bound, not an exhaustive novelty claim.

## Conditional full zeta functions over exponent-three bases

Retain the squarefree top-annulus quartic family over \(K=\mathbb Q(i)\), and instead take \(\sigma=\theta=4369347/5000000\), \(\kappa=1/10\), \(m=3\). In addition to the analytic inputs already named, assume the separately staged all-Dirichlet candidate has its conventional interpretation, with all-height nonvanishing for primitive Dirichlet L-functions in the open half-plane \(\Re s>\theta\), apart from the principal pole. The candidate's formal-dependency and semantic qualifications are separate from the source-qualified density inputs here.

The quartic moving-density source gives
\[
 R_4=\frac{842755}{1674204},\qquad
 t=\frac{625000}{418551},\qquad t-1=\frac{206449}{418551}>\frac1{10}.
\tag{9}
\]
The quadratic-core moving source gives
\[
 R_2=\frac{1891959}{5630653},\qquad
 \frac{1-h}{2+h}=\frac{1869347}{5630653}>\frac1{10},\qquad h=\frac{630653}{2500000}.
\tag{10}
\]
Thus κ=1/10 is inside both moving-twist margins. The bounded-order union in (4) gives the common exceptional-label bound
\[
 O\!\left(X^{5050877/8371020+\epsilon}\right),\qquad
 \frac{5050877}{8371020}=R_4+\frac1{10}=0.6033765\ldots;\tag{11}
\]
the quadratic power contributes only exponent \(R_2+1/10<0.437\). The faithful conjugate power is handled by conjugation or the corresponding powered source embedding, and the moving estimates retain all cancellation and deletion masks. Choose one uniform polynomial height power τ after fixing the losses.

For every H/K in the exponent-three conductor ball which is also abelian over \(\mathbb Q\), \(\zeta_H\) is a finite product of primitive Dirichlet L-functions. The staged candidate therefore makes \(\zeta_H\) nonzero for \(\Re s>\theta\) at every height. Outside the single exceptional-label set (11), (5) controls the relative factors in the closed region \(\Re s\ge\theta\) up to height \(X^\tau\). Consequently the **full** \(\zeta_{L_uH}\) is nonzero in
\[
 \Re s>\theta,\qquad |\Im s|\le X^\tau,
\tag{12}
\]
away from its pole at 1. This does not assert nonvanishing on the boundary \(\Re s=\theta\).

Because \([H:K]\) is a power of 3 and \([L_u:K]=4\), the two fields are disjoint over K. Moreover \(\operatorname{Gal}(L_uH/K)\simeq C_4\times\operatorname{Gal}(H/K)\) has a unique cyclic quartic quotient, so the compositum determines \(L_u\). At most two primitive quartic characters generate a given \(L_u\), and good squarefree labels supply \(\gg X\) distinct such characters. Hence for every admissible H there are **\(\gg X\)** distinct composita, uniformly in H, and at most (11) are exceptional. This is a specified family, rather than a count of every extension of H.

For comparison, if \(\psi=\chi_u^j\nu\) with \(\nu^3=1\) and \(j=1,2,3\), then \(\psi^4=\nu^4=\nu\); the primitive product character determines ν and then the relevant primitive power of \(\chi_u\), up to the bounded source-label fibers. The named Khale et al. density input at conductor \(\ll X^{11/10}\) gives exponent
\[
 \frac{11}{10}\frac{2522612}{4369347}
 =\frac{13874366}{21846735}=0.6350773\ldots,
\tag{13}
\]
which is larger than (11), after absorbing a sufficiently small height loss. This is a comparison with that named input, not an exhaustive novelty claim. It remains conditional on the source and candidate interpretations specified above.

The [targeted quartic prior-art comparison](../2026-10-29-quartic-theta-twist-prior-art.md) records the scopes and height factors of these and other named results, including the slightly weaker untwisted de Faveri exponent at θ. It is not an exhaustive literature search.

**Independent review.** High_match and Other_families independently checked the bounded-order local inertia and fixed-conductor counts, fibre-product and compositum fibers, the corrected named-source comparisons, and the θ/m=3 full-zeta example. The cited moving-density/source and staged-candidate inputs remain external qualifications.
