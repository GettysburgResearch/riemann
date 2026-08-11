# L-90605 — Third-order Brownian truncation and the all-fixed-order expansion

Claim ID: `L-90605`  
Status: **PROPOSED COMPLETE LOCAL ASYMPTOTIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: the serial-gamma representation and first-order formula of PR #376 (`L-90602`)  
RH status: **unproved**

## 1. Setting

Let

\[
 S_N=\sum_{n\le N}\frac{X_n}{n^2},
 \qquad
 S_\infty=S_N+R_N,
 \qquad
 R_N=\sum_{n>N}\frac{X_n}{n^2},
\tag{L-90605.1}
\]

where the \(X_n\) are independent Gamma variables of shape \(2\) and scale \(1\).  Write

\[
 F_N(u)=\mathbb E[S_N^u],
 \qquad
 m_N(s)=\pi^{-s/2}F_N(s/2).
\tag{L-90605.2}
\]

The infinite law satisfies

\[
 \pi^{-s/2}F_\infty(s/2)=2\xi(s).
\tag{L-90605.3}
\]

## 2. Exact binomial-convolution inverse

Put

\[
 \mu_j(N)=\mathbb E[R_N^j],
 \qquad
 M_N(t)=\sum_{j\ge0}\mu_j(N)\frac{t^j}{j!},
\]

and define \(\nu_j(N)\) by

\[
 \frac1{M_N(t)}=\sum_{j\ge0}\nu_j(N)\frac{t^j}{j!}.
\tag{L-90605.4}
\]

Independence and the generalized binomial theorem give

\[
 F_\infty(u)=\sum_{j\ge0}\binom uj\mu_j(N)F_N(u-j).
\tag{L-90605.5}
\]

Binomial-convolution inversion therefore yields, to every fixed order \(J\),

\[
 \boxed{
 F_N(u)=\sum_{j=0}^J\binom uj\nu_j(N)F_\infty(u-j)
 +O_{K,J}(N^{-J-1})
 }
\tag{L-90605.6}
\]

uniformly for \(u\) in a fixed compact set \(K\).  The coefficients are completely algorithmic.  The cumulants of the tail are

\[
 \kappa_r(R_N)=2(r-1)!\sum_{n>N}n^{-2r},
\tag{L-90605.7}
\]

so \(\mu_j\), then \(\nu_j\), are obtained from complete Bell polynomials and Euler--Maclaurin expansions.

The first inverse coefficients are

\[
 \nu_1=-\mu_1,
 \qquad
 \nu_2=2\mu_1^2-\mu_2,
 \qquad
 \nu_3=-6\mu_1^3+6\mu_1\mu_2-\mu_3.
\tag{L-90605.8}
\]

## 3. Tail moments through order three

Euler--Maclaurin and the Gamma moments give

\[
 \begin{aligned}
 \mu_1&=\frac2N-\frac1{N^2}+\frac1{3N^3}+O(N^{-5}),\\
 \mu_2&=\frac4{N^2}-\frac{10}{3N^3}+O(N^{-4}),\\
 \mu_3&=\frac8{N^3}+O(N^{-4}).
 \end{aligned}
\tag{L-90605.9}
\]

Hence

\[
 \mu_1^2-\frac{\mu_2}{2}
 =\frac2{N^2}-\frac7{3N^3}+O(N^{-4}),
\tag{L-90605.10}
\]

and

\[
 -\mu_1^3+\mu_1\mu_2-\frac{\mu_3}{6}
 =-\frac4{3N^3}+O(N^{-4}).
\tag{L-90605.11}
\]

## 4. Third-order xi expansion

Using

\[
 \pi^{-s/2}F_\infty(s/2-j)
 =2\pi^{-j}\xi(s-2j),
\]

one obtains uniformly on compact subsets of \(\mathbb C\):

\[
 \boxed{
 \begin{aligned}
 m_N(s)={}&2\xi(s)
 -\frac{2s}{\pi N}\xi(s-2)\\
 &+\frac1{N^2}\left[
 \frac{s}{\pi}\xi(s-2)
 +\frac{s(s-2)}{\pi^2}\xi(s-4)
 \right]\\
 &+\frac1{N^3}\left[
 -\frac{s}{3\pi}\xi(s-2)
 -\frac{7s(s-2)}{6\pi^2}\xi(s-4)
 -\frac{s(s-2)(s-4)}{3\pi^3}\xi(s-6)
 \right]\\
 &+O_K(N^{-4}).
 \end{aligned}}
\tag{L-90605.12}
\]

This extends PR #376's first-order formula by two complete orders.

## 5. One-sided Dirichlet numerator

Let

\[
 A(s)=\pi^{-s/2}\Gamma(1+s/2),
 \qquad
 D_N(s)=\frac{m_N(s)}{A(s)}.
\]

Using the gamma recursion, (L-90605.12) becomes

\[
 \boxed{
 \begin{aligned}
 D_N(s)={}&2(s-1)\zeta(s)
 -\frac4N(s-3)\zeta(s-2)\\
 &+\frac1{N^2}\big[2(s-3)\zeta(s-2)+4(s-5)\zeta(s-4)\big]\\
 &+\frac1{N^3}\bigg[
 -\frac23(s-3)\zeta(s-2)
 -\frac{14}{3}(s-5)\zeta(s-4)
 -\frac83(s-7)\zeta(s-6)
 \bigg]\\
 &+O_K(N^{-4}).
 \end{aligned}}
\tag{L-90605.13}
\]

This is an explicit finite shifted-zeta normal form for every fixed compact-height calculation.

## 6. Fixed simple-zero jet

Let \(\rho\) be a fixed simple zero of \(\xi\), and write the nearby zero as

\[
 s_N=\rho+\frac{a_\rho}{N}+\frac{b_\rho}{N^2}+O_\rho(N^{-3}).
\]

Put

\[
 E_1(s)=-\frac{2s}{\pi}\xi(s-2),
 \qquad
 E_2(s)=\frac{s}{\pi}\xi(s-2)
 +\frac{s(s-2)}{\pi^2}\xi(s-4).
\]

Then

\[
 \boxed{
 a_\rho=\frac{\rho\,\xi(\rho-2)}{\pi\xi'(\rho)},
 }
\tag{L-90605.14}
\]

and

\[
 \boxed{
 b_\rho=-\frac{
 \xi''(\rho)a_\rho^2+E_1'(\rho)a_\rho+E_2(\rho)
 }{2\xi'(\rho)}.
 }
\tag{L-90605.15}
\]

Higher jets follow recursively from (L-90605.6).

## 7. Scope

The expansion is a **fixed-height** theorem.  Its constants deteriorate when the compact set grows, and it does not contradict PR #376's Bohr-instability theorem, whose unwanted zeros escape to infinite imaginary height for each fixed \(N\).

The durable Brownian frontier is therefore:

```text
all fixed orders on compact height ranges       algorithmically available;
height-dependent diagonal N=N(T)                still live;
global finite-N half-plane stability            refuted;
Riemann Hypothesis                               unproved.
```
