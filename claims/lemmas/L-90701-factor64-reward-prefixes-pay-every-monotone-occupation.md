# L-90701 — Factor-64 reward prefixes pay every nonincreasing Pascal occupation

Claim ID: `L-90701`  
Status: **PROPOSED COMPLETE EXACT FINITE/ABEL LEMMA — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-90217` (the exact factor-64 signed reward)  
Scope: uniform-Pascal reward geometry; no proof that the critical arithmetic occupation is nonincreasing and no RH conclusion

## 1. Setup

Let \(d_{64}(m)\) be the exact reward of `L-90217`. Thus

\[
d_{64}(m)<0\iff 13\le m\le63,
\]

while \(d_{64}(m)>0\) for \(2\le m\le12\) and every \(m\ge64\), and

\[
d_{64}(m)=\frac{39(\sqrt2-1)}{m(m-1)}
\qquad(m\ge64).
\tag{L-90701.1}
\]

Put

\[
D(M)=\sum_{m=2}^{M}d_{64}(m).
\tag{L-90701.2}
\]

The point of this note is that the signed reward has a much stronger property than mere positivity of its total mass: **every prefix is uniformly positive**.

## 2. Uniform prefix positivity

### Theorem 2.1

For every integer \(M\ge2\),

\[
\boxed{\frac9{10}<D(M)<\frac{21}{10}.}
\tag{L-90701.3}
\]

In particular the factor-64 reward lies in the dual cone of all nonnegative nonincreasing occupations.

### Proof

The sign classification from `L-90217` implies that \(D(M)\) increases on \(2\le M\le12\), decreases on \(13\le M\le63\), and increases again for \(M\ge64\). It is therefore enough to control \(D(2),D(12),D(63)\), and the infinite tail.

First,

\[
D(2)=d_{64}(2)=\frac58+\frac{\sqrt2}{4}>\frac9{10},
\tag{L-90701.4}
\]

using \(\sqrt2>7/5\).

Exact summation on the four finite sign blocks gives

\[
\begin{aligned}
\sum_{m=2}^{12}d_{64}(m)
  &=\frac{4313}{1760}-\frac{319}{1120}\sqrt2>2,\\
\sum_{m=13}^{15}d_{64}(m)
  &=\frac{53}{546}-\frac1{12}\sqrt2>-\frac1{40},\\
\sum_{m=16}^{31}d_{64}(m)
  &=\frac{849728754059}{10314539492400}
    -\frac{8066209431179}{27505438646400}\sqrt2>-\frac13,\\
\sum_{m=32}^{63}d_{64}(m)
  &=-\frac{416}{651}
    -\frac{50519225495478448442768729}
           {1182266884102822267511361600}\sqrt2>-\frac7{10}.
\end{aligned}
\tag{L-90701.5}
\]

All four inequalities follow from the rational enclosure

\[
\frac{707}{500}<\sqrt2<\frac{283}{200},
\tag{L-90701.6}
\]

whose two sides square respectively below and above \(2\). Consequently

\[
D(63)>2-\frac1{40}-\frac13-\frac7{10}
=\frac{113}{120}>\frac9{10}.
\tag{L-90701.7}
\]

This proves the lower bound in (L-90701.3).

For the upper bound, \(D(M)\le D(12)\) on \(M\le63\), and (L-90701.5), together with \(\sqrt2>7/5\), gives \(D(12)<21/10\). For \(M\ge64\),

\[
D(M)\le D(63)+39(\sqrt2-1)\sum_{m=64}^{\infty}\frac1{m(m-1)}
=D(63)+\frac{39(\sqrt2-1)}{63}.
\tag{L-90701.8}
\]

The exact value of \(D(63)\), bounded using \(\sqrt2>707/500\), is \(<1\); the final term in (L-90701.8), bounded using \(\sqrt2<283/200\), is \(<0.257\). Hence the right side is \(<21/10\). This proves (L-90701.3). ∎

The large rational coefficients in (L-90701.5) are only finite harmonic sums of the affine block formula

\[
m(m-1)d_{64}(m)=A_j+(m+1-2^{j+1})S_j
\qquad(2^j\le m<2^{j+1});
\tag{L-90701.9}
\]

the retained verifier reconstructs them from the short \(\mathbb Q(\sqrt2)\) data of `L-90217` rather than treating them as inputs.

## 3. Monotone-occupation payment

Let \(M(m)\ge0\) be finitely supported and nonincreasing. Set \(M(m)=0\) past its support. Finite Abel summation gives

\[
\sum_{m\ge2}d_{64}(m)M(m)
=
\sum_{m\ge2}D(m)\,[M(m)-M(m+1)].
\tag{L-90701.10}
\]

Every bracket is nonnegative. Therefore Theorem 2.1 yields the quantitative payment

\[
\boxed{
\sum_{m\ge2}d_{64}(m)M(m)
\ge\frac9{10}M(2).
}
\tag{L-90701.11}
\]

In particular the complete negative block \(13,\ldots,63\) is automatically paid by the low rows and positive reciprocal-square tail for every nonincreasing occupation.

This is stronger than the original 51-state target `L-90217.25`, but under an additional structural hypothesis on the occupation.

## 4. A stable nonmonotone defect bound

For an arbitrary finitely supported nonnegative occupation define its total upward variation

\[
V_+(M)=\sum_{m\ge2}[M(m+1)-M(m)]_+.
\tag{L-90701.12}
\]

Writing \(\Delta_m=M(m)-M(m+1)\), the total positive variation is \(M(2)+V_+(M)\), while the total negative variation is \(V_+(M)\). From (L-90701.3),

\[
\begin{aligned}
\sum_{m\ge2}d_{64}(m)M(m)
&=\sum_{m\ge2}D(m)\Delta_m\\
&\ge\frac9{10}\,[M(2)+V_+(M)]
-\frac{21}{10}V_+(M).
\end{aligned}
\]

Thus

\[
\boxed{
\sum_{m\ge2}d_{64}(m)M(m)
\ge\frac9{10}M(2)-\frac65V_+(M).
}
\tag{L-90701.13}
\]

A sufficient payment condition is therefore

\[
\boxed{V_+(M)\le\frac34M(2).}
\tag{L-90701.14}
\]

The original factor-64/Pascal bridge has consequently been reduced from a 51-coordinate signed comparison to one scalar **upward-variation bound** for the critical uniform-Pascal Green occupation.

## 5. Consequence for the live route

The result separates the remaining work cleanly:

```text
factor-64 reward algebra                       exact
all reward prefixes uniformly positive         proved here
every nonincreasing occupation pays the debt   proved here
bounded upward variation pays the debt         proved here
critical arithmetic occupation variation       open / RH-bearing
factor-64 sign and RH                           unproved
```

A continuation should estimate \(V_+(M)\) directly from the explicit Green formula

\[
M_n=s_n+\frac2{n+1}\sum_{m>n}s_m,
\]

rather than return to the 51 individual states.
