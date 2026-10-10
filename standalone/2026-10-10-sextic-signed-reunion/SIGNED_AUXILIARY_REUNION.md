# Exact signed auxiliary reunion and a quantitative tail for every fixed order

**Status:** proposed exact identities and quantitative component theorems. The
identities use the native arithmetic and Poisson normalizations pinned below.
The counting specialization of the tail is unconditional relative to these
standard identities. A stronger tail explicitly assumes the stated uniform
finite-order inverse estimate. No full fourth moment, generalized moment
hierarchy, new zero-free boundary, or RH conclusion is proved.

**Authorship:** signed_auxiliary_attack. This file is a new mathematical object;
it does not amend a previously reviewed source. An independent review must bind
its final hash.

**Scope:** all nonzero Eisenstein element rows, all literal nonunit zeros, and
the full original coupled smoothing in the signed first-Poisson formula. The
quantitative result applies to the actual fixed-order smooth squarefree
convolution coefficients, not arbitrary arithmetic coefficients. The new
cutoff is on a reunited signed divisor; it is distinct from a common gcd of all
original tuple entries.

**Exact dependencies.**

1. PR #914, commit `0cc0428fedbbfc340044c7451b3d392c1da9a103`,
   `standalone/2026-10-10-sextic-moment-conductor-core/A2_COMPLETION.md`,
   equations (6.3), (6.9), and the exact row/column conventions. SHA-256:
   `d99eade56807077b07e5ec1325001f1592115db216e1e10e6a3906a3e01f0aad`.
2. OpenAI/math commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`,
   October 5 `paper2.tex`, `lem:arithmetic`, equations `eq:crt-a`,
   `eq:convert1`, `eq:quotient`, and `lem:poisson` with its self-dual radial
   Fourier normalization. The imported local file has SHA-256
   `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
   The present identities do not use that source's unrebuilt canonical mean
   square theorem.
3. PR #921, commit `4e6d4aa57ae4cb04d76b2b31279ac367951b469a`,
   `standalone/2026-10-10-sextic-centered-covariance/HERMITIAN_INCIDENCE.md`,
   Section 2, for the exact forward coprimality correction. Its all-pointwise
   specialization is reproved below. SHA-256:
   `5c1844409097959a772916e1658ec61dfa747da857dd48321869d0a38cbc66e9`.
4. The optional finite-order estimate is the common-zero-free-half-plane
   consequence in PR #913, commit
   `6498d6cc2eded03159c7332b25fd224ad07f89c1`,
   `standalone/2026-10-10-sextic-moment-descent/FOURTH_MOMENT_ATTACK.md`,
   Section 8. That file has SHA-256
   `354e8f7f5f81d0f8821ea6e821f55546f9c9641ac0690def1ae373000b4b3d08`.
   Its uniform reciprocal input is a hypothesis here, with no claim that the
   entire imported zero-free proof was independently established.

The adjacent PR #919 at `9b04a887e171b3104a66cf57296ce5b0b2920d78`
and PR #922 at `f71a9bc6ac3ce59a3c19d7e842a3fa082ecfbe32` were inspected.
Their signed scale averages and later theta finite-ray reunion are separate
objects; neither is used as a premise for the identities or estimates below.

## 1. Data and the exact signed quantity

Work over \(K=\mathbb Q(\sqrt{-3})\), with \(\mathcal O=\mathbb Z[\omega]\),
the pinned multiplicative primary-generator convention, and a fixed set
\(S\) containing the primes above 6 and all fixed ray conductors. All ideal
variables in the sums below are squarefree and prime to \(S\), unless another
condition is written. Put

\[
a_\xi(n)=\overline{\alpha(n)}\gamma_2(n)\xi(n),
\qquad \chi_n(x)=(x/n)_6.
\tag{1.1}
\]

Symbols are extended by zero at every nonunit; an exponent zero retains the
nonunit mask. All row variables are elements of \(\mathcal O\), not ideal
representatives, and all six units occur.

Let \(v(n)\) be any finitely supported coefficient on squarefree columns,
supported in \(\ell L\le Nn\le uL\) for fixed \(0<\ell<u\). Put

\[
R_L(n)=\sqrt{L/Nn}\,\overline{v(n)}.
\tag{1.2}
\]

