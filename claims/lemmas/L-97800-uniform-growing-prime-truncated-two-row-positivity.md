# L-97800 — Uniform growing-prime positivity for the literal truncated rows

Claim ID: `L-97800`  
Status: **PROVED UNCONDITIONAL UNIFORM TAIL THEOREM**  
Created: 2026-08-18  
Frozen source: PR #579 at `9f56688236d33c515a92032c640888488c06ed6e`  
RH status: **not assumed**

## 1. Literal dictionaries and finite Euler projection

For the two conclusion-producing rows retain the exact integer dictionaries

\[
 q_2(n)=
 \begin{cases}
 0,&n<2,\\
 3,&n=2,\\
 0,&n=3,\\
 1,&n\ge4,
 \end{cases}
\]

and

\[
 q_3^\sharp(n)=
 \begin{cases}
 0,&n<3,\\
 6,&n=3,\\
 -2,&n=4,\\
 1,&n\ge5.
 \end{cases}
\]

The physical row three is one third of the sharp row. Let `j=2` denote `q_2`, and let `j=3` denote `q_3^sharp`. Set

\[
 Q_2=3,\qquad Q_3=6.
\]

For real `z>=5`, put

\[
 P_z=\prod_{3<p\le z}p,
 \quad
 \omega_z=\#\{p:3<p\le z\},
 \quad
 V_z={\varphi(P_z)\over P_z}=\prod_{3<p\le z}\left(1-{1\over p}\right),
\]

\[
 A_z=\prod_{3<p\le z}\left(1+{1\over p}\right),
 \qquad
 R_z={A_z\over V_z}
 =\prod_{3<p\le z}{p+1\over p-1}.
\]

Define the literal finite Euler projection

\[
 a_{j,z}(n)=\sum_{d\mid(n,P_z)}\mu(d)q_j(n/d),
\tag{L-97800.1}
\]

its prefix derivative

\[
 A_{j,z}(N)=\sum_{n\le N}{a_{j,z}(n)\over\sqrt n},
\tag{L-97800.2}
\]

and its all-real Riesz row

\[
 C_{j,z}(X)=\sum_{n\le X}{a_{j,z}(n)\over\sqrt n}\log {X\over n}.
\tag{L-97800.3}
\]

No activation boundary is smoothed: the summands in (L-97800.2)--(L-97800.3) are the actual row coordinates.

## 2. Exact terminalization and a uniform prefix threshold

Put

\[
 M_j=(j+1)P_z.
\]

If `n>M_j`, then `n/d>j+1` for every `d|(n,P_z)`, so every dictionary value in (L-97800.1) is the constant tail value one. Therefore

\[
 \boxed{a_{j,z}(n)=\mathbf1_{(n,P_z)=1}\qquad(n>M_j).}
\tag{L-97800.4}
\]

Let

\[
 D_{j,z}=\sum_{n\le M_j}{|a_{j,z}(n)|\over\sqrt n}.
\tag{L-97800.5}
\]

Expanding the divisor sum and using `sum_(k<=Y) k^(-1/2) <= 2 sqrt(Y)` gives the source-free bound

\[
 \boxed{
 D_{j,z}
 \le2Q_j\sqrt{(j+1)P_z}\,A_z.
 }
\tag{L-97800.6}
\]

Every complete residue block of length `P_z` beyond `M_j` contains exactly `phi(P_z)` positive coefficients. Consequently, if

\[
 K_j(z)=
 \max\left\{j+1,
 \left\lceil8Q_j^2(j+1)R_z^2\right\rceil\right\},
\tag{L-97800.7}
\]

then

\[
 \boxed{
 N\ge P_z(j+1+K_j(z))
 \Longrightarrow A_{j,z}(N)\ge0.
 }
\tag{L-97800.8}
\]

Indeed at the first such complete-block endpoint the positive tail contributes at least

\[
 {K\varphi(P_z)\over\sqrt{P_z(j+1+K)}}
 \ge {\varphi(P_z)\sqrt K\over\sqrt{2P_z}}
 \ge D_{j,z},
\]

and (L-97800.4) makes the prefix nondecreasing thereafter.

## 3. An explicit all-real row lower bound

Assume `X>4(j+1)P_z`. The contribution from `n<=M_j` is bounded below by `-D_(j,z) log X`. In the interval `(X/4,X/2]` all coefficients are already terminal and positive. Inclusion-exclusion gives

\[
 \#\{X/4<n\le X/2:(n,P_z)=1\}
 \ge {XV_z\over4}-2^{\omega_z}.
\]

Every selected summand has `n^(-1/2)>=sqrt(2/X)` and `log(X/n)>=log 2`. Thus

\[
 \boxed{
 C_{j,z}(X)\ge
 \sqrt{2\over X}\log2
 \left({XV_z\over4}-2^{\omega_z}\right)
 -D_{j,z}\log X.
 }
\tag{L-97800.9}
\]

Combining with (L-97800.6), define

\[
 \mathscr L_j(X,z)=
 \sqrt{2\over X}\log2
 \left({XV_z\over4}-2^{\omega_z}\right)
 -2Q_j\sqrt{(j+1)P_z}A_z\log X.
\tag{L-97800.10}
\]

Then

\[
 \boxed{\mathscr L_j(X,z)>0\Longrightarrow C_{j,z}(X)>0.}
\tag{L-97800.11}
\]

This implication covers every real activation cell; no integer interpolation is assumed.

## 4. The maximal certified growing cutoff

Let `z_*(X)` be the largest prime cutoff `z` for which

\[
 X>16P_z
 \qquad\text{and}\qquad
 \mathscr L_3(X,z)>0.
\tag{L-97800.12}
\]

The row-three bound is stricter because `2Q_2 sqrt(3)<2Q_3 sqrt(4)`. Therefore

\[
 \boxed{
 C_{2,z_*(X)}(X)>0,
 \qquad
 C_{3,z_*(X)}^\sharp(X)>0.
 }
\tag{L-97800.13}
\]

The prime number theorem and Mertens' product theorem give

\[
 \log P_z\sim z,
 \quad
 V_z\asymp(\log z)^{-1},
 \quad
 A_z\asymp\log z,
 \quad
 2^{\omega_z}=\exp(O(z/\log z)).
\tag{L-97800.14}
\]

For every fixed `0<kappa<1`, substituting `z=kappa log X` into (L-97800.10) gives

\[
 \mathscr L_3(X,z)
 \gg {\sqrt X\over\log\log X}
 -X^{\kappa/2+o(1)}\log X\log\log X>0
\]

for all sufficiently large `X`. Conversely `X>16P_z` and the prime number theorem force `z<=(1+o(1))log X`. Hence

\[
 \boxed{z_*(X)=(1+o(1))\log X.}
\tag{L-97800.15}
\]

Thus the growing finite Euler sieve is closed uniformly through a cutoff asymptotic to `log X`. Any remaining obstruction must use primes beyond this cofinal cutoff and cannot be a fixed finite-sieve phenomenon.
