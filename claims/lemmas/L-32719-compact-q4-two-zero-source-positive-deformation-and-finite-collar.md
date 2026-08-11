# L-32719 — A compact Q=4 two-zero source has positive inverse/deformation and no interior bare-source boundary

Claim ID: `L-32719`  
Title: Multiplying the Q=4 Euler–Blaschke source by the missing local zero produces a finite three-tap inverse source, positive inverse and finite Jordan deformation, a uniformly zero-safe critical multiplier, and a bare carry field supported only on a fixed endpoint collar  
Status: **PROPOSED COMPLETE EXACT SOURCE/FILTER THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: elementary Euler products and carry/divisor switching  
Scope: exact compact source, positivity, pole preservation, and cofinal reserve interface; no subexponential current bound or RH conclusion

## 1. Definition

Put

\[
 \boxed{
 B_\square(s)
 =\frac{(1-4^{-s})(1-4^{1-s})}{\zeta(s)},
 \qquad
 A_\square(s)=B_\square(s)^{-1}.
 }
 \tag{L-32719.1}
\]

Let

\[
 x=4^{-s}.
\]

The local numerator is

\[
 p(x)=(1-x)(1-4x)=1-5x+4x^2.
 \tag{L-32719.2}
\]

At coefficient level,

\[
 \boxed{
 b_\square
 =(\varepsilon-\delta_4)
  *(\varepsilon-4\delta_4)*\mu.
 }
 \tag{L-32719.3}
\]

## 2. Positive inverse and generalized primes

The inverse is

\[
 A_\square(s)
 =\frac{\zeta(s)}{(1-4^{-s})(1-4^{1-s})}.
 \tag{L-32719.4}
\]

Every Euler factor has a power-series expansion with nonnegative coefficients. Hence

\[
 \boxed{a_\square(n)>0\qquad(n\ge1).}
 \tag{L-32719.5}
\]

Its generalized von Mangoldt sequence is

\[
 \boxed{
 \Lambda_\square(n)
 =\Lambda(n)
 +(\log4)\sum_{r\ge1}(1+4^r)
  \mathbf1_{n=4^r}
 \ge0.
 }
 \tag{L-32719.6}
\]

The complete Selberg sequence

\[
 C_\square
 =\Lambda_\square\log
  +\Lambda_\square*\Lambda_\square
 \tag{L-32719.7}
\]

is therefore coefficientwise nonnegative.

## 3. Positive finite Jordan deformation

For real `tau>=0`, define

\[
 J_{\square,\tau}(s)
 ={A_\square(s-\tau)\over A_\square(s)}.
 \tag{L-32719.8}
\]

At an odd prime the local factor is

\[
 {1-p^{-s}\over1-p^{\tau-s}},
\]

which has nonnegative coefficients.

At the prime two, put

\[
 y=2^{-s},
 \qquad b=2^\tau\ge1,
 \qquad x=y^2.
\]

The local ratio factors as

\[
 \boxed{
 {1-y\over1-by}
 {1-x\over1-b^2x}
 {1-4x\over1-4b^2x}.
 }
 \tag{L-32719.9}
\]

Each factor has the form

\[
 {1-cz\over1-caz}
 =1+\sum_{m\ge1}(a-1)c^m a^{m-1}z^m
\]

with `a>=1` and `c>0`. Thus every coefficient is nonnegative, and multiplication preserves positivity. Therefore

\[
 \boxed{
 J_{\square,\tau}(n)\ge0
 \qquad(n\ge1,\ \tau\ge0).
 }
 \tag{L-32719.10}
\]

For `tau>0`, every coefficient permitted by the Euler factors is strictly positive.

## 4. The bare inverse-source carry field is compact

Because

\[
 \mathbf1*b_\square
 =\varepsilon-5\delta_4+4\delta_{16},
 \tag{L-32719.11}
\]

the divisor prefix is

\[
 D_\square(X)
 =\sum_{d\le X}b_\square(d)
   \left\lfloor{X\over d}\right\rfloor
 =\sum_{m\le X}(\mathbf1*b_\square)(m).
\]

Hence

\[
 \boxed{
 D_\square(X)=
 \begin{cases}
 0,&0\le X<1,\\
 1,&1\le X<4,\\
 -4,&4\le X<16,\\
 0,&X\ge16.
 \end{cases}}
 \tag{L-32719.12}
\]

For a split `n=j+k`, the bare source charge is

\[
 Y_\square(n,j)
 =D_\square(n)-D_\square(j)-D_\square(k).
 \tag{L-32719.13}
\]

Consequently

\[
 \boxed{
 n,j,k\ge16
 \quad\Longrightarrow\quad
 Y_\square(n,j)=0.
 }
 \tag{L-32719.14}
\]

Every nonzero bare-source row belongs to a fixed endpoint collar independent of parent scale.

## 5. Critical multiplier is uniformly zero-safe

On the critical line, `|x|=1/2`. Directly,

\[
 |1-4x|=2|1-x|,
\]

so

\[
 \boxed{
 |p(x)|=2|1-x|^2.
 }
 \tag{L-32719.15}
\]

Since `|x|=1/2`,

\[
 \boxed{
 \frac12\le|p(x)|\le\frac92.
 }
 \tag{L-32719.16}
\]

Thus the compact source is uniformly equivalent to the ordinary inverse-zeta source on the complete critical line.

The zeros of `p(4^{-s})` lie only on `Re(s)=0` and `Re(s)=1`. Therefore every nontrivial zeta-zero pole in the open strip survives.

## 6. True pole current and exact finite collar

Let

\[
 L_\square=-{A_\square'\over A_\square},
 \qquad
 q_\square=b_\square*\Lambda_\square=-b_\square\log.
 \tag{L-32719.17}
\]

Its physical carry multiplier is

\[
 \zeta(s)B_\square(s)L_\square(s)N_\theta(s)
 =p(4^{-s})L_\square(s)N_\theta(s).
 \tag{L-32719.18}
\]

At every nontrivial zero `rho`, the residue is nonzero because `p(4^{-rho})` is nonzero and `N_theta(rho)` is nonzero as a carry-position vector.

The bare source term in the source-convolved reflected identity vanishes identically on every row with both children and parent at least sixteen. Thus all individual source terms outside that fixed collar have no unweighted factor.

## 7. Cofinal Kummer reserve

Define

\[
 P_\square(n,j)=\mathcal L_{n,j}(\Lambda_\square),
 \quad
 S_\square(n,j)=\mathcal L_{n,j}(C_\square),
 \quad
 R_\square=P_\square^2-S_\square.
\]

On every fixed balanced cone,

\[
 P_\square(n,j)
 \ge\log\binom nj\gg n.
 \tag{L-32719.19}
\]

The generalized-prime prefix satisfies

\[
 \sum_{m\le x}\Lambda_\square(m)\ll x,
\]

because the added four-adic tower is geometric. Consequently

\[
 S_\square(n,j)\ll n\log n.
 \tag{L-32719.20}
\]

Therefore

\[
 \boxed{
 R_\square(n,j)
 =(1-o(1))P_\square(n,j)^2>0
 }
 \tag{L-32719.21}
\]

uniformly on every fixed balanced cone.

The true physical current also has vanishing relative reserve cost by the classical PNT: the linear density in the finite source prefix cancels because

\[
 1-\frac54+\frac4{16}=0.
\]

This is a cofinal interface, not an RH-scale estimate.

## 8. What this changes

The compact source removes two bookkeeping problems at once:

```text
unweighted source boundary:
    exactly zero away from a fixed endpoint collar;

local neutral state:
    replaced by one finite two-zero multiplier
    uniformly bounded above and below on the critical line.
```

The remaining theorem is now purely the signed Hermitian estimate for the true compact-source current. It cannot be replaced by the deterministic generalized-prime second difference; the source-typing correction of `R-32707` continues to apply.

## 9. Proof boundary

Closed exactly or cofinally here:

1. positive inverse and generalized-prime coefficients;
2. coefficientwise-positive finite Jordan deformation;
3. finite three-tap inverse source;
4. fixed compact bare-source collar;
5. uniform critical-line frame bounds;
6. retention of every open-strip zeta pole;
7. cofinal balanced Kummer reserve and current/reserve interface.

Still open:

1. a source-complete Hermitian inequality for the compact current;
2. a subexponential physical energy bound;
3. RH.
