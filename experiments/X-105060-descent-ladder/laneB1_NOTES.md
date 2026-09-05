# Lane B1 — Strip + Conservation + Rolle + Monotone Ladder
Status: in progress. All derivations independent of the orchestrator note (which was re-checked and corrected where wrong; see §6).

## §0 Conventions

xi(s) = (1/2) s(s-1) pi^{-s/2} Gamma(s/2) zeta(s); entire of order 1, xi(s) = xi(1-s), real on R and on the critical line. Xi(t) := xi(1/2 + it); real entire, EVEN, order 1. Xi_k := (d/dt)^k Xi, so Xi_k(t) = i^k xi^{(k)}(1/2 + it) (chain rule d/dt = i d/ds).

Map t <-> s = 1/2 + it. A zero rho = beta + i gamma of xi corresponds to t = gamma - i(beta - 1/2): Re t = gamma, Im t = 1/2 - beta... (check: s = 1/2 + it = 1/2 + i Re t - Im t; so beta = 1/2 - Im t, gamma = Re t). So the s-strip 0 <= beta <= 1 is exactly |Im t| <= 1/2, and the count N_0(T) of zeros of Xi with 0 < Re t <= T equals the classical N(T) = #{rho : 0 < gamma <= T} (with multiplicity).

N_k(T) = # zeros of Xi_k with 0 < Re t <= T (multiplicity); N_k^r(T) real ones; D_k(T) = # DISTINCT real zeros in (0, T].

Parity: Xi even => Xi_k(-t) = (-1)^k Xi_k(t). Reality: Xi real entire => all Xi_k real entire, i.e. Xi_k(conj t) = conj Xi_k(t).

---

## §1 STRIP LEMMA

**Theorem 1 (Strip Lemma).** For every k >= 0, every zero of Xi_k lies in the closed strip |Im t| <= 1/2. Equivalently, every zero of xi^{(k)} lies in 0 <= Re s <= 1.

**Classical facts invoked** (each with hypotheses checked below):

- (F1) Hadamard factorization, genus-0 case: an entire function G of order < 1 with G(0) != 0 satisfies G(w) = G(0) prod_n (1 - w/w_n) over its zeros (with multiplicity), the product converging absolutely and locally uniformly. [Titchmarsh, *Theory of Functions*, §8.24; Conway, *Functions of One Complex Variable*, XI.3.]
- (F2) The derivative of an entire function of order rho has order <= rho. [Boas, *Entire Functions*, §2.9; or directly by Cauchy's estimate |f'(z)| <= max_{|w-z|=1}|f(w)|.]
- (F3) Exponent of convergence of the zeros of an entire function <= its order; in particular for order <= 1, sum_{z_n != 0} |z_n|^{-2} < infinity. [Titchmarsh, *Theory of Functions*, §8.22 (Borel).]
- (F4) Gauss–Lucas: the zeros of P' lie in the convex hull of the zeros of P, for ANY complex polynomial P (no reality needed). [Marden, *Geometry of Polynomials*, Thm 6.1.]
- (F5) Hurwitz: if f_n -> f locally uniformly on a domain Omega, f not identically 0, and f(z_0) = 0 for z_0 in Omega, then every neighborhood of z_0 contains zeros of f_n for all large n. [Conway, VII.2.5.]
- (F6) All zeros of xi lie in 0 <= Re s <= 1 (indeed 0 < Re s < 1): zeta(s) != 0 for Re s > 1 by the Euler product; the poles of Gamma(s/2) at s = 0, -2, -4, ... are cancelled/removed and xi(s) != 0 for Re s > 1 since s(s-1)Gamma(s/2)zeta(s) != 0 there; the functional equation xi(s) = xi(1-s) gives Re s < 0. [Titchmarsh, *Theory of the Riemann Zeta-Function* (TZF), §2.12.]
- (F7) xi has order 1; hence Xi(t) = xi(1/2+it) has order 1 in t. [TZF Thm 2.12.]

**Proof.** Induction on k. The inductive hypothesis H_k: Xi_k is a real entire function of order <= 1, of parity (-1)^k, not identically zero, with all zeros in |Im t| <= 1/2.

H_0 holds by F6, F7, and the given parity/reality of Xi. (Xi not identically 0: it has order exactly 1 and Xi(0) = xi(1/2) != 0.)

