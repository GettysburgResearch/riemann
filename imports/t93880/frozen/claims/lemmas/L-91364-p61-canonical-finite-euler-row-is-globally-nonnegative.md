# L-91364 — The canonical `P_61` finite-Euler component row is globally nonnegative

Claim ID: `L-91364`  
Status: **PROPOSED COMPLETE EXACT/DIRECTED GLOBAL ROW THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-13  
Frozen parent: PR #439 at `1546d866cdedb8a13b55b2deb154e47e0559e808`  
Depends on: retained `L-91112.25--26`; exact Green decomposition `L-91344`; finite-block error corridor from `L-91346`; replay `X-91138`  
RH status: **unproved**

## 1. Statement

Put

\[
P=P_{61}=\prod_{p\le61}p
\]

and retain the positive component row

\[
Q_Y(j)
=(j+1)\Delta^2\!\left[\frac{S_Y(j)}{j-1}\right],
\qquad j\ge2,
\]

with causal value zero for `Y<j`. Define the canonical finite-Euler row

\[
\boxed{
D_{P,X}(j)
=\sum_{\substack{d\mid P\\d\le X/j}}
 \frac{\mu(d)}{\sqrt d}\,Q_{X/d}(j).
}
\tag{L-91364.1}
\]

Then, for every real `X>=1` and every integer `j>=2`,

\[
\boxed{D_{P,X}(j)\ge0.}
\tag{L-91364.2}
\]

More precisely,

\[
D_{P,X}(j)=0\quad(X\le j),
\qquad
D_{P,X}(j)>0\quad(X>j).
\tag{L-91364.3}
\]

This is coefficientwise positivity of the actual finite average-binomial row. It is stronger than positivity of its ordinary columns, radix-four columns, or total entropy.

## 2. The first quotient cell

If

\[
1\le u:=X/j<2,
\]

then no divisor `d>1` can occur in (L-91364.1). Hence

\[
D_{P,X}(j)=Q_X(j)\ge0,
\tag{L-91364.4}
\]

with strict positivity for `X>j`.

It remains to treat `u>=2`.

## 3. Large-row scaling limit

For `v>=1`, put

\[
R_j(v)=j^{3/2}Q_{jv}(j)
\tag{L-91364.5}
\]

and define

\[
\boxed{
q(v)=8\sqrt v-7-\frac32\log v.
}
\tag{L-91364.6}
\]

The function is positive and increasing on `v>=1`.

### 3.1 Local two-node part

Using the three-sector formula for `Q`, write

\[
R_j(v)=L_j(v)+T_j(v),
\]

where

\[
L_j(v)=c_j\log v+k_j,
\tag{L-91364.7}
\]

\[
c_j=
\frac{j[(j+1)-(j-2)\sqrt{1+1/j}]}{j-1},
\tag{L-91364.8}
\]

and

\[
k_j=
\frac{j(j-2)\sqrt{1+1/j}}{j-1}
\log\!\left(1+\frac1j\right).
\tag{L-91364.9}
\]

The elementary bounds

\[
1+\frac1{2j}-\frac1{8j^2}
\le\sqrt{1+\frac1j}
\le1+\frac1{2j}
\]

and

\[
\frac1j-\frac1{2j^2}
\le\log\!\left(1+\frac1j\right)
\le\frac1j
\]

give, for `j>=3`,

\[
0<c_j-\frac52<\frac4{j-1},
\qquad
0<1-k_j<\frac2{j-1}.
\tag{L-91364.10}
\]

Consequently

\[
\left|
L_j(v)-\left(1+\frac52\log v\right)
\right|
\le
\frac{2+4\log v}{j-1}.
\tag{L-91364.11}
\]

### 3.2 Tail Riemann sum

Put

\[
f_v(t)=t^{-1/2}\log(v/t)\mathbf1_{1\le t\le v}
\]

and

\[
I(v)=\int_1^v f_v(t)\,dt
=4\sqrt v-4-2\log v.
\tag{L-91364.12}
\]

For `v>=1+1/j`,

\[
T_j(v)
=\frac2{j-1}
\sum_{m=j+2}^{\lfloor jv\rfloor}f_v(m/j).
\tag{L-91364.13}
\]