Let \(\Phi\) be the fixed radial Schwartz profile in the source's first
Poisson formula and \(\Psi=\widehat\Phi\) its compactly supported smooth
radial transform. In the source normalization
\(\widehat\Psi=\Phi\). Let \(H>0\).

Retain the exact strict off-diagonal from PR #914:

\[
\begin{aligned}
\mathcal O_\xi[v]
={}&\frac H{L^2}
\sum_{\substack{b,f\ {\rm sf}\\(b,f)=1}}
\mu(f)Nb
\sum_{k\ne0}
\sum_{\substack{m_1,m_2\ {\rm sf}\\(m_1m_2,bS)=1\\m_1\ne m_2}}
a_\xi(m_1)\overline{a_\xi(m_2)}
\chi_{m_1}(kf^4)\overline{\chi_{m_2}(kf^4)}
R_L(bfm_1)\overline{R_L(bfm_2)}\\
&\hspace{27mm}\cdot
\Psi\!\left(\frac{HNk}{(Nf)^2Nm_1Nm_2}\right).
\end{aligned}
\tag{1.3}
\]

Here and subsequently the support of \(v\) enforces the required column
squarefreeness, even where a zero term would already be absent from the
original symbol. One can equivalently state the pairwise exclusions
explicitly after removing those zero terms.

## 2. Exact collapse of every auxiliary divisor, including the off-diagonal

For coprime squarefree \(z_1,z_2\), write

\[
\psi_{z_1,z_2}=\chi_{z_1}\overline{\chi_{z_2}},
\qquad C=N(z_1z_2).
\tag{2.1}
\]

The condition \((z_1,z_2)\ne(1,1)\) will always mean that they are not
both unit ideals. Because they are coprime, this is also \(z_1\ne z_2\).

### Theorem 2.1. The complete signed primitive-pair identity

The strict off-diagonal (1.3) equals

\[
\boxed{
\begin{aligned}
\mathcal O_\xi[v]
={}&\frac HL
\sum_{\substack{b,w\ {\rm sf}\\(b,w)=1}}
\frac{\mu(w)}{Nw}
\sum_{\substack{z_1,z_2\ {\rm sf}\\(z_1,z_2)=1\\
 (z_1z_2,bwS)=1\\(z_1,z_2)\ne(1,1)}}
\frac{a_\xi(z_1)\overline{a_\xi(z_2)}}{\sqrt{N(z_1z_2)}}
\overline{v(bwz_1)}v(bwz_2)\\
&\hspace{9mm}\cdot
\sum_{h\ne0}\psi_{z_1,z_2}(h w^5)
\Psi\!\left(\frac{HNh}{Nw\,N(z_1z_2)}\right).
\end{aligned}}
\tag{2.2}
\]

It remains exact after inserting any fixed bounded multiplier depending on
\(b,w,z_1,z_2,h\) into the reunited expression and pulling that multiplier
back through the change of variables proved below. A cutoff on \(w\) is in
particular legitimate. A cutoff on the original \(f\) alone generally is not
invariant under this reunion.

**Proof.** In a nonzero term of (1.3), put

\[
d=(m_1,m_2),\qquad m_i=d z_i,\qquad w=f d.
\tag{2.3}
\]

The ideals \(b,f,d,z_1,z_2\) are pairwise coprime, except that this assertion
does not place any extra condition on the element \(k\) at \(f\). The
restriction \((d,k)=1\) is forced by the two original row symbols. Since
\(z_1,z_2\) are coprime, \(m_1\ne m_2\) is exactly the exclusion of
\((z_1,z_2)=(1,1)\).

The actual Gauss CRT gives

\[
a_\xi(dz_1)\overline{a_\xi(dz_2)}
=a_\xi(z_1)\overline{a_\xi(z_2)}
\chi_{z_1}(d)^4\overline{\chi_{z_2}(d)^4}.
\tag{2.4}
\]

The common factor \(|a_\xi(d)|^2\) equals one. Combining (2.4) with the
original row and auxiliary symbols leaves

\[
a_\xi(z_1)\overline{a_\xi(z_2)}
\psi_{z_1,z_2}(k w^4)\mathbf1_{(k,d)=1}.
\tag{2.5}
\]

Every residual column and norm kernel is now independent of the divisor
\(f\mid w\): they are \(bwz_i\) and
\(\Psi(HNk/((Nw)^2N(z_1z_2)))\). Thus the entire remaining dependence on
this divisor is

