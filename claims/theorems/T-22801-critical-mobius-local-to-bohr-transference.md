# T-22801 — Critical Möbius local-to-Bohr transference

Claim ID: `T-22801`  
Title: The complete analytic-totient packet has physical critical energy bounded by its positive Jordan Bohr energy up to a subpower factor  
Status: **PROPOSED FULL-PROOF STEP PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-20`  
Created: 2026-08-07  
Issue: #228  
Dependencies: `L-22801`; elementary Farey determinant counting, Jordan divisor factorization, and the bandlimited majorant in `L-22801`  
Scope: the sole new RH-bearing estimate in the proposed proof

## 1. Statement

For `D>=2`, let `mathscr C_D` and `mathcal B_D` be the completed packet and Bohr energy of `L-22801`. Then, for every `epsilon>0`,

\[
\boxed{
\int_{D/2}^{D}|\mathscr C_D(x)|^2dx
\ll_\varepsilon
D^{1+\varepsilon}\bigl(1+\mathcal B_D\bigr).}
\tag{T-22801.1}
\]

Since `mathcal B_D<<D`,

\[
\boxed{
\int_{D/2}^{D}|E^{\rm AN}(x)|^2dx
\ll_\varepsilon D^{2+\varepsilon}.}
\tag{T-22801.2}
\]

The theorem is scale-critical: the physical interval has length comparable with the denominator cutoff, while distinct Farey frequencies may be only `D^-2` apart. The gain over the phase-blind large sieve comes from the exact Möbius divisor coordinates and the completed endpoint channel.

## 2. The Farey cluster operators

For `r=1,2`, define

\[
\mathcal R_{D,r}(k,q)
=\sum_{\substack{a\ne0,(a,q)=1\\a/q\in I_{D,k}}}
 {q^r\over a^r\sqrt{J_{2r}(q)}}.
\tag{T-22801.3}
\]

For `x=(x_q)_(q<=D)`, put

\[
(\mathcal R_{D,r}x)_k
=\sum_{q\le D}\mathcal R_{D,r}(k,q)x_q.
\tag{T-22801.4}
\]

The two pieces of the reduced coefficient formula are obtained by taking

\[
x_q^{(1)}={\sqrt{J_2(q)}\over2\pi}U_q(D),
\qquad
x_q^{(2)}={\sqrt{J_4(q)}\over2\pi^2}V_q(D),
\tag{T-22801.5}
\]

and inserting the factor `i` in the first channel. Their squared coefficient norms are exactly the two positive summands of `mathcal B_D`.

The low-frequency rows must be completed by the polynomial endpoint channel `P_D`. Denote the resulting augmented operators by

\[
\widetilde{\mathcal R}_{D,r}.
\tag{T-22801.6}
\]

Concretely, the augmentation replaces the `k=0` and two adjacent rows by the exact Fourier action of

\[
1+M_D/3+x^2R_D
\]

on the majorant `W(x/D)`. Two integrations by parts and

\[
\sum_{d\le x}\mu(d)\lfloor x/d\rfloor=1
\]

show that no free `M_D` or `R_D` term remains.

The load-bearing estimate is

\[
\boxed{
\|\widetilde{\mathcal R}_{D,r}x\|_{\ell^2(\mathbb Z)}^2
\ll_\varepsilon
D^\varepsilon\|x\|_{\ell^2(\{1,\ldots,D\})}^2,
\qquad r=1,2.}
\tag{T-22801.7}
\]

## 3. Farey determinant lemma

We prove (T-22801.7). Expanding the Gram matrix reduces it to pairs of reduced fractions `a/q`, `a'/q'` which lie in the same or adjacent critical cells. Such a pair satisfies

\[
\left|{a\over q}-{a'\over q'}\right|\le{2\over D},
\]

and therefore its integer Farey determinant obeys

\[
\boxed{|aq'-a'q|\le{2qq'\over D}.}
\tag{T-22801.8}
\]

Put `g=(q,q')`, `q=gQ`, `q'=gQ'`, with `(Q,Q')=1`. For a fixed nonzero determinant `Delta`, the equation

\[
aQ'-a'Q=\Delta/g
\tag{T-22801.9}
\]

has either no solutions or one affine family

\[
a=a_0+Qn,
\qquad
a'=a'_0+Q'n.
\tag{T-22801.10}
\]

The common-cell condition restricts `n` to one interval. Summing the weights `|a|^-r|a'|^-r` along that interval and then summing the admissible determinants gives

