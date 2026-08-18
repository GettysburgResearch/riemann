# Q4 SACF critical-resonance packet

**Scientific status: SACF, FOCC, OCHD, and RH remain unproved.**

Frozen parent: PR #580 at `812e7fcbaff2dd1c2c53c885def7b6c0d0e68a05`.

The carry route is frozen and not imported.


---

# L-95500 — Critical gcd resonance exactly factorizes the SACF arithmetic source

Claim ID: `L-95500`  
Status: **PROPOSED COMPLETE EXACT ARITHMETIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Frozen parent: PR #580 at `812e7fcbaff2dd1c2c53c885def7b6c0d0e68a05`  
Scope: source and dual-frequency factorization; no pointwise SACF estimate and no RH conclusion

## 1. Odd squarefree reciprocal state

Let \(\mathscr S_o\) be the odd squarefree integers and put

\[
M_o(s)
=
\sum_{n\in\mathscr S_o}\frac{\mu(n)}{n^s}
=
\prod_{p>2}(1-p^{-s})
=
\frac{1}{(1-2^{-s})\zeta(s)}
\tag{L-95500.1}
\]

for \(\Re s>1\).

For \(m,n\in\mathscr S_o\), write uniquely

\[
d=(m,n),\qquad m=da,\qquad n=db.
\]

Then \(a,b,d\in\mathscr S_o\) are pairwise coprime and

\[
\mu(m)\mu(n)=\mu(a)\mu(b).
\tag{L-95500.2}
\]

## 2. Exact resonant triple series

For \(\Re s_1,\Re s_2>1\), the gcd change of variables gives

\[
\boxed{
\begin{aligned}
M_o(s_1)M_o(s_2)
&=
\sum_{\substack{a,b,d\in\mathscr S_o\\
(a,b)=(a,d)=(b,d)=1}}
\frac{\mu(a)\mu(b)}
{a^{s_1}b^{s_2}d^{s_1+s_2}}.
\end{aligned}
}
\tag{L-95500.3}
\]

At one odd prime put

\[
u=p^{-s_1},\qquad v=p^{-s_2}.
\]

The four source-owned choices are:

```text
prime absent:       +1;
prime in a:         -u;
prime in b:         -v;
prime in d:         +uv.
```

Hence the local factor is

\[
\boxed{1-u-v+uv=(1-u)(1-v).}
\tag{L-95500.4}
\]

This identity is the critical gcd resonance. The sign-free common-divisor
state supplies exactly the product term needed to reconstruct two independent
Möbius Euler factors.

## 3. Why the critical exponents are forced

In the Q4 square, the exact gcd-coordinate weight is

\[
\frac{1}{d\sqrt{ab}}
\Psi_1(da/X)\Psi_2(db/Y).
\]

After Mellin inversion with variables \(z_1,z_2\), the exponents are

\[
s_1=\frac12+z_1,\qquad
s_2=\frac12+z_2,
\]

and the common-divisor exponent is

\[
1+z_1+z_2=s_1+s_2.
\tag{L-95500.5}
\]

Thus the physical \(1/(d\sqrt{ab})\) normalization lies exactly on the
resonant hyperplane where (L-95500.4) factorizes. This is not an approximate
singular-series calculation.

## 4. Two-scale Mellin identity

For compactly supported kernels \(\Psi_1,\Psi_2\), define

\[
\mathcal B_{\Psi_1,\Psi_2}(X,Y)
=
\sum_{m,n\in\mathscr S_o}
\frac{\mu(m)\mu(n)}{\sqrt{mn}}
\Psi_1(m/X)\Psi_2(n/Y).
\]

For initially large real parts,

\[
\boxed{
\begin{aligned}
&\int_1^\infty\int_1^\infty
\mathcal B_{\Psi_1,\Psi_2}(X,Y)
X^{-z_1-1}Y^{-z_2-1}\,dX\,dY\\
&\qquad=
\widehat\Psi_1(z_1)\widehat\Psi_2(z_2)
M_o(z_1+\tfrac12)M_o(z_2+\tfrac12).
\end{aligned}
}
\tag{L-95500.6}
\]