\[
\sum_{f\mid w}\mu(f)\mathbf1_{(k,w/f)=1}
=\prod_{p\mid w}\left(\mathbf1_{p\nmid k}-1\right)
=\mu(w)\mathbf1_{w\mid k}.
\tag{2.6}
\]

All divisors \(f\mid w\) occur in the original finite sum: reconstruct
\(d=w/f\) and \(m_i=d z_i\). This is why no missing coprimality condition
can be inserted into (2.6). Write \(k=w h\). No condition \((h,w)=1\)
is imposed. Equation (2.5) becomes \(\psi(h w^5)\), the norm kernel becomes
the one in (2.2), and

\[
\frac H{L^2}Nb\,R_L(bwz_1)\overline{R_L(bwz_2)}
=\frac H{L\,Nw\sqrt{N(z_1z_2)}}
\overline{v(bwz_1)}v(bwz_2).
\tag{2.7}
\]

This proves every factor in (2.2). All column sums are finite. The compact
support of \(\Psi\) makes every displayed nonzero-frequency sum finite.
The assertion about an inserted invariant multiplier follows from the same
bijection. QED.

The local identity (2.6) also explains what the unsigned replacement loses:
without the sign, the local factor is
\(\mathbf1_{p\nmid k}+1\), rather than a condition forcing divisibility.
The difference occurs before any norm estimate.

## 3. A second row Poisson removes every angular Gauss coefficient

For the primitive pair in (2.1), \(\psi=\psi_{z_1,z_2}\) is a primitive
character of modulus \(z_1z_2\): at a prime of \(z_1\) its local exponent
is 1, and at a prime of \(z_2\) it is 5. Both local sextic characters are
nonprincipal. Its modulus is nonunit by the excluded pair, so
\(\psi\) is nonprincipal and its value at zero is zero.

The source's primitive Poisson formula, now with no additional row mask,
at the scale

\[
T=\frac{Nw\,N(z_1z_2)}H
\tag{3.1}
\]

gives exactly

\[
\sum_{h\ne0}\psi(h w^5)\Psi(Nh/T)
=\overline{\psi(w)}\frac{Nw\sqrt{N(z_1z_2)}}H
\gamma(\psi)
\sum_{r\ne0}\overline{\psi(r)}\Phi(Nw\,Nr/H).
\tag{3.2}
\]

The factor \(\psi(w)^5=\overline{\psi(w)}\) is used only on
\((w,z_1z_2)=1\). There are no zero frequencies on either side. Every
unit row is retained. If \(\psi\) is nontrivial on the six units, the radial
row sum vanishes by the unit permutation; (3.2) still holds.

Let \(G\) and \(\mathcal R\) be the fixed finite-ray function and the
symmetric reciprocity bicharacter in the source's `lem:arithmetic`.

### Lemma 3.1. Exact native scalar after two Poisson operations

\[
\boxed{
a_\xi(z_1)\overline{a_\xi(z_2)}\gamma(\psi_{z_1,z_2})
=\mu(z_1)\mu(z_2)\xi(z_1)\overline{\xi(z_2)}
G(z_1z_2^{-1}).
}
\tag{3.3}
\]

The quotient on the right is taken in the fixed ray class group. No
archimedean angular character is hidden in \(G\).

**Proof.** The primitive CRT for the Gauss sum yields

\[
\gamma(\psi)=\gamma_1(z_1)\gamma_{-1}(z_2)
\chi_{z_1}(z_2)\overline{\chi_{z_2}(z_1)}
=\gamma_1(z_1)\gamma_{-1}(z_2)\mathcal R(z_1,z_2).
\tag{3.4}
\]

The identities `eq:convert1` and
\(\gamma_{-1}(z)=\chi_z(-1)\overline{\gamma_1(z)}\) imply

\[
\begin{aligned}
a_\xi(z_1)\gamma_1(z_1)&=\mu(z_1)\xi(z_1)G(z_1),\\
\overline{a_\xi(z_2)}\gamma_{-1}(z_2)
&=\mu(z_2)\overline{\xi(z_2)}\chi_{z_2}(-1)\overline{G(z_2)}.
\end{aligned}
\tag{3.5}
\]

