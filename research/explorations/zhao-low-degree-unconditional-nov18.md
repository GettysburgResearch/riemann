# An unconditional classification at one for small-degree Dedekind zeta functions

For \(B_K^*=2\Xi_K'(1)/\Xi_K(1)\), where \(\Xi_K\) is the entire pole-cancelled completed Dedekind zeta function, exactly **367 cubic fields and 871 quartic fields** satisfy \(B_K^*<2\). Their lists agree entry by entry up to field isomorphism with the [cubic](zhao-cubic-fields-nov18.md) and [quartic](zhao-quartic-fields-nov18.md) spectral inventories. The [unconditional inventory](zhao-low-degree-unconditional-nov18.json) gives each passing field's number of complex places, signed discriminant and descending canonical defining polynomial coefficients. This test concerns an unconditional real number attached to the field. On GRH it equals the zero-ordinate sum used in Zhao's question. Every field passing the test has no nontrivial real zero, with no GRH assumption.

The [Euler checker](../../scripts/check_zhao_low_degree_unconditional_nov18.py) reduces 13,818 non-Galois cubic candidates to 2,200 at \(P=16\), then to 1,195 at \(P=64\), and to 928 at \(P=256\). The [contour finisher](../../scripts/finish_zhao_low_degree_unconditional_nov18.py) tests these 928 and all 50 cyclic candidates. Its first target tolerance separates 977 strict comparisons; tightening from 0.03 to 0.0001 decides the last one.
For quartics the enlarged discriminant caps give 81,145 fields over all Galois groups. The Euler sieve leaves 7,264 at \(P=8\), 3,509 at \(P=32\), and 2,384 at \(P=128\). At the first contour tolerance 2,377 comparisons separate strictly, and the tighter second tolerance settles all seven remaining comparisons. In both degrees the finisher uses PARI's canonical defining polynomial to compare all passing fields to the previous inventories. For an abelian character group it obtains the field directly as the cyclotomic subfield fixed by the common character kernel. Every isomorphism class matches. The collection of 1,184 nonabelian cubic and quartic passing fields was independently checked with the full logarithmic-derivative Euler contour.

## A finite Euler rejection with no zero hypothesis

Let \(D(s)=\Xi_K'(s)/\Xi_K(s)\) for the pole-cancelled completed Dedekind zeta function. Its symmetry gives
\[
 M(g)=\frac{D(s)}{s-1/2}=\sum_\rho\Re\frac{1}{y_\rho+g},\qquad y_\rho=\rho(1-\rho),\quad g=s(s-1),\quad M(0)=B_K^*.
\]
This follows by averaging \(1/(s-\rho)\) at \(\rho\) and \(1-\rho\). The real summands at \(g=0\) are positive. Suppose \(B_K^*\le2\). Each central zero contributes four and every distinct real pair contributes at least eight, so all nontrivial zeros are nonreal. For an off-line quartet let \(y=u+iv\), with \(u=\beta(1-\beta)+\gamma^2>0\) and \(v^2=(1-2\beta)^2\gamma^2\le u\). Its four occurrences give \(4u/(u^2+v^2)\le2\), hence \(u^2+u\ge2u\), so \(u\ge1\) and \(|v|\le u\). On-line zeros have real \(y>0\). For \(g\ge0\), all terms of \(-M'(g)=\sum\Re(1/(y+g)^2)\) are consequently nonnegative. Thus
\[
 D(s)\le(s-1/2)B_K^*,\qquad
 D'(s)=M(g)+2(s-1/2)^2M'(g)\le B_K^*,\qquad s>1 .
\]

The first inequality and the completely split estimate \(\zeta_K'/\zeta_K(s)\ge n\zeta'/\zeta(s)\) give the discriminant condition
\[
 \log|\Delta|\le4(s-1/2)-2/s-2/(s-1)+n\log\pi
 -(n-r_2)\psi(s/2)-r_2\psi((s+1)/2)-2n\zeta'/\zeta(s).
\]
At \(s=109/50,17/8\) respectively this gives cubic caps 96900 and 55200. At \(s=5/2,61/25,12/5\) it gives quartic caps 861000, 533000 and 326000. The program checks each inequality with Arb. The cubic candidate enumeration uses PARI's complete cubic lists; the class field GRH caveat in the PARI manual starts at degree four. The quartics come directly from the three complete, corrected Bordeaux tables with SHA-256 verified in the [quartic source checker](../../scripts/check_zhao_quartic_tables_nov18.py), including all abelian quartics.

Fix \(T=\log P\). The two differential inequalities imply
\[
 D(s)+D'(s)/T-2(s-1/2+1/T)\le0.
\]
An ideal power of norm \(N\) contributes \((\log N/T-1)\log(N\mathfrak p) N^{-s}\), nonnegative if \(N\ge P\). Thus one may include *all* powers over each rational prime \(p\le P\) and omit every higher rational prime. For each residue degree \(f\), with \(z=p^{fs}\), the local correction to the archimedean and discriminant terms is exactly
\[
 f\log p\left(-\frac1{z-1}+\frac{f\log p}{T}\frac{z}{(z-1)^2}\right).
\]
A positive lower bound for this finite combination rejects the field unconditionally. The checker rounds each contribution downward to an integer multiple of \(2^{-28}\). Polynomial factorization supplies the residue degrees outside index primes, with full ideal decomposition at the remaining primes. It tests \(s=11/10,6/5,4/3,3/2,7/4,2,5/2\).

Every residual field then goes through the [full completed-function threshold certificate](../../scripts/check_zhao_field_threshold_nov18.py) operating on exact ideal counts. Its interval for \(H'(1)-(37/36)H(1)\), where \(H(s)=\Xi_K(s)e^{(s-1/2)^2/36}\), has the sign of \(B_K^*-2\). The program tightens the tolerance on intervals touching zero. It accepts no unresolved limit.

From the repository root the cubic census can be reproduced with

```sh
python scripts/check_zhao_low_degree_unconditional_nov18.py --degree 3 --limits 16 64 256 --output cubic-screen.json
python scripts/finish_zhao_low_degree_unconditional_nov18.py --degree 3 --input cubic-screen.json --output cubic-unconditional.json
```


For quartics, put the three authenticated Bordeaux tables in the directory named tables and run

```sh
python scripts/check_zhao_low_degree_unconditional_nov18.py --degree 4 --table-dir tables --limits 8 32 128 --output quartic-screen.json
python scripts/finish_zhao_low_degree_unconditional_nov18.py --degree 4 --input quartic-screen.json --output quartic-unconditional.json
```
