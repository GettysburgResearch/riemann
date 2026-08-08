# L-24531 — Eta–Mersenne collapse of the central cascade and the exact dyadic zeta filter

Claim ID: `L-24531`  
Title: Pairing the exact central carry cascade with the reciprocal eta source leaves only the bottom value and sparse Mersenne jumps; one explicit dyadic difference removes the artificial eta zeros and recovers the Möbius Riesz coordinate  
Status: **PROPOSED COMPLETE — exact finite Dirichlet and carry algebra**  
Authoring agent: `gpt56-pro-25`  
Created: 2026-08-08  
Issue: #245  
Dependencies: `L-24523`, `L-24525`; elementary Dirichlet convolution  
Scope: exact sparse source identity and its correct RH-bearing dyadic filter

## 1. Reciprocal eta coefficients

Write

\[
\eta_D(s)=(1-2^{1-s})\zeta(s)
\]

for the Dirichlet eta function.  Let `b(n)` be the Dirichlet coefficients of
its reciprocal:

\[
\sum_{n\ge1}{b(n)\over n^s}={1\over\eta_D(s)}.
\tag{L-24531.1}
\]

Since

\[
{1\over1-2^{1-s}}
 =\sum_{r\ge0}{2^r\over(2^r)^s},
\qquad
{1\over\zeta(s)}=\sum_{m\ge1}{\mu(m)\over m^s},
\]

one obtains, for `n=2^r m` with `m` odd,

\[
\boxed{
 b(n)=
 \begin{cases}
 \mu(m),&r=0,\\
 2^{r-1}\mu(m),&r\ge1.
 \end{cases}}
\tag{L-24531.2}
\]

The convolution with the constant-one sequence is especially sparse:

\[
\boxed{
(\mathbf1*b)(n)=
\begin{cases}
2^r,&n=2^r,\\
0,&n\ne2^r.
\end{cases}}
\tag{L-24531.3}
\]

Indeed its Dirichlet series is

\[
{\zeta(s)\over\eta_D(s)}={1\over1-2^{1-s}}.
\]

## 2. Dyadic staircase divisor prefix

Define

\[
D_b(x)=\sum_{q\le x}b(q)\left\lfloor{x\over q}\right\rfloor.
\]

Finite divisor switching and (L-24531.3) give

\[
D_b(x)=\sum_{n\le x}(\mathbf1*b)(n)
      =\sum_{2^r\le x}2^r.
\]

Therefore, if

\[
2^K\le x<2^{K+1},
\]

then

\[
\boxed{D_b(x)=2^{K+1}-1.}
\tag{L-24531.4}
\]

No estimate enters this identity.

## 3. Central carry collapse

For the central split

\[
n=\lfloor n/2\rfloor+\lceil n/2\rceil,
\]

put

\[
Y_b(n)=\sum_{q=2}^{n}b(q)\chi_n^{\rm c}(q).
\tag{L-24531.5}
\]

The omitted term `q=1` is harmless because its carry indicator is zero.  By
(L-24531.4),

\[
Y_b(n)
 =D_b(n)-D_b(\lfloor n/2\rfloor)-D_b(\lceil n/2\rceil).
\tag{L-24531.6}
\]

Let `P` be the unique power of two with

\[
P\le n<2P.
\]

If `n<2P-1`, both children lie in `[P/2,P)`, and (L-24531.4) gives

\[
Y_b(n)=(2P-1)-2(P-1)=1.
\]

At the single Mersenne parent `n=2P-1`, the two children are `P-1` and `P`, so

\[
Y_b(2P-1)
 =(2P-1)-(P-1)-(2P-1)=1-P.
\]

Consequently

\[
\boxed{
Y_b(n)=1-
\sum_{\substack{P\text{ a power of }2\\n=2P-1}}P.
}
\tag{L-24531.7}
\]

Thus the dense reciprocal-eta source has collapsed on central rows to one
constant mode plus one sparse Mersenne defect per binary scale.

## 4. Exact sparse formula for any completed central cascade

Let `f_0,...,f_{L-1}` be any finite central residual cascade, extended by zero
outside `2,...,X`, and put

\[
A(n)=\sum_{j=0}^{L-1}[f_j(n)-f_j(n+1)].
\tag{L-24531.8}
\]

Assume its central carry load is a target `w(q)`:

\[
\sum_{n\ge q}A(n)\chi_n^{\rm c}(q)=w(q)
\qquad(2\le q\le X).
\tag{L-24531.9}
\]