The source's `eq:quotient`, with \(a=z_2,b=z_1\), identifies the product
of the remaining finite factors as \(G(z_1z_2^{-1})\). This proves (3.3).
All factors \(\alpha\) have canceled explicitly in (3.5). QED.

### Theorem 3.2. Exact native form of the complete strict covariance

\[
\boxed{
\begin{aligned}
\mathcal O_\xi[v]
={}&\frac1L
\sum_{\substack{b,w\ {\rm sf}\\(b,w)=1}}
\mu(w)
\sum_{\substack{z_1,z_2\ {\rm sf}\\(z_1,z_2)=1\\
 (z_1z_2,bwS)=1\\(z_1,z_2)\ne(1,1)}}
\mu(z_1)\mu(z_2)\xi(z_1)\overline{\xi(z_2)}
G(z_1z_2^{-1})\overline{v(bwz_1)}v(bwz_2)\\
&\hspace{10mm}\cdot
\sum_{r\ne0}\overline{\chi_{z_1}(rw)}\chi_{z_2}(rw)
\Phi(Nw\,Nr/H).
\end{aligned}}
\tag{3.6}
\]

**Proof.** Insert (3.2) and (3.3) into (2.2). The factors
\(H/(L Nw\sqrt{N(z_1z_2)})\) and
\(Nw\sqrt{N(z_1z_2)}/H\) cancel exactly. The remaining phase is
\(\overline{\psi(rw)}\). This proves (3.6). The new unrestricted row sum
is absolutely convergent by the fixed Schwartz bounds. QED.

One may expand \(G\) on its actual fixed ray class group:

\[
G(x)=\sum_\eta c_\eta\eta(x),\qquad
\sum_\eta|c_\eta|\ll_{S}1.
\tag{3.7}
\]

For a fixed \(\eta\), the two primitive coefficients in (3.6) are exactly
the conjugate pair of native inverse factors with fixed finite datum
\(\xi\eta\), evaluated at the row \(rw\). Equation (3.7) is not an
expansion of arbitrary moving Fourier data. Its group and number of terms
are fixed by the pinned arithmetic lemma.

## 4. The precise finite-order input and its tensor consequence

Fix \(1/2<\beta\le1\). Use the following estimate for all fixed finite
characters arising from (3.7), their conjugates, and the finite reciprocity
corrections needed below. For every fixed polynomial conductor bound and
every \(\epsilon>0\),

\[
\left|\sum_{(n,qS)=1}\mu(n)\vartheta(n)V(Nn/X)\right|
\ll D^\epsilon X^\beta\|V\|_{C^J},
\qquad c\le X\le C D,
\tag{4.1}
\]

where the finite-order character \(\vartheta\) and the moving exclusion
\(q\) have polynomially bounded conductors in the reference \(D\). The
estimate is quantified at every reference \(D\ge2\). It is enough to
assume the indicated native row-character subfamily for the main tail
theorem; the alternative signed-divisor estimate also uses its reciprocal
primitive-pair character. All literal zeros are retained.

At \(\beta=1\), (4.1) is elementary ideal counting. For \(\beta<1\),
this is an explicitly additional input. PR #913 Section 8 derives it,
including the moving-conductor subpower bound, from a common zero-free
half-plane. No constant depending arbitrarily on a moving character is
permitted. In particular \(\beta=7/8\) is only a source-conditional
specialization; it is not a new zero-free conclusion.

### Lemma 4.1. Pointwise products with exact disjointness

Let \(j\) be fixed and let \(U\) be a fixed smooth function of \(j\)
positive variables supported in a compact rectangle. Under (4.1),