Because `f_v` is nonnegative and decreasing,

\[
0\le
I(v)-\frac1j
\sum_{m=j+2}^{\lfloor jv\rfloor}f_v(m/j)
\le\frac{2\log v}{j}.
\tag{L-91364.14}
\]

It follows that

\[
\left|T_j(v)-2I(v)\right|
\le
\frac{4\log v+8\sqrt v}{j-1}.
\tag{L-91364.15}
\]

Combining (L-91364.11)--(L-91364.15),

\[
\boxed{
|R_j(v)-q(v)|
\le
\frac{2+8\log v+8\sqrt v}{j-1},
\qquad
v\ge1+\frac1j.
}
\tag{L-91364.16}
\]

The estimate is intentionally coarse but uniform.

## 4. Finite-Euler limit profile

Define

\[
\boxed{
F(u)
=\sum_{\substack{d\mid P\\d\le u}}
 \frac{\mu(d)}{\sqrt d}\,
 q(u/d).
}
\tag{L-91364.17}
\]

On one divisor-activation cell, put

\[
A=\sum_{d\le u}\frac{\mu(d)}d,
\qquad
B=\sum_{d\le u}\frac{\mu(d)}{\sqrt d},
\qquad
C=\sum_{d\le u}\frac{\mu(d)\log d}{\sqrt d}.
\]

Then

\[
\boxed{
F(u)
=8A\sqrt u
-\left(7+\frac32\log u\right)B
+\frac32C.
}
\tag{L-91364.18}
\]

Thus `F` is elementary on every one of the `2^18` divisor cells. In the variable `t=sqrt(u)`,

\[
\frac{dF}{dt}=8A-\frac{3B}{t}.
\tag{L-91364.19}
\]

An interior minimum can occur only when `A>0`, `B>0`, and `3B/(8A)` lies in the current cell.

The directed replay checks every cell endpoint and excludes every possible interior minimum. It proves

\[
\boxed{
F(u)>\frac52,
\qquad
2\le u\le67,
}
\tag{L-91364.20}
\]

with directed minimum

\[
2.5668809469\ldots
\]

at the first divisor cell.

For

\[
H(u)=F(u)-\frac34\sqrt u,
\]

the same cell analysis proves

\[
\boxed{
F(u)-\frac34\sqrt u>\frac3{20},
\qquad
u\ge67.
}
\tag{L-91364.21}
\]

The directed minimum is

\[
0.1547430065\ldots
\]

at `u=82`, on the cell beginning at `78`.

## 5. Activation-strip correction

Estimate (L-91364.16) is not uniform in the first width-`1/j` activation strip. For a lower bound on the signed Euler sum, only positive-Möbius divisors in that strip are adverse.

For `j>=511`,

\[
\frac{j+1}{j}\le\frac{512}{511}
\]

and the directed divisor census proves

\[
\sup_{\substack{2\le u\le67}}
\sum_{\substack{\mu(d)=1\\u/(1+1/j)<d\le u}}
\frac1{\sqrt d}
<
\frac5{12},
\tag{L-91364.22}
\]

\[
\sup_{\substack{u\ge67}}
\sum_{\substack{\mu(d)=1\\u/(1+1/j)<d\le u}}
\frac1{\sqrt d}
<
\frac18.
\tag{L-91364.23}
\]

The respective extremal windows contain only `d=6` and `d=69`.

The same replay proves

\[
q(512/511)<\frac{101}{100}.
\tag{L-91364.24}
\]

## 6. Large rows: compact quotient range

The exact absolute divisor masses satisfy

\[
\sum_{\substack{d\mid P\\d\le67}}\frac1{\sqrt d}<10,
\qquad
\sum_{\substack{d\mid P\\d\le67}}\frac1d<4.
\tag{L-91364.25}
\]

For `2<=u<=67`, summing (L-91364.16) over active divisors gives an error below

\[
\frac{
2\cdot10
+8(\log67)\cdot10
+8\sqrt{67}\cdot4
}{j-1}
<
\frac{624}{j-1}.
\tag{L-91364.26}
\]

