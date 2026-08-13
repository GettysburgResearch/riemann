# L-91352 — The direct `P_79` Euler residual row has a uniform physical-entropy surplus

Claim ID: `L-91352`  
Status: **PROPOSED COMPLETE EXACT/EXPLICIT REPAIR THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-13  
Frozen main parent: `d688cc7cb73eea9e50f10352a50516ab2c4f4625`  
Depends on: exact component entropy `R-91552.4`; direct row identity `L-91351`; inherited-row positivity `L-91346`; positive truncated Euler factorization `L-91317`; Eberl, *Concrete bounds for Chebyshev's prime counting functions* (AFP, 2024), theorem `psi(x)>=0.9x` for `x>=41`; replay `X-91130`  
RH status: **unproved**

## 1. Physical entropy, not declared source score

For `Y>=1`, let

\[
 \mathcal E(Y)
 =\sum_{j\ge2}Q_Y(j)G_j.
\]

The exact double-summation identity gives

\[
\boxed{
 \mathcal E(Y)
 =\sum_{2\le q\le Y}
  \frac{\log q}{\sqrt q}\log\frac Yq.
}
\tag{L-91352.1}
\]

Put

\[
 P=P_{79}=\prod_{q\le79}q
\]

and retain the exact finite Euler row

\[
 D_P(x;j)
 =\sum_{d\mid P}\frac{\mu(d)}{\sqrt d}Q_{x/d}(j)
\]

with causal zero extension. Its literal average-binomial entropy is

\[
\boxed{
 \mathcal E_P(x)
 :=\sum_{j\ge2}D_P(x;j)G_j
 =\sum_{d\mid P}\frac{\mu(d)}{\sqrt d}\mathcal E(x/d).
}
\tag{L-91352.2}
\]

This is the score actually represented by the component row.

## 2. Exact positive von Mangoldt convolution

Substitute (L-91352.1) into (L-91352.2), put `n=dq`, and use

\[
 \log m=\sum_{b\mid m}\Lambda(b).
\]

The coefficient of

\[
 n^{-1/2}\log(x/n)
\]

is

\[
\begin{aligned}
 c_P(n)
 &=\sum_{\substack{d\mid n\\d\mid P}}
   \mu(d)\log(n/d)\\
 &=\sum_{b\mid n}\Lambda(b)
   \sum_{\substack{d\mid n/b\\d\mid P}}\mu(d)\\
 &=\sum_{\substack{ab=n\\(a,P)=1}}\Lambda(b)\ge0.
\end{aligned}
\]

Consequently

\[
\boxed{
 \mathcal E_P(x)
 =\sum_{\substack{ab\le x\\(a,P)=1}}
  \frac{\Lambda(b)}{\sqrt{ab}}
  \log\frac{x}{ab}.
}
\tag{L-91352.3}
\]

This is a coefficientwise positive arithmetic formula. It also explains why a
scalar source label need not equal the row entropy: the row contains a positive
rough multiplier `a` in addition to the prime-power variable `b`.

## 3. One-prime entropy residual

Let

\[
 p\ge83,
 \qquad1\le y<83,
 \qquad x=py,
 \qquad r=p^{-1/2}.
\]

Define

\[
 \mathcal E_{P,p}(x)
 =\mathcal E_P(x)-r\mathcal E_P(y).
\tag{L-91352.4}
\]

For every term with `ab<=y`, its residual logarithmic coefficient is

\[
 \log\frac{x}{ab}-r\log\frac y{ab}
 =\log p+(1-r)\log\frac y{ab}>0.
\tag{L-91352.5}
\]

Terms with `y<ab<=x` occur only in the parent and are also positive. Keeping
only the subfamily `a=1` gives

\[
\boxed{
 \mathcal E_{P,p}(x)
 \ge R(x)-rR(y),
}
\tag{L-91352.6}
\]

where

\[
 R(X)=\sum_{n\le X}
       \frac{\Lambda(n)}{\sqrt n}
       \log\frac Xn.
\tag{L-91352.7}
\]

## 4. A uniform derivative moat

Put

\[
 A(X)=\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n},
 \qquad
 \psi(X)=\sum_{n\le X}\Lambda(n).
\]

The imported formal theorem

\[
 \psi(t)\ge\frac9{10}t
 \qquad(t\ge41)
\tag{L-91352.8}
\]

and partial summation give, for `X>=83`,

\[
\begin{aligned}
 A(X)
 &=\frac{\psi(X)}{\sqrt X}
   +\frac12\int_1^X\frac{\psi(t)}{t^{3/2}}dt\\
 &\ge\frac9{10}\sqrt X
   +\frac9{10}(\sqrt X-\sqrt{41}).
\end{aligned}
\]

Since

\[
 \sqrt{41/83}<\frac{71}{100},
\]

we obtain

\[
\boxed{
 A(X)>\frac{1161}{1000}\sqrt X
 \qquad(X\ge83).
}
\tag{L-91352.9}
\]

For `1<=y<83`, the elementary estimates

\[
 \Lambda(n)\le\log y<\frac92,
 \qquad
 \sum_{n\le y}n^{-1/2}<2\sqrt y
\]

give

\[
 A(y)<9\sqrt y.
\tag{L-91352.10}
\]