The same formula follows from the triple series (L-95500.3), with the
common-divisor exponent (L-95500.5).

On the dual-frequency slice

\[
z_1=\sigma+it,\qquad z_2=\sigma-it,
\]

the arithmetic factor is

\[
\boxed{
M_o(\sigma+\tfrac12+it)
M_o(\sigma+\tfrac12-it)
=
\left|M_o(\sigma+\tfrac12+it)\right|^2.
}
\tag{L-95500.7}
\]

The exact coprime/gcd Type-II source is therefore a reciprocal-zeta square on
its natural dual-frequency line.

## 5. Logarithmic channels are exact derivatives

The PR #580 packet contains both \(\mu(m)\log m\) and \(\mu(m)\) channels.
In gcd coordinates,

\[
\log m=\log a+\log d,
\qquad
\log n=\log b+\log d.
\]

Differentiating (L-95500.3) in \(s_1\) or \(s_2\) produces these complete
logarithmic factors exactly. Thus every `J0` logarithmic term and every `J1`
boundary term is a derivative or zeroth-order component of the same tensor
product. No source term is lost by the gcd parameterization.

## 6. Determinant/product parameterization

If the common-divisor state is temporarily omitted, the coprime pair local
factor is

\[
1-u-v.
\]

The common-divisor state restores \(+uv\), giving the exact determinant
completion

\[
1-u-v+uv=(1-u)(1-v).
\]

Equivalently, after putting \(k=ab\) with \((a,b)=1\), the balanced divisor
sum is a finite coefficient presentation of the same two reciprocal-zeta
legs. The determinant parameterization does not manufacture a third source of
oscillation.

## 7. Boundary

```text
unique gcd/source decomposition             EXACT
critical common-divisor exponent             EXACT
local Euler completion (1-u)(1-v)            EXACT
full triple Dirichlet factorization           EXACT
logarithmic derivative channels              EXACT
dual-frequency reciprocal-zeta square        EXACT
SACF pointwise bound                          OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVEN
```


---

# L-95501 — The Q4 annular kernel has no counterexample-strip zero and its ratio completion is positive spectral mass

Claim ID: `L-95501`  
Status: **PROPOSED COMPLETE EXACT KERNEL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Depends on: PR #580 `L-95400/L-95402`  
Scope: exact finite-band/Mellin geometry; no Möbius estimate

## 1. Exact Mellin factors

Retain

\[
\widehat J_0(z)
=q(z)\mathcal A_2(t)\widehat W(z),
\qquad
 t=2^{-z-1/2},
\]

where

\[
q(z)=\prod_{k=1}^{3}(1-2^{-z-k}),
\]

\[
\mathcal A_2(t)=(1+t)(1-4t^2)^2,
\]

and

\[
\widehat W(z)
=(1-4^{1-z})\frac{z-1}{3(z+1)(z+2)(z+3)}.
\tag{L-95501.1}
\]

## 2. Zero-free counterexample strip

Suppose

\[
0<\Re z<\frac12.
\]

Then:

- a zero of `q` has real part `-1`, `-2`, or `-3`;
- `1+t=0` requires \(|t|=1\), hence \(\Re z=-1/2\);
- `1-4t^2=0` requires \(|t|=1/2\), hence \(\Re z=1/2\);
- `1-4^{1-z}=0` requires \(\Re z=1\);
- `z-1=0` requires \(z=1\).

The denominator in (L-95501.1) is also nonzero. Therefore

\[
\boxed{
\widehat J_0(z)\ne0
\qquad(0<\Re z<\tfrac12).
}
\tag{L-95501.2}
\]

At a hypothetical zeta zero \(\rho\) with \(1/2<\Re\rho<1\), the relevant
point is

\[
z_\rho=\rho-\frac12,
\]

which lies exactly in this strip.

## 3. Pole order cannot cancel

Put

\[
M_o(s)=\frac1{(1-2^{-s})\zeta(s)}.
\]

The exact one-variable Mellin transform of the annular packet is

\[
\mathfrak F(z)
=
-\widehat J_0(z)M_o'(z+\tfrac12)
+(\log2)\widehat J_1(z)M_o(z+\tfrac12).
\tag{L-95501.3}
\]

