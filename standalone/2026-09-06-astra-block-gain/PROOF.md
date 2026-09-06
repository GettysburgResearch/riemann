# Source-complete block gain, an exact parity split, and the unresolved lift

Status: proposed complete proofs of BG26.1–BG26.7; independent review required.
**The uniform source-complete gain BG26.G and RH are NOT proved.**
This is an author continuation of PR #805, not an independent acceptance.
The odd-detail problem solved below is a precisely identified relaxation;
its all-scale gain is never substituted for the original gain.

## 0. Frozen source and target

Use the real Hilbert space and literal integer dictionary of the parent:

\[
 \mathcal H=\ell^2(\mathbb N_{\ge1},[n(n+1)]^{-1}),\quad
 \chi(n)=1,\quad h_k(n)=\{n/k\},\quad h_1=0.
\]

Set \(f(0)=0\), \(B_N=\operatorname{span}(h_2,\ldots,h_N)\),
\(P_N=P_{B_N}\), \(g_N=P_N\chi\), \(r_N=\chi-g_N\), and
\(\delta_N=\|r_N\|^2\). These are **squared** distances. The source is
not a finite zero set or a fitted Gram. Its exact Gram and coupling are

\[
 G_{jk}=\sum_{n\ge1}\frac{\{n/j\}\{n/k\}}{n(n+1)},\qquad
 b_k=\frac{\log k}{k}.
\]

Every finite Gram is strictly positive definite, as proved by the explicit
Vasyunin dual in the parent. All displayed infinite sums defining these
finite matrices are absolutely convergent. The parent also proves

\[
 D_2f(n)=f(\lfloor n/2\rfloor),\quad
 \|D_2f\|^2=\tfrac12\|f\|^2,\quad
 D_2h_k=h_{2k}-h_2/k,
\]

and, for the full new block,

\[
 \Delta_N:=\delta_N-\delta_{2N}
 =z_N^TS_N^{-1}z_N=\|g_{2N}-g_N\|^2.
\]

The requested, still open, estimate is

\[
 \boxed{\mathrm{BG26.G}:\quad
 \exists c>0\ \exists j_0\ \forall j\ge j_0:\quad
 \Delta_{2^jN_0}\ge c\,\delta_{2^jN_0}^{\,2},}
\]

where \(N_0\ge2\) is fixed in advance. It implies RH: dividing by
\(\delta_N\delta_{2N}>0\) gives
\(1/\delta_{2N}-1/\delta_N\ge c\), so \(\delta_{2^jN_0}\to0\).
The classical integer Nyman–Beurling criterion then applies. This is a
sufficient quantitative target, not an assertion that RH alone proves this
particular rate of block gain. No finite experiment establishes it.

## 1. BG26.1 — a genuine source-complete lower bound

Let \(O_N=\operatorname{span}\{h_k:N<k\le2N,\ k\text{ odd}\}\), with
orthogonal projector \(P_{O_N}\), and define

\[
 I_N=\|P_ND_2^*r_N\|^2+\|P_{O_N}r_N\|^2.
\]

Then, for every integer \(N\ge2\),

\[
 \boxed{\Delta_N\ge\tfrac23 I_N,\qquad
 I_N=0\ \Longleftrightarrow\ \Delta_N=0.}                 \tag{1}
\]

**Proof.** Put \(u=g_{2N}-g_N\). Since \(D_2B_N,O_N\subset B_{2N}\),
\(P_ND_2^*r_{2N}=P_{O_N}r_{2N}=0\). Hence both terms of \(I_N\) may
replace \(r_N\) by \(u\). The norms of \(D_2^*\) and any orthogonal
projection are \(1/\sqrt2\) and at most one. Thus
\(I_N\le(1/2+1)\|u\|^2\), proving the inequality.

