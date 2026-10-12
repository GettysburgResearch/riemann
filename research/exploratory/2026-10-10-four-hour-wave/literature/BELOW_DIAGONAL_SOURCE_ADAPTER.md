# Signed source cancellation below the row/column diagonal

Date: 2026-10-10. Status: exact source arithmetic adapter and an OPEN
off-diagonal contract. No improved moment estimate or zero-free theorem is
proved here. The normalized diagonal cancellation was independently derived
by the coordinator, `review_setup`, and `kappa_proof_audit`.

Source: [the October 5 simplified quasi-RH manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf),
at literal commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`.
The local frozen source is
`/workspace/.riemann-research/sources/qrh11-12.tex`, SHA-256
`d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
Line references below refer to that file. This adapter imports the source's
arithmetic identities and Poisson formula; it does not rebuild them.

## Preserve the original normalization and arithmetic family

The field is K=Q(sqrt(-3)). The coefficient is the literal ideal Möbius
function times a fixed finite-order Hecke character. The finite excluded
set S and all ray characters remain fixed. Ideals are represented by their
unique primary generators; nonzero dual frequencies remain lattice elements.

At lines 1031–1034, the original smoothed row moment is

    M_D = D^(-1) sum_u Phi(Nu/H) |A_u(D)|^2.

The fixed nonnegative majorant Phi dominates the requested row disk and has
compact Fourier support. Lines 1054–1080 give

    M_D = Z + sum_xi c_xi S_xi,       Z = O(H),

with a fixed finite ray sum. Every bound for the unnormalized row moment
must restore the factor D.

Use W0(x)=x^(-1/2) conjugate(W(x)) and the source coefficient
a_xi(n)=conjugate(alpha(n)) gamma_2(n) xi(n), of modulus one on allowed
squarefree ideals. The exact initial-column identity, lines 1156–1173, is

    S_xi = (H/D^2) sum_{b,f squarefree,(b,f)=1} mu(f) Nb
             sum_{k!=0} sum_{m1,m2 squarefree,(m1*m2,b)=1}
               a_xi(m1) conjugate(a_xi(m2))
               chi_m1(k f^4) conjugate(chi_m2(k f^4))
               W0(N(b f m1)/D) conjugate(W0(N(b f m2)/D))
               Phi_hat(H Nk / ((Nf)^2 Nm1 Nm2)).

Every ideal variable is good for S. Character zeros enforce (m_j,f)=1.
The finite full f-sum and its sign must be retained. A positive dyadic
majorant formed after taking absolute values discards the cancellation.

## Exact diagonal collapse and its cost

Set m1=m2=m and c=fm. Then c is squarefree, (b,c)=1, and the complete
divisor coefficient is the exact ideal identity

    sum_{f|c} mu(f) 1_{(c/f,k)=1} = mu(c) 1_{c|k}.                (D1)

For each prime of c the local contribution is 1-1=0 if the prime does not
divide k, and 0-1=-1 if it does. Substituting k=ch gives

    S_xi,diag = (H/D^2) sum_{b,c squarefree,(b,c)=1} mu(c) Nb
                  |W0(Nbc/D)|^2
                  sum_{h!=0} Phi_hat(H Nh/Nc).                   (D2)

Compact Fourier support implies Nh<=C Nc/H. When a nonzero frequency
exists, Nc/H is bounded below by a fixed positive constant, so the fixed
lattice count bounds the inner absolute sum by O(Nc/H). The annular
support gives Nb Nc comparable to D. The ideal divisor census gives
O(D log D) pairs (b,c) in that annulus. Therefore

    |S_xi,diag| << D^(-2) sum_{Nbc comparable to D} Nb Nc
                << log D.                                     (D3)

The diagonal in the original row moment is O(D log D), not O(D^2).
At H=D^(18/23), the proposed penalty kappa=2/5 asks for row exponent
43/23, so this diagonal is harmless. No off-diagonal bound follows from D3.

## Coupled columns: the same identity retains their common factor

There is a useful exact reorganization beyond the displayed diagonal.
Put c_j=fm_j and g=(c1,c2), d_j=c_j/g. All are squarefree where appropriate,
(d1,d2)=1, and (b,c1*c2)=1. The source CRT identity at line 851 is

    a_xi(fm)=a_xi(f)a_xi(m)chi_m(f)^4.

Consequently, the entire f|g sum in the initial-column expression is

    a_xi(c1) conjugate(a_xi(c2)) chi_d1(k) conjugate(chi_d2(k))
        sum_{f|g} mu(f) 1_{(g/f,k)=1}
      = a_xi(c1) conjugate(a_xi(c2)) chi_d1(k) conjugate(chi_d2(k))
        mu(g) 1_{g|k}.                                         (D4)

The Fourier kernel and both W0 factors are independent of f in these
coordinates. Thus the exact regrouping sets k=gh and retains the kernel

    Phi_hat(H Nh / (Ng Nd1 Nd2)).                               (D5)

D4 reduces to D1 on c1=c2. It retains source-specific signs, cubic Gauss
phases, the coupled common factor and the common Fourier kernel. It is
an algebraic reorganization of the source, not a new estimate. The terms
d1!=d2 still require cancellation; treating them by absolute values does
not prove a power saving.

## A precisely unpaid estimate

For a specified fixed 0<h<1 and 0<=kappa<1/2, let H=D^h. A sufficient
source-qualified new input is, for each fixed allowed xi and every fixed
smooth compact norm profile W,

    |S_xi,off| << D^epsilon H (D/H)^kappa p_J(W)^2,              (OPEN-D6)

with a finite smooth seminorm, fixed S and fixed Fourier majorant, for every
D>=2. Here `off` means the literal c1!=c2 terms of D4–D5, equivalently
the original m1!=m2 terms after the complete signed regrouping. Z and D3
then give the desired original moment after multiplication by D. No
arbitrary coefficient estimate or growing exclusion set is licensed.

OPEN-D6 is unproved. The accompanying exact checker certifies only the
finite divisor identities, normalization exponents and declared scope.

## Why the existing positive-energy proof stops at penalty one

The source initial scales are X=D/(BF), Sigma=XF=D/B, and dual height
Hcal of order D^2/(HB^2). Hence Hcal/Sigma is of order D/(HB), which
exceeds one in the small B blocks when H<D. The cube lemma requires
Hcal<=Sigma. At B=F=1, its cutoff Hc^3=min(X,X^2/Hcal^2) becomes
H^2/D^2<1, leaving the b=1 same-scale long child. The strict contraction
used by the finite induction is lost. Relevant source blocks are lines
1000–1021, 1176–1188, 1336–1373 and 1567–1575.

The transfer can be applied with an enlarged target
Sigma_target=D^gamma max(Hcal,XF), with fixed gamma inside epsilon.
Its child ratio is Hcal' / Sigma' = Hcal/(Sigma_target F R), so the
canonical positive-gap induction becomes available. This only gives
E(Hcal,X,F)<<D^epsilon max(Hcal,XF). Restoring the initial prefactor and
the original D yields

    sum_{0<Nu<=H}|A_u(D)|^2 << D^(1+epsilon)(H+D).

For H<=D this is the penalty kappa=1. It supplies no kappa<1 bound and
does not pay OPEN-D6. The exact signed common-factor collapse identifies
where the positive majorant lost useful arithmetic, while leaving its
remaining off-diagonal obligation explicit.
