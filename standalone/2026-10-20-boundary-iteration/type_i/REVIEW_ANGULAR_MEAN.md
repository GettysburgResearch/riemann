# Complete analytic review of the proposed angular mean

Date: 2026-10-20. Reviewer: Type-I subagent, independently of the author
of the mean-value and absorption argument.

**Verdict:** no outstanding gap was found in the stated deduction from
the source identities and cubic large sieve, after the presentation
repairs recorded below. In particular the unconditional bilinear
\(A^{1/2}B(AB)^\epsilon\) consequence follows with all common-prime
zeros and the complete cube factor retained. This is a review of the
written deduction, not certification of every theorem in the cited
preprints.

## Frozen scope and authorship

| File | Reviewed SHA256 |
|---|---|
| ../average/ANGULAR_SELF_ABSORPTION.md | 0c195c93ef2548a81197e21d0eca58f1632f25e9339d0f078fa185f8605d59e8 |
| FINITE_PROFILE_CLOSURE.md | a4a1798f304fd9a551c35b2a161ef2f7b82644d62d9f0eae986df2afb7100dad |
| DUAL_RESUMMATION.md | d8dae0a17a85b466ba9d9d5b762ee532ce92b0a45de7236ffe5b3bb8256dbef2 |
| ../mixed/AUDIT_CUSP_REFLECTION.md | d5c27a75e7952b02d8ccaef606e4347ed634ad3efbe1a57e6ca23f91102c9866 |

I authored the finite-profile and divisor-resummation notes, so rereading
those is not represented as a second independent review of my own work.
The separate mixed-agent cusp audit independently checks that interface.
For the present review I independently recomputed the original-series
mean, divisor average, height-weighted absorption and Type-I return, and
rechecked the underlying source coefficient and gamma normalizations.

