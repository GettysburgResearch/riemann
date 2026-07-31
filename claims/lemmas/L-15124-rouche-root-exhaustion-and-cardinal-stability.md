# L-15124 — Rouché root exhaustion and quantitative cardinal stability

Claim ID: `L-15124`  
Status: **PROVED ANALYTIC/FINITE LEMMA; COFINAL ROUCHÉ DATA OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: the integer-node finite CvS transform formula; `L-15122`; Rouché's theorem and the real symmetry of the finite transform  
Scope: a directed bridge from smooth-transform approximation to simple real target roots and selected-zero cardinal leakage  
Related counterexample candidates: none

## 1. Purpose

The phase-aware residue theorem `L-15123` requires:

1. all finite target roots to be simple and real;
2. a selected critical-line zero close to every target root;
3. quantitative control of the cardinal cross leakage.

This lemma proves that one directed Rouché ledger around exactly `2N` simple
critical-line zeros gives all three conclusions simultaneously.  In particular,
canonical Loewner inertia need not be certified separately on a level that
passes this stronger root-exhaustion gate.

## 2. Finite transform and scaling

Let the CCM interval length be `L>0`, the integer node set be

\[
 -N,-N+1,\ldots,N,
\]

and put

\[
 h=\frac{2\pi}{L}.
\]

Let

\[
 p=(p_{-N},\ldots,p_N)
\]

be a real even target vector with every coordinate nonzero, and let

\[
 P(s)=\sum_{n=-N}^{N}p_n
       \prod_{\substack{m=-N\\m\ne n}}^{N}(m-s)
 \tag{L-15124.1}
\]

be its degree-`2N` interpolation polynomial.

Let `F` be the compactly supported finite transform in the CvS convention,
normalized by a nonzero real scalar as desired.  The integer-node transform
formula implies:

- the non-skeleton zeros of `F` are exactly
  
  \[
  z=h u,
  \qquad P(u)=0;
  \tag{L-15124.2}
  \]
- the uncancelled skeleton zeros are
  
  \[
  z=hm,
  \qquad |m|>N.
  \tag{L-15124.3}
  \]

The nonzero-coordinate hypothesis makes the lattice singularities at
`|m|<=N` removable and nonzero.

Assume the normalization is chosen so that `F` is compared directly with
`Xi`.

## 3. Directed Rouché disks

Choose `2N` distinct simple proof-grade real zeros of `Xi`, indexed as

\[
 \gamma_1,\ldots,\gamma_{2N},
\]

and positive rational or directed radii `rho_k` such that the closed disks

\[
 D_k=\{z:|z-\gamma_k|\le\rho_k\}
 \tag{L-15124.4}
\]

are pairwise disjoint and each disk contains exactly the one simple `Xi` zero
at its center.

Require also that no disk meets the skeleton set (L-15124.3).  A sufficient
check is

\[
 \operatorname{dist}(D_k,h\mathbb Z\setminus[-hN,hN])>0.
 \tag{L-15124.5}
\]

Let

\[
 M_k=\min_{|z-\gamma_k|=\rho_k}|\Xi(z)|>0
 \tag{L-15124.6}
\]

and suppose a directed transform enclosure proves

\[
 \boxed{
 \sup_{|z-\gamma_k|=\rho_k}|F(z)-\Xi(z)|<M_k}
 \tag{L-15124.7}
\]

for every `k`.

Then every disk `D_k` contains exactly one zero of `F`, counted with
multiplicity.

### Proof

On the boundary of `D_k`, (L-15124.7) permits Rouché's theorem with the pair
`Xi` and `F-Xi`.  The two functions therefore have the same number of zeros in
the disk.  The certified simple-zero isolation says that number is one. QED.

## 4. Reality, simplicity, and exhaustion of the target roots

Every zero obtained in Part 3 is real.  Indeed, `F` is a real entire function,
so a nonreal zero would bring its conjugate.  The disk is invariant under
conjugation and contains only one zero counting multiplicity.

The zero is simple because its total multiplicity in the disk is one.  By the
skeleton exclusion (L-15124.5), it has the form

\[
 z_k=hu_k,
 \qquad P(u_k)=0.
\]

The disks are disjoint, so the `u_k` are distinct.  Since `P` has degree `2N`,
these roots exhaust it.  Therefore

\[
 \boxed{
 P\text{ has exactly }2N\text{ simple real roots}.}
 \tag{L-15124.8}
\]

Consequently the canonical Loewner matrix is positive semidefinite of corank
one by `L-15111`.

This conclusion uses no root finder and no midpoint inertia calculation.

## 5. Directed root-displacement bound

Assume, in addition, that a directed real-interval calculation gives

\[
 d_k=\inf_{x\in[\gamma_k-\rho_k,\gamma_k+\rho_k]}
      |\Xi'(x)|>0
 \tag{L-15124.9}
\]

and

\[
 \epsilon_k^F
 =\sup_{x\in[\gamma_k-\rho_k,\gamma_k+\rho_k]}
  |F(x)-\Xi(x)|.
 \tag{L-15124.10}
\]

Let `z_k` be the real zero of `F` in `D_k`.  Since `Xi'` is continuous and
nonzero on the real interval, its sign is constant there.  The mean-value
theorem gives

\[
 |\Xi(z_k)|\ge d_k|z_k-\gamma_k|.
\]

But `F(z_k)=0`, so

\[
 |\Xi(z_k)|=|\Xi(z_k)-F(z_k)|\le\epsilon_k^F.
\]

Hence

\[
 \boxed{
 |z_k-\gamma_k|
 \le\frac{\epsilon_k^F}{d_k}.}
 \tag{L-15124.11}
\]

In node coordinates, with

\[
 r_k=\frac{\gamma_k}{h}=\frac{L\gamma_k}{2\pi},
\]

one obtains

\[
 \boxed{
 |u_k-r_k|\le
 \delta_k:=\frac{\epsilon_k^F}{h d_k}.}
 \tag{L-15124.12}
\]

All quantities in (L-15124.12) admit directed finite enclosures.

## 6. Cardinal derivative bounds

Order the target roots according to their paired disks and let

\[
 \mathcal K_k(r)
 =\frac{\Omega(u_k)}{P'(u_k)}
   \frac{P(r)}{\Omega(r)(r-u_k)}
 \tag{L-15124.13}
\]

be the cardinal kernel of `L-15122`.  It satisfies

\[
 \mathcal K_k(u_k)=1,
 \qquad
 \mathcal K_k(u_l)=0\quad(l\ne k).
 \tag{L-15124.14}
\]

Put

\[
 J_l=[r_l-\delta_l,r_l+\delta_l]
 \tag{L-15124.15}
\]

and suppose directed arithmetic proves that every `J_l` avoids the finite nodes.
Define

\[
 \boxed{
 B_{kl}=\sup_{r\in J_l}|\mathcal K_k'(r)|.}
 \tag{L-15124.16}
\]

Then the mean-value theorem gives

\[
 \boxed{
 |\mathcal K_k(r_k)-1|\le B_{kk}\delta_k,}
 \tag{L-15124.17}
\]

and, for `l!=k`,

\[
 \boxed{
 |\mathcal K_k(r_l)|\le B_{kl}\delta_l.}
 \tag{L-15124.18}
\]

The derivative is a rational function whose numerator and denominator are
explicit in `P`, `P'`, `Omega`, and `Omega'`; interval evaluation on each
node-free `J_l` is therefore finite and directed.

## 7. Complete selected-zero leakage bound

Let the paired certified zeros carry positive masses `A_l` from `L-15122`.
Then the capture quantities of `L-15123` obey

\[
 \boxed{
 \varepsilon_k\le B_{kk}\delta_k,}
 \tag{L-15124.19}
\]

and

\[
 \boxed{
 C_k^Z
 \le\sum_{l\ne k}A_lB_{kl}\delta_l.}
 \tag{L-15124.20}
\]

Consequently the zero-boundary-scalar residue is strictly positive whenever

\[
 \boxed{
 A_kB_{kk}\delta_k
 +\sum_{l\ne k}A_lB_{kl}\delta_l
 +E_k
 <A_k
 \qquad(1\le k\le2N),}
 \tag{L-15124.21}
\]

where `E_k` is the complete directed prime-side residual-residue radius.

Equation (L-15124.21) simultaneously proves:

1. every target root is simple and real;
2. every exact arithmetic residue weight at `c=0` is positive;
3. the target-pinned arithmetic matrix is positive semidefinite with kernel
   exactly the target line.

## 8. Cofinal Rouché--cardinal condition

For a sequence of levels, a sufficient cofinal asymptotic is

\[
 \boxed{
 \max_k B_{j,kk}\delta_{j,k}
 +
 \max_k\frac{
   \sum_{l\ne k}A_{j,l}B_{j,kl}\delta_{j,l}
   +E_{j,k}}
  {A_{j,k}}
 \longrightarrow0.}
 \tag{L-15124.22}
\]

Here every level must use exactly `2N_j` disjoint simple certified line-zero
disks that avoid the skeleton and satisfy the directed Rouché inequalities.

This is a complete, quantitative version of the root-capture statement left
implicit in `T-15106`.

## 9. Gap audit

1. The requirement of `2N` isolated simple certified line zeros is load bearing.
   A repeated zeta zero needs a confluent version and does not give one simple
   target root by symmetry alone.
2. The selected disks must avoid the uncancelled finite-transform skeleton.
3. Local-uniform convergence by itself does not provide the simultaneous
   boundary moats for a growing set; every Rouché disk needs a directed budget.
4. The derivative constants `B_kl` can grow rapidly with dimension and root
   clustering.  Their cofinal control is part of the theorem, not a cosmetic
   conditioning issue.
5. The complete residual `E_k` must be produced from the full arithmetic source.
6. This lemma proves a finite and cofinal sufficient criterion.  It does not
   establish the criterion for the Riemann target sequence.