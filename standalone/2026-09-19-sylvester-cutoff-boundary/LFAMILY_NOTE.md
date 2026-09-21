# L-family continuation: exact GL(2) boundaries and Sylvester reference fixtures

This is a bounded extension of programme #738 beyond its original quadratic
GL(2)-twist scope. It does not reclassify cubic twists as quadratic twists.
Owner of THIS continuation: Astra research pass requested by the user; #738 as
a whole is not reassigned. No background computation is implied.

## 1. What is imported from Burungale--Tian

The supplied arXiv:2609.14893v2, dated 15 September 2026, states that for every
prime p=8 mod 9, both E_p and E_(p^2), with

```text
E_m: y^2=x^3+m^2/4,
```

have analytic rank exactly one at the arithmetic center s=1 (Theorem 1.1).
The auxiliary cubic-residue condition controls both a complementary rank-zero
factor and a nonzero division boundary. The integral norm/projector identity
then forces nonzero cubic components; local torsion exclusion and Gross--Zagier
complete the proof. We have not independently verified the global inputs.

The paper is a reference for an arithmetic nonvanishing mechanism. It is not
an imported proof of GRH or an upper bound for the Riemann Newton covariance.

## 2. A genuine coefficient-level extension of the cutoff construction

Let a(n) be the multiplicative coefficients of an elliptic L-function in
ARITHMETIC normalization, and let nu be their Dirichlet inverse. At a good
prime ell the local series and inverse are

```text
sum_(j>=0) a(ell^j) T^j = 1/(1-a_ell T+ell T^2),
nu(1)=1, nu(ell)=-a_ell, nu(ell^2)=ell, nu(ell^j)=0 (j>2).
```

Put g_Y(n)=nu(n)1_(n<=Y), e_Y=delta-a*g_Y. For n=ell^h m, (ell,m)=1, h>=1,

```text
e_Y(n) = -sum_(d|m) nu(d)a(m/d)
          sum_(j=0)^min(h,2) nu(ell^j)a(ell^(h-j))
                              1_(ell^j d<=Y).           (G1)
```

Proof: write each divisor of n uniquely as ell^j d, use multiplicativity,
and the degree-two inverse coefficients. A complete three-term local fiber
cancels because the two local series are inverses. Only its cutoff defect
remains. This is ordinary Euler-factor algebra, with no priority claim.

For the CM family above, a good inert prime ell=2 mod 3 has a_ell=0.
Indeed cubing is a bijection over F_ell, so the quadratic-character point
count on E_m sums to zero and #E_m(F_ell)=ell+1. Consequently

```text
a(ell^(2h))=(-ell)^h, a(ell^(2h+1))=0.
```

Equation (G1) becomes the particularly simple boundary:

```text
e_Y(ell^(2h+1)m)=0,
e_Y(ell^(2h)m)=-(-ell)^h
     sum_(d|m,Y/ell^2<d<=Y) nu(d)a(m/d),  h>=1.          (G2)
```

The first surviving local operation is at ell^2, NOT ell. This is the
coefficient-level consequence of the vanishing Hecke eigenvalue. It is not
the paper's lambda-division boundary: it has no Kummer obstruction built in.
The wider interval in (G2) is not generally the antichain from the Mobius
one-prime case. Nor are its coefficients ternary.

For arbitrary invertible a the same Newton algebra gives

```text
N_a(g)=2g-a*g*g=g+g*e,
nu-N_a(g)=nu*e*e.
```

Thus a correct inverse prefix through Y generates nu(n) for n<(Y+1)^2.
Bad Euler factors must be specified before this is used for a FULL family
member. The committed finite fixture uses only the three good Euler factors
ell=5,7,11 of E_17; it is explicitly NOT the full elliptic L-function.

## 3. Exact finite-field reproduction of the paper's local calculation

lfamily.py constructs

```text
F_(p^6)=F_p[omega,t]/(omega^2+omega+1, t^3-varpi),
```

after verifying p is inert and varpi is a noncube in F_(p^2). For (q,p)
=(13,17),(13,107),(31,17) it checks, with finite-field integer arithmetic:

- the explicit Fermat lift from Appendix A;
- the curve equation and its first lambda division;
- t^(p^2)=alpha*t, and the independent cubic-symbol calculation modulo q;
- elliptic Frobenius R^(p^2)=[-p alpha]R;
- [p+1]R=epsilon*T_E != O, with epsilon=+1,-1,+1 respectively;
- the relative-Frobenius unit normalization sending T_E to T_E-sharp.

The q=31 case includes the nontrivial cube multiplier from Lemma A.2. These
are checks of the actual local geometry in the paper, not a mock scalar
trace example. The inadmissible pair (q,p)=(13,53) is rejected before a field
is constructed. Reversing the predicted boundary sign is also rejected.

The integral projector identities are checked over Z[omega] for cyclic
orders 3,6,9,27,81, for both cubic characters. They do not numerically test
Theorem 8.7's field-of-definition or nondivisibility hypotheses.

These checks do NOT establish that the starting point is the stated global
CM value, reconstruct its full Galois orbit, prove non-torsion over a number
field, or reprove Gross--Zagier. The paper separately proves those steps.
Its numerical recognition of some CM evaluations is kept distinct from its
exact group-law data (Appendix B.4).

## 4. Rank-sensitive detector interface

Assume the standard entire completed normalization

```text
Lambda_E(s)=N_E^(s/2)(2pi)^(-s) Gamma(s) L(E,s),
Lambda_E(s)=-Lambda_E(2-s),
ord_(s=1) Lambda_E(s)=1.
```

Here N_E is the ACTUAL conductor, not m or an assumed power of m. No conductor
value is invented by these fixtures. Set

```text
D_E(z)=Lambda_E(1+z)/z,
D_E(0)=Lambda_E'(1).
```

Then D_E is entire and even, and D_E(0)!=0. This follows from the Taylor
expansion and the odd functional equation. Its noncentral zeros, with their
multiplicities, are unchanged. Away from zeros,

```text
D_E'(z)/D_E(z)=Lambda_E'(1+z)/Lambda_E(1+z)-1/z.
```

At zero the apparent pole is removable. Thus a rank-deflated detector must
remove precisely this central contribution, not other zeros.

Exact polynomial controls are supplied: z(1+z^2) has a removable simple
center; z(z^2-1/4) keeps both off-critical real-z zeros after deflation;
z^3(1+z^2) remains centrally vanishing after only one division and is not a
rank-one fixture. Critical-line zeros correspond to imaginary z in this
arithmetic coordinate. These are synthetic controls, not elliptic zero data.

The new family is useful for distinguishing genuine central multiplicity,
normalization bugs, and off-line detection. It supplies no distributional
claim about the other zeros.
