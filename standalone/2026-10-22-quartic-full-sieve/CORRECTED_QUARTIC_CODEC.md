# Corrected quartic Gauss-square identity

**Status:** exact algebraic correction, with proof. It restores the pure
angular form of the quartic coefficient conversion. It does not establish
a new inverse moment or zero-free region.

The primary source used here is David--Dunn--Hamieh--Lin (DDHL),
[*Quartic Gauss sums over primes and metaplectic theta functions*,
arXiv:2306.11875v4](https://arxiv.org/html/2306.11875v4), especially
(3.4)--(3.12). Formula (3.11) in that inspected version includes a quadratic
self-symbol that must be retained until it is evaluated. Omitting it gives
an incorrect extra finite ray character.

## 1. Correct statement

Let \(F=\mathbb Q(i)\), \(\lambda=1+i\), and let \(c\) be a nonzero
primary Gaussian integer prime to \(\lambda\). Use the DDHL convention

\[
 g_4(c)=\sum_{x\bmod c}\left(\frac{x}{c}\right)_4
       e\left(\operatorname{Tr}_{F/\mathbb Q}(x/c)\right),
 \qquad \widetilde g_4(c)=\frac{g_4(c)}{\sqrt{Nc}}.
\]

Write \(\alpha(c)=c/|c|\). Then, including nonsquarefree \(c\),

\[
 \boxed{\widetilde g_4(c)^2=\mu_F(c)\alpha(c).}
 \tag{1.1}
\]

In particular the corrected identities for the first Poisson coefficient
are

\[
 \boxed{\mu_F(c)\widetilde g_4(c)
       =\alpha(c)\overline{\widetilde g_4(c)},\qquad
 \mu_F(c)\overline{\widetilde g_4(c)}
       =\alpha(c)^{-1}\widetilde g_4(c).}
 \tag{1.2}
\]

These hold literally at the zeros as well. The conversion introduces the
angular character \(\alpha^{\pm1}\), without an additional factor
\(\big(\frac{-1}{c}\big)_4\). Separate ray factors already present in a
Poisson formula must of course still be retained.

## 2. Split primes: the self-symbol cancels the finite sign

Let \(\pi=a+bi\) be a primary Gaussian prime of degree one. Then
\(p=N\pi=a^2+b^2\) is a rational prime with \(p\equiv1\pmod4\),
\(a\) is odd, \(b\) is even, and \((a,b)=1\). DDHL (3.11) states

\[
 g_4(\pi)^2
 =-\left(\frac{-1}{\pi}\right)_4
    \left(\frac{\bar\pi}{\pi}\right)_4^{-2}
       \sqrt p\,\pi.
 \tag{2.1}
\]

The self-symbol is quadratic. Since \(\bar\pi\equiv2a\pmod\pi\)
and \(\mathbb Z[i]/(\pi)\cong\mathbb F_p\),

\[
 \left(\frac{\bar\pi}{\pi}\right)_4^{-2}
   =\left(\frac{2a}{p}\right).
 \tag{2.2}
\]

Here the right side is a rational Legendre symbol. Quadratic reciprocity,
using \(p\equiv1\pmod4\), gives

\[
 \left(\frac{a}{p}\right)
 =\left(\frac{|a|}{p}\right)
 =\left(\frac{p}{|a|}\right)
 =\left(\frac{b^2}{|a|}\right)=1.
 \tag{2.3}
\]

The symbols with denominator \(|a|\) are Jacobi symbols; the case
\(|a|=1\) has value one. The sign of \(a\) causes no change because
\(\big(\frac{-1}{p}\big)=1\). Therefore

\[
 \left(\frac{\bar\pi}{\pi}\right)_4^{-2}
 =\left(\frac2p\right)
 =(-1)^{(p-1)/4}
 =\left(\frac{-1}{\pi}\right)_4.
 \tag{2.4}
\]

The two finite signs in (2.1) cancel. Dividing by \(p\) gives

\[
 \widetilde g_4(\pi)^2=-\frac\pi{\sqrt p}
 =\mu_F(\pi)\alpha(\pi).
 \tag{2.5}
\]

Thus the self-symbol is not generally one. Its exact value is what removes
the other finite sign.

## 3. Inert primes: Frobenius makes the Gauss sum real

Let \(p\equiv3\pmod4\) be a rational prime. Its primary Gaussian
generator is \(\pi=-p\), of norm \(p^2\). Work in the residue field
\(\mathbb F_{p^2}\). Let \(\chi\) be the quartic multiplicative
character and \(\psi\) the nontrivial additive character induced by the
DDHL trace convention.

Frobenius sends \(\chi\) to its conjugate, since \(p\equiv-1\pmod4\),
and preserves \(\psi\), since the latter is a trace character. Changing
variables by Frobenius therefore gives

\[
 g(\chi,\psi)=g(\bar\chi,\psi).
 \tag{3.1}
\]

Also \(p^2\equiv1\pmod8\), so \(\chi(-1)=1\). Complex
conjugation of the finite sum, followed by \(x\mapsto-x\), yields

\[
 \overline{g(\chi,\psi)}
   =\bar\chi(-1)g(\bar\chi,\psi)=g(\chi,\psi).
 \tag{3.2}
\]

Thus the Gauss sum is real. Its absolute value is \(p\), by the standard
finite-field Gauss norm, equivalently DDHL (3.8). Its sign need not be
chosen: its square is \(p^2\). Consequently

\[
 \widetilde g_4(-p)^2=1
 =(-1)(-1)=\mu_F(-p)\alpha(-p).
 \tag{3.3}
\]

This proves the required identity without assuming that the normalized
inert Gauss sum itself is always \(+1\).

## 4. Composite moduli and literal zeros

For coprime primary \(c,d\), the CRT formula gives

\[
 \widetilde g_4(cd)
 =\left(\frac cd\right)_4\left(\frac dc\right)_4
       \widetilde g_4(c)\widetilde g_4(d).
 \tag{4.1}
\]

The square of the CRT phase is one, by quadratic reciprocity in
\(\mathbb Z[i]\), or by squaring the quartic reciprocity formula. Hence
\(\widetilde g_4(c)^2\) is multiplicative on coprime primary moduli.
Equations (2.5) and (3.3) prove (1.1) for every squarefree modulus. The
unit modulus gives \(1=1\).

For a nonsquarefree modulus, DDHL (3.7), (3.12) give
\(\widetilde g_4(c)=0\), while \(\mu_F(c)=0\). Thus (1.1) remains
valid. For squarefree \(c\), multiply (1.1) by
\(\overline{\widetilde g_4(c)}\) and use
\(|\widetilde g_4(c)|=1\) to obtain (1.2). For nonsquarefree \(c\),
both sides of each identity in (1.2) are zero.

## 5. An exact counterexample to the old extra-ray formula

Take the primary prime \(\pi=-1+2i=1+\lambda^3\), with \(N\pi=5\).
Then

\[
 \left(\frac{-1}{\pi}\right)_4=-1,\qquad
 \left(\frac{\bar\pi}{\pi}\right)_4^{-2}
   =\left(\frac35\right)=-1.
\]

The corrected value is

\[
 \widetilde g_4(\pi)^2=\frac{1-2i}{\sqrt5}.
 \tag{5.1}
\]

The expression
\(\mu_F(\pi)\big(\frac{-1}{\pi}\big)_4\pi/|\pi|\)
instead equals \((-1+2i)/\sqrt5\), its negative.

This can also be checked directly with no numerical approximation. In the
residue field, \(i\equiv3\pmod\pi\), so the quartic character on
\(1,2,3,4\) is \(1,-i,i,-1\), and the additive character is
\(x\mapsto e(-2x/5)\). Hence

\[
 g_4(\pi)=2\sin(2\pi/5)-2i\sin(\pi/5),\qquad
 g_4(\pi)^2=\sqrt5(1-2i),
\]

which gives (5.1) after dividing by five.

## 6. Consequences and limits

The correction preserves the intended order-matching feature: a quartic
inverse's first Poisson coefficient is converted to a quartic Gauss
coefficient with fixed angular type \(\pm1\). DDHL's completed series
for that nonzero angular type are entire, as stated in their Proposition
4.3. The correction removes the erroneous additional ray factor; it does
not justify replacing the scalar primitive norm by a full invariant matrix
norm, deleting its companion component, or subtracting an unverified
spectral main term.

The primitive-sieve tail estimate and the all-row completion identities in
this research packet use the local Gauss and CRT formulas directly. Their
proofs do not depend on the incorrect extra-ray formula. The unresolved
step remains a centered, uniformly controlled low-divisor automorphic
estimate with the correct arithmetic diagonal.
