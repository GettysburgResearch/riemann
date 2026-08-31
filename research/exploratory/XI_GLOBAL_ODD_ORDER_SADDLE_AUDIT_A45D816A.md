# Independent audit of the global Xi saddle at a45d816a

Scientific source: a45d816a2b390de0efaa468622be65bb87737361.
Authoring base: af809698fe6cb5046a5bcc00e9175296e4597060.

Verdict: PASS for the written analytic theorems and exact finite identities;
REPAIR REQUIRED for the frozen numerical-campaign artifact. The latter
does not invalidate the analytic proof, but the original seven-file release
is not accepted without correcting its declared odd-order provenance.
No scientific source file was edited by this reviewer.

## 1. Concrete release finding

The campaign says that each K is the nearest positive odd integer to
b*xi*exp(gamma*xi). Four saved K values violate this contract in
research/exploratory/xi_global_odd_order_scout_results.json:

| Line | Case | Saved value | Correct nearest odd K |
|---:|---|---|---|
| 368 | xi=12, gamma=3, b=1 | 51734778565382344, even | 51734778565382343 |
| 428 | xi=12, gamma=4, b=1 | 8.420083094517158e+21, float | 8420083094517158086385 |
| 488 | xi=12, gamma=5, b=1 | 1.3704088677788212e+27, float | 1370408867778821140395548619 |
| 548 | xi=20, gamma=5, b=1 | 5.376234283632271e+44, float | 537623428363227089682525110316002717472222375 |

The scout itself returns a Python integer and rejects even orders. The
corruption occurred in aggregation/transport, not in its live computation.
Fresh 50-requested-digit, radius-24 runs for (xi,gamma)=(12,4) and (20,5)
reproduce EVERY saved nonelapsed result field except K. Their standardized
wrong-center shifts are respectively -0.50788047940314073188616117 and
-9936.688097602339297185995147. Those reruns remain non-directed checks,
not interval certificates.

The exact producer authenticates the campaign's bytes but does not validate
this semantic contract; its passing test is not evidence that saved K is
an admissible odd current order. A new identity should preserve K as a
canonical decimal string (or through a transport that retains arbitrary
integers), regenerate the campaign, and reject wrong case/type/parity/source
metadata. Original a45d816a must remain immutable.

## 2. Analytic reconstruction

All seven new files and their four frozen dependencies were read. The
full-line theta normalization comes from the literal source at 3b697232;
no fixed-K asymptotic is used with growing K.

### Complete theta factor and corner

For X>=1 the first theta orbit is at least 1-3/(2pi)>=1/2.
The complete remaining n>=2 sum is at most (512/31)exp(-3pi X)<=1/31.
For the logarithmic derivative, the first-orbit contribution is at most
1/2, the positive differentiated tail contributes at most 1/62, and
y exp(-y)<=2exp(-y/2) gives the remaining bound 32/15.
Their sum is 1232/465<3, so division by theta_*>=1/2 gives six.

Thus the two-factor correction B has a global absolute upper/lower bound
and logarithmic Lipschitz constant twelve. These are full-series estimates,
including when the low kernel argument crosses zero. Multiplication of
the two exact even-kernel formulas gives exactly the phase F in (1.3):
the amplitude is (9/2)max(xi,d), not (9/2)xi on the unbalanced side.

The derivative jump is downward by 2pi-9/2, and the curvature J is
continuous at d=xi. The two order endpoints K_L,K_R and their difference
xi(4pi-9) follow directly from the one-sided slopes. Strict concavity and
F'(0)=K/xi>0 give a unique positive maximizing a. The auxiliary phase's
corner is not a plateau of modes of the smooth literal kernel.

### Uniform separation and quantitative bracket bound

Write L=a sqrt(J) and R=K min(xi,a)/max(xi,a). The proof that J and L
diverge under xi->infinity, kappa->infinity is valid: for a<=1 the
balanced saddle equation makes both J/E and kappa/(a sqrt(E)) bounded
above and below by positive absolute constants; for a>=1 use J>=2pi E.

A useful independent strengthening of the manuscript's case check is

    R >= (1/3) min(J,L^2),     xi>=2.

For balanced a<=1, using coth(a)<=1+1/a gives

    R/L^2=(xi+a)/[xi*a*(coth(a)+1/(xi+a))] >=3/7.

For balanced 1<=a<=xi,

    R/J=a(xi+a)/[xi*(coth(a)+1/(xi+a))] >=3/7.

For unbalanced a>=xi, put Q=K/(xi+a). Then
Q=pi(exp(xi+a)+exp(a-xi))-9/2>87/2, using pi>3,e>2.
Consequently J=Q(1+1/(xi+a))+9/2<(3/2)Q, whereas
R=Q*xi*(xi+a)/a>=2Q. At a=xi in the corner interval,
Q=K/(2xi)>=pi(E^2-1), so
J/Q<=1/4+(E^2+1)/(E^2-1)<=83/60<3/2, and R=2xi Q.
This proves the claimed uniform lower bound on every branch, with no
upper cap on K.

