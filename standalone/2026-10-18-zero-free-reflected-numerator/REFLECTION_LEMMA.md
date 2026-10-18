# Reuse the zero-free rectangle on the numerator side

Status: PROPOSED component argument, awaiting independent mathematical review.
This checkpoint does not yet announce a new global zero-free boundary. The
classical functional equation and logarithm estimates are credited, not claimed
new. The contribution is their use on the SAME zero-selected Poisson classes.
No RH, GRH, global zero-free theorem, new inverse-L moment or independence
hypothesis is assumed.

## 1. Precise local-in-family statement

Fix a number field F, finite S, and a fixed finite list of finite-order
S-supported twists. Use the actual sixth-power-free family identified in
#965/#966/#971, with full exterior ideal norm q_u in [U,2U). Its primitive
conductors satisfy Q_u <= C U. Principal inducing characters are excluded.
Write chi_u for the numerator character and bar(chi_u) for the denominator
character. The finite S omissions and original nonunit values are retained.

Fix 1/2 < tau < 1, rho > 0 and 0 < e < (1-tau)/10. Suppose a subset C(U)
has no denominator zero in

    Re s >= tau, |Im s| <= 4 U^rho.

For every eta > 0, for sufficiently large U, uniformly for

    x = tau + 3e, y = 1-tau-e,
    |v| <= U^rho, |t| <= U^rho,

one has

    |L_F^S(y+it,chi_u) / L_F^S(x+iv,bar(chi_u))|
       << U^(tau-1/2+e+eta) (2+|t|)^C.                 (R1)

C is fixed by F and the real strips. The constants may depend on e, eta,
rho, tau and the fixed family data. No equality between t and -v is needed.
For a subset of cardinality O(U^nu), summing gives exponent

    nu + tau - 1/2 + e + eta.                         (R2)

This is a selected-family ratio estimate, NOT a statement that the same
bound holds on the unrestricted family or across a denominator zero.

## 2. Both signs of log L

For the primitive denominator, use the branch of log L obtained from the
Euler logarithm at 2+it. On a zero-free rectangle as above, disks about
2+it with radii

    R=2-tau-e/4, r_o=2-tau-e/2,
    r_t=2-tau-e, r_i=1-e/4

are strictly nested and lie inside the rectangle for |t|<=2 U^rho and
large U. Polynomial conductor/height growth and Borel--Caratheodory give
|log L| << log U on the r_o disk. Absolute Euler convergence gives
|log L| <<_e 1 on the r_i disk. Hadamard three circles therefore gives

    |log L(s,bar(chi_u))| <<_e (log U)^theta, theta<1,

on the r_t disk. In particular, for EVERY later eta>0,

    |L_F^S(s,bar(chi_u))| + |1/L_F^S(s,bar(chi_u))|
       <<_(e,eta) U^eta,
    Re s >= tau+e, |Im s| <= U^rho,                  (R3)

on the fixed real strips used here. Points to the right of 1+e can instead
use Euler convergence. Fixed S factors and any primitive Euler restoration
are bounded separately on these positive real-part strips. Their logarithms
have no positive-real-part singularities. The exceptional set, rho and e
remain fixed when eta is subsequently reduced.

The earlier arguments used only the inverse half of (R3). Its direct half
is equally available. It is not Lindelof assumed on the critical line.

## 3. Reflect the actual numerator character

The complete primitive Hecke functional equation gives

    L(y+it,chi_u)
      = epsilon_u Q_u^(1/2-y-it) G_u(y+it)
                          L(1-y-it,bar(chi_u)),       (R4)

where |epsilon_u|=1 and |G_u(y+it)| << (2+|t|)^C on the
fixed strip. Expand the finitely many omitted S Euler factors before
using this identity. Both y and 1-y are strictly positive, so their fixed
local ratios are bounded on these strips. Any conductor type at S belongs
to a fixed finite list.

Now 1-y=tau+e. Thus the reflected numerator in (R4), as well as the
original denominator at x=tau+3e, lies INSIDE the same zero-free rectangle.
Apply both halves of (R3). Since 1/2-y=tau-1/2+e>0, the conductor inequality
Q_u<=CU has the required direction. This proves (R1) after rescaling eta.
There is no negative conductor power incorrectly replaced by a power of U.

## 4. Compatibility with the original correction

The enlarged correction domain proved as a proposed component in #971 is

    x,y,z>0; 6z+y>1; x+6z>1; x+y>1;
    x+y+6z>2; 6x+6z>5.

Its actual H_u is subpower for x>=1/2 on fixed-margin real compacts, uniformly
in all imaginary parts. At z=2/5, the new coordinates obey x+y=1+2e and
x>1/2. All the other inequalities have positive margins. The obsolete
conditions 3x>2 and 3x+y>5/2 must NOT be reinstated or silently imported.
The local-domain component is a load-bearing proposed dependency, not
something independently certified by this checkpoint.

For physical X=Y=Z^a, a<1/2, put h=1-a. A Poisson dyad has scale exponent

    E=a/2+x-1+h z+a(y-1)

and row power nu+tau-1/2+e-z. At U=Z^h and e=0, its combined exponent is

    (1-a)(2tau+nu)+a-3/2.                              (R5)

Comparison with the physical bound Z^(a/2) therefore needs

    (1-a)(2tau+nu) <= 3/2-a/2.                        (R6)

For a middle class E_sigma minus E_tau, nu comes from the LOWER threshold
sigma; the zero-free rectangle comes from the UPPER threshold tau. The
limiting symbolic check nu=g(tau) is only exploratory: a finite proof must
use the actual lower-threshold count and retain a positive contour buffer.
The unrestricted good class can retain its BGL second mean, and the terminal
exceptional class must retain an Euler-line treatment. Neither is deleted.

## 5. A necessary additional tail check

Unlike a global numerator moment, (R1) is valid only for the TRUNCATED
w-height. A full composition must split both xi and w at height U^rho.
For w tails and horizontal connectors use ordinary convexity, the existing
reciprocal bound on the shifted xi segment, and the original Schwartz
w-weight. For original xi tails keep its Euler line. The joint weight is
Gaussian in Im(xi)+Im(z), not in Im(xi) alone; integration in z must retain
its independent rapid decay. None of these tail arguments is replaced by
(R1) outside its stated rectangle.

## 6. Source and overlap record

Live reads: #971 RAMIFIED_FACTORS.md at
3f1d2a07631eb6cca1f2716be01f64e874667639; the current descriptions of #969,
#974, #975 and #976; the previously delivered nineteen-file local-support
packet. The functional-equation/finite-part work in #975 is relevant context,
not a new result reattributed here and not a premise of (R1).

De Faveri arXiv:2610.04045v1 was freshly opened: Theorem 1.1 genuinely uses
sixth-free rows AND columns, and Corollary 1.5 gives the displayed full-norm
density. BGL arXiv:1112.1650 was retrieved. Fresh CT v2 landing/PDF/TeX
retrieval failed in this pass. CT identities and the subcritical reflection
must consequently retain their pinned repository-source qualifications.
No Lean build, external referee review or full metaplectic reconstruction
has been performed. A separately labeled continuation will contain any
complete global comparison and its finite checks.