If \(\rho\) is a zeta zero of multiplicity \(m\), then `M_o'` has a pole of
order \(m+1\), while the `J1` term has pole order at most \(m\). By
(L-95501.2), the leading pole has nonzero coefficient. Hence

\[
\boxed{
\mathfrak F(z)
\text{ has a pole of order }m+1
\text{ at }z=\rho-\tfrac12.
}
\tag{L-95501.4}
\]

The ten-band Q4 kernel creates no spectral cancellation of an off-line zero.

## 4. Exact nonzero low-frequency mass

At `z=0`, exact substitution gives

\[
\boxed{
\widehat J_0(0)
=\frac7{128}\left(1+\frac1{\sqrt2}\right)>0.
}
\tag{L-95501.5}
\]

Thus the logarithmic channel has nonzero Mellin mass at frequency zero.

## 5. Positive multiplicative autocorrelation

For \(L=\log X\), extend by zero and put

\[
\gamma_L(u)
=
(L-u)J_0(e^{-u})+(\log2)J_1(e^{-u}),
\qquad 0\le u\le10\log2.
\]

Define the ratio autocorrelation

\[
R_L(v)=\int_{\mathbb R}\gamma_L(u)\gamma_L(u+v)\,du.
\tag{L-95501.6}
\]

Its Fourier transform is exactly

\[
\boxed{
\widehat R_L(t)=|\widehat\gamma_L(t)|^2\ge0.
}
\tag{L-95501.7}
\]

For all sufficiently large `X`, (L-95501.5) makes
\(\widehat\gamma_L(0)\ne0\). Hence the exact finite-band ratio completion has
strict positive spectral mass near zero. A positive-kernel completion
reinforces the resonant reciprocal-zeta square; it does not provide an
oscillatory cancellation mechanism.

## 6. Boundary

```text
J0 zero-free in 0<Re z<1/2              EXACT
higher-order pole survives J1 channel    EXACT
nonzero zero-frequency Mellin mass        EXACT
multiplicative autocorrelation PSD        EXACT
kernel-generated SACF cancellation        ABSENT
arithmetic Möbius cancellation            OPEN / RH-BEARING
```


---

# L-95502 — Any power saving for SACF implies a fixed zeta zero-free strip

Claim ID: `L-95502`  
Status: **PROPOSED COMPLETE ANALYTIC CONSEQUENCE — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Depends on: PR #580 `L-95401/T-95400`; `L-95501`  
Scope: implication from SACF bounds to zeta zero exclusion

## 1. Parent decomposition

Fix

\[
H=(\log(2X))^B
\]

and let \(\mathcal S_H(X)\) be PR #580's separated annular coprime form.
The diagonal and every deleted sector in PR #580 satisfy

\[
\boxed{
|\mathcal A(X)|^2
=
\mathcal S_H(X)
+O_B(\log^{B+2}(2X)).
}
\tag{L-95502.1}
\]

This includes the annular diagonal, near-diagonal, large-gcd, and small reduced
Type-I pieces.

## 2. General exponent dictionary

Assume for some \(0\le\theta<1/2\) that

\[
\boxed{
|\mathcal S_H(X)|\ll X^{2\theta}
}
\tag{L-95502.2}
\]

for all sufficiently large `X`. Equation (L-95502.1) gives

\[
\mathcal A(X)=O(X^\theta+\log^{(B+2)/2}(2X)).
\tag{L-95502.3}
\]

Consequently

\[
\int_1^\infty\mathcal A(X)X^{-z-1}\,dX
\]

is holomorphic in \(\Re z>\theta\).

By PR #580 and `L-95501`, its meromorphic expression is

\[
-\widehat J_0(z)M_o'(z+\tfrac12)
+(\log2)\widehat J_1(z)M_o(z+\tfrac12),
\]

and every zero \(\rho\) of zeta with \(\Re\rho>1/2\) produces an uncancelled
pole at \(z=\rho-1/2\). Holomorphy therefore implies

\[
\boxed{
\zeta(\rho)=0
\Longrightarrow
\Re\rho\le\frac12+\theta.
}
\tag{L-95502.4}
\]

