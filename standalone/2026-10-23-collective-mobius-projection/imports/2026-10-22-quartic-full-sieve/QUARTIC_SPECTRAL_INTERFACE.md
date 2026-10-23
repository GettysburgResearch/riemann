# Quartic spectral interface: exact identities and the remaining estimate

Status: research interface with proved local/archimedean identities and explicitly unproved global estimates. No new zero-free boundary is established or numerically proposed here.

Scope: the angular ±1 quartic Gauss-series route over the Gaussian field. The arithmetic target is the full squarefree-modulus, punctured, signed inverse norm. An unpunctured positive numerator mean does not suffice.

Primary sources inspected: David--Dunn--Hamieh--Lin, *Quartic Gauss sums over primes and metaplectic theta functions*, arXiv:2306.11875v4, especially (3.4)--(3.12), (4.4)--(4.7), (4.25)--(4.28), and Proposition 4.3; de Faveri--Dunn--Hoffstein, *Non-orthogonality of the cubic and quartic large sieves via Rankin--Selberg*, arXiv:2607.07911v2, especially §§4--5 and Proposition 8.1. The latter numerator mean is not silently promoted to the primitive inverse norm.

What was actually done: exact differentiation of the DDHL archimedean integral; exact Bessel Wronskian reconstruction; prime-by-prime decomposition of primitive bottom rows for an ordinary Eisenstein level identity; checking finite-dimensional evaluation normalization. No spectral remainder estimate for the full arithmetic target was proved.

Smallest remaining gap: a uniform estimate for the low-divisor, two-column squarefree projection, with its exact diagonal, all cross terms, common profiles, and finite-level evaluation cost retained. Section 7 specifies this interface.

Arithmetic normalization: the companion `CORRECTED_QUARTIC_CODEC.md` proves, in the DDHL v4 convention and for every odd primary Gaussian integer c,

\[
 \widetilde g_4(c)^2=\mu_F(c)\alpha(c),\qquad
 \alpha(c)=c/|c|,
\]

and hence

\[
 \mu_F(c)\widetilde g_4(c)
     =\alpha(c)\overline{\widetilde g_4(c)},\qquad
 \mu_F(c)\overline{\widetilde g_4(c)}
     =\alpha(c)^{-1}\widetilde g_4(c).
\]

These identities include nonsquarefree c, where both sides vanish. The proof evaluates the self-symbol in DDHL v4 (3.11); dropping that symbol prematurely would introduce an incorrect extra finite ray factor. The conversion therefore has precisely the angular factors alpha^{±1}. Any separate ray factors already present in the original Poisson formula remain part of the arithmetic target. The archimedean identities below use this corrected normalization.

## 1. The angular-one archimedean matrix

Use the additive character convention in DDHL: for a complex number z, checke(z)=exp(2 pi i (z+bar z)). Their angular-one Jacquet matrix is

\[
 K(u,s,1)=\int_{\mathbb C}(1+|z|^2)^{-s-1/2}
       \begin{pmatrix}\bar z&1\\-1&z\end{pmatrix}
       \check e(-uz)\,dx\,dy.                    \tag{1}
\]

Initially this integral is taken in an absolutely convergent half-plane; the identities below then continue meromorphically. Put

\[
 r=|u|>0,\quad R=4\pi r,\quad
 C_s=\frac{(2\pi)^{s+1/2}}{\Gamma(s+1/2)},\quad
 \nu=s-\frac32.
\]

Directly from (1),

\[
 \boxed{K(u,s,1)=C_sr^{s-1/2}
 \begin{pmatrix}
 -i(u/r)K_\nu(R)&K_{\nu+1}(R)\\
 -K_{\nu+1}(R)&-i(\bar u/r)K_\nu(R)
 \end{pmatrix}.}                                \tag{2}
\]

Here the scalar K on the right is the modified Bessel function. To verify every sign and order, let

