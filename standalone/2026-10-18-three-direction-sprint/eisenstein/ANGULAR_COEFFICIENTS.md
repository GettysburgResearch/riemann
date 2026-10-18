# Complete native cube coefficients avoid the specified radial Gauss direction

Status: **PROPOSED arithmetic estimates; independent review required.**
Scope: K=Q(omega), omega^2+omega+1=0; all exterior ideals, outside the primes
above 2 and 3. This is a cancellation estimate for the actual coefficient
shape of a completed cubic theta sum. It is not a bound for the whole
character transform or an improved zero-free theorem.

## 1. Exact arithmetic objects and source mapping

Every exterior ideal I has a unique primary generator alpha_I=1 mod(3).
The generators multiply exactly. Let N denote ideal norm. Fix an integer
angular order m!=0, a real t0, a fixed ideal modulus f, and a bounded periodic
unit-modulus function eta on the admissible residues modulo f. Define

    theta(I)=eta(alpha_I) (alpha_I/|alpha_I|)^m (NI)^(it0).

No multiplicativity of eta is needed for the estimates. Thus a fixed finite
ray classification is allowed, in addition to genuine unitary Hecke
characters. The finite modulus, m and t0 never grow. At excluded residues
one may extend eta by zero and retain the original exterior condition.
For the norm identity below, eta has modulus one on exterior ideals.

Let g(c) be the normalized cubic Gauss sum on each squarefree exterior ideal
c, with the fixed primary/additive convention. Its modulus is one there.
The proof uses only that modulus identity; it does not change its phase.
For P(y)=exp[-log(y)^2/4]/sqrt(4pi), define the COMPLETE vectors indexed by
every squarefree exterior c and every exterior n:

    v_(c,n)(Z)=g(c) theta(c n^3)/(sqrt(Nc) Nn) P(Nc (Nn)^3/Z),
    w_(c,n)(Z)=g(c)             /(sqrt(Nc) Nn) P(Nc (Nn)^3/Z). (1)

There is no coprimality condition between c and n. Every cube power and both
Gaussian tails remain. The vectors are square summable for every fixed Z>0.

The coefficient shape in (1) is exactly the c,n coefficient in CT v2 equation
`eq:B`, with its gamma_2(c) in place of g(c) and its fixed correction character
vartheta in place of theta. Since gamma_2 is the normalized Gauss sum of the
square of a sextic character, it is a cubic Gauss sum; no sextic/cubic Gauss
phase identity is required for this identification. The variable family
chi_(c n^3)(m) is NOT replaced by a cubic family in this note.

The CT general-field construction itself assumes a field containing mu_12;
Q(omega) does not satisfy that assumption. The theorem here is proved directly
over Q(omega), for the explicit theta above. Applying it to a particular
Eisenstein native construction requires checking that its angular/ray
correction has that form. The primary CT discussion of the older Eisenstein
argument records a fixed angular character and fixed ray factors; we do not
infer an entire general-field source by substituting K into its hypotheses.

## 2. The complete-vector theorem

Put kappa_S=pi/(6sqrt(3)) and

    J_P=integral_0^infinity |P(y)|^2 dy/y=1/(2sqrt(2pi)).

As Z tends to infinity,

    ||v(Z)||_2^2=||w(Z)||_2^2=kappa_S J_P+O(Z^(-1/3)),
    |<v(Z),w(Z)>|=O(Z^(-1/3)).                            (2)

Constants depend on the fixed angular/ray data and P. In particular the
normalized overlap is O(Z^(-1/3)). This is power orthogonality to ONE specified
radial Gauss coefficient vector. It does not control a full bad eigenspace,
angularly varying Gauss directions, or the norm of the sextic transform.

The same estimates hold for a fixed log-Schwartz profile P: require every
logarithmic derivative of |P(y)|^2 to decay faster than any power at both
endpoints. In the first line replace J_P accordingly. The stated Gaussian
satisfies these conditions. No finite cutoff is used in the proof.

## 3. Primary-lattice angular cancellation

Uniformly over every bounded choice of weights on the finitely many residue
classes modulo a fixed modulus, the full ideal angular sum satisfies

    sum_(NI<=X, exterior I) eta(alpha_I)
        (alpha_I/|alpha_I|)^m (NI)^(it0)=O(sqrt(X)), X>=1. (3)

Here m!=0 is essential. Write the primary generators as finitely many lattice
cosets after combining the primary, exterior and ray conditions. On a coset
the finite weight is constant. The continuous angular integral over any
centered circular annulus is zero. On an annulus of radius R>=1, the gradient
of (z/|z|)^m |z|^(2it0) is O_(m,t0)(1/R). Comparing lattice cells of fixed
diameter with their continuous integrals costs O(R): O(R^2) interior cells
have error O(1/R) each, and O(R) boundary cells have bounded contribution.
Dyadic annuli down to radius one sum to O(sqrt(X)). The bounded inner disk
costs O(1). This treats the origin explicitly. Multiplication by any bounded
finite list of coset weights preserves the uniform constant.

The same argument without the angular factor gives

    I_S(X)=kappa_S X+O(sqrt(X)).                           (4)

The full ideal count has residue pi/(3sqrt(3)). Equivalently the primary
coset alpha=1 mod(3), of index 9 in the element lattice, already deletes
the ideal above 3 and has density 2pi/(9sqrt(3)). Deleting also the ideal
above 2, of norm 4, leaves pi/(6sqrt(3)). Thus relative to the full ideal
count the two deleted factors are (1-1/4)(1-1/3)=1/2. Counting all ideals
gives I_S(X)<=3X, as also proved in
PROOF.md section 3. In particular

    sum_(NI<=U) 1/NI=O(log(2U)).                          (5)

