# An energy-adaptive rough-core target and the exact price of an intermediate strip

Status: PROPOSED source-qualified deductions and complete elementary exponent
lemmas. No new signed rough-core estimate, energy contraction, or zeta boundary
is proved. The native sector bound is explicitly imported from #994, not
silently reclassified as a new analytic theorem.

## 1. Use the original native coefficients

Retain #994, native/PROOF.md at c93ca65a510b6acaf167f929b9bf7e67d742b05a:

    m(k)=sum_(n<=k)mu(n)/n, F_Y=sum_(k<=Y)m(k)^2,
    g_Y(n)=mu(n)1_(n<=Y), z_Y=g_Y*g_Y
                               (Dirichlet convolution),
    C_Y(q)=sum_(q|d,d<=Y^2)z_Y(d)/d.

The notation g_Y in the preceding line means mu(n)1_(n<=Y), not a
convolution with the interval indicator. All old products, including
those above an output cell, occur in C_Y.

A cubefree q has unique form q=r^2 s with r,s squarefree and coprime;
its squarefree core is s. For fixed 1/2<rho<2/3 let V_Y be the complete
large-denominator amplitude in #994, using its exact dyadic output
windows and centered Ramanujan harmonic modes. Let Vrough_(Y,S) retain
only core(q)>S in that amplitude. Define S=0 to mean Vrough=V_Y.

The source gives, for every integer S>=1,

    ||V_Y-Vrough_(Y,S)||_2 <=12 H_Y sqrt(S) H_S^3,       (1)

including coherent cross terms and arbitrary bounded per-q window masks.
At the native reciprocal sign crossings Y in Xcal it also gives

    |sqrt(F_((Y+1)^2-1)-F_Y)-||V_Y||_2|<=eta_Y,
    eta_Y ->0.                                        (2)

These complete-source statements, not an independent-coefficient model,
are the inputs of the following new budget adapter. Their proofs were
read at the displayed pin. No claimed sharpness or independent referee
certification is inferred from that read.

## 2. Spend an intermediate-error allowance on much larger cores

Fix ANY G_Y>0. Put

    S_Y=min(Y^2, floor(G_Y/[2304 H_Y^2 H_(Y^2)^6])).     (3)

S_Y=0 is permitted and removes no core. Then the full removed amplitude
obeys

    ||V_Y-Vrough_(Y,S_Y)||_2<=sqrt(G_Y)/4.              (4)

Proof. If S_Y=0 the statement is trivial. Otherwise S_Y<=Y^2 and
H_(S_Y)<=H_(Y^2). Square (1), and use the floor bound in (3):
144 S_Y H_Y^2 H_(S_Y)^6<=G_Y/16. All annular masks and mixed terms
are inherited from (1); none is estimated separately or deleted. QED.

At the crossings, (2) therefore implies

    sqrt(F_((Y+1)^2-1)-F_Y)
       <=||Vrough_(Y,S_Y)||_2+sqrt(G_Y)/4+eta_Y.         (5)

This permits a core cutoff of order G_Y/(log Y)^8 whenever it grows.
The earlier subpower-core choice was tailored to a subpower final error.
For an intermediate power saving, that restriction is unnecessarily strong.

Take, for example,

    G_Y=Y^a(1+F_Y)^p, a>=0, 1<=p<2.                    (6)

The cutoff is chosen from the ACTUAL old energy, not an asserted
asymptotic for it. It is a native, computable, prefix-dependent cutoff.
A bound ||Vrough_(Y,S_Y)||_2<=C sqrt(G_Y) would imply the corresponding
square-step recurrence at every cut where (2) is available. This remaining
rough bound is OPEN; (4) does not provide it.

If F_Y has size Y^kappa, the paid core scale is roughly
Y^(a+p kappa)/(log Y)^8, rather than just Y^o(1). Under the illustrative
values kappa=3/4, a=1/3, p=3/2, it is Y^(35/24)/(log Y)^8. This is
budget arithmetic, not a proved growth law or the removal of all larger
cores. It points to a much narrower high-core target in a contradiction
argument where the native energy is large.