\[
 F_a(u)=\int_{\mathbb C}(1+|z|^2)^{-a}\check e(-uz)\,dx\,dy
       =\frac{(2\pi)^a}{\Gamma(a)}r^{a-1}K_{a-1}(4\pi r).
\]

Since the phase is exp(-4 pi i (u_1 x-u_2 y)), the integral with bar z inserted equals

\[
 -\frac{1}{4\pi i}(\partial_{u_1}+i\partial_{u_2})F_a
 =\frac{i}{4\pi}\frac{u}{r}F_a'(r).
\]

The identity

\[
 \frac{d}{dr}\{r^{a-1}K_{a-1}(4\pi r)\}
       =-4\pi r^{a-1}K_{a-2}(4\pi r)
\]

gives the first diagonal entry. The other uses the conjugate angular phase. The two off-diagonal entries are F_a and -F_a. Substituting a=s+1/2 proves (2).

At u=0, rotational symmetry makes both diagonal entries zero and a polar integral gives

\[
 K(0,s,1)=\frac{\pi}{s-1/2}
          \begin{pmatrix}0&1\\-1&0\end{pmatrix}. \tag{3}
\]

Thus the angular-one constant-term matrix is off-diagonal. This has consequences for the appropriate Maass--Selberg pairing, but it does not permit dropping a cross term in an arbitrary mixture of input columns.

## 2. Exact analytic reconstruction without division by a K-Bessel function

The modified-Bessel Wronskian and derivative recurrences give

\[
 \boxed{R\{I_{\nu+1}(R)K_\nu(R)
             +I_\nu(R)K_{\nu+1}(R)\}=1.}          \tag{4}
\]

One proof starts from I_nu' K_nu-I_nu K_nu'=1/R and substitutes

\[
 I_\nu'=I_{\nu+1}+\frac\nu R I_\nu,\qquad
 K_\nu'=-K_{\nu+1}+\frac\nu R K_\nu.
\]

Consequently, if K_11 and K_12 denote the first-row entries in (2),

\[
 A(u,s)K_{11}(u,s,1)+B(u,s)K_{12}(u,s,1)=1,        \tag{5}
\]

where

\[
 A(u,s)=\frac{i(\bar u/r)R I_{\nu+1}(R)}{C_sr^{s-1/2}},
 \qquad
 B(u,s)=\frac{R I_\nu(R)}{C_sr^{s-1/2}}.           \tag{6}
\]

There is no division by K_it(R). Thus its real-order zeros do not obstruct (5).

For r in a fixed compact subinterval of (0,infinity), A and B are holomorphic for Re s>-1/2 and have polynomial growth on every closed vertical strip in that region, as do any fixed number of logarithmic r derivatives. This can be checked without an asymptotic expansion. The power series for I gives

\[
 \Gamma(s+1/2)I_{s-1/2}(R)
  =(R/2)^{s-1/2}
    \sum_{j\ge0}\frac{(R^2/4)^j}{j!\,(s+1/2)_j}, \tag{7}
\]

and

\[
 \Gamma(s+1/2)I_{s-3/2}(R)
  =(R/2)^{s-3/2}
   \left\{s-\frac12+\sum_{j\ge1}
       \frac{(R^2/4)^j}{j!\,(s+1/2)_{j-1}}\right\}. \tag{8}
\]

On Re s at least -1/2+delta, every denominator in (7)--(8) is bounded below by the corresponding positive real rising factorial. The sums and their fixed R derivatives are bounded on compact R intervals. The one displayed linear term costs O(1+|s|). This proves the asserted strip bounds. Poles of Gamma to the left of this domain are not silently crossed.

DDHL's arithmetic Fourier coefficient matrix phi(s,k,1) is diagonal. Therefore the same scalar entry phi_11 occurs in both first-row Fourier coefficients phi_11 K_11 and phi_11 K_12. Formula (5) is a genuine exact reconstruction of that scalar entry from two entries of the matrix Fourier expansion.

