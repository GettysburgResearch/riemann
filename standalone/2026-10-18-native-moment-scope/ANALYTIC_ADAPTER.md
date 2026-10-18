# Uniform reciprocals from the family zero-free hypothesis

Status: PROPOSED complete classical analytic adapter. The zero-free
hypothesis is assumed here, not proved. No GRH-dependent conclusion is
used in the unconditional identities or mask-average lemma of PROOF.md.

The argument extends the conductor-free proof in the repository's
`research/integrated/2026-09-06/proof-extracts/D2.md`, R15 §1.
Borel–Carathéodory and Gaussian-damped three-lines are classical methods.
The contribution is their explicit uniform use with the precise inducing
conductor, zero extension and repeated rows in #976's native target.

## Analytic contracts

Fix F and finitely many finite-order archimedean types (the cited family
has trivial infinity type). For a primitive finite-order Hecke character
theta write Q>=1 for its conductor norm. Classical Hecke theory supplies:

* continuation to the plane, with at most the principal simple pole at 1;
* the functional equation and finite order in fixed vertical strips;
* for each fixed compact real strip, a polynomial upper bound in
  Q(2+|t|), uniform over these characters after removing the principal pole;
* an absolutely convergent Euler logarithm, uniformly bounded on
  Re s>=b for every fixed b>1.

The polynomial upper bound follows, for example, by bounding the Euler
product on a fixed line to the right of 1, applying the functional equation
and Stirling on a fixed left line, and applying Phragmen–Lindelof. All gamma
types and the field degree are fixed. No lower bound or Lindelof premise is
part of these unconditional contracts.

## Lemma R

Assume each primitive L(s,theta) under consideration is zero-free on
Re s>1/2. For any fixed sigma0>1/2 and eta>0,

    |1/L(s,theta)| <= C_(sigma0,eta,F) [Q(2+|Im s|)]^eta,
                                      Re s>=sigma0.       (R1)

The constant is uniform in theta and Q. The reciprocal of a principal pole
is assigned its removable value zero.

Proof. It suffices to treat sigma0<1; Euler convergence treats a right-hand
half-plane. Choose fixed

    1/2 < alpha0 < alpha < sigma0 < b,  b>1.

Put g_theta(s)=L(s,theta) for nonprincipal theta, and
g_theta(s)=(s-1)L(s,theta)/(s+1) for the principal character. This is
holomorphic and zero-free on Re s>1/2, including at s=1. There is a unique
analytic logarithm ell_theta there that agrees on Re s>1 with the Euler
logarithm and, in the principal case, the compatible logarithm of
(s-1)/(s+1). On Re s=b its modulus is uniformly bounded.

Apply Borel–Carathéodory to ell_theta on discs centered at b+it. Choose
outer radius b-alpha0 and inner radius b-alpha; both are fixed. The real
part is log|g_theta| and is O(log(2Q)+log(2+|t|)) on the outer disc by the
polynomial upper contract. The center value is uniformly bounded by its
Euler branch. Hence, uniformly throughout the closed strip [alpha,b],

    |ell_theta(x+it)| <= C [log(2Q)+log(2+|t|)].            (R2)

For a fixed t0 apply three-lines on [alpha,b] to

    ell_theta(s) exp[(s-sigma0-it0)^2].

At the left boundary its supremum is at most
C[log(2Q)+log(2+|t0|)]; at the right boundary it is at most C. The Gaussian
beats the logarithmic growth in (R2) as the imaginary part tends to either
infinity, so the infinite-strip application is legitimate. At s=sigma0+it0,
the Gaussian is 1. Therefore

    |ell_theta(sigma0+it0)|
      <= C [log(2Q)+log(2+|t0|)]^theta0,
    theta0=(b-sigma0)/(b-alpha) < 1.                      (R3)

The same estimate is uniform for sigma0<=Re s<=b (replace theta0 by the
largest interpolation exponent on that strip). For any eta>0,
exp(C(log X)^theta0)<=C_eta X^eta for X>=2. Exponentiate -Re ell_theta.
In the principal case, 1/L=[(s-1)/(s+1)]/g_theta and the displayed rational
factor has modulus at most 1 on Re s>0. This proves (R1) up to b. The Euler
side proves it for Re s>=b. QED.

## All imprimitive deletions, including repeated-row masks

Let theta_u be the primitive character inducing chi_u. The original
L^S(s,chi_u) is

    L(s,theta_u) product_(p in T_u) (1-theta_u(p)q(p)^(-s)), (R4)

where T_u consists of the omitted Euler primes, including S and any
additional modulus primes. The portion outside S divides rad(u), even
when u has sixth-power factors. Factors with theta_u(p)=0 can be retained
as 1. Their zeros all lie on Re s=0.

For fixed sigma0>0 and any rho>0,

    product_(p|u) (1-q(p)^(-sigma0))^(-1)
                                                <= C_(rho,sigma0,F) q(u)^rho. (R5)

To prove this without a prime-counting assumption, first take a norm cutoff
M so large that -log(1-q^(-sigma0))<=rho log q for q>M. There are finitely
many prime ideals of norm <=M, whose factors form a fixed constant. Sum
the large-prime inequalities and use product_(p|u)q(p)<=q(u). This proves
(R5), retaining all nonunit zeros through (R4).

Since Q_u<=C q(u), apply (R1) with a smaller preliminary exponent and then
(R5). The fixed S factors cost a constant. Renaming the losses proves

    |1/L^S(s,chi_u)| << (2+q(u))^eta (2+|Im s|)^eta,
                                      Re s>=sigma0>1/2.   (R6)

This is exactly the uniform bound used in Theorem A. It follows from the
family zero-free hypothesis plus the displayed classical contracts; it is
not an unstated uniformity assumption about separately chosen row constants.

The Gaussian inverse Mellin integral is absolutely convergent on every
such line, uniformly for q(u) in any specified finite cap. On a fixed strip
its horizontal integrals are bounded by a polynomial times exp(-tau T^2)
and tend to zero. Thus its contour shift really reproduces the literal
arithmetic A_u(D); it is not a new holomorphic function unrelated to the
initial source.
