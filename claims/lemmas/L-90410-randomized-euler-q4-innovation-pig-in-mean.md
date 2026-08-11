# L-90410 — The randomized Euler Q4 innovation satisfies PIG in mean

Claim ID: `L-90410`  
Title: Randomizing the squarefree Euler signs makes the complete compact-Q4 innovation orthogonal and gives a uniform quadratic block bound  
Status: **PROPOSED COMPLETE EXACT RANDOM-MODEL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: PR #362 compact innovation notation; elementary Rademacher orthogonality  
Scope: randomized Euler model only; no deterministic Möbius comparison, PIG, or RH conclusion

## 1. Random squarefree Euler source

Let \((\varepsilon_p)_p\) be independent Rademacher signs and, for squarefree \(s\), put

\[
\varepsilon(s)=\prod_{p\mid s}\varepsilon_p,
\qquad
r_\varepsilon(s)=\mu^2(s)\varepsilon(s).
\]

Define the randomized analogues of the compact and Q4 sources by

\[
b_{\circ,\varepsilon}
=(\epsilon-4\delta_4)*r_\varepsilon,
\]

\[
b_{4,\varepsilon}
=r_\varepsilon-3\sum_{a\ge1}\delta_{4^a}*r_\varepsilon,
\]

\[
q_{\circ,\varepsilon}(m)
=-b_{\circ,\varepsilon}(m)\log m,
\]

and

\[
\boxed{
i_{\circ,\varepsilon}
=q_{\circ,\varepsilon}
-(\log4)\,\delta_4*b_{4,\varepsilon}.
}
\tag{L-90410.1}
\]

The deterministic Möbius innovation is recovered at the single sign point
\(\varepsilon_p=-1\) for every prime.

## 2. Exact four-adic fibers

Every integer in the support has a unique form

\[
m=4^a s,
\qquad a\ge0,\qquad 4\nmid s,\qquad \mu^2(s)=1.
\]

Direct substitution in (L-90410.1) gives

\[
\boxed{
i_{\circ,\varepsilon}(s)
=-\varepsilon(s)\log s,
}
\tag{L-90410.2}
\]

\[
\boxed{
i_{\circ,\varepsilon}(4s)
=\varepsilon(s)\bigl(4\log s+3\log4\bigr),
}
\tag{L-90410.3}
\]

and, for every \(a\ge2\),

\[
\boxed{
i_{\circ,\varepsilon}(4^as)
=3(\log4)\varepsilon(s).
}
\tag{L-90410.4}
\]

For the actual Möbius source these are the same formulas with
\(\varepsilon(s)=\mu(s)\).

## 3. Orthogonal squarefree decomposition of every carry row

For an integer parent \(N\), child \(J\), and divisor \(d\), write

\[
\chi_{N,d}(J)
=
\left\lfloor\frac Nd\right\rfloor
-\left\lfloor\frac Jd\right\rfloor
-\left\lfloor\frac{N-J}{d}\right\rfloor
\in\{0,1\}.
\]

Define

\[
\mathcal L_{N,J}(f)
=\sum_{d\le N}f(d)\chi_{N,d}(J).
\]

For each squarefree \(s\) with \(4\nmid s\), put

\[
\begin{aligned}
A_s(N,J)
={}&-(\log s)\chi_{N,s}(J)\\
&+\bigl(4\log s+3\log4\bigr)\chi_{N,4s}(J)\\
&+3(\log4)\sum_{\substack{a\ge2\\4^as\le N}}
\chi_{N,4^as}(J).
\end{aligned}
\tag{L-90410.5}
\]

Equations (L-90410.2)--(L-90410.4) give the exact Walsh expansion

\[
\boxed{
\mathcal L_{N,J}(i_{\circ,\varepsilon})
=
\sum_{\substack{s\le N\\4\nmid s\\\mu^2(s)=1}}
\varepsilon(s)A_s(N,J).
}
\tag{L-90410.6}
\]

For distinct squarefree \(s,t\),

\[
\mathbb E[\varepsilon(s)\varepsilon(t)]=0,
\]

because \(s\triangle t\) contains a prime occurring to odd exponent. Therefore

\[
\boxed{
\mathbb E_\varepsilon
\left|\mathcal L_{N,J}(i_{\circ,\varepsilon})\right|^2
=
\sum_{\substack{s\le N\\4\nmid s\\\mu^2(s)=1}}
|A_s(N,J)|^2.
}
\tag{L-90410.7}
\]

This is exact; no large sieve, asymptotic independence, or averaging over the
carry position is used.

## 4. Uniform quadratic bound

Since every carry indicator is at most one,

\[
\begin{aligned}
|A_s(N,J)|
&\le
5\log s
+3\log4\left(1+\left\lfloor\log_4\frac Ns\right\rfloor\right)\\
&\le 12\log(2N)
\end{aligned}
\tag{L-90410.8}
\]

for \(N\ge2\). There are at most \(N\) admissible squarefree cores. Hence

\[
\boxed{
\mathbb E_\varepsilon
\left|\mathcal L_{N,J}(i_{\circ,\varepsilon})\right|^2
\le
144\,N\log^2(2N).
}
\tag{L-90410.9}
\]

Consequently, for any set \(\mathcal J_N\subseteq\{0,\ldots,N\}\),

\[
\boxed{
\mathbb E_\varepsilon
\left[
\frac1{N^2}
\sum_{J\in\mathcal J_N}
\left|\mathcal L_{N,J}(i_{\circ,\varepsilon})\right|^2
\right]
\le
288\log^2(2N).
}
\tag{L-90410.10}
\]

If logarithmic endpoint weights \(\ell_N\asymp N^{-1}\) are summed over one
block \(e^J\le N<e^{J+1}\), their total mass is \(O(1)\), and therefore

\[
\boxed{
\mathbb E_\varepsilon\mathcal I_\varepsilon(J)
\ll (1+J)^2
}
\tag{L-90410.11}
\]

for every positive PIG-type block measure dominated by the complete row grid.

## 5. Exact scope

The theorem proves that the compact-Q4 PIG mechanism is automatic after
independent randomization of the prime signs.

It does **not** compare the deterministic point
\(\varepsilon_p=-1\) with the random mean. Such a comparison would need a
global phase-locked inequality for the complete multiplicative Gram. Individual
prime flips need not move the energy monotonically, and (L-90410.11) cannot be
specialized to the Möbius point.

Thus

```text
randomized Euler PIG in expectation       proved here;
deterministic Möbius PIG                  open / RH-bearing;
RH                                        unproved.
```
