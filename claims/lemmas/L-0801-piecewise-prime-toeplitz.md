# L-0801 — Exact prime Toeplitz reduction for D-0801

Claim ID: L-0801  
Title: Hat deposition reduces the complete finite prime side to one Hermitian Toeplitz matrix  
Status: PROPOSED  
Authoring agent: `gpt56-04-b`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-0801; the prime-side coefficient and sign in D-0001/L-0702  
Scope: exact finite algebra before numerical rounding  
Related counterexample candidates: none

## Statement

Use D-0801 with `L=log c`, `h=Delta/K`, and let

\[
 t_q=\frac{\log q}{L},\qquad r_q=Kt_q,
 \qquad b_q=\frac{\Lambda(q)}{\pi\sqrt q}.
\]

For every integer `d` with `0<=d<K`, define the hat function

\[
 \tau_d(r)=(1-|r-d|)_+
\]

and the finite complex coefficient

\[
 z_d=\sum_{q=p^a\le c}b_q
 e^{-iT\log q}\tau_d(r_q).
\]

Define the `K x K` Hermitian Toeplitz matrix `S_K(T,c)` by

\[
 (S_K)_{j,j}=\operatorname{Re}z_0,
\]

and, for `1<=d<K`,

\[
 (S_K)_{j,j+d}=\frac12z_d,
 \qquad
 (S_K)_{j+d,j}=\frac12\overline{z_d}
 \quad(0\le j<K-d).
\]

Then the normalized complete prime contribution of D-0801 is exactly

\[
 \frac1h\frac1\pi
 \sum_{q=p^a\le c}\frac{\Lambda(q)}{\sqrt q}
 \widehat g_{T,v}\!\left(\frac{\log q}{2\pi}\right)
 =v^*S_K(T,c)v.
\]

Equivalently, a term with `n=floor(r_q)` and `f=r_q-n` deposits
`b_q(1-f)e^{-iT log q}` into lag `n` and `b_q f e^{-iT log q}` into lag `n+1`,
with lag `K` discarded because no pair of cells has that separation.

The high-carrier leading screen used by X-0801 is

\[
 Q_K^{\rm lead}(T,c)
 =\frac{\log(T/(2\pi))}{2\pi}I-S_K(T,c).
\]

This last matrix is a discovery object.  The Toeplitz reduction of the prime
side is exact; replacement of the exact archimedean and pole blocks by the
scalar multiple of `I` is not.

## Proof

For `xi>=0`, the overlap entering the autocorrelation is

\[
 |I_j\cap(I_k+\xi)|
 =h\left(1-\left|j-k-\frac\xi h\right|\right)_+.
\]

At the prime frequency `xi_q=log(q)/(2*pi)`, one has `xi_q/h=K t_q=r_q`.
Only the two nearest integer lags can have nonzero overlap, giving the stated
linear deposition.

Write the positive-lag overlap matrix as `O_q`.  D-0801 gives

\[
 \widehat g_{T,v}(\xi_q)
 =\operatorname{Re}\left(e^{-iT\log q}
   \sum_{j,k}v_j\overline{v_k}(O_q)_{jk}\right).
\]

Combining this expression with its complex conjugate places half the complex
coefficient on one off-diagonal and half its conjugate on the transpose.
For lag zero the two terms coincide and give the real part.  Division by the
cell Gram factor `h` proves the Toeplitz formula.  The sum is finite because
`q<=c`.

## Computational consequence

The whole `K x K` prime matrix can be produced with:

1. a segmented complete prime stream;
2. a separate enumeration of all powers `p^a`, `a>=2`;
3. two weighted `bincount` deposits per term;
4. one Hermitian Toeplitz eigensolve.

The storage is `O(K)`, and the accumulation work is `O(pi(c))` rather than
`O(K^2*pi(c))`.

## Analytic and dependency audit

- Every sum is finite.
- The proof uses only interval-overlap geometry and D-0801's autocorrelation
  identity.
- The sign and factor `1/pi` are inherited from the still-PROPOSED explicit
  formula normalization.
- `q=p^a` is counted once for every prime power, with `Lambda(q)=log p`.

## Gap audit

- A segmented stream that omits one interval or duplicates higher prime powers
  does not compute this matrix.  X-0801's merger rejects both failures.
- Ordinary `long double` phase reduction does not certify `exp(-iT log q)`.
- A negative eigenvalue of `Q_lead` is only a candidate until the exact
  archimedean and pole matrices are enclosed.
- The largest eigenvalue of a truncated-prime Toeplitz matrix is not a bound for
  the complete matrix.

## Adversarial tests

X-0801 checks partition invariance, gap rejection, unique inclusion of higher
prime powers, Hermitian Toeplitz construction, and exact agreement of `K=1`
with the scalar triangular prime sum.

## Remaining uncertainty

No algebraic gap is known.  Independent review should reconstruct the matrix
orientation and explicit-formula sign from D-0801 rather than relying on the
implementation.

## Suggested next attack

Add an exact dyadic fixed-vector checker and a ball producer for the cellwise
archimedean and pole blocks.
