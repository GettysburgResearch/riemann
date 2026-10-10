# Exact scalar in the mixed sextic reflection

Status: exact source-level arithmetic identity, 2026-10-10. This calculation audits the full scalar in the imported reflection, including its angular factor. It does not prove a new moment estimate or supply a new completed-theta theorem.

Source: OpenAI `math` commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, October 5 `build/paper2.tex`, the arithmetic identities at lines 800–861, local transform at lines 3231–3269, and full reflection scalar at lines 3414–3424. The completed reflection itself is an input. The present calculation is elementary once those displayed source formulas are granted.

## 1. Precise mixed branch

Let \(k,a\) be coprime squarefree primary elements outside the fixed bad-prime set. At the primes of \(k\), take local exponent \(j=1\); at those of \(a\), take \(j=4\). All these primes are active. Write

\[
r=ka,\qquad c=c_0r,\qquad t=\lambda^2c_0,
\qquad \lambda=\sqrt{-3}.
\]

The fixed bad-prime translate and ray class fix \(c_0\), the initial frequency label \(h_0\), and \(\kappa_0\). In particular, this is a branchwise identity: the finite ray-class dependence is retained, rather than declared uniform without splitting. There are no further active or inactive good primes in the branch considered here.

The source scalar is

\[
C=-\frac{i}{81}\overline{\alpha(c)}^{\,2}
\widehat\phi(h_0)\overline{\kappa_0}
\prod_{p\mid r}\chi_p(\sigma_p)^{-2}\omega_{p,j_p},
\qquad
\sigma_p=\lambda^2c/p,
\]

where \(\alpha(x)=x/|x|\). Its local factors are

\[
\omega_{p,1}=\chi_p(-1)\gamma_1(p)\gamma_3(p)
                  \chi_p(\epsilon_p)^{-3},
\qquad
\omega_{p,4}=\gamma_4(p),
\quad
\epsilon_p=-\lambda^{-5}(c/p)^{-2}.
\]

All displayed arguments of negative powers are units modulo their character modulus.

## 2. Simplify the local exponent-one factor

Since the sixth power of a nonzero sextic value is one,

\[
\chi_p(\epsilon_p)^{-3}
=\chi_p(-1)^{-3}\chi_p(\lambda)^{15}\chi_p(c/p)^6.
\]

Also \(\chi_p(-1)^2=1\). Therefore

\[
\omega_{p,1}=\gamma_1(p)\gamma_3(p)\chi_p(\lambda)^3.
\tag{2.1}
\]

The dependence on \(c/p\) cancels in this local factor. It remains in the separate \(\sigma_p\) product and cannot yet be discarded.

The source Gauss identities give

\[
\gamma_2(p)\gamma_4(p)=1,\quad
\gamma_1(p)\gamma_2(p)=-\alpha(p)G(p),\quad
G(p)=\chi_p(4)^{-1}\gamma_3(p),\quad
\gamma_3(p)^2=\chi_p(-1).
\]

Consequently

\[
\frac{\omega_{p,1}}{\gamma_4(p)}
=-\alpha(p)\chi_p(-1)\chi_p(4)^{-1}\chi_p(\lambda)^3.
\tag{2.2}
\]

## 3. Aggregate the CRT factors before cancellation

For squarefree \(r\), the normalized Gauss sum obeys the exact CRT formula

\[
\gamma_j(r)=\prod_{p\mid r}\gamma_j(p)
                \prod_{p\mid r}\chi_p(r/p)^j.
\tag{3.1}
\]

This follows by expanding a residue modulo \(r\) in CRT coordinates and rescaling the local additive characters. There is no unspecified scalar in (3.1).

As \(-2\equiv4\pmod6\) and \(\sigma_p=t(r/p)\), (3.1) yields

\[
\prod_{p\mid r}\chi_p(\sigma_p)^{-2}\gamma_4(p)
=\chi_r(t)^{-2}\gamma_4(r).
\tag{3.2}
\]

Combining (2.2) and (3.2), the complete active-prime product in \(C\) is

\[
\mu(k)\alpha(k)
\chi_k(-1)\chi_k(4)^{-1}\chi_k(\lambda)^3
\chi_{ka}(t)^{-2}\gamma_4(ka).
\tag{3.3}
\]

For coprime \(k,a\), sextic reciprocity has a fixed-ray sign \(\mathcal R(a,k)\). Its fourth power is one, so another exact CRT identity is

\[
\gamma_4(ka)
=\gamma_4(k)\gamma_4(a)\chi_a(k)^2.
\tag{3.4}
\]

## 4. Multiply by the outer cubic coefficient

Let the outer coefficient be exactly

\[
a_\xi(a)=\overline{\alpha(a)}\gamma_2(a)\xi(a).
\]

Define

\[
F=-\frac{i}{81}\overline{\alpha(c_0)}^{\,2}
                   \widehat\phi(h_0)\overline{\kappa_0},
\]

\[
\Gamma(k)=\mu(k)\overline{\alpha(k)}\gamma_4(k)
\chi_k(-1)\chi_k(4)^{-1}\chi_k(\lambda)^3\chi_k(t)^{-2},
\qquad
\Xi(a)=\xi(a)\chi_a(t)^{-2}.
\]

Then the exact scalar identity is

\[
\boxed{\quad
C\,a_\xi(a)
=F\,\Gamma(k)\,\Xi(a)\,
\overline{\alpha(a)}^{\,3}\chi_a(k)^2.
\quad}
\tag{4.1}
\]

Indeed, insert (3.3) and (3.4), cancel \(\gamma_2(a)\gamma_4(a)=1\), and use

\[
\overline{\alpha(c)}^{\,2}\alpha(k)\overline{\alpha(a)}
=\overline{\alpha(c_0)}^{\,2}
 \overline{\alpha(k)}\overline{\alpha(a)}^{\,3}.
\]

Here \(|\Gamma(k)|=|\Xi(a)|=1\). Since \(t\) is supported at the fixed bad primes, its supplementary symbol factors are fixed-ray functions after the source's prescribed ray-class split. The factor \(F\) is fixed on each such branch. The angular factor \(\overline{\alpha(a)}^3\) is not a fixed-ray factor and is not deleted.

If the original balanced coefficient also contains the literal external factor \(\chi_a(k)\), multiplication gives

\[
\boxed{\quad
\chi_a(k)\,C\,a_\xi(a)
=F\,\Gamma(k)\,\Xi(a)\,
\overline{\alpha(a)}^{\,3}\chi_a(k)^3.
\quad}
\tag{4.2}
\]

Thus the remaining cross-symbol is quadratic. If it is rewritten with denominator \(k\), reciprocity contributes the sign \(\mathcal R(a,k)\), which must be retained or absorbed only after the fixed ray split. The angular weight also remains.

## 5. Scope of the gain

The outer cubic Gauss factor really cancels after the entire CRT scalar is accounted for. Equations (4.1)–(4.2) expose the exact remaining oscillation for a coupled estimate. They do not justify taking the divisor sum outside the reflection, deleting its angular factor, or applying a quadratic sieve before identifying all row-dependent coefficients. Branches with overlapping \(k,a\), extra active good-prime factors, or other local exponents require their own calculation.
