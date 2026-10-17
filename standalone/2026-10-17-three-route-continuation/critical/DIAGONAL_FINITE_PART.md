# The functional-equation diagonal has a pole: an exact first-jet detector

Status: proposed exact principal-row component, with proof. The result below is a new factorization and a reduction of a specific transverse finite part to the native logarithmic derivative. It proves no signed estimate and no zero-free region.

Scope: the principal row of the literal CT/OpenAI Poisson Euler factor, with the second Mellin variable fixed at z=1/2. The full physical projection, its test functions, and its tails are not estimated here.

Exact source: PR #962, head `b2032c663736ecd1e3872559d160ce069664ea06`, `standalone/2026-10-17-critical-scattering-reset/PRINCIPAL_TWO_VARIABLE_FACTOR.md`, and the primary local formula `eq:Euler-good-exact` that it cites at OpenAI/math commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`, blob `c8526f74b281d37fda034c17195c4bb5afd5f79b`, `preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/05-poisson.tex`. The same exterior local calculation is imported by CT v2, Section 11, over its fixed field containing mu_12.

The point of this calculation is to distinguish a bare functional-equation diagonal from its first transverse finite part. The diagonal residue has already canceled the target zeta zeros. The finite part retains every such zero, with its multiplicity.

## 1. The full principal local factor before taking w=1

Fix the source field F and the finite set S. Specialize the fixed TARGET character called `eta` in the OpenAI source to the principal character, and take its principal Poisson row u=1. In this note only, write eta=theta^6 for the ANGULAR phase; this is the notation of #962, not the source's target character. The angular phase is retained, and only |eta(p)|=1 is used. Write Zeta(s)=zeta_F^S(s). At an exterior prime of norm Q put

    r=Q^(-1), D=Q^(-xi), W=Q^(-w),
    V=Q^(-6z), E=eta(p) Q^4 D^6 V.

The literal principal-row source formula is

    F_p=1/(1-V)+W/(1-W)
        + E/(1-E) [(1-r)/(1-V)+W]
        - D/(1-E) [1+(r^(-1)-1) W V/(1-V)],

    H_p=(1-V)(1-W) F_p/(1-D).                             (1)

This is the formula before the specialization w=1 in #962. We now fix z=1/2, so

    V=r^3, E=eta(p) Q D^6.                                (2)

Let

    N_p=(1-D)(1-E) H_p.

Expanding the exact expression (1), with no asymptotic deletion, gives

    N_p=1-D+DW
        + V[D-W-r^(-1)DW+(r^(-1)-1)DW^2]
        + E[-r+rW-(1-V)W^2].                             (3)

In particular, when V=E=0 the remaining local correction is

    1+DW/(1-D).

Thus the first correction term contains Q^(-xi-w). The condition Re(xi+w)>1 in the older product domain is tracking an actual zeta factor on the principal row.

## 2. Extracting that factor at z=1/2

Define

    K_p(xi,w)=(1-Q^(-xi-w)) H_p(xi,w,1/2),
    K(xi,w)=product_(p notin S) K_p(xi,w).

**Theorem 1.** K is holomorphic on

    Re xi>1/3,   Re w>0,   2 Re xi+Re w>1.                (4)

On the initial Euler-product domain and hence by meromorphic continuation,

    H_1(xi,w,1/2)=Zeta(xi+w) K(xi,w).                     (5)

If all exterior norms are at least three, then the diagonal restriction

    k0(xi)=K(xi,1-xi)

is holomorphic and nowhere zero on

    1/2<Re xi<1.                                         (6)

It and its inverse are bounded on every closed vertical substrip strictly inside (6). The source field containing mu_12 and its fixed S satisfy the exterior-norm condition: primes above two are in S. If working in other data that retain a norm-two prime, its finite local factor must be checked or retained explicitly; it is not silently omitted.

### Proof of convergence and factorization

Put x=Re xi and y=Re w. On every fixed-margin subdomain of (4), 1-D and 1-E stay uniformly away from zero, because |D|=Q^(-x)<1 and |E|=Q^(1-6x)<Q^(-1). Set

    H_p^0=1+DW/(1-D).

From (3), subtracting H_p^0 shows

    H_p-H_p^0
       = {V[D-W-r^(-1)DW+(r^(-1)-1)DW^2]
          +E[(1-r)-D+DW+rW-(1-V)W^2]}
          /[(1-D)(1-E)].                                 (7)

Consequently

    |H_p-H_p^0|
       << Q^(-3-x)+Q^(-3-y)+Q^(-2-x-y)
             +Q^(-2-x-2y)+Q^(1-6x).                      (8)

The exact leading cancellation is

    (1-DW) H_p^0-1 = D^2 W(1-W)/(1-D).                   (9)

Combining (8) and (9), and using |1-DW|<=2, yields

    |K_p-1|
       << Q^(-2x-y)+Q^(-3-x)+Q^(-3-y)
             +Q^(-2-x-y)+Q^(-2-x-2y)+Q^(1-6x).           (10)

Every displayed prime-ideal series is summable on a fixed-margin subdomain of (4). Normal convergence proves that K is holomorphic there. Its first w derivative is normally convergent as well: differentiating the local factors adds at most fixed multiples of log Q, still summable on every smaller fixed-margin subdomain.

In the initial region where the Euler products converge absolutely, multiplication of K_p=(1-Q^(-xi-w))H_p proves (5). Equation (5) then supplies the claimed meromorphic continuation. This continues the PRINCIPAL local correction only; no unrestricted continuation of all nonprincipal H_u is claimed.

### Proof of diagonal nonvanishing

On w=1-xi one has DW=r exactly. Write d=|D| and omega=|W|. For 1/2<Re xi<1,

    r<d<sqrt(r),  sqrt(r)<omega<1,  |E|=d^6/r<r^2.

Equation (3) simplifies to

    N_p=1-D+r
        +r^3[D-1-rW]
        +E[-r+rW-(1-r^3)W^2].                            (11)

The baseline satisfies

    |1-D+r| >=1+r-d >=1+r-sqrt(r) >=3/4.                 (12)

When Q>=3, r<=1/3 and sqrt(r)<3/5. The two remaining terms in (11) have total modulus at most

    r^3(1+sqrt(r)+r)+r^2(1+2r+r^3)
       <=29/405+46/243=317/1215<3/4.                      (13)

Thus N_p is nonzero. The denominators 1-D and 1-E, and the additional factor 1-DW=1-r, are also nonzero. Every diagonal K_p is therefore nonzero.

The normal convergence already proved applies on a neighborhood of the diagonal. Together with local nonvanishing, it implies that their product k0 is nowhere zero. On a closed vertical substrip, (10) is uniform in Im xi, and (12)--(13) give a uniform positive lower bound for the finitely many small local numerators. A finite initial product and the uniformly convergent logarithmic tail give the asserted bounds for k0 and its inverse. This proves Theorem 1.

## 3. The residue is elementary; the finite part detects every target zero

Let R_S>0 and c_S be the first two Laurent coefficients

    Zeta(1+v)=R_S/v+c_S+O(v).                              (14)

The functional equation, with ALL fixed S factors retained, supplies a holomorphic nowhere-zero function B_S on 0<Re xi<1 such that

    Zeta(1-xi)=B_S(xi) Zeta(xi).                           (15)

For example, if A_F(s) is the gamma/discriminant factor in the completed Dedekind zeta function and E_S(s)=product_(p in S finite)(1-Q_p^(-s)), then

    B_S(s)=A_F(s) E_S(1-s)/[A_F(1-s) E_S(s)].              (16)

Every factor in (16) is holomorphic and nonzero in the open strip. Thus (15) is valid across nontrivial zeros by analytic continuation; it is not an assumption that Zeta has no zeros there.

After removing the fixed nonzero scalar Zeta(3), the principal-row arithmetic factor at z=1/2 is

    A(xi,w)=Zeta(w) H_1(xi,w,1/2)/Zeta(xi).

Introduce the transverse coordinate v=xi+w-1, and define

    Atilde(xi,v)=A(xi,1-xi+v)
       =Zeta(1+v) K(xi,1-xi+v)
          Zeta(1-xi+v)/Zeta(xi).                          (17)

All statements below are identities of meromorphic functions in xi. Put

    k0(xi)=K(xi,1-xi),
    k1(xi)=partial_w K(xi,1-xi).

**Theorem 2.** On 1/2<Re xi<1, the normal residue is

    Res_(v=0) Atilde(xi,v)=R_S B_S(xi) k0(xi).             (18)

It is holomorphic and nowhere zero, including at any hypothetical off-line zero of Zeta. Define FP(xi) to be the constant Laurent coefficient of Atilde in v. Its renormalization satisfies the exact identity

    FP(xi)/[R_S B_S(xi) k0(xi)]
       -k1(xi)/k0(xi)-c_S/R_S+B_S'(xi)/B_S(xi)
       =-Zeta'(xi)/Zeta(xi).                              (19)

Consequently, every zero rho of Zeta with 1/2<Re rho<1 produces a SIMPLE pole of this renormalized finite part, with residue minus its multiplicity. None is canceled by the angular numerator or the correction K. Equivalently, FP itself has a simple pole with residue

    -m_rho R_S B_S(rho) k0(rho).                           (20)

### Proof

First take xi away from zeros, so ordinary Taylor expansions may be used. Equations (14)--(17) yield

    Res_(v=0) Atilde=R_S k0 B_S,

    FP=B_S [R_S k1+c_S k0
             +R_S k0 Zeta'(1-xi)/Zeta(1-xi)].             (21)

Differentiate (15) logarithmically away from its zeros:

    Zeta'(1-xi)/Zeta(1-xi)
       =-Zeta'(xi)/Zeta(xi)-B_S'(xi)/B_S(xi).              (22)

Substituting (22) in (21) proves (19) on that open set and hence everywhere in the strip as a meromorphic identity. The functions B_S, k0, k1 and their displayed quotients are holomorphic there, and B_S k0 is nowhere zero by (16) and Theorem 1.

At a zero rho of multiplicity m, write Zeta(xi)=(xi-rho)^m q(xi), where q is holomorphic and q(rho)!=0. Then

    Zeta'/Zeta = m/(xi-rho)+q'/q.

This proves (20) and the normalized residue assertion, with no simplicity assumption on zeta zeros. Equations (18) and (19) also show exactly where the functional-equation cancellation occurs: it removes every target zero from the normal residue but only lowers its multiplicity to a simple pole in the finite part. QED.

## 4. What the next automorphic target must retain

Equation (18) rules out using the bare diagonal residue as a detector: that object is already explicit and holomorphic whether or not an off-line zero exists. Equation (19) gives a precise substitute. A proposed diagonal method must estimate the RENORMALIZED FIRST TRANSVERSE FINITE PART, including its signed contribution. Bounding only the residue cannot supply this information.

In the physical monomial of the source, with z=1/2 and w=1-xi+v,

    X^(1/2-z) Z^(xi+z-1) Y^(w-1)
       = Z^(-1/2) (Z/Y)^xi Y^v.                           (23)

The factor in X disappears exactly. Multiplication by Y^v adds log(Y) times (18) to the finite part. It therefore introduces an explicit, removable logarithmic term; it does not erase the logarithmic derivative in (19). Any additional holomorphic Mellin test factor contributes its normal derivative times the same explicit residue. Such test factors must still be retained, and a zero of an inspected test factor can still erase a particular detector unless nonvanishing is separately ensured.

This component establishes the arithmetic identity before those physical projections. It does NOT justify restricting a full double Mellin integral to the diagonal, exchanging a residue with an absolute-value bound, or taking a finite part through an unestimated tail. In particular, #965's linked-scale positive bound does not estimate (19). An actual estimate for the native signed first transverse finite part, with its physical weights and tails, remains open.

The distinction is useful for choosing the next attack: the diagonal is a pole of the exact principal Euler correction, and its leading residue has lost the zeta-zero information. The first normal finite part is the first place that information reappears. A successful coercivity or projection theorem would have to retain that signed first-order quantity.

## 5. Verification boundary

The algebra is supported by `verify_diagonal.py`, which checks the exact polynomial expansion of (1) after clearing denominators, the diagonal specialization, the leading Euler cancellation, and the strict rational margin in (13). The primary local formula and the definitions immediately preceding it were fetched again from the exact OpenAI commit above; the returned blob was `c8526f74b281d37fda034c17195c4bb5afd5f79b`. The written proof establishes the convergence domains, nonvanishing, and finite-part identity. The script does not authenticate the primary-source identity, the full physical Poisson formula, or any missing projection estimate. Those remain separate mathematical review obligations.
