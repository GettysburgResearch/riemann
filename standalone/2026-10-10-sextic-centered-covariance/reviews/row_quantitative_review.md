# Second independent review of the arbitrary-row quantitative adapter

**Verdict: PASS, subject to the explicitly named analytic inputs.**

The arbitrary-row reduction preserves the exact scalar cancellation, all nonunit zeros, and the separate column coefficients required by the quadratic–cubic norm argument. The powerful-row weights are summable in the squared norm. Thus the numerical completed and literal cube-free estimates extend from squarefree rows to every nonzero element row, subject to the same analytic premises as the companion proofs. The exact auxiliary-prime reindexing gives the sharper factors \(1,Q,Q^{2/3}\). Sharp row balls and fixed rapidly decreasing scalar row profiles obey the same bounds.

## 1. Snapshot and analytic boundary

The complete frozen proof reviewed is ARBITRARY_ROW_MOMENTS.md, 33,984 bytes, SHA-256 a12605808006c07f1a413e743545441e0541577367c8ea1bbe09a7fc493cc52a. This includes Corollary 7.2 and Section 8 in their final forms.

The dependency snapshots are:

| Input | SHA-256 |
|---|---|
| centered_a2_attack.md | bbc139f956731482fcf9e33645bfe2832b7b7471594d9cbc1f21cd08eaf2ac5a |
| all_cusp_gauss_factorization.md | b596f3f7c43bb84c699201f3b14c81eae18ae89d3b45e2357bcdccfb9eb3ea1c |
| cube_inverse_attack.md | a865338882111bf3bc96ffc539dd93f3b2ee59390499caaf14852ed8cde77804 |
| ARBITRARY_ROW_SUPPORT.md | f859936fb555de1afd0215fa74e89ce10b8afa1b9a193e4d355be3da3f542dd5 |

I checked the new scalar calculation directly against the full reflection scalar after eq:dual-cusp-mellin-series, the local factors in eq:ray-local-transform, the zero-extension convention in eq:theta-row-twist, and the fixed-residue calculation in eq:ray-multiplier of the imported October 5 paper2.tex, OpenAI/math commit adc7f1241b42e322a6451854ab7e4b4c146bf78a. The PR #915 coefficient and norm interfaces retain pin 9959364671f89b86f3992ec5ed5e19f804eb607b.

The scalar estimate with exponent \(1/2<\beta\le1\) is an explicit hypothesis of the adapter. At \(\beta=1\) it follows by counting. The specialization \(\beta=11/12\) retains the companion canonical/angular premise. The present review does not certify the imported paper's global main results. Its new claims are the local arithmetic reduction, the transfer of the already reviewed norm arguments, and the convergent summation over row sectors.

## 2. Full scalar for every good-prime exponent: PASS

Write \(j=v_p(k)\bmod6\), and retain the zero extension even for \(j=0\). The source gives

\[
\sigma_p=\lambda^2c/p,\qquad
\epsilon_p=-\lambda^{-5}(c/p)^{-2}.
\]

For \(j\notin\{0,4\}\), direct substitution in
\(\chi_p(\sigma_p)^{-2}\omega_{p,j}\) makes the sign exponent \(-2\), hence trivial, and the \(c/p\) exponent

\[
-2+2(j+2)=2j+2.
\]

The remaining \(\lambda\) exponent is \(5j+6\equiv-j\pmod6\). The exact local formulas are therefore

\[
\chi_p(\sigma_p)^{-2}\omega_{p,j}
=\Omega_{p,j}\chi_p(c/p)^{2j+2},
\]

\[
\Omega_{p,j}=
\begin{cases}
\gamma_j(p)\gamma_{j+2}(p)\chi_p(\lambda)^{-j},
  &j\notin\{0,4\},\\
\gamma_4(p)\chi_p(\lambda)^{-4},&j=4,\\
-\gamma_2(p),&j=0\text{ active}.
\end{cases}
\]

These match (2.1)–(2.2) of the note. The \(j=0\) and \(j=4\) formulas use their actual exceptional source factors; they are not obtained by inserting a trivial-character Gauss sum into the generic formula. All displayed \(\Omega_{p,j}\) have modulus one. An inactive \(j=0\) prime contributes the scalar \(1-(Np)^{-1}\), as in the source.

Let \(r\) denote the active row radical, so \(c=c_0ra\). Aggregating the primes of the squarefree outer variable \(a\) by exact Gauss CRT gives

\[
\gamma_4(a)\chi_a(\lambda^2c_0r)^{-2}.
\]

