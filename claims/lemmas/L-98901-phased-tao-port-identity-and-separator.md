# L-98901 — The Tao semigroup port is not phase-covariant with its unit diagonal

Claim ID: `L-98901`  
Status: **PROVED EXACT FINITE PHASE-SEPARATOR THEOREM**  
Created: 2026-08-18  
Depends on: the unphased Tao port of PR #610 / `L-98701`  
RH status: **not assumed**

Let `P` be a finite prime set, `S_P` its multiplicative semigroup, and for real
`tau` put

\[
A_{P,\tau}(x)
=\sum_{\substack{n\le x\\n\in S_P}}
 \frac{\mu(n)}n n^{-i\tau}.
\tag{L-98901.1}
\]

Then restricted Möbius inversion with phases gives the exact identity

\[
\boxed{
\begin{aligned}
xA_{P,\tau}(x)
={}&\sum_{k\le x}
 \prod_{\substack{p\mid k\\p\in P}}(1-p^{-i\tau})\\
&+\sum_{\substack{n\le x\\n\in S_P}}
 \mu(n)\{x/n\}n^{-i\tau}.
\end{aligned}}
\tag{L-98901.2}
\]

At `tau=0`, the product in the first line is the indicator that `k` has no
prime factor in `P`; this recovers the positive complementary-semigroup atom
count used by the Tao completion. For nonzero phase it is a complex product,
not a positive indicator.

## Smallest exact separator

Take

\[
P=\{3\},\qquad x=3,\qquad \tau=\frac\pi{\log3}.
\]

Then `3^{-i tau}=-1`, so

\[
A_{P,\tau}(3)=1-\frac13(-1)=\frac43.
\tag{L-98901.3}
\]

The unphased Tao diagonal is

\[
C_P(3)=\frac{N_P(3)+N_{P^c}(3)-H_P(3)}3=\frac89.
\tag{L-98901.4}
\]

Hence the putative phase-rotated port

\[
\begin{pmatrix}8/9&4/3\\4/3&8/9\end{pmatrix}
\]

has determinant

\[
\boxed{-\frac{80}{81}<0.}
\tag{L-98901.5}
\]

The same local diagonal that pays the unphased Möbius port therefore does not
pay its logarithmic phase.

## Scope

The unphased atom decomposition in `L-98701` remains exact. What fails is the
last inference that these atoms are automatically “phase-ready” for the common
log-carrier Fock construction used in `L-98703`. A valid phased completion must
add a larger, phase-dependent diagonal or a separate cross-scale covariance
theorem. Neither is supplied by the local Tao port.
