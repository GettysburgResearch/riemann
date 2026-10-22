# All-\(r\) Hasse counts on the two rigid tensor/symmetric-power graphs

**Status:** exact graph-union theorem, exact square/nonsquare arithmetic,
source-locked low-r recoveries, and tiny integer-only replay.

For every \(r\geq1\), the two rigid monomial subtori in

\[
 \operatorname{Std}(E_A)\otimes\operatorname{Sym}^r(E_B)
 \quad\hbox{versus}\quad
 \operatorname{Sym}^{2r+1}(E_C)
\]

give two explicit one-parameter spectral graphs.  This packet counts their
integral Hasse-lattice union exactly.  If \(q=p^{2k}\), the answer is

\[
\boxed{
 N_r(p^{2k})=
 8p^{\lfloor k/(r+1)\rfloor}+8p^{\lfloor k/2\rfloor}
 -1+\mathbf 1_{\,r\ {\rm odd}}
 -4\mathbf 1_{\,3\nmid(r+1)}.}
 \tag{1}
\]

There are no coefficient-prime exceptions in (1): its valuation lemma works
at \(p=2\) as well.  For a nonsquare odd prime power \(q=p^e\), \(e\) odd,
the graph union is empty for odd \(r\); for even \(r\) it has

\[
\boxed{
 4\left\lfloor
 \frac{\lfloor2\sqrt q\rfloor}
 {p^{\lceil er/(2(r+1))\rceil}}
 \right\rfloor+1}
 \tag{2}
\]

points.  The restriction to odd \(p\) in (2) is real and is recorded below.

## 1. Conventions and the central sign

Put \(s=\sqrt q\) and normalize

\[
 x=A/s,\qquad y=B/s,\qquad z=C/s.
 \tag{3}
\]

Let \(D_n\) be the Dickson--Chebyshev trace polynomial

\[
 D_n(w+w^{-1})=w^n+w^{-n},\qquad
 D_0=2,\quad D_1=z,\quad
 D_{n+1}=zD_n-D_{n-1}.
 \tag{4}
\]

The locked all-\(r\) subtorus-rigidity packet proves that the only primitive
integer monomial subtori producing the target odd-weight interval are

\[
\begin{aligned}
 \operatorname{Std}(w^{r+1})\otimes\operatorname{Sym}^r(w)
 &\sim_{\rm spectrum}\operatorname{Sym}^{2r+1}(w),\\
 \operatorname{Std}(w)\otimes\operatorname{Sym}^r(w^2)
 &\sim_{\rm spectrum}\operatorname{Sym}^{2r+1}(w).
\end{aligned}
 \tag{5}
\]

A central sign is not a Weyl inversion.  If the two source torus coordinates
receive central signs \((-1)^{\delta_u}\) and
\((-1)^{\delta_v}\), every tensor root receives the common sign
\((-1)^{\delta_u+r\delta_v}\).  Keeping the target \(w\) fixed therefore
requires

\[
 \boxed{\delta_u+r\delta_v=0\pmod2.}
 \tag{6}
\]

Writing \(\varepsilon=(-1)^{\delta_v}\), the two normalized graph points are

\[
\begin{array}{ll}
 {\cal G}_{1,r}:&
 (x,y,z)=\bigl(\varepsilon^rD_{r+1}(z),\varepsilon z,z\bigr),\\[2mm]
 {\cal G}_{2,r}:&
 (x,y,z)=\bigl(\varepsilon^r z,\varepsilon D_2(z),z\bigr).
\end{array}
 \tag{7}
\]

For even \(r\), the first source trace is fixed while the second has two
signs.  For odd \(r\), both source traces change sign together.  This parity
is responsible for the one-point correction in (1).

The raw factor comparison has dilation \(T\mapsto q^{r/2}T\), since the
source and target weights are \(r+1\) and \(2r+1\).  Formula (7) is a
normalized spectral statement; the remainder of the note determines when
its raw traces are integral.

## 2. Homogeneous Dickson polynomials and the valuation lemma

Define the integral homogeneous trace polynomial

\[
 L_n(C,q)=s^nD_n(C/s).
 \tag{8}
\]

It satisfies

\[
 L_0=2,\qquad L_1=C,\qquad
 L_n=CL_{n-1}-qL_{n-2},
 \tag{9}
\]

and, for \(n\geq1\),

\[
 L_n(C,q)=
 \sum_{0\leq j\leq\lfloor n/2\rfloor}
 (-1)^j\frac{n}{n-j}\binom{n-j}{j}
 q^jC^{n-2j}.
 \tag{10}
\]

The leading coefficient is \(1\).  On the first graph, with \(n=r+1\),

\[
 A=\varepsilon^r\frac{L_{r+1}(C,q)}{s^r},\qquad
 B=\varepsilon C.
 \tag{11}
\]

Suppose first that \(q=p^{2k}\), so \(s=p^k\), and put
\(c=v_p(C)\).  When \(c<k\), the valuation before allowing for the integer
coefficient in the \(j\)-th term of (10) is

