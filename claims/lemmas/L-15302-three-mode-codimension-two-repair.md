# L-15302 — Three-mode codimension-two source repair

Claim ID: `L-15302`  
Title: Three same-parity modes enforce both radical-source constraints exactly  
Status: `PROPOSED`  
Authoring agent: `gpt56-03-j`  
Created: 2026-07-31  
Dependencies: elementary linear algebra and finite Fourier concentration identities

## Exact repair

Let `p_0,p_1,p_2` be real even source functions and define

\[
 v_j=p_j(0),\qquad m_j=\widehat p_j(0)=\int p_j.
\]

Set

\[
 a_0=v_1m_2-v_2m_1,\quad
 a_1=v_2m_0-v_0m_2,\quad
 a_2=v_0m_1-v_1m_0.                         \tag{1}
\]

If the vectors `v=(v_0,v_1,v_2)` and `m=(m_0,m_1,m_2)` are not proportional,
then `a` is nonzero and

\[
 f=\sum_{j=0}^2a_jp_j
\]

satisfies exactly

\[
 \boxed{f(0)=0,\qquad\widehat f(0)=\int f=0.} \tag{2}
\]

Indeed, direct expansion gives

\[
 \sum_ja_jv_j=0,\qquad\sum_ja_jm_j=0.
\]

No asymptotic approximation enters these two source constraints.

## Finite-Fourier specialization

Suppose the modes are orthonormal, supported in one interval, and satisfy

\[
 PFp_j=\chi_jp_j,\qquad 0<\chi_j<1,
\]

where `P` is the time projection and `F` is unitary Fourier transform. In a
normalization where evaluation at zero is integration,

\[
 m_j=\chi_jv_j.
\]

Equation (1) becomes

\[
 \begin{aligned}
 a_0&=v_1v_2(\chi_2-\chi_1),\\
 a_1&=v_2v_0(\chi_0-\chi_2),\\
 a_2&=v_0v_1(\chi_1-\chi_0).
 \end{aligned}                               \tag{3}
\]

Moreover

\[
 \|P(Ff-f)\|_2^2=\sum_ja_j^2(1-\chi_j)^2
\]

and

\[
 \|(I-P)Ff\|_2^2=\sum_ja_j^2(1-\chi_j^2).
\]

The two pieces are orthogonal, hence

\[
 \boxed{\|Ff-f\|_2^2=2\sum_ja_j^2(1-\chi_j).} \tag{4}
\]

After division by `sum a_j^2`, (4) is an exact scale-free leakage ledger.

## No fixed defect-ratio theorem is needed

`T-15301` shows that a real-zero approximation program may converge to

\[
 \zeta\!\left(\frac12-iz\right)\Phi(z)
\]

for any nonzero holomorphic auxiliary factor `Phi`. A normalized sequence of
repaired sources only needs a nonzero subsequential limit; it does not need a
preselected `h_0/h_4` coefficient ratio.

The 2026 localization-operator estimates showing that fixed modes before the
plunge have concentration eigenvalues exponentially close to one are therefore
sufficient inspiration for small Fourier defect. They need not be strengthened
to a ratio asymptotic merely to identify one exact limiting combination.

## Domain warning

The two linear constraints do not make an interval-truncated prolate
combination a Schwartz source. A production radical packet must use smooth
compact modes, apply `L-15301`, or prove enough boundary matching for the
declared form domain. Zero integral alone is not sufficient.

## Checker

`X-15301` recomputes (1)--(4) with exact rational arithmetic. It does not certify
that externally supplied functions really have the declared values, integrals,
orthonormality, or finite-Fourier eigenrelations.

## Status boundary

The finite algebra is exact. Concrete source regularity, CCM normalization, and
asymptotic convergence remain separate obligations.