Inductive step H_k => H_{k+1}. Let m >= 0 be the order of vanishing of Xi_k at t = 0 and write Xi_k(t) = t^m E(t) with E entire, E(0) != 0. Since Xi_k has parity (-1)^k, E is EVEN (an odd entire function nonvanishing at 0 is impossible; parity of t^m E forces E even after extracting the full power t^m: if E were odd it would vanish at 0). E has order <= 1 (removing a polynomial factor does not raise order beyond max(order,0)).

Since E is even, G(w) := sum-of-even-coefficients form, i.e. the unique entire function with G(t^2) = E(t), is entire; from |E(t)| <= exp(|t|^{1+eps}) for large |t| we get |G(w)| <= exp(|w|^{(1+eps)/2}), so G has order <= 1/2 < 1. By F1,
  G(w) = G(0) prod_n (1 - w/w_n),
absolutely and locally uniformly, over the zeros w_n of G with multiplicity. The zeros of E are exactly the two square roots ±tau_n of each w_n (tau_n != 0), with matching multiplicities, and sum 1/|w_n| = sum 1/|tau_n|^2 < infinity, consistent with F3. Substituting w = t^2:
  Xi_k(t) = c t^m prod_n (1 - t^2/tau_n^2),   c = Xi_k^{(m)}(0)/m!,
absolutely and locally uniformly convergent.

Let P_N(t) := c t^m prod_{n<=N} (1 - t^2/tau_n^2). Each P_N is a polynomial whose zeros are 0 (if m>0) and ±tau_n, n <= N — ALL in the closed strip S := {|Im t| <= 1/2} by H_k. S is convex and closed, so by F4 all zeros of P_N' lie in S. P_N -> Xi_k locally uniformly (absolute convergence of the product), hence P_N' -> Xi_{k+1} locally uniformly (Cauchy integral formula on compacts). 

Suppose Xi_{k+1}(t_0) = 0 with |Im t_0| > 1/2. Apply F5 on the domain Omega = {Im t > 1/2} (or its mirror): Xi_{k+1} is not identically zero (else Xi_k is a polynomial, contradicting that Xi_k has infinitely many zeros — it does, since Xi does (order-1 with sum 1/|zeros| divergent; or simply the infinitude of zeta zeros) and by the just-established product representation Xi_k is a polynomial iff its zero set is finite iff ... in any case if Xi_{k+1} ≡ 0 then Xi_k is constant, impossible since Xi_k -> has zeros and c != 0 — cleanest: Xi_{k+1} ≡ 0 => Xi_k constant => Xi is a polynomial of degree <= k, contradicting order 1 with infinitely many zeros). So F5 gives zeros of P_N' arbitrarily close to t_0 for large N; but a disk around t_0 of radius (|Im t_0| - 1/2)/2 misses S, where all zeros of P_N' live. Contradiction. Hence all zeros of Xi_{k+1} are in S.

Reality of Xi_{k+1}: derivative of real entire is real entire. Parity: (-1)^{k+1}. Order <= 1: F2. Not identically 0: shown above. H_{k+1} holds. QED.

Remarks. (i) We only get the CLOSED strip even though Xi's zeros are in the open strip; that is all we need (contour at |Im t| = 1 stays zero-free). (ii) The infinitude-of-zeros point: N_k(T) -> infinity also follows independently from §2's Riemann–von Mangoldt corollary, but the proof above only needs "Xi is not a polynomial", which is F7 + Hadamard (order 1 exactly, and xi has infinitely many zeros — classical, TZF §2.12/§9.2 — either suffices).

**Rejected variant (recorded).** The note's "second route" via Re(xi'/xi) > 0: pairing zeros rho and 1-conj(rho), the two terms Re 1/(s-rho) + Re 1/(s-(1-conj rho)) = a/(a^2+c^2) + b/(b^2+c^2) with a = sigma - beta, b = sigma - (1-beta), same c = tau - gamma; a+b = 2 sigma - 1 > 0 for sigma > 1/2 does NOT force positivity termwise: a/(a^2+c^2)+b/(b^2+c^2) = (a+b)(ab+c^2)/((a^2+c^2)(b^2+c^2)), negative when ab + c^2 < 0 (e.g. c = 0, b < 0 < a). Termwise positivity holds only for sigma >= 1 (both a,b > 0), which puts zeros of xi' in 0 <= Re s <= 1 by symmetry, but the INDUCTION step then needs a Hadamard product for xi^{(k)} with the symmetric pairing and a vanishing linear coefficient — doable but messier than Route 1. Not pursued.

