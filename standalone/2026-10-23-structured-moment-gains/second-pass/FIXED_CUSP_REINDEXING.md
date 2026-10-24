# Exact fixed-cusp reindexing in the completed cubic reflection

This note isolates the finite-place identities needed to test the signed
quadratic diagonal after **both** raw completion inversions. It proves
identities for the complete finite Fourier sum; it does not estimate the
nonprincipal moving-conductor terms or the full inverse moment.

## 1. Pinned input and notation

The input is `openai/math`, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
`preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`,
Proposition `prop:completed-reflection` and equations
`eq:reflection-row-phase`, `eq:reflection-cusp-fraction`,
`eq:reflection-multiplier`, `eq:reflection-additive-phase`, and
`eq:reflection-cross-prime-phase`. Its local copy has SHA256
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.

For the theta coefficients we use Dunn--Radziwill,
*Bias in cubic Gauss sums: Patterson's conjecture*,
[arXiv:2109.07463v3](https://arxiv.org/html/2109.07463v3),
(5.7), (5.13), (5.14), (5.16), and Appendix A, rows 1, 19, 10.
These explicit coefficient and automorphy identities are unconditional;
the paper's conditional prime asymptotic is not used.

Retain the pinned source's Eisenstein field, fixed bad-prime set `S`,
fixed modulus `L`, fixed finite-ray character `Psi_0`, and finite Fourier
mask

\[
 \phi(x)=1_{x\equiv1\ (3),\,(x,L)=1}
          \left(\frac\lambda x\right)_3\Psi_0(x),
 \qquad
 \widehat\phi(h)=N(L)^{-1}\sum_{x\bmod L}\phi(x)e(-hx/L).
\tag{1}
\]

On the indicated subgroup of units this is a multiplicative character.
For every primary `a` prime to `L`, finite Fourier inversion gives

\[
 \widehat\phi(ah)=\phi(a)^{-1}\widehat\phi(h)
 \quad\text{for every }h\bmod L,
\tag{2}
\]

including nonunit and zero `h`. Indeed, substitute `x=a^{-1}y` in the
finite sum. Multiplication by `a` preserves both zero branches of (1).

Let `r` be an active squarefree good radical, with exponents `j_p` and
put `e_p=2j_p+2` (read modulo six). For each `h mod L`, write

\[
 \lambda^2h/L=a_F/c_F
\]

in the normalized reduced form of the source. Thus `c_F` is supported
on `S`. The source selects a cusp function `d_H`, a scalar `kappa_F`,
and an additive character `vartheta_{h,r}`. Its moving-prime phase is

\[
 \chi_p(\sigma_p)^{-2}\omega_{p,j_p}
   =\xi_{p,j_p}\chi_p(c_F r/p)^{e_p},
 \qquad |\xi_{p,j_p}|=1,
\tag{3}
\]

where `xi_{p,j_p}` depends on `p,j_p` and not on `h`, `c_F`, or the
other active primes.

For any complex `z` define the full finite-cusp coefficient

\[
 \begin{split}
 F_{r,\boldsymbol j;z}(\mu)
  =\sum_{h\bmod L}&\overline{\alpha(c_F)}^2
       N(c_F)^{2z}\widehat\phi(h)\overline{\kappa_F(h,r)}\\
   &\times\prod_{p\mid r}\chi_p(c_F)^{e_p}
       d_H(\mu)\vartheta_{h,r}(\lambda^4\mu).
 \end{split}
\tag{4}
\]

This leaves the local `B_p` outside (4). It also leaves outside all
factors independent of `h,mu`, in particular

\[
 -\frac{i}{81}\overline{\alpha(r)}^2
 \prod_{p\mid r}\xi_{p,j_p}\chi_p(r/p)^{e_p},
\tag{5}
\]

and the inactive factors `1-N(p)^{-1}`. The factor `N(c_F)^{2z}` is the
one arising on Mellin-transforming the reflected kernel. The proofs
below work with any additional weight depending only on `c_F`.

## 2. How the fixed cusp data change

Put `M=lambda^{12}L^4`, as in the source. The following observations
include the nonunit `h` branches.

Suppose two choices of data have the same `c_F`, have primary scaling
factors, and their fixed numerator congruences satisfy

\[
 a'\equiv t a\pmod{Mc_F},\qquad (t,L)=1,
 \quad t\equiv1\pmod3.
\tag{6}
\]

Then the selected one of the three cusp coefficient functions is the
same, and

\[
 \kappa_F'=\kappa_F\left(\frac{c_F}{t}\right)_3.
\tag{7}
\]

Here and below the right side is interpreted through the fixed ray
character in `t`; all moduli needed for it divide the source's fixed
congruence modulus. For completeness, (7) follows in all three cases
of the source's proof:

* If `3|c_F`, the formula is `kappa_F=(c_F/a)_3`; multiplicativity and
  the fixed-modulus supplementary laws give (7).
* If `v_lambda(c_F)=1`, the source gives
  `kappa_F=(-u_0/A)_3 ((c_F/u_0)/a)_3`, where
  `A=a-u_0 b` and `u_0` is unchanged. At the ramified prime the source
  imposes `b=0 mod M`, hence `A=a mod 9`, and likewise `A'=a' mod 9`.
  The two ratios multiply to
  `(-u_0/t)_3((c_F/u_0)/t)_3=(c_F/t)_3`; the cubic symbol of `-1` is
  one.
* If `(lambda,c_F)=1`, then `c_F` is primary and
  `kappa_F=(a/c_F)_3`. The ratio is `(t/c_F)_3=(c_F/t)_3` by cubic
  reciprocity.

The cusp label is unchanged because the valuation of `c_F` is
unchanged and multiplication by a primary element fixes the numerator
and denominator classes modulo 3 used to select it. This also covers
`h=0`, for which `c_F=1`.

At the primes of `c_F`, the fixed lower-right entry is the inverse of
`a`; at the other primes of `M`, it is zero. Consequently (6) gives

\[
 \delta_F'\equiv t^{-1}\delta_F\pmod{D_F},
 \qquad D_F=\lambda^3c_F.
\tag{8}
\]

The source's additive character is

\[
 \vartheta_{h,r}(x)=e(-\delta_F r^{-1}x/D_F).
\tag{9}
\]

One may use any representatives of `h mod L` in these comparisons.
Replacing a representative by `h+Lk` translates the original theta
argument by `lambda^2 k`, a period of theta with multiplier one.
Thus the complete transformed function is independent of that
choice. In particular we may choose the new representatives by
multiplying the old representatives, rather than reducing them to an
unrelated list. The normalized denominator stays exactly `c_F`, since
all multipliers used here are primary units at `S`.

## 3. Removing a common active exponent-four radical

**Proposition 1.** Suppose `r=s r_0`, `(s,Lr_0)=1`, and `j_p=4` for
every `p|s`. Keep the exponents at the primes of `r_0`. Then, for
every `mu` and every `z`,

\[
 F_{s r_0,\boldsymbol j;z}(\mu)
    =\phi(s)^2 F_{r_0,\boldsymbol j_0;z}(\mu).
\tag{10}
\]

**Proof.** Reindex the entire sum by `h'=s^2h mod L`, choosing the
new lifts so that `a_F'=s^2a_F` and `c_F'=c_F`. In the source's cusp
construction all moving Fourier representatives can be taken to be
zero modulo `M^2`. Thus

\[
 a\equiv a_F s r_0\pmod{Mc_F},\qquad
 a'\equiv s^2a_F r_0\equiv s a\pmod{Mc_F}.
\]

Equations (7)--(9) give

\[
 \kappa_F'=\kappa_F\eta,
 \quad\eta=\left(\frac{c_F}{s}\right)_3,
 \qquad
 \delta_F'r_0^{-1}=\delta_F(sr_0)^{-1}\pmod{D_F}.
\]

Hence the cusp function and the additive character agree. The extra
fixed-denominator contribution from the primes of `s` is

\[
 \prod_{p\mid s}\chi_p(c_F)^{10}
  =\prod_{p\mid s}\chi_p(c_F)^4
  =\eta^2=\eta^{-1}.
\]

This exactly compensates the change in the conjugated `kappa_F`:
`overline{kappa_F'}=overline{kappa_F} eta^{-1}`. Finally,
`widehat phi(h)=phi(s)^2 widehat phi(h')` by (2). Every other factor
in (4) is unchanged. Summing proves (10). No restriction to unit
Fourier frequencies was used. QED.

In the complete reflected formula, (10) says that adding these primes
changes the fixed-cusp profile only by a scalar of absolute value one.
The remaining changes are the explicitly displayed factors
`B_p(lambda^4 mu)`, the conductor scale `N(s)^2` in the kernel, and
the scalar factors in (5). Those scalar factors also have absolute
value one and do not depend on the dual variable. They cancel between
a column and its complex-conjugate column.

## 4. Exact covariance under multiplication by good cubes

The explicit theta coefficient formulas imply

\[
 d_H(\mu b^3)=|b|d_H(\mu)
 \qquad (b\equiv1\pmod3,\ (b,L)=1)
\tag{11}
\]

for each of the three cusp functions. Indeed, on the source support
`mu=u lambda^k n b_0^3`, the coefficient is a fixed unit/ramified
factor times a Gauss coefficient depending on `n`, times `|b_0|`.
Multiplication by `b^3` replaces `b_0` by `b_0b` and leaves the other
data unchanged. The extra factor `check e(mu)` in Appendix A, rows
19 and 10, is unchanged as well: primary `b` satisfies
`b^3=1 mod 9`, while `mu` lies in `lambda^{-4}O` and `(9)=(lambda^4)`.
Thus `mu(b^3-1)` is integral. The formulas do **not** require `(n,b_0)=1` or
`(n,b)=1`. Outside the support, multiplication by a good cube preserves
the prohibited valuation classes, so both sides vanish.

**Proposition 2.** For every primary `b` prime to `L`, every active
radical and exponent pattern, every `mu`, and every complex `z`,

\[
 F_{r,\boldsymbol j;z}(\mu b^3)
    =|b|\Psi_0(b)^{-3} F_{r,\boldsymbol j;z}(\mu).
\tag{12}
\]

**Proof.** Choose a primary element `t` congruent to `b^{-3}` modulo
a sufficiently divisible fixed modulus containing `M^2L`, and
reindex by `h'=t h mod L`, with numerator lifts `a_F'=t a_F`.
Then `c_F,H` are unchanged. In (7),

\[
 \left(\frac{c_F}{t}\right)_3
   =\left(\frac{c_F}{b}\right)_3^{-3}=1.
\]

Thus `kappa_F'=kappa_F`. Equations (8)--(9) show that the additive
factor in the term for `h'` at `mu` is the additive factor in the
term for `h` at `mu b^3`. The local fixed-denominator factors and
the weights depending on `c_F` remain the same. By (2),

\[
 \widehat\phi(h)=\phi(t)\widehat\phi(h')
              =\phi(b)^{-3}\widehat\phi(h').
\]

Now apply (11) termwise. Finally
`phi(b)^{-3}=Psi_0(b)^{-3}` because the supplementary cubic symbol
in (1) has cube one. This proves (12). QED.

## 5. Consequence for the raw reflected principal diagonal

The two propositions require the complete finite Fourier sum. They
need not hold for one isolated cusp branch or after replacing its
coefficients by absolute values.

Consider two reflected copies of the **same** finite character
`Psi_0`, with the second arithmetic column complex conjugated, as in
the original squared inverse moment. The Mellin variables may be
independent; no relation `v=conjugate(u)` is required.

1. Proposition 1 removes the common exponent-four radical from both
   fixed-cusp profiles. Its scalar and the scalars in (5) cancel in
   the product. Thus they cannot supply a residual nonprincipal
   fixed-ray character of the common sieve divisor.
2. Write each dual cube factor as a good factor times an `S`-supported
   factor. Proposition 2 removes its good part from the finite-cusp
   coefficient. The remaining good-cube character in the first
   column is `Psi_0(b_1)^{-3}` and in the conjugate second column is
   `Psi_0(b_2)^3`.
3. The first raw completion inverse has the coefficient
   `overline{alpha(h_1)}^3 Psi_0(h_1)^3`; its finite character agrees
   exactly with the conjugate second dual-cube coefficient. Likewise
   the second raw inverse agrees with the first dual-cube coefficient.
   Thus, on `u+v=0`, the equalities between the two crossed local
   variables, conventionally written `A=y` and `B=x`, remain valid
   with all fixed-ray factors included.

After extracting the `S`-supported squarefree and cube parts, the
remaining theta coefficient divided by the common good Gauss
coefficient is a function of the good squarefree index modulo a
fixed modulus. This follows directly from the same explicit cusp
formulas and cubic Gauss CRT. Its expansion in finite-ray characters
has a principal part independent of the common sieve divisor by
Proposition 1. Nonprincipal fixed-ray parts do not carry the principal
good-index zeta pole. This statement concerns the fixed-prime data;
it does not discard any moving-conductor characters.

Consequently the finite cusp/ray data do **not** invalidate the
good-prime principal-diagonal cancellation established from the raw
local Euler factors, provided the original pair uses the same
`Psi_0` and all finite branches have been summed before taking that
principal part.

This note does not establish an inverse-moment bound or a new
zero-free boundary. In particular, it does not bound the noncommon
good squarefree indices, justify an infinite signed sieve sum in a
new half-plane, or supply uniform estimates for the other dual terms.
Those are separate analytic requirements.
