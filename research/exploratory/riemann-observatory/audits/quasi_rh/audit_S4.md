# Level-2 audit of Section 4: Poisson summation and the dual mean square

```text
Status:      Level-2 audit. Unrefereed object, independent audit. This is NOT a review approval of the paper.
Scope:       paper2.tex l.773-1253 (Lemma 4.1, Lemma 4.2, Definition 4.3, Lemma 4.4, Proposition 4.5),
             plus the parts of App. A.1 (l.2689-2872) and App. B (Lemmas B.1, B.2, l.3491-3615) that
             Section 4 invokes, and the interface with Sec. 5.4 (l.1611-1629) that supplies the
             hypothesis of Prop. 4.5.
Sources:     "The Quasi-Riemann Hypothesis" (OpenAI, Oct 5 2026), github.com/openai/math @ 4eaee87548250b2682affda7d05d947c05554bae,
             paper2.pdf sha256 f919b57829b178c8e60e7c17b018cf773e7907cf642ef5a3347d8a826e8dbf18 (re-hashed: matches).
             LaTeX (authoritative for formulas): scratchpad qrh/tex1112/paper2.tex. The Section 4 PDF text
             (qrh/sec_s4_poisson.txt) agrees with the LaTeX on every formula spot-checked.
             Dunn-Radziwill, arXiv:2109.07463 (rendered p.10 inspected for (2.1)-(2.3)).
What was run: our own Z[omega] code only (nothing from the OpenAI repository), python3 -I, in
             research/exploratory/riemann-observatory/experiments/code/quasi_rh/s4_*.py. See Sec. 9.
Smallest remaining gap: none found inside Section 4. Section 4 is a conditional reduction:
             Prop. 3.1 <= [Prop. 4.5 + hypothesis (eq:auxiliary-target)]. The hypothesis is the content of
             Secs. 5-7 (Prop. 5.1) and is outside this audit.
```

## 0. Verdict

* **verified_error:** none.
* **suspected_gap:** none.
* **unresolved_ambiguity:** one minor item (U-S4-1: theorem and equation numbers of the Iwaniec-Kowalski
  citations were not checked against the book). The mathematics behind them was re-derived and
  verified numerically, so nothing depends on it.
* **typo_or_presentation:** five harmless items (P-S4-1 to P-S4-5) and one auditor pitfall (A-S4-1).
* Every exact identity in Section 4 was checked by hand and then **verified numerically end to end**.
  The test computes M_D directly as a sum over u in O and compares it with each successive rewriting in the
  proof of Prop. 4.5, down to (eq:initial-column-output). It used a nontrivial nu, the inert prime 11, four
  values of H, and agreement to relative error <= 4e-15. Negative controls (deliberately wrong conventions)
  fail at O(1).
* Every inequality step (Lemma 4.4, supports, dyadic scales, kernel bounds, the application of Lemma B.2,
  and the final count) was re-derived by hand and is correct as stated.

Section 4 is an exact, essentially lossless (D^eps) duality. It reduces Prop. 3.1 to the bound
E(H,X,F) << D^eps XF, which is the optimal large-sieve size for the dual family, at row range
H <= C D^{1-theta}/B^2 and Sigma = XF = D/B. All the analytic difficulty of the paper sits in that hypothesis
(Secs. 5-7), not in Section 4.

## 1. Conventions re-derived (used throughout)

* `e(z) = exp(4 pi i Im z/sqrt3) = exp(2 pi i Tr(z/sqrt(-3)))`. Indeed z/(i sqrt3) has real part
  Im z/sqrt3, and Tr = 2 Re. The bilinear form B(z,w) = Tr(zw/sqrt(-3)) = (2/sqrt3) Im(zw) is
  nondegenerate on C = R^2. The dual of O under B is sqrt(-3) * (inverse different) = sqrt(-3) * (1/sqrt(-3)) O = O,
  so **O is self-dual**, and the dual of mO is m^{-1}O.
* covol(O) = sqrt3/2 for dx dy. The measure (2/sqrt3) dx dy gives O covolume 1, as stated at l.902.
  Lattice Poisson in the form sum_{k in a+mO} f(k) = N(m)^{-1} sum_{h in O} hat f(h/m) e(ah/m) holds with
  hat f(w) = (2/sqrt3) int f(z) e(-zw) dx dy. No Jacobian appears, because the pairing matrix cancels
  between the transform and the dual lattice.