This is exactly the note's (2.3). The factor involving \(r\) has exponent four. Reciprocity to this even exponent contributes no sign, and it combines with the row-prime exponent \(2j+2\) to give \(2j\pmod6\). The original external factor \(\chi_a(k)\) then makes the exponent \(3j\). Thus every odd good row valuation contributes a quadratic character of \(a\); every even valuation is trivial on units.

The original \((a,k)=1\) condition is essential throughout this calculation. When a positive valuation is divisible by six, the original character still vanishes on multiples of its prime. For inactive primes, the initial Fourier zero mode has already contributed the stated scalar; this does not authorize deleting the original outer-variable exclusion.

Finally, \(\gamma_2(a)\gamma_4(a)=1\), and the complete angular factor is

\[
\alpha(c)^{-2}\alpha(a)^{-1}
=\alpha(c_0r)^{-2}\alpha(a)^{-3}.
\]

This verifies the exact angular type and the absence of a remaining \(a\)-dependent Gauss factor. The scalar is consequently the asserted bounded row factor times

\[
\eta(a)\alpha(a)^{-3}\chi_{k_0\tau_{\rm odd}}(a)^3
\quad\text{on }(a,k)=1.
\]

I also checked the finite-family issue as \(a\) varies. In the source's multiplier calculation, every factor besides the explicit cubic symbol depends only on fixed residues at \(S\). Choosing the local translate representatives to be zero modulo \(M^2\) makes those residues functions of the fixed bad translate and the active product modulo \(M^2\). Fixed ray splits in \(a\) and \(k_0\) therefore suffice. An arbitrary arithmetic coefficient of \(a\) is not hidden in the remaining bounded scalar.

## 3. Repeated-prime multipliers and the scalar exclusions: PASS

In a fixed row sector, \(\tau\) is powerful outside \(S\), \(k_0\) is squarefree, and \((k_0,\tau)=1\). The outer mask implies

\[
(efg,\tau)=1
\]