---

## §2 CONSERVATION LEMMA

**Theorem 2 (Conservation).** For every k >= 0 there are explicit constants A_k, B_k, T_k (defined in the proof; admissible values A_k = 70 + 6k) such that for all T >= T_k,
  |N_{k+1}(T) - N_k(T)| <= A_k log T + B_k.
In particular N_{k+1}(T) = N_k(T) + O_k(log T).

**Corollary 2.1 (Riemann–von Mangoldt on every rung).** N_k(T) = (T/2pi) log(T/2pi) - T/2pi + O_k(log T), with error coefficient <= [classical RvM constant] + sum_{j<k} A_j. (Telescoping Theorem 2 from the classical k = 0 case, N_0(T) = N(T), TZF Thm 9.4.)

### §2.1 Sub-lemma A (log-derivative expansion right of the strip)

Notation: l(s) := (1/2) log(s/(2pi));  l0(x) := (1/2) log(x/(2pi));
L(s) := xi'/xi(s) = 1/s + 1/(s-1) - (1/2)log pi + (1/2)psi(s/2) + zeta'/zeta(s)   (log-differentiate the definition of xi; psi = digamma).

**Fact S (Stirling for psi).** For Re z >= 5/8: |psi(z) - log z| <= 0.64/|z|.
Proof: Binet-type formula psi(z) = log z - 1/(2z) - 2 int_0^infty t dt/((t^2+z^2)(e^{2pi t}-1)), valid Re z > 0 [Whittaker–Watson §12.3]. For Re z >= 5/8: |t^2+z^2| = |z-it||z+it| >= (5/8)|z| (one factor >= Re z >= 5/8, the larger >= |z|), and int_0^infty t/(e^{2pi t}-1) dt = 1/24. So the integral term is <= 2*(8/(5|z|))*(1/24) = 2/(15|z|); total <= 1/(2|z|) + 2/(15|z|) < 0.64/|z|.

**Fact Z.** For sigma >= 5/4: |zeta'/zeta(sigma+ix)| <= sum Lambda(n) n^{-5/4} = -zeta'/zeta(5/4) =: Z1 (numeric: Z1 = 3.46665..., verified run). Similarly |log zeta(sigma+ix)| <= log zeta(5/4) for sigma >= 5/4.

**Consequence.** On sigma in [5/4, 5], x >= 40:
  L(s) = l(s) + E(s),  |E(s)| <= 1/|s| + 1/|s-1| + 1.28/|s| + Z1 <= Z1 + 4.7/x <= B := Z1 + 9/8  (generous; B = 4.5916...).
[(1/2)psi(s/2) = (1/2)log(s/2) + err, |err| <= (1/2)(0.64)/(|s|/2) = 0.64/|s|... correction: (1/2)*0.64/|s/2| = 0.64/|s|; and (1/2)log(s/2) - (1/2)log pi = l(s).]

**Sub-lemma A.** Define regions Omega_k := {sigma + ix : sigma in [5/4 + eps_k, 5 - eps_k], x >= a_k}, eps_k := (1/8)(1 - 2^{-k}), r_k := 2^{-k-4} (so eps_{k+1} = eps_k + r_k). Define
  C_0 = 0,  C_{k+1} := C_k + 2B + k + 2^{k+1}   (closed form C_k = 2kB + k(k-1)/2 + 2^{k+1} - 2),
  a_0 := 40,  a_{k+1} := max(a_k + 1, 2 pi exp(16 C_{k+1})).
Then on Omega_k:
  xi^{(k)}(s) = xi(s) l(s)^k (1 + delta_k(s)),  |delta_k(s)| <= min( C_k / l0(x), 1/8 ).

