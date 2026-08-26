# R-106080 — Core-only centered phase packing does not transport the varying owner squareclass

Claim ID: `R-106080`  
Programme aliases: `LFAM1.OWNER_SQUARECLASS_TRANSPORT_FIREWALL`, `STRESS.SOURCE_TIED_PHASE_SELECTOR`, `LFAM2.MINIMUM_OWNER_SELF_AUDIT`  
Status: **PROVED EXACT SOURCE-KERNEL FIREWALL; `L-106082.3` AND THE `T-106080` CLOSURE ADAPTER ARE RETRACTED**  
Created: 2026-08-25  
Depends on: `L-102882--L-102883`; `R-102840`; `T-106030`; `R-106071`; `L-106080--L-106082`  
Programme issues: #743, #736, #737  
RH status: **unproved**

A source-level reconstruction of `T-106080` confirms the Boolean Vaughan
algebra and the minimum-owner geometry, but rejects the step which promotes
those facts to the complete coherent phase estimate.

The failure is not the inequality

\[
\lambda^2\le a.
\]

It is the attempted replacement of a source packet with varying owner
squareclass \(P=\lambda\Lambda\) and source-tied phase modulus by the
fixed-squareclass, modulus-independent coefficient sequence of `L-102883`.

## 1. What survives the reconstruction

On the finite squarefree Euler algebra, with disjoint-support convolution
\(\star\),

\[
\mu_{\rm sf}\star\mathbf 1_{\rm sf}=\varepsilon
\]

and therefore

\[
\mu_{\rm sf}
=2\mu_U-\mu_U\star\mu_U\star\mathbf1_{\rm sf}
+a_U\star a_U\star\mu_{\rm sf}.
\]

For \(1<n\le U\), every divisor is present in the truncated Boolean
convolution, so \(a_U(n)=0\); also \(a_U(1)=0\). Every nonzero balanced
representation consequently contains two disjoint nontrivial factors and at
least two distinct literal core primes.

For a fixed owner pair \(P\), after fixing Boolean Type-I factors \(d,e\), the
remaining lattice is

\[
\mathscr L_{K,\mathrm{sf}}^{(Pde)}(Z)
=
\sum_{\substack{k\ge1\\(k,Pde)=1}}
\frac{\mu(k)}{k^2}
\mathscr L_K^{(Pde)}(Z/k^4).
\]

The support of \(K_L\) gives \(k\le Z^{1/4}\). The parent
\(Z^{-1/2}\) zero-moment lattice estimate and the finite Euler exclusions give

\[
\mathscr L_{K,\mathrm{sf}}^{(Pde)}(Z)
\ll X^{o(1)}Z^{-1/4}.
\]

Hence, with the parent cutoff \(U=Y^{1/6}\) in the owner-quotient core
variable,

\[
\sum_{d,e\le U}\frac1{de}
\left|
\mathscr L_{K,\mathrm{sf}}^{(Pde)}
\left(\frac{Y}{d^2e^2}\right)
\right|
\ll
X^{o(1)}Y^{-1/4}
\left(\sum_{d\le U}d^{-1/2}\right)^2
\ll X^{o(1)}Y^{-1/12}.
\]

Thus the fixed-owner Boolean Type-I estimate is valid. The additional
squarefree and finite-Euler operators have only subpower norm relative to the
already-frozen parent Type-I owner ledger.

The minimum-owner rule also survives. Since it is applied before Vaughan
factorization and every balanced core prime is a nonowner, every such prime is
at least the smaller selected owner \(\lambda\). Two distinct core primes give

\[
\lambda^2\le a,
\qquad
B\le a<2B,\quad L\le\lambda<2L
\quad\Longrightarrow\quad
L^2<2B.
\]

These statements remain useful unconditional reductions.

## 2. The actual source-tied clean phase identity

After carrier, gauge, overlap and equal-product recombination, write one clean
balanced source atom as

\[
i=(\lambda_i,\Lambda_i,a_i,\xi_i),\qquad
n_i=P_i a_i^2,\qquad
P_i=\lambda_i\Lambda_i,
\]

where \(\xi_i\) denotes all retained representation, shell, marked-prime and
carrier labels. Its physical coefficient has the form

\[
\alpha_i
=
\frac{\gamma_i}{a_i\sqrt{\lambda_i\Lambda_i}},
\qquad
|\gamma_i|=X^{o(1)}.
\]

Let \(I_\ell\) be the atoms whose distinguished owner is \(\ell\). For a clean
cross term \(i\in I_\ell\), \(j\in I_\rho\), the four relevant labels are
distinct and

\[
\ell\mid n_i,\quad \ell\nmid n_j,
\qquad
\rho\mid n_j,\quad \rho\nmid n_i.
\]

Therefore

\[
1=
\sum_{h=1}^{\ell-1}
\sum_{k=1}^{\rho-1}
e_\ell(h(n_i-n_j))e_\rho(k(n_i-n_j)).
\]

Put

\[
\beta_i=\ell\alpha_i
=
\frac{\gamma_i}{a_i}\sqrt{\frac{\ell}{\Lambda_i}}.
\]

The clean Gram is exactly the source-selector bilinear form

\[
\boxed{
\begin{aligned}
\mathcal G_{\rm clean}
={}&
\sum_{\ell\ne\rho}
\frac1{\ell\rho}
\sum_{h=1}^{\ell-1}
\sum_{k=1}^{\rho-1}
\\
&\left\langle
\sum_{i\in I_\ell}
\beta_i e_\ell(hn_i)e_\rho(kn_i)v_i,
\;
\sum_{j\in I_\rho}
\beta_j e_\ell(hn_j)e_\rho(kn_j)v_j
\right\rangle .
\end{aligned}
}
\tag{R-106080.1}
\]