## 3. Full recurrence theorem: no hidden assumption about sparse cuts

### Theorem N1 (conditional on a COMPLETE recurrence)

Suppose F is nonnegative and nondecreasing, has some polynomial upper
bound, and for every sufficiently large integer Y satisfies

    1+F_((Y+1)^2-1)<=C Y^a(1+F_Y)^p,
    a>=0, 1<=p<2.                                     (7)

Then for every epsilon>0,

    F_X<<_epsilon X^(a/(2-p)+epsilon).                  (8)

Proof. An input bound F_X<<X^(kappa+epsilon) in (7), followed by
Y=floor(sqrt X), yields exponent (a+p kappa)/2 with an arbitrarily
small loss. After any FIXED j iterations the exponent is

    kappa_j=a/(2-p)+(p/2)^j[kappa_0-a/(2-p)].            (9)

Choose a sufficiently large fixed j for the desired final epsilon,
and choose the earlier losses small enough. Constants may depend on j;
no constant uniform as j tends to infinity is needed. This proves (8).
The same argument permits separately quantified arbitrarily small
power losses in (7). QED.

WARNING: (5) was supplied at native crossings, whereas (7) is an ALL-Y
recurrence. Theorem N1 is not applied directly to the sparse cuts. A
separate native all-prefix/cofinal growth theorem, such as the additional
source used in #994, would have to be adopted and audited to justify
that weaker sufficient formulation. No gap-size hypothesis or such
promotion is silently inserted here.

## 4. Energy to ordinary zeta: the elementary forward implication

For the actual m and F, if F_X<<X^(kappa+epsilon), Cauchy-Schwarz on
dyadic intervals shows that

    integral_1^infinity m(x)x^(-z-1)dx

converges absolutely and holomorphically for
Re z>(kappa-1)/2. Initially on Re z>0 it equals

    1/[z zeta(z+1)].                                    (10)

The apparent singularity at z=0 is removable, since zeta has its pole
at one. Every nontrivial zero rho with Re rho>(kappa+1)/2 would give a
nonremovable pole at z=rho-1 in (10), a contradiction. This forward
implication needs no equality between liminf and limsup energy exponents.

The half-plane resulting from a PROVED full recurrence (7) would thus be

    Re s > [1+a/(2-p)]/2.                              (11)

Examples of STILL OPEN targets:

| a | p | limiting boundary from (11) |
|---|---|---|
| 1/3 | 3/2 | 5/6 |
| 1/4 | 3/2 | 3/4 |
| 1/3 | 4/3 | 3/4 |
| 0 | any fixed 1<=p<2 | 1/2 |

For reference, starting at the round imported energy exponent 3/4,
the illustrative first row would give one-step exponent 35/48 and
boundary 83/96, before further iterations. These are hypothetical
consequences, not newly attained bounds. Liu v2's slightly smaller
benchmark is recorded separately in SOURCES.md.

## 5. Where further arithmetic has to enter

The remaining high-core amplitude retains the signs of the full
masked reciprocal sums in the exact C_Y(q). Replacing those sums by
independent variables or taking the absolute coefficient majorant in
#994 does not produce p<2. The intended next attack is a correlated
estimate on the energy-adaptive complement (3), not the same full
positive coefficient envelope optimized again.

The new sixth-zeta-moment paper's exponential-sum bounds are only
background here: no derivation of a square-root phase for this precise
native window and coefficient class was found in this pass. A theorem
about that external phase class is therefore NOT inserted as a bound
for Vrough. This is a tested research stopping point, not an imported
unproved interface.

The finite checker rebuilds actual integer prefixes and complete
C_Y(q), tests their mask factorization and the budget (3), and verifies
(9) exactly. It does not test or prove (7) for unbounded Y.