For |d-a|<=a/2 the logarithmic ratio inequality (2.7) therefore bounds
the absolute Kth bracket remainder by exp(-R). On the complement,
the global phase tails control its weighted integral. This handles
a arbitrarily larger than xi; no balanced-region estimate is smuggled in.

### Full tails, rate, and normalization

The estimate |J'|<=2J and continuity of J give curvature comparison
on every unit neighborhood of a. At a corner maximum the one-sided
slopes have the required signs and magnitudes bounded by 2pi-9/2.
This proves both the local quadratic expansion with error
C(|v|+|v|^3)/sqrt(J) and the global quadratic/linear tail bound (2.10).

The tail estimate is genuinely global: use the tangent at a+1 and,
when it lies in the domain, a-1. No low-frequency endpoint or remote
unbalanced region is omitted. After rescaling it integrates against
every fixed polynomial times exp(T|v|). The missing Gaussian portion
v<-L is also exponentially small as L grows.

The inequality for differences of exponentials applies with both
exponentials bounded by a common Gaussian on the unit neighborhood;
hence its cubic Taylor error integrates to O(J^-1/2). The correction B
has the same order, and d/a=1+v/L supplies O(L^-1).
The bracket error and all complementary tails are exponentially small
in min(J,L^2). A fixed central interval supplies a positive normalization.
This verifies the stated weighted L1 rate, including both plus/minus laws,
not just weak convergence or a pointwise saddle substitution.

### Translated response and phase diagram

Cancelling the factor d before taking expectations gives exactly (3.2).
The coth term is uniformly removable: its deviation from sign(tau) is
at most 1/(|tau|L), while E|sinh(tau v)| is at most
|tau|E[|v|exp(T|v|)]. This is O(1/L), including tau approaching zero.
At tau=0 the original normalized response is exactly one.
Thus (3.1) follows uniformly on bounded real tau intervals; for bounded
physical translation h it is a relative, not absolute, asymptotic.

The phase-diagram constants follow by solving the actual branch equation:
a=(gamma-1)xi+log[b/(pi gamma)]+o(1) and J~(b/gamma)exp(gamma xi).
The plus-weight second moment, not the d-weighted current moment,
decides the scalar carrier sign. The finer b=2pi threshold remains
the separately pinned theorem, with its odd-lattice qualification.

Finally the wrong balanced-center slope defect is

    9/2-pi[exp(a_hat-xi)+exp(xi-a_hat)].

For gamma>2, comparison with curvature pi exp(xi+a_hat) gives
exp(2xi)(a-a_hat)->-1. Consequently the standardized displacement is
-sqrt(b/gamma)exp[(gamma/2-2)xi]. At gamma=4 it tends to -sqrt(b)/2;
for gamma>4 the wrong-centered law escapes to negative infinity.
This does not contradict the older bounded-order/bounded-b theorem.

No analytic gap was found in GS1, GS2 or these stated consequences.

## 3. Frozen replay and boundaries

The correct commands on the fresh source checkout were

    python -B -m unittest tests.test_xi_global_odd_order_saddle tests.test_xi_odd_current_scaling
    python -B -O -m unittest tests.test_xi_global_odd_order_saddle tests.test_xi_odd_current_scaling

Both ran 42 tests and passed, in 19.849 and 20.085 seconds.
Both --check runs and all four exact LF emits (--emit-report and
--emit-manifest in normal/optimized modes) pass. Ruff and the complete
af809698-to-a45d816a whitespace check pass. The source was unchanged.

The four frozen commit/blob/LF bindings authenticate correctly. The six
current artifact hashes in the fixture also match. Key hashes are:

- proof: 7f1a47052335a2916204dbb0161d3390566e2e6dbb13885a911b9c916cd4e2b9
- exact producer: 667b4906d996e2e8fffe57e8742b62ed390969db4ec7324063d20484afeb6bf8
- source manifest: d2004cc18bba1907f9b8683c0f274543cfd90e7b044d8cd3ec246852de58c62c
- scout: 7af88a760414d8dd720e11e6771dfaea6c3c07cf98ca15c2b9cda135fb02f6d4
- defective original campaign: 8d94aa0c3e45a8312f9ed258961587629c1702897af35478ae2fd86d3f6048e2
- tests: 50373289983b158d8eedc0cd074e2d809a4204679e3306a7f543324e00a9fc8a

The exact producer uses rational/symbolic algebra with no transcendental
rounding. The separate mpmath campaign is explicitly non-directed and
uses a bounded quadrature window. Ordinary authenticated JSON loading
is not advertised as a hostile unbounded-input parser. Neither finite
replay nor the numerical campaign proves the all-K analytic quantifiers.

This review certifies no prescribed physical-lambda selection, source-Pick
congruence, complete capture, innerness, topological free energy, global
zero census, new external priority, or RH. Acceptance of a corrected
campaign requires a separate review of its new source identity.