Using (L-91364.20), (L-91364.22), and (L-91364.24), for every `j>=511`,

\[
\begin{aligned}
j^{3/2}D_{P,ju}(j)
&>
\frac52-\frac{624}{510}
-\frac{101}{100}\frac5{12}\\
&=
\boxed{\frac{3491}{4080}>0.}
\end{aligned}
\tag{L-91364.27}
\]

## 7. Large rows: global quotient range

The complete absolute divisor masses satisfy

\[
\sum_{d\mid P}\frac1{\sqrt d}<60,
\qquad
\sum_{d\mid P}\frac1d<5.
\tag{L-91364.28}
\]

For `u>=67`,

\[
\log u/\sqrt u\le\log67/\sqrt{67}<\frac{17}{32},
\qquad
\sqrt u>8.
\]

Hence the summed approximation error is below

\[
\frac{
120+480\log u+40\sqrt u
}{j-1}
<
\frac{310\sqrt u}{j-1}.
\tag{L-91364.29}
\]

The activation-strip loss in (L-91364.23)--(L-91364.24) is less than

\[
\frac1{32}\sqrt u.
\tag{L-91364.30}
\]

Therefore, using (L-91364.21), for `j>=511` and `u>=67`,

\[
\begin{aligned}
j^{3/2}D_{P,ju}(j)
&>
\left(
\frac34-\frac{310}{510}-\frac1{32}
\right)\sqrt u\\
&=
\boxed{
\frac{181}{1632}\sqrt u>0.
}
\end{aligned}
\tag{L-91364.31}
\]

Sections 2, 6, and 7 prove the theorem for every `j>=511`.

## 8. Finite rows below the quotient split

It remains to treat

\[
2\le j\le510.
\]

For an integer `n`, define

\[
\gamma_j(m)=
\begin{cases}
j(j+1),&m=j,\\
-(j+1)(j-2),&m=j+1,\\
2,&m\ge j+2,\\
0,&m<j.
\end{cases}
\tag{L-91364.32}
\]

Then

\[
\boxed{
j(j-1)D_{P,X}(j)
=
\sum_{n\le X}
\frac{c_j(n)}{\sqrt n}\log(X/n),
}
\tag{L-91364.33}
\]

where the integer coefficient is

\[
\boxed{
c_j(n)
=
\sum_{\substack{d\mid(n,P)\\n/d\ge j}}
\mu(d)\gamma_j(n/d).
}
\tag{L-91364.34}
\]

Between consecutive integer knots, the right side is affine in `log X`. If

\[
V_j(N)=j(j-1)D_{P,N}(j),
\qquad
S_j(N)=\sum_{n\le N}\frac{c_j(n)}{\sqrt n},
\]

then

\[
\boxed{
V_j(N+1)
=V_j(N)+S_j(N)\log\frac{N+1}{N}.
}
\tag{L-91364.35}
\]

The directed checker evaluates every interval

\[
j\le N<67j,
\qquad
2\le j\le510.
\]

It proves all

\[
\boxed{8,600,064}
\]

endpoint inequalities and hence every intervening real cell. The least positive endpoint beyond the trivial first cell is

\[
\boxed{
j(j-1)D_{P,4}(2)
>2.9407744304.
}
\tag{L-91364.36}
\]

Thus

\[
D_{P,X}(j)>0
\qquad
(2\le j\le510,\ j<X\le67j).
\tag{L-91364.37}
\]

## 9. Finite rows above the quotient split

For `X>=67j`, use the exact Green decomposition

\[
D_{P,X}(j)
=
C_j\mathcal R_P(X)
+\int E_P(\log X+t)\,d\nu_j(t)
+\beta_{61}
\int(\log X+t)\,d\nu_j(t),
\tag{L-91364.38}
\]

where

\[
C_j=\frac2{j(j-1)},
\qquad
\beta_{61}=\prod_{p\le61}(1-p^{-1/2}),
\]

\[
\mathcal R_P(X)
=
\sum_{\substack{k\le X\\(k,P)=1}}
\frac1{\sqrt k}\log(X/k)>0,
\]

and `nu_j` is the explicit `j+1`-point boundary measure of `L-91344`.

The finite-block corridor of `L-91346` gives

