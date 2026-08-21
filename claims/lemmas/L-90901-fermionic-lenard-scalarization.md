# L-90901 — Fermionic Lenard scalarization of the odd trace-class Weil hierarchy

Claim ID: `L-90901`  
Status: **PROPOSED COMPLETE ABSTRACT THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: the corrected odd-sector sine/Cauchy sandwich of PR #368, especially `L-90511/T-90506`; the trace-class interpretation of its scalar explicit-formula distribution  
RH status: **unproved**

## 1. Purpose

PR #368 reduces the pole-free odd Weil form to one scalar even distribution

\[
 m(\tau)=2\pi\mu(\tau)
 -2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
       \cos(\tau\log n),
\tag{L-90901.1}
\]

sandwiched by a universal positive sine/Cauchy regularizer.  This note computes the **entire Fredholm exterior hierarchy** of that operator as a family of scalar determinantal pairings.  The noncommutative prime-word expansion collapses to a signed fermionic gas with a manifestly nonnegative Lenard kernel.

Nothing below proves that the resulting scalar pairings are nonnegative.  Their all-order nonnegativity remains equivalent to RH, subject to the index theorem of PR #368.

## 2. The odd sandwich

Let \(\mathcal S:L^2(0,\infty)\to L^2(0,\infty)\) be the unitary sine transform

\[
 (\mathcal Sh)(\tau)=\sqrt{\frac2\pi}
 \int_0^\infty h(x)\sin(\tau x)\,dx.
\]

For \(a,c>0\), define

\[
 K_a=\mathcal S M_{e^{-ax}}\mathcal S^{-1},
 \qquad
 r_c(\tau)=\frac1{c^2+\tau^2},
 \qquad
 B_{a,c}=M_{r_c}K_a.
\tag{L-90901.2}
\]

The integral kernel of \(K_a\) is

\[
 K_a(\tau,\sigma)
 =\frac a\pi\left[
 \frac1{a^2+(\tau-\sigma)^2}
 -\frac1{a^2+(\tau+\sigma)^2}
 \right]
 =\frac{4a\tau\sigma}
 {\pi[a^2+(\tau-\sigma)^2][a^2+(\tau+\sigma)^2]}.
\tag{L-90901.3}
\]

In particular

\[
 K_aK_b=K_{a+b}.
\tag{L-90901.4}
\]

On the common test core declared in PR #368, the corrected odd trace-class Weil operator is

\[
 A_{a,c}=B_{a,c}^*M_mB_{a,c}
 =K_aM_{r_c}M_mM_{r_c}K_a.
\tag{L-90901.5}
\]

The companion positive operator is

\[
 L_{a,c}:=B_{a,c}B_{a,c}^*
 =M_{r_c}K_{2a}M_{r_c}.
\tag{L-90901.6}
\]

Its kernel is

\[
 L_{a,c}(\tau,\sigma)
 =r_c(\tau)K_{2a}(\tau,\sigma)r_c(\sigma).
\tag{L-90901.7}
\]

## 3. Dense-range firewall

Multiplication by \(e^{-ax}\) is injective with dense range on \(L^2(0,\infty)\), so \(K_a\) is injective with dense range.  Multiplication by the strictly positive function \(r_c\) is likewise injective with dense range.  Therefore \(B_{a,c}\) has dense range.

Consequently, at the form-core scope of PR #368,

\[
 B_{a,c}^*M_mB_{a,c}\succeq0
 \quad\Longleftrightarrow\quad
 M_m\succeq0
 \text{ on the closure of the scalar form domain}.
\tag{L-90901.8}
\]

Thus no choice of \(a,c\) can create positivity by regularization: the Cauchy sandwich is a faithful compactification, not an arithmetic source of sign.

## 4. Fredholm expansion for a regular scalar

Let \(q\) be a bounded, compactly supported real function, and put

\[
 A_q=B_{a,c}^*M_qB_{a,c}.
\]

The cyclic determinant identity gives

\[
 \det(I+tA_q)
 =\det(I+tM_qL_{a,c}).
\tag{L-90901.9}
\]

For \(k\ge1\), define the Lenard density

\[
 \Delta_k(\tau_1,\dots,\tau_k)
 =\det\big[L_{a,c}(\tau_i,\tau_j)\big]_{i,j=1}^k.
\tag{L-90901.10}
\]

Since \(L_{a,c}\succeq0\),

\[
 \boxed{\Delta_k\ge0.}
\tag{L-90901.11}
\]

The Fredholm expansion yields

\[
 \boxed{
 \operatorname{tr}(\wedge^kA_q)
 =\frac1{k!}
 \int_{(0,\infty)^k}
 \Delta_k(\boldsymbol\tau)
 \prod_{j=1}^kq(\tau_j)\,d\boldsymbol\tau.
 }
\tag{L-90901.12}
\]

