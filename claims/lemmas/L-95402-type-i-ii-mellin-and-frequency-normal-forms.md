# L-95402 — Exact Type I/II, Mellin and frequency normal forms for annular FOCC

Claim ID: `L-95402`  
Status: **PROPOSED COMPLETE EXACT REWRITING THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Depends on: `L-95400/L-95401`  
Scope: source-faithful arithmetic normal forms; no claimed estimate for the final Type-II form

## 1. The logarithmic and boundary channels

Write

\[
\mathcal A(X)=\mathcal A_0(X)+(\log2)\mathcal A_1(X),
\]

where

\[
\mathcal A_0(X)
=
\sum_m\frac{\mu(m)\log m}{\sqrt m}J_0(m/X),
\tag{L-95402.1}
\]

and

\[
\mathcal A_1(X)
=
\sum_m\frac{\mu(m)}{\sqrt m}J_1(m/X).
\tag{L-95402.2}
\]

All sums are over odd squarefree `m` in the factor-1024 annulus.

## 2. Exact prime-divisor expansion

For every squarefree `m>1`,

\[
\boxed{
\mu(m)\log m
=-\sum_{p\mid m}(\log p)\mu(m/p).
}
\tag{L-95402.3}
\]

Consequently

\[
\boxed{
\mathcal A_0(X)
=-
\sum_{p\ \mathrm{odd}}
\frac{\log p}{\sqrt p}
\sum_{d\ \mathrm{odd\ squarefree}\atop(d,p)=1}
\frac{\mu(d)}{\sqrt d}
J_0(pd/X).
}
\tag{L-95402.4}
\]

Every activation remains literal through the factor `J_0(pd/X)`.

Choose the symmetric threshold

\[
U=\sqrt X.
\]

Then

\[
\mathcal A_0=\mathcal T_I+\mathcal T_{II},
\]

where

\[
\mathcal T_I
=-
\sum_{p\le U}
\frac{\log p}{\sqrt p}
\sum_{d\atop(d,p)=1}
\frac{\mu(d)}{\sqrt d}J_0(pd/X),
\tag{L-95402.5}
\]

and

\[
\boxed{
\mathcal T_{II}
=-
\sum_{p>U}
\frac{\log p}{\sqrt p}
\sum_{d<U}
\frac{\mu(d)}{\sqrt d}J_0(pd/X).
}
\tag{L-95402.6}
\]

In the second form, coprimality is automatic because `p>d`. The activation requires

\[
X/1024<pd\le X.
\]

Thus the large-prime part is an exact bilinear form with both variables at most `sqrt(X)` after the reciprocal change `p approximately X/d`; it is not an all-integer surrogate.

The `J_1` boundary channel has no `log m` factor and remains as the explicit lower-order reciprocal-zeta state (L-95402.2). It may not be deleted.

## 3. Mellin transform

Put

\[
M_{\mathrm{odd}}(s)
=
\sum_{m\ \mathrm{odd}}\frac{\mu(m)}{m^s}
=
\frac1{(1-2^{-s})\zeta(s)}.
\tag{L-95402.7}
\]

For `Re z` initially large, Mellin interchange gives

\[
\boxed{
\int_1^\infty\mathcal A(X)X^{-z-1}\,dX
=
-\widehat J_0(z)M_{\mathrm{odd}}'(z+\tfrac12)
+(\log2)\widehat J_1(z)M_{\mathrm{odd}}(z+\tfrac12).
}
\tag{L-95402.8}
\]

By `L-95400`,

\[
\widehat J_\nu(z)=q(z)\widehat K_\nu(z),
\]

where `q` has zeros only on `Re z=-1,-2,-3`. The finite Q4 factors do not cancel a pole coming from a zero

\[
\rho=z+\tfrac12,
\qquad \Re\rho>\tfrac12.
\]

Thus a polylogarithmic bound for `mathcal A` is conclusion-producing rather than a routine smoothing consequence.

## 4. Log-Fourier representation

Put

\[
\varphi_{\nu}(u)=J_\nu(e^{-u}),
\qquad 0\le u\le10\log2.
\]

