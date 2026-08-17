# L-93291 — Every fixed finite large-prime sieve is eventually positive

Claim ID: `L-93291`  
Status: **PROVED UNCONDITIONAL THEOREM**  
Created: 2026-08-18  
Scope: every fixed finite set of primes greater than three; not the growing `LPTRP_23` sieve  
RH status: **not assumed**

Let `P` be a fixed squarefree product of primes greater than three. Use the
integer row dictionaries

\[
 q_2(n)=
 \begin{cases}0,&n<2,\\3,&n=2,\\0,&n=3,\\1,&n\ge4,
 \end{cases}
\tag{L-93291.1}
\]

and

\[
 q_3^\sharp(n)=
 \begin{cases}0,&n<3,\\6,&n=3,\\-2,&n=4,\\1,&n\ge5.
 \end{cases}
\tag{L-93291.2}
\]

For `j=2,3`, define

\[
 a_{j,P}(n)=\sum_{d\mid(n,P)}\mu(d)q_j(n/d),
\tag{L-93291.3}
\]

where `q_3` means `q_3^sharp`, and form the corresponding prefix and Riesz row.

## 1. Exact terminalization

Put

\[
 M_j=(j+1)P.
\tag{L-93291.4}
\]

If `n>M_j`, then `n/d>j+1` for every `d|P`. Every active dictionary value is
therefore its constant tail value one, and

\[
\boxed{
 a_{j,P}(n)
 =\sum_{d\mid(n,P)}\mu(d)
 =\mathbf1_{(n,P)=1}.
}
\tag{L-93291.5}
\]

Thus every negative coefficient is confined to the finite prefix
`n<=M_j`. After that point the prefix derivative is nondecreasing.

## 2. Explicit derivative threshold

Let

\[
 D_{j,P}=\sum_{n\le M_j}\frac{|a_{j,P}(n)|}{\sqrt n}.
\tag{L-93291.6}
\]

At

\[
 N=M_j+KP=P(j+1+K),
\tag{L-93291.7}
\]

the `K` complete residue blocks after `M_j` contain exactly `K phi(P)`
integers coprime to `P`. Hence, if `K>=j+1`,

\[
 A_{j,P}(N)
 \ge-D_{j,P}+\frac{K\varphi(P)}{\sqrt N}
 \ge-D_{j,P}+\frac{\varphi(P)\sqrt K}{\sqrt{2P}}.
\tag{L-93291.8}
\]

Therefore

\[
\boxed{
 K\ge
 \max\left\{j+1,
 \left\lceil\frac{2P D_{j,P}^2}{\varphi(P)^2}\right\rceil
 \right\}
 \Longrightarrow A_{j,P}(N)\ge0.
}
\tag{L-93291.9}
\]

By (L-93291.5), the prefix remains nonnegative at every later endpoint.

A source-free bound is also explicit. If `Q_2=3`, `Q_3=6`, then

\[
 D_{j,P}
 \le2Q_j\sqrt{(j+1)P}
 \prod_{p\mid P}\left(1+\frac1p\right).
\tag{L-93291.10}
\]

Thus a completely written threshold depends only on the finite prime set.

## 3. Eventual row positivity

The signed prefix contributes only `O_P(log X)` to the Riesz row. On the
terminal tail, restrict to coprime integers in `[X/4,X/2]`; their number is
`(phi(P)/(4P))X+O_P(1)`, every weight is at least `sqrt(2/X)`, and every
logarithmic factor is at least `log 2`. Consequently

\[
 C_{j,P}(X)\gg_P\sqrt X-O_P(\log X),
\tag{L-93291.11}
\]

so

\[
\boxed{C_{j,P}(X)>0\quad\text{for all sufficiently large real }X.}
\tag{L-93291.12}
\]

Every fixed finite sieve depth is therefore closed unconditionally. A failure
of `LPTRP_23`, if one exists, must use a number of active large primes tending
to infinity with the endpoint. This is a genuine cofinal localization, not a
proof of the growing-sieve theorem.