\[
\left|
\sum_{\substack{n_1,\ldots,n_j\ {\rm pairwise\ coprime}\\
 (n_1\cdots n_j,qS)=1}}
\prod_i\mu(n_i)\vartheta_i(n_i)
U(Nn_1/X_1,\ldots,Nn_j/X_j)
\right|
\ll D^\epsilon\prod_i X_i^\beta\,\|U\|_{C^{J'}}.
\tag{4.2}
\]

The bound is uniform for nonempty bounded subunit scales and every stated
moving modulus. There is no arbitrary arithmetic coefficient on an axis.

**Proof.** Mellin separation on the fixed compact rectangle expresses
\(U\) as a superposition of products of fixed-support smooth tests. Its
coefficients decay faster than any fixed polynomial in the Mellin
frequencies, while each test seminorm grows polynomially. It therefore
suffices to prove (4.2) for such a product, with finite seminorm dependence.

Outside the moving exclusion, write
\(t_i=\vartheta_i(p)(Np)^{-s_i}\). The exact forward correction from
independent inverse sums to pairwise disjoint inverse sums is

\[
\frac{1-\sum_i t_i}{\prod_i(1-t_i)}.
\tag{4.3}
\]

A nonconstant monomial supported on \(I\) has coefficient \(1-|I|\).
Thus only monomials using at least two axes occur. At the common weight
\(\beta\), the absolute local factor is

\[
1+\sum_{|I|\ge2}(|I|-1)
\prod_{i\in I}\frac{(Np)^{-\beta}}{1-(Np)^{-\beta}}
=1+O_j((Np)^{-2\beta}).
\tag{4.4}
\]

Its Euler product converges because \(2\beta>1\). One may either begin
with inverse factors already omitting \(qS\), or retain the finite mask
correction \(\prod_{p\mid q,i}(1-(Np)^{-\beta})^{-1}\ll(Nq)^\epsilon\).
At a nonunit of a row character, every affected monomial remains zero.

Expand the correction before estimating, apply (4.1) at every shifted
scale, and sum its absolutely weighted coefficients using (4.4). Terms
below the fixed support threshold are empty. Rapid Mellin decay then
proves (4.2) with the claimed seminorm. QED.

## 5. Genuine fixed-order convolution coefficients

Fix an integer \(k\ge1\) and a smooth function
\(V\in C_c^\infty((0,\infty)^k)\), supported in a fixed rectangle.
For squarefree \(n\), define

\[
v_k(n;D)=
\sum_{n_1\cdots n_k=n}
V(Nn_1/D,\ldots,Nn_k/D),
\qquad L=D^k.
\tag{5.1}
\]

All factor ideals are the chosen primary ideals outside \(S\). They are
automatically squarefree and pairwise coprime. The product test
\(V(x_1,\ldots,x_k)=\prod_iW(x_i)\) is the squarefree product-column face
of the actual \(k\)-fold inverse polynomial. The theorem also allows a
fixed finite linear combination of such smooth convolution profiles.

One may add a moving exclusion \(q_0\) of polynomial norm by replacing
\(v_k(n;D)\) with \(\mathbf1_{(n,q_0)=1}v_k(n;D)\). Then the common
factor \(g\) and both primitive columns avoid \(q_0\), and the moving
exclusion in Lemmas 4.1 and 5.1 is \(q_0g\). All stated estimates are
uniform in this explicitly retained mask. In the divisor argument of
Section 7, the excluded product is correspondingly \(q_0bz_1z_2S\).

### Lemma 5.1. Two native primitive columns at a fixed common product

Fix squarefree \(g\) and a nonzero element \(s\). The primitive-pair
column sum in (3.6), with \(g=bw\), satisfies

\[
\left|
\sum_{\substack{z_1,z_2\ {\rm sf}\\(z_1,z_2)=1\\
 (z_1z_2,gS)=1\\(z_1,z_2)\ne(1,1)}}
\mu(z_1)\mu(z_2)\xi(z_1)\overline{\xi(z_2)}
G(z_1z_2^{-1})\overline{v_k(gz_1;D)}v_k(gz_2;D)
\overline{\chi_{z_1}(s)}\chi_{z_2}(s)
\right|
\ll D^\epsilon\left(\frac L{Ng}\right)^{2\beta}.
\tag{5.2}
\]

Initially \(Ns\) is polynomial in \(D\); the Schwartz extension used
below is quantified in the proof of Theorem 6.1.

**Proof.** First expand the fixed finite function \(G\) as in (3.7).
For a factorization counted by each of the two copies of \(v_k\), assign
every prime of \(g\) to its left factor index \(i\) and right factor
index \(j\). This gives a unique disjoint squarefree matrix
\((g_{ij})_{1\le i,j\le k}\) with product \(g\). There are at most
\(k^{2\omega(g)}\ll_{k,\epsilon}(Ng)^\epsilon\) such matrices.

Put \(g_i^{\rm L}=\prod_jg_{ij}\),
\(g_j^{\rm R}=\prod_i g_{ij}\). The remaining singleton factors are
\(x_1,\ldots,x_k,y_1,\ldots,y_k\), with
\(z_1=\prod_i x_i\), \(z_2=\prod_j y_j\), and scales

\[
X_i=D/Ng_i^{\rm L},\qquad Y_j=D/Ng_j^{\rm R},
\qquad \prod_iX_i=\prod_jY_j=L/Ng.
\tag{5.3}
\]

They are pairwise coprime across all \(2k\) axes and avoid \(gS\).
These conditions are exactly the old within-column squarefreeness and
the new primitive-pair coprimality; none is omitted. Their coefficients
are \(\mu\) times the two fixed finite data and the literal characters at
\(s\), so Lemma 4.1 applies. The two copies of the fixed smooth \(V\)
give a fixed \(2k\)-variable profile. Its bound is
\(D^\epsilon\prod_iX_i^\beta\prod_jY_j^\beta
=D^\epsilon(L/Ng)^{2\beta}\).

Any nonempty factor scale below one is bounded below by the fixed
support constants. Sum the subpower number of assignments. Finally,
the excluded primitive unit pair contributes only if \(Ng\asymp L\),
where \(L/Ng\asymp1\); its divisor-bounded coefficient satisfies the
same estimate. Subtracting it preserves (5.2). QED.

This argument cancels the actual singleton inverse coefficients. It does
not bound arbitrary divisor weights by their magnitudes before applying
the inverse estimates.

## 6. The proved sharp signed auxiliary tail

For \(R\ge1\), define \(\mathcal O_{\xi,\ge R}[v]\) by restricting
the reunited expression (2.2), or equivalently (3.6), to \(Nw\ge R\).
In the original formula (1.3), this means the exact invariant selection

\[
N\bigl(f\,(m_1,m_2)\bigr)\ge R.
\tag{6.1}
\]

All divisor partners in (2.6) remain present. The original \(k\) after
reunion must be a multiple of \(w\); this is a consequence, not an
extra assumption on the original sum. The cutoff is sharp and is not a
cutoff on \(f\) alone.

### Theorem 6.1. Uniform quantitative signed tail

Fix \(k\), \(V\), the source smoothing, and a polynomial bound on
\(1\le H\) and all moving excluded ideals in the reference \(D\ge2\).
Under (4.1), for every \(\epsilon>0\) and every \(R\ge1\),

\[
\boxed{
\bigl|\mathcal O_{\xi,\ge R}[v_k]\bigr|
\ll D^\epsilon H L^{2\beta-1}R^{-2\beta},
\qquad L=D^k.
}
\tag{6.2}
\]

The constants are uniform in \(H,R\), every nonempty column scale, and
the finite family of \(\xi\). A tail empty by the column support is zero.
All nonzero rows, including the entire Schwartz tail, are included.

In particular,

\[
\boxed{
R\ge L^{(2\beta-1)/(2\beta)}
\quad\Longrightarrow\quad
\bigl|\mathcal O_{\xi,\ge R}[v_k]\bigr|
\ll H D^\epsilon.
}
\tag{6.3}
\]

**Proof.** Use (3.6). At fixed \(b,w\), apply Lemma 5.1 at the row
\(s=rw\), before taking absolute values in the primitive columns.
The fixed Schwartz bound gives, for every fixed \(A>1\),

\[
\sum_{r\ne0}|\Phi(Nw\,Nr/H)|
\ll_{A,\Phi}
\begin{cases}
H/Nw,&Nw\le H,\\
(H/Nw)^A,&Nw>H.
\end{cases}
\tag{6.4}
\]

For the first case, split into norm annuli and use the elementary
\(O(T)\) lattice count. For the second, use
\(\sum_{r\ne0}(Nr)^{-A}<\infty\). In particular (6.4) is always
\(O(H/Nw)\). The zero row is absent because the primitive pair is
nonprincipal. Adding that row would destroy this bound when \(Nw>H\).

To justify use of the uniform pointwise input in the unrestricted row
sum, on annulus \(2^{j-1}H<N(rw)\le2^jH\) use the reference
\(D_j=2^jD\), with the preliminary conductor-bound exponent enlarged
to at least one. The original factor scales and excluded ideals remain
polynomially bounded in \(D_j\). A preliminary loss
\(D_j^{\epsilon_0}=D^{\epsilon_0}2^{j\epsilon_0}\) is absorbed by a
fixed Schwartz decay power. The same argument gives an arbitrarily
large extra decay in \(Nw/H\) when \(Nw>H\). Thus Lemma 5.1 and
(6.4) combine uniformly after assigning the preliminary losses within
the final \(D^\epsilon\).

The entire tail is therefore bounded by

\[
\frac{D^\epsilon}{L}
\sum_{\substack{b,w\ {\rm sf}\\Nw\ge R}}
\left(\frac L{Nb\,Nw}\right)^{2\beta}\frac H{Nw}
\le D^\epsilon H L^{2\beta-1}
\left(\sum_b(Nb)^{-2\beta}\right)
\left(\sum_{Nw\ge R}(Nw)^{-2\beta-1}\right).
\tag{6.5}
\]

Removing coprimality and support constraints is legitimate in this
positive majorant. The first series converges because \(2\beta>1\).
Elementary ideal counting and partial summation bound the second by
\(O_\beta(R^{-2\beta})\). The small divisor-factor losses from
Lemma 5.1 can be absorbed in \(D^\epsilon\), since the original
support already forces \(Nb,Nw\ll L\); these losses are removed
before the final extension of the positive majorant to all ideals.
This proves (6.2), including a sharp cutoff. Equation (6.3) follows by
substitution. QED.

### Explicit specializations

For the fourth-moment squarefree face, \(k=2\) and \(L=D^2\):

| Scalar premise | Proved tail bound | Sufficient reunited cutoff |
| --- | --- | --- |
| Counting, \(\beta=1\) | \(H D^{2+\epsilon}R^{-2}\) | \(R\ge D\) |
| Optional \(\beta=7/8\) | \(H D^{3/2+\epsilon}R^{-7/4}\) | \(R\ge D^{6/7}\) |
| Optional \(\beta=139999/160000\) | \(H D^{59999/40000+\epsilon}R^{-139999/80000}\) | \(R\ge D^{119998/139999}\) |

At general fixed order, the optional \(7/8\) cutoff is
\(R\ge D^{3k/7}\), and the counting cutoff is \(R\ge D^{k/2}\).
No constant uniform in growing \(k\) is asserted.

The complementary exact quantity \(\mathcal O_{\xi,<R}\) satisfies

\[
\mathcal O_\xi[v_k]=\mathcal O_{\xi,<R}[v_k]
 +O_\epsilon(H D^\epsilon)
\tag{6.6}
\]

at the sufficient cutoff. Hence (6.9) of the parent packet can be
replaced by the same target for this strictly smaller reunited
divisor range. No sign condition is imposed on either part.

## 7. An additional cancellation estimate in the reunited divisor itself

The next result concerns complete smooth blocks, since cancellation in
\(w\) now matters. Take fixed smooth dyadic cutoffs for
\(Nb\asymp B\), \(Nw\asymp W\), and put

\[
Z=\frac L{BW}.
\tag{7.1}
\]

The support of the actual column weights already has
\(Nz_1,Nz_2\asymp Z\); no nonsmooth primitive-column selection is made.
Write \(\mathcal O_{B,W}\) for the complete signed block of (3.6).

### Theorem 7.1. Two alternative native cancellation bounds

Under (4.1),

\[
\boxed{
|\mathcal O_{B,W}|
\ll D^\epsilon H
\min\left\{
Z W^{\beta-2},\quad \frac{Z^{2\beta-1}}W
\right\}.
}
\tag{7.2}
\]

Both bounds have arbitrarily strong additional decay for \(W/H\to\infty\),
with fixed Schwartz seminorms. The first estimate cancels the reunited
Möbius divisor; the second is the block form of Theorem 6.1.

**Proof of the first estimate.** Expand each prime of \(b\) and \(w\)
according to its left and right factor index in the two copies of
\(v_k\). Thus there are two disjoint \(k\)-by-\(k\) matrices
\((b_{ij})\) and \((w_{ij})\). The remaining \(2k\) singleton ideals
factor \(z_1,z_2\). The construction is unique for each original pair of
factorizations. Freeze the \(b\)-matrix and the singleton ideals, and
partition the \(w_{ij}\) into smooth dyadic norm blocks of product scale
\(W\). The number of scale profiles is a fixed logarithmic power.

The only nonsmooth factor depending on these \(w\)-variables, apart
from their exact masks, is

\[
\mu(w)\overline{\psi_{z_1,z_2}(w)}
=\prod_{i,j}\mu(w_{ij})
 \overline{\psi_{z_1,z_2}(w_{ij})}.
\tag{7.3}
\]

This is a finite-order character in each primary ideal, independent
of the row \(r\). Its conductor is polynomially bounded by
\(N(z_1z_2)\) times the fixed primary ray. It has no angular factor.
The \(w_{ij}\) are pairwise coprime and avoid exactly \(bz_1z_2S\).
They are not required to avoid \(r\).

Every remaining dependence is a smooth function of their normalized
norms: the original two copies of \(V\), the block cutoffs, and
\(\Phi(Nw\,Nr/H)\). On a fixed block all mixed derivatives of this
last factor are bounded by
\(C_{A,J}(1+WNr/H)^{-A}\). Apply Lemma 4.1 to the \(k^2\)
inverse axes. Their product scale is \(W\), so the result is
\(D^\epsilon W^\beta(1+WNr/H)^{-A}\).

There are \(O(D^\epsilon B)\) frozen \(b\)-assignments and
\(O(D^\epsilon Z^2)\) frozen singleton tuples. These bounds follow
from ideal counting and the fixed-order divisor estimate. Sum \(r\)
using (6.4), and divide by \(L\). The result is

\[
\frac{D^\epsilon}{L} B Z^2W^\beta\frac HW
=D^\epsilon H Z W^{\beta-2}.
\tag{7.4}
\]

This proves the first alternative. The second follows from (5.2),
counting \(b,w\) in their blocks and again using (6.4):

\[
\frac{D^\epsilon}{L}BW Z^{2\beta}\frac HW
=D^\epsilon H Z^{2\beta-1}/W.
\tag{7.5}
\]

Taking their minimum proves (7.2). QED.

For \(\beta<1\), the first estimate is stronger when \(W>Z^2\);
the second is stronger when \(W<Z^2\). At \(\beta=1\), both bounds
equal \(Z/W\) for every \(W\). They are alternative bounds on the same
bilinear character interaction. Multiplying their savings would
require a new argument and is not done here.

## 8. Boundaries and the remaining primitive core

1. **A complete auxiliary divisor set is essential.** The equality
   (2.6) holds after grouping every \(f\mid w\). An isolated old
   auxiliary annulus does not obey it. The proved sharp tail is the
   invariant set (6.1), with the full signed sum inside it.
2. **The primitive diagonal is unchanged.** Because
   \((z_1,z_2)=1\), the old strict condition is exactly the exclusion
   of the unit pair. If an A2 inverse correction is subsequently
   applied, the condition remains equality of reconstructed product
   columns; it cannot be replaced by equality of factor pairs.
3. **The common-G notation is not an all-tuple gcd.** Here
   \(g=bw\) is the common product-column factor, and \(w\) is a
   selected signed divisor of it. The new bound does not assert a
   stronger version of #921's different common-gcd theorem.
4. **The angular-to-finite-order conversion is specific.** It uses
   the actual normalized Gauss coefficients and the source quotient
   identity. No analogous assertion for arbitrary coefficient phases
   or for an arbitrary later theta correction is made.
5. **The shorter restored row cannot silently acquire a native M2.**
   Its norm scale is \(H/Nw\), but its column character is
   \(\chi_z(rw)\). Treating \(w\) as a moving fixed twist requires
   a separate uniform theorem. Positivity alone embeds these rows in
   the full original ball of height \(H\), losing the density
   \(1/Nw\). The present tail uses the explicit pointwise premise
   and the exact row count, so it has no such unstated interface.
6. **The balanced leading component remains.** At \(b=w=1\),
   the primitive columns still have length \(L=D^k\). The new tail
   estimates do not control that block at normalized size \(H\).
   The second Poisson identity is exact and reversible; it does not
   independently reduce its conductor. All genuinely difficult
   signed primitive correlations at small \(w\) remain.

Thus the proved advance is an exact collapse of the full auxiliary
average, a complete return to native inverse coefficients with the
correct finite rays, and a quantitative removal of its large reunited
divisor range for every fixed order. The full moment hypothesis is
still not established.
