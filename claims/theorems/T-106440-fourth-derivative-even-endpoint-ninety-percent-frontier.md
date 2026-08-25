# T-106440 — Fourth-derivative even-endpoint frontier for ninety percent

Claim ID: `T-106440`  
Status: **UNCONDITIONAL ENDPOINT/SOURCE REDUCTION; EVENST106440 OPEN**  
Created: 2026-08-25  
Depends on: `L-106440--L-106443`; pinned unconditional fixed-order input `R_4/N>2487/2500-o(1)`  
RH status: **unproved**

The order-two endpoint of `T-106430` is not the strongest fixed-order entry.
The same exact architecture applies directly from `Xi^(4)` to `Xi`, with no
intermediate companion estimate.

## 1. Endpoint symbol

Put

\[
U_{0,4,T}
 =\frac{(\Xi-i\lambda_T\Xi')
          (\Xi^{(4)}+i\lambda_T\Xi^{(5)})}
        {(\Xi+i\lambda_T\Xi')
          (\Xi^{(4)}-i\lambda_T\Xi^{(5)})}.
\tag{T-106440.1}

Then

\[
\operatorname{wind}U_{0,4,T}=R_0(T,2T)-R_4(T,2T)+o(N),
\]

and the actual numerator is

\[
2i\lambda_T
\bigl(\Xi\Xi^{(5)}-\Xi'\Xi^{(4)}\bigr).
\]

Its Fourier transform is `i xi` times the nonnegative density

\[
\Lambda_2(\xi)
 ={1\over2}\int
 (u-v)^2(u^2+v^2)\Phi(u)\Phi(v)\,du.
\]

## 2. Visible and signed-unobserved charges

Let `P_(4,T)` be the fixed four-channel source projection of `L-106443`.  Put

\[
\Delta_{4,T}
 =\operatorname{tr}
   \bigl(P_{4,T}^\perp H_{U_{0,4,T}}^*H_{U_{0,4,T}}P_{4,T}^\perp\bigr)
 -\operatorname{tr}
   \bigl(P_{4,T}^\perp H_{\overline{U_{0,4,T}}}^*
          H_{\overline{U_{0,4,T}}}P_{4,T}^\perp\bigr).
\tag{T-106440.2}

The exact signed index split and `L-106443` give

\[
\boxed{
R_0(T,2T)
 \ge R_4(T,2T)
 -{1\over982}N(T,2T)
 -(\Delta_{4,T})_+
 -o(N(T,2T)).
}
\tag{T-106440.3
}

The exact source constant may replace `1/982`; the displayed value is a clean
rational upper bound.

## 3. Enlarged ninety-percent allowance

The pinned unconditional fixed-order theorem gives

\[
\frac{R_4(T,2T)}{N(T,2T)}
 >\frac{2487}{2500}-o(1)=0.9948-o(1).
\]

Therefore the remaining signed-tail allowance above ninety percent is

\[
\boxed{
\frac{2487}{2500}-\frac9{10}-\frac1{982}
 =\frac{115117}{1227500}
 =0.0937816700\ldots .
}
\tag{T-106440.4}

Define

```text
EVENST106440:

limsup_(T->infinity)
  (Delta_(4,T))_+ / N(T,2T)
< 115117/1227500.
```

Then

\[
\boxed{
\mathrm{EVENST}_{106440}
\Longrightarrow
\liminf_{T\to\infty}
\frac{N_0(T,2T)}{N(T,2T)}>0.9.
}
\tag{T-106440.5}

The admissible signed tail is about `9.378%`, versus `5.673%` in the
second-derivative endpoint `T-106430`.

## 4. Residue-Gram form

By `L-106442`, `Delta_(4,T)` is exactly the difference of the upper- and
lower-half-plane Cauchy--exponential residue Grams of the denominator

\[
(\Xi+i\lambda_T\Xi')
(\Xi^{(4)}-i\lambda_T\Xi^{(5)}).
\]

Every simple residue equals

\[
{2i\lambda_T
 (\Xi\Xi^{(5)}-\Xi'\Xi^{(4)})(z)
 \over
 [(\Xi+i\lambda_T\Xi')
  (\Xi^{(4)}-i\lambda_T\Xi^{(5)})]'(z)}.
\]

Thus `EVENST106440` is one explicit signed residue-moment theorem, not an
unspecified contour estimate.

## 5. Boundary

```text
even-endpoint all-pass telescope              PROVED EXACT
actual fourth-endpoint exterior-square source PROVED UNCONDITIONALLY
uniform four-channel visible cost <1/982      PROVED
residue-Gram normal form                      PROVED EXACT
EVENST106440 signed 9.378% estimate            OPEN / RECORD-BEARING
ninety percent for zeta                       UNPROVED
density one                                   UNPROVED
Riemann Hypothesis                            UNPROVED
```