Every even new generator obeys \(h_{2j}=D_2h_j+h_2/j\). Therefore
\(B_{2N}=B_N+D_2B_N+O_N\). If \(I_N=0\), \(r_N\) is orthogonal to
all three spaces, hence to \(B_{2N}\), and \(u=0\). The converse follows
from the first paragraph. No independence between the two channels is
assumed. In particular odd composite and nonsquarefree generators, such as
9 and 15, are retained. ∎

This lower bound avoids a full Schur inverse. Write
\(z_k=\langle r_N,h_k\rangle\), and use exact zeros \(z_k=0\) for
\(k\le N\). Then

\[
 I_N=t^TG_N^{-1}t+v^TG_{O_N}^{-1}v,\quad
 t_j=z_{2j}\ (2\le j\le N),\quad
 v_k=z_k\ (N<k\le2N,\ k\text{ odd}).                    \tag{2}
\]

Indeed \(\langle r_N,D_2h_j\rangle=z_{2j}\), since
\(\langle r_N,h_2\rangle=0\); apply the finite projection formula.
An all-scale lower bound \(I_N\ge c_0\delta_N^2\) would prove BG26.G.
**That additional lower bound is not proved here.** Source completeness of
the two channels is a zero-detection statement, not a uniform frame bound
for this target.

## 2. BG26.2 — weighted arithmetic Haar decomposition

Define the coarse average and odd detail by

\[
 (Af)(j)=\frac{(j+1)f(2j)+j f(2j+1)}{2j+1},\qquad j\ge1,
\]

\[
 (Jf)(1)=f(1),\qquad (Jf)(n)=f(n)-f(n-1)\quad(n\ge3\text{ odd}).
\]

The detail space is
\(\mathcal K=\ell^2(\mathbb N_{\rm odd},(2n^2)^{-1})\). For every
\(f\in\mathcal H\),

\[
 \boxed{\|f\|^2=\tfrac12\|Af\|^2+\|Jf\|_{\mathcal K}^2.} \tag{3}
\]

The corresponding bilinear identity follows by polarization. Also
\(AD_2=I\), \(JD_2=0\), and \(D_2^*=A/2\).

**Proof.** The two weights at \(2j,2j+1\) sum to
\(1/[2j(j+1)]\); their product divided by their sum is
\(1/[2(2j+1)^2]\). The weighted two-variable variance identity therefore
gives their exact coarse and detail contribution in (3). Add the first
cell \(f(1)^2/2\) and sum nonnegative identities. This proves convergence
and boundedness of both maps as well. Conversely any coarse vector \(a\)
and detail vector \(d\) reconstruct

\[
 f(1)=d(1),\quad f(2j)=a(j)-\frac{j}{2j+1}d(2j+1),\quad
 f(2j+1)=a(j)+\frac{j+1}{2j+1}d(2j+1).
\]

Thus this is a full Hilbert-space decomposition, not a truncation. The
identities for \(D_2\) and its adjoint follow either from the formulas or
from the bilinear identity. ∎

For the actual dictionary, finite differences give exactly

\[
 Jh_k(n)=\frac1k-\mathbf1_{k\mid n}\quad(n\text{ odd}),\qquad
 J\chi=\mathbf1_{\{1\}},\quad A\chi=\chi.                \tag{4}
\]

At \(n=1\), (4) uses \(k\ge2\); for even \(k\) the divisibility term
vanishes on every odd cell. These endpoint and parity conventions matter.

## 3. BG26.3 — the detail Gram is an explicit Jordan-totient matrix

For integer \(M\ge1\), let \(\mathcal O_M=\{k\le M:k\text{ odd}\}\),
including 1, and set

\[
 H_1=2h_2,\qquad H_k=\frac2k h_2-h_k\ (k\ge3\text{ odd}),\qquad
 H_M(a)=\sum_{k\in\mathcal O_M}a_kH_k.
\]

By (4),

\[
 JH_M(a)(n)=\sum_{\substack{k\mid n\\k\in\mathcal O_M}}a_k.
\]

