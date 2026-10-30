# The local positive-moment bottleneck

This is a limitation of the displayed source-moment and Hölder upper bounds, not a lower bound for the actual character sums. It applies at the binding dyad of [the p=4,5 reduction](README.md). All physical source, mask, profile and reciprocity inputs there remain in force.

Write \(P=Y^{6/5}\), let \(D=Y^\Delta\), \(B=Y^b\), and let the cube-index scale be \(x=Y^s\), with completed-theta scale \(Z=Y^{\Delta-3s}\). At the residual-core point \(d=C,\ k=g=0\), write \(T_2,T_4\) for the base-\(Y\) exponents of the *upper bounds* for the second and fourth completed-theta sums. The common physical prefactor has exponent \(p_0=1/30+2C/3-b/6\). If the quadratic prefix has the input
\[
 \sum_b|A_b(x)|^{2p}\ll (Yx)^\epsilon\bigl(Bx^p+B^{1/2}x^{2p}\bigr),
\]
then for each fixed integer \(p\ge2\), interpolation of theta moments followed by Hölder gives the exponent
\[
 E_p=p_0-2s+\frac{\max(b+ps,b/2+2ps)}p
       +\Bigl(1-\frac2p\Bigr)T_2+\frac{T_4}p. \tag{1}
\]
The source masks, derivatives and bounded row multipliers are included in these moment inputs; (1) does not assume that a row-independent term can be dropped before a positive square.

For the 21/20 target, the exact witness is
\[
 C=\frac7{50},\quad b=\frac{10283}{11000},\quad
 \Delta=\frac{53}{50},\quad s=\frac{579}{5500},\quad
 \Delta-3s=\frac{4093}{5500}.
\]
At it, the active T2 source face and fourth Θ6 face have
\[
 T_2=\frac{619}{550},\quad T_4=\frac{17071}{11000},\quad
 p_0=-\frac{641}{22000}.
\]
The A8 first face and A10 second face equal \(2983/2200\) and \(33443/22000\), respectively; substitution gives \(E_4=E_5=21/20\). The T2 source face is strictly below both its trivial bound and \(\sqrt{B T_4}\); all named active A and Θ faces are strict.

For the theta target, substitute \(C=1925877/15625000\), \(b=3294802253/3437500000\), \(s=550399567/5156250000\), and \(\Delta-3s=1300253963/1718750000\). Then
\[
 T_2=\frac{199454829}{171875000},\quad
 T_4=\frac{16297341883}{10312500000},\quad
 E_4=E_5=\frac{19949123}{18750000}.
\]

At either witness, \(4s<b/2<5s\). Put
\[
 U=b-2T_2+T_4>0,\qquad V=b/2-2T_2+T_4<0.
\]
For the first witness \(U=1297/5500\), \(V=-1019/4400\); for the second \(U=1123584581/5156250000\), \(V=-1078013687/4125000000\). Thus (1) decreases strictly with integer \(p=2,3,4\), and increases strictly with integer \(p\ge5\). It is minimized by \(p=4\) and \(p=5\), both at the target. Interpolating any two available integer prefix moments makes the logarithm of the prefix norm affine in \(1/p\), and the theta Hölder exponents are affine in \(1/p\) too; the resulting bound is a convex combination of the two corresponding integer bounds, hence cannot improve this witness. This statement concerns interpolation of the *available integer moments*. Directly assuming the displayed two-face prefix bound for arbitrary real p would be a stronger input and has a lower minimum between 4 and 5.

A concrete way past this obstruction is a **uniform structured saving** in one active moment, for the actual row family and all fixed ray, column-mask and profile/derivative variants. For example, in a fixed small neighborhood of the first witness, one could seek
\[
 \sum_b |T_{bk}(Z;f)|^2\ll Y^{619/550-\eta+\epsilon},\qquad \eta>0, \tag{2}
\]
where the exponent is adjusted continuously with the dyadic parameters and (2) retains the original squarefree label and masks. Alternatively one could seek the corresponding saving in the fourth mean \(\sum_b|T_{bk}|^4\) below \(Y^{17071/11000}\). Since the two active scale slopes are \(-3/4\) and \(4/5\), a saving \(\eta\) in the second mean lowers the local crossing by \(17\eta/31\), and the same saving in the fourth mean lowers it by \(7\eta/31\). A saving \(\eta\) in the active eighth or tenth prefix mean lowers it by \(4\eta/31\) or \(3\eta/31\), respectively. These are local consequences; a uniform improvement of the global core also requires checking the rest of its parameter polytope and handling the physical signed-diagonal and profile interfaces. None of these structured savings is established here.

## A common-spike model

The obstruction is also visible without appealing merely to the form of the Hölder bound. At the 21/20 witness set
\[
 N=Y^{699/1000},\qquad |A_b|=Y^{3613/44000},\qquad
 |T_b|=Y^{4691/22000}
\]
on the same \(N\) abstract rows, and set both quantities to zero on the remaining rows. Floors and fixed constants do not affect exponents. Then
\[
 \begin{aligned}
 N|A|^8&=Y^{2983/2200},& N|A|^{10}&=Y^{33443/22000},\\
 N|T|^2&=Y^{619/550},& N|T|^4&=Y^{17071/11000}.
 \end{aligned}
\]
The number of rows is at most \(B\), and the pointwise size constraints \(|A|\le x\), \(|T|\le Z^{1/2}\) hold with strict power margins. For every integer \(p\le4\), the difference between the first GL prefix face \(b+ps\) and the model's \(699/1000+2p(3613/44000)\) is \((4-p)1297/22000\). For every integer \(p\ge5\), the corresponding difference from the second face \(b/2+2ps\) is \((p-5)1019/22000\). Thus the model obeys every displayed positive integer prefix-moment bound, and hence their interpolated bounds; its second and fourth theta moments meet the active source bounds and obey their trivial/Cauchy alternatives.

Nevertheless the aligned product has physical exponent
\[
 p_0-2s+\frac{699}{1000}+\frac{2\cdot3613}{44000}
                         +\frac{2\cdot4691}{22000}=\frac{21}{20}.
\]
Consequently those positive moment inequalities, even all together, do not force a power saving in the product. This is an abstract feasibility example; it does not construct character sums, a physical dual block, or a counterexample to a signed arithmetic estimate.

The theta-boundary witness has the same construction with
\[
 N=Y^{694294327/937500000},\quad
 |A|=Y^{1108394283/13750000000},\quad
 |T|=Y^{4330052143/20625000000}.
\]
These exponents saturate its displayed A8, A10, T2 and T4 bounds simultaneously. The first-face margin decreases to zero at \(p=4\), and the second-face margin increases from zero at \(p=5\), so the same all-integer-moment argument applies.
