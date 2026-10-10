# Complete-residue product moments and a positive fourth cumulant

Status: **Root-reviewed elementary finite-profile component lemmas C-P1--C-P4.**
The profile below is a complete squarefree hypercube over finitely many
prime ideals, rather than the native sharp norm band. It supplies no
infinite short-row upper bound, new zero-free region, or RH conclusion.
It complements the exact translation in `correlations/MOBIUS_CRT_TRANSLATION.md`.

Let P be a finite set of distinct Eisenstein prime ideals outside the
primes above 6. Average uniformly over the entire residue ring modulo
their product. The local sixth-residue variables Z_p=chi_p(u) are independent
under ideal CRT. Put rho_p=1-1/Np. Their exact law is

    Pr(Z_p=0)=1/Np,  Pr(Z_p=epsilon^j)=rho_p/6 (0<=j<6).

Thus E Z_p^i conjugate(Z_p)^j is one when i=j=0, and otherwise is
rho_p if i-j is a multiple of six, and zero if it is not. This retains
the nonunit mask even at a positive exponent divisible by six.

## C-P1. Exact every-order local polynomial

For real w_p>=0 define the finite Möbius product source

    X(u)=product_(p in P)(1-w_p Z_p(u))
        =sum_(A subset P) mu_K(n_A) product_(p in A)w_p chi_(n_A)(u).

For every integer k>=1, independence gives

    E|X|^(2k)=product_(p in P) L_k(w_p,rho_p),

where the exact local polynomial is

    L_k(w,rho)=1+rho sum_(i=1)^k binom(k,i)^2 w^(2i)
       +2rho sum_(h=1)^floor(k/6) sum_(j=0)^(k-6h)
                    binom(k,j+6h)binom(k,j) w^(2j+6h).

Indeed, expand (1-w Z)^k(1-w conjugate(Z))^k. The only surviving
terms have i-j divisible by six. Such i+j is even, so every surviving
sign is positive. The i=j=0 term is one; every other surviving term has
its rho mask. Grouping the diagonal and the two orientations of every
nonzero multiple-of-six difference gives precisely the displayed formula.

For k<=5 this equals the model with a uniform continuous unit-circle
variable and the same zero mask. At k=6 the additional term is 2rho w^6,
and at higher k all additional terms are positive. In particular the
first extra sixth-root moment collisions occur at moment order twelve,
not order six. This is the same exact mask distinction preserved by
PR914's complete-row diagonal formulas; it does not justify replacing
the native short norm-ball average by this complete residue law.

## C-P2. Exact centered fourth cumulant

Write

    A=product_p(1+rho_p w_p^2),
    B=product_p(1+2rho_p w_p^2),
    D=product_p(1+4rho_p w_p^2+rho_p w_p^4).

The mixed local character moments give

    E X=E X^2=1, E|X|^2=A,
    E(X^2 conjugate(X))=B, E|X|^4=D.

For Y=X-1, it follows that E Y=E Y^2=0 and E|Y|^2=A-1.
Expanding the centered fourth power gives

    E|Y|^4=D-4B+4A-1.

Consequently its complex fourth connected cumulant is exactly

    kappa_4=E|Y|^4-2(E|Y|^2)^2-|E Y^2|^2
           =D-4B+8A-3-2A^2.                         (C-P2)

This equality uses no Gaussian approximation. The Möbius signs do not
force the displayed expression to be nonpositive.

## C-P3. A uniform positive three-prime example

Take exactly three distinct prime ideals and w_p=1. Every Np>=7,
so all three rho_p lie in [6/7,1]. The polynomial (C-P2) is concave
separately in each rho_p: A,B,D are affine in each variable, and the
only quadratic part is -2A^2. Therefore its minimum on this cube is
at least the smallest vertex value, by three successive applications
of the concave chord lower bound. The vertex values depend only on
the number of coordinates equal to one:

| Number of rho coordinates equal to one | Exact vertex cumulant |
|---:|---|
| 0 | `3985434/117649` |
| 1 | `87023/2401` |
| 2 | `1893/49` |
| 3 | `41` |

All four are at least 3985434/117649>0. Thus every such three-prime
product profile has a strictly positive complete-residue fourth cumulant.
For the actual split ideals of norms 7,13,19, the exact value is

    kappa_4=8445096/229957>0.                         (C-P3)

This gives a finite-profile counterexample even under complete-residue
averaging. The positive cumulants of the native sharp bands recorded by
the root probe are a separate, source-specific counterexample. Neither
example supplies an asymptotic lower obstruction to the desired upper
moment estimate. The product profile may behave differently from a sharp
norm band or a fixed smooth dilation profile.

## C-P4. Exact source check and limits

`check_crt_product_moments.py` independently builds the three actual
split-field characters at norms 7,13,19, including all zero residues,
and enumerates all 1729 complete rows. It verifies the mean and mixed
moments in C-P2, every even moment through order sixteen in C-P1, the
strict extra sextic collisions at orders twelve, fourteen and sixteen,
and the exact positive centered cumulant. It also checks every exact
cube-vertex value used in C-P3. All checks use integer or rational
arithmetic and survive Python optimization.

The coefficients are a finite Möbius hypercube with arbitrary product
weights. Complete-residue independence is justified only for that entire
residue ring; it is not a hypothesis about the original short lattice
rows. Together with the CRT translation, this calculation rules out a
general negative-cumulant comparison based solely on the Möbius signs.
Further cancellation must use the norm profile and its incomplete-row
weight, rather than those signs alone.