Let \(\mathsf Q_M\) be the Gram of these detail vectors. Then

\[
 (\mathsf Q_M)_{k\ell}
 =\frac{\pi^2}{16\operatorname{lcm}(k,\ell)^2}
 =\frac{\pi^2}{16}\frac{\gcd(k,\ell)^2}{k^2\ell^2}.        \tag{5}
\]

Define \(J_2(d)=d^2\prod_{p\mid d}(1-p^{-2})\). With
\(E_{kd}=\mathbf1_{d\mid k}\) on the divisor-closed set \(\mathcal O_M\),

\[
 \mathsf Q_M=\frac{\pi^2}{16}
 \operatorname{diag}(k^{-2})E\operatorname{diag}(J_2(d))
 E^T\operatorname{diag}(k^{-2}).                           \tag{6}
\]

**Proof.** Sum \(1/(2n^2)\) over the odd multiples of the lcm; the sum of
reciprocal squares of odd positive integers is \(\pi^2/8\). Unique
factorization gives \(\sum_{d\mid n}J_2(d)=n^2\), proving (6). The divisor
incidence matrix is unit triangular, with inverse
\((E^{-1})_{kd}=\mu(k/d)\mathbf1_{d\mid k}\). All diagonal factors in
(6) are positive, proving strict positive definiteness. ∎

The exact relaxed detail objective is

\[
 \mathscr D_M(a)=\|\mathbf1_{\{1\}}-JH_M(a)\|_{\mathcal K}^2
 =\frac12-a_1+a^T\mathsf Q_Ma.
\]

Its unique minimizer and minimum are

\[
 a^*_{k,M}=\frac8{\pi^2}k^2
 \sum_{\substack{\ell\le M,\ \ell\text{ odd}\\k\mid\ell}}
 \frac{\mu(\ell/k)\mu(\ell)}{J_2(\ell)},                  \tag{7}
\]

\[
 \boxed{e_M=\frac12-\frac4{\pi^2}
 \sum_{\substack{k\le M\\k\text{ odd}}}\frac{\mu(k)^2}{J_2(k)}
 =\frac4{\pi^2}\sum_{\substack{k>M\\k\text{ odd}}}
 \frac{\mu(k)^2}{J_2(k)}.}                                \tag{8}
\]

**Proof.** Solve \(\mathsf Q_Ma^*=\mathbf e_1/2\) using (6) and substitute
in the quadratic objective. The absolute Euler product

\[
 \sum_{k\text{ odd}}\frac{\mu(k)^2}{J_2(k)}
 =\prod_{p\text{ odd}}\left(1+\frac1{p^2-1}\right)=\frac{\pi^2}{8}
\]

proves the second expression. Its convergence is unconditional. ∎

For squarefree odd \(k\), (7) also equals

\[
 \frac8{\pi^2}\mu(k)\frac{k^2}{J_2(k)}
 \sum_{\substack{m\le M/k,\ m\text{ odd}\\(m,k)=1}}
 \frac{\mu(m)^2}{J_2(m)}.
\]

For nonsquarefree \(k\) it vanishes. Therefore
\(0\le\mu(k)a^*_{k,M}\le1\), and for each fixed odd \(\!k\),
\(a^*_{k,M}\to\mu(k)\). This convergence is of individual detail
coefficients, **not** convergence in the original norm.

## 4. BG26.4 — complete all-scale gain for the relaxation

For every integer \(M\ge1\),

\[
 e_M-e_{2M}=\frac4{\pi^2}
 \sum_{\substack{M<k\le2M\\k\text{ odd}}}\frac{\mu(k)^2}{J_2(k)}.
                                                               \tag{9}
\]

For every \(M\ge64\),

\[
 \boxed{e_M\le\frac1{2M},\qquad
 e_M-e_{2M}>\frac1{40M}\ge\frac{e_M}{20}.}                 \tag{10}
\]

