# L-99030 — Hall target exactness gives an exact factor-67 root mass below sixteen

Claim ID: `L-99030`  
Status: **PROPOSED COMPLETE EXACT/DIRECTED THEOREM**  
Created: 2026-08-19  
Parent: PR #620 at `493e12fcba3f9b98dda7c3595bff73b256e00ca4`  
RH status: **not assumed**

## 1. The point of the theorem

The earlier physical-root estimate bounded one Hall fibre by the complete even
target supply and obtained a global mass below `3020`. That estimate is valid
but discards the strongest output of compact Hall: the residual target is
**exactly the signed target**, not merely bounded by the even supply.

The exactness collapses the integrated root mass by two orders of magnitude.

## 2. Exact Hall residual mass on one quotient fibre

For `1<=x<67`, put

\[
 a_N=\sum_{n\le N}\frac{\mu(n)}n,\qquad
 b_N=\sum_{n\le N}\frac{\mu(n)}{\sqrt n},\qquad N=\lfloor x\rfloor.
\]

The positive equality endpoint density is

\[
 L(x)=2a_N\sqrt x-b_N.
\tag{L-99030.1}
\]

The compact single-SHARP signed target is

\[
 \Psi(x)=4a_N\sqrt x-3b_N.
\tag{L-99030.2}
\]

Let `u_x(e)` be the residual target masses from `L-99020`. Target conservation
of the Hall flow gives

\[
\boxed{
 m(P_x)=\sum_eu_x(e)=\sum_k\mu(k)T_x(k)=\Psi(x).
}
\tag{L-99030.3}
\]

The Hall row bonus has target zero and therefore does not alter (L-99030.3).
The strict compact Hall theorem implies `Psi(x)>0` throughout the window.

## 3. Exact endpoint measure

The factor-67 endpoint-frame measure is

\[
\boxed{
 d\nu(x)=\frac{2L(x)}x\,dx,\qquad 1\le x<67.
}
\tag{L-99030.4}
\]

Therefore the total positive recursive root target mass before any common
restriction or safety thinning is

\[
\boxed{
 M_{67}=\int_1^{67}\Psi(x)\frac{2L(x)}x\,dx.
}
\tag{L-99030.5}
\]

This is the actual mass of the Hall residual-source sort. It does not include
the target-free Hall row sort.

## 4. Sixty-six explicit cells

On `N<=x<N+1`,

\[
 \frac{2L(x)\Psi(x)}x
 =16a_N^2-20a_Nb_Nx^{-1/2}+6b_N^2x^{-1}.
\tag{L-99030.6}
\]

Hence the cell integral is exactly

\[
\boxed{
 I_N=16a_N^2
 -40a_Nb_N(\sqrt{N+1}-\sqrt N)
 +6b_N^2\log\frac{N+1}{N}.
}
\tag{L-99030.7}
\]

Thus

\[
 M_{67}=\sum_{N=1}^{66}I_N.
\tag{L-99030.8}
\]

No quadrature, endpoint sampling, or asymptotic estimate enters this formula.

## 5. Directed evaluation

`X-99030` encloses every square root by integer-square bracketing and every
logarithm by the exact atanh series with a rational tail. It obtains

\[
15.7134406686557167269450969040578439770772\ldots
<M_{67}<
15.7134406686557167269450969040578439770773\ldots .
\]

In particular,

\[
\boxed{15<M_{67}<16.}
\tag{L-99030.9}
\]

Any bottom, top, or activation-knot restriction and any common scalar thinning
only decreases this mass.

## 6. Consequence

If a packet theorem incurs terminal score debt at most `C_T` per unit target
mass, then the entire retained root incurs at most `C_T M_67<16C_T`.

For the canonical terminal inequality used in `L-99031`, `C_T=2`; hence the
complete arithmetic score-realization debt is below `32`.

```text
Hall residual target exactness              exact
root endpoint measure                       frozen exact interpretation
66-cell mass formula                        exact
root target mass <16                        directed exact
Hall row bonus target                       zero
restrictions/thinning                       mass nonincreasing
Riemann Hypothesis                          unproved
```
