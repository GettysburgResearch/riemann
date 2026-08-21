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

Substitution of `t=2log N` in Nakamura--Suzuki's explicit screw formula gives

\[
\boxed{\mathscr S(N)=\Psi(2\log N)=-g_\zeta(2\log N).}
\tag{T-19801.3}
\]

Thus one level uses no zero ordinate, no spectral approximation, and no infinite
prime tail.

## 2. Exact equivalence

Interpret

\[
a_N=N^{o(1)}
\]

to mean that, for every `epsilon>0`, there is a constant `C_epsilon` such that
`a_N<=C_epsilon N^epsilon` for all sufficiently large `N`.

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

Under RH, the exact zero expansion pairs `gamma` with `-gamma` and gives

\[
\Psi(t)
 =\sum_{\gamma>0}
 \frac{2m_\gamma(1-\cos\gamma t)}{\gamma^2}
 \ge0.
\tag{T-19801.6}
\]

The series is uniformly bounded because
`sum_gamma m_gamma/|gamma|^2<infinity`. Hence RH implies 2--5.

Clearly 2 implies 3, while 3 and 5 each imply 4. Assume 4. Given any
`delta>0`, apply (T-19801.4) with exponent `2delta`. Since
`N=exp(t/2)` at the square samples, `L-19801` extends the sample lower bound to

\[
\Psi(t)\ge-C_\delta(1+t)^{B_\delta}e^{\delta t}
\tag{T-19801.7}
\]

on the complete half-line. Add a positive polynomial multiple of
`e^(delta t)` and one compactly supported correction to obtain a nonnegative
function. Landau's one-sign Laplace theorem, together with

\[
\int_0^\infty\Psi(t)e^{izt}dt
 =-z^{-2}\frac{\xi'}{\xi}(1/2-iz),
\]

then excludes zeros in `Re s>1/2+delta`. Since `delta>0` is arbitrary and the
functional equation reflects zeros about `Re s=1/2`, RH follows. Thus 4 implies
1. QED.

## 3. Quantitative zero-free-region version

More generally, suppose that for some `theta>=0` and every `epsilon>0`,

\[
(-\mathscr S(N))_+
 \le C_\varepsilon N^{2\theta+\varepsilon}
\tag{T-19801.8}
\]

for all sufficiently large `N`. Applying the preceding argument with an
arbitrarily small additional exponential loss gives

\[
\boxed{
\xi(s)\ne0
\quad\text{for}\quad
\Re s>\frac12+\theta.}
\tag{T-19801.9}
\]

Thus the smallest admissible power exponent for the negative square-cutoff
excursions controls a zero-free half-plane. The RH endpoint is `theta=0`.

## 4. Exact false-RH contrapositive

`L-15622` shows that a hypothetical off-line zero contributes one complete
clipped-excess quantum to every sufficiently large localized low-index model.
The square-screw criterion gives a scalar version of the same obstruction.

If RH is false, (T-19801.4) fails. Equivalently, there exists
`epsilon_0>0` such that

\[
\boxed{
\sup_{N\ge N_0}
 \frac{(-\mathscr S(N))_+}{N^{\epsilon_0}}
 =\infty
\quad\text{for every }N_0.}
\tag{T-19801.10}
\]

This is the precise unconditional contrapositive. It does **not** assert a
pointwise asymptotic or a fixed-sign leading term: obtaining either would require
additional phase/noncancellation information about the rightmost off-line zeros.

The scalar route bypasses complete low-packet construction, packet/eigenspace
alignment, selected-zero conditioning, Schur correction, clipped traces, and an
unbounded critical-line zero census. Its entire RH content is concentrated into
one explicit cofinal arithmetic assertion:

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
3. a directed interval for the complete finite prime sum;
4. directed intervals for `psi(1/4)`, `log pi`, and `Phi(1,2,1/4)`;
5. a positive-term tail enclosure for (T-19801.2);
6. one rational interval enclosing `mathscr S(N)`.

A nonnegative lower endpoint certifies that level. A strictly negative upper
endpoint would refute RH immediately by (T-19801.6). A finite collection of
nonnegative levels, however long, does not prove the eventual assertion.

The constants may be simplified by

\[
\psi(1/4)=-\gamma-\frac\pi2-3\log2,
\qquad
\Phi(1,2,1/4)=\zeta(2,1/4)=\pi^2+8G,
\tag{T-19801.12}
\]

where `G` is Catalan's constant.

## 6. Why the square scale is critical

The unconditional explicit-formula derivative bound is

\[
|\Psi'(t)|\ll(1+t)e^{t/2}.
\]

At `t=2log N`, adjacent samples are separated by

\[
2\log(1+1/N)\asymp N^{-1}=e^{-t/2}.
\]

The exponents cancel, leaving only a polynomial interpolation loss. More
generally, sampling at `t=Alog N` has residual interpolation exponent

\[
\sigma_A=\max(0,1/2-1/A).
\]

For `A>2`, eventual sample nonnegativity yields only the zero-free half-plane

\[
\Re s>\frac12+\sigma_A=1-\frac1A.
\]

Thus `A=2` is the sparsest elementary polynomial cutoff schedule for which the
unconditional derivative budget reaches the critical line.

## 7. Honest frontier

The transfer theorem is complete from the imported screw/Laplace identity and
Landau's theorem. The arithmetic estimates (T-19801.11) and (T-19801.4) are not
proved. Standard phase-blind prime-number-theorem bounds remain far too coarse
to establish them.

Accordingly, this is a new scalar proposal for RH, not a completed proof of RH.