**Proof.** Since \(J_2(k)/k^2\ge8/\pi^2\) for odd \(k\), (8) and
\(\sum_{k>M}k^{-2}\le1/M\) give the upper bound. There are at least
\((M-1)/2\) odd integers in \((M,2M]\). Any nonsquarefree one is divisible
by \(d^2\) for some odd \(3\le d\le\sqrt{2M}\). Such multiples have
spacing \(2d^2\), so the union bound excludes at most

\[
 \frac M2\sum_{d\ge3,\ d\text{ odd}}d^{-2}+\frac{\sqrt{2M}}2
 <\frac M8+\frac{\sqrt{2M}}2.
\]

Here \(\pi^2<10\) suffices. The surviving number is at least \(M/4\)
for \(M\ge64\): indeed
\(M/8-1/2\ge\sqrt{M/2}\), as follows on squaring from
\(M^2-40M+16\ge0\). Each surviving term in (9) is at least
\(1/(4M^2)\). Hence the gain is at least \(1/(4\pi^2M)>1/(40M)\).
No prime number theorem or zero information has been used. ∎

There is also a sharp asymptotic, with an explicit positive Euler product:

\[
 \beta=\frac12\prod_{p\text{ odd}}\left(1-\frac1{p(p+1)}\right),\quad
 e_M=\frac{4\beta}{\pi^2M}+O(M^{-5/4}),\quad
 \frac{e_M-e_{2M}}{e_M}\longrightarrow\frac12.             \tag{11}
\]

**Proof.** Put \(b(n)=\mathbf1_{n\text{ odd}}\mu(n)^2n^2/J_2(n)\) and
\(v=b*\mu\). At 2, \(v(2)=-1\) and \(v(2^r)=0\) for \(r\ge2\).
For odd primes,
\(v(p)=1/(p^2-1)\), \(v(p^2)=-p^2/(p^2-1)\), and higher powers vanish.
The Euler product proves \(H=\sum |v(n)|n^{-3/4}<\infty\), and
\(\sum v(n)/n=\beta>0\). Since \(b=1*v\), replacing
\(\lfloor x/d\rfloor\) by \(x/d\) and bounding the omitted tail yields

\[
 \left|\sum_{n\le x}b(n)-\beta x\right|\le2H x^{3/4}.
\]

Stieltjes partial summation then gives
\(\sum_{n>M}b(n)n^{-2}=\beta/M+O(M^{-5/4})\); inserting this into (8)
proves (11). This argument uses only absolute convergence and elementary
summation, not cancellation of the ordinary Möbius function. ∎

**Boundary:** \(e_M\) is not \(\delta_M\). Its small size and its
uniform fractional gain do not imply either property for \(\delta_M\).

## 5. BG26.5 — lossless recursion for the original full source

For every integer \(N\ge2\), every element of \(B_{2N}\) has a unique
representation

\[
 F=D_2v+H_{2N}(a),\qquad v\in B_N,\quad a\in\mathbb R^{\mathcal O_{2N}}.
                                                               \tag{12}
\]

Let \(T a=A H_{2N}(a)\) and \(R_N=I-P_N\). Then

\[
 \boxed{\delta_{2N}=\min_a\left\{
 \mathscr D_{2N}(a)+\frac12\|R_N(\chi-Ta)\|^2\right\}.}   \tag{13}
\]

**Proof.** For even generators use \(h_{2j}=D_2h_j+h_2/j\), while
\(h_k=H_1/k-H_k\) for odd \(k\ge3\). These identities span the whole
source. If (12) is zero, apply \(J\); its divisor-incidence values on
odd cells through \(2N\) force \(a=0\), then injectivity of \(D_2\)
forces \(v=0\). Formula (3) gives the objective before minimizing over
\(v\); its minimum is the coarse orthogonal projection, giving (13). ∎