## 4. Squarefreeness is retained by exact inversion

Use the ideal identity mu_K(I)^2=sum_(d^2|I)mu_K(d). For theta above,
write alpha_I=alpha_d^2 alpha_a. The angular/radial phase separates into a
unit factor depending on d and the same fixed nonzero angular order in a.
The finite weight becomes eta(alpha_d^2 alpha_a), still a bounded function
on the SAME finite residue group. Thus (3)'s constant is uniform in d,
even when eta is not multiplicative. Summing over Nd<=sqrt(X) gives

    sum_(NI<=X)^flat theta(I)=O(sqrt(X)log(2X)).           (6)

The superscript flat here means SQUAREFREE, not sixth-free. This is not an
uncontrolled character-family restriction. Formula (5) pays all square
divisors. No primes shared between later c,n indices have been removed.

Likewise (4) gives the complete squarefree counting formula

    I_S^flat(X)=kappa_sf X+O(sqrt(X)log(2X)),
    kappa_sf=kappa_S/zeta_K^S(2)>0.                       (7)

Indeed the absolutely convergent main coefficient is sum_d mu_K(d)/(Nd)^2;
its omitted tail beyond sqrt(X) is O(X^(-1/2)) by ideal counting. The lattice
error sums to O(sqrt(X)log(2X)). This proof imports no RH or Hecke zero bound.

## 5. Weighted complete squarefree sums

Set H(y)=|P(y)|^2. Stieltjes integration against (6)--(7) gives, for B>=1,

    S_0(B):=sum_c^flat H(Nc/B)/Nc
        =kappa_sf J_P+O(B^(-1/2)log(2B)),
    S_eta,m(B):=sum_c^flat eta(alpha_c)
        (alpha_c/|alpha_c|)^m (Nc)^(it0) H(Nc/B)/Nc
        =O(B^(-1/2)log(2B)).                             (8)

The latter estimate is uniform over bounded weights on the fixed ray group.
To see that both endpoint tails are paid, differentiate H(x/B)/x in the
Stieltjes integral. The resulting integrals are bounded by fixed moments of
y^(-3/2)(|H(y)|+y|H'(y)|)(1+|log y|), which converge at both endpoints.
The count error at x<1 is bounded by O(sqrt(x)log(2+x)) as well; alternatively
retain its exact zero count before integrating. There is no hidden boundary
term at x=1.

For 0<B<1 and EVERY fixed L>0, absolute ideal counting and rapid decay at
infinity yield

    |S_0(B)|+|S_eta,m(B)|<=C_L B^L.                       (9)

For example H(Nc/B)<=C_L B^L(Nc)^(-L); the remaining sum is a convergent
zeta_K^S(L+1). Constants are uniform in the bounded ray weights.

## 6. Every cube divisor is summed, with a power saving

The norm identity is

    ||v||_2^2=||w||_2^2=sum_n (Nn)^(-2) S_0(Z/(Nn)^3).   (10)

For the overlap, primary multiplicativity gives
theta(c n^3)=eta(alpha_c alpha_n^3)
*(alpha_n/|alpha_n|)^(3m)(Nn)^(3it0)
*(alpha_c/|alpha_c|)^m(Nc)^(it0).
For each n the outside factor has modulus one, and eta(alpha_c alpha_n^3)
is one of the bounded weights covered uniformly by (8)--(9). Thus

    |<v,w>|<=sum_n (Nn)^(-2)
      |S_(eta_n),m(Z/(Nn)^3)|.                           (11)

Put U=Z^(1/3). On Nn<=U the error in either formula is bounded by

    Z^(-1/2) sum_(Nn<=U) (Nn)^(-1/2)
                                log(2(U/Nn)^3)=O(Z^(-1/3)). (12)

For a fully uniform check, split Nn into (U/2^(j+1),U/2^j]. Ideal counting
bounds the weighted count in that shell by O(sqrt(U)2^(-j/2)), while the log
is O(j+1). The convergent sum of (j+1)2^(-j/2) proves (12). The final possibly
incomplete shell includes n=1 and obeys the same bound. This is why no log Z
loss remains after all cube divisors have been summed.

For Nn>U, take L=1 in (9). Its total is

    O(Z sum_(Nn>U)(Nn)^(-5))=O(Z U^(-4))=O(Z^(-1/3)).     (13)

The norm's omitted constant main term has size O(sum_(Nn>U)(Nn)^(-2))=
O(U^(-1)), too. Therefore (10)'s main coefficient is

    kappa_sf J_P sum_n (Nn)^(-2)
       =[kappa_S/zeta_K^S(2)]J_P zeta_K^S(2)=kappa_S J_P.

Equations (11)--(13) prove the overlap estimate and complete the proof of (2).

## 7. Interpretation and the remaining obstacle

The known cubic large-sieve lower-bound construction uses a radial profile
times a normalized cubic Gauss phase. A fixed nonzero angular correction
produces strong cancellation against that specified direction. In the complete
cube coefficient space, the angle tends to pi/2 at a proved power rate.

This does not prove that the native vector enjoys a perfectly orthogonal
large-sieve bound. The transform could have further angularly twisted bad
directions, and the actual varying characters are sextic until the specified
reflection changes the interaction. Removing the scalar phase theta changes
the coefficient vector and is used ONLY as a comparison, never as a substitute
for v in the source. A useful next theorem would control the complete transform
on the relevant angular class, or identify every polar bad direction with a
uniform remainder. The present result handles the literal known radial overlap.
