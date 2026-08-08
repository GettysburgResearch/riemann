# L-30405 — Exact parity-shell, shift-commutator, and collar decomposition

Claim ID: `L-30405`  
Title: The complete critical cutoff boundary is one analytically regularized dyadic half-pole shell plus a subpower finite shift source and at most one collar atom  
Status: **PROPOSED COMPLETE EXACT STRUCTURAL THEOREM — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `R-30403`, `R-30404`; elementary alternating-series algebra and finite Möbius inversion  
Scope: exact decomposition and source-cost separation; no estimate of the dyadic half-pole shell and no RH conclusion

## 1. Complete paired boundary

Fix an integer endpoint `N>=4` and put

\[
Q=\left\lfloor{N+1\over2}\right\rfloor.
\tag{L-30405.1}
\]

For `2<=q<=Q`, define the complete critical paired cutoff boundary by

\[
\boxed{
\begin{aligned}
H_N(q)={}&
 \sum_{\substack{k\ge1\\2kq-1>N}}
 {1\over\sqrt{2kq-1}}\\
&-
 \sum_{\substack{k\ge1\\(2k+1)q>N}}
 {1\over\sqrt{(2k+1)q}}.
\end{aligned}}
\tag{L-30405.2}
\]

The two series are interpreted by extracting their at-most-one unmatched term
and pairing the remaining common tails. The paired series is absolutely
convergent, because each paired summand is `O(k^(-3/2)q^(-1/2))`.

## 2. Three exact pieces

Define the unshifted parity tail

\[
\boxed{
P_N(q)=
 \sum_{\substack{r\ge1\\rq>N}}
 {(-1)^r\over\sqrt{rq}}.}
\tag{L-30405.3}
\]

The `r=1` term is absent automatically for `q<=Q`, so this is the same as the
sum beginning at `r=2`. It converges by the alternating-series test.

Define the one-step shifted-even commutator

\[
\boxed{
E_N(q)=
 \sum_{\substack{k\ge1\\2kq-1>N}}
 \left[
 {1\over\sqrt{2kq-1}}-{1\over\sqrt{2kq}}
 \right]
 \ge0.}
\tag{L-30405.4}
\]

Finally define the collar

\[
\boxed{
C_N(q)=
 -{1\over\sqrt{N+1}}
 \mathbf1_{\,2q\mid N+1}.}
\tag{L-30405.5}
\]

Then

\[
\boxed{
H_N(q)=P_N(q)+E_N(q)+C_N(q)
\qquad(2\le q\le Q).}
\tag{L-30405.6}
\]

### Proof

Replace every shifted-even term in (L-30405.2) by its unshifted partner plus
(L-30405.4). The unshifted even cutoff is `2kq>N`, whereas the original shifted
cutoff is

\[
2kq-1>N
\quad\Longleftrightarrow\quad
2kq>N+1.
\]

They differ only when

\[
2kq=N+1.
\]

The corresponding unshifted parity term is present in `P_N` but absent from the
original boundary, producing exactly (L-30405.5). All remaining unshifted even
and odd terms combine into (L-30405.3). This proves (L-30405.6) without an
asymptotic estimate.

## 3. The collar is one source atom

If `N` is even, `N+1` is odd and `C_N=0`.

If `N` is odd, put

\[
M={N+1\over2}\le Q.
\]

Then

\[
C_N(q)=-(N+1)^{-1/2}\mathbf1_{q\mid M}.
\]

Consequently its unique finite divisor source is

\[
\boxed{
\sigma^{\rm col}_m
=-(N+1)^{-1/2}\mathbf1_{m=M}.}
\tag{L-30405.7}
\]

Its critical adjacent-tree atomic norm is exactly

\[
\boxed{
\|\sigma^{\rm col}\|_{\rm at}
={\sqrt M\over\sqrt{N+1}}
={1\over\sqrt2}.}
\tag{L-30405.8}
\]

Thus the parity-cutoff mismatch is an absolute constant, not the source of the
linear obstruction in `R-30404`.

## 4. The shifted-even commutator has bounded load mass

For

\[
L_q=\left\lfloor{N+1\over2q}\right\rfloor+1,
\]

one has `L_q>=2` and

\[
E_N(q)=
 \sum_{k\ge L_q}
 \left[(2kq-1)^{-1/2}-(2kq)^{-1/2}\right].
\]

The integral formula for `x^(-1/2)` gives

\[
0<(2kq-1)^{-1/2}-(2kq)^{-1/2}
\le {1\over2(kq)^{3/2}}.
\tag{L-30405.9}
\]

Moreover

\[
\sum_{k\ge L}k^{-3/2}
\le {2\over\sqrt{L-1}},
\]

and, since `floor(x)>=x/2` for `x>=1`,

\[
L_q-1
=\left\lfloor{N+1\over2q}\right\rfloor
\ge {N+1\over4q}.
\]

Therefore

\[
\boxed{
E_N(q)
\le {2\over q\sqrt{N+1}}.}
\tag{L-30405.10}
\]

Summing gives the uniform critical weighted-load estimate

\[
\begin{aligned}
\sum_{q=2}^{Q}\sqrt q\,E_N(q)
&\le {2\over\sqrt{N+1}}
 \sum_{q=2}^{Q}q^{-1/2}\\
&< {4\sqrt Q\over\sqrt{N+1}}\\
&\le2\sqrt2<3.
\end{aligned}
\tag{L-30405.11}
\]

