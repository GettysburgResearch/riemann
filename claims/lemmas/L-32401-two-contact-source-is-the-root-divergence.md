# L-32401 — The dyadic two-contact source is exactly the root divergence

Claim ID: `L-32401`  
Title: The source `(epsilon-delta_2)*mu` pairs every carry target with only the root node of its exact fragmentation divergence  
Status: **PROPOSED COMPLETE EXACT FINITE/TRANSFORM LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #272 `L-26205`, `L-27205`; elementary Dirichlet convolution  
Scope: exact source/carry/divergence identities and a Cycle-Debt lower bound; no sign estimate for the root scalar and no RH claim

## 1. The source

Let

\[
 b_2=(\varepsilon-\delta_2)*\mu,
\]

so

\[
 b_2(q)=\mu(q)-\mathbf1_{2\mid q}\mu(q/2)
\tag{L-32401.1}
\]

and

\[
 \sum_{q\ge1}{b_2(q)\over q^s}
 ={1-2^{-s}\over\zeta(s)}.
\tag{L-32401.2}
\]

Here `1` denotes the constant-one arithmetic function and `epsilon` the Dirichlet-convolution unit. Since `1*mu=epsilon`,

\[
\boxed{
 1*b_2=\varepsilon-\delta_2.
}
\tag{L-32401.3}
\]

## 2. Its floor potential is a point mass at the root

For an integer `n>=0`, define

\[
 H_2(n)=\sum_{q\le n}b_2(q)\left\lfloor{n\over q}\right\rfloor,
 \qquad H_2(0)=0.
\tag{L-32401.4}
\]

Interchanging the finite divisor sums and using (L-32401.3),

\[
 H_2(n)
 =\sum_{m\le n}(1*b_2)(m).
\]

Therefore

\[
\boxed{
 H_2(1)=1,
 \qquad
 H_2(n)=0\quad(n=0\text{ or }n\ge2).
}
\tag{L-32401.5}
\]

Thus `H_2` is literally the root-node indicator.

## 3. Pointwise carry profile

For a split `e=(n,j)`, put

\[
 \chi_e(q)
 =\left\lfloor{n\over q}\right\rfloor
 -\left\lfloor{j\over q}\right\rfloor
 -\left\lfloor{n-j\over q}\right\rfloor.
\]

Then

\[
\begin{aligned}
 Y_2(n,j)
 &:=\sum_qb_2(q)\chi_e(q)\\
 &=H_2(n)-H_2(j)-H_2(n-j).
\end{aligned}
\]

For `n>=2` this gives the exact two-contact law

\[
\boxed{
 Y_2(n,j)
 =-\mathbf1_{j=1}-\mathbf1_{n-j=1}.
}
\tag{L-32401.6}
\]

In particular all genuine interior carry positions are invisible to `b_2`; the only nonzero rows are the two unit-child contacts. At `n=2,j=1` the value is `-2`.

## 4. Pairing with an arbitrary exact target

Let `d=(d_e)` be any finite signed split flow with node divergence

\[
 r=\partial d
 =\sum_e d_e(e_n-e_j-e_{n-j})
\]

and carry loads

\[
 w(q)=\sum_e d_e\chi_e(q).
\]

Using (L-32401.6) and then the divergence pairing with `H_2`,

\[
\begin{aligned}
 \sum_qb_2(q)w(q)
 &=\sum_ed_eY_2(e)\\
 &=\sum_mr(m)H_2(m)\\
 &=r(1).
\end{aligned}
\]

Hence

\[
\boxed{
 \sum_qb_2(q)w(q)=r(1).
}
\tag{L-32401.7}
\]

The fixed-`q_0=2` Möbius scalar is therefore not merely a mutation of the fragmentation system: it is exactly its root divergence and is invariant under every Pascal cycle.

## 5. The critical target

For

\[
 w_X(q)=q^{-1/2}\log(X/q)\mathbf1_{q\le X},
\]

put