The initial mean file, SHA256
33243ca5df642fdbd38da16c26de58977f721f91c26e2c2938dc213fc1dba471,
had two abbreviated statements in Section 3. With the author's
authorization, I restored the free cube variable \(d'\) away from \(r\)
in its dual-index formula, and clarified that the local product is
subpower only *after extracting \(Nh\)*. The later coefficient
\(\sum_{h\mid k}Nh\) and the exact identity (D5) already retained these
factors. No theorem or exponent changed.

A further review pass made the sign closure explicit in Section 2.
The norm is now defined on the eight-component direct sum of the four
ramified channels at both \(\ell\) and \(-\ell\). This is required
because reflection reverses the angular sign. The original estimates
apply to each sign with the same fixed constants, so the supremum
controls the complete reflected family without changing any exponent.

## 1. Analytic family and exact reflection

The actual cusp minor uses rows 22, 26, 27, not the rejected exploratory
minor. Its inverse \(M^*/3\) is uniformly bounded. The trivial channel
has the nonzero scalar \(3^{5/2+3s}i^\ell\psi_r(\lambda)\). The full
27-row coefficient table is spanned by those four complete Mellin
channels on \(\Re s>1/6\), because its ramified geometric ratio has
modulus \(3^{1/2-3\Re s}<1\). This is Mellin-series closure; literal
unit-index shifts of the original 27 coefficient arrays are not used.

The source matrices \(\beta\) depend modulo 9 only on the modulus.
Their quotient lies in the normal principal congruence subgroup, acting
with a common scalar on the cusp functions. Both fix the nonzero first
cusp with scalar one, so that common scalar is one. Thus the complete
primitive Fourier transform survives in every cusp component.
The transformed arithmetic factor is the full signed Ramanujan sum,
with its Gauss factor of modulus \((Nr)^{1/2}\).

Nonzero angular order removes every constant term in the split Mellin
integral, so the extracted completed scalar functions are entire.
The source gamma quotient has, on \(s=1/2-\delta+it\), two numerator
arguments each with real part \(2\delta\) larger than the corresponding
denominator argument. Stirling therefore gives exactly
\((1+|t|)^{4\delta}\); its exponential factors cancel. Fixed ramified
scalars are bounded in height. The moving factor
\((Nr)^{1/2-2s}\) becomes \((Nr)^{-1/2+2\delta}\).

In (D5), the complementary local factor is \(qz_p-1\), with
\(|qz_p|=q^{-3\delta}\) at the reflected point. Hence its product is
\(O((Nr)^\eta)\). The divisor coefficient has size
\((Nk)^{1/2-\delta}\). The angular sign reverses, and both signs are
included in the vector. This gives exactly equation (7).

## 2. The two mean estimates

After squaring (7), the divisor bound costs an arbitrary small power.
For \(k\mid r\), ideal counting gives
\[
 \sum_{Nr\le R,\ k\mid r}(Nr)^{-1+4\delta}
 \ll_\delta R^{4\delta}/Nk.
\]
The squarefree and coprimality restrictions can be retained or removed
in this positive majorant. Multiplying by
\((Nk)^{1-2\delta}\) leaves precisely the weight
\((Nk)^{-2\delta}\) in (8); no row larger than \(R\) appears.

For the original integral at \(\sigma=1/2+\delta\), expand the full
cube completion before applying the cubic large sieve. At a fixed cube
index \(d\), the restriction \((r,d)=1\) is a positive restriction of
the row sum, and the squarefree Gauss variable remains a genuine
squarefree column. The square roots of the three sieve terms give
\[
 R^{1/2},\qquad Y^{1/2-\delta},\qquad
 R^{1/3}Y^{1/3-\delta}.
\]
The first weighted column sum is dominated by its short end, since
\(\sigma>1/2\). After Minkowski, the respective cube exponents are
\(-1-3\delta,-5/2,-2\), all convergent. Squaring gives (9).
The Gaussian weight supplies summable tails beyond the nominal split.
No cube coefficient or common-prime zero is discarded.

## 3. Absorption and height control

The finite \(R_{\max}\) supremum is finite before absorption: there are
only finitely many rows, and the completed family has polynomial
vertical growth of an order independent of the row. Absolute right-line
estimates, the reflected left-line estimates and strip interpolation
give this common order. The constants may depend polynomially on the
row at this preliminary stage, which is allowed for a finite cutoff.

Partial summation bounds the weighted sum in (8) by
\(M R^{1+\epsilon_0-2\delta}(1+|u|)^C\). The shifted Gaussian integral
has real part \(-2\delta\), so its squared split factor is
\(Y^{-4\delta}\). Its height convolution costs at most
\((1+|t|)^{C+8\delta}\), times a finite Gaussian integral independent
of \(R_{\max}\).

Choosing \(Y=R^{1/2+\delta/4}(1+|t|)^2\) cancels the extra
\(8\delta\) height power and leaves a contraction factor
\(R^{-\delta^2+\eta}\). The two nonconstant original-series powers are
strictly below \(R^1\) for \(0<\delta<1/4\), as displayed in the note.
Auxiliary losses fit within \(\epsilon_0\). Above a fixed \(R_0\) the
remainder coefficient is at most one half; below it the independent
finite-row bound is uniform in \(R_{\max}\). Thus letting
\(R_{\max}\) grow is legitimate and does not assume the desired estimate.

Reflection then gives exponent \(2-2p\) on \(1/4<p<1/2\), since
\(4\delta+(1-2\delta)=1+2\delta=2-2p\).

## 4. The strongest Type-I consequence and its limits

Twisted Gauss multiplicativity gives
\[
 \widetilde g(uv)
  =\widetilde g(u)\widetilde g(v)\overline{(u/v)_3}
\]
on the coprime squarefree support, and both sides vanish on a collision.
Thus Mellin inversion in the unrestricted smooth \(u\)-variable gives
the scalar \(\mathcal R_v(s)\) exactly. The outer row has squarefree
\(v\), and its coefficient has squared norm \(O(B)\).
On \(\sigma=1/2+\delta\), the completion has
\(\Re(3s-1/2)>1\), so its inverse is uniformly controlled by absolute
Euler convergence. This step uses no Hecke zero-free hypothesis.

The mean contributes \(B^{1/2+\epsilon}\), outer Cauchy contributes
\(B^{1/2}\), and Mellin inversion contributes \(A^{1/2+\delta}\).
Choosing \(\delta\) inside the requested final loss proves
\[
 |T_\ell(A,B)|\ll(AB)^\epsilon A^{1/2}B.
\]
At \(A=B=X^{1/2}\) the exponent is exactly \(3/4+\epsilon\).
Equivalently the unconditional form is \(X^{1/2}B^{1/2}\), strictly
below \(X^{5/6}\) on every fixed-margin range
\(B\le X^{2/3-\eta}\).

The conditional left-line consequence additionally needs the zero-free
premise for the actual fixed Hecke factor, and has exponent
\(A^pB^{3/2-p}\). It has the same balanced \(3/4\), not a further
balanced saving.

These assertions concern an angular cubic block at fixed nonzero
\(\ell\). They do not assert a bound uniform in unbounded angular
order. They also do not include a growing quadratic row character.
The separately reviewed quadratic/sextic pair supplies an explicit
pointwise-conductor extension, but its bound remains above the required
\(KL\) mixed norm at the adverse terminal face \(U=KL,\ K\gg L\).
Consequently this review supports the strict Type-I improvement, while
making no claim of a stricter numerical global zero-free boundary or RH.