### 2.1 What this reconstruction does not yet prove

For rows Nk comparable to K, take y=K^{-1/2}. Then u is a fixed nonzero multiple of ky, so r remains in a compact annulus. If the desired Mellin factor is D^{s-1}, multiplying a Fourier coefficient by y^{s-2}D^{s-1} writes it as

\[
 y^{-1}(Dy)^{s-1}=y^{-1}L^{s-1},\qquad L=D/\sqrt K. \tag{9}
\]

This is the expected wavepacket scale. The exact multipliers (6), however, depend on the actual row radius and angular phase. They must remain in the reconstruction. They may be separated with a common smooth transform only if its full cross terms and seminorms are retained.

Also, (5) combines two input columns of the matrix Eisenstein series. The vanishing of a reflected self-pairing for one fixed angular input column does not imply vanishing for this mixture. A height-derivative variant of the Wronskian may be formulated in one inducing representation, but its covariant automorphic realization and exact scalar Fourier kernel have not been supplied here.

Replacing the reconstructed square by two unrelated positive norms can change the diagonal and erase the signed projector cancellation needed by the inverse problem. The identity (5) alone is therefore not a centered mean-square theorem.

## 3. An exact ordinary scalar level identity

This section concerns ordinary, nonmetaplectic Eisenstein series over the Gaussian integers. It is independent of the unproved arithmetic packet estimate.

For Re s>2, let E(w,s) be the level-one Eisenstein series represented by primitive bottom rows (c,b), with the conventional common unit quotient, and normalized incoming term y^s. Write w=(z,y). For a nonzero Gaussian integer r define

\[
 T_rw=(rz,|r|y).
\]

Let E_{p^a}(w,s) denote the same primitive-row sum with p^a dividing c. This is the cusp-infinity series for Gamma_0(p^a). For a good prime ideal with chosen generator p, put q=Np. Then

\[
 E(T_pw,s)=q^{s/2}E_p(w,s)
                 +q^{-s/2}\{E(w,s)-E_p(w,s)\}.    \tag{10}
\]

Indeed, replace the bottom row (c,b) of E(T_pw) by (pc,b). If p does not divide b, the new pair is primitive and has p dividing its first entry. If p divides b, primitivity forces p not to divide c; removing their common p leaves a primitive pair whose first entry is prime to p, with the displayed norm factor.

Similarly, partition the bottom rows of E(T_{p^2}w,s) by the valuation of b at p: zero, exactly one, or at least two. Removing the common p or p^2 gives

\[
 E(T_{p^2}w,s)
   =q^s E_{p^2}+(E_p-E_{p^2})+q^{-s}(E-E_p).      \tag{11}
\]

Substitution of (10) into (11) yields

\[
 \boxed{E_{p^2}(w,s)=
   \frac{E(T_{p^2}w,s)-q^{-s/2}E(T_pw,s)}{q^s-1}.} \tag{12}
\]

These are identities on the absolute convergence half-plane and hence throughout their common meromorphic continuation. Applying the decomposition independently at the primes of a squarefree d gives

\[
 \boxed{E_{d^2}(w,s)=(Nd)^{-s}
    \prod_{p\mid d}(1-(Np)^{-s})^{-1}
    \sum_{e\mid d}\mu(e)(Ne)^{-s/2}
            E(T_{d^2/e}w,s).}                    \tag{13}
\]

As a normalization check, the incoming y^s coefficient in (12) is exactly one. Its residue at s=2 is the level-one residue divided by q(q+1), the index of Gamma_0(p^2).

### 3.1 Fixed ray restrictions

The same calculation can be made before expanding finite ray data into characters. Let B be a fixed Gaussian modulus prime to p, and let E_b be the primitive-bottom-row sum restricted by c=0 mod B and second entry b mod B, with b a unit class. Collect these sums into a finite vector E. Dividing a row by p replaces b by bp^{-1}; let U_p be that permutation of the fixed finite vector.

