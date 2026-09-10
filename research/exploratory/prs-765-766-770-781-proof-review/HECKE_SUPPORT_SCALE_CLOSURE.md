# Hecke-support scale closure for endpoint period restrictions

**Status:** proposed source-specific analytic theorem; independent proof review required.  
**Parent source:** PR #766 at `17c7624a0bd56c5356d00278b2a846d2efdbdccc`.  
**Repository effect:** proof/exposition only; no producer, fixture, certificate, or inherited source is modified.  
**RH/GRH status:** RH and GRH remain unproved.

This note closes the four logarithms separating the two Hecke-support scales in
`CUSP_FLAG_HECKE_SOURCE_CONCENTRATION.md`.  The parent proves

\[
\text{cusp-localized divisor nullvector}
   \Longrightarrow r_k\gg \frac{k}{\log k},
\]

but its endpoint zero-free theorem assumes
\(r_k=o(k/\log^5 k)\).  All four extra logarithms enter at HC8--HC11,
where the exact Rankin--Selberg series is discarded in favor of
\(\tau(n)^2\le d_4(n)\).

The exact series gives the correct bound:

\[
M_X(e_f)\ll \log k.
\]

Consequently the zero-free scale is \(r_k=o(k/\log k)\), matching the
existing source-support obstruction up to constants.

---

## 1. Imported objects and the one additional classical input

Use the exact normalization of the parent.  Let \(f\) be the level-one
holomorphic Hecke eigencuspform of even weight \(k\), normalized by
\(a_f(1)=1\), and put

\[
a_f(n)=\lambda_f(n)n^{(k-1)/2},\qquad
\mathcal L_f=L(1,\operatorname{sym}^2 f)>0.
\]

Let \(e_f=f/\sqrt{G(f)}\), and define

\[
M_X(e_f)=\int_{\mathcal F}X(z)y^k|e_f(z)|^2\,d\mu(z),
\qquad X(z)=\max(1,\Im z).
\]

The parent proves the exact high-cusp identity

\[
\int_{y\ge1} y\,y^k|e_f|^2\,d\mu
=
\frac{\pi}{2\mathcal L_f}
\sum_{n\ge1}\frac{\lambda_f(n)^2}{n}
Q(k,4\pi n),
\tag{HS1}
\]

where \(Q(a,x)=\Gamma(a,x)/\Gamma(a)\).  It also proves

\[
\sum_{n\ge1}\frac{\lambda_f(n)^2}{n^s}
=
\frac{\zeta(s)L(s,\operatorname{sym}^2 f)}{\zeta(2s)},
\qquad \Re s>1.
\tag{HS2}
\]

The only additional classical input is the following standard consequence
of the zero-free region already imported in the parent.

### Imported near-one comparison lemma

There is an absolute \(C_0\) such that, uniformly over level-one
holomorphic Hecke eigenforms of weight \(k\),

\[
L(1+u,\operatorname{sym}^2 f)
\le C_0\,L(1,\operatorname{sym}^2 f)
\qquad
\left(0\le u\le\frac1{\log k}\right)
\tag{HS3}
\]

for all sufficiently large \(k\).

The parent already imports the zero-free region

\[
\Re s\ge
1-\frac{c_0}{\log(k(1+|\Im s|))}
\tag{HS4}
\]

with no exceptional real zero.  In a fixed narrower region, the standard
zero-free-strip logarithmic-derivative estimate gives