\[
\boxed{
\left|
(\mathcal R_{D,r}^*\mathcal R_{D,r})(q,q')
\right|
\ll_\varepsilon
D^\varepsilon
{(q,q')^{2r}\over
 \sqrt{J_{2r}(q)J_{2r}(q')}}
{1\over[qq']^r}.}
\tag{T-22801.11}
\]

Here `[q q']` denotes the least common multiple. The same estimate holds for the two adjacent-cell couplings. The determinant-zero contribution is the diagonal reduced fraction and is bounded by the same right side.

### Arithmetic summation of the determinant kernel

Jordan's identity

\[
(q,q')^{2r}=\sum_{\ell\mid q,\ell\mid q'}J_{2r}(\ell)
\tag{T-22801.12}
\]

factorizes the gcd kernel into divisor incidence matrices. Writing `q=ell*m`, `q'=ell*n`, the lcm denominator in (T-22801.11) contributes `ell^r[mn]^r`. The elementary divisor-Hilbert estimate

\[
\sum_{m,n\le X}
 {u_m\overline{u_n}\over[mn]^r}
\ll_\varepsilon
X^\varepsilon\sum_{m\le X}|u_m|^2
\qquad(r=1,2)
\tag{T-22801.13}
\]

follows by expanding `[mn]^-r=(m,n)^r/(mn)^r`, applying Jordan's identity once more, and using

\[
\sum_{d\mid n}1\ll_\varepsilon n^\varepsilon.
\tag{T-22801.14}
\]

Substitution into (T-22801.11) proves the operator estimate away from the completed low rows.

### Endpoint completion

For the low rows, retain the finite Fourier cutoff `|h|<=H`, combine them with `P_D`, and integrate twice by parts against `W(x/D)`. The boundary terms are

\[
\sum_{d\le D}\mu(d)\lfloor x/d\rfloor-1
\]

and its first integrated moment, hence vanish by Möbius inversion. The remaining kernel has the same determinant form as (T-22801.11), with one additional factor `min(1,|Delta|D/(qq'))`; this only improves the determinant sum. Letting `H` tend to infinity by `L2` convergence gives (T-22801.7) for the augmented operator.

This endpoint step is the reason the theorem concerns `mathscr C_D`, not the truncated centered packet `S_D` alone.

## 4. From clusters to the physical interval

Use the majorant of `L-22801`:

\[
1_{[D/2,D]}(x)\le W(x/D).
\]

Because `hat W` is supported in `[-1,1]`, only equal and adjacent frequency cells interact. Positivity of the triangular Fourier kernel and the elementary inequality

\[
2|uv|\le|u|^2+|v|^2
\]

give

\[
\int_{\mathbb R}W(x/D)|\mathscr C_D(x)|^2dx
\ll
D\sum_k|\widetilde B_{D,k}|^2.
\tag{T-22801.15}
\]

Applying (T-22801.7) to the two channels in (T-22801.5), and using the exact Bohr identity (L-22801.10), yields

\[
\sum_k|\widetilde B_{D,k}|^2
\ll_\varepsilon
D^\varepsilon(1+\mathcal B_D).
\tag{T-22801.16}
\]

Equations (T-22801.15) and (T-22801.16) prove (T-22801.1).

## 5. Critical review hinge

The entire proposed proof of RH downstream of this theorem is formal. The only genuinely new arithmetic estimate is the uniform operator bound (T-22801.7), whose most vulnerable points are:

1. the determinant-kernel estimate (T-22801.11), including numerator ranges near zero;
2. the divisor-Hilbert estimate (T-22801.13) at `r=1`;
3. the endpoint completion which removes the `M_D` and `R_D` channels before the norm is taken;
4. passage from finite Fourier cutoff to the nonsmooth Bernoulli packet.

The theorem is published as **PROPOSED**, not as independently verified. A counterexample to any of these four steps invalidates the full proposed proof but does not affect the exact parent identities.

## 6. Proof boundary

No RH input, zero-free region, Mertens bound, prime-number theorem, or unproved cancellation estimate is invoked explicitly. The claimed gain is entirely the Möbius–Farey/Jordan operator contraction above.

The theorem should be reviewed independently before any public statement that RH has been proved.