The identical valuation partition now gives

\[
 \boxed{\boldsymbol E_{p^2}=
   (q^sI-U_p)^{-1}
   \{\boldsymbol E\circ T_{p^2}
                 -q^{-s/2}U_p(\boldsymbol E\circ T_p)\}.}        \tag{14}
\]

For example, the first-step identity is

\[
 (q^s I-U_p)\boldsymbol E_p
          =q^{s/2}(\boldsymbol E\circ T_p)-U_p\boldsymbol E.
\]

The p^2 identity follows by the same substitution as above. These permutation operators commute for distinct primes. Since U_p is unitary,

\[
 \|(q^sI-U_p)^{-1}\|\le(q^{\operatorname{Re}s}-1)^{-1}
 \quad(\operatorname{Re}s>0).                    \tag{15}
\]

Thus fixed ray restrictions add only a fixed finite vector and no growing-conductor ray character at this step. Formula (14) is stated for these exact ray-restricted primitive-row sums; it is not a replacement for the complete growing-level metaplectic scattering matrix.

## 4. A useful pointwise consequence and its limitation

Let Y(w) be the invariant height for the level-one Gaussian group, with a fixed lower truncation. For every nonzero integral r,

\[
 Y(T_rw)\le |r|Y(w).                              \tag{16}
\]

To prove this, a primitive pair (c,b) at T_rw produces (cr,b). Divide this pair by its Gaussian gcd g, obtaining a primitive pair (a,b_0). The corresponding height is

\[
 \frac{|r|}{Ng}\,
 \frac{y}{|az+b_0|^2+|a|^2y^2}\le |r|Y(w).
\]

Take the supremum over the original pair. Fixed base congruence data alter only the fixed finite set of height charts.

Suppose a fixed-base ordinary Eisenstein bound is available on Re s=u with 0<u<1:

\[
 |E(w,u+it)|\le C(1+|t|)^A Y(w)^{2-u}.            \tag{17}
\]

This is a premise in the following deduction. It can be obtained in an appropriate zero-free region from the fixed-base functional equation and corresponding scattering bounds; no new zero-free premise is proved here.

Substituting (16)--(17) into (13), with all finite ray components treated together if necessary, gives

\[
 \boxed{|E_{d^2}(w,u+it)|
    \ll_{u,\epsilon}(Nd)^{2-2u+\epsilon}
             (1+|t|)^A Y(w)^{2-u}.}              \tag{18}
\]

Indeed, the e summand has norm exponent

\[
 (Nd)^{-u}(Ne)^{-u/2}
       (Nd/\sqrt{Ne})^{2-u}
       =(Nd)^{2-2u}(Ne)^{-1}.
\]

Both the finite Euler correction and sum_{e|d}(Ne)^{-1} cost an arbitrarily small power of Nd. The vector resolvent bound (15) gives the same estimate for the fixed-ray version.

This is an individual ordinary-Eisenstein estimate. It does not prove that the aggregate low-divisor inverse error has the same power of R. The packets at different d have cross terms; their common-cover norms, evaluation functional, and exact diagonal must also be controlled.

## 5. Two wavepacket cautions

### 5.1 The incoming and outgoing scales are reciprocal

For a packet with phase L^{s-1}, a typical constant term has the two factors

\[
 y^sL^{s-1}=y(Ly)^{s-1},\qquad
 y^{2-s}L^{s-1}=y(L/y)^{s-1}.                     \tag{19}
\]

The incoming bump is at height comparable to 1/L and the outgoing bump at height comparable to L. A weighted norm must therefore allow both scales. A bound of the schematic form

\[
 \int |F_L|^2Y^{a}\ll (L+L^{-1})^a               \tag{20}
\]