Thus the extra term in (13) retains **all** coupling to the constrained
coarse arithmetic source. Taking it to be zero changes the problem to the
larger space \(D_2\mathcal H+\operatorname{span}(H_k:k\in\mathcal O_{2N})\).
The latter really is the detail relaxation, because any coarse target can
then be fitted exactly. In particular \(\delta_M\ge e_M\) for every
\(M\ge2\), but differences need not obey the same ordering.

The coarse source can also be read without any matrix inversion. For odd
\(k\ge1\), including \(H_1=2h_2\),

\[
 (AH_k)(j)=-\{2j/k\}+\frac{j}{2j+1}\mathbf1_{k\mid 2j+1}.
                                                               \tag{13a}
\]

For \(A_M(a)=\sum_{k\in\mathcal O_M}a_k/k\), the lifted source is exactly

\[
 H_M(a)(n)=\sum_{k\in\mathcal O_M}a_k\lfloor n/k\rfloor
                 -2A_M(a)\lfloor n/2\rfloor.              \tag{13b}
\]

Both follow by expanding the fractional parts in \(H_k\); for (13a) use
\(h_k(2j+1)-h_k(2j)=1/k-\mathbf1_{k\mid2j+1}\).
The explicit detail optimizer has the **signed** normalization

\[
 A_M(a^*)=\frac8{\pi^2}
 \sum_{\substack{\ell\le M\\\ell\text{ odd}}}
 \frac{\mu(\ell)\varphi(\ell)}{J_2(\ell)}.                \tag{13c}
\]

Indeed insert (7), exchange two finite sums, and use
\(\sum_{k\mid\ell}k\mu(\ell/k)=\varphi(\ell)\). The positive
\(\mu^2\) tail in (8) does not estimate this signed normalization or the
coarse correlations in (13). No such cancellation is assumed here.

Here is an explicit finite-matrix form of (13). Index \(i\) by odd
\(i\le2N\), set \(T_i=AH_i\), and define

\[
 F_{ij}=\langle H_i,H_j\rangle,\quad B_i=\langle\chi,H_i\rangle,\quad
 V_{ji}=\langle h_j,T_i\rangle\quad(2\le j\le N).
\]

Every entry comes from the **original** full Gram through index \(2N\):

\[
 V_{ji}=2\left(\langle h_{2j},H_i\rangle-
                    \langle h_2,H_i\rangle/j\right),
\]

\[
 C=2(F-\mathsf Q_{2N})-V^TG_N^{-1}V\succeq0,\qquad
 w=2B-\mathbf e_1-V^TG_N^{-1}b_N.
\]

In fact \(C_{ij}=\langle R_NT_i,R_NT_j\rangle\) and
\(w_i=\langle r_N,T_i\rangle\). Consequently, putting
\(M_N=\mathsf Q_{2N}+C/2\) and \(t=(\mathbf e_1+w)/2\),

\[
 \boxed{\delta_{2N}=\frac{1+\delta_N}{2}-t^TM_N^{-1}t.}    \tag{14}
\]

The matrix \(M_N\) is strictly positive definite. To verify the identities,
apply the bilinear form of (3) to \(D_2h_j,H_i\), to \(\chi,H_i\), and
to \(H_i,H_j\). Completing the finite quadratic square in (13) proves
(14). No inverse of an infinite compact operator occurs.

The explicit detail minimizer gives a legitimate full-source trial with
squared error

\[
 U_N=e_{2N}+\frac12\left(\delta_N-2w^Ta^*+(a^*)^TCa^*\right),\quad
 a^*=a^*_{\cdot,2N},\qquad \delta_{2N}\le U_N.             \tag{15}
\]

For completeness its exact adjustment to the true coupled minimizer is

\[
 \delta_{2N}=U_N-\frac14(w-Ca^*)^TM_N^{-1}(w-Ca^*).        \tag{16}
\]

Indeed translate \(a=a^*+x\) in (13), use
\(\mathsf Q_{2N}a^*=\mathbf e_1/2\), and complete the square. Thus the
correction is positive but its necessary magnitude is still arithmetic.