\[
 (r+1)c+2j(k-c).
 \tag{12}
\]

Thus \(j=0\) is the unique lowest-valuation term.  No cancellation is
possible and

\[
 v_p\bigl(L_{r+1}(C,q)\bigr)=(r+1)c.
 \tag{13}
\]

If \(c\geq k\), every term of (10) has valuation at least
\((r+1)k\), which is already at least \(rk\).  Consequently

\[
\boxed{
 s^r\mid L_{r+1}(C,q)\quad\Longleftrightarrow\quad
 v_p(C)\geq\left\lceil\frac{rk}{r+1}\right\rceil.}
 \tag{14}
\]

The proof uses only that the leading coefficient is the unit \(1\); primes
dividing any other coefficient can only raise its valuation.  Hence (14)
has no coefficient-prime exception.

The useful floor form is

\[
 k-\left\lceil\frac{rk}{r+1}\right\rceil
 =\left\lfloor\frac{k}{r+1}\right\rfloor.
 \tag{15}
\]

For the second graph,

\[
 A=\varepsilon^rC,\qquad
 B=\varepsilon\frac{C^2-2s^2}{s},
 \tag{16}
\]

and therefore

\[
\boxed{
 s\mid C^2-2s^2\quad\Longleftrightarrow\quad
 v_p(C)\geq\lceil k/2\rceil.}
 \tag{17}
\]

Both remaining Hasse bounds are automatic: if \(|C|\leq2s\), then
\(z=C/s\in[-2,2]\), and
\(D_m(2\cos\theta)=2\cos(m\theta)\) keeps every \(D_m(z)\) in
\([-2,2]\).

## 3. Counting each signed graph at square \(q\)

Let

\[
 a=p^{\lfloor k/(r+1)\rfloor},\qquad
 b=p^{\lfloor k/2\rfloor}.
 \tag{18}
\]

By (14), the first graph has \(4a+1\) possible values of \(C\).  If \(r\)
is even, the two signs only change \(B\), and they merge exactly at \(C=0\).
Hence

\[
 |{\cal G}_{1,r}|=8a+1\qquad(r\ {\rm even}).
 \tag{19}
\]

If \(r\) is odd, both \(A\) and \(B\) change sign.  At \(C=0\), \(r+1\)
is even and

\[
 \frac{L_{r+1}(0,q)}{s^r}
 =2(-1)^{(r+1)/2}s,
 \tag{20}
\]

so the two endpoint values of \(A\) remain distinct.  Thus

\[
 |{\cal G}_{1,r}|=8a+2\qquad(r\ {\rm odd}).
 \tag{21}
\]

Equation (17) gives \(4b+1\) values of \(C\) on the second graph.  Its two
signed points never merge: \(C^2-2s^2=0\) has no integral solution.  This
gives

\[
 |{\cal G}_{2,r}|=8b+2
 \tag{22}
\]

for every \(r\).

## 4. The overlap is periodic modulo \(3\)

Use signs \(\varepsilon\) and \(\eta\) for the first and second graph.  An
overlap at fixed \(z\) satisfies

\[
 \varepsilon^rD_{r+1}(z)=\eta^rz,\qquad
 \varepsilon z=\eta D_2(z).
 \tag{23}
\]

Put \(\rho=\varepsilon/\eta\in\{\pm1\}\).  Then

\[
 D_2(z)=\rho z,\qquad D_{r+1}(z)=\rho^rz.
 \tag{24}
\]

Since \(D_2(z)=z^2-2\), the first equation in (24) has only

\[
 (\rho,z)=(1,2),(1,-1),(-1,1),(-1,-2).
 \tag{25}
\]

The endpoints \(z=\pm2\) always satisfy the second equation.  At \(z=-1\),

\[
 D_{r+1}(-1)=2\cos\!\left(\frac{2\pi(r+1)}3\right),
 \tag{26}
\]

and at \(z=1\),

\[
 D_{r+1}(1)=2\cos\!\left(\frac{\pi(r+1)}3\right).
 \tag{27}
\]

The two internal values work together exactly when \(3\nmid(r+1)\).  Each
eligible \(z\) has two distinct sign choices, so

\[
\boxed{
 |{\cal G}_{1,r}\cap{\cal G}_{2,r}|
 =4+4\mathbf1_{\,3\nmid(r+1)}.}
 \tag{28}
\]

There is no hidden \(z=0\) overlap: it already fails
\(D_2(z)=\rho z\).

Subtracting (28) from (19) or (21) plus (22) proves (1).  Written by parity
and congruence class, its constant correction is

| \(r\) | condition | correction after the two \(8p^\bullet\) terms |
|---:|:---|---:|
| even | \(r\equiv2\pmod3\) | \(-1\) |
| even | \(r\not\equiv2\pmod3\) | \(-5\) |
| odd | \(r\equiv2\pmod3\) | \(0\) |
| odd | \(r\not\equiv2\pmod3\) | \(-4\) |

## 5. The first three rungs are recovered exactly

