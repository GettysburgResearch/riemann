# L-92205 — The order-three Xi Loewner–Hankel matrix is positive above five million

Claim ID: `L-92205`  
Status: **PROPOSED COMPLETE EVENTUAL THEOREM — HOSTILE REVIEW REQUIRED**  
Created: 2026-08-14  
Depends on: `L-92204`; Platt–Trudgian verified height; explicit zero-count bounds  
RH status: **unproved**

## 1. Normalised third-order moment matrix

Put

\[
 t=x^2,
 \qquad
 A_k(t)=\frac{(-1)^k}{k!}p^{(k)}(t),
\]

and

\[
 H_3(t)=
 \begin{pmatrix}
 A_1&A_2&A_3\\
 A_2&A_3&A_4\\
 A_3&A_4&A_5
 \end{pmatrix}.
\]

Let

\[
 D_x=\operatorname{diag}(x^2,x^4,x^6).
\]

For a squared-pole parameter `s`, define

\[
 q_x(s)=\frac{x^2}{x^2+s},
 \qquad
 v(q)=(q,q^2,q^3)^T.
\]

Then

\[
 \boxed{
 D_xH_3(x^2)D_x
 =\sum_\alpha w_\alpha
   v(q_x(s_\alpha))v(q_x(s_\alpha))^T.
 }
\tag{L-92205.1}
\]

For an off-line conjugate pair `s=c+id`, `bar s=c-id`, replace it temporarily
by two copies of its real projection `c`.  This gives a positive projected
matrix `P_x`.  Write

\[
 D_xH_3D_x=P_x+E_x.
\]

## 2. Uniform three-band frame

Use the three height intervals

\[
 I_1=[x,1.1x],
 \qquad
 I_2=[1.4x,1.5x],
 \qquad
 I_3=[1.9x,2x].
\]

For `x>=5·10^6`, the explicit Riemann–von Mangoldt bounds give

\[
 \boxed{
 N(I_j)\ge\frac{x\log x}{100}
 \qquad(j=1,2,3).
 }
\tag{L-92205.2}

If `2x<=H`, every zero in these intervals is verified simple and critical.
If `2x>H`, use instead the real projections of all zeros; the total projected
pole weight in `I_j` is exactly twice `N(I_j)`.

For any projected poles selected one from each interval, their `q`-coordinates
lie respectively in

\[
 [0.45,0.51],
 \qquad
 [0.30,0.35],
 \qquad
 [0.19,0.23].
\]

The `3x3` matrix with columns `v(q_1),v(q_2),v(q_3)` has

\[
 |\det V|
 =q_1q_2q_3
  |q_1-q_2||q_1-q_3||q_2-q_3|
 >3.9\cdot10^{-5}
\]

and `||V||_F^2<1.1`.  Therefore

\[
 \sigma_{\min}(V)^2>4\cdot10^{-9}.
\]

Partitioning the available pole weight into triples gives

\[
\boxed{
 \lambda_{\min}(P_x)
 \ge4\cdot10^{-11}x\log x.
 }
\tag{L-92205.3
}

## 3. Quadratic depth perturbation

For one possible off-line pair put

\[
 q=\frac{q_0}{1+i\varepsilon},
 \qquad
 q_0=\frac{x^2}{x^2+c},
 \qquad
 \varepsilon=\frac d{x^2+c}.
\]

Since `|d|<=b` and `c>=b^2-1/4`,

\[
 |\varepsilon|
 \le\frac1{2\sqrt{x^2-1/4}}.
\]

For the powers `2<=k<=6`, conjugation cancels the linear term and

\[
 \left|
 \Re(1+i\varepsilon)^{-k}-1
 \right|
 \le22\varepsilon^2.
\]

It follows that the pair perturbation obeys

\[
 \|E_{x,\mathrm{pair}}\|
 \le132w\varepsilon^2q_0^2.
\]

The explicit zero-count bound and unit-interval summation give

\[
 \sum_{\rho:\gamma>0}
 m_\rho
 \left(
 \frac{x^2}{x^2+\gamma^2-1/4}
 \right)^2
 \le20x\log(x+3).
\]

Hence, when `x>=H/2`,

\[
\boxed{
 \|E_x\|
 \le700\frac{\log(x+3)}x.
 }
\tag{L-92205.4
}
\]

When `5·10^6<=x<H/2`, every zero below `H` is already real and only the tail
`gamma>H` contributes to `E_x`; the stronger estimate

\[
\boxed{
 \|E_x\|
 \le C\frac{x^4\log H}{H^5}
 }
\tag{L-92205.5
}
\]

holds with an effective absolute `C<10^4`.

Both bounds are far below the frame moat (L-92205.3).  At the only critical
endpoint `x=H/2`, the ratio between the lower frame bound and the perturbation
bound exceeds `10^11`; it improves in both directions.

Therefore

\[
\boxed{
 H_3(x^2)\succ0
 \qquad(x\ge5\cdot10^6).
 }
\tag{L-92205.6
}

By the reciprocal congruence `L-92204`, the confluent third-order Loewner
matrix of the Xi impedance is positive on the same range.

## 4. Review joints

1. the explicit lower count in each of the three moving intervals;
2. the conversion from ordinary zero multiplicity to projected pole weight;
3. the uniform Vandermonde/frame constant;
4. the quadratic conjugate-pair perturbation bound;
5. the global unit-interval summation in (L-92205.4);
6. the verified-tail estimate in (L-92205.5);
7. normal convergence of the scaled matrix series.

## 5. Boundary

```text
order-three local Loewner matrix above 5e6       PROPOSED POSITIVE
compact interval (1/2,5e6)                       OPEN / DIRECTED
matrix monotonicity of order three               CONDITIONAL ON COMPACT SIGN
matrix monotonicity of all orders                OPEN / RH-EQUIVALENT
Riemann Hypothesis                               UNPROVED
```
