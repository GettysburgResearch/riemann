> Part of the [PR #766/#769/#781 proof-oriented synthesis packet](README.md).

# 3. New Theorem II: cycle-index alternants reconstruct the full \(S_m\)-equivariant Euler character

The ordinary alternant of T-108522 sees only the trace of the identity permutation on the tensor factors. That cannot determine the \(S_m\)-isotypic refinement. The correct replacement is a family of twisted alternants indexed by conjugacy classes.

## Theorem II

For \(\tau\in S_m\), define the twisted Hilbert series

\[
F^\tau_{d,m}(A,T)
=
\sum_{r\ge0}
\operatorname{Tr}\!\left(
(A,\tau)\mid(\operatorname{Sym}^rV)^{\otimes m}
\right)T^r,
\]

and the twisted numerator

\[
N^\tau_{m,d}(A,T)
=
\det(1-TA\mid\operatorname{Sym}^mV)
F^\tau_{d,m}(A,T).
\]

Let the cycle lengths of \(\tau\) be
\(\ell_1,\ldots,\ell_a\). Then

\[
F^\tau_{d,m}(A,T)
=
\sum_{r\ge0}
\prod_{\nu=1}^{a}
h_r(A^{\ell_\nu})\,T^r,
\]

where \(h_r(A^\ell)=\operatorname{Tr}(A^\ell\mid\operatorname{Sym}^rV)\).

Consequently:

1. \(N^\tau_{m,d}\) is a polynomial and equals the class trace of \(\tau\) on the alternating Chow-base Tor character:
   \[
   N^\tau_{m,d}(A,T)
   =
   \sum_{q,j}(-1)^q
   \operatorname{Tr}\!\left((A,\tau)\mid B_{q,j}\right)T^j.
   \]

2. T-108522's multilinear alternant applied to the alphabets
   \[
   \{x_1^{\ell_\nu},\ldots,x_d^{\ell_\nu}\}
   \]
   gives an explicit finite alternant expression for every \(N^\tau_{m,d}\).

3. Write the virtual \(S_m\)-isotypic decomposition as
   \[
   \mathcal N_{m,d}(T)
   =
   \sum_{\lambda\vdash m}
   \mathcal N_\lambda(T)\otimes[\lambda].
   \]
   Then character orthogonality reconstructs every multiplicity-character polynomial:
   \[
   \mathcal N_\lambda(A,T)
   =
   \frac1{m!}
   \sum_{\tau\in S_m}
   \chi_\lambda(\tau^{-1})
   N^\tau_{m,d}(A,T).
   \]

Thus the full \(GL(V)\times S_m\) **alternating Tor character** is reconstructed from cycle-index alternants.

## Proof

Let \(U_r=\operatorname{Sym}^rV\) and let \(B=\operatorname{Sym}^rA\). The standard tensor-cycle trace identity is

\[
\operatorname{Tr}\!\left(B^{\otimes m}\tau\mid U_r^{\otimes m}\right)
=
\prod_{c\in\operatorname{Cycles}(\tau)}
\operatorname{Tr}(B^{|c|}\mid U_r).
\]

Functoriality of symmetric powers gives
\(B^{|c|}=\operatorname{Sym}^r(A^{|c|})\), yielding the displayed formula for \(F^\tau\).

The \(S_m\)-action on the base \(W=\operatorname{Sym}^mV\) is trivial. Therefore the same equivariant Hilbert-series computation as in [Theorem I](THEOREM_I.md) gives the twisted numerator as the class trace on the Tor Euler characteristic.

The multilinear alternant theorem applies first on the dense locus where the relevant powered eigenvalue alphabets are separated, and then extends as a polynomial identity.

Finally, if
\(\mathcal N=\sum_\lambda\mathcal N_\lambda\otimes[\lambda]\), then

\[
N^\tau=\sum_\lambda\chi_\lambda(\tau)\mathcal N_\lambda.
\]

The irreducible character orthogonality relations invert this system.

\(\square\)

## Rank-three, power-three reconstruction

For \(m=3\), write

\[
N_e=
D_W\sum_r h_r(A)^3T^r,
\]

\[
N_t=
D_W\sum_r h_r(A)h_r(A^2)T^r,
\]

\[
N_c=
D_W\sum_r h_r(A^3)T^r,
\]

for the identity, transposition, and three-cycle classes. If
\(\mathcal N_{\mathbf1},\mathcal N_\varepsilon,\mathcal N_\sigma\)
are the three \(S_3\)-multiplicity polynomials, then

\[
\mathcal N_{\mathbf1}
=
\frac{N_e+3N_t+2N_c}{6},
\]

\[
\mathcal N_{\varepsilon}
=
\frac{N_e-3N_t+2N_c}{6},
\]

\[
\mathcal N_{\sigma}
=
\frac{N_e-N_c}{3}.
\]

Using the exact PR #769 Tor table gives the full identity in
\(R(GL_3\times S_3)[T]\):

\[
\begin{aligned}
\mathcal N_{3,3}(T)
={}&[000]\otimes\mathbf1\\
&+\bigl([210]\otimes\sigma+[111]\otimes\varepsilon\bigr)T\\
&+\bigl([222]\otimes\mathbf1+[330]\otimes\varepsilon
-[411]\otimes\sigma\bigr)T^2\\
&-\bigl([522]\otimes(\mathbf1+\sigma)
+([531]+[432])\otimes\varepsilon\bigr)T^3\\
&+\bigl([552]\otimes(\mathbf1+\sigma)
+([642]+[543])\otimes\varepsilon\bigr)T^4\\
&+\bigl([663]\otimes\sigma-[555]\otimes\mathbf1
-[744]\otimes\varepsilon\bigr)T^5\\
&-\bigl([765]\otimes\sigma+[666]\otimes\varepsilon\bigr)T^6\\
&-[777]\otimes\mathbf1\,T^7.
\end{aligned}
\]

Forgetting \(S_3\) but retaining its dimensions gives the exact
\(GL_3\)-representation-ring expansion of the ordinary alternant:

\[
\begin{aligned}
N_{3,3}(T)
={}&1+(2[210]+[111])T\\
&+([222]+[330]-2[411])T^2\\
&-(3[522]+[531]+[432])T^3\\
&+(3[552]+[642]+[543])T^4\\
&+(2[663]-[555]-[744])T^5\\
&-(2[765]+[666])T^6-[777]T^7.
\end{aligned}
\]

This is the requested term-by-term reconciliation, not merely a dimension check.

For example, the scalar coefficient \(-9\) in degree two is

\[
\dim[222]+\dim[330]-2\dim[411]
=
1+10-20.
\]

It hides genuine generators and relations; it is not a Betti number.

## Exact no-go correction

The ordinary alternant \(N_e\) alone cannot reconstruct the \(S_3\)-refinement. The forgetful map

\[
R(GL_3\times S_3)\longrightarrow R(GL_3),
\qquad
U\otimes\rho\longmapsto(\dim\rho)\,U
\]

has nonzero kernel. For example,

\[
U\otimes(\sigma-\mathbf1-\varepsilon)
\]

maps to zero because \(2-1-1=0\). Therefore any assertion that the ordinary alternant canonically determines the factor-permutation representations is false. The transposition and three-cycle alternants are the minimal correction.

---