Then

\[
\widehat J_\nu(\sigma+it)
=
\int_0^{10\log2}
\varphi_\nu(u)e^{-(\sigma+it)u}\,du.
\tag{L-95402.9}
\]

The transform is entire of exponential type `10 log 2`. It is not compactly supported in `t`.

For a dyadic annular Dirichlet polynomial

\[
P(t)=\sum_{X/1024<m\le X}c_m m^{-it},
\]

the elementary Hilbert-inequality expansion gives

\[
\boxed{
\int_{-T}^{T}|P(t)|^2dt
\le
(2T+C X)\sum_m|c_m|^2
}
\tag{L-95402.10}
\]

with an absolute constant `C`. Indeed

\[
|\log(m/n)|\ge\frac{|m-n|}{X}
\]

on the annulus, and the off-diagonal integral kernel is bounded by

\[
\frac2{|\log(m/n)|}
\le
\frac{2X}{|m-n|}.
\]

Hilbert's inequality completes the estimate.

At any fixed Mellin window `T=polylog(X)`, the `CX` term remains. Mellin compactness therefore supplies no source-blind polylogarithmic pointwise estimate.

## 5. Ratio form of the square

The annular square has the exact ratio-kernel form

\[
\mathcal X_A(X)
=
2\sum_{m<n}
\mu(m)\mu(n)
\frac{\Gamma_X(m/X)\Gamma_X(n/X)}{\sqrt{mn}},
\tag{L-95402.11}
\]

where

\[
\Gamma_X(x)
=(\log X+\log x)J_0(x)+(\log2)J_1(x).
\]

After `m=da,n=db`, this becomes

\[
\boxed{
2\sum_{a<b<1024a\atop(a,b)=1}
\mu(a)\mu(b)
\sum_{d\in\mathcal I_X(a,b)\atop(d,ab)=1}
\frac{
\Gamma_X(da/X)\Gamma_X(db/X)
}{d\sqrt{ab}},
}
\tag{L-95402.12}
\]

where `d,a,b` are odd squarefree and `mathcal I_X(a,b)` is the exact intersection of the two activation intervals from `L-95401`.

The inner common-divisor kernel is sign free. The only arithmetic signs left are the coprime parity character `mu(a)mu(b)`.

Because `(a,b)=1`, one may also put `k=ab`. Then

\[
\mu(a)\mu(b)=\mu(k),
\]

and the complete balanced Type-II core becomes the single-sign product form

\[
\boxed{
2\sum_{k\ \mathrm{odd\ squarefree}}\mu(k)
\sum_{a\mid k\atop a<k/a<1024a}
\sum_{d\in\mathcal I_X(a,k/a)\atop(d,k)=1}
\frac{
\Gamma_X(da/X)\Gamma_X(dk/(aX))
}{d\sqrt{k}}.
}
\tag{L-95402.13}
\]

The divisor-pair weight is explicit and finite. This reparametrization
collapses the two coprime signs to one Möbius sign but does not remove the
reciprocal-zeta obstruction.

## 6. Pretentious and dispersion boundary

The Type I/II and gcd rewritings preserve all six Q4 bands, but they do not remove the reciprocal-zeta source. Any estimate that replaces `mu` by absolute values loses a factor of order `sqrt(X)`. Any estimate depending only on the modulus-one character, local support, or the diagonal square is ruled out by `R-95400`.

A successful dispersion theorem must therefore estimate the complete coprime Type-II form (L-95402.12), including the `J_1` boundary and all band cross terms, at square-root strength. Standard zero-free-region or pretentious first-moment bounds do not reach that scale.

## 7. Boundary

```text
source-faithful Type I/II split             EXACT
large-prime bilinear form                   EXACT
J1 boundary retained                       EXACT
Mellin transform and pole audit             EXACT
log-Fourier entire/exponential type         EXACT
fixed-window large-sieve loss O(X)          EXACT
coprime finite-ratio dispersion estimate    OPEN / RH-BEARING
Riemann Hypothesis                          UNPROVEN
```
