# Strip-multiplier firewall for powered inner Euler phase banks

**Status:** exact functional-analytic no-go.  
**RH status:** no conclusion.

## 1. The issue

The powered Q4 inner-bank proposal uses

\[
\Psi_{\omega,k}(z)=\phi_1(z)\phi_\omega(z)^k,
\qquad
\phi_\omega(z)={a-\omega e^{-Lz}\over1-a\omega e^{-Lz}},
\quad a=\tfrac12,
\]

with boundary modulus one on the critical line. A reflected off-line pair sees an eigenvalue whose magnitude grows exponentially in \(k\). Critical-line \(L^2\) conservation and a polynomial derivative gauge might suggest that this gain is free.

It is not free in any norm controlling off-line evaluation.

## 2. Universal RKHS multiplier bound

Let \(\mathcal H\) be a reproducing-kernel Hilbert space of analytic functions on \(\Omega\), and let \(F\) be a multiplier. For the reproducing kernel \(K_z\),

\[
M_F^*K_z=\overline{F(z)}K_z.
\]

Therefore

\[
\boxed{\|M_F\|_{\mathcal H\to\mathcal H}\ge|F(z)|\qquad(z\in\Omega).}
\tag{PB.1}
\]

For a bank \(F_1,\ldots,F_M\), define

\[
\mathcal Mf=M^{-1/2}(F_1f,\ldots,F_Mf)\in\mathcal H^{\oplus M}.
\]

Then

\[
\boxed{\|\mathcal M\|^2\ge{1\over M}\sum_{j=1}^M|F_j(z)|^2.}
\tag{PB.2}
\]

## 3. Application to the Xi-cardinal strip metric

The Xi-cardinal capture theorem uses the strip RKHS obtained from

\[
H_a=L^2(\mathbb R,e^{2a|u|}du),\qquad a>\tfrac12,
\]

whose transform kernel is

\[
\kappa_a(z,w)={4a\over4a^2+(z-\bar w)^2}.
\]

It contains evaluation at every centered zeta zero.

For \(\Re z>0\), \(|\phi_\omega(z)|<1\), while

\[
\phi_\omega(-\bar z)={1\over\overline{\phi_\omega(z)}}.
\]

Hence

\[
|\Psi_{\omega,k}(-\bar z)|
=|\phi_1(z)|^{-1}|\phi_\omega(z)|^{-k}.
\]

By (PB.1), whenever multiplication by \(\Psi_{\omega,k}\) acts on the strip space,

\[
\boxed{
\|M_{\Psi_{\omega,k}}\|
\ge|\phi_1(z)|^{-1}|\phi_\omega(z)|^{-k}.
}
\tag{PB.3}
\]

For a root-of-unity bank,

\[
\boxed{
\|\mathcal M_k\|^2
\ge|\phi_1(z)|^{-2}{1\over M}\sum_\omega|\phi_\omega(z)|^{-2k}.
}
\tag{PB.4}
\]

The right side grows exponentially whenever the phase radii are not all equal.

## 4. Consequence

The exact exponential negative reflected-pair eigenvalue is accompanied by an exponential operator norm in every native strip/form metric that can see that pair. Boundary \(L^2\) unitarity does not control this norm.

In the causal coefficient picture the same cost is exponentially growing weighted impulse-response mass. A finite-delay truncation preserving the off-line evaluation must preserve that weighted mass; ordinary unweighted \(\ell^2\) energy can remain one while the off-line/strip norm grows exponentially.

Thus the following inference is invalid:

```text
critical-line norm = 1
+ deterministic derivative gauge = O(k^2)
+ positive averaged row reserve
=> complete arithmetic/form block is subexponential in k.
```

The missing subexponential estimate is already an RH-equivalent assertion strong enough to contradict (PB.4) under a hypothetical off-line zero.

## 5. Dichotomy

1. **One common Weil form, coherent channels.** The coefficient-space coisometry theorem applies; the nonzero spectrum does not amplify.
2. **Separate Euler systems/source-resolved channels.** The channels are no longer a cost-free common compression; the strip/form multiplier norm and the complete source/collar metric carry the exponential factor.

This does not refute the powered phase-bank criterion. It locates its exact conclusion-producing step and prevents boundary unitarity and polynomial gauge bounds from being mistaken for that step.
