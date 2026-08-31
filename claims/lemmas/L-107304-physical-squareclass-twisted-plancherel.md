# L-107304 — Physical squareclass multiplication is a rank-free twisted Plancherel operator

Claim ID: `L-107304`  
Programme aliases: `RIEMANNSTRUCT.SQUARECLASS_PLANCHEREL`, `LFAM2.KUMMER_CONVOLUTION_NORM`  
Status: **PROVED EXACT FINITE-FOURIER OPERATOR THEOREM**  
Created: 2026-08-30  
Depends on: `L-107300--L-107302`  
Programme issues: #763, #737, #739  
RH/GRH status: **not assumed**

Let \(X\) be a finite abelian group of order \(m\), and let
\(S:X	o X\) be the square map \(S(y)=y^2\). For functions
\(A,B:X	o\mathbf C\), define the physical squareclass convolution

\[
oxed{
(A\star_2 B)(r)
=
\sum_{\substack{x,y\in X\\xy^2=r}}A(x)B(y).
}
	ag{L-107304.1}
\]

Use the unnormalized Fourier transform

\[
\widehat f(\chi)=\sum_{x\in X}f(x)\overline{\chi(x)}.
\]

## 1. Exact diagonalization

A change of variables gives

\[
oxed{
\widehat{A\star_2 B}(\chi)
=\widehat A(\chi)\widehat B(\chi^2).
}
	ag{L-107304.2}
\]

Consequently Parseval gives

\[
oxed{
\|A\star_2B\|_2^2
=
rac1m\sum_{\chi\in\widehat X}
|\widehat A(\chi)|^2|\widehat B(\chi^2)|^2.
}
	ag{L-107304.3}
\]

This is the exact Fourier form of the physical map
\((Q,d)\mapsto Qd^2\).

## 2. Reduced augmentation norm

Let \(P^{m nr}\) be the projection onto the characters satisfying

\[
\chi
e1,\qquad \chi^2
e1.
\]

For fixed \(B\), put

\[
T_BA=P^{m nr}(A\star_2B).
\]

Then

\[
oxed{
\|T_B\|_{\ell^2(X)	o\ell^2(X)}
=
\max_{\substack{\chi\in\widehat X\\\chi
e1,\ \chi^2
e1}}
|\widehat B(\chi^2)|.
}
	ag{L-107304.4}
\]

The upper bound follows from (L-107304.3), and equality is attained by one
Fourier basis vector.

Thus complete physical occupancy in one reduced Kummer fibre costs the
largest surviving core character coefficient. It does **not** cost the number
of characters or the rank of the augmentation sheaf.

## 3. Two-place tensor

For two conductor groups \(X_\ell,X_ho\), the complete shared-fibre map is
the tensor product of the two operators. Hence

\[
oxed{
\|T_{B_\ell}\otimes T_{B_ho}\|
=
\left(\max_{\chi^2
e1}|\widehat B_\ell(\chi^2)|ight)
\left(\max_{	heta^2
e1}|\widehat B_ho(	heta^2)|ight).
}
	ag{L-107304.5}
\]

No family-size factor appears.

## 4. Squareclass specialization

For \(X=\mathbf F_Q^	imes/\{\pm1\}\), the characters of \(X\) are exactly the
even multiplicative characters. The omitted modes in \(P^{m nr}\) are
precisely the principal mode and the possible even quadratic mode classified
in `L-107301`.

## Scope

The theorem is exact for complete convolution fibres. A live shell or incidence
mask which couples owner and core variables need not factor as \(A(x)B(y)\);
that boundary is recorded in `R-107301`.