* hat Phi is radial: rotating z leaves Phi(|z|^2) unchanged and rotates zw. Hence hat Phi(|w|^2) is well defined (l.899).
* Scaling: f(z) = Phi(|z|^2/H') gives hat f(w) = H' hat Phi(H'|w|^2).
* For a primitive chi mod m, sum_{x mod m} chi(x) e(xh/m) = conj(chi(h)) tau(chi) **for every h**. This
  uses that x -> e(x/m) is a primitive additive character mod m, which is exactly the self-duality above.
  The formula is independent of the generator chosen for m: replacing m by eps*m multiplies gamma by chi(eps)
  and conj(chi(h')) by conj(chi(eps)).

## 2. Section preamble and the ray-class absorption (l.775-818, l.955-956)

Claim: functions on a fixed ray class group can be expanded in the characters xi of that group. The modulus
is supported on S, divisible by cond(nu), and large enough that G and R factor through it.

Check: G(c) = conj(chi_c(4)) Gamma_quad(c) depends only on c mod 4, for c primary (see Sec. 3).
The ray class group mod 12 is isomorphic to (O/4)^x via primary generators. If two primary generators
c, c' satisfy c' = eps*alpha*c with alpha = 1 mod^x 12, then eps = 1 mod 3, so eps = 1. A modulus divisible by
12 * cond(nu) therefore suffices for Section 4, and S contains the primes above 2 and 3 by definition
(l.665-667). nu is a finite-order Hecke character of an imaginary quadratic field, hence a ray class character.
**No issue.**

## 3. Lemma 4.1 (l.823-857; proof App. A.1, l.2691-2872)

Statement: there are a unimodular class function G and a symmetric {+-1} bicharacter R on the ray class group,
with (recip), (gj), (g), and the consequences (convert1), (convert2), (crt-a) (a,b squarefree, l.854), and (quotient).

Hand checks.
* (gj), prime case. The substitution u = 2x-1 gives 4x(1-x) = 1-u^2, so chi_p(4)J(chi,chi) = J(chi,chi^3)
  (l.2700-2707). Gauss-Jacobi then gives gamma_1 gamma_3/gamma_4 = chi_p(4) gamma_1^2/gamma_2. With gamma_2 gamma_4 = 1
  this yields gamma_1 gamma_2 = conj(chi_p(4)) gamma_3 gamma_2^3 (l.2709-2726).
* The value J(chi^2,chi^2) = -p (l.2728-2762) has three parts, each re-derived. Divisibility by p: the
  power sums of exponents strictly between 0 and q-1 vanish. Norm q. The unit: J = -1 mod 3, because
  omega^j = 1 + j(omega-1) mod (omega-1)^2 and the product of x(1-x) over x != 0,1 equals (-1)^2 = 1. Since
  p = 1 mod 3, the unit is -1. This holds for split and for inert p. Hence gamma_2(p)^3 = -alpha(p).
* CRT. The decomposition x = b*y + a*z gives gamma_j(ab) = gamma_j(a)gamma_j(b) chi_a(b)^j chi_b(a)^j. For j=2,
  cubic reciprocity for primary (= 1 mod 3) elements gives (crt-a). This is valid for 1 mod 3 as well as
  for the Ireland-Rosen 2 mod 3 normalization, because (-1/.)_3 = 1. For j=3 the factor is the quadratic
  reciprocity quotient. Cubing kills the j=2 factor, so (gj) holds for squarefree n with one sign per prime.
* (g), second identity: g(chi) g(conj chi) = chi(-1) q for every nontrivial additive character, then CRT.
* (convert1) and (convert2) follow algebraically from (gj) and (g). I redid this. (quotient) follows from
  G(1) = 1, G(a^{-1}) = R(a,a) conj(G(a)) and R(a,a) = chi_a(-1).
* chi_c(4) = (4/c)_6 = (2/c)_3 = (-2/c)_3 = (c/-2)_3, read as c mod 2 in F_4^x (l.2849).

Imported results. Gauss-Jacobi [IK04 (3.18)] and g(chi)g(conj chi) = chi(-1)q are finite-field facts, valid
for any nontrivial additive character of O/p = F_q. Hasse's formula [Has50], as recorded in **DR (1.8)/(2.2)**
(arXiv:2109.07463, checked in the PDF): g~_DR(c)^3 = mu(c) c/|c|, with DR's additive character
exp(2 pi i (z + conj z)). The bridge is e(z) = e_DR(z/lambda) with lambda = 1+2omega = sqrt(-3). Hence
**gamma_2(n) = (lambda/n)_3 g~_DR(n)**, and the paper's (gj) is exactly DR (1.8). Verified numerically.
DR's twisted multiplicativity (2.3) reads g~(ab) = **conj**((a/b)_3) g~(a)g~(b) in the rendered PDF, which
matches (crt-a) since chi_b(a)^4 = (a/b)_3^2 = conj((a/b)_3). See A-S4-1.

Numerical checks (s4_lemma41_checks.py, s4_dr_bridge_check.py, s4_chirp_ft_check.py). 77 primes of norm <= 400,
split and inert (5, 11, 17), and 263 squarefree moduli with up to 3 prime factors and norm <= 1500.
All of the following hold with 0 failures:
* (gj), (g), (convert1), (convert2), |gamma_j| = 1, and gamma_3 = Gamma_quad on 263 moduli each;
* (crt-a): 214 pairs;
* R in {+-1}, symmetric, depends only on classes mod 4: 1754 pairs;
* R = (-1)^{eh+fg+fh} on square classes (143 of the 144 class pairs hit by coprime test pairs; the formula is also used on all 144 pairs in the (quotient) check);
* R = Gamma_quad(ab)/(Gamma_quad(a)Gamma_quad(b)) and G(ab) = G(a)G(b)R(a,b): 1754 pairs;
* G is a class function mod 4 (all 12 classes hit);
* (quotient) on all 144 class pairs;
* R(c,c) = chi_c(-1);
* chi_c(4) is a function of c mod 2;
* (quadratic-gaussian), the closed form (1+i^{-b}+i^a+i^{b-a})/2, and the square-class table,
  for 280 c coprime to 2, including non-primary c, c divisible by lambda, and non-squarefree c;
* the chirp-Gaussian Fourier transform at l.2796-2800, by 2-D quadrature: worst relative error 8e-14;
* gamma_2 = (lambda/n)_3 g~_DR and DR (1.8): 197 moduli; DR (2.3) with the overline: 351 pairs.

**No issue.** The previous architecture pass reached the same conclusion with separate code. This pass is
independent and wider: three-factor moduli, the bridge to DR, and the A.1 Fourier transform are new.

## 4. Lemma 4.2, Poisson summation with excluded primes (l.875-932)

Statement (eq:poisson):

sum_k chi(k) 1_{(k,r)=1} Phi(N k/H) = (H gamma(chi)/sqrt(N m)) sum_{d | rad r} mu(d) chi(d)/N(d) sum_h conj(chi(h)) hatPhi(H N h/(N d N m)).

For the principal character, the zero-frequency term is H hatPhi(0) prod_{p|r}(1 - 1/Np).

Hand derivation, step by step.
1. Inclusion-exclusion 1_{(k,r)=1} = sum_{d | (k, rad r)} mu(d). Then k = d*l for a **fixed generator** d.
   The identity is exact for any generator, including the non-primary generators of primes above 2 or 3,
   provided chi(d) uses the same generator.
2. Split by classes a mod m and apply Poisson on a + mO (dual lattice m^{-1}O, covolume N(m)) to
   f(z) = Phi(|z|^2/(H/N d)). This gives (1/N m) sum_h hat f(h/m) sum_a chi(a) e(ah/m) =
   (tau(chi)/N m) sum_h conj(chi(h)) (H/N d) hatPhi(H N h/(N d N m)).
3. Since tau(chi) = sqrt(N m) gamma(chi), the prefactor is H gamma(chi)/sqrt(N m) * mu(d)chi(d)/N(d). This
   matches (eq:poisson) exactly: normalization, the sign conj(chi(h)) rather than chi(-h), and the
   argument of hatPhi.
4. Principal case (m = 1, chi(0) = 1): the h = 0 term is H hatPhi(0) sum_{d|rad r} mu(d)/N d. Correct.
   At k = 0, the convention (0,r) = r is the one consistent with step 1.

Numerical checks (s4_poisson_checks.py), with Phi(t) = exp(-pi t) and closed form hatPhi(t) = (2/sqrt3) exp(-4 pi t/3).
* The closed form agrees with direct 2-D quadrature of the defining integral to relative error <= 3e-16.
  This checks the e(-zw) convention and the 2/sqrt3 factor independently.
* Plain lattice Poisson sum_k Phi(Nk/H) = H sum_h hatPhi(H N h): 4 values of H, relative error <= 2e-16.
  Omitting the covolume factor gives a 13% error (negative control).
* (eq:poisson) itself: 27 cases.
  * Characters chi_p^j (split and inert), conj(chi_z1) chi_z2 (the case used in Prop. 4.5), the principal
    character, and a character with two prime factors.
  * Exclusion ideals r containing 2 and lambda with non-primary generators, r sharing primes with m,
    and r coprime to m.
  * Values H in {0.7, 3.3, 17}.
  * Result: 0 failures.
* **Caveat about these tests (no issue in the paper).** With a *radial* weight, both sides of (eq:poisson)
  vanish identically whenever chi is nontrivial on the six units: summing over a unit orbit gives
  sum_eps chi(eps) = 0. Radial tests are therefore vacuous for most sextic chi. I added the same identity
  for a **shifted** Gaussian, where the proof produces the extra phase e(-z0 h/(dm)). This gives 21
  nontrivial cases with nonzero left-hand sides. All pass to relative error <= 5e-15.
* Negative controls: an imprimitive character, or chi(h) used in place of conj(chi(h)), fail with
  relative errors 0.83 and 0.62.

Remark (not used by the paper, harmless). In Prop. 4.5 the u-sum is radial, so only pairs (z1,z2) with
conj(chi_z1) chi_z2 trivial on the units contribute. All other pairs give 0 = 0.

**No issue.** For the imported citations, see U-S4-1.

## 5. Definition 4.3 (eq:energy, l.938-960)

E(H,X,F;xi,W) = (XF)^{-1} sum over squarefree f prime to S with F <= Nf < 2F, and over k in O with
0 < Nk <= H, of |sum*_n a_xi(n) chi_n(k) chi_n(f)^4 W(Nn/X)|^2. E_r adds the condition (n,r) = 1. The rows k
are elements, so each ideal is counted with its 6 unit multiples, which is consistent with k = e*h at
l.1144. **No issue.**

## 6. Lemma 4.4, removing exclusions (l.962-992)

Claim: E_r(H,X,F) <= tau(r_0) sum_{d|r_0} E(H, X/N d, F N d).

Check.
* (n,r) = 1 is equivalent to (n,r_0) = 1, because n is prime to S.
* Write 1_{(n,r_0)=1} = sum_{d|r_0} mu(d) 1_{d|n} and n = d*m, with m primary since d and n are primary.
* (crt-a) gives a_xi(dm) = a_xi(d) a_xi(m) chi_m(d)^4. The factor chi_m(d)^4 vanishes unless (m,d) = 1, so
  the m-sum may run over all squarefree m. Also chi_{dm}(f)^4 = chi_d(f)^4 chi_m(f)^4, and
  W(N(dm)/X) = W(N m/(X/N d)).
* The result is the displayed identity C_r(X;k,f) = sum_{d|r_0,(d,f)=1} mu(d) a_xi(d) chi_d(k) chi_d(f)^4 C_1(X/N d; k, df).
  It has exterior coefficients of modulus <= 1, since |gamma_2(d)| = 1.
* Cauchy-Schwarz over at most tau(r_0) = 2^{omega(r_0)} terms, then the injective map f -> df into the
  dyadic range [F N d, 2F N d), then positivity. The normalization (X/N d)(F N d) = XF is preserved.

Numerical check of the identity (s4_prop45_end_to_end.py): 300 random cases per run (r_0 with 1-3 primes,
random k and f, nontrivial xi, arbitrary complex weights), 4 runs, 0 failures. **No issue.**

## 7. Proposition 4.5, reduction to the dual mean square (l.1000-1252)

Statement. Fix 0 < theta <= 1/10, H = D^{1+theta}, C >= 1, real B, F >= 1, and the ranges
X = D/(BF), 0 < H_dual <= C D^2/(H B^2) (eq:initial-scales). Suppose that for each eps there is J(theta,eps)
with E(H_dual,X,F;xi,W) << ||W||_{C^J(I)}^2 D^eps XF for every compact I and W supported in I
(eq:auxiliary-target). Then Prop. 3.1 holds.

Step-by-step audit (H denotes D^{1+theta}, and H_dual denotes the dual row parameter written \mathcal H in the paper).

| step | lines | check | result |
|---|---|---|---|
| Choice of Phi >= 0, radial Schwartz, Phi >= 1 on [0,1], supp hatPhi in [0,C_Phi] | 1025-1027 | Exists: Phi(t) = c \|check psi(rho z)\|^2 with psi in C_c^infty radial, psi >= 0; hatPhi = c' (psi*psi~) rescaled has compact support; Phi(0) > 0 and continuity give Phi >= 1 on [0,1] after scaling. Not written in the paper (P-S4-2). | OK |
| Reduction to M_D | 1028-1034 | sum_{0<Nu<=H}\|A_u\|^2 <= D M_D because Phi >= 0 and Phi >= 1 on [0,1]; u = 0 is included in M_D and harmless | OK |
| Expansion, g = (n1,n2), n_j = g z_j | 1035-1041 | squarefree: (z1,z2) = (z1 z2, g) = 1; conj(chi_{n1}(u)) chi_{n2}(u) = 1_{(u,g)=1} conj(chi_{z1}(u)) chi_{z2}(u); mu(n1)mu(n2) = mu(z1)mu(z2); \|nu(g)\|^2 = 1 | OK |
| Poisson (eq:initial-poisson-rows) | 1042-1053 | Lemma 4.2 with chi = conj(chi_{z1}) chi_{z2}, primitive of modulus z1 z2 (each local factor is a nontrivial character mod a prime), r = g = rad g | OK |
| Zero frequency Z | 1054-1061 | only z1 = z2 = 1; Z = (H/D) hatPhi(0) sum_g \|W\|^2 prod(1 - 1/Np) <<_{Phi,I} H \|\|W\|\|_inf^2 (O(D) ideals g with Ng <= b_0 D) | OK |
| (eq:initial-paired-gauss) | 1063-1070 | CRT gives gamma(conj chi_{z1} chi_{z2}) = conj(chi_{z1}(z2)) chi_{z2}(z1) gamma_{-1}(z1) gamma_1(z2). Then (convert2) for z1, (convert1) for z2, (recip) giving conj(chi_{z1}(z2)) chi_{z2}(z1) = R(z1,z2), and (quotient) give conj(nu(z1)) nu(z2) G(z2 z1^{-1}) a(z1) conj(a(z2)) = sum_xi c_xi a_xi(z1) conj(a_xi(z2)) with Psi(t) = conj(nu(t)) G(t^{-1}). At z1 = z2 = 1 both sides equal 1. | OK |
| Normalization H N(g)/D^2 and W_0 = x^{-1/2} conj(W) | 1071-1099 | (1/D) conj(W(x1)) W(x2) H/sqrt(N z1 N z2) = (H N g/D^2) W_0(x1) conj(W_0(x2)), with x_j = N(g z_j)/D; chi(e) conj(chi(h)) = chi_{z1}(h e^5) conj(chi_{z2}(h e^5)) using conj(chi_z(e)) = chi_z(e^5) | OK |
| \|M_D - Z\| << max_xi \|S_xi\| | 1076-1080 | \|c_xi\| <= 1 and the set of xi is fixed and finite | OK |
| Insertion of v | 1106-1140 | z_j = v m_j, a_xi(v m) = a_xi(v) a_xi(m) chi_m(v)^4, \|a_xi(v) chi_v(h e^5)\|^2 = 1_{(v,h)=1} since (v,e) = 1; conditions (g,v) = 1, (m1 m2, g v) = 1; hatPhi argument H N h/(N e N v^2 N m1 N m2) | OK |
| Bijection (g,e,v,h) <-> (b,f,k) | 1141-1154 | e = (f,k) because (ev, eh) = e(v,h) = e; inverse well defined; (b,f) = 1 iff (g,v) = 1 and g squarefree; g v = b f; h e^5 v^4 = k f^4; mu(e)mu(v) = mu(f); N g/N e = N b; the hatPhi argument becomes H N k/(N f^2 N m1 N m2) | OK |
| (eq:initial-column-output) | 1155-1175 | (m_j, f) = 1 is enforced by chi_{m_j}(f^4); (m_j, b) = 1 is kept explicitly | OK |
| Supports | 1176-1180 | N b N f <= N(b f m_1) <= b_0 D; N(f m_1) N(f m_2) <= (b_0 D/N b)^2 gives N k <= C_Phi b_0^2 D^2/(H N b^2) | OK |
| Dyadic scales | 1182-1190 | X = D/(BF), H_dual = C_{I,Phi} D^2/(H B^2) >= C_Phi b_0^2 D^2/(H B^2) >= all k in the support; XF = D/B; (eq:initial-scales) holds with C = C_{I,Phi} >= 2 >= 1 | OK |
| Kernel K_{b,f,k} | 1191-1205 | W_0(N(bfm)/D) = W_0(r x) with r = Nb Nf/(BF) in [1,4) and x = N m/X; hatPhi argument = a/(x1 x2), a = H N k/(N f^2 X^2) <= C_{I,Phi} F^2/N f^2 <= C_{I,Phi}; support in [a_0/4, b_0]^2 since x in [a_0/r, b_0/r]; C^q norm << \|\|W\|\|^2_{C^q(I)}, uniform in a in (0, C] and r in [1,4) | OK |
| S_U and Lemma 4.4 | 1206-1224 | sum_{f,k} \|S_U\|^2 = XF E_{(b)}; shifts (X,F) -> (X/N d, F N d) keep B, H_dual and XF = D/B, so (eq:initial-scales) holds; tau(b)^2 <<_eps D^{eps/4}; hypothesis applied at eps/4 on I_* = [a_0/8, 2b_0] | OK |
| Application of Lemma B.2 | 1225-1234 | rows (f,k), w_r = 1, c_r = mu(f) 1_{(f,b)=1}, a_{1,r} = a_{2,r}, x_{r,n} = N n/X; Lemma B.2's I = [a_0/4, b_0] lies in int I_* = (a_0/8, 2b_0); m = J and q = 2J+4 (even; the integral (1+\|s\|)^m (1+\|t\|)^m (1+\|s\|+\|t\|)^{-q} converges iff q > 2m+2); enlarged rows have vanishing kernel | OK |
| Final count (eq:weighted) | 1235-1246 | (H/D^2) * sum_{N b ~ B} N(b) * (XF)^2 << (H B/D^2) * B * (D/B)^2 = H | OK |
| Dyadic sum, restore D | 1247-1250 | O((log D)^2) pairs (B,F), since B, F <= b_0 D; sum \|A_u\|^2 <= D M_D << D^{2+theta+eps} \|\|W\|\|^2_{C^{J'}} with J' = 2J(theta, eps/4) + 4 | OK |

**End-to-end numerical test of the identity chain** (s4_prop45_end_to_end.py). Toy instance: S = {2, lambda, 5},
nu((t)) = psi(N t) with psi of order 4 mod 5 (a nontrivial ray class character), D = 1, and W an arbitrary
complex function of Nn supported on Nn <= NMAX. The identities are exact and do not need smoothness.
Phi(t) = e^{-pi t}, so hatPhi is not compactly supported, but every identity remains exact with rapidly
convergent h-sums. Levels compared:
* L0: the direct u-sum of M_D;
* L1: Z plus Lemma 4.2 per (g, z1, z2), with gamma(conj chi_{z1} chi_{z2}) computed by brute force;
* L2: Z plus sum_xi c_xi S_xi in the (g,e,h,z1,z2) form, with Psi evaluated on classes mod 4 using
  brute-force G;
* L3: Z plus (eq:initial-column-output) in the (b,f,k,m1,m2) form.

| H | NMAX | columns | (b,f,m1,m2) terms | M_D | M_D - Z | max relerr (L1, L2, L3) |
|---|---|---|---|---|---|---|
| 19.7 | 100 | 28 | 940 | 1418.28 | 333.19 | 1.8e-15 |
| 5.3 | 100 | 28 | 940 | 569.32 | 277.39 | 3.8e-15 |
| 41.0 | 130 | 35 (incl. inert 11) | 1395 | 3433.42 | 130.21 | 9.3e-16 |
| 12.5 | 160 | 45 (incl. inert 11) | 2335 | 1501.47 | 294.33 | 3.6e-15 |

Negative control: using G(z1 z2^{-1}) in place of G(z2 z1^{-1}) in Psi gives relative errors from 2e-2
to 5e-1. The off-diagonal part M_D - Z is a large share of M_D, so the test has power. In addition,
s4_paired_crt_check.py verifies the CRT factorization of gamma(conj chi_{z1} chi_{z2}) and
(eq:initial-paired-gauss) with the nontrivial nu: 660 coprime pairs with N(z1 z2) <= 3000, 0 failures.

Sizes (main and error terms). The diagonal Z is of size H||W||^2. The off-diagonal is
<< D^eps H ||W||^2, conditional on the hypothesis. Hence sum |A_u|^2 << D^{1+eps} H. This is the diagonal
(square-root cancellation) size, so the reduction loses only D^eps. The hypothesis demands the
optimal-large-sieve size: E << D^eps XF, with H_dual/Sigma <= C D^{-theta}/B. This positive gap is what
Sec. 5 needs (eq:positive-gap) with kappa = theta/2.

Interface with Sec. 5.4 (l.1613-1629). Prop. 5.1 is applied with kappa = theta/2 and C_0 = 2, for
D >= C^{2/theta}. Here H_dual/Sigma <= C D^{-theta}/B and Sigma = D/B <= D^2. The cases X < 1, H_dual < 1
and bounded D are handled by counting. The derivative order J(kappa, C_0, eps) supplied this way does
**not** depend on C, so the order k(theta, eps) in Prop. 3.1 does not depend on I. See P-S4-1. **No issue.**

## 8. Findings

| id | location | class | severity | statement |
|---|---|---|---|---|
| U-S4-1 | l.923-926, l.813, l.2709 | unresolved_ambiguity | cosmetic | The theorem and equation numbers [IK04 Thm 4.5] (lattice Poisson), [IK04 (3.12)] (primitive Gauss sum), [IK04 (3.18)] (Gauss-Jacobi) and [IK04 Sec. 3.1] were not checked against the book, which was not available. The statements used are standard. They were re-derived for O = Z[omega], where they need self-duality of O under e and finite-field facts, and verified numerically (Secs. 3-4). Nothing load-bearing depends on the numbering. |
| P-S4-1 | l.1001-1013 vs l.1029-1030 | typo_or_presentation | cosmetic | Quantifier order. "For each fixed C >= 1 ... there exists J = J(theta, eps)" does not say explicitly that J is independent of C. The proof uses C = C_{I,Phi}, which depends on I, so a C-dependent J would make k in Prop. 3.1 depend on I, contrary to its statement. This is resolved by Sec. 5.4, whose J comes from Prop. 5.1 with (kappa, C_0) = (theta/2, 2) and is independent of C. It would also be harmless for Theorem 1.1, where W is fixed. |
| P-S4-2 | l.1025-1027 | typo_or_presentation | cosmetic | The existence of a radial Schwartz Phi >= 0 with Phi >= 1 on [0,1] and compactly supported hatPhi is asserted without construction. It is standard: Phi = c \|check psi(rho .)\|^2. |
| P-S4-3 | l.1188 | typo_or_presentation | cosmetic | The "2" in C_{I,Phi} = max(2, C_Phi b_0^2) is unexplained. Only C_{I,Phi} >= max(1, C_Phi b_0^2) is used. |
| P-S4-4 | l.1203, l.1230-1238 vs l.3563 | typo_or_presentation | cosmetic | Notation overload. I denotes the support interval [a_0,b_0] and also Lemma B.2's inner interval, which is instantiated as [a_0/4, b_0]. C denotes both a constant and C^q norms. N denotes the norm. The intended meaning is clear from context. |
| P-S4-5 | l.877 | typo_or_presentation | cosmetic | "Phi(N(k)/H) a smooth radial Schwartz weight": what is meant is that z -> Phi(\|z\|^2) is Schwartz on C. Harmless. |
| A-S4-1 | DR (2.3), (5.7) | typo_or_presentation (auditor pitfall, not a paper defect) | cosmetic | pdftotext drops overlines in DR. The rendered DR p.10 shows g~(ab) = conj((a/b)_3) g~(a) g~(b). This matches (crt-a) (chi_b(a)^4 = conj((a/b)_3)). The text extraction would wrongly suggest a conjugation mismatch, as with DR (5.7) noted in the architecture pass. |
| O-S4-1 | l.1042-1061 | no_issue_found_in_inspected_portion | n/a | Observation: with a radial row weight, pairs (z1,z2) with conj(chi_{z1}) chi_{z2} nontrivial on the units contribute exactly 0 after Poisson. Both sides vanish, nothing is lost, and the paper does not need this. |
| N-S4-1 | l.823-857, l.2691-2872 | no_issue_found_in_inspected_portion | n/a | Lemma 4.1 and its App. A.1 proof: all identities hand-checked and numerically verified (Sec. 3). |
| N-S4-2 | l.875-932 | no_issue_found_in_inspected_portion | n/a | Lemma 4.2: normalization (2/sqrt3, dual lattice m^{-1}O, conj(chi(h)), H/N d, gamma/sqrt(N m)) re-derived; 56 numerical cases including 21 shifted (non-vacuous) cases; negative controls fail. |
| N-S4-3 | l.938-992 | no_issue_found_in_inspected_portion | n/a | Definition 4.3 and Lemma 4.4: identity verified numerically in 1200 cases; Cauchy-Schwarz, injectivity and dyadic enlargement correct. |
| N-S4-4 | l.1024-1252 | no_issue_found_in_inspected_portion | n/a | Prop. 4.5: the exact identity chain from M_D to (eq:initial-column-output) verified end to end (4 instances, relative error <= 4e-15). Supports, scales, kernel bounds, the use of Lemma B.2 and the final count H all re-derived. |

## 9. Code and reproduction

All scripts are in `research/exploratory/riemann-observatory/experiments/code/quasi_rh/`. Run each one as
`python3 -I <script> [args]`. The code is ours; no OpenAI repository code was executed.

| script | what it authenticates | result |
|---|---|---|
| `s4_zw.py` | Z[omega] arithmetic, sextic symbol via x^{(q-1)/6} on O/p (split: Z/q; inert: F_{l^2}), e(z), residue systems by HNF, Gauss sums by brute force | library |
| `s4_lemma41_checks.py` | Lemma 4.1 identities, R and G as class functions, (quotient) on all classes, (quadratic-gaussian), closed form, square-class table | 0 failures (all counts in Sec. 3) |
| `s4_dr_bridge_check.py` | gamma_2 = (lambda/n)_3 g~_DR; DR (1.8); DR (2.3) with the overline | 0 / 197, 0 / 197, 0 / 351 |
| `s4_chirp_ft_check.py` | App. A.1 chirp-Gaussian Fourier transform (l.2796-2800) by quadrature | relative error <= 8e-14 |
| `s4_poisson_checks.py` | hatPhi closed form vs quadrature; lattice Poisson; Lemma 4.2 (radial and shifted); negative controls | 56 tests, 0 failures; controls fail |
| `s4_paired_crt_check.py` | CRT factorization of gamma(conj chi_{z1} chi_{z2}); (eq:initial-paired-gauss) with nu != 1 | 0 / 660 |
| `s4_prop45_end_to_end.py H NMAX` | M_D = Z + L1 = Z + L2 = Z + L3 (Prop. 4.5 identity chain); Lemma 4.4 identity | see Sec. 7 table; Lemma 4.4 0 / 300 per run |

What these checks do **not** authenticate. They do not test the hypothesis (eq:auxiliary-target), i.e. Prop. 5.1
and everything in Secs. 5-7 and App. A.2. They do not test the analytic inequalities (Lemma B.2, the kernel bounds),
which were checked by hand only. The toy instances are tiny, so they test identities, not sizes. The Lean formalization
of the companion 7/8 theorem was not replayed.