On every activation cell, define

\[
 F_p(y)=R(py)-p^{-1/2}R(y)-\frac43\sqrt{py}.
\]

Then

\[
\begin{aligned}
 yF_p'(y)
 &=A(py)-p^{-1/2}A(y)-\frac23\sqrt{py}\\
 &>
 \left(
  \frac{1161}{1000}-\frac9{83}-\frac23
 \right)\sqrt{py}\\
 &=\boxed{
   \frac{96089}{249000}\sqrt{py}
  }>0.
\end{aligned}
\tag{L-91352.11}
\]

The ramp `R` is continuous at every prime-power activation because the entering
term has logarithm zero. Hence `F_p` is strictly increasing on the complete
real interval `1<=y<83`.

At `y=1`, the function

\[
 G(X)=R(X)-\frac43\sqrt X
\]

is itself strictly increasing for `X>=83`, because

\[
 XG'(X)=A(X)-\frac23\sqrt X>0.
\tag{L-91352.12}
\]

Thus the global minimum of `F_p(y)` occurs at

\[
 (p,y)=(83,1).
\]

## 5. Directed base gate

Keeping only the nine prime-power terms

\[
 2,3,4,5,7,8,9,11,13
\]

in `R(83)`, the directed replay proves

\[
\boxed{
 R(83)>\frac{649}{50}.
}
\tag{L-91352.13}
\]

The exact rational inequality

\[
 \sqrt{83}<\frac{228}{25}
\]

gives

\[
 \frac43\sqrt{83}<\frac{304}{25}.
\]

Therefore

\[
\boxed{
 R(83)-\frac43\sqrt{83}>rac{41}{50}>0.
}
\tag{L-91352.14}
\]

Combining Sections 3--5 yields the uniform physical entropy bound

\[
\boxed{
 \mathcal E_{P,p}(py)>rac43\sqrt{py}
 \qquad(p\ge83,\ 1\le y<83).
}
\tag{L-91352.15}
\]

## 6. The native target and source-score upper corridor

For

\[
 F_{a,Q}(X)
 =\sum_{d\mid Q}\mu(d)
  \left(\frac{a\sqrt X}{d}-\frac1{\sqrt d}\right),
 \qquad1\le a\le2,
\]

the positive truncated Euler factorization shows that adjoining a new prime
preserves positivity. The exact recurrence

\[
 F_{a,Qq}(X)=F_{a,Q}(X)-q^{-1/2}F_{a,Q}(X/q)
\]

therefore also shows that every additional Euler factor can only decrease the
forcing.

At `X>=83`, the complete block `Q=30` is active, and

\[
 F_{a,30}(X)
 =a\sqrt X\prod_{q\mid30}(1-q^{-1})
  -\prod_{q\mid30}(1-q^{-1/2})
 <\frac{4a}{15}\sqrt X.
\tag{L-91352.16}
\]

Thus

\[
\boxed{
 \mathfrak T_P(X)<\frac{16}{15}\sqrt X,
 \qquad
 \mathfrak S_P(X)<\frac43\sqrt X.
}
\tag{L-91352.17}
\]

The child target and score are positive, so the one-prime residuals satisfy the
same upper bounds:

\[
\boxed{
 \mathfrak T_{Pp}(py)<\frac{16}{15}\sqrt{py},
 \qquad
 \mathfrak S_{Pp}(py)<\frac43\sqrt{py}.
}
\tag{L-91352.18}
\]

## 7. Corrected score conclusion

Equations (L-91352.15) and (L-91352.18) give

\[
\boxed{
 \mathcal E_{P,p}(py)>
 \mathfrak S_{Pp}(py)
 \quad\text{and}\quad
 \mathcal E_{P,p}(py)-\mathfrak T_{Pp}(py)
 >\frac4{15}\sqrt{py}.
}
\tag{L-91352.19}
\]

Therefore, provided the inherited-row positivity theorem `L-91346` and the
resident exact current-frontier/collar assembly survive review in the same row
normalization, the direct current-generation arithmetic row has strictly
negative physical score loss. The false scalar inequality refuted in
`R-91310` is not needed.

This repair is stronger than the original claim:

```text
original attempted statement:
    declared source score > declared target;

correct physical statement:
    literal component-row entropy > declared score and target.
```

## 8. Scope firewall

This theorem does not establish the complete factor-54 proof by itself. It
repairs one exact interface only. The following still require independent
source-bound review:

```text
coefficientwise positivity of the inherited residual row L-91346;
terminal P79 target/row typing L-91342;
exact realization of all rows j>y by the current frontier;
one-use frontier/collar/radix-four assembly;
substochastic recurrence and the final loss-to-RH consumer.
```

```text
exact component-row entropy                       EXACT
positive von Mangoldt convolution                 EXACT
uniform physical entropy > (4/3)sqrt(py)          EXACT FROM IMPORTED PSI BOUND
source target/score upper corridor                EXACT
false scalar score-over-target surplus            NOT USED
current arithmetic physical loss                  STRICTLY FAVORABLE, CONDITIONAL ON EXACT ROW ASSEMBLY
full factor-54 composition                        REVIEW REQUIRED
Riemann Hypothesis                                UNPROVEN
```