\[
\frac{L'}{L}(s,\operatorname{sym}^2f)
=O(\log(k(1+|\Im s|))).
\tag{HS5}
\]

Integrating HS5 on the real segment from \(1\) to \(1+u\) proves HS3.
The local factors are positive for real \(s\ge1\), so the real logarithm
is unambiguous.  This comparison is a classical imported tool, not a
new automorphic zero-free theorem.

The Goldfeld--Hoffstein--Lieman lower bound
\(\mathcal L_f\gg1/\log k\) remains imported from the parent, but it is
no longer needed in the \(X\)-moment estimate below.

---

## 2. Gamma-tail Mellin domination

### Lemma 2.1

For \(a>0\), \(x>0\), and \(0<u\le1\),

\[
Q(a,x)\le \frac{\Gamma(a+u)}{\Gamma(a)x^u}.
\tag{HS6}
\]

If \(a=k\) is a positive integer, then

\[
Q(k,x)\le \left(\frac{k}{x}\right)^u.
\tag{HS7}
\]

#### Proof

Let \(Z\) have Gamma distribution with shape \(a\) and scale \(1\).
Then \(Q(a,x)=\Pr(Z\ge x)\).  Markov's inequality gives

\[
Q(a,x)\le x^{-u}\mathbb E Z^u
=x^{-u}\frac{\Gamma(a+u)}{\Gamma(a)}.
\]

For \(0<u\le1\), Gautschi's inequality gives
\(\Gamma(k+u)/\Gamma(k)\le k^u\). ∎

This is the step that preserves the exact Rankin--Selberg series.  It
replaces the divisor-function majorant of HC8--HC9.

---

## 3. Uniform logarithmic \(X\)-moment

### Theorem 3.1

There is an absolute constant \(C\) such that every level-one normalized
Hecke eigenform of sufficiently large even weight \(k\) satisfies

\[
\boxed{M_X(e_f)\le C\log k.}
\tag{HS8}
\]

#### Proof

Put

\[
u=\frac1{\log k}.
\]

By HS7,

\[
Q(k,4\pi n)
\le
\left(\frac{k}{4\pi n}\right)^u.
\]

Therefore

\[
\begin{aligned}
\sum_{n\ge1}\frac{\lambda_f(n)^2}{n}Q(k,4\pi n)
&\le
\left(\frac{k}{4\pi}\right)^u
\sum_{n\ge1}\frac{\lambda_f(n)^2}{n^{1+u}}\\
&=
\left(\frac{k}{4\pi}\right)^u
\frac{\zeta(1+u)L(1+u,\operatorname{sym}^2 f)}
     {\zeta(2+2u)}.
\end{aligned}
\tag{HS9}
\]

Now

\[
\left(\frac{k}{4\pi}\right)^u\le e,\qquad
\zeta(1+u)\le1+\frac1u\le2\log k,\qquad
\zeta(2+2u)\ge1.
\]

Using HS3 in HS9 gives

\[
\sum_{n\ge1}\frac{\lambda_f(n)^2}{n}Q(k,4\pi n)
\le 2eC_0\,\mathcal L_f\log k.
\tag{HS10}
\]

The part of \(M_X(e_f)\) below \(y=1\) is at most \(1\).  Substitution
of HS10 into the exact identity HS1 proves HS8. ∎

### Why the logarithm is natural

The pole of the nonnegative Rankin--Selberg series in HS2 occurs at
\(s=1\).  The smoothing \(Q(k,4\pi n)\) samples coefficients at length
comparable with \(k\), so a harmonic sum of size \(\log k\) is the
expected scale.  The previous \(\log^5 k\) was not a geometric feature
of Hecke-selected sources; it was the cost of the coefficientwise
\(d_4\) majorant and the separate lower bound for \(\mathcal L_f\).

No lower asymptotic or sharp leading constant is claimed here.

---

## 4. Compression to an arbitrary selected Hecke set

Let \(S_k\) be any subset of the Petersson-orthonormal Hecke eigenbasis,
and let

\[
V(S_k)=\operatorname{span}\{e_f:f\in S_k\},
\qquad r_k=|S_k|.
\]

Let \(T_X\) be the positive form operator obtained by compressing
multiplication by \(X\) to \(V(S_k)\).

### Corollary 4.1

Uniformly over every selection \(S_k\),

\[
\boxed{\|T_X|_{V(S_k)}\|_G\le C r_k\log k.}
\tag{HS11}
\]

#### Proof

A positive finite-dimensional operator has norm at most trace.  In the
orthonormal Hecke basis,

\[
\operatorname{tr}(T_X|_{V(S_k)})
=\sum_{f\in S_k}M_X(e_f)
\le Cr_k\log k
\]

by Theorem 3.1. ∎

No cancellation between different Hecke lines is used.  Hence the result
is uniform over adversarial subsets and not merely over the complete
family or a harmonic average.

---

## 5. Matched-scale endpoint zero-free theorem

Retain the parent period

\[
I_s(u,v)=\int_{\mathcal F}y^k\overline{u(z)}v(z)E^*(z,s)\,d\mu(z).
\]

For a compact set \(\mathcal K\Subset\{\Re c>0\}\), the parent proves the
pointwise Laurent estimate

\[
\left|E^*(z,1-c/k)+\frac{k}{2c}\right|
\le C_{\mathcal K}X(z)
\tag{HS12}
\]

and therefore, for \(u,v\in V(S_k)\),

\[
\left|I_{1-c/k}(u,v)+\frac{k}{2c}G(u,v)\right|
\le
C_{\mathcal K}\sqrt{M_X(u)M_X(v)}.
\tag{HS13}
\]

### Theorem 5.1 — Hecke-support scale closure

Uniformly for \(c\in\mathcal K\),

\[
\boxed{
\frac1k
G_S^{-1/2}I_S(1-c/k)G_S^{-1/2}
=
-\frac1{2c}I
+
O_{\mathcal K}\!\left(\frac{r_k\log k}{k}\right).
}
\tag{HS14}
\]

Consequently:

1. if
   \[
   r_k=o\!\left(\frac{k}{\log k}\right),
   \tag{HS15}
   \]
   the restricted period and every restriction to a subspace of
   \(V(S_k)\) are invertible uniformly on \(\mathcal K\);

2. there is a constant \(\eta_{\mathcal K}>0\) such that the same
   conclusion holds whenever
   \[
   r_k\le \eta_{\mathcal K}\frac{k}{\log k};
   \tag{HS16}
   \]

3. on a fixed positive real \(c\)-interval, all these restrictions are
   negative definite for sufficiently large \(k\);

4. every determinant and every determinant quotient arising from a
   fixed-in-\(s\) flag inside the selected Hecke space has no zero or
   pole in the corresponding endpoint chamber;

5. reflection gives the identical left-endpoint conclusion.

#### Proof

Whiten HS13 by the Petersson Gram.  The operator on its right is bounded
by \(C_{\mathcal K}\|T_X\|\), and Corollary 4.1 gives HS14.  A Neumann
inverse about \(-I/(2c)\) proves HS15--HS16.  Compression to a subspace
cannot increase the error norm.  The real statement follows from
Hermitian symmetry, and reflection is inherited from the completed
period. ∎

This improves HC15 from

\[
O_{\mathcal K}\!\left(\frac{r_k\log^5k}{k}\right)
\]

to

\[
O_{\mathcal K}\!\left(\frac{r_k\log k}{k}\right).
\]

---

## 6. The phase transition now has one scale

The parent proves that every fixed-depth divisor-ladder nullvector carries
asymptotically full Petersson mass above \(y=\eta_Jk\).  Its exact cusp
mass estimate then gives

\[
\text{number of Hecke lines supporting that nullvector}
\ge c_J\frac{k}{\log k}.
\tag{HS17}
\]

It also proves the stronger projection statement

\[
\|\operatorname{proj}_{V(S_k)}v_{i,J,k}\|_G
\le
C_J\sqrt{\frac{r_k\log k}{k}}+o_J(1).
\tag{HS18}
\]

Combining HS14--HS18 yields the matched-scale conclusion:

\[
\boxed{
\begin{array}{c}
r_k=o(k/\log k)
\\[2mm]\Longrightarrow\\[2mm]
\text{endpoint zero-free and asymptotically orthogonal to every
fixed-depth divisor nullvector},
\end{array}
}
\tag{HS19}
\]

whereas an actual divisor-ladder nullvector requires
\(r_k\gg_J k/\log k\).

Thus the former four-logarithm gap is closed.  What remains is a
constant-scale critical window

\[
r_k\asymp \frac{k}{\log k}.
\]

The present proof does not determine a universal sharp constant, and the
constants in the zero-free theorem and the cusp-support obstruction are
not compared.

---

## 7. Scope, failure modes, and review points

### New in this note

* the Gamma-tail Mellin domination HS6--HS9;
* the use of the exact Rankin--Selberg pole together with the near-one
  comparison HS3;
* the uniform \(M_X(e_f)\ll\log k\) theorem;
* the matched endpoint estimate HS14 and scale closure HS19.

### Imported

* all source normalizations and exact identities HS1--HS2;
* the completed Eisenstein Laurent estimate HS12;
* the symmetric-square automorphy, zero-free region, and absence of an
  exceptional real zero;
* the standard zero-free-strip logarithmic-derivative estimate used in
  HS3;
* the parent cusp-support/nullvector theorems.

### Not claimed

* a sharp constant at \(r\asymp k/\log k\);
* zero-freeness for arbitrary rotated rank-\(r\) spaces not contained in
  a selected Hecke span;
* diagonalization of the period in the Hecke basis;
* a growing-depth divisor theorem;
* RH, GRH, or an automorphic purity theorem.

### Priority review points

1. the normalization of HS1 and HS2;
2. the exact range and conductor dependence in the imported comparison
   HS3;
3. the Gamma-moment inequality HS7;
4. the passage from the positive trace HS11 to the operator estimate
   HS14;
5. preservation of the statement under arbitrary internal subspaces.