## 6. BG26.6 — the attempted detail-to-full transfer fails on the real source

The attached outward interval replay encloses the **infinite** Gram sums,
using the parent's periodic digamma formula and explicit analytic remainder.
It gives, at the fixed stage \(N=8\),

\[
 0.024244525306<\delta_8<0.024244525307,
 \qquad 0.025491663369<U_8<0.025491663370.
\]

Thus the exact optimizer of the entire odd-detail problem, even followed
by its best allowed old-coarse correction, performs **worse** than the old
optimum. This refutes \(U_N\le\delta_N\) for all \(N\); it does not
refute an eventual bound with additional hypotheses or BG26.G itself.
The full coupled optimization still gives

\[
 0.017936267020<\delta_{16}<0.017936267021.
\]

Let \(\kappa_M=\delta_M-e_M\ge0\). The exact gain identity is

\[
 \Delta_N=(e_N-e_{2N})+\kappa_N-\kappa_{2N}.              \tag{17}
\]

The same directed replay proves
\(\kappa_{16}-\kappa_8>0.0015\), so nonincreasing lifting penalty is
also false. The full coupled optimizer at \(M=16\) has

\[
 -0.105967221800<a_{9,16}^{\rm full}<-0.105967221797,
\]

whereas \(a^*_{9,16}=0\) exactly because \(\mu(9)=0\). Deleting
nonsquarefree coordinates is valid only for the solved detail relaxation;
it is not valid for the source-complete minimization.

These are conditional on review of the explicit interval implementation
and remainder proof, not proof-kernel-verified numerical theorems. The
verification object is rebuilt from the fractional-part dictionary and
contains no sampled or prescribed zero data.

## 7. BG26.7 — no source-blind bounded coarse lift

Even for the genuine odd generators \(h_k\), \(k\ge3\), there is no
constant \(C\) with \(\|h_k\|^2\le C\|Jh_k\|_{\mathcal K}^2\).
Precisely, with \(A_0=\pi^2/8\),

\[
 \|Jh_k\|_{\mathcal K}^2=\frac{A_0}{k^2}(1-1/k),\qquad
 \|h_k\|^2\ge\frac{k-\sum_{j=1}^k1/j}{k^2}\ge\frac1{3k}.
\]

Hence their squared-norm ratio is at least \(k/(3A_0)>4k/15\).
For the first equality expand (4) and sum over odd multiples of \(k\).
For the second use only the positive Gram summands \(1\le n<k\);
\(\sum_{j=1}^k1/j\le2k/3\) follows at \(k=3\) and by induction.
This proves the claim. It rules out a uniform ambient lifting estimate,
not a special estimate for the exact optimal residuals.

## 8. The attempted completion and the exact remaining obligation

Two attacks were carried out. The complete even-dilation/odd-birth frame
proves (1), but no lower bound \(I_N\ge c_0\delta_N^2\) is obtained.
The parity-divisor problem gives the explicit weights (7), the all-scale
rate (10), and asymptotic (11). Its direct lift fails at the actual stage
\(8\to16\); (17) identifies the missing coarse penalty. The full formula
(14) remains exact, with no omitted cross terms.

An explicit sufficient remaining theorem, stronger than BG26.G, is

\[
 \exists c_0>0\ \exists j_0\ \forall j\ge j_0:\quad
 t_N^TG_N^{-1}t_N+v_N^TG_{O_N}^{-1}v_N
 \ge c_0\delta_N^2,\quad N=2^jN_0,                       \tag{BG26.I}
\]

with the **actual residual correlations** of (2). Alternatively one must
control the coupled minimization in (13) directly. Neither assertion is
established by the determinant's positivity, the detail gain, coefficientwise
Möbius convergence, or the three bounded numerical stages.

The remaining task is not an unaudited tail in the bounded computation:
all infinite Gram tails used there are enclosed. It is the uniform
arithmetic coupling estimate. RH remains unproved.