\[
|E_P|<\frac76,
\qquad
\operatorname{Lip}(E_P)<\frac{27}{20}.
\tag{L-91364.39}
\]

Let

\[
A_j=\sum_{\substack{k\le67j\\(k,P)=1}}\frac1{\sqrt k},
\qquad
B_j=\sum_{\substack{k\le67j\\(k,P)=1}}
\frac{\log k}{\sqrt k}.
\]

Then

\[
\mathcal R_P(X)\ge A_j\log X-B_j.
\tag{L-91364.40}
\]

Writing

\[
s_j=\nu_j(\mathbb R),
\qquad
\ell_j=\int\log m\,d\nu_j,
\]

and `W_j` for the optimal anchored one-dimensional Kantorovich--Rubinstein norm, one obtains

\[
\boxed{
\begin{aligned}
D_{P,X}(j)\ge{}&
\left(C_jA_j+\beta_{61}s_j\right)\log X
-C_jB_j-\beta_{61}\ell_j\\
&-\frac76|s_j|-\frac{27}{20}\mathcal W_j.
\end{aligned}}
\tag{L-91364.41}
\]

For every `2<=j<=510`, the directed replay proves

\[
C_jA_j+\beta_{61}s_j>0
\tag{L-91364.42}
\]

and proves that the right side of (L-91364.41) is positive at `X=67j`. It is therefore positive for every larger `X`.

The smallest certified tail margin is

\[
\boxed{
D_{P,67\cdot510}(510)
>9.2012\times10^{-5}.
}
\tag{L-91364.43}
\]

Combining Sections 8--9 proves the theorem for every `j<=510`.

## 10. Physical consequences

`L-91363` proves that this same canonical row has exact positive ordinary and radix-four responses

\[
C_{P,X}(q)
=\frac1{\sqrt q}H_P(X/q)\ge0,
\]

\[
\Theta_{P,X}(q)
=\frac1{\sqrt q}
[H_P(X/q)-H_P(X/(4q))]\ge0,
\]

and the exact positive literal-entropy density

\[
\mathcal E_P(X)
=
\sum_{n\le X}
\frac{\lambda_P(n)}{\sqrt n}\log(X/n),
\qquad
\lambda_P(n)\ge0.
\]

The present theorem adds the previously missing fact

\[
\boxed{D_{P,X}\ge0\text{ coefficientwise}.}
\]

Thus the complete canonical finite-Euler packet is a genuine nonnegative physical row, not merely a positive image under selected functionals.

## 11. CFFP scope

This theorem closes the hardest row-sign component of the Complete Finite-Forcing Producer.

It does **not by itself** establish CFFP or RH. A complete review must still verify, in one normalization:

1. that the two labelled balanced/reserve forcing packets may be combined into the canonical native row without duplicating source mass;
2. that the imported literal-entropy surplus on PR #437 is the benchmark required by the root endpoint deficit;
3. that the finite base, terminal collar, and common endpoint port are included once;
4. that the positive row capacities above match the exact packet capacities consumed by `T-91307`.

```text
canonical P61 row coefficient sign               CLOSED HERE
ordinary capacity sign                           CLOSED / L-91363
radix-four detail sign                           CLOSED / L-91363
literal entropy density                          CLOSED / L-91363
label/benchmark/port normalization                OPEN / INTEGRATION AUDIT
CFFP                                             NOT YET PROMOTED
Riemann Hypothesis                               UNPROVEN
```

## 12. Replay

```bash
cd experiments/X-91138-p61-global-canonical-row
python3 verify.py
```

Expected verdict:

```text
PASS_P61_CANONICAL_FINITE_EULER_ROW_GLOBAL_POSITIVITY
```

The checker uses only the Python standard library, exact `Fraction` arithmetic, integer fixed-point outward intervals, and exact divisor enumeration.

It certifies:

```text
262,144 divisor states;
524,207 global asymptotic endpoint gates;
209,475 stationary-minimum exclusions;
8,600,064 finite row-cell intervals;
509 finite Green-tail rows;
all activation-strip and divisor-mass corridors.
```

It does not audit the four CFFP integration items in Section 11 and does not certify RH.