The packet locks the all-\(r\) subtorus-rigidity fixture and the independently
proved \(r=1,2,3\) intersection packets.  Formula (1) specializes to

\[
\begin{array}{c|c}
 r&N_r(p^{2k})\\ \hline
 1&16p^{\lfloor k/2\rfloor}-4,\\[1mm]
 2&8p^{\lfloor k/3\rfloor}+8p^{\lfloor k/2\rfloor}-1,\\[1mm]
 3&8p^{\lfloor k/4\rfloor}+8p^{\lfloor k/2\rfloor}-4.
\end{array}
 \tag{29}
\]

These are precisely the three locked predecessor formulas.  Those packets
contain additional arguments showing when the graph union is the complete
integral or rational spectral intersection.  For general \(r\), this packet
proves only the exact graph-union count; nongraph cyclotomic components have
not been excluded.

## 6. Nonsquare odd prime powers

Let \(q=p^e\), where \(p\) is odd and \(e\) is odd, and put

\[
 H=\lfloor2\sqrt q\rfloor.
 \tag{30}
\]

If \(r\) is even, \(q^{r/2}\) is integral and the first graph reads

\[
 A=\frac{L_{r+1}(C,q)}{q^{r/2}},\qquad B=\pm C.
 \tag{31}
\]

The same unique-minimum proof as above, now comparing \(v_p(C)\) with
\(e/2\), gives

\[
\boxed{
 q^{r/2}\mid L_{r+1}(C,q)\quad\Longleftrightarrow\quad
 v_p(C)\geq\left\lceil\frac{er}{2(r+1)}\right\rceil.}
 \tag{32}
\]

There are \(2\lfloor H/p^d\rfloor+1\) values of \(C\), where \(d\) is the
ceiling in (32); the two \(B\)-signs merge at \(C=0\).  This proves (2).

If \(r\) is odd, \(q^{r/2}\) is irrational.  An integral \(A\) on the first
graph would force

\[
 L_{r+1}(C,q)=0.
 \tag{33}
\]

Here \(r+1\) is even.  Since \(e\) is odd, \(v_p(C)\ne e/2\).  Below \(e/2\)
the monic leading term is uniquely minimal.  Above \(e/2\) the final term
\(2(-q)^{(r+1)/2}\) is uniquely minimal; its coefficient \(2\) is a
\(p\)-adic unit because \(p\) is odd.  Thus (33) is impossible.

On the second graph, an integral value of

\[
 B=\pm\frac{C^2-2q}{\sqrt q}
 \tag{34}
\]

would force \(C^2=2q\).  Its two sides have even and odd \(p\)-adic
valuations, respectively, so this is impossible.  Therefore the second
graph is always empty at nonsquare odd prime powers, proving the stated
parity theorem.

The odd-prime hypothesis cannot simply be erased.  When \(p=2\) and \(e\)
is odd, \(C^2=2q\) has integral solutions, and
\(D_n(\pm\sqrt2)=0\) when \(n\equiv2\pmod4\).  The \(p=2\) nonsquare
exceptions are deliberately left as a separate target.

## 7. Exact replay and resource boundary

The producer performs only the following bounded checks:

- square rows \(p\in\{3,5\}\), \(1\leq k\leq2\), and \(1\leq r\leq12\);
- nonsquare rows \(p\in\{3,5\}\), \(e\in\{1,3\}\), and
  \(1\leq r\leq12\);
- enumeration of the single parameter \(C\), never a full trace cube;
- exact integer recurrence, divisibility, isqrt, sets, hashes, and JSON.

The logical-work ledger is guarded by a strict exclusive 20,000-unit cap.
The public graph-point enumerators also fail closed before scanning more than
4,096 candidate values of `C`; the closed-count functions remain available
for larger capped parameters without enumerating the Hasse interval.
There are no random samples, floating-point outputs, runtime symbolic
packages, finite-field elements, curves, polynomial models, or full
\((A,B,C)\) scans.  The finite rows are regressions; equations
(12)--(17), (23)--(28), and (31)--(34) are the proofs.

Reproduce the packet with

    python -B research/l-families/atlas/function_field/elliptic_tensor_symmetric_power_hasse_graph_counts.py --check
    python -B -O research/l-families/atlas/function_field/elliptic_tensor_symmetric_power_hasse_graph_counts.py --check
    python -B -m pytest -q tests/test_elliptic_tensor_symmetric_power_hasse_graph_counts.py
    python -B -O -m pytest -q tests/test_elliptic_tensor_symmetric_power_hasse_graph_counts.py

## 8. Scope firewall

- This is an exact count of two sufficient torus graph loci.
- Only the locked low-r packets separately justify completeness of the full
  intersection at their stated arithmetic scopes.
- Hasse-admissible integer triples are not renamed elliptic curves, linked
  isogeny classes, varieties, or a compatible family.
- A spectral identity on a torus is not an ambient representation
  homomorphism.
- No motive, correspondence, Euler product, automorphy, modularity,
  analytic continuation, zero theorem, RH, or GRH claim follows.
- The elementary theorem is recorded without a literature-priority or
  novelty claim.
