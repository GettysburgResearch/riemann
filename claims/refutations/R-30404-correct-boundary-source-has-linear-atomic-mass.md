# R-30404 — The correctly inverted terminal boundary has linear atomic mass

Claim ID: `R-30404`  
Title: Möbius inversion does not rescue the terminal adjacent-commutator proof: the unique genuine divisor source of the complete critical cutoff boundary has atomic norm at least `N/480`  
Status: **EXACT HYPOTHESIS-MATCHING REFUTATION OF THE ABSOLUTE TERMINAL CLOSURE**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen target: PR #304 at `78b75fc17e27334a9950018528c1c6e083d74820`  
Dependencies: the cutoff boundary definition of PR #286; elementary finite Möbius inversion  
Scope: the complete critical boundary and every exact source decomposition terminated by a sum of atomic norms; non-absolute coupled estimates are not refuted

## 1. Complete cutoff boundary

Fix an integer endpoint `N>=30` and put

\[
Q=\left\lfloor{N+1\over2}\right\rfloor.
\tag{R-30404.1}
\]

For the critical power

\[
p(x)=x^{-1/2},
\]

let `h_N(q)` denote the complete paired cutoff boundary on the output columns
`2<=q<=Q`. On the common-tail cells used below this is the absolutely convergent
paired series

\[
 h_N(q)=
 \sum_{k=K(q)}^\infty
 \left[
  {1\over\sqrt{2kq-1}}
  -{1\over\sqrt{(2k+1)q}}
 \right],
\tag{R-30404.2}
\]

where both omitted tails have the same first index `K(q)`. Every summand in
(R-30404.2) is positive and is `O(k^{-3/2}q^{-1/2})`, so no regularization or
interchange of divergent series is involved in the argument below.

## 2. The unique genuine divisor source

There is one and only one finite divisor source

\[
\sigma^{(N)}=(\sigma_m^{(N)})_{2\le m\le Q}
\]

whose carry loads equal the complete boundary:

\[
\boxed{
 h_N(q)=
 \sum_{\substack{m\le Q\\q\mid m}}
 \sigma_m^{(N)}
 \qquad(2\le q\le Q).}
\tag{R-30404.3}
\]

Finite Möbius inversion gives

\[
\boxed{
 \sigma_m^{(N)}
 =\sum_{d\le Q/m}\mu(d)h_N(md).}
\tag{R-30404.4}
\]

This is the correctly typed replacement for the `q`-dependent pseudo-source
rejected in `R-30403`.

Define its critical adjacent-tree atomic norm by

\[
\boxed{
 \|\sigma^{(N)}\|_{\rm at}
 =\sum_{m=2}^{Q}\sqrt m\,|\sigma_m^{(N)}|.}
\tag{R-30404.5}
\]

This is exactly the source cost used by an absolute adjacent-commutator
termination.

## 3. A linear family on which Möbius inversion is the identity

Put

\[
\boxed{
 I_N=
 \left\{
  m:\
  \left\lfloor{N+1\over4}\right\rfloor+1
  \le m\le
  \left\lfloor{N\over3}\right\rfloor
 \right\}.}
\tag{R-30404.6}
\]

For every `m in I_N`,

\[
 m>{Q\over2}.
\tag{R-30404.7}
\]

Therefore `d=1` is the only term in (R-30404.4), and