## 5. Finite Möbius inversion of the shift costs only `N^(o(1))`

Let

\[
\boxed{
\sigma_m^{\rm sh}
=\sum_{d\le Q/m}\mu(d)E_N(md)
\qquad(2\le m\le Q)}
\tag{L-30405.12}
\]

be the unique finite divisor source of the shift load. Then

\[
\begin{aligned}
\|\sigma^{\rm sh}\|_{\rm at}
&\le
\sum_{m\le Q}\sqrt m
 \sum_{d\le Q/m}E_N(md)\\
&=
\sum_{n\le Q}\sqrt n E_N(n)
 \sum_{d\mid n}d^{-1/2}\\
&\le
\left(\max_{n\le Q}\tau(n)\right)
 \sum_{n\le Q}\sqrt n E_N(n).
\end{aligned}
\tag{L-30405.13}
\]

For every `epsilon>0`, the elementary divisor bound gives

\[
\max_{n\le Q}\tau(n)
\le C_\epsilon N^\epsilon.
\]

Together with (L-30405.11),

\[
\boxed{
\|\sigma^{\rm sh}\|_{\rm at}
\le3C_\epsilon N^\epsilon.}
\tag{L-30405.14}
\]

Thus the one-lattice-step shift is already harmless at the subpower scale
required by the carry/Cycle-Debt consumers.

## 6. Analytic Möbius inversion of the parity tail

The only remaining large piece is `P_N`.

For a complex parameter with `Re(s)>1`, define

\[
P_{N,s}(q)
=\sum_{rq>N}{(-1)^r\over(rq)^s}.
\tag{L-30405.15}
\]

Its infinite multiple-Möbius transform is absolutely convergent:

\[
\Sigma_{N,s}(m)
=\sum_{d\ge1}\mu(d)P_{N,s}(md).
\tag{L-30405.16}
\]

Interchanging the absolutely convergent sums and writing `n=dr` gives

\[
\begin{aligned}
\Sigma_{N,s}(m)
&=m^{-s}
 \sum_{n>N/m}{(\mu*\lambda)(n)\over n^s},
\end{aligned}
\tag{L-30405.17}
\]

where

\[
\lambda(r)=(-1)^r.
\]

The Dirichlet series of `lambda` is

\[
-\eta(s)=-(1-2^{1-s})\zeta(s),
\]

so

\[
\boxed{
\mu*\lambda=-\delta_1+2\delta_2.}
\tag{L-30405.18}
\]

Consequently

\[
\boxed{
\Sigma_{N,s}(m)
=m^{-s}
\left[
2^{1-s}\mathbf1_{m>N/2}
-\mathbf1_{m>N}
\right].}
\tag{L-30405.19}
\]

This is an exact identity in the absolute-convergence half-plane. It supplies
the analytic continuation of the transformed source to every `s`.

At the critical exponent, the analytically regularized source is therefore the
explicit dyadic half-pole shell

\[
\boxed{
\Sigma^{\rm reg}_{N,1/2}(m)
={1\over\sqrt m}
\left[
\sqrt2\,\mathbf1_{m>N/2}
-\mathbf1_{m>N}
\right].}
\tag{L-30405.20}

Equation (L-30405.20) is **not** asserted to be an absolutely summable raw
multiple source at `s=1/2`; its positive tail would diverge. Its correct scope is
analytic regularization or pairing in the declared half-pole-null physical
quotient. This scope distinction is mandatory.

## 7. Structural consequence

The linear finite atomic mass of `R-30404` has now been localized exactly:

```text
complete cutoff boundary
 = dyadic half-pole parity shell
 + subpower shifted-even commutator
 + at most one constant-cost collar atom.
```

Thus:

- an absolute finite-source termination is impossible by `R-30404`;
- the lattice shift and parity-cutoff collar are not the hard terms;
- the entire remaining obstruction is the analytically regularized dyadic
  half-pole shell (L-30405.20).

This is the same digital boundary type appearing in the repository's dyadic
shell, parity-comb, central-cascade, and WSTS programmes. Those programmes are
therefore not parallel accidents: they are the unique surviving source after
correct terminal recombination.

## 8. Correct next theorem

A successful continuation must prove a **physical null-quotient or lower-scale
identity** for (L-30405.20), retaining the complete analytic bulk and all
independent-frequency cross terms. It may then add the shift source using
(L-30405.14) and the collar using (L-30405.8).

The theorem is not permitted to reinterpret (L-30405.20) as an absolutely
summable divisor source. Nor may it charge its positive half-pole tail by total
variation.

## 9. Proof boundary

Proved exactly here:

- the three-term boundary decomposition;
- the one-atom collar source and exact norm;
- the uniform weighted-load bound for the shift;
- the subpower finite-source bound for the shift;
- the parity convolution `mu*lambda=-delta_1+2delta_2`;
- the exact analytic parity-source formula;
- identification of the sole surviving hard source as one dyadic half-pole
  shell.

Not proved here:

- a physical estimate or recurrence for the dyadic half-pole shell;
- Cycle Debt or WSTS;
- RH.