\[
 R(X)=\sum_{n\le X}{\mu(n)\over\sqrt n}\log{X\over n}.
\]

Then (L-32401.1) gives

\[
\boxed{
 \mathcal R_2(X)
 :=\sum_{q\le X}{b_2(q)\over\sqrt q}\log{X\over q}
 =R(X)-2^{-1/2}R(X/2).
}
\tag{L-32401.8}
\]

For the exact target divergence `r_X` of PR #272,

\[
\boxed{
 r_X(1)=\mathcal R_2(X).
}
\tag{L-32401.9}
\]

Thus the RH-bearing dyadic Riesz scalar and the root node of the exact carry problem are one object.

## 6. Mellin firewall and stable recovery

Initially for `Re z>1/2`,

\[
 \int_1^\infty R(X)X^{-z-1}dX
 ={1\over z^2\zeta(z+1/2)}.
\]

Therefore

\[
\boxed{
 \int_1^\infty\mathcal R_2(X)X^{-z-1}dX
 ={1-2^{-z-1/2}\over z^2\zeta(z+1/2)}.
}
\tag{L-32401.10}
\]

The numerator has no zero in `Re z>0`, so every zeta zero to the right of the critical line remains an uncancelled pole.

Conversely (L-32401.8) has the finite stable inverse

\[
\boxed{
 R(X)=\sum_{k\ge0\,:\,2^k\le X}
 2^{-k/2}\,\mathcal R_2(X/2^k).
}
\tag{L-32401.11}
\]

Hence `R` and `mathcal R_2` have the same subpower status. In particular a bound

\[
 \mathcal R_2(X)=O_\varepsilon(X^\varepsilon)
\]

for every `epsilon>0` gives the classical reciprocal-zeta Riesz bound and therefore RH.

## 7. Exact Cycle-Debt lower bound

Fix the balance parameter `eta` of PR #272. For an allowed split let

\[
 m_e=\mathbf1_{j=1}+\mathbf1_{n-j=1}=-Y_2(e).
\]

Only finitely many `eta`-balanced rows have `m_e>0`, because `eta n<=1` whenever a unit child occurs. Put

\[
 c_\eta
 =\min_{e:\,m_e>0}{\omega_e\over m_e}>0,
\tag{L-32401.12}
\]

where `omega_e` is the Cycle-Debt capacity of `L-27205`.

The potential

\[
 F(n)=-c_\eta H_2(n)
\]

has split defect

\[
 F(n)-F(j)-F(n-j)=c_\eta m_e
\]

and hence satisfies

\[
 0\le F(n)-F(j)-F(n-j)\le\omega_e.
\]

It is therefore an admissible dual potential in `L-27205`. The dual identity yields

\[
\boxed{
 \mathfrak N_\eta(X)
 \ge c_\eta\,[r_X(1)]_+
 =c_\eta\,[\mathcal R_2(X)]_+.
}
\tag{L-32401.13}
\]

This proves that the positive part of the two-contact Riesz scalar is a literal Cycle-Debt obstruction. No cycle optimization can remove it.

## 8. Consequence for the proof graph

The two apparently different surviving fronts

```text
fixed-q0=2 reciprocal-zeta scalar;
cycle-optimized balanced fragmentation debt
```

share the same irreducible coordinate: the root divergence.

A future constructive proof may contract every transverse boundary mode, but it must consume `r_X(1)` by a source-specific one-sided or Hermitian theorem. Hiding that coordinate inside an absolute boundary norm cannot prove RH.

## 9. Proof boundary

Closed exactly here:

- the two-contact carry profile;
- the root-divergence identity for every exact flow;
- the critical dyadic Riesz formula and stable inverse;
- the uncancelled Mellin pole;
- a concrete admissible Cycle-Debt dual potential and lower bound.

Open:

- an unconditional subpower or favorable one-sided bound for `r_X(1)`;
- a source-specific physical/Selberg consumer for that root coordinate;
- RH.