Proof by induction; delta_0 = 0. Differentiating xi^{(k)} = xi l^k (1+delta_k):
  1 + delta_{k+1} = (1+delta_k)(1 + E/l) + k (l'/l^2)(1+delta_k) + delta_k'/l.        (*)
Bounds on Omega_{k+1}: |l(s)| >= (1/2) log|s/2pi| >= l0(x) > 0 for x > 2pi. |E| <= B. |l'| = 1/(2|s|) <= 1/(2x). Cauchy on the disk of radius r_k about s (contained in Omega_k since the sigma-margin grows by exactly r_k and x - r_k >= a_k because a_{k+1} >= a_k + 1): |delta_k'(s)| <= (1/r_k) sup |delta_k| <= 2^{k+4} * (1/8) = 2^{k+1}. Hence from (*), using |1+delta_k| <= 9/8:
  |delta_{k+1}| <= C_k/l0(x) + (9/8)B/l0(x) + (9/8)k/(2x l0(x)^2) + 2^{k+1}/l0(x)
              <= [C_k + 2B + k + 2^{k+1}]/l0(x) = C_{k+1}/l0(x),
and C_{k+1}/l0(x) <= 1/8 for x >= 2 pi exp(16 C_{k+1}). QED.

(The a_k are enormous — exp of exp-type in k — but explicit; only additive constants B_k, T_k inherit them. The log T coefficient A_k does not.)

**Corollary A.1 (ratio of consecutive derivatives).** On Omega_{k+1},
  xi^{(k+1)}/xi^{(k)}(s) = l(s) (1 + theta_k(s)),  |theta_k| <= (|delta_k|+|delta_{k+1}|)/(1-|delta_k|) <= 2/7 < 1/2.
In particular |xi^{(k+1)}/xi^{(k)} - l(s)| <= |l|/2 + ... <= (2/7)|l|; and since arg l(s) in (0, pi/2) for sigma>0, x>2pi and |arg(1+theta)| <= arcsin(2/7) < pi/6, the ratio lies in the open sector arg in (-pi/6, pi/2 + pi/6), and is nonzero.

**Corollary A.2 (lower bound at sigma = 9/2).** For T >= a_k (using |zeta(9/2+iT)| >= zeta(9)/zeta(4.5) >= 0.94, |Gamma(9/4+iT/2)| >= exp((7/4)log(T/2) - pi T/4 - 9/4 - 1) by Stirling with |arg z| <= pi/2, |s(s-1)|/2 >= T^2/2, |pi^{-s/2}| = pi^{-9/4}):
  log|xi^{(k)}(9/2 + iT)| >= -pi T/4 + k log l0(T) - 9  >= -pi T/4 - 9.

### §2.2 Contour and edge geometry (orientation done carefully)

Fix k. Choose eta = eta_k in (0, 1] such that no zero of Xi_k or Xi_{k+1} has Re t in (0, eta] or Re t = eta (possible: zeros in the compact box [0,1] x [-1,1] are finitely many; zeros with Re t = 0 sit on the segment [-i/2, i/2] of the imaginary axis and are excluded from all counts N_j). Let nu_j := #{zeros of Xi_j : 0 < Re t <= eta} (a finite k-dependent constant; with the above choice nu_j = 0, but keep it symbolic).

Rectangle R(T) := [eta, T] x [-1, 1] in the t-plane, boundary counterclockwise:
  bottom edge t = x - i, x: eta -> T;  right edge t = T + iy, y: -1 -> 1;  top edge t = x + i, x: T -> eta;  left edge t = eta + iy, y: 1 -> -1.
Under s = 1/2 + it:
  bottom edge (Im t = -1)  <->  s = 3/2 + ix   (RIGHT of the strip);
  top edge (Im t = +1)     <->  s = -1/2 + ix  (LEFT of the strip).
[The orchestrator note's confusion resolved: t = x - i is the edge seeing Re s = 3/2.] By Theorem 1 no zeros of any Xi_j on the horizontal edges (distance >= 1/2 from the strip).

G_k(t) := Xi_{k+1}(t)/Xi_k(t). If no zeros of Xi_k, Xi_{k+1} lie on the boundary of R(T), the argument principle for the meromorphic G_k gives
  (1/2pi) Delta_{boundary R(T)} arg G_k = Z_{k+1}(T) - Z_k(T),
where Z_j(T) = # zeros of Xi_j in the open rectangle = N_j(T) - nu_j (no zeros on |Im t| = 1; none on the two vertical lines by the choices of eta and of good T below).

**Top edge = conjugate of bottom edge.** Since Xi_j are real entire, Xi_j(x+i) = conj(Xi_j(x-i)), so G_k(x+i) = conj(G_k(x-i)) and |Delta arg G_k(top)| = |Delta arg G_k(bottom)| (traversal direction only flips the sign). So it suffices to bound the bottom edge, where s = 3/2 + ix sits inside every Omega_j (sigma = 3/2 in [5/4 + 1/8, 5 - 1/8]).

**Bottom edge.** G_k(x - i) = i * (xi^{(k+1)}/xi^{(k)})(3/2 + ix). Split [eta, T] at X_k := a_{k+1}.
- Far part x in [X_k, T]: by Corollary A.1, arg G_k in (pi/2 - pi/6, pi/2 + pi/2 + pi/6) = (pi/3, 7pi/6), an open sector of opening 5pi/6 < pi with vertex 0, and G_k != 0. A continuous nonvanishing path confined to a sector of opening < pi stays in the half-plane {Re(e^{-i 3pi/4} w) > 0}; a continuous branch of its argument therefore stays inside an interval of length < 2*(pi/2) around 3pi/4, so the NET argument change satisfies |Delta arg| < pi.
- Near part x in [eta, X_k]: a FIXED compact segment (T-independent) on which G_k is continuous and nonvanishing; let c_k^{near} := total variation of arg G_k(x - i) on [eta, X_k] — a finite constant depending only on k (real-analytic nonvanishing function on a compact interval). If T < X_k the whole edge is inside the near part and the bound c_k^{near} still applies.
Total bottom edge: |Delta arg G_k| <= pi + c_k^{near}. Top edge: same. Left edge: fixed compact segment, zero-free; contributes a constant c_k^{left}.

### §2.3 Right edge: Landau's lemma + Jensen

**Fact J (Jensen count).** f holomorphic on |z-c| <= R', f(c) != 0, |f/f(c)| <= M on the disk: the number of zeros in |z-c| <= r < R' is <= log M / log(R'/r). [Jensen's formula; Titchmarsh, *Theory of Functions* §3.61.]

**Fact L (Landau's lemma).** f holomorphic on |z-c| <= R with |f(z)/f(c)| <= M. Then for |z-c| <= R/4:
  | f'/f(z) - sum_{rho : |rho - c| <= R/2} 1/(z - rho) | <= 16 log M / R.
[Montgomery–Vaughan, *Multiplicative Number Theory I*, Lemma 6.4 (Borel–Carathéodory + Jensen); any absolute constant is admissible below.]

**Segment argument bound.** For a straight segment I and any point rho, Delta_I arg(z - rho) in (-pi, pi) (image of a line segment under translation is a line segment; its argument varies by < pi if 0 not on it, and I is zero-free by choice of T). Hence if I subset D(c, R/4), f zero-free on I:
  |Delta_I arg f| = |Im int_I (f'/f) dz| <= pi * n(D(c, R/2)) + |I| * 16 log M / R.

**Application.** f = Xi_k, c := T - 4i (i.e. s = 9/2 + iT), R = 20, I = right edge {T + iy : |y| <= 1} (endpoints at distance sqrt(1+25) < 5.1 <= R/4 = 5? — NO: sqrt(26) ≈ 5.10 > 5. Fix: take R = 21; then R/4 = 5.25 > 5.10, D(c, R/2) has radius 10.5, all fine).
- Upper bound on D(c, 21+1) (the +1 for a Cauchy step): points have Im t in [-26, 18], so sigma = 1/2 - Im t in [-17.5, 26.5], x = Re t in [T-22, T+22]. For sigma >= 1/2: |pi^{-s/2}| <= 1, |s(s-1)/2| <= 2x^2, |zeta(s)| <= 6 x^{1/2} (Euler–Maclaurin partial-sum bound, TZF Thm 4.11 with crude constants; any polynomial bound suffices), and Stirling: log|Gamma(s/2)| <= (sigma/2 - 1/2) log|s/2| - (pi/4)x + sigma/2 + 1 <= -(pi/4)x + 13 log x + 15. For sigma < 1/2 use xi(s) = xi(1-s) and conjugation symmetry — dominated by the same form. Hence
    log sup_{D(c,22)} |Xi| <= -(pi/4)(T-22) + 16 log T + 40   (T >= 100, generous roundings).
  Cauchy: sup_{D(c,21)} |Xi_k| <= k! sup_{D(c,22)} |Xi|.
- Lower bound at center: Corollary A.2: log|Xi_k(c)| = log|xi^{(k)}(9/2+iT)| >= -(pi/4)T - 9.
- So log M <= log k! + (22 pi/4) + 16 log T + 49 <= (17 + k) log T for all T >= T_k^{(1)} := max(a_k, exp(49 + 18 + log k!)) (explicit; generous).
Conclusion (right edge, per function):
  |Delta_I arg Xi_j| <= pi log M/log 2 + 2 * 16 log M/21 <= 6.1 log M <= 6.1 (17 + j) log T <= (104 + 7 j) log T,
for j = k, k+1, T >= T_k^{(1)}, provided T is "good" (no zeros of Xi_k Xi_{k+1} with Re t = T).

**Good T and transfer to all T.** Zeros of Xi_k Xi_{k+1} with Re t in [T-1, T] are finite in number, so pick T' in [T-1, T] with no zero abscissa. Every strip point with Re t in [T-1, T], |Im t| <= 1/2 lies within distance sqrt(1 + 20.25) < 4.7 of c' = T - 4i, so by Fact J with radii (6, 21): #{zeros of Xi_j, Re t in (T', T]} <= log M / log(21/6) <= 0.8 (17+j) log T <= (14 + j) log T. Hence |N_j(T) - N_j(T')| <= (14 + j) log T.

### §2.4 Assembly

For good T' >= max(T_k^{(1)}, X_k):
  |N_{k+1}(T') - N_k(T')| = |Z_{k+1} - Z_k + nu_{k+1} - nu_k|
   <= (1/2pi)[ 2(pi + c_k^{near}) + c_k^{left} + (104 + 7k) log T' + (104 + 7(k+1)) log T' ] + |nu_{k+1} - nu_k|
   <= (35 + 3k) log T' + B_k'.
Transfer to arbitrary T >= T_k := T_k^{(1)} + 1 via §2.3's local counts (adds (14+k) + (15+k) per rung):
  |N_{k+1}(T) - N_k(T)| <= (35+3k) log T + (29 + 2k) log T + B_k' + ... <= (70 + 6k) log T + B_k.
All constants explicit modulo the c_k^{near}, c_k^{left}, nu_j, which are T-independent finite numbers defined above (absorbed in B_k). QED Theorem 2.

Corollary 2.1 follows by telescoping and classical RvM (TZF Thm 9.4: N(T) = (T/2pi)log(T/2pi) - T/2pi + O(log T)). In particular N_k(T)/(T/2pi log T) -> 1 and N_k(T) >= (T/7) log T for T >= T_k' explicit.

---

## §3 ROLLE FLOOR

**Theorem 3 (Rolle floor, multiplicity version).** For all k >= 0 and all T > 0:
  N_{k+1}^r(T) >= N_k^r(T) - 1.
Moreover if k is odd, N_{k+1}^r(T) >= N_k^r(T).

**Proof.** If N_k^r(T) = 0 the claim is trivial. Otherwise let 0 < t_1 < ... < t_M <= T be the distinct real zeros of Xi_k in (0, T], with multiplicities m_1, ..., m_M, so N_k^r(T) = sum m_i. Two disjoint sources of real zeros of Xi_{k+1} in (0, T]:
(1) Multiplicity drop: at each t_i with m_i >= 2, Xi_{k+1} has a zero of multiplicity exactly m_i - 1 (a real-analytic function with an m-fold zero has derivative with an (m-1)-fold zero at the same point). Contributes sum (m_i - 1).
(2) Rolle gaps: for each i = 1..M-1, Xi_k(t_i) = Xi_k(t_{i+1}) = 0 and Xi_k is real C^1 on [t_i, t_{i+1}], so Rolle gives a zero of Xi_{k+1} in the OPEN interval (t_i, t_{i+1}). These points are distinct from each other (disjoint open intervals) and from the t_i. Contributes M - 1.
All these zeros lie in (t_1, t_M] union {t_i} subset (0, T] — no endpoint leakage at T since t_M <= T and gap zeros are < t_M. Total:
  N_{k+1}^r(T) >= sum(m_i - 1) + (M - 1) = N_k^r(T) - 1.
Origin refinement for odd k: Xi_k is odd, so Xi_k(0) = 0; Rolle on [0, t_1] gives one more zero of Xi_{k+1} in (0, t_1), distinct from all of the above, giving N_{k+1}^r(T) >= N_k^r(T). QED.

(For even k, Xi_{k+1} is odd and vanishes AT 0, but 0 is excluded from the count (0, T]; no gain claimed.)

**Theorem 3' (distinct-zeros version).** D_{k+1}(T) >= D_k(T) - 1 (and >= D_k(T) for k odd). Proof: the M - 1 Rolle gap zeros are at M - 1 DISTINCT points (one per disjoint open gap), plus the odd-k origin-gap zero. QED.

---

## §4 MONOTONE LADDER THEOREM

kappa_k(T) := N_k^r(T)/N_k(T) in [0, 1] (defined once N_k(T) > 0);
kappa~_k(T) := D_k(T)/N_k(T).

**Theorem 4.** For every k there are explicit constants (from Theorem 2) such that for all T >= T_k*,
  kappa_{k+1}(T) >= kappa_k(T) - C_k' log T / N_k(T),  with C_k' = A_k + 1 (A_k from Theorem 2, absorbing B_k into T_k*),
and the same for kappa~. Consequently, since N_k(T) >= (T/7) log T for large T (Corollary 2.1), log T/N_k(T) -> 0 and
  liminf_{T->infty} kappa_{k+1}(T) >= liminf_{T->infty} kappa_k(T),
  liminf_{T->infty} kappa~_{k+1}(T) >= liminf_{T->infty} kappa~_k(T).

**Proof.** By Theorem 2, N_{k+1}(T) <= N_k(T) + A_k log T + B_k. By Theorem 3, N_{k+1}^r(T) >= N_k^r(T) - 1. Then, with N = N_k(T), N^r = N_k^r(T) <= N, and Q := A_k log T + B_k:
  kappa_{k+1}(T) >= (N^r - 1)/(N + Q) = N^r/N - [ N^r Q / (N(N+Q)) + 1/(N+Q) ] >= kappa_k(T) - (Q + 1)/N.
For T >= T_k* (explicit), Q + 1 <= (A_k + 1) log T. The liminf statement: fix eps > 0; for T large, kappa_{k+1}(T) >= kappa_k(T) - eps >= liminf kappa_k - 2 eps. The distinct version is identical with D in place of N^r (D <= N holds). QED.

**Remark (baseline transfer).** Any unconditional asymptotic lower bound on kappa_0 (resp. kappa~_0) — e.g. an on-line proportion result for zeta zeros, since N_0^r(T) counts precisely the critical-line zeros of zeta up to height T (a real zero t of Xi is s = 1/2 + it on the line) and N_0(T) = N(T) — transfers verbatim to EVERY rung k: liminf kappa_k >= liminf kappa_0. Definition-matching with any imported baseline (multiplicity vs distinct/simple) must be done by the orchestrator; both versions are provided here. RH is NOT addressed: RH would say kappa_0 -> 1; nothing here bounds kappa_0 from below by itself.

---

## §5 NUMERICAL VERIFICATION (falsification duty) — see census.py, results.json; dps=40

Implementation: Xi_k(t) = i^k xi^{(k)}(1/2+it), Leibniz on xi = A*zeta with A^{(j)} via psi, psi', psi'' and zeta^{(j)} = mp.zeta(s,1,j). Validated against mp.diff to rel. error < 1e-39 at s=0.7+3i, and against the functional equation xi^{(k)}(s)=(-1)^k xi^{(k)}(1-s) (rel < 1e-39). Reality on the axis: |Im| < 1e-10 |Xi_k| enforced.

(1) Real-zero counts (sign changes, grid 0.25, bisection refined) vs TOTAL counts (winding number of Xi_k around rectangle [2,T]x[-1,1], adaptive phase tracking, all winding numbers integer to ~1e-13):

  window (2, T] | k=0 | k=1 | k=2 | k=3
  T=50  real    |  10 |   9 |  10 |   9
  T=50  total   |  10 |   9 |  10 |   9
  T=100 real    |  29 |  29 |  29 |  29
  T=100 total   |  29 |  29 |  29 |  29

  => every zero of Xi_0..Xi_3 in these rectangles is REAL and SIMPLE (each detected by a clean sign change; counts match winding exactly).
  Conservation observed: |N_{k+1}-N_k| <= 1 at T=50 (values 10,9,10,9 — the +-1 breathing at the right edge is real: Xi_0 has zeros 48.005, 49.774 <= 50 while Xi_1's last is 48.623 and its next lies beyond 50; |diff|<=1 << (70+6k)log 50), and = 0 at T=100. Rolle floor observed sharp: 9 = 10 - 1 at (k=0 -> 1, T=50).
  Interlacing: every open gap between consecutive real zeros of Xi_k on (2,100] contains >= 1 real zero of Xi_{k+1}, verified for k=0,1,2 at T=50 and 100 (extra(G)=0 ledger: no gap carries more than the forced zeros, since counts match exactly).
  Low window: no real zeros of any rung in (0.02, 2]; winding of [0.02,2]x[-1,1] = 0 (to 1e-42) for k=0..3, so nu_k = 0 in that window. (Zeros with 0 < Re t < 0.02 not excluded numerically, but none expected; irrelevant to the theorems.)
  First real zeros (T=100 window): Xi_0: 14.1347; Xi_1: 15.5857 (plus its odd zero at t=0 exactly, excluded from (0,T]); Xi_2: 4.7502; Xi_3: 8.2607.
  RvM check: (T/2pi)log(T/2pi)-T/2pi+7/8 = 9.42 (T=50; observed 9-10), 29.00 (T=100; observed 29). Consistent.

(2) Edge sub-lemma reality check, s = 3/2 + ix: E_k := xi^{(k+1)}/xi^{(k)}(s) - (1/2)log(s/2pi):

   x    |l|     |E_0|   |E_1|   |E_2|
   20   0.947   0.373   0.290   0.376
   50   1.292   0.514   0.112   0.197
  100   1.587   0.276   0.177   0.168
  200   1.899   0.653   0.446   0.112
  500   2.325   0.412   0.269   0.089

  All |E_k| far below the proved bound B = 4.59 (at sigma=3/2 the sharper bound -zeta'/zeta(3/2)+4.7/x = 1.51+o(1) also holds for k=0 and is respected); |E_k|/|l| < 0.40 already at x = 20, i.e. the sector-confinement mechanism used on the horizontal edges is active from very low height, far earlier than the (astronomical) proved abscissae a_k. |E| does NOT decay in x (zeta'/zeta oscillates) — the proof correctly claims only boundedness, not o(1). [The orchestrator note's "o(1)" at §2 line 42 is FALSE as stated; boundedness is what is true and is sufficient.]

(3) Constants: Z1 = -zeta'/zeta(5/4) = 3.46665; -zeta'/zeta(3/2) = 1.50524.

---

## §6 LIMITS, FAILURE NOTES, HONEST CAVEATS

1. RH is not addressed. Nothing here bounds kappa_0; the ladder only transports lower bounds upward in k.
2. Constants: the log T coefficient A_k = 70+6k is explicit and admissible but very lossy (truth at T<=100 is |N_{k+1}-N_k| <= 1). The ADDITIVE constants B_k, T_k inherit the abscissae a_k of Sub-lemma A, which grow like 2 pi exp(16 C_k), C_k ~ 2^{k+1} — tower-type in k. This affects nothing asymptotic but makes finite-height use of Theorem 2 at small T vacuous for k >= 1; the numerics compensate at low height.
3. The Landau-lemma constant 16 is cited (MV Lemma 6.4); if the exact constant there differs, any absolute constant works and only changes A_k's numeric value.
4. |zeta(sigma+ix)| <= 6 x^{1/2} for sigma >= 1/2, x >= 2 is used with crude constants (Euler–Maclaurin/partial summation, TZF Thm 4.11); only "polynomial in x" matters.
5. Orchestrator-note errors found: (i) §1's alternate route via termwise Re-positivity of the paired Hadamard sum fails for 1/2 < sigma < 1 (counterexample in §1 above); works only for sigma >= 1. (ii) §2's "o(1)" for the edge error term is false (zeta'/zeta does not decay on sigma = 3/2); bounded suffices. (iii) The orientation of the two horizontal edges is as re-derived here: Im t = -1 is the Re s = 3/2 edge; the Im t = +1 edge needs no separate estimate by conjugation symmetry of real entire functions.
6. Failed/abandoned approaches: (a) bounding right-edge arg variation via zeros of Re Xi_k on the segment (Backlund g-function trick) stalls on the lower bound at the disk center when the center is forced near the real axis where Xi_k may be tiny; replaced by Landau's lemma with the off-axis center t = T - 4i (s = 9/2 + iT), where Sub-lemma A gives an unconditional lower bound. (b) Getting the OPEN strip in Theorem 1 for k >= 1: Gauss–Lucas + Hurwitz only yields the closed strip; open-strip refinement not needed and not pursued.
7. Multiplicity conventions: all counts with multiplicity unless "distinct" (D_k); both ladders proved. Simple-zero ladders (transfer of simplicity) NOT proved: Rolle produces a zero in each gap but does not certify its simplicity; the distinct-zero ladder is the honest strengthening and is what transfers "distinct/simple" baselines as *distinct* counts.
