# Exact column optimization in the marked inverse moment

Status: proposed source-dependent theorem. This sharpens one face of the full marked inverse-moment range. It does not establish a new zero-free boundary.

Scope: all rows, all allowed slot subcollections, the original finite ray data, the original moving fixed punctures, and the full canonical label average. This is a second-moment statement, not a scalar pairing or a selected-row estimate.

Pinned source: *The Quasi-Riemann Hypothesis*, commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`, `_source-original-quasi.tex`, SHA256 `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`. The native change below replaces the terminal column optimization in `lem:canonical-moment`. All reflection, Poisson, reconstruction, principal-term, tail, and finite-seminorm statements are imported with their exact source scope.

What was actually checked: the algebraic optimization, every occurrence of the canonical second invariant, its exact child transition, and its exact initialization. No numerical experiment proves the theorem. A separate agent independently checked the optimization and all source use sites. This is not an integrated or independently source-replayed theorem.

Smallest remaining gap toward a new boundary: the first marked constraint remains `r+2z<m`. It is the active marked capacity at the present zero-count optimizer. The improvement below therefore does not change that optimizer.

## 1. Statement

Keep the source's Eisenstein ideal conventions, fixed bad-prime set S, normalized sixth-order symbols, and all zero extensions. Let nu be one fixed finite-order ray character with its full defining modulus supported on S. Choose one common sign e in {1,-1}, and put

\[
 \psi_u(n)=\nu(n)\chi_n(u)^e.
\]

For a fixed smooth annular test W and r at least zero, define

\[
 M_u(Z^r;W)=Z^{-r/2}\sum_n\mu(n)\psi_u(n)W(Nn/Z^r).
\]

Let I be a finite set of slots, of bounded cardinality. For every i in I, take a set of primes P_i outside S, with Np comparable to Z^{z_i}, where z_i is nonnegative. These sets are pairwise disjoint and independent of u. Let |a_i(p)| be at most one, independently of u, and let W_i be fixed smooth annular tests. Set

\[
 Q_u=\prod_{i\in I}Z^{-z_i/2}
       \sum_{p\in P_i}a_i(p)\psi_u(p)W_i(Np/Z^{z_i}),
 \qquad z=\sum_{i\in I}z_i.
\]

The empty product is allowed. Fix bounded ranges for m,r,z_i and positive margins c_1,c_2. Under

\[
 \boxed{r+2z\le m-c_1,\qquad
        2r+\frac{22}{3}z\le3m-c_2,}                 \tag{1}
\]

the source-dependent conclusion is

\[
 \boxed{\sum_{\substack{u\in\mathcal O\\0<Nu\ll Z^m}}
       |M_u(Z^r;W)Q_u|^2\ll_\epsilon Z^{m+\epsilon}.}             \tag{2}
\]

For each epsilon greater than zero, the implied constant may depend on the fixed arithmetic data, the two margins, the bounded parameter ranges, the slot-count bound, and finitely many smooth seminorms. It is uniform in the prime subsets and their bounded coefficients. The conclusion holds for both common signs, for every slot subcollection, and for a fixed finite sum of whole products by the source's Hilbert-space triangle inequality. In each whole product the inverse and every prime slot must use the same nu. Separated norm twists have the same fixed polynomial height cost as in the source.

The old second premise was `2r+8z <= 3m-c_2`. The first premise, the raw moment normalization, and the class of coefficients are unchanged. There is no claim here for arbitrary bounded residual column weights, arbitrary row-dependent masks, or arbitrary moving ray moduli.

## 2. Exact optimization of the reflected column branch

Write the source reflected block variables as

\[
 T=2H+2A_0+2z_a-N_*-N_0-3B_0,
 \qquad u(v,z)=\min\{v,z,(v+z)/3\}.
\]

With the harmless dyadic and tail tolerances temporarily suppressed, the retained support is

\[
 v,b,e\ge0,\qquad v+3b+e\le T,
\]

and the source aggregate exponent is

\[
 \frac O2+\max(H,v+b)-S_0-B_0+z_a-u(v,z_a)-b-\frac{2e}{3}
   -\frac12(T-v-3b-e).                            \tag{3}
\]

For the column branch of the maximum, define

\[
 \Phi(T,z)=\sup_{v+3b+e\le T}
 \left\{v-u(v,z)+z-\frac{2e}{3}
                 -\frac12(T-v-3b-e)\right\}.
\]

Then, exactly,

\[
 \boxed{\Phi(T,z)=\max\{T,z,\tfrac23(T+z)\}.}       \tag{4}
\]

Indeed, fixing v and e, the displayed expression is increasing in b. Its maximum is therefore at b=(T-v-e)/3. It becomes v-u(v,z)+z-2e/3. For fixed z, the function

\[
 v-u(v,z)=\max\{0,v-z,(2v-z)/3\}
\]

is nondecreasing in v. Thus v can be replaced by T-e, and then by T while deleting the nonpositive e penalty. The maximum is attained at v=T,b=e=0, and equals

\[
 T+z-\min\{T,z,(T+z)/3\}
   =\max\{T,z,2(T+z)/3\}.
\]

It follows from (3), without changing the source O/2 powerful-part count, that

\[
 E_{\rm col}\le\frac O2-S_0-B_0
    +\max\{T,z_a,\tfrac23(T+z_a)\}.               \tag{5}
\]

The actual source allows e at least -eta and the retained inequality v+3b+e at most T+tau_ref, with bounded unit dyads. Replacing these by nonnegative variables changes each affine expression, minimum, maximum, and positive part by O(eta+tau_ref). Consequently (5) holds with such an additive loss in the source's exact dyadic conventions. A retained nonempty dyad with negative T has T bounded below by the same small tolerance and is covered by the same argument.

The source relaxation `u >= v/2` in the non-z branch loses the useful third affine expression in (4). Formula (4) is the only new analytic-exponent input in this note.

## 3. Strengthened canonical theorem

Keep the exact family in source `lem:canonical-moment`, including

- squarefree labels f with Nf comparable to Z^V;
- nonnegative label weight w(f), depending on f alone and bounded by a fixed power of the ideal divisor function;
- the fixed-in-row-and-label puncture rho(n)=1_{(n,rho_rad)=1};
- Q=log_Z N(rho_rad), the actual logarithmic norm of that radical;
- the coefficient bar(alpha(n)) gamma_2(n) nu(n), with no additional residual coefficient;
- the source product-form divisor mark d(n), from disjoint prime lists, total nominal cap z_0, with bounded individual prime coefficients independent of the row and label;
- the original common tests and full zero conventions.

Put F=N+V. The strengthened sufficient hypotheses are

\[
 \boxed{F-M-Q-z_0\ge c_*,\qquad
        4F-3M-\frac{16}{3}z_0\ge c_*.}             \tag{6}
\]

Under (6), the same source conclusion holds:

\[
 \begin{split}
 &Z^{-V}\sum_{f\ {\rm sf}}w(f)
 \sum_{\substack{k\in\mathcal O\\0<Nk\ll Z^M}}
 \left|Z^{-N/2}\sum_{n\ {\rm sf}}
 \bar\alpha(n)\gamma_2(n)\nu(n)\rho(n)
 \chi_n(k)\chi_n(f)^4\mathfrak d(n)W(Nn/Z^N)\right|^2\\
 &\hspace{35mm}\ll Z^{F+\epsilon}.                 \tag{7}
 \end{split}
\]

All ranges are bounded and nonnegative, with fixed positive c_*. Uniformity is exactly the source uniformity in growing fixed punctures, labels, prime-slot data, and separated heights. Every subcollection retains the same original nominal cap z_0.

### 3.1 Terminal estimate

At a terminal node, let c be the current margin. Source `old-eq:4.9`, using only the first invariant, gives

\[
 T-S_0-B_0\le M-O+2z_a-z_0-c+5d+4\eta,
 \qquad0\le z_a\le z_0.                          \tag{8}
\]

The same source support gives H at most M-O+eta. In particular a nonempty row block has O at most M+O(eta). The row branch is unchanged:

\[
 E_{\rm row}\le M+z_a+\tfrac53\eta
             \le F-c+\tfrac53\eta.               \tag{9}
\]

For the column branch, write L=S_0+B_0, which is nonnegative, and Tbar=T-L. The three terms in (5) are estimated separately.

For the T term, (8) and the first invariant yield

\[
 \frac O2+\overline T
 \le M-\frac O2+2z_a-z_0-c+5d+4\eta
 \le F-2c+5d+O(\eta).                            \tag{10}
\]

For the z_a term, nonemptiness and the first invariant give

\[
 \frac O2+z_a-L
 \le\frac M2+z_0+O(\eta)
 \le F-c-\frac M2+O(\eta).                        \tag{11}
\]

For the cross term,

\[
 \begin{split}
 \frac O2+\frac23(T+z_a)-L
 &=\frac O2+\frac23(\overline T+z_a)-\frac L3\\
 &\le\frac23M-\frac O6+2z_a-\frac23z_0-\frac23c
        +\frac{10}{3}d+\frac83\eta\\
 &\le\frac23M+\frac43z_0-\frac23c
        +\frac{10}{3}d+\frac83\eta.               \tag{12}
 \end{split}
\]

The new second invariant says

\[
 \frac43z_0\le F-\frac34M-\frac14c.
\]

Therefore (12) is at most

\[
 \boxed{F-\frac{M}{12}-\frac{11c}{12}
             +\frac{10}{3}d+O(\eta+\tau_{\rm ref}).}             \tag{13}
\]

Since M is nonnegative, (9)--(13) all have a fixed reserve below F when c is at least c_*/2 and d, eta, tau_ref and the aggregate divisor/logarithmic loss are sufficiently small in terms of c_*. One may shrink the freely chosen tolerances from the source as needed. Their exact numerical choices have no bearing on the stated exponent range.

The reflected estimate is applied with f fixed. The source weighted mass bound sum_f w(f) at most Z^{V+epsilon} cancels the outside normalization Z^{-V}; no moving fourth-power label is inserted into the hybrid norm. All mark assignments, common-profile conditions, and tail handling remain as in the source terminal proof.

### 3.2 The unchanged two-transform transition preserves (6)

For a nonterminal node, use the source reconstruction variables and its exact formal transition `eq:canonical-transition`. With

\[
 D_c=\ell+A_i+t+g-\theta+V,
\]

the identities are

\[
 \begin{split}
 F_c&=F-D_c-2\ell+j,\qquad M_c=M-2D_c-2\ell+j,\\
 F_c-M_c&=F-M+D_c,\\
 4F_c-3M_c&=4F-3M+2(A_i+t+g-\theta+V)+j.          \tag{14}
 \end{split}
\]

The exact source witness bounds imply g-theta at least -2eta, j at least zero, and

\[
 Q_{\rm new}\le Q+D_c+4\eta.
\]

For the actual nonnegative child parameters,

\[
 F_{\rm ch}=F_c+\delta_N,\qquad M_{\rm ch}=M_c+\eta,
 \qquad\delta_N\ge0.
\]

The slot cap z_0 is unchanged: retained marks are subcollections of the original slots. Thus (14) gives

\[
 \begin{split}
 F_{\rm ch}-M_{\rm ch}-Q_{\rm new}-z_0
    &\ge c+\delta_N-5\eta\ge c-5\eta,\\
 4F_{\rm ch}-3M_{\rm ch}-\frac{16}{3}z_0
    &\ge c+4\delta_N-7\eta\ge c-7\eta.             \tag{15}
 \end{split}
\]

These are the same losses as in the original recursion. Its row decrease, F growth bound, principal terms, common Fourier density, fixed-puncture reconstruction, fiber count, single normalized measure mass, and coefficient closure are unchanged. The finite depth and seminorm propagation proof therefore closes with (6) and terminal estimates (9)--(13).

The linear form `4F-3M` is essential to this unchanged induction. Merely replacing it by the apparently sharper terminal form `3F-2M` would not be justified by (14): its transition has an uncontrolled negative contribution from the cube length. This note does not make that replacement.

## 4. Initialization of the full marked inverse moment

Use the source's exact one-transform initialization of `lem:marked`. Let G be the total logarithmic overlap-prime length. The surviving nominal cap is

\[
 z_0=z-G,\qquad G\ge0.
\]

For its formal child centers, source `eq:inverse-initial-margins` is preceded by the exact identities

\[
 \begin{split}
 F_c^{\rm init}-M_c^{\rm init}-(P_1+G)-z_0
    &=m-r-2z+2G,\\
 4F_c^{\rm init}-3M_c^{\rm init}-6z_0
    &=3m-2r-8z+10G+2P_1.                          \tag{16}
 \end{split}
\]

Adding (2/3)z_0 to the second identity gives exactly

\[
 \boxed{4F_c^{\rm init}-3M_c^{\rm init}-\frac{16}{3}z_0
     =3m-2r-\frac{22}{3}z+\frac{28}{3}G+2P_1.}    \tag{17}
\]

The actual puncture bound remains Q_init at most P_1+G+3eta; the source gives P_1 at least -2eta and favorable nonnegative clipping delta_init. Consequently (1), (16), and (17) imply the actual margins

\[
 \begin{split}
 F_{\rm init}-M_{\rm init}-Q_{\rm init}-z_0
   &\ge c_1-9\eta-\tau_{\rm init},\\
 4F_{\rm init}-3M_{\rm init}-\frac{16}{3}z_0
   &\ge c_2-22\eta-3\tau_{\rm init}.              \tag{18}
 \end{split}
\]

The positive G contribution is retained, rather than discarded before the exact identity. The numerical losses in (18) are exactly the source losses, since neither the row enclosure nor clipping changed.

Apply the strengthened canonical estimate (7) with tolerances chosen to preserve a positive fixed margin in (18). The source energy identity

\[
 \kappa_c^{\rm init}+P_1+2F_c^{\rm init}=m
\]

and its normalized quotient measure, witness-multiplicity weight, and one fiber-count factor are unchanged. The source final exponent is therefore m+epsilon, proving (2) under the inherited analytic statements.

## 5. Exact source dependency map

| Source object | Use in this deduction | Change |
|---|---|---|
| `lem:hybrid-energy`, `old-eq:4.6b` | Full hybrid quadratic-cubic norm | Imported unchanged |
| `lem:reflected-energy`, `old-eq:4.4`--`old-eq:4.7` | Actual retained reflected exponent and support | Imported unchanged |
| `lem:canonical-moment`, `eq:invariant` | Canonical class and target norm | Replace 6z_0 by (16/3)z_0 in the second premise only |
| `eq:inverse-fixed-invariant` | Node invariants | Same second-premise replacement |
| `eq:inverse-terminal-width`, `old-eq:4.9` | Actual terminal dual width | Imported unchanged; uses first premise only |
| `old-eq:4.10`, `old-eq:4.11` | Terminal column bounds | Replace by the exact three-branch bounds (10)--(13) |
| `eq:canonical-transition` | Formal two-transform identities | Imported unchanged |
| `eq:inverse-child-margins` | Actual child margins | Replace 6z_0 by (16/3)z_0; same loss |
| `eq:inverse-initial-margins` | Full marked initialization | Replace using (17)--(18) |
| `eq:inverse-initial-energy` | Final energy normalization | Imported unchanged |

The audit found no additional use of the coefficient 6 in this canonical second invariant. Unrelated earlier occurrences of a symbol z_0 in the source are not part of this replacement. The proposed theorem is conditional on the full correctness and exact scope of the pinned source statements; it is not a new standalone proof of the imported cubic theta reflection.

## 6. Why this is not a new zero-free boundary

At the current zero-count optimizer described by the root analysis, the marked capacity is selected at

\[
 z=(1-r)/2,\qquad r\ge23/37>1/2.
\]

Already the old second marked constraint then satisfies

\[
 2r+8z=4-2r\le102/37<3.
\]

It therefore has a positive reserve while the first constraint is active. Changing the second coefficient from 8 to 22/3 cannot increase the usable marked capacity there. This diagnosis depends only on that supplied optimizer range; it is not a global claim about every possible future consumer of (2).

The unmarked face z=0 is also unchanged. In particular, this theorem does not prove the raw inverse estimate below the diagonal H=D required by the direct principal sixth-power amplification proposal. That requires additional cancellation in the full signed reconstruction or a genuinely different estimate.

## 7. The exact positive face forcing the first marked constraint

The first constraint is already sharp for the exponent supplied by the source's positive terminal norm, even if its second invariant is improved further. This is an obstruction to that particular upper-bound argument, not a lower bound for the true arithmetic sum.

Set

\[
 Q=V=O=A_0=N_0=B_0=S_0=0,\qquad H=M,\qquad z_a=z_0=z.
\]

Take the short completion with N_*=F. The exact reflected width is

\[
 T=2M+2z-F.
\]

On the retained column face v=T,b=e=0, if T is at least 2z, then u=z. There is no small-kernel saving, and the exact source exponent is

\[
 E_{\rm col}=T=2M+2z-F.                           \tag{19}
\]

Hence a proof that bounds every such positive block by Z^{F+epsilon} needs

\[
 F\ge M+z.                                      \tag{20}
\]

The face condition T>=2z is equivalent to F<=2M and holds in a neighborhood of the binding current range. The refined powerful-part count is exactly zero on O=A_0=0, so it changes nothing in (19). The exact cube and column optimizations are attained on this face, rather than merely failing to rule it out.

In the clean marked initialization, take the unit overlap and quotient data G=P_1=0, with unit new label and no puncture. The source formal centers are

\[
 F=r+z,\qquad M=2r+2z-m.
\]

Thus

\[
 E_{\rm col}-F=2(r+2z-m).                         \tag{21}
\]

Exactly the original first marked condition m>=r+2z is necessary to close this face by the same positive estimate. At its boundary, M=r and F=r+z, so the face condition is z<=r; this includes the supplied optimizing range r>=23/37 and z=(1-r)/2.

A change to the second invariant cannot address (21). A genuine gain in the first marked capacity must exploit arithmetic cancellation before this positive hybrid norm, use a stronger norm for the actual restricted coefficients, or use a different full moment construction.
