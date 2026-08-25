# T-106620 — Mesoscopic frozen Riemann--Siegel-gauge frontier for more than ninety percent

Claim ID: `T-106620`  
Status: **UNCONDITIONAL INDEX/HEIGHT/CARRIER REDUCTION + ONE SHALLOW ARITHMETIC CORRELATION OPEN**  
Created: 2026-08-26  
Depends on: `L-106500--L-106514`, `L-106620--L-106621`; pinned
\(R_5/N>997/1000-o(1)\) input  
RH status: **unproved**

## 1. Why the gauge is frozen

`R-106620` shows that the fixed analytic scale \(1/\vartheta'(t)\), although
\(O(1/\log T)\), has not been proved smaller than the window-dependent
Rouché threshold required by `L-106603`.

The repair is to partition \([T,2T]\) into
\(J_T=\lceil(\log T)^B\rceil\) regular mesoscopic windows and use the constant

\[
\lambda_j=\vartheta'(t_j)^{-1}
\]

on each window.

Constant scales retain the exact endpoint index and admit the rank-one
companion-height theorem. Their carrier mismatch is
\(O((\log T)^{-B-1})\).

## 2. Exact arithmetic packet

On each subwindow,

\[
U_{5,j}
=
\frac{R_{0,j}C_{5,j}}{C_{0,j}R_{5,j}},
\]

where \(C_{k,j},R_{k,j}\) are explicit finite combinations of
\(\zeta,\ldots,\zeta^{(k+1)}\) and known gamma/digamma coefficients.
The endpoint difference is exactly

\[
R_{0,j}C_{5,j}-C_{0,j}R_{5,j}
=
2i\lambda_j
\left(h\,DH_5-(Dh)H_5\right).
\]

Thus the amplitude connection cancels exactly and the Riemann--Siegel carrier
is matched to arbitrary fixed logarithmic accuracy without using a variable
scale.

## 3. Macroscopic charge is closed

`L-106621` proves

\[
\sum_j\sum_{B_{-,j}(x+iy)=0}y
\le
\left(\frac3{4000}+o(1)\right)N(T,2T).
\]

At height cutoff \(1/100\), every deep denominator direction costs at most

\[
\left(\frac3{40}+o(1)\right)N(T,2T).
\]

## 4. The single remaining gate

Let

\[
\mathfrak C_{\rm meso,sh}(T)
=
\sum_j
\left\|
P_{K_{B_{-,j}^{\le1/100}}}
T_{B_{+,j}}
\right\|_{\mathcal S_2}^2
\]

for the reduced inner factors of the explicit cross-ratios \(U_{5,j}\).
Let \(\mathcal E_{\rm meso,reg}\) retain all common-zero, confluent, boundary,
partition, and cofinal-exhaustion terms.

Define `MESORSGAUGE106620` by

\[
\boxed{
\limsup_{T\to\infty}
\frac{
\mathfrak C_{\rm meso,sh}(T)
+\mathcal E_{\rm meso,reg}(T)
}{
N(T,2T)
}
<
\frac{11}{500}.
}
\tag{T-106620.1}
\]

Then

\[
\sum_j\|H_{U_{5,j}}\|_{\mathcal S_2}^2
<
\left(\frac3{40}+\frac{11}{500}+o(1)\right)N
=
\left(\frac{97}{1000}+o(1)\right)N.
\]

The summed endpoint index and the pinned fifth-derivative theorem therefore
give

\[
\boxed{
\mathrm{MESORSGAUGE}_{106620}
\Longrightarrow
\liminf_{T\to\infty}
\frac{N_0(T,2T)}{N(T,2T)}
>0.9.
}
\tag{T-106620.2}
\]

## 5. Boundary

```text
exact Riemann--Siegel gauge factorization        PROVED
fixed-scale diagonal Rouché inference            REFUTED
mesoscopic constant carrier matching             PROVED
amplitude-connection cancellation                PROVED
constant-scale denominator height <=3/4000 N     PROVED
all charge above height 1/100                    PAID <=3/40 N
MESORSGAUGE106620 <11/500                        OPEN / 90%-BEARING
ninety percent / density one / RH                UNPROVED
```

The theorem supersedes only the height assertion attached to the exact
variable scale in `T-106610`. Its algebraic gauge identities remain valid.
