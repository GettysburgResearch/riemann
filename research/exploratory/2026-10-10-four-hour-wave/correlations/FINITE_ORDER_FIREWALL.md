# Global finite order and growing tail order can coexist with a hidden quartet

Status: proposed exact modified-source deduction; independent review pending.
Scope: a theta-derived auxiliary function, not actual xi. The construction
retains the stronger complete-count envelope used by the new height proofs.
It identifies the remaining arithmetic source-binding obligation, and gives
no RH conclusion.
Dependencies: the already reviewed quartet and modular constructions in
`../xi/POSITIVE_THETA_QUARTET.md` and
`../xi/MODULAR_BINDING_AND_TRANSPORT.md`; the named classical actual-xi
count and published finite verification; the annular proofs in `../heights/`.
What ran: exact rational count-margin and quartet-factor controls in the
accompanying checker. No actual high zero is located or inserted into xi.
Smallest remaining gap: a theorem using the exact Euler/lattice source,
rather than only the properties retained below.

## 1. A fully specified auxiliary source

Set R=10^50 and d=1/4, and use the real-zero convention
Xi(z)=xi(1/2+iz). Define

    Q(z)=((z-R)^2+d^2)((z+R)^2+d^2),
    G(z)=Q(z)Xi(z)/Q(i/2).                                      (F1)

The denominator is strictly positive. The reviewed complete atom argument
proves that G has a strictly positive, smooth, even theta-derived Fourier
source. Its primitive retains the exact additive Jacobi reflection, and
G(+/-i/2)=1/2. It is even real entire of order one and has the complete
actual Xi zero multiset plus the four zeros +/-R+/-id. Its critical census
through H=3*10^12 is unchanged, including multiplicities. The four inserted
zeros lie strictly inside the classical strip.

These are complete modified-source identities. The polynomial factor
breaks the actual constant-coefficient lattice Gaussian and ordinary
Dirichlet/Euler normalization; those failures are proved in the cited
modular packet. The construction does not modify the actual xi function.

## 2. Preserve the precise quarter-log complete count

Let N(T) be the actual count of positive ordinates, with multiplicity, and
let M(T) be the Riemann--von Mangoldt main term used by the height proofs.
For the auxiliary completed function E_G(z)=G(-iz), the count is exactly

    N_G(T)=N(T)+2*1_(T>=R).                                    (F2)

There are two new upper-half-plane zeros, not four; the other two are their
lower reflections. An overlap with an actual zero increases its multiplicity
and does not change this count identity. Right-continuous counts and
one-sided endpoint values use the same convention.

For H<=T<R, the count is unchanged, so the source-qualified bound
|N_G(T)-M(T)|<(1/4)logT holds. For T>=R, combine the published Trudgian bound
with the elementary theta remainder used in the annular proof:

    |N(T)-M(T)|
      < (14/125)logT +(139/500)loglogT +677/200 +1/T.             (F3)

Here 677/200=2.510+7/8. Since logT>100, loglogT<logT/8 and 1/T<1,
adding the two new zeros gives

    |N_G(T)-M(T)| < (587/4000)logT +1277/200
                      < (1/4)logT.                            (F4)

The final strict gap at logT=100 is

    (413/4000)*100-1277/200=197/50>0,

and grows thereafter. Thus the auxiliary source retains the *same explicit*
complete-count envelope for every T>=H, rather than merely its asymptotic
logarithmic order. Its literal S(T) need not be claimed equal to the actual
zeta argument: F4 is the direct count estimate needed by the height proof.

## 3. Apply the reviewed proofs at their actual source interfaces

E_G is even entire of order one and has the required complete paired product,
classical strip and count envelope. On the positive real axis its quartet
factor is positive and has no zero. The logarithmic derivative and kernel
are therefore defined there. All zeros below H remain critical. The
arbitrary-node congruence and annular proof consequently apply to

    K_G(x,y)=(E_G'(x)/E_G(x)+E_G'(y)/E_G(y))/(x+y).

They give global positive definiteness at every packet of at most 6000
distinct positive nodes, and positive semidefiniteness when nodes repeat.
The growing-tail theorem also applies: for T>=H and every even n>=256 with
14n^3<=T, the *complete tail above T* has positive packets through order n.
The newly added quartet is nevertheless off the critical line.

These conclusions do not contradict either height theorem. The global
statement has fixed finite order; the cofinal statement changes the source
tail when T changes. The exact modified example shows why combining those
two kinds of positivity without a further source argument does not settle
RH. It is not a counterexample to the actual arithmetic source, an accepted
RH equivalence, or an unproved all-order positivity theorem.

If the complete actual source is assumed to satisfy the imported 7/8 strip,
the auxiliary function also satisfies that strip because d=1/4<3/8. This
optional stronger retained property still does not restore Euler binding.
