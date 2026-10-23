# Exact local cube-frequency trace and the remaining weighted interface

23 October 2026. This is finite algebra, not an identification of the metaplectic packet with a finite-cover trace. In particular it does not remove the centered-moment gap in the physical quartic problem.

Let O be an unramified local discrete valuation ring of odd residue size q, with residue characteristic different from 3. Put A=O/p^2 and X=P^1(A), so |X|=q^2+q. The right action of n(t)=[[1,t],[0,1]], t in A, on primitive bottom rows has exactly the following orbits:

* The q^2 points [1:x], x in A, form one regular translation orbit.
* The q points [p y:1], y in O/p, are fixed, since (p y)^2=0 in A.

Use the Haar-normalized inner product on functions on X. For a in A, let P_a be the orthogonal Fourier projector for a fixed perfect additive pairing on A. Then P_0 has dimension q+1, and every P_a with a nonzero has dimension one. This follows directly by decomposing the regular orbit and the q fixed points.

## Cube sampling is not uniform frequency sampling

Define

\[
 T_{\rm cube}=q^{-2}\sum_{k\in A}P_{k^3}. \tag{F1}
\]

Exactly q residues k, namely those divisible by p, have k^3=0 in A. A nonzero nonunit is never a cube modulo p^2. Each unit cube has gcd(3,q-1) roots, by Hensel lifting and the finite-field unit group. Thus the eigenvalues of F1 are q^-1 on P_0, gcd(3,q-1)/q^2 on the unit-cube frequency spaces, and zero on the remaining frequencies.

Deleting only k=0 changes the first eigenvalue to (q-1)/q^2. It does not remove the q fixed cosets. Deleting the whole frequency-zero space does remove them, but that is a different operation. In particular a global deletion of the physical zero row cannot by itself be identified with the local zero-frequency deletion: nonzero physical rows divisible by p still contribute.

If x is a fixed point and delta_x its indicator, its squared Haar norm is 1/(q^2+q), and

\[
 \langle\delta_x,T_{\rm cube}\delta_x\rangle
 ={1\over(q^2+q)q}. \tag{F2}
\]

At a point of the regular orbit the corresponding value is 1/[(q^2+q)q^2]. The fixed-coset contribution therefore carries an extra factor q compared with the regular orbit. Restricting to unit k eliminates it; however, the physical inverse contains nonunit rows and their local branches must then be restored.

The same assertions tensor over a squarefree level d. In particular the mass of cube frequency zero modulo d^2 is 1/Nd, rather than 1/(Nd)^2. Fixed bad primes may be treated separately; the assertion about at most three unit cube roots is not made at residue characteristic 3.

## The exact local Ramanujan cancellation

The first nonsquarefree modulus surviving in g_4(k^3,c) is p^4. Its normalized Ramanujan coefficient is

\[
 r_p(k)=1_{p^2\mid k}-q^{-1}1_{p\mid k}. \tag{F3}
\]

Uniform averaging over k modulo p^2 gives

\[
 \mathbb E r_p(k)=0,\qquad
 \mathbb E|r_p(k)|^2=q^{-2}-q^{-3}. \tag{F4}
\]

Consequently tensor products of these factors have an exactly diagonal Gram matrix under complete independent residue averaging: if r_d is the product over p|d, then E[r_d conjugate(r_e)]=0 for distinct squarefree d,e, and E|r_d|^2 is the product of q^-2(1-q^-1). This is a real signed cancellation; replacing both terms in F3 by separate positive bounds loses its zero mean.

It is not yet the required arithmetic Gram identity. The physical coefficient multiplying F3 is a sum of moving quartic characters in k. For a fixed puncture prime p outside those moduli, replacing k by p^a v multiplies each column by its own quartic value at p^a. Thus the two terms of F3 pair with differently twisted column vectors. A complete residue count K>=N(d e)^2 does not make those vectors constant on residue classes or independent of them.

Even at finite level, zero mean is not a weighted zero-mean identity: E[r_p(k) 1_(p^2|k)]=(1-q^-1)/q^2 is nonzero. This example does not refute cancellation for the actual metaplectic coefficients. It shows exactly why a proof must retain those coefficients when passing from F4 to a packet norm.

The remaining useful target is to derive the actual two-column Whittaker pairing and show that its weighting either preserves F4 or has a controlled nonprincipal remainder. The arithmetic diagonal must be identified in that derivation. Neither the ordinary-level outgoing-coefficient obstruction nor this finite calculation supplies that identification.
