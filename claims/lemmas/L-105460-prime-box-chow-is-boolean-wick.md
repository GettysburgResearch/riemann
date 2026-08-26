# L-105460 — The prime-box Chow algebra is the Boolean/Wick source algebra

Claim ID: `L-105460`

Status: **PROVED EXACT FINITE SOURCE-ALGEBRA IDENTIFICATION**

Fix a finite labelled prime set \(\mathcal P\); the two labelled copies of the
marked prime \(67\) remain distinct.  The degree-graded Chow algebra used by the
finite prime-box model is

\[
\mathscr C_{\mathcal P}
 =
 \mathbf Q[h_p:p\in\mathcal P]/(h_p^2:p\in\mathcal P).
\tag{L-105460.1}
\]

For \(S\subseteq\mathcal P\), put \(h_S=\prod_{p\in S}h_p\).  Then

\[
\boxed{
h_Ah_B=
\begin{cases}
h_{A\sqcup B},&A\cap B=\varnothing,\\
0,&A\cap B\ne\varnothing.
\end{cases}}
\tag{L-105460.2}
\]

Thus multiplication in \(\mathscr C_{\mathcal P}\) is exactly disjoint-support
Boolean convolution.  In particular, if \(F,G\) are coefficient functions on
the Boolean cube and

\[
[F]=\sum_S F(S)h_S,\qquad [G]=\sum_SG(S)h_S,
\]

then

\[
[F][G]=[F\star G].
\tag{L-105460.3}
\]

No quotient is being taken after multiplication: the square-zero relation is
the literal self-intersection rule of each prime divisor.

## 1. The F1 half-Euler class

Define

\[
\mathfrak h
 =
 \prod_{p\in\mathcal P}\left(1-\frac12h_p\right).
\]

Since \(h_p^2=0\),

\[
\left(1-\frac12h_p\right)^2=1-h_p.
\]

Tensoring over the labelled prime box gives

\[
\boxed{
\mathfrak h^2
 =
 \prod_{p\in\mathcal P}(1-h_p).
}
\tag{L-105460.4}
\]

Coefficientwise, this is

\[
h(S)=\left(-\frac12\right)^{|S|},
\qquad
h\star h=\mu_{\rm sf}.
\tag{L-105460.5}
\]

Hence the Boolean square root of the squarefree Möbius class is the ordinary
square root **inside the Chow algebra**.

## 2. The balanced Vaughan class

Let

\[
a_U=\varepsilon-\mu_U\star\mathbf 1_{\rm sf},
\qquad
f_U=a_U\star h.
\]

Write \(\mathfrak a_U,\mathfrak f_U\) for their classes in
\(\mathscr C_{\mathcal P}\).  The balanced coefficient is

\[
b_U=a_U\star a_U\star\mu_{\rm sf}.
\]

Using (L-105460.4),

\[
\boxed{
\mathfrak b_U
 =
 \mathfrak f_U^2,
\qquad
b_U=f_U\star f_U.
}
\tag{L-105460.6}
\]

This is a coefficientwise finite identity.  It imports no analytic
continuation and no positivity after physical collapse.

## 3. Physical realization and its correct product

Give a singleton label either the owner atom

\[
x_p=p^{-1/2}U_p
\]

or the completed core atom

\[
y_p=p^{-1}U_{p^2}.
\]

The physical realization map is an algebra homomorphism precisely when the
target is equipped with the disjoint-label Wick–Mellin product:

\[
\boxed{
\rho_{\rm Wick}(FG)
 =
 \rho_{\rm Wick}(F)\diamond_M\rho_{\rm Wick}(G).
}
\tag{L-105460.7}
\]

It is not an algebra homomorphism into ordinary Mellin convolution, because

\[
h_p^2=0
\quad\hbox{whereas}\quad
x_p*_Mx_p=p^{-1}U_{p^2}\ne0.
\]

The defect between the two target products is the diagonal contraction ideal,
treated in `L-105462`.

## Meaning

The source geometry is now literal:

```text
finite prime-box Chow multiplication
  =
disjoint-support Boolean convolution
  =
Wick normal ordering of prime labels.
```

The remaining difficulty cannot come from choosing a square root of the
Boolean source.  It enters only when the F1 configuration class is physically
collapsed into multiplicative translations.
