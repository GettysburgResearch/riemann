# Exploration: the exact local cost of varying the auxiliary guard

Status: the ramified local Fourier/Mellin identity and its operator norm below
are proved. The varying-prime amplification proposal is exploratory
and does not improve a zero-free boundary. Existing frozen theorem
and review files are not changed by this note.

Question: within the nontrivial ramified character channel, can a different local test, valuation shell, or conductor
reduce the \(q^{1/3}\) normalization paid by the cubic guard at its
principal Mellin point \(s=1/6\)?

## 1. Exact local identity for arbitrary tests

Let \(K\) be a nonarchimedean local field of odd residue cardinality
\(q\), and use an additive character of conductor \(\mathcal O_K\)
and self-dual additive measure \(\operatorname{vol}(\mathcal O_K)=1\).
Fix a uniformizer \(\pi\). Let \(\lambda\) be a nontrivial tame
unitary character on \(\mathcal O_K^\times\), extended by
\(\lambda(\pi)=1\), and put
\[
 \tau_-(\lambda)=
    \sum_{u\in(\mathcal O_K/\pi)^\times}
                    \lambda(u)e(-u/\pi),\qquad
 |\tau_-(\lambda)|=q^{1/2}.
 \tag{1.1}
\]
Normalize multiplicative Haar measure arbitrarily, and write
\(c_K=\operatorname{vol}(\mathcal O_K^\times)\).
For a Schwartz--Bruhat test \(f\), define
\[
 {\cal F}_s(f)=
      \int_{K^\times}\widehat f(y)\lambda(y)|y|^s\,d^\times y,
 \qquad
 {\cal Z}_{1-s}(f)=
      \int_{K^\times}f(x)\overline{\lambda(x)}
                                 |x|^{1-s}\,d^\times x .
 \tag{1.2}
\]
Only the \(\lambda\)-isotypic part of \(f\) contributes to these
functionals. Because \(\lambda\) is nontrivial on units, that part
vanishes in a neighborhood of zero and outside a compact set.
Thus both are finite sums of valuation terms and are entire in \(s\).

The exact identity is
\[
                 {\cal F}_s(f)=
           \tau_-(\lambda)q^{s-1}{\cal Z}_{1-s}(f).
 \tag{1.3}
\]
This formula also fixes the Fourier orientation. Here is an elementary
proof that permits arbitrary local tests, rather than assuming one
unit annulus.

Write the unit-character projection of \(f\) as
\[
 f_\lambda(\pi^a u)=c_a\lambda(u),\qquad
 c_a=c_K^{-1}\int_{\mathcal O_K^\times}
                         f(\pi^a v)\overline{\lambda(v)}\,d^\times v .
 \tag{1.4}
\]
There are only finitely many nonzero \(c_a\). A change of unit
variable shows that all other unit-character components vanish in
(1.2). The Fourier transform of the \(a\)-th shell in (1.4) is
supported exactly on \(v(y)=-a-1\), with
\[
 \widehat f_{\lambda,a}(\pi^{-a-1}u)
                  =c_a q^{-a-1}\tau_-(\lambda)
                         \overline{\lambda(u)}.
 \tag{1.5}
\]
Its contribution to \({\cal F}_s\) is
\[
 c_K c_a\tau_-(\lambda)q^{s-1}q^{-a(1-s)}.
 \tag{1.6}
\]
The last factor, without \(\tau_-(\lambda)q^{s-1}\), is the
contribution to \({\cal Z}_{1-s}\). Summing proves (1.3).

## 2. Sharp weighted operator norm

For real \(0<\sigma<1\), equip the physical test with the weighted
absolute norm
\[
            \|f\|_{\mathrm{phys},\sigma}
               =\int_{K^\times}|f(x)|\,|x|^{1-\sigma}\,d^\times x .
 \tag{2.1}
\]
Equation (1.3) and the triangle inequality give
\[
 \boxed{\quad
 |{\cal F}_{\sigma+it}(f)|
       \le q^{\sigma-1/2}\|f\|_{\mathrm{phys},\sigma}.
 \quad}
 \tag{2.2}
\]
The constant is sharp. At \(t=0\), take
\(f(x)=\lambda(x)h(|x|)\), where \(h\ge0\) is any nonzero
finitely supported radial function. At nonzero \(t\), insert the
corresponding unit-modulus radial phase so that the integrand in
\({\cal Z}_{1-s}\) has constant argument.

