# Independent review of the cofactor root-average note

**Reviewer:** the coherent-identity agent, independently of the author of
the HLC root-average note. **Verdict:** pass for the exact identities,
fixed-label measure bounds and explicitly stated conditional interfaces.
This review approves no full HLC operator bound, native inverse moment,
or new zero-free region.

## 1. Exact reviewed objects

| Object | SHA256 | Git blob |
|---|---|---|
| `HLC_ROOT_AVERAGING.md` | `1f3cd6e20936830ee91ab8591c5d289133ecdcdf1339633df3231e47fd8f80b0` | `81b749827db0683341b82bab0ebd73a4fb17255b` |
| `check_hlc_root_averaging.py` | `22ca022f856927eaf1dd9ee9490797c95e941bddf8dc9a0ecddcd8d5a3e04c59` | `008c5bb5d9cb80e5641761716df623f679f30cbd` |

I read the full note, inspected the checker, and independently ran the
checker under `python -O`. The result was `passed`. The review is bound
to the hashes above, not to a branch name or an unverified later edit.

I also checked the source PDF used by this pass, SHA256
`32ef255566d4f3611d2d89c3a5f3db94c792883cc713d77a7f9d33b163f55e88`,
at pp. 22--24, equations (4.29)--(4.31); p. 25, equations
(4.33)--(4.35); p. 28, equation (4.40); and pp. 30--31, equation
(4.47) and its displayed dirty-window consequence. The source is
[Lü--Wang--Wu, arXiv:2610.20242v1](https://arxiv.org/pdf/2610.20242).

## 2. Integer lift, CRT grids and the moving center

The basic cofactor identity follows by writing
\(R=(s+k)/P\), \(0\le k<P\). The independent CRT residues are
\(k\bmod p_i\) **conditional on s**. The note does not mistakenly
claim independence of the whole continuous phase vector. Its exact
Fourier lattice follows by reducing a relation modulo each p_i.

For the moving dirty center, I checked the definitions

\[
 n_i=CP/p_i,\quad G=HP,\quad A_i=p_0n_i-G.
\]

The common shift when R is translated by an integer j is
\(-jG/p_0\) modulo one. Since \((G,p_0)=1\), the p_0 shifts
are exactly the original p_0 h residues. Thus averaging h **once**
turns the integral on [0,1] into \(p_0^{-1}\) times the integral
on [0,p_0]. The substitution R=p_0t cancels that factor. There is
no unpaid extension of the integration interval and no second line
draw.

The second split \(t=(s+k)/P\) gives

\[
 A_it=(p_0C-Hp_i)s/p_i+p_0Ck/p_i-Hk.
\]

The last term is an integer, and multiplication by p_0C permutes
each residue field. This verifies all normalizers in equations
(6)--(7). A translated p_i-point grid meets an arc of length ell_i
in at most p_i ell_i+1 points, proving the product upper bound.
The positive-frequency marginal claim is valid because each A_i is
a nonzero integer: A_i=0 would contradict p_0 not dividing G.

The source correspondence is exact for the stated fixed cofactor
family. In equation (4.47), the raw determinant is
\(j=G-p_0n_i\). The residue of the position coefficient h is
determined by the already named projective line, yielding precisely
the moving center in the note's equation (10). The incoming product,
the excluded current prime, and the cross-group coprimalities are
retained. The note does not identify every successive path edge with
this one fixed family.

For a fixed z,w of determinant one, the vectors Gw+hz label all
projective lines except [z] as h ranges modulo p_0. Their original
line measure is therefore p_0/(p_0+1) times the normalized h average.
The source line is impossible because the raw determinant is nonzero
modulo p_0. This explains, and pays, exactly the factor in (11).

## 3. Actual root measure and averaged ambiguity

I independently differentiated
\(R(r)=\tau_r(w)/\tau_r(z)\), with
\(\tau_r(z)=z_1-2rz_2\), obtaining

\[
                  R'(r)=-2/\tau_r(z)^2.
\]

The sign agrees with the source. Its retained range puts tau between
1/16 and 16, so \(|dr/dR|\le128\). For z_2 nonzero, the exact
identity

\[
 R(r)=w_2/z_2-1/(z_2\tau_r(z))
\]

puts the entire retained image in an interval of length less than
16. For z_2=0, primitivity and positive tau give z=(1,0), and the
image length is at most two. Hence at most 17 integer unit intervals
cover the image. The h-averaged density is one-periodic in R, again
because integer translation permutes h. This proves the stated
\(C_{\rm root}=128\cdot17=2176\), including fixed-label,
root-independent-data and unnormalized-measure qualifications.

Deleting endpoint, good-state or parity projectors is legitimate in
this nonnegative upper bound. It does not preserve a conditional
probability or its denominator. The other real source coordinates
remain fixed at this step, exactly as stated.

Expanding N(N-1) over **distinct** omitted primes and applying the
same two-event theorem gives (11d). The inequality
\(1_{N\ge2}\le N(N-1)/2\) then proves (11e), including the
factor \(\binom m2\), the once-only p_0/(p_0+1), and the
comparable-prime assumption p_i at least c p_0. This is an actual
\(O(m^2/p_0^2)\) bound for the fixed-family ambiguous mass under
the source's root-and-line measure. The total weight of a family
of label sets and any conditional history denominator remain unpaid;
the note states both limitations explicitly.

## 4. Conditional history and fixed-path prime returns

The conditional bound (12) divides the joint upper bound by the
**uniform model's exact** marginal ell_1. If a smaller past event
has relative mass rho within that event, its bound must acquire
rho inverse, as in (13). No exact marginal is asserted for the
restricted actual-root measure in (11c). The repeated-event negative
control is necessary: conditioning on one event cannot make its
identical repeat rare.

For the fixed-path divisor bound, distinct positive primitive integer
vertices have a nonzero determinant. A common recorded projective
line forces its prime to divide that one fixed integer. Counting
distinct prime divisors of size at least P_min gives (14), and the
original weight bound C/(Vp) is charged once. The exact repeated
position case is excluded for the right reason, determinant zero.

The note's later formula for Delta(p) shows why this divisor count
cannot be applied after selecting the successor separately for every
p. The position coefficient h(p) varies with p. I agree with that
scope restriction; there is no unjustified exchange of a fixed-path
sum and an O(1)-successor sum.

## 5. Eisenstein extension

The first equality of (17) uses that the translates Q+j for
representatives of \(\mathcal O/(\pi_0)\) form a fundamental
domain for the sublattice \(\pi_0\mathcal O\). The h=0
integrand is periodic under that sublattice. Multiplication by G
permutes the residues; scaling R=pi_0t multiplies real area by q_0
and cancels the q_0 normalizer.

For the second equality, multiplication by P on the complex torus
has degree NP. The CRT separates k modulo the nonassociate prime
elements, and the term Hk belongs to the integer ring. Thus the
same conditional grid structure holds without inventing independent
continuous complex phases.

I also checked the disk count. The pi_i-torsion grid has separation
at least \(q_i^{-1/2}\) between distinct lifts. Disks of radius
\(1/(2\sqrt{q_i})\) about grid points in an embedded disk of
radius r_i are disjoint and lie within the concentric disk of
radius \(r_i+1/(2\sqrt{q_i})\). Comparing their ordinary areas
gives \((2r_i\sqrt{q_i}+1)^2\). Dividing by q_i gives the
factor in (18). The disk radius assumption ensures an unambiguous
embedded lift, and the one line average is q_0/(q_0+1).

This is a theorem for a specified Haar root law. The note explicitly
does not claim that law for the Eisenstein inverse detector, or a
coefficient comparison with the native Möbius/Hecke expression.

## 6. Replay and limits

The optimized checker passed 18 exact lift/grid cases, 2,847 Fourier
relations, 42 marginal checks, 12 conditional-history checks, 18
factorial-ambiguity cases, 22 projective-line normalizer checks,
5,940 fixed-path divisor cases, 195 source Jacobians, 65 source
image cases, 8 exact source-root pullback integrals, 162 Eisenstein
Fourier lift checks, and 206 Eisenstein grid identities. Its three
negative controls remain active under optimization.

These finite checks support the algebra, measure changes and
normalizers. They do not independently certify the source's complete
root replacement or build the missing conditional history law.
The exact fixed-family arithmetic gains are approved at that scope.
