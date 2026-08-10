# Root-of-unity powered Euler frame: exponential off-line depth with exact averaged reserve

Status: **PROPOSED COMPLETE EXACT FINITE THEOREM — independent review required**  
Date: 2026-08-10  
Dependencies: PR #363 off-line pair spectrum; PR #325 `L-32421` and `R-32404`; ordinary Selberg–Kummer row inequality  
RH status: **unproved**

## 1. Powered phase frame

Put

\[
a(s)=4^{1-s},\qquad L=\log4,
\]

and let \(\Omega_M\) be the \(M\)-th roots of unity. For integers \(k\ge1\),
define

\[
\boxed{
F_{\omega,k}(s)=(1-\omega a(s))^k.
}
\tag{RU.1}

For \(x\ge0\), put

\[
\boxed{
C_k(x)=\sum_{j=0}^k\binom{k}{j}^2x^j.
}
\tag{RU.2}

If \(M>2k\), root-of-unity orthogonality gives

\[
\boxed{
\frac1M\sum_{\omega\in\Omega_M}
|F_{\omega,k}(s)|^2
=C_k(|a(s)|^2).
}
\tag{RU.3}

On the critical line \(|a|=2\), so the exact frame constant is

\[
\boxed{\mathfrak C_k=C_k(4).}
\tag{RU.4}

Unlike a scalar power of one Q4 system, the phase bank retains every mixed
channel until the final Fourier average.

## 2. Reflected off-line pair spectrum

Write \(s=\tfrac12+z\), and let

\[
z^\#=-\overline z.
\]

Then

\[
\boxed{
a(1/2+z^\#)=\frac4{\overline{a(1/2+z)}}.}
\tag{RU.5}

Let a right-half-plane zero have

\[
q=|a(1/2+z)|=2\,4^{-\Re z}<2.
\]

For the normalized channel evaluation vectors

\[
u_\omega={F_{\omega,k}(1/2+z)\over\sqrt{M\mathfrak C_k}},
\qquad
v_\omega={\overline{F_{\omega,k}(1/2+z^\#)}\over
\sqrt{M\mathfrak C_k}},
\]

orthogonality gives

\[
\|u\|^2={C_k(q^2)\over C_k(4)},
\qquad
\|v\|^2={C_k(16/q^2)\over C_k(4)},
\tag{RU.6}

and, exactly,

\[
\boxed{\langle u,v\rangle=1.}
\tag{RU.7}

Indeed the diagonal coefficient \(j=\ell\) contributes \(4^j\), independently
of the zero location.

A reflected pair of multiplicity \(m\) therefore has exactly two nonzero
normalized eigenvalues

\[
\boxed{
\lambda_\pm
=m\left(1\pm R_k(q)\right),
\qquad
R_k(q)={\sqrt{C_k(q^2)C_k(16/q^2)}\over C_k(4)}.
}
\tag{RU.8}

## 3. Strict and exponential depth

The function

\[
t\longmapsto\log C_k(e^t)
\]

is strictly convex for \(k\ge1\): its second derivative is the variance of the
index \(j\) under the positive weights
\(\binom{k}{j}^2e^{tj}\). The two arguments in (RU.8) have logarithmic midpoint
\(\log4\). Hence

\[
\boxed{R_k(q)>1\qquad(q\ne2).}
\tag{RU.9}

Thus every off-line reflected pair creates a genuine negative eigenvalue.

There is also an explicit exponential lower bound. Cauchy–Schwarz gives

\[
C_k(x)\ge{(1+\sqrt x)^{2k}\over k+1},
\]

while

\[
C_k(4)\le(1+2)^{2k}=9^k.
\]

Therefore

\[
\boxed{
R_k(q)
\ge{1\over k+1}
\left[{(1+q)(1+4/q)\over9}\right]^k.
}
\tag{RU.10}

Since

\[
(1+q)(1+4/q)=5+q+4/q>9
\]

for \(q\ne2\), the negative moat

\[
\boxed{-\lambda_-=m(R_k(q)-1)}
\tag{RU.11}

is exponentially deep in \(k\) for every fixed off-line depth.

This is a channel effect, not scalar inner-power amplification. The scalar
Q4 power failure of `R-32404` remains valid.

## 4. Separate Dirichlet systems and phase-separated generalized primes

For each channel define

\[
\boxed{
B_{\omega,k}(s)={F_{\omega,k}(s)\over\zeta(s)},
\qquad A_{\omega,k}=B_{\omega,k}^{-1}.
}
\tag{RU.12}

Its generalized-prime sequence is

\[
\boxed{
\Lambda_{\omega,k}
=\Lambda+kL\sum_{r\ge1}\omega^r4^r\delta_{4^r}.
}
\tag{RU.13}

Fix an integer carry endpoint \(n\), let

\[
R=\lfloor\log_4n\rfloor,
\]

and choose

\[
\boxed{M>2\max(k,R).}
\tag{RU.14}

For a carry row \(e=(n,j)\), write

\[
F(e)=\mathcal L_e(\Lambda)=\log\binom nj,
\]

\[
d_r(e)=kL4^r\chi_{n,4^r}(j),
\]

and

\[
P_\omega(e)=\mathcal L_e(\Lambda_{\omega,k}).
\]

Then

\[
P_\omega=F+\sum_{r=1}^R\omega^rd_r,
\]

and phase orthogonality gives

\[
\boxed{
{1\over M}\sum_\omega|P_\omega(e)|^2
=F(e)^2+\sum_{r=1}^Rd_r(e)^2.
}
\tag{RU.15}

Let

\[
C_{\omega,k}
=\Lambda_{\omega,k}\log
 +\Lambda_{\omega,k}*\Lambda_{\omega,k}.
\]

Because \(M>2R\):

- every local logarithmic term has nonzero phase;
- every ordinary/local mixed term has nonzero phase;
- every active local/local product has phase \(r_1+r_2\) strictly between
  zero and \(M\).

Consequently

\[
\boxed{
{1\over M}\sum_\omega C_{\omega,k}
=\Lambda\log+\Lambda*\Lambda
}
\tag{RU.16}

through the complete endpoint \(n\).

Therefore the averaged Selberg–Kummer reserve is exactly

\[
\boxed{
\begin{aligned}
\mathcal R_{M,k}(e)
&={1\over M}\sum_\omega
 \left(|P_\omega(e)|^2-
       \mathcal L_e(C_{\omega,k})\right)\\
&=F(e)^2-S_0(e)+\sum_{r=1}^Rd_r(e)^2\\
&\ge0,
\end{aligned}}
\tag{RU.17}

where \(S_0\) is the ordinary Selberg forcing and the final inequality is the
ordinary Selberg–Kummer theorem.

Thus arbitrary power \(k\) is compatible with a complete positive row reserve
once the local levels are separated before the Hermitian square.

## 5. Exact current frame and polynomial deterministic gauge

Let

\[
B_0={1\over\zeta},\qquad q_0=B_0'.
\]

The separate-system inverse-source current is

\[
q_{\omega,k}=B_{\omega,k}'
=F_{\omega,k}q_0+g_{\omega,k},
\tag{RU.18}

with

\[
\boxed{
g_{\omega,k}
=kL\,\omega a(1-\omega a)^{k-1}B_0.}
\tag{RU.19}

The first term is the gauge-free externally filtered ordinary pole current.
On the critical line,

\[
\boxed{
{1\over M\mathfrak C_k}
\sum_\omega|F_{\omega,k}q_0|^2
=|q_0|^2.
}
\tag{RU.20}

The normalized gauge energy is exactly

\[
{1\over M\mathfrak C_k}
\sum_\omega|g_{\omega,k}|^2
=4k^2L^2{C_{k-1}(4)\over C_k(4)}|B_0|^2
\le4k^2L^2|B_0|^2.
\tag{RU.21}

After multiplication by the common atomized physical factor
\(\zeta(s)N_\theta(s)\), the factor \(B_0\) cancels. Hence the gauge becomes a
completely explicit deterministic field with only polynomial \(k^2\) energy.

In particular,

\[
\boxed{
{1\over M\mathfrak C_k}
\sum_\omega|F_{\omega,k}q_0|^2
\le
{2\over M\mathfrak C_k}
\sum_\omega|q_{\omega,k}|^2
+8k^2L^2|B_0|^2.
}
\tag{RU.22}

No exponential arithmetic loss is introduced by passing from the separate
systems to the genuine ordinary pole current.

## 6. What this changes

The scalar powered-Q4 route failed because the same mixed local forcing was
stacked repeatedly in one generalized-prime row. The root-of-unity powered
frame has the opposite behavior:

```text
critical current frame                 exactly normalized;
off-line pair negative depth           exponential in k;
active four-adic generalized primes     separated by phase;
complete averaged Selberg reserve       ordinary reserve + local squares;
current gauge                           deterministic, polynomial in k;
channel count                           finite, M>2 max(k,log_4 n).
```

This is the first source family in the repository that combines the Anthropic
off-line signature mechanism with arbitrary Euler–Blaschke depth **without**
destroying the source-matched Selberg reserve.

## 7. Exact remaining theorem

The theorem does not yet prove RH. The remaining production statement is a
uniform independent-frequency accounting theorem:

> after physical localization, average the complete reflected identities of
> the \((\omega,k)\) systems, use (RU.17) without spending the ordinary reserve
> twice, and prove that the normalized product/current block is bounded by a
> subexponential function of \(k\) plus the polynomial gauge.

Any bound

\[
\exp(o(k))
\]

for that complete normalized arithmetic block would contradict the exponential
negative eigenvalue (RU.10) from a hypothetical off-line zero and prove RH.

The gap is now an explicit growth comparison, not a sign, local-source, channel,
or interpolation-conditioning problem.

## 8. Scope firewall

Do not infer the final subexponential block bound from:

- row reserve positivity alone;
- scalar powers of one Q4 source;
- a same-lattice direct-sum trace estimate;
- the normalized critical frame identity without prime off-diagonal control;
- finite \(k\) computations.

Closed here are the exact phase frame, off-line spectrum, complete finite row
reserve, and polynomial gauge theorem. The full independent-frequency growth
bound remains RH-bearing.