In particular
\[
            \|{\cal F}_{1/6}\|_{\mathrm{phys},1/6}
                                =q^{-1/3}.
 \tag{2.3}
\]
Moving the test to another valuation shell changes the two sides
of (1.3) by the same physical weight. Superposing shells, signed
tests, or smooth unit profiles cannot increase the normalized
principal Mellin functional. This is an exact local norm statement;
it does not assume that a particular global Cauchy bound is sharp.

For a primitive unitary character of conductor \(\pi^h\), the same
calculation uses the Gauss sum modulo \(\pi^h\), of magnitude
\(q^{h/2}\), and Fourier valuation \(-a-h\). The norm in (2.2)
is \(q^{h(\sigma-1/2)}\); at \(1/6\) it is \(q^{-h/3}\).
Thus deeper conductor only increases the cost. At the good primes
of the cubic guard, every nontrivial cubic character is tame, so
\(h=1\) is already the least possible conductor.
For a product of independent local guard characters, the exact
cost is the conductor norm to the power \(-1/3\).

## 3. Valuation selectors do not bypass this cost

Suppose a local test is supported on \(v(x)=a\), and the physical
norm-one probe is restricted to \(v(t_0)\equiv b\pmod6\).
The physical row has valuation \(a+b\bmod6\). In the high
Poisson variable the principal frequency survives only when
\[
                            b\equiv-a-1\pmod6,
 \tag{3.1}
\]
by (1.5). Hence the surviving physical rows always have valuation
\(-1\bmod6\). With the cubic twist of digit \(2\), their actual
theta digit is \(-2-1=3\), as required for cancellation.

This permits any shell \(a\), with its corresponding selector,
but it does not alter (2.3). For a fixed selector and a sum of
shells, only the congruence class \(a\equiv-b-1\pmod6\) contributes
to the principal functional. Applying (1.3) to that projection
gives the same bound. Finite linear combinations of selectors have
the same estimate when charged with the sum of their physical norms.

## 4. What a varying-prime cubic amplifier would still need

Every fixed auxiliary-prime probe targets the same original
reciprocal, so one can formally align their principal phases.
Equation (2.3) says that a prime of norm about \(P\) must be
normalized by \(P^{1/3}\), relative to its physical test norm,
before its principal Mellin term has unit size.

In the native Eisenstein presentation, write the physical row as
\(m=a/\pi\). The inserted cubic twist and the row symbol combine
in the theta coefficient as
\[
 \psi(A)^{-1}\chi_A(m)
       =\chi_A(a)\chi_A(\pi)^{-3}.
 \tag{4.1}
\]
The Gauss dilation in the additive factor combines with
\(\psi(s)^{-1}\) to give \(\chi_s(\pi)^{-1}\). Its row phase is
\(\chi_\pi(a)^2\), in the adapted reciprocal convention.
Thus the new prime is coupled to both columns and the row.
It is not a collection of independent copies of the same detector.

As a coarse diagnostic only, if a nonprincipal average over these
primes were bounded by \(P^{\beta+\epsilon}\) using only the
available zero-free input, the local normalization would change
that to \(P^{\beta+1/3+\epsilon}\). This would beat a coherent
\(P\)-sized principal sum only for \(\beta<2/3\), far below the
current boundary. The exact sixth-power cases of the coupled
numerator also require separate analysis and cannot be included
in that nonprincipal estimate.

A better result would need cancellation in this coupled average
beyond the pointwise prime bound, while preserving those principal
configurations and the physical weights. The ramified local Fourier/Mellin
operator itself offers no smaller conductor cost. The separate exploratory
note ODD_CLASS_GUARD_EXPLORATION.md studies a cheaper unramified odd-class
probe, proves its unavoidable leakage into other frequency valuation
classes, and explains why it still gives no numerical boundary gain.
