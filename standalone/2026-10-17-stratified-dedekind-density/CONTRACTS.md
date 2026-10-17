# Exact analytic inputs and their verification boundary

Status: imported source contracts, NOT mathematical results certified by the
finite checker. These contracts are reported as unconditional in the cited
sources. Their use introduces no RH, GRH, native-moment conjecture, or signed
covariance assumption. However, the primary CT v2 body could not be freshly
retrieved in this session. Its contracts below are adopted from the complete
pinned #957 proof and its source map, cross-checked where possible against the
older #948 import. Independent primary-source verification remains required.
A proof from these contracts is not an independent reconstruction of CT.

## CT: unchanged general-field source

CT denotes Cureton--Thorner, Hexagon 2610.00200v2. The exact repository adapter
read in full is #957 at ec54cb6b0029aedd8a99e6016a42a1426a0223a2, file
standalone/2026-10-17-dedekind-density-upgrade/PROOF.md, blob
3bc7cf80bdbfe1dbba84081bd1e8096ccc13987f. In particular its Sections 2--6,
not just its proposed conclusion 23/24, supply the interfaces adopted here.

Fix F containing mu_12, d=[F:Q], the original finite S and its profiles.
Put R=O_(F,S), Gamma=(R*)^6. All norms below are exterior ideal norms. The
allowed generator of an exterior ideal a is g(a) modulo Gamma. It is
multiplicative, and is characterized by membership of its local sixth-power
class in CT's fixed subgroup B. The finite group R*/(R*)^6 is retained.
There is one principal Poisson class modulo Gamma; other classes give the
nonprincipal finite-order denominator characters specified below.

**CT-1: source and reflected bound.** The same three-scale arithmetic average
I(X,Y,Z), with the same source coefficients and fixed profiles, is available
for every fixed alpha,beta>0 with beta<=alpha and M=alpha+beta>1. With
X=Z^alpha, Y=Z^beta, its reflected squared moment on the full
powerful/squarefree dyad is

    P^(1/2) (D + D^2 P/Z) Z^epsilon,    PD << Z^M.

The additive squared norm is O(1/Y+1/X). Its proof permits every fixed M>1
by selecting sufficient decay seminorms of the fixed profiles; M=1 is NOT
asserted. This implies |I| << Z^(alpha+beta/2-1/2+epsilon).

**CT-2: actual Poisson identity.** It is an identity on initial absolute
convergence lines, with scale monomial

    X^(1/2-z) Z^(xi+z-1) Y^(w-1).

The u-th denominator is L_F^S(xi,bar chi_u), the numerator character is
chi_u in L_F^S(w,chi_u), and the common pole factor is zeta_F^S(6z).
The original correction, common-prime factors, finite S data and archimedean
profiles are retained. We do not replace this source by a native moment.

For a set of O(U^nu) representatives with U<=q_u<2U, reciprocal bound
|1/L_F^S(xi,bar chi_u)| << U^epsilon on the central segment, and
x=Re xi, y=Re w in (0,1], z=Re z, the dyadic central bound is

    Z^[alpha/2+x-1+(1-alpha)z+beta(y-1)]
                  U^[nu+(1-y)/2-z+epsilon].             (CT-D)

The convexity exponent uses conductor << q_u, not equality with q_u.
At x>1 absolute Euler convergence supplies the reciprocal bound at all
heights. On the large-frequency initial lines x=y=4, (CT-D) is replaced by

    Z^[alpha/2+3+(1-alpha)L+3beta] U^(1-L+epsilon), L>1. (CT-L)

Thus one must not use (CT-D)'s (1-y)/2 formula at y=4.

**CT-3: correction domain.** The meromorphic correction is holomorphic and
bounded as required in CT-D on each closed subdomain of

    x>0, y>0, z>0,
    6z+y>1, x+6z>1, x+y>1, x+y+6z>2,
    6x+6z>5, x>1/2, 3x>2, 3x+y>5/2.                  (CT-Omega)

The fixed-domain bound may lose any prescribed U^epsilon. Outside the
specified principal poles there are no extra poles inside this domain.
In particular for nonprincipal chi_u the movement of w through 1 crosses
no pole; in this proof z is kept above 1/6 on every nonprincipal contour.

**CT-4: tails and principal detector.** Fixed Mellin weights have polynomial
height control and arbitrary inverse-polynomial decay in the joint height.
In particular the xi+z Gaussian together with the z and w decay controls
also the direction Im z approximately -Im xi. Truncating the central xi
segment at U^rho and retaining the original x>1 tails gives the dyad bound
with an extra U^(-rho A), for any fixed A, on horizontal edges and retained
tails. This is the CT height argument, not decay of the Gaussian in xi alone.

In the principal row, the residues w=1,z=1/6 give c0 f_alpha(Z), where c0 is
fixed and nonzero, h=1-alpha, C=alpha/2+h/6, b=1-C, and

    f_alpha(Z) = (1/2pi i) integral_(Re s=2)
          Z^(s-b) exp((s-5/6)^2) H(s)/zeta_F^S(s) ds.    (CT-P)

The unchanged H is holomorphic and nowhere zero in Re s>2/3. It and its
inverse Euler expression have the ordinary initial-line and vertical bounds
needed for Mellin inversion. f_alpha is flat at zero by moving its initial
line right. Changing beta does not change b or the principal detector.
The single-residue principal remainders obey the corresponding scale
monomials, without a growing u sum.

These are substantive analytic inputs. The new rational checker checks their
application domains and powers, not their truth or source fidelity.

## DF and BGL: freshly inspected primary inputs

DF is de Faveri, arXiv:2610.04045v1, Theorem 1.1, Corollary 1.5 and its proof.
For the specified nth-order ideal character family with n=6, BOTH indices
in its enlarged sieve are sixth-power-free, not only squarefree:

    Theta_6(N,L) << (NL)^epsilon
          (N+L+N^(5/6)L^(1/3)+N^(1/3)L^(5/6)).          (DF-LS)

The norm of the full sixth-power-free index, with exponents 0,...,5, orders
the rows. It is NOT the radical norm. DF Section 2 supplies the exact
allowed choices for S, the deep ray modulus, representative generators,
multiplicativity for coprime indices, and literal zero extension.

BGL is Blomer--Goldmakher--Louvel, arXiv:1112.1650, Theorem 1.3 and Section 5,
especially (5.1),(5.3)--(5.5). We import its squarefree large sieve and the
classical analytic zero-detection inequality. PDF pages 18--19 were freshly
rendered and inspected. No GRH-dependent result is used. DF-LS replaces
only the relevant arithmetic mean values in that zero detector. The
fixed-S-unit twist adapter is reconstructed in PROOF.md, crediting #957.

No proof of DF-LS or of the full CT metaplectic construction is supplied by
this packet. The finite checker also does not construct a number field,
count actual L-function zeros, or validate a Lean dependency graph.