Here \(v_i\) is the complete physical logarithmic-observation vector. The
minimum-owner choice is helpful because
\(\sqrt{\ell/\Lambda_i}\le1\), but it does not remove the varying co-owner
\(\Lambda_i\), the varying squareclass \(P_i\), or the selector
\(i\in I_\ell\).

Equation (R-106080.1), rather than the fixed-sequence energy in `L-102883`, is
the conclusion-facing object.

## 3. The centered kernel is on the physical squareclasses, not only the cores

For a fixed phase prime \(q\), a source-faithful aggregated phase field is

\[
F_{q,h}
=
\sum_i c_i e_q(hP_i a_i^2)v_i.
\]

Exact orthogonality gives

\[
\boxed{
\frac1q\sum_{h=1}^{q-1}\|F_{q,h}\|^2
=
\sum_{i,j}
\langle c_iv_i,c_jv_j\rangle
\left(
\mathbf1_{q\mid P_i a_i^2-P_j a_j^2}
-\frac1q
\right).
}
\tag{R-106080.2}
\]

By contrast, `L-102883` applies to one common coefficient sequence with kernel

\[
\mathbf1_{q\mid a_i^2-a_j^2}-\frac1q.
\tag{R-106080.3}
\]

The two kernels are not equal when \(P_i\) varies. No same-family identity in
the modulus indices changes (R-106080.2) into (R-106080.3).

This mismatch is finite and exact. Choose units \(P,Q,a,b\pmod q\) such that

\[
Pa^2\equiv Qb^2\pmod q,
\qquad
a^2\not\equiv b^2\pmod q.
\]

For two equal Hilbert vectors, the physical-squareclass cross kernel in
(R-106080.2) is \(1-1/q\), whereas the core-only cross kernel in
(R-106080.3) is \(-1/q\). Reversing the two congruence conditions gives the
opposite mismatch. Consequently there is neither an identity nor a
source-independent one-sided domination.

For the actual minimum-owner clean pair with the same literal core
\(a_i=a_j\) and four distinct owners, the discrepancy is especially visible:

\[
\mathbf1_{\ell\mid n_i-n_j}=0,
\qquad
\mathbf1_{\rho\mid n_i-n_j}=0,
\]

while the core-only differences vanish. The source-tied and core-only
double-phase kernels therefore differ by factors of order \(\ell\rho\) after
normalization.

## 4. The Hilbert-coordinate trilemma

There are only three ways to try to hide the owner squareclass inside the
Hilbert coefficient \(v_a\) used by `L-102883`.

### A. Orthogonal owner coordinates

Put different \(P\)'s in an orthogonal direct sum. Then the norm is controlled
by the free owner energy \(\sum_P1/P\), but every cross-owner physical inner
product is deleted. Those deleted terms are exactly `BPOE103300`,
`HQORO106071`, and the open owner moment of `T-106030`.

### B. Physical owner aggregation

Put all \(P\)'s in the actual logarithmic-observation Hilbert space. Then the
cross-owner products are retained, but

\[
\left\|
\sum_P \frac1{\sqrt P}v_{P,a}
\right\|^2
\]

is itself the coherent owner-occupancy quantity. The bound
\(\|v_a\|\le X^{o(1)}\), required to invoke the square-core corollary of
`L-102883`, is not supplied by the minimum-owner inequality.

### C. Freeze \(P\) and apply `L-102883` separately

This is valid for each fixed squareclass. Recombining the fixed-\(P\) estimates
coherently is precisely the source-blind summation forbidden by `R-102840`;
the required replacement is the principal/nonprincipal owner-conductor moment
of `T-106030` or the quadratic owner-residue occupancy of `T-106071`.

Thus the sentence in `L-106082` that all co-owner and Boolean labels may be
retained in a Hilbert vector at only \(X^{o(1)}\) cost assumes the open theorem
it is meant to prove.

## 5. Why \(L^2<2B\) does not remove owner coherence

The inequality \(L^2<2B\) pays the conductor/core ratio for the distinguished
owner. It does not make all owner products \(P_i\) equal modulo the phase
prime, does not make the owner selectors independent of the moduli, and does
not bound the coherent sum over co-owners.

A literal family already exists inside the Boolean balanced support. Choose a
core \(a=uv\) with two primes \(u,v>U\), and choose many owner pairs
\((\lambda,\Lambda)\) below \(\min(u,v)\). Then

\[
a_U(u)a_U(v)\mu(1)\ne0,
\]

the minimum-owner rule selects \((\lambda,\Lambda)\), and every atom satisfies
\(\lambda^2\le a\). Nevertheless the physical residues
\(\lambda\Lambda a^2\) vary with the owner pair. The long-core inequality does
not collapse this family to the fixed-squareclass packet of `L-102883`.

## 6. Binding consequence

The abstract identity

\[
\sum_{\substack{\ell,\rho\in\mathcal P\\\ell\ne\rho}}
A_\ell(d)A_\rho(d)
=
K_{\mathcal P}(d)^2-\sum_{\ell\in\mathcal P}A_\ell(d)^2
\]

is correct. What fails is its promotion to the complete minimum-owner source
without first proving the selector- and squareclass-dependent estimate
(R-106080.1).

Therefore:

```text
L-106080 Boolean source identity                         RETAINED
fixed-owner Boolean Type-I estimate                      RETAINED
L-106081 minimum-owner geometry                          RETAINED
L-106082.2 abstract same-family identity                 RETAINED
L-106082.3 complete-source transport                     NOT PROVED
L-106082.5 global balanced-field energy                  DOES NOT FOLLOW
T-106080 full RH composition                             RETRACTED
Riemann Hypothesis                                       UNPROVED
```

The corrected remaining theorem is stated in `T-106081`.
