# L-23804 — One-sided carry mass and screw transfer

Claim ID: `L-23804`  
Title: A sharp nonnegative carry packing, without any upper cover, gives the square-screw envelope required for RH  
Status: **PROPOSED EXACT COMPOSITION LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-07  
Issue: #238  
Dependencies: `L-23801`, the square-sampling Landau transfer `L-19801`  
Scope: finite packing to RH; the sharp packing mass remains open

## 1. Only a packing is needed

For an endpoint `X>=2`, let

\[
w_X(q)=q^{-1/2}\log(X/q),
\qquad 2\le q\le X,
\]

and let `B_X=(beta_(nq))` be the carry matrix of `L-23801`.
A **carry packing** is a vector `d_X=(d_X(2),...,d_X(X))` satisfying

\[
\boxed{
 d_X(n)\ge0,
 \qquad
 B_X^T d_X\le w_X.
}
\tag{L-23804.1}
\]

By the exact Legendre/carry identity and `Lambda>=0`,

\[
\boxed{
 \mathcal P(X)
 :=\sum_{q=p^a\le X}{\Lambda(q)\over\sqrt q}\log{X\over q}
 \ge \sum_{n=2}^X d_X(n)G_n.
}
\tag{L-23804.2}
\]

No nonnegative carry cover is needed for the argument below.

## 2. Every packing has logarithmic coefficient mass

Put

\[
S_n=\sum_{q=2}^n{\beta_{nq}\over q}.
\tag{L-23804.3}
\]

There is an absolute lower bound

\[
\boxed{S_n\ge {1\over16}\qquad(n\ge2).}
\tag{L-23804.4}
\]

For `n>=8`, restrict the sum to

\[
\left\lceil{3(n+1)\over4}\right\rceil\le q\le n.
\]

On this range `q>n/2`, so

\[
\beta_{nq}={2q-n-1\over n+1}\ge{1\over2}.
\]

There are at least `n/8` such integers and `q<=n`, giving (L-23804.4).
The cases `2<=n<8` are checked directly from the displayed formula for
`beta_(nq)`.

Multiply every packing constraint by `1/q` and sum. Then

\[
{1\over16}\sum_{n=2}^X d_X(n)
\le
\sum_{q=2}^X{w_X(q)\over q}.
\tag{L-23804.5}
\]

Since

\[
\sum_{q=2}^X{w_X(q)\over q}
=
\sum_{q=2}^X q^{-3/2}\log(X/q)
\ll\log X,
\]

one obtains the unconditional packing bound

\[
\boxed{
\sum_{n=2}^X d_X(n)\ll\log X.
}
\tag{L-23804.6}
\]

This is useful because it makes the entropy error only polylogarithmic for
**every** feasible packing, not merely for the exact triangular inverse.

## 3. Mass-to-entropy conversion

The entropy estimate of `L-23801` gives

\[
G_n\ge {n\over2}-\log(n+1)-3.
\]

Combining this with (L-23804.6),

\[
\boxed{
\sum_{n=2}^X d_X(n)G_n
\ge
{1\over2}\sum_{n=2}^Xn\,d_X(n)-O(\log^2X).
}
\tag{L-23804.7}
\]

Accordingly, the single finite mass estimate

\[
\boxed{
\sum_{n=2}^X n\,d_X(n)
\ge8\sqrt X-X^{o(1)}
}
\tag{L-23804.8}
\]

implies

\[
\boxed{
\mathcal P(X)\ge4\sqrt X-X^{o(1)}.
}
\tag{L-23804.9}
\]

The error convention means that for every `epsilon>0` the deficit is
`O_epsilon(X^epsilon)`.

## 4. The upper screw envelope also gives a zero-free half-plane

Use the zeta screw normalization

\[
\begin{aligned}
\Psi(t)={}&4(e^{t/2}+e^{-t/2}-2)
-\sum_{m\le e^t}{\Lambda(m)\over\sqrt m}(t-\log m)\\
&+O(1+t),
\end{aligned}
\tag{L-23804.10}
\]

where the displayed `O(1+t)` consists of the explicit linear and absolutely
convergent Lerch terms.
At `X=e^t`, the prime sum is exactly `mathcal P(X)`.
Hence (L-23804.9), evaluated at `X=N^2`, gives

\[
\boxed{
\Psi(2\log N)\le N^{o(1)}.
}
\tag{L-23804.11}
\]

`L-19801` states the square-sampling Landau transfer for a lower envelope of
`Psi`. The identical proof applies to an upper envelope: replace `Psi` by
`-Psi`, add a positive polynomial-exponential correction so that the resulting
function is nonnegative, and apply Landau's one-sign theorem to the negative of
the same Fourier--Laplace transform. Multiplication by `-1` changes no pole
location. The unconditional derivative budget used to interpolate between the
square samples is likewise unchanged.

Consequently, if for every `epsilon>0`

\[
\Psi(2\log N)\le C_\epsilon N^{2\epsilon}
\]

eventually, then zeta has no zero in `Re s>1/2+epsilon`. Letting `epsilon`
tend to zero and using functional-equation symmetry gives RH.

Thus

\[
\boxed{
\text{(L-23804.1) and (L-23804.8) for square endpoints}
\Longrightarrow\mathrm{RH}.}
\tag{L-23804.12}
\]

## 5. Proof boundary

Closed here:

- packing alone controls the prime ramp in the required direction;
- every feasible packing has only logarithmic coefficient mass;
- weighted carry mass `8 sqrt(X)` converts to entropy `4 sqrt(X)` with only
  polylogarithmic loss;
- an upper, rather than lower, subexponential screw envelope has the same
  Landau zero-exclusion consequence.

Open:

- construction of a packing satisfying (L-23804.8);
- RH.

The two-sided carry sandwich of `T-23801` remains a valid stronger sufficient
condition, but it is not the minimal theorem.