## 3. Fixed power saving

If for some \(\delta>0\),

\[
|\mathcal S_H(X)|\ll X^{1-\delta},
\]

then \(2\theta=1-\delta\), so

\[
\boxed{
\zeta(\rho)=0
\Longrightarrow
\Re\rho\le1-\frac\delta2.
}
\tag{L-95502.5}
\]

Thus any genuine fixed exponent improvement over the source-blind
\(O(X\operatorname{polylog}X)\) scale proves a fixed classical zero-free
strip for zeta.

## 4. Polylogarithmic SACF

If

\[
|\mathcal S_H(X)|\ll\log^A(2X),
\]

then (L-95502.3) has exponent \(\theta=0\). Hence no zero satisfies
\(\Re\rho>1/2\); functional-equation symmetry gives

\[
\boxed{
\mathrm{SACF}\Longrightarrow\mathrm{RH}.
}
\tag{L-95502.6}
\]

## 5. Interpretation

The statement does not say that dispersion, Type-II, or pretentious methods
cannot prove SACF. It states exactly what such a proof must accomplish. A
fixed power saving is already a fixed zero-free strip; the requested
polylogarithmic bound is a complete RH-producing estimate.

## 6. Boundary

```text
SACF exponent -> zeta zero-free exponent     PROVED
fixed SACF power saving -> fixed strip        PROVED
polylog SACF -> RH                            PROVED CONDITIONAL
unconditional fixed power saving              NOT PROVED
SACF                                           OPEN / RH-BEARING
RH                                             UNPROVEN
```


---

# L-95503 — Product-variable and log-derivative normal forms preserve the full reciprocal-zeta resonance

Claim ID: `L-95503`  
Status: **PROPOSED COMPLETE EXACT REWRITING THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Depends on: `L-95500`; PR #580 `L-95402`

## 1. Product variable

In the separated coprime core put

\[
k=ab,
\qquad (a,b)=1.
\]

Then \(k\) is odd squarefree and

\[
\mu(a)\mu(b)=\mu(k).
\]

The ratio condition \(a<b<1024a\) selects finitely many balanced divisor
pairs of `k`. Thus SACF may be written as a one-sign product sum

\[
\sum_k\frac{\mu(k)}{\sqrt k}
\sum_{a\mid k\atop a<k/a<1024a}
\mathcal W_X(a,k/a),
\tag{L-95503.1}
\]

with the exact common-divisor and ten-band kernel retained in
\(\mathcal W_X\).

This is a change of coordinates, not a reduction to a divisor-bounded
coefficient. The number and location of balanced divisors remain arithmetic.

## 2. Dual-frequency divisor polynomial

For a ratio frequency `t`, the unrestricted coprime divisor polynomial has
local factor

\[
1-p^{-s-it}-p^{-s+it}.
\]

Restoring the common-divisor source adds \(p^{-2s}\). On the resonant line,

\[
\boxed{
1-p^{-s-it}-p^{-s+it}+p^{-2s}
=(1-p^{-s-it})(1-p^{-s+it}).
}
\tag{L-95503.2}
\]

The determinant parameterization therefore reconstructs the two shifted
reciprocal-zeta factors rather than producing an independent divisor-sum
cancellation.

## 3. Vaughan/Heath–Brown coefficient identities

The exact squarefree identity

\[
\mu(m)\log m
=-\sum_{p\mid m}(\log p)\mu(m/p)
\]

is the first derivative of the reciprocal Euler product. More elaborate
finite Vaughan or Heath–Brown decompositions distribute this derivative among
Type-I and Type-II convolution factors. After exact reassembly, the local
factor remains (L-95503.2).

Therefore the identities themselves do not create an extra averaging
parameter. A successful use of them must prove cancellation in at least one
balanced factor strong enough to meet `L-95502`.

## 4. Resonant logarithmic derivatives

Differentiating

\[
M_o(s_1)M_o(s_2)
\]

produces the complete \(\log m\), \(\log n\), and mixed logarithmic channels.
The `J1` term is the zeroth-order boundary component. No derivative gauge or
band remainder lies outside the tensor product.

## 5. Boundary