is the natural target; L^a alone is not uniform when corrections produce L<1. Formula (20) itself requires a sufficiently holomorphic packet coefficient, uniform shifted decay, the appropriate scattering bounds, and control of the nonconstant cusp part. It is not assumed here for the complete arithmetic packet.

The direction of the contour shift matters. For large y/L the outgoing factor in (19) is made small by shifting s to the right. It is incorrect to infer an unavoidable outgoing slow cusp tail merely from zeros of a scattering denominator to the left of Re s=1. An earlier exploratory diagnosis in the working conversation used that wrong direction and is withdrawn.

The Wronskian multipliers in §2 supply holomorphy on useful fixed strips without dividing by a real-zero Bessel function. They do not alone settle all packet, cusp, or arithmetic-mask uniformity.

### 5.2 Single-column and mixed-column Maass--Selberg terms differ

The matrix (3) swaps the two angular input directions. Thus a statement that a fixed input column has no reflected self-pairing is compatible with a nonzero reflected pairing between different columns. The reconstruction (5) uses a mixture of two columns. Any norm calculation for that reconstruction must compute the resulting pairing with the actual coefficients A and B. No spherical formula or vanishing self-pairing may be substituted without that calculation.

## 6. The finite-cover evaluation normalization

Let V be functions on a finite coset space of size n, with Haar-normalized norm

\[
 \|v\|^2=\frac1n\sum_x|v(x)|^2.
\]

An old section v_d that is the indicator of a subset of relative density approximately (Nd)^{-2} then has norm squared of that order. This is the useful small section norm.

But evaluation at one coset x_0 has norm sqrt(n), not one. If P_{x_0} is the orthogonal rank-one projection onto that coordinate, then

\[
 |v(x_0)|^2=n\,\langle v,P_{x_0}v\rangle.         \tag{21}
\]

Using counting measure instead makes the projection formula have no n, but multiplies the old-section norm squared by n. One cannot simultaneously use the Haar-small section norm and a unit-norm evaluation functional for the actual scalar component.

This also distinguishes Hilbert--Schmidt unitarity from operator-norm control. Scattering is unitary on its natural finite-dimensional Hilbert space on the unitary axis. A unitary map of an endomorphism space with Hilbert--Schmidt norm need not preserve matrix operator norm. A proof based on an operator-valued Eisenstein series must state which norm is used throughout.

For a truncated squarefree sieve

\[
 v_R=\sum_{Nd\le R}\mu(d)v_d,
\]

the mutual Gram kernel is naturally of the scale N(lcm(d,e))^{-2}, so its Haar norm can remain bounded. Tensor products from one pair d,e factor through a level dividing lcm(d,e)^2, whose norm is at most R^4. This observation suggests projecting to the relevant finite-conductor subspaces before evaluating. It does not bound the norm of the projected evaluation functional. That bound, including any cancellation in the coefficients, remains necessary.

A compensating choice of sieve coefficients can remove the incoming value v_R(identity). It does not by itself control all other finite-coset evaluations or the complete pair kernel. No such compensation is used as an analytic estimate in this note.

## 7. The explicit unproved low-divisor requirement

Let K=D^2/H and L=D/sqrt(K). Begin with the actual signed quartic inverse Poisson expansion, including its squarefree-modulus projector, natural zeros, fixed puncture, diagonal/principal restoration, and common Fourier kernel. Resolve the squarefree condition by mu(d) over d^2 dividing the modulus.

For each R, the required estimate is for the **whole** truncated two-copy expression with Nd,Ne at most R. It must retain its cross terms and subtract or restore exactly the arithmetic diagonal prescribed by the original inverse identity. It is not enough to estimate each unpunctured numerator packet separately.

A useful target would be a bound of the form

\[
 |\mathcal C_{\le R}(H,D)-\mathcal D_{\le R}(H,D)|
 \ll (HD)^{\epsilon}\,K^{u/2}(L+L^{-1})^{2-u}\,
                   \mathcal A(R),                \tag{22}
\]