Pairing (L-24531.9) with `b(q)` and using (L-24531.7) gives

\[
\sum_{q=2}^{X}b(q)w(q)
 =\sum_nA(n)
  -\sum_{\substack{P\text{ power of }2\\2P-1\le X}}P A(2P-1).
\tag{L-24531.10}
\]

Both pieces telescope in the stage coordinate:

\[
\sum_nA(n)=\sum_{j=0}^{L-1}f_j(2),
\]

and

\[
A(2P-1)
 =\sum_{j=0}^{L-1}
 [f_j(2P-1)-f_j(2P)].
\]

Therefore

\[
\boxed{
\begin{aligned}
\sum_{q=2}^{X}b(q)w(q)
={}&\sum_{j=0}^{L-1}f_j(2)\\
&-\sum_{j=0}^{L-1}
 \sum_{\substack{P\text{ power of }2\\2P-1\le X}}
 P[f_j(2P-1)-f_j(2P)].
\end{aligned}}
\tag{L-24531.11}
\]

For the terminating Neumann cascade of `L-24523`, equation (L-24531.11) is an
exact `O(log^2 X)`-entry representation of the reciprocal-eta Riesz coordinate.
It contains no sum over all primes or all integers after the central rows have
been paired.

## 5. Raw eta is not the RH-facing scalar

For a finite arithmetic sequence `c`, define the complete logarithmic Riesz
coordinate

\[
\widetilde{\mathcal R}_c(X)
 =\sum_{n\le X}{c(n)\over\sqrt n}\log{X\over n}.
\tag{L-24531.12}
\]

With `c=b`, its Mellin transform is initially

\[
\int_1^\infty
 \widetilde{\mathcal R}_b(X)X^{-z-1}\,dX
 ={1\over z^2\eta_D(z+1/2)}.
\tag{L-24531.13}
\]

The factor `1-2^{1-s}` has zeros on the line `Re(s)=1`.  Hence the raw eta
coordinate contains artificial poles unrelated to RH.  A subpower estimate for
(L-24531.12) is not the correct theorem and must not be claimed.

This is a mandatory firewall for every Mersenne-cascade argument.

## 6. Exact dyadic filter back to the Möbius source

Coefficientwise,

\[
\boxed{
\mu=b-2\,\delta_2*b.
}
\tag{L-24531.14}
\]

Indeed its Dirichlet multiplier is

\[
(1-2^{1-s}){1\over\eta_D(s)}={1\over\zeta(s)}.
\]

Under the square-root logarithmic normalization, (L-24531.14) becomes

\[
\boxed{
\widetilde{\mathcal R}_\mu(X)
 =\widetilde{\mathcal R}_b(X)
  -\sqrt2\,\widetilde{\mathcal R}_b(X/2),
}
\tag{L-24531.15}
\]

with the usual zero convention below the first endpoint.  The artificial eta
zeros cancel exactly.  The Mellin transform is

\[
\boxed{
\int_1^\infty
 \widetilde{\mathcal R}_\mu(X)X^{-z-1}\,dX
 ={1\over z^2\zeta(z+1/2)}.
}
\tag{L-24531.16}
\]

Thus the RH-bearing coordinate is the **completed dyadic difference of the
sparse Mersenne functional**, not either raw endpoint separately.

## 7. Central-Haar shell form

Let `A_X` and `A_Y`, `Y=floor(X/2)`, be the exact central-Neumann coefficient
vectors.  The shell vector

\[
B_X=A_X-A_Y
\]

saturates the target shell.  Apply (L-24531.11) separately at `X` and `Y`, and
then form the combination in (L-24531.15).  The result is a finite signed ledger
involving only

```text
bottom values f_j(2);
Mersenne adjacent jumps P[f_j(2P-1)-f_j(2P)];
the exact lower-endpoint copies;
explicit q=1 logarithmic terms.
```

All dense eta modes are removed before a positive part or norm is taken.  This
is the source-specific sparse coordinate nominated for the continuation in
`T-24508`.

## 8. Proof boundary

Proved exactly here:

1. the reciprocal-eta coefficient formula;
2. the dyadic staircase divisor prefix;
3. the central-row Mersenne collapse;
4. the sparse formula for every finite central cascade;
5. the artificial-pole firewall for raw eta;
6. the exact dyadic filter to the Möbius Riesz coordinate.

Not proved here:

1. a subpower estimate for the completed dyadic Mersenne ledger;
2. RH.