```text
product k=ab parameterization              EXACT
balanced divisor-pair representation       EXACT
dual-frequency local determinant            EXACT
log channels as Euler derivatives           EXACT
finite coefficient decompositions           SOURCE-FAITHFUL BUT NON-CLOSING
new balanced cancellation theorem            OPEN / RH-BEARING
```


---

# L-95504 — The classical zero-free region gives a genuine subexponential SACF improvement

Claim ID: `L-95504`  
Status: **PROVED FROM ONE CLASSICAL IMPORT — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Depends on: PR #580 `L-95400/L-95401`; the classical zero-free-region bound for the Mertens function  
Scope: unconditional subexponential gain; no fixed power saving and no RH conclusion

## 1. Imported classical estimate

Let

\[
M(x)=\sum_{n\le x}\mu(n).
\]

A classical consequence of the de la Vallée Poussin zero-free region and
Perron contour displacement is that there are absolute constants `c,C>0`
such that

\[
\boxed{
|M(x)|\le Cx\exp\!\bigl(-c\sqrt{\log x}\bigr)
}
\tag{L-95504.1}
\]

for all sufficiently large `x`.  The modern Vinogradov--Korobov region gives a
stronger logarithmic exponent; the weaker form (L-95504.1) is sufficient here.

No zero-density theorem, RH hypothesis or unproved cancellation statement is
imported.

## 2. Odd Mertens state

Put

\[
M_o(x)=\sum_{\substack{n\le x\\n\ \mathrm{odd}}}\mu(n).
\]

Since every nonzero even Möbius coefficient is `mu(2m)=-mu(m)` with `m` odd,

\[
\boxed{M(x)=M_o(x)-M_o(x/2).}
\tag{L-95504.2}
\]

Iteration gives the finite identity

\[
\boxed{M_o(x)=\sum_{j\ge0}M(x/2^j).}
\tag{L-95504.3}
\]

Splitting the sum at `2^j=sqrt(x)` and applying (L-95504.1) to the first part
shows, after changing the constants, that

\[
\boxed{
|M_o(x)|\ll x\exp\!\bigl(-c_1\sqrt{\log x}\bigr)
}
\tag{L-95504.4}
\]

for some absolute `c_1>0`.

## 3. Partial summation through the exact ten bands

Retain PR #580's annular weight

\[
G_X(t)=
\frac{(\log t)J_0(t/X)+(\log2)J_1(t/X)}{\sqrt t},
\qquad X/1024<t\le X.
\tag{L-95504.5}
\]

On each of the ten exact activation bands, `J_0,J_1` are fixed cubics over
`Q(sqrt(2))`.  Hence there are absolute constants `C_0,C_1` such that on every
open band

\[
|G_X(t)|\le C_0\frac{\log(2X)}{\sqrt X},
\qquad
|G_X'(t)|\le C_1\frac{\log(2X)}{X^{3/2}}.
\tag{L-95504.6}
\]

The kernels are continuous at the activation knots.  Applying Stieltjes
partial summation separately on the ten bands, and using (L-95504.4) uniformly
for `X/1024<=t<=X`, gives

\[
\begin{aligned}
|\mathcal A(X)|
&=
\left|\sum_{X/1024<m\le X\atop m\ \mathrm{odd}}
\mu(m)G_X(m)\right|\\
&\ll
\sqrt X\,\log(2X)
\exp\!\bigl(-c_2\sqrt{\log X}\bigr)
\end{aligned}
\tag{L-95504.7}
\]

for some absolute `c_2>0`.

This estimate visibly uses the actual odd Möbius coefficients.  It is not a
source-blind kernel or diagonal bound.

## 4. Consequence for SACF

For `H=log^B(2X)`, PR #580 gives

\[
|\mathcal A(X)|^2
=
\mathcal S_H(X)+O_B(\log^{B+2}(2X)).
\]

Therefore

\[
\boxed{
|\mathcal S_H(X)|
\ll_B
X\log^2(2X)
\exp\!\bigl(-2c_2\sqrt{\log X}\bigr)
+
\log^{B+2}(2X).
}
\tag{L-95504.8}
\]

