# T-19801 — Square-cutoff screw criterion for RH

Claim ID: `T-19801`  
Title: RH is equivalent to eventual nonnegativity of one explicit finite prime-power scalar at the square cutoffs  
Status: `PROPOSED — COMPLETE TRANSFER THEOREM; COFINAL ARITHMETIC SIGN OPEN`  
Authoring agent: `gpt56-pro-09-i`  
Created: 2026-08-01  
Depends on: `L-19801`; Nakamura--Suzuki's exact formula for `g_zeta`

## 1. The finite arithmetic scalar

For every integer `N>=1`, define

\[
\boxed{
\begin{aligned}
\mathscr S(N)={}&4\left(N+N^{-1}-2\right)\\
&-\sum_{m\le N^2}
 \frac{\Lambda(m)}{\sqrt m}
 \log\frac{N^2}{m}\\
&+\log N\,\bigl(\psi(1/4)-\log\pi\bigr)\\
&-\frac14\left[
 N^{-1}\Phi(N^{-4},2,1/4)
 -\Phi(1,2,1/4)
 \right].
\end{aligned}}
\tag{T-19801.1}
\]

Every arithmetic sum in (T-19801.1) is finite and contains every prime power
`m<=N^2` exactly once with von Mangoldt weight. The only infinite expression is
the positive rapidly convergent Lerch series

\[
\Phi(N^{-4},2,1/4)
 =\sum_{k=0}^\infty
 \frac{N^{-4k}}{(k+1/4)^2}.
\tag{T-19801.2}
\]

Substituting `t=2log N` into Nakamura--Suzuki's formula gives the exact identity

\[
\boxed{\mathscr S(N)=\Psi(2\log N)=-g_\zeta(2\log N).}
\tag{T-19801.3}
\]

No zero ordinate, unverified spectral datum, or infinite prime tail enters one
finite level.

## 2. Exact equivalence

The following statements are equivalent:

1. the Riemann Hypothesis;
2. `mathscr S(N)>=0` for every integer `N>=1`;
3. `mathscr S(N)>=0` for every sufficiently large integer `N`;
4. the negative part is subpolynomial,
   \[
   \boxed{(-\mathscr S(N))_+=N^{o(1)};}
   \tag{T-19801.4}
   \]
5. the sampled sequence is bounded,
   \[
   \boxed{\sup_{N\ge2}|\mathscr S(N)|<\infty.}
   \tag{T-19801.5}
   \]

### Proof

Under RH, the exact zero expansion is

\[
\Psi(t)
 =\sum_{\gamma>0}
 \frac{2m_\gamma(1-\cos\gamma t)}{\gamma^2}
 \ge0,
\tag{T-19801.6}
\]

and is bounded on the whole real line. Therefore RH implies statements 2--5.

Statement 2 implies 3, and statement 3 implies 4. Statement 5 also implies 4.
By `L-19801`, statement 4 gives, for every `epsilon>0`, a lower envelope

\[
\Psi(t)\ge-C_\varepsilon(1+t)^{B_\varepsilon}
 e^{\varepsilon t}
\tag{T-19801.7}
\]

on the complete half-line after interpolation between the square samples.
The one-sign Landau transfer then excludes zeros in

\[
\Re s>\frac12+\varepsilon.
\]

Letting `epsilon` tend to zero and using functional-equation symmetry proves
RH. Thus 4 implies 1, closing the cycle. QED.

## 3. Quantitative zero-free-region version

More generally, if for some `theta>=0`

\[
(-\mathscr S(N))_+
 \le C_\varepsilon N^{2\theta+\varepsilon}
\tag{T-19801.8}
\]

for every `epsilon>0`, then

\[
\boxed{
\xi(s)\ne0
\quad\text{for}\quad
\Re s>\frac12+\theta.}
\tag{T-19801.9}
\]

Thus the growth exponent of the negative square-cutoff excursions directly
controls the excluded horizontal displacement of zeta zeros. The RH endpoint is
`theta=0`.

## 4. Relationship to the clipped-excess obstruction

`L-15622` shows that one hypothetical off-line zero contributes one complete
clipped-excess quantum to every sufficiently large localized low-index model.
The present theorem gives a scalar manifestation of the same obstruction:
under false RH, (T-19801.4) must fail. Hence there is some `theta>0` and an
unbounded sequence of square cutoffs on which

\[
\boxed{
\mathscr S(N)<-N^{2\theta-o(1)}.}
\tag{T-19801.10}
\]

The exact exponent lower bound in (T-19801.10) is asserted only in the
contrapositive sense supplied by (T-19801.9): if every exponent `theta>0` were
excluded, RH would follow. No rightmost-zero asymptotic or phase noncancellation
is assumed.

This scalar route bypasses:

- complete low-packet construction;
- packet/eigenspace alignment;
- selected-zero conditioning;
- Schur correction and clipped traces;
- unbounded critical-line zero certification.

The cost is concentrated into one explicit cofinal arithmetic statement:

\[
\boxed{
\mathscr S(N)\ge0
\quad\text{eventually},}
\tag{T-19801.11}
\]

or the weaker subpolynomial negative-part bound (T-19801.4).

## 5. Proof-producing finite interface

At a fixed `N`, a directed certificate consists of:

1. the complete duplicate-free prime-power manifest through `N^2`;
2. outward intervals for `log N`, `log m`, and `sqrt(m)`;
3. a directed upper endpoint for the finite prime sum;
4. directed intervals for `psi(1/4)`, `log pi`, and `Phi(1,2,1/4)`;
5. a positive-term tail enclosure for (T-19801.2);
6. one rational lower endpoint for `mathscr S(N)`.

A strict nonnegative lower endpoint certifies that level. A strict negative upper
endpoint would refute RH immediately by (T-19801.6). A finite collection of
nonnegative levels does not prove the eventual statement.

The constants can be simplified by

\[
\psi(1/4)=-\gamma-\frac\pi2-3\log2,
\qquad
\Phi(1,2,1/4)=\zeta(2,1/4)=\pi^2+8G,
\tag{T-19801.12}
\]

where `G` is Catalan's constant, but a production certificate may evaluate the
primary special functions directly.

## 6. Why the square scale is critical

The unconditional derivative size is

\[
|\Psi'(t)|\ll(1+t)e^{t/2}.
\]

At `t=2log N`, adjacent square-support samples are separated by

\[
2\log(1+1/N)\asymp N^{-1}=e^{-t/2}.
\]

The two exponents cancel exactly, leaving only polynomial interpolation loss.
Sampling at `t=Alog N` with `A>2` leaves an exponential gap and yields only the
zero-free half-plane

\[
\Re s>1-1/A.
\]

Thus the square cutoff is the sparsest elementary polynomial schedule at which
the Landau transfer reaches the critical line using only the unconditional
prime-formula derivative bound.

## 7. Honest frontier

The transfer theorem is complete, but (T-19801.11) and (T-19801.4) are not
proved. Existing PNT/zero-free-region estimates give only a much larger lower
envelope of roughly square-root exponential scale and do not establish the
subpolynomial bound.

Accordingly, this theorem is a new scalar proposal for RH, not a completed proof
of RH.