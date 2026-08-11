# L-91028 — The normalized sixteenfold Cauchy recurrence holds unconditionally at every sufficiently large scale

Claim ID: `L-91028`  
Status: **PROPOSED COMPLETE UNCONDITIONAL TERMINAL-RECURRENCE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91021`; the definition of `E_x(a)` in `T-91005`  
RH status: **unproved**

## 1. The recurrence residual

Recall

\[
 \mathcal E_x(a)=a^{-4}[\mathcal N_x(2a)-\mathcal N_x(a)].
\]

Then

\[
 \boxed{
 a^4[\mathcal E_x(a)-\mathcal E_x(2a)]
 =-\mathcal N_x(a)+\frac{17}{16}\mathcal N_x(2a)
  -\frac1{16}\mathcal N_x(4a).
 }
 \tag{L-91028.1}
\]

This is the completed scalar attached to the residual kernel of `L-91022`.

## 2. Uniform asymptotic

For `c in {1,2,4}`, put

\[
 w_c=ca+\frac12+ix,
 \qquad R_c=|w_c|.
\]

The uniform expansion of `L-91021` gives

\[
 \mathcal N_x(ca)
 =\frac{ca}{4}\log\frac{R_c}{2\pi}
 -\frac{c^2a^2}{4}\Re\frac1{w_c}+O(1),
 \tag{L-91028.2}
\]

where the error is absolute, uniformly in `a>=1`, `x in R` and the three fixed
values of `c`.

Substitution into (L-91028.1) gives

\[
\begin{aligned}
 a^4[\mathcal E_x(a)-\mathcal E_x(2a)]
 ={}&\frac a4\left[
 -\log\frac{R_1}{2\pi}
 +\frac{17}{8}\log\frac{R_2}{2\pi}
 -\frac14\log\frac{R_4}{2\pi}
 \right]\\
 &+\frac{a^2}{4}\left[
 \Re\frac1{w_1}
 -\frac{17}{4}\Re\frac1{w_2}
 +\Re\frac1{w_4}
 \right]+O(1).
\end{aligned}
 \tag{L-91028.3}
\]

## 3. Positive logarithmic leading term

Let

\[
 R=\sqrt{a^2+x^2}.
\]

For `c in {1,2,4}`,

\[
 \log R_c=\log R+O(1)
 \tag{L-91028.4}
\]

uniformly in `a>=1,x`.  Since

\[
 -1+\frac{17}{8}-\frac14=\frac78,
 \tag{L-91028.5}
\]

the logarithmic line of (L-91028.3) is

\[
 \frac{7a}{32}\log\frac{R}{2\pi}+O(a).
 \tag{L-91028.6}
\]

Every reciprocal term in (L-91028.3) is `O(a)`, uniformly, because

\[
 a^2\left|\Re\frac1{ca+1/2+ix}\right|\ll a.
\]

Therefore

\[
 \boxed{
 a^4[\mathcal E_x(a)-\mathcal E_x(2a)]
 =\frac{7a}{32}\log(2+a+|x|)+O(a)
 }
 \tag{L-91028.7}
\]

uniformly in `a>=1` and real `x`.

## 4. Terminal recurrence

There exists an effective absolute `A_1` such that

\[
 \boxed{
 \mathcal E_x(a)-\mathcal E_x(2a)>0
 \qquad(a>=A_1,\ x\in\mathbb R).
 }
 \tag{L-91028.8}
\]

This is stronger than the terminal gate in `L-91021`: it proves the exact
coefficient-one recurrence residual positive in the same carrier state.

## 5. Consequence for the full proposal

To prove RH through `T-91005`, it is now enough to prove the recurrence on the
bounded scale interval

\[
 0<a<A_1.
\]

Equivalently, one may prove the scale-doubling step only until the first iterate
reaches `A_1`; every later step is unconditional.

This does not make the problem finite-dimensional because the carrier `x`
remains unbounded and the scale approaches zero.  It does remove every terminal
or high-scale asymptotic obligation from the source/scattering intertwiner.

## 6. Boundary

Closed:

```text
uniform asymptotic for the exact recurrence residual;
positive 7/32 logarithmic leading coefficient;
unconditional same-carrier terminal recurrence;
reduction of production work to bounded scales.
```

Open:

```text
subterminal prime-side residual positivity;
cofinal small-scale source/scattering theorem;
RH.
```