This is a genuine subexponential improvement over the source-blind
`O(X polylog X)` scale.

It is not a fixed power saving: for every fixed `delta>0`,

\[
\exp(-c\sqrt{\log X})>X^{-\delta}
\]

for all sufficiently large `X`.  Thus (L-95504.8) does not enter the fixed
zero-free-strip regime of `L-95502` and does not imply RH.

## 5. Stronger classical option

Replacing (L-95504.1) by a Vinogradov--Korobov Mertens estimate strengthens
(L-95504.7)--(L-95504.8) by the corresponding

\[
\exp\!\left[-c(\log X)^{3/5}(\log\log X)^{-1/5}\right]
\]

factor.  No part of the Q4 argument changes.

## 6. Boundary

```text
odd-Mertens reduction                         EXACT
partial summation through all ten Q4 bands   COMPLETE
unconditional subexponential SACF gain        PROVED ON CLASSICAL IMPORT
fixed SACF power saving                       NOT PROVED
polylog SACF                                  OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVEN
```


---

# R-95500 — Common-divisor dispersion is the resonant Euler completion, not an independent average

Claim ID: `R-95500`  
Status: **EXACT MECHANISM FIREWALL**  
Created: 2026-08-18  
Depends on: `L-95500`

A natural SACF attack treats the sign-free common divisor `d` as an averaging
or modulus variable and hopes to gain cancellation before confronting the two
Möbius signs.

At one prime, however, the source-owned `d` state contributes exactly

\[
p^{-(s_1+s_2)}=p^{-s_1}p^{-s_2}=uv.
\]

The complete local source is

\[
1-u-v+uv=(1-u)(1-v).
\]

Thus the `d` average is not independent noise. It is the precise Euler state
which completes the two reciprocal Möbius factors. Any argument that:

```text
replaces d by its unsigned density;
drops coprimality before reassembly;
takes absolute values in d;
or treats the d-sum as an external modulus average
```

must separately recover the lost `+uv` source state. Otherwise it is not an
estimate of SACF.

The large-gcd sector closed on PR #580 may be removed at polylogarithmic cost,
but reattaching it restores the exact Euler completion. Hence no conclusion-
scale gain comes merely from naming `d` a dispersion variable.

This firewall does not forbid a source-faithful dispersion theorem. It requires
such a theorem to retain the complete local factor and therefore to confront
the reciprocal-zeta square explicitly.


---

# R-95501 — Positive-kernel, generic large-sieve, and finite-decomposition shortcuts do not close SACF

Claim ID: `R-95501`  
Status: **EXACT SCOPE FIREWALLS**  
Created: 2026-08-18  
Depends on: `L-95501/L-95502/L-95503`; PR #580 `R-95400`

## 1. Positive ratio kernel

The multiplicative autocorrelation of the exact ten-band kernel has Fourier
transform \(|\widehat\gamma_L(t)|^2\ge0\), with nonzero mass near `t=0`.
A positive-kernel completion therefore converts the arithmetic source into a
positive reciprocal-zeta square. It does not create an oscillatory sign.

## 2. Fixed Mellin window

PR #580 proves

\[
\int_{-T}^{T}\left|\sum c_m m^{-it}\right|^2dt
\le(2T+CX)\sum|c_m|^2.
\]

The exact annular kernel is compact in log position but not compact in
frequency. For `T=polylog(X)`, the `CX` term remains. The local kernel cannot
remove it because `L-95501` gives nonzero low-frequency mass.

## 3. Finite coefficient decompositions

Vaughan/Heath–Brown identities and the prime-divisor expansion are exact
rearrangements of derivatives of `M_o`. On reassembly they return the local
factor `(1-u)(1-v)`. An estimate that treats every resulting factor only by
source-blind size cannot beat the parent diagonal/firewall examples.

## 4. Quantitative burden

By `L-95502`, any bound

\[
|\mathcal S_H(X)|\ll X^{1-\delta}
\]

already proves a fixed zero-free strip \(\Re\rho\le1-\delta/2\). Thus a claimed
routine Type-II power saving must be reviewed as a new zeta zero-free theorem,
not as an ordinary large-sieve consequence.