\[
\boxed{
 \sigma_m^{(N)}=h_N(m)
 \qquad(m\in I_N).}
\tag{R-30404.8}

Thus this entire cell is immune to any possible Möbius cancellation.

The endpoint inequalities are also exact:

\[
 2m-1\le N,
 \qquad
 3m\le N,
\tag{R-30404.9}
\]

while

\[
 4m-1>N,
 \qquad
 5m>N.
\tag{R-30404.10}
\]

Hence the shifted-even and unshifted-odd omitted tails both start at `k=2`, and

\[
\boxed{
 h_N(m)=
 \sum_{k=2}^\infty
 \left[
  {1\over\sqrt{2km-1}}
  -{1\over\sqrt{(2k+1)m}}
 \right]>0.}
\tag{R-30404.11}
\]

## 4. Uniform atomic lower bound on the common-tail cell

Keeping only the first positive summand in (R-30404.11),

\[
\begin{aligned}
 \sqrt m\,\sigma_m^{(N)}
 &\ge
 {\sqrt m\over\sqrt{4m-1}}
 -{1\over\sqrt5}\\
 &>{1\over2}-{1\over\sqrt5}\\
 &>{1\over20}.
\end{aligned}
\tag{R-30404.12}
\]

The last inequality is exact, since

\[
 {1\over\sqrt5}<{9\over20}
 \quad\Longleftrightarrow\quad
 400<405.
\tag{R-30404.13}
\]

Moreover

\[
\begin{aligned}
 |I_N|
 &\ge {N\over3}-1-{N+1\over4}\\
 &= {N\over12}-{5\over4}\\
 &\ge {N\over24}
 \qquad(N\ge30).
\end{aligned}
\tag{R-30404.14}

Combining (R-30404.5), (R-30404.8), (R-30404.12), and
(R-30404.14) gives the advertised bound:

\[
\boxed{
 \|\sigma^{(N)}\|_{\rm at}
 > {N\over480}
 \qquad(N\ge30).}
\tag{R-30404.15}
\]

This is a lower bound for the unique correctly inverted **complete** boundary
source, not for one arbitrarily selected Euler jet.

## 5. Every absolute source decomposition inherits the lower bound

Suppose an exact Euler, Peano, stopped-power, or other source decomposition
writes

\[
\sigma^{(N)}=\sum_{a\in\mathcal A_N}\sigma_a^{(N)}.
\tag{R-30404.16}
\]

The atomic norm is a norm, so

\[
\boxed{
 \sum_{a\in\mathcal A_N}
 \|\sigma_a^{(N)}\|_{\rm at}
 \ge
 \left\|\sum_a\sigma_a^{(N)}\right\|_{\rm at}
 =\|\sigma^{(N)}\|_{\rm at}
 >{N\over480}.}
\tag{R-30404.17}
\]

Consequently no exact decomposition followed by absolute adjacent-commutator
termination can have total source cost

\[
O((\log N)^C).
\]

The obstruction cannot be repaired by increasing Euler order, regrouping the
jets, or first correcting the source typing. The complete source itself already
has linear atomic mass.

## 6. Precise disposition of PR #304

The following implications in the frozen proposal are false:

```text
complete terminal boundary
-> source atomic mass polylogarithmic
-> absolute adjacent-tree lift has polylogarithmic capacity debt
-> terminal family closes Cycle Debt.
```

In particular the bounds asserted in `L-30403.6`, `L-30403.8`, and the terminal
consumer in `T-30401` are unavailable.

The exact sparse tree identity

\[
\mathcal L_q(E_h)=\mathbf1_{q\mid h+1}
\]

survives. What fails is the use of that identity after taking the absolute
atomic norm of the complete critical boundary.

## 7. Correct research frontier

This theorem does **not** rule out a coupled signed or Hilbert-space estimate.
It proves that any successful continuation must preserve cancellations between
source coordinates until after the physical quadratic form is assembled.
The viable logical shape is therefore

```text
complete boundary vector
-> exact Möbius-inverted source
-> signed/two-frequency normal Gram
-> source-specific cancellation or lower-scale recurrence
```

and not

```text
complete boundary vector
-> sum of atomic source norms
-> absolute adjacent-tree termination.
```

The corrected route remains RH-bearing: the complete boundary contains the
fixed-ratio Möbius modes which the repository's first-cell and WSTS decoders
already identify as equivalent to the unresolved critical cancellation.

## 8. Proof boundary

Proved exactly here:

- the unique finite divisor source for the complete boundary;
- a linear common-tail cell on which Möbius inversion is the identity;
- a uniform positive contribution greater than `1/20` per source node;
- the linear lower bound `N/480`;
- inheritance by every exact decomposition terminated through a sum of atomic
  norms;
- rejection of the absolute terminal closure of PR #304.

Not proved or refuted here:

- a coupled non-absolute physical normal-Gram estimate;
- Cycle Debt by a different mechanism;
- WSTS;
- RH.