after the positive allocation is split. At a prime \(p\mid\tau\), all factors of the frequency outside \(n_0b'\) are therefore units, so

\[
B_{p,4}(\lambda^4\ell)
=(Np)^{-1/2}\bigl[-1+Np\,\mathbf1_{p\mid n_0b'}\bigr].
\]

Once the complete \(b'\) is frozen, this is a coefficient of \(n_0\) alone. Its modulus is at most \(\sqrt{Np}\). The other local factors are multiplicative characters times a scalar of modulus at most one, and split into separate factors in \(e\), \(n_0\), and the frozen indices. Their zeros at \(p\mid n_0b'\) remain literal zeros.

Thus the product amplitude is at most

\[
\Lambda(\tau)^2
=\prod_{\substack{p\mid\tau\\v_p(\tau)\equiv4\ (6)}}Np
\]

in the squared norm. After normalization by \(\Lambda(\tau)\), the positive \(e,n_0\) vectors satisfy the same separate bounded-coefficient hypotheses as the earlier quadratic–cubic composition. Freezing all cube powers, including bad-prime powers, is necessary for this separation and is done in the correct order.

The two Möbius scalar variables use the squarefree index

\[
s=k_0\tau_{\rm odd}.
\]

Its norm is at most a fixed multiple of the original row height. The full radical \(\operatorname{rad}\tau\), including even and inactive row primes, is placed in the moving exclusion. Hence no theorem for a new finite-character family is required. The scalar estimate is applied pointwise to the actual \(k_0\)-rows. The remaining positive quadratic norm is still a norm in \(k_0\); it is not relabeled as a mean square in the larger index \(s\).

The same observation applies to the inverse variable \(h\). Its original factor \(\chi_h(k)^3\) excludes every prime of \(\tau\), even when the valuation of that prime is even. In the shared-divisor identity, both scalar exclusions retain \(\operatorname{rad}\tau\). No condition involving the theta variables is added.

## 4. Fixed-sector norms and their support interfaces: PASS

The exact support theorem applies before the positive allocation is split, with conductor \(c=c_0k_0r_\tau a\). Consequently \(G\ll\sqrt B\) for the completion and \(G^2Z^3\ll B\) in the cube inverse, uniformly in the active radical \(r_\tau\).

Put \(R_\iota=N(r_\tau)\le R=N(\operatorname{rad}\tau)\) and \(H_0=H/N(k_S\tau)\). The effective lengths are

\[
Y_\iota=\frac{H_0^2R_\iota^2EG^2}{BF}
\]

for the completed block, and the same quantity times \(Z^3\) after inverse completion. The corresponding component energies have the original brackets

\[
\Lambda(\tau)^2G^{2\beta-2}
\bigl[H_0E+Y_\iota+(EY_\iota)^{2/3}\bigr]
\]

and

\[
\Lambda(\tau)^2G^{2\beta-2}Z^{2\beta-2}
\bigl[H_0E+Y_\iota+(EY_\iota)^{2/3}\bigr].
\]

The extra row phases are separate bounded column coefficients, so the previous norm proof applies. Its common-divisor costs remain \((Nd)^{-\beta-1/2}\), \((Nj)^{-\beta-1/2}\), and \((N\ell)^{-2\beta}\), all summable for \(\beta>1/2\). The last shared divisor may intersect the remaining positive variable \(e'\), exactly as in the independently reviewed cube inverse.

Optimizing with \(EFG\asymp A\) and the respective support constraints gives (4.1) and (5.1). Replacing \(R_\iota\) by \(R\) is legitimate because each term is nonnegative and increasing in \(R_\iota\). The at most \(2^{\omega_0(\tau)}\) active/inactive branches cost at most \(4^{\omega_0(\tau)}=b(\tau)\) in squared norm. The full ramified and cube tails are unchanged, apart from the polynomially bounded effective length.

A nonempty sector has \(H_0>1/2\). Thus the finitely bounded interval \(1/2<H_0<1\), including the possible \(k_0=1\) row, is covered by enlarging a sieve height to one at constant cost. No small row sector is omitted.

## 5. Summation over powerful rows: PASS

The decomposition \(k=u k_S\tau k_0\) is unique. Its sectors partition the original rows, so their energies are added directly. Applying Minkowski over the infinitely many possible \(\tau\) would introduce an unnecessary loss; the note correctly avoids that step.

The three required weights, apart from fixed bad-prime factors, are

\[
\frac{b(\tau)\Lambda(\tau)^2}{N\tau},\qquad
\frac{b(\tau)\Lambda(\tau)^2R^2}{(N\tau)^2},\qquad
\frac{b(\tau)\Lambda(\tau)^2R^{4/3}}{(N\tau)^{4/3}}.
\]

At a good prime of norm \(q\), a positive powerful valuation has \(v\ge2\). Splitting \(v\) into its six residue classes gives decreasing geometric progressions with leading exponents

\[
\mathbf1_{v\equiv4}-v,\qquad
\mathbf1_{v\equiv4}+2-2v,\qquad
\mathbf1_{v\equiv4}+\frac43-\frac43v.
\]

Their maxima are respectively \(-2,-2,-4/3\), all at \(v=2\). The branch multiplier four occurs only at positive valuations divisible by six and does not change these decay exponents. The resulting Euler factors are \(1+O(q^{-2})\), \(1+O(q^{-2})\), and \(1+O(q^{-4/3})\); all products converge over prime ideals.

The bad-prime valuations produce geometric series with positive decay exponents \(1,2,4/3\), and the six units cost a fixed factor. This establishes the claimed all-row bounds with exactly the earlier right-hand sides. Uniform subpower losses may be taken outside the original polynomially bounded sector range before enlarging these nonnegative convergent sums.

At \(A=B=D\), the completed row range remains \(H\le D^{(5-2\beta)/4}\), and the literal range remains \(H\le D^{(5-2\beta)/6}\). In particular, the conditional \(19/24\) and \(19/36\) exponents now concern every nonzero element row. Their numerical value has not changed, and they are row ranges rather than zero-free boundaries.

## 6. The initial moving-auxiliary estimate: PASS

For squarefree primary \(\mathfrak q\) outside \(S\), complete multiplicativity with the zero extension gives exactly the row replacement \(k\mapsto k\mathfrak q^4\) for both specified objects. There is no assumption \((k,\mathfrak q)=1\).

At \(p\mid\mathfrak q\), retain the original valuation \(\nu=v_p(k)\ge0\). The reflected exponent is \(j=\nu+4\bmod6\), but the physical row-height denominator remains \((Np)^\nu\). The odd quadratic radical depends on the parity of \(\nu\), while the whole \(\mathfrak q\) enters the scalar exclusions, including the case \(j=0\). The inverse variable also remains coprime to \(\mathfrak q\).

The crude squared amplitude has exponent one exactly when \(\nu\equiv0\pmod6\). The three local sums have leading powers \(q,q^3,q^{7/3}\), each at \(\nu=0\), and the six residue progressions give the normalized remainder bounds in (7.3). These establish the initial uniform auxiliary factors \(Q,Q^3,Q^{7/3}\), including overlapping original rows and auxiliary primes.

## 7. Exact auxiliary reindexing and the sharper costs: PASS

When the physical valuation at \(p\mid\mathfrak q\) is zero, the reflected exponent is four. Because \(p\nmid a=efg\), the local identity is exactly

\[
B_{p,4}(x)
=-q^{-1/2}
+q^{1/2}\mathbf1_{p\mid n_0}
+q^{1/2}\mathbf1_{p\nmid n_0,\ p\mid b'},
\qquad q=Np.
\]

The proof applies this identity to the complete theta sum, before freezing or truncating its cube index. The squarefree branch substitutes \(n_0=pn_1\), keeping \(p\nmid n_1\). The cube branch substitutes \(b'=pb_1\), keeping \(p\nmid n_0\) and allowing every valuation of \(p\) in \(b_1\). This is the source's actual disjoint positive allocation.

Including the first-reflection conductor factor \(q^2\), the exact squared-amplitude and effective-length multipliers are

| Branch | Squared amplitude | Effective length |
|---|---:|---:|
| Negative | \(q^{-1}\) | \(q^2\) |
| Squarefree theta index | \(1\) | \(q\) |
| Cube theta index | \(q^{-1}\) | \(q^{-1}\) |

The denominators \(1/\sqrt{Nn_0}\) and \(1/Nb'\) give precisely these amplitudes. They are not inferred merely from the upper coefficient bound.

The all-cusp coefficient factorization survives the changes of variables. With the unchanged fixed bad part suppressed, the squarefree branch has

\[
\gamma_2(epn_1)
=\gamma_2(p)\gamma_2(e)\gamma_2(n_1)
\chi_e(p)^4\chi_{n_1}(p)^4\chi_{n_1}(e)^4.
\]

The new factors are separate bounded twists in \(e\) and \(n_1\); the associated row phase has modulus one because the actual \(k_0\)-rows are coprime to \(\mathfrak q\). The same calculation with the fixed bad squarefree part included only adds further bounded factors. Repeated extraction at distinct auxiliary primes remains a sequence of such separate twists. The Möbius variables \(g,h\) acquire no theta-column dependence and retain their existing exclusions by \(\mathfrak q\).

For the three energy monomials \(H_0E\), \(Y_0\), and \((EY_0)^{2/3}\), Minkowski gives the local costs

\[
(q^{-1/2}+1+q^{-1/2})^2\ll1,
\]

\[
(q^{1/2}+q^{1/2}+q^{-1})^2\ll q,
\]

\[
(q^{1/6}+q^{1/3}+q^{-5/6})^2\ll q^{2/3}.
\]

The product of fixed constants over auxiliary primes is bounded by \(C^{\omega(\mathfrak q)}\ll_\eta Q^\eta\) and is absorbed in the permitted subpower. A uniformly bounded Euler product for these refined factors is neither needed nor claimed.

For every positive physical valuation \(\nu\ge1\), the proof retains both the amplitude indicator \(\mathbf1_{\nu\equiv0\ (6)}\) and the branch factor \(4^{\mathbf1_{\nu\equiv2\ (6)}}\). The three crude local sums are \(O(q^{-1})\), \(O(1)\), and \(O(1)\). In particular, the amplitude at \(\nu=6,12,\ldots\) is not lost in an invalid pointwise estimate. These disjoint row sectors can be added to the reindexed \(\nu=0\) sector. The resulting local costs remain \(O(1),O(q),O(q^{2/3})\).

The exact \(g\) and \(g,h\) support cutoffs have already been inserted in the reunited sums. Auxiliary reindexing leaves those cutoffs intact, and normalized smooth ratios are rescaled together with the new effective length. Thus the previous scalar separations, divisor extractions, dyadic tails, and \(E,F,G,Z\) optimizations remain valid uniformly for polynomially bounded \(Q\).

This proves the asserted improved bounds

\[
\sum_{k\sim H}|\mathcal C_{A,B}(k;\mathfrak q)|^2
\ll D^\epsilon
\left[
HA+\frac{QH^2A}{B}\min(A,\sqrt B)^{2\beta-1}
+Q^{2/3}\left(\frac{H^2A^2}{B}\right)^{2/3}
\right]
\]

and

\[
\sum_{k\sim H}|P_{A,B}(k;\mathfrak q)|^2
\ll D^\epsilon
\left[
HA+QH^2A B^{(2\beta-2)/3}
+Q^{2/3}H^{4/3}A^{4/3}B^{(2\beta-2)/3}
\right].
\]

Every nonzero row and every overlap with \(\mathfrak q\) is included. At \(A=B=D\), the row ranges are respectively

\[
H\le D^{(5-2\beta)/4}Q^{-1/2},
\qquad
H\le D^{(5-2\beta)/6}Q^{-1/2},
\]

when these ranges contain \(H\ge1\). The other energy terms do not impose stronger restrictions on \(1/2<\beta\le1\). In the completed case, the third exponent after substitution is \((7-2\beta)/3\le2\); in the literal case it is \((16+2\beta)/9\le2\).

## 8. Sharp balls and rapidly decreasing row profiles: PASS

Each final bracket is a positive combination of \(H\), \(H^2\), and \(H^{4/3}\). Summing inward dyadic annuli therefore gives the sharp ball estimate without a logarithmic row loss. The unit-norm rows are included in the terminal annulus at scale one.

For a fixed scalar profile \(\Phi(Nk/H)\), the bounded part \(Nk\le H\) follows from the ball estimate. On \(2^jH\le Nk<2^{j+1}H\), the profile is \(O(2^{-Mj})\). The choice

\[
H_j=2^jH,\qquad D_j=2^jD
\]

keeps \(A,B,\mathfrak q,H_j\) within one fixed polynomial ceiling in \(D_j\), after taking that ceiling's exponent to be at least one. The theorem's constant and smooth seminorm order are therefore independent of \(j\). Its loss becomes \(D^{\epsilon_0}2^{j\epsilon_0}\), and the largest row power contributes at most \(2^{2j}\).

Consequently \(M>2+\epsilon_0\) makes the full weighted tail geometric. This checks the otherwise material issue of row heights beyond any one polynomial scale in the original \(D\). The argument does not silently apply the original fixed-\(D\) estimate outside its declared parameter range.

The result concerns a fixed scalar row profile. It does not turn a row-dependent bilinear kernel into a product or remove the centered-column correction.

## 9. Finite algebra checker: PASS

I inspected the complete program and independently ran ordinary Python and Python with optimization enabled. Both outputs were byte-identical to the author's report.

| Artifact | SHA-256 |
|---|---|
| check_arbitrary_row_algebra.py | e24c08cca27df69e087e9a6ae71585bb5b2aeded01bd7fdde9a98f1c81883a08 |
| arbitrary_row_algebra_report.json | 31cb5ed797ffc306cd3f6b1d6eaaeea7796395d89ac5c3ac6932c144657c6e5d |
| arbitrary_row_algebra_audit_normal.json | 31cb5ed797ffc306cd3f6b1d6eaaeea7796395d89ac5c3ac6932c144657c6e5d |
| arbitrary_row_algebra_audit_optimized.json | 31cb5ed797ffc306cd3f6b1d6eaaeea7796395d89ac5c3ac6932c144657c6e5d |

The replay commands, run from /workspace/scratch/6ec6134c1535, were:

~~~bash
python check_arbitrary_row_algebra.py --output arbitrary_row_algebra_audit_normal.json
python -O check_arbitrary_row_algebra.py --output arbitrary_row_algebra_audit_optimized.json
~~~

The checker uses explicit exception-raising requirements, so optimization does not disable its tests. It checks 432 local scalar phase cases with formal fixed Gauss monomials; 336 cross-symbol, reciprocity, and zero cases; 104 Ramanujan valuation cases; the six rational valuation progressions for both powerful rows and the crude auxiliary weights; and 24 auxiliary parity cases.

The literal-zero regressions include a positive row valuation divisible by six. The sign regression detects omission of the odd reciprocity sign. A separate example detects that the Ramanujan separation fails without \(p\nmid ef\). These tests exercise the main exceptional arithmetic cases of the proposed adapter.

The computation uses exact sixth-root exponents and rational powers in the valuation algebra. It does not evaluate actual Gauss sums or residue symbols. It corroborates finite identities and exponent bookkeeping only; automorphy, coefficient formulas, scalar estimates, upper sieves, and infinite analytic bounds remain outside its certification scope.

## 10. Remaining boundary

The new transfer removes the squarefree-row restriction for the two specified positive norm families. It does not allow arbitrary coefficients in the Möbius sums, and the conditional scalar exponent still has its original analytic dependency.

The auxiliary estimate controls one corrected polynomial at a time. It does not control a retained signed auxiliary sum or the centered sesquilinear family with two independently corrected product columns. The original adverse fourth-moment dual range is still much larger than the literal row range proved here. No complete fourth moment, generalized hierarchy, or RH result follows.

No unresolved mathematical defect was found in the frozen proof snapshot.