These statements do not prove that all Type-II methods fail. They identify the
exact arithmetic gain that a successful proof must supply.


## 5. Classical gain boundary

The actual odd Möbius coefficients do yield the standard zero-free-region gain
through exact partial summation, as recorded in `L-95504`.  That estimate is
subexponential in `log X`, not a fixed power of `X`.  It therefore confirms
that arithmetic input matters without supplying the fixed exponent needed by
`L-95502`.


---

# T-95500 — SACF is an RH-strength resonant reciprocal-zeta correlation

Claim ID: `T-95500`  
Status: **PROPOSED COMPLETE DIAGNOSIS/CONDITIONAL CONSUMER — SACF OPEN**  
Created: 2026-08-18  
Depends on: PR #580 at exact head `812e7fcbaff2dd1c2c53c885def7b6c0d0e68a05`; `L-95500`–`L-95504`; `R-95500/R-95501`

## 1. What the new analysis proves

After the exact PR #580 deletions, SACF is not an independent generic
coprime bilinear form. Reattaching the already-polylogarithmic sectors gives
the square of one annular Möbius packet. In gcd coordinates the common-divisor
state lies on the critical hyperplane and exactly factorizes the source as

\[
M_o(s_1)M_o(s_2).
\]

The ten Q4 bands contribute only explicit entire Mellin multipliers. The
logarithmic channel has no zero in the counterexample strip, and the boundary
channel cannot cancel its higher-order pole.

## 2. Exact strength statement

For \(H=\log^B(2X)\), let \(\mathcal S_H\) denote SACF. Then:

\[
|\mathcal S_H(X)|\ll X^{2\theta}
\quad\Longrightarrow\quad
\zeta(\rho)=0\Rightarrow\Re\rho\le\frac12+\theta.
\]

In particular:

\[
|\mathcal S_H(X)|\ll X^{1-\delta}
\quad\Longrightarrow\quad
\Re\rho\le1-\frac\delta2,
\]

and

\[
|\mathcal S_H(X)|\ll\log^A(2X)
\quad\Longrightarrow\quad
\mathrm{RH}.
\]

## 3. Unconditional gain that survives

The classical zero-free-region Mertens estimate and exact ten-band partial
summation give

\[
|\mathcal S_H(X)|
\ll_B
X\log^2(2X)e^{-c\sqrt{\log X}}+\log^{B+2}(2X).
\]

Thus the arithmetic coefficients do provide a genuine subexponential gain
over the source-blind `O(X polylog X)` scale.  The gain is not a fixed power,
so it does not yield a new fixed zero-free strip.

## 4. Disposition of the requested methods

```text
dyadic/ratio/gcd localization          retained exactly
common-divisor dispersion              exact Euler resonance, not free averaging
Vaughan/Heath–Brown                    exact derivative decompositions; balanced factor survives
determinant k=ab                       reconstructs shifted reciprocal-zeta pair
dual-frequency analysis               gives |M_o(s+it)|^2
positive-kernel completion             PSD and resonant, not cancelling
fixed-window large sieve               retains O(X) spacing loss
pretentious/zero-free input            would need fixed-strip or RH-scale strength
```

## 5. Correct frontier

The requested polylogarithmic SACF theorem remains unproved. The exact new
result is that its formulation already contains the classical reciprocal-zeta
square with no unused finite-band cancellation. Any successful continuation
must introduce genuinely new arithmetic information about the Möbius
coefficients; it cannot obtain the required gain solely from the Q4 band
geometry or from generic bilinear energy.

```text
critical gcd resonance                 PROVED EXACT
kernel noncancellation                  PROVED EXACT
classical subexponential SACF gain       PROVED
power-saving -> fixed zero-free strip  PROVED
polylog SACF -> RH                      PROVED CONDITIONAL
SACF                                   OPEN / RH-BEARING
FOCC / OCHD                            OPEN / RH-BEARING
Riemann Hypothesis                     UNPROVEN
```


---

# M-95500 — Hostile review protocol for the SACF resonance packet

Review in this order:

1. Freeze PR #580 at `812e7fcbaff2dd1c2c53c885def7b6c0d0e68a05`.
2. Reconstruct the bijection `m=da,n=db` for odd squarefree pairs.
3. Verify the local state table and
   `1-u-v+uv=(1-u)(1-v)`.
4. Check that the common-divisor exponent is exactly `s1+s2`; reject any
   normalization with a different `d` power.
5. Differentiate the triple series and verify that `log m=log a+log d`.
6. Audit every zero of `q`, `A2`, and `W_hat` in `0<Re z<1/2`.
7. Check pole orders: `M_o'` is one order higher than the `J1` term.
8. Reconstruct the parent identity
   `A(X)^2=S_H(X)+O_B(log^(B+2) X)`.
9. Apply the Mellin holomorphy argument for the exponent dictionary.
10. Verify the odd-Mertens identity and ten-band partial summation in `L-95504`.
11. Treat the classical zero-free-region estimate as an explicit imported theorem.
12. Treat every numerical scan as reconnaissance only.

Immediate rejection conditions:

```text
common divisor treated as carrying a Möbius sign;
d exponent not equal to s1+s2;
J1 allowed to cancel the M_o' leading pole;
positive autocorrelation claimed to give arithmetic cancellation;
the imported subexponential gain promoted to a fixed power;
a fixed SACF power saving called routine;
SACF or RH represented as proved.
```


---

# O-95500 — SACF method disposition after exact resonance extraction

| Proposed mechanism | Exact disposition |
|---|---|
| dyadic bands | useful finite localization; no pole zero |
| ratio localization | yields compact log kernel and dual frequency |
| gcd parameterization | exact source bijection |
| common-divisor dispersion | supplies resonant `+uv` Euler state |
| determinant/product `k=ab` | finite presentation of two reciprocal-zeta legs |
| prime-divisor Type I/II | exact logarithmic derivative split |
| Vaughan/Heath–Brown | may organize terms; balanced reciprocal factor remains |
| Mellin almost orthogonality | fixed window loses `O(X)` from frequency spacing |
| positive kernel / PSD | produces positive spectral square |
| square function / log Sobolev | source-blind and blocked by parent sign replacement |
| classical zero-free-region input | gives `X exp(-c sqrt(log X))`-scale SACF gain |
| fixed SACF power saving | proves a fixed zeta zero-free strip |
| polylog SACF | proves RH |

The packet establishes the strength and exact source structure of the remaining
theorem and transfers the classical zero-free-region Mertens gain through the
ten bands. It does not establish a fixed power saving or the theorem itself.


---

# Q4 SACF continuation: exact critical gcd resonance

## Executive result

The separated annular coprime Type-II form was attacked through the requested
arithmetic parameterizations. The common-divisor coordinate does not create an
independent dispersion average. At the exact critical weights it contributes
the local state `+uv`, completing

\[
1-u-v+uv=(1-u)(1-v).
\]

Thus the full source is exactly the tensor square of the odd reciprocal-zeta
Möbius channel. The ten Q4 bands have no zero in the off-line counterexample
strip and their ratio autocorrelation has positive spectral density.

## New rigorous consequences

- exact triple Dirichlet factorization in gcd coordinates;
- exact dual-frequency form `|M_o(s+it)|^2`;
- exact treatment of both logarithmic and boundary channels;
- zero-free classification of the annular `J0` multiplier;
- any SACF bound `O(X^(1-delta))` implies the fixed strip
  `Re rho <= 1-delta/2`;
- polylogarithmic SACF implies RH.

## Scientific boundary

No unconditional SACF estimate at a fixed power-saving scale was obtained.
The packet proves that obtaining one would itself be a new fixed zero-free
strip theorem. The remaining bound cannot come from source-blind kernel,
large-sieve, PSD, or finite-decomposition algebra alone.


## Classical zero-free-region gain

Exact partial summation through the ten activation bands, combined with the
classical Mertens bound, yields

\[
\mathcal S_H(X)
\ll_B X\log^2(2X)e^{-c\sqrt{\log X}}+\log^{B+2}(2X).
\]

This is a genuine unconditional subexponential improvement, but not a fixed
power saving.  The stronger Vinogradov--Korobov version transfers unchanged.