Equivalently,

\[
 \det(I+tA_q)
 =1+\sum_{k\ge1}\frac{t^k}{k!}
 \int\Delta_k\prod q.
\tag{L-90901.13}
\]

## 5. Manifest positivity of the Lenard kernel

By Andréief's identity and the sine representation of \(K_{2a}\),

\[
 \boxed{
 \begin{aligned}
 \Delta_k(\boldsymbol\tau)
 ={}&\left(\prod_{i=1}^k r_c(\tau_i)^2\right)
 \frac{(2/\pi)^k}{k!}\\
 &\times\int_{(0,\infty)^k}
 e^{-2a\sum_jx_j}
 \det[\sin(\tau_i x_j)]_{i,j=1}^k^2
 \,d\boldsymbol x.
 \end{aligned}}
\tag{L-90901.14}
\]

This makes the fermionic exclusion structure explicit: the kernel vanishes quadratically when two spectral coordinates collide.

## 6. Physical determinant representation

Define the scalar physical kernel

\[
 \mathcal M_c(x,y)
 =\left\langle m(\tau),
 r_c(\tau)^2\sin(\tau x)\sin(\tau y)
 \right\rangle.
\tag{L-90901.15}
\]

For regular \(q\), a second application of Andréief to (L-90901.12) gives

\[
 \boxed{
 k!\operatorname{tr}(\wedge^kA_q)
 =\left(\frac2\pi\right)^k
 \int_{(0,\infty)^k}
 e^{-2a\sum_jx_j}
 \det[\mathcal M_{c,q}(x_i,x_j)]_{i,j=1}^k
 \,d\boldsymbol x,
 }
\tag{L-90901.16}
\]

where \(\mathcal M_{c,q}\) is (L-90901.15) with \(m\) replaced by \(q\).

The prime part is completely explicit.  Put

\[
 J_c(u)=\int_0^\infty\frac{\cos(u\tau)}{(c^2+\tau^2)^2}\,d\tau
 =\frac\pi{4c^3}(1+c|u|)e^{-c|u|}.
\tag{L-90901.17}
\]

If

\[
 F_c(t)=2\pi\int_0^\infty
 \mu(\tau)r_c(\tau)^2\cos(t\tau)\,d\tau
 -\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \big[J_c(t-\log n)+J_c(t+\log n)\big],
\tag{L-90901.18}
\]

then

\[
 \boxed{
 \mathcal M_c(x,y)=\frac12\big[F_c(x-y)-F_c(x+y)\big].
 }
\tag{L-90901.19}
\]

Thus every exterior coefficient is a weighted determinant of one explicit Wiener--Hopf-minus-Hankel kernel.

## 7. Extension to the zeta distribution

Let \(q_R\) be any regularization for which

\[
 B_{a,c}^*M_{q_R}B_{a,c}\longrightarrow A_{a,c}
 \quad\text{in trace norm}.
\tag{L-90901.20}
\]

Trace-norm continuity of exterior powers implies that

\[
 \mathcal Z_k(a,c)
 :=k!\operatorname{tr}(\wedge^kA_{a,c})
 =\lim_{R\to\infty}
 \int\Delta_k\prod q_R
\tag{L-90901.21}
\]

exists and is independent of the regularization.  Equation (L-90901.21) is the canonical meaning of

\[
 \boxed{\mathcal Z_k(a,c)=\langle m^{\otimes k},\Delta_k\rangle.}
\tag{L-90901.22}
\]

The same limit gives the physical determinant formula (L-90901.16) for \(m\).

## 8. RH criterion

Subject to PR #368's proposed exact index theorem,

\[
 n_-(A_{a,c})
 =\#\{\text{reflected off-line zeta-zero pairs}\}.
\]

Therefore

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal Z_k(a,c)\ge0
 \quad\text{for every }k\ge1.
 }
\tag{L-90901.23}
\]

The forward implication is immediate from \(A_{a,c}\succeq0\).  Conversely, if \(A_{a,c}\) has a negative eigenvalue, \(\det(I+tA_{a,c})\) has a positive real zero, so not all of its Taylor coefficients can be nonnegative.

## 9. Interpretation and proof boundary

The hierarchy is an exact all-order nonlinear completion of the two-trace Zeta23 method:

```text
finite Gabor rank/Frobenius statistic
    -> full trace-class operator
    -> exterior powers
    -> nonnegative Lenard determinants
    -> scalar signed activity m.
```

It removes noncommutative prime-word bookkeeping, but it does not remove the arithmetic sign problem.  The remaining theorem is exactly

\[
 \langle m^{\otimes k},\Delta_k\rangle\ge0
 \quad(k=1,2,\ldots),
\]

or the equivalent physical determinant inequalities.  Proving these inequalities would prove RH.