with all smooth seminorms specified, and with an explicitly proved growth rate for A(R) strong enough for the full consumer. Here D_{<=R} must be the actual arithmetic diagonal, not a limiting spectral norm chosen after the fact. At growing punctures, the finite Euler factors, their zeros, and their dependence on the rows must be retained. If an ordinary zero-free parameter u is used, its exact character family and conductor-uniform bounds must also be stated.

The companion `QUARTIC_PRIMITIVE_SIEVE_TAIL.md` now supplies a proved positive mean-square estimate for the large-divisor complement, including all local valuations and all nonzero Gaussian rows. In its notation, for a bounded profile W supported in a fixed interval [a,b] contained in (0,infinity), and any column weight xi(c) of modulus at most one that is independent of the row, put

\[
 T_R(k,D)=\sum_{c\ {\rm primary}}
       \frac{\xi(c)g_4(k,c)}{Nc}W(Nc/D)
       \sum_{\substack{d^2\mid c\\Nd>R}}\mu_F(d).
\]

For D,R,K at least one, that companion proves

\[
 \boxed{\sum_{0<Nk\le K}|T_R(k,D)|^2
       \ll_{\epsilon,W}(KD)^\epsilon
          \left(\frac K R+\frac{D^2}{R^4}\right).} \tag{23}
\]

Fixed ray and coprimality restrictions on the column may be incorporated in xi. The zero row is excluded and must be restored separately when the original inverse formula requires it. At K=D^2/H, the second term in (23) is at most K/R precisely when R^3 is at least H. Thus the simplified K/R estimate is available in that range; it must not be used uniformly for smaller R. The tail is exactly empty once R exceeds sqrt(bD), and also once R exceeds K, by its local row support.

Estimate (23) controls the complete positive square of this tail. It does not alone control its mixed pairing with the low-divisor part, or identify the centered arithmetic diagonal. For example, write a_k for an actual low-divisor amplitude and b_k=T_R(k,D). If J_low=sum |a_k|^2 and J_tail=sum |b_k|^2 over the same rows, then the elementary available bound is

\[
 \left|\sum_k|a_k+b_k|^2-\sum_k|a_k|^2\right|
       \le 2\sqrt{J_{\rm low}J_{\rm tail}}+J_{\rm tail}. \tag{24}
\]

Using (24) still requires a bound for J_low, or an independently justified substitute using a full norm; a desired bound for that total norm cannot be assumed to prove itself. Applying (23) after any common transform also requires retaining its profile dependence and the row-independent nature of its column weights. The arithmetic diagonal and principal or zero-row restorations must be accounted for in their original normalization.

The tail estimate (23) is established in the companion note. Estimate (22), its required A(R), and the necessary centered low-divisor and mixed-term control remain unproved. Consequently no zero-free constant follows from this note.

## References

- C. David, A. Dunn, A. Hamieh, H. Lin, [Quartic Gauss sums over primes and metaplectic theta functions](https://arxiv.org/html/2306.11875v4).
- A. de Faveri, A. Dunn, J. Hoffstein, [Non-orthogonality of the cubic and quartic large sieves via Rankin--Selberg](https://arxiv.org/html/2607.07911v2).
- NIST Digital Library of Mathematical Functions, [Modified Bessel Wronskians](https://dlmf.nist.gov/10.28) and [modified Bessel derivatives and recurrences](https://dlmf.nist.gov/10.29).
- Companion proof note `CORRECTED_QUARTIC_CODEC.md`, *Corrected quartic Gauss-square identity*: the DDHL v4 self-symbol evaluation and the exact angular coefficient conversion.
- Companion proof note `QUARTIC_PRIMITIVE_SIEVE_TAIL.md`, *A full all-row tail bound for the quartic primitive sieve*: the all-valuation estimate (23) and its exact support ranges.
