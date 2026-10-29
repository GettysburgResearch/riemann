# The square-part p6 local barrier

This note describes a bottleneck in the *separate* positive prefix/theta moment reduction, not a lower bound for an arithmetic character sum. The [coupled product estimate](../2026-10-29-coupled-theta-tail/README.md) is additional information and excludes the abstract spike below at the original endpoint. The source qualifications and exact rational full-core certificate are in [the main note](README.md) and [its checker](check_stratified_p6.py).

At the binding square-part stratum \(V=1\), set \(d=C\), \(\kappa=g=0\), \(D=Y^{\Delta}\), \(\Delta=6/5-C\), and \(B=Y^b\). For a cube-index dyad \(H=Y^s\), write \(X=Y^{\Delta-3s}\). The physical prefactor has exponent \(p_0=1/30+2C/3-b/6\). The active prefix bound for fixed \(p\) is the first face of
\[
 A_{2p}(H)\ll B H^p+H^{2p},
\]
while the active theta faces are
\[
 T_2(X)\ll B^2/X,\qquad T_4(X)\ll B^{1/3}X^{5/3},
\qquad T_2(X)\ll\sqrt{B T_4(X)}.
\]
The last two T2 bounds meet exactly at
\[
 s=\frac{11\Delta-8b}{33}.\tag{1}
\]
At that scale \(b-2T_2+T_4=0\), where the latter symbols mean base-\(Y\) exponents, so every fixed \(p\ge2\) for which the first prefix face is active gives the same Hölder exponent \(p_0-s+T_2\). It equals
\[
 \frac{445b+330d+320g+355\kappa-121}{330}
\]
in the corresponding general-face formula. Extra positive prefix moments alone cannot improve this witness.

For \(C=7/50\), the binding values are
\[
 b=\frac{4213}{4450},\quad s=\frac{551}{4450},\quad
 \log_Y X=\frac{1532}{2225},\quad
 T_2=\frac{2681}{2225},\quad T_4=\frac{6511}{4450};
\]
the physical exponent is exactly \(21/20\). For \(C=1925877/15625000\), the second witness is
\[
 b=\frac{1348218883}{1390625000},\quad
 s=\frac{516824123}{4171875000},\quad
 \log_Y X=\frac{122565353}{173828125},\quad
 T_2=\frac{857957471}{695312500},\quad
 T_4=\frac{2083611001}{1390625000},
\]
and the physical exponent is exactly \(19949123/18750000\).

There is an especially simple abstract feasibility model: take \(Y^b\) rows, and on every row put
\[
 |A|=Y^{s/2},\qquad |T|=Y^{(T_2-b)/2}.
\]
At either witness \(T_4=2T_2-b\). Hence, simultaneously, every real positive prefix moment equals the first-face upper bound \(Y^{b+ps}\), the second and fourth theta means equal their active bounds, and Cauchy is an equality. The elementary pointwise restrictions \(|A|\le H\), \(|T|\le X^{1/2}\) also hold with positive power margins. The aligned product has the target physical exponent. In particular, even an arbitrary collection of these positive moment bounds and their Hölder interpolations cannot force a local power saving. The model is not a construction of sextic characters, Möbius coefficients, or the signed physical dual sum; arithmetic cancellation could still improve the source estimate.

## An interior witness beyond both available bounds

The endpoint \(d=7/50\) alone is not enough to show a remaining obstruction: there the separately derived second-Poisson estimate already meets the 21/20 target. Consider instead the fixed interior parameters
\[
 d=\frac{13}{100},\quad \kappa=g=\log_YV=0,\quad b=\frac{24}{25},\quad \Delta=\frac{107}{100}.
\]
Then (1) gives
\[
 s=\frac{409}{3300},\quad \log_YX=\frac{192}{275},\quad
 T_2=\frac{336}{275},\quad T_4=\frac{408}{275}.
\]
The stratified positive-moment scalar bound has exponent \(3491/3300>21/20\). At the same parameters, even granting the proposed signed-diagonal cancellation, the existing second-Poisson nonzero-frequency upper bound has exponent
\[
 \frac76-\frac{5d}{6}-\frac{5g}{6}-\kappa=\frac{127}{120}>\frac{21}{20}.
\]
Thus taking the better of these two displayed bounds still does not reach the target at this fixed interior point. A uniform abstract spike on \(Y^{24/25}\) rows with \(|A|=Y^{409/6600}\), \(|T|=Y^{36/275}\) saturates the active prefix, theta and Cauchy faces here as well. The physical source and signed-diagonal qualifications of the second-Poisson estimate remain in force; this model is not a lower bound for either actual arithmetic expression.

## The coupled estimate excludes the endpoint model

The separate-moment spike does not obey the additional source-qualified coupled estimate \(\sum_b|A_b(H)T_b(X)|^2\ll H\Theta_6(B,D)Y^\epsilon\). At the E21 endpoint above, its product exponent is
\[
 s+T_2=\frac{5913}{4450},
\]
whereas \(s+\Theta_6(B,D)=35317/26700\). The difference is \(161/26700>0\). Thus the coupled estimate rules out this abstract positive model at that point; the separate-moment bottleneck does not apply once the coupled information is added. The coupled estimate still requires the source and orientation qualifications in its own note, and excluding this model does not itself complete the inverse-moment target.

The coupled estimate also excludes the abstract spike at the interior witness above: there the active \(\Theta_6(B,D)\) exponent is \(727/600\), below \(T_2=336/275\) by \(67/6600\). The coupled physical exponent at this single cube dyad is \(461/440<21/20\). Controlling the entire tail still requires a uniform estimate across all cube scales; this one-dyad calculation is not such an estimate.

## A new model that also respects the coupled estimate

The additional direct theta-second-moment cap changes the scalar witness. At the E21 endpoint take
\[
 C=\frac7{50},\quad b=\frac{554}{575},\quad u=\log_Y V=\frac b2,
 \quad\Delta=\frac{53}{50},\quad
 s=\frac{499}{6900},\quad \log_YX=\frac{7b}{8}=\frac{1939}{2300}.
\]
The prop:R off-face and the \(B^{5/6}X^{1/3}\) face of \(\Theta_6(B,X)\) meet at \(T_2=9b/8\). The relevant fourth-moment source face is \(T_4=43b/24\). Inserting this T2 cap throughout the cube sum gives the physical exponent
\[
 p_0+\frac{9b}{8}=\frac1{30}+\frac{2C}{3}+\frac{23b}{24}=\frac{21}{20}.
\]
The same formula gives the theta-boundary witness \(b=88917107/89843750\) and physical exponent \(19949123/18750000\). For a fixed-p prefix-Hölder tail at this scale, the second prefix face is active and its squared exponent is \(T_2+b/(24p)>T_2\); the coupled dyad upper bound exceeds \(T_2\) by \((\Delta-b)/2>0\). Thus placing this scale in the short or tail part cannot improve the displayed upper bounds by changing the cutoff or adding a fixed prefix power.

There is also a *new* uniform abstract model which respects the coupled-product information that excluded the preceding spikes. Take \(V=B^{1/2}\), hence \(M=B/V=B^{1/2}\) abstract rows in this square-part stratum, and on every row put
\[
 |A|=H,\qquad |T|=B^{5/16}.
\]
For every real \(p>0\), the prefix \(2p\)-moment is \(MH^{2p}=VH^{2p}\), exactly the second GL prefix face. The theta second moment is \(M|T|^2=B^{9/8}\), meeting both the prop:R off-face and \(\Theta_6(B,X)\); the actual fourth moment is \(M|T|^4=B^{7/4}\), below the source upper bound \(B^{43/24}\). Its pointwise constraints hold because \(|A|=H\) and \(|T|=B^{5/16}<X^{1/2}=B^{7/16}\). At the witness, the model's product exponent is \(2s+9b/8\), while the coupled \(H\Theta_6(B,D)\) exponent is larger by \((\Delta-b)/2>0\); the model therefore respects that coupled estimate as well. All identities hold at either endpoint after substituting its value of \(b\).

This is a feasibility model for the listed positive input inequalities at one scale; it does not construct actual characters or prove a lower bound for the signed physical core. A further source-qualified fixed-\(w\) cubic-sieve cap does rule it out: at \(V=B^{1/2}\), \(X=B^{7/8}\), that cap bounds T2 by \(B^{11/12+\epsilon}\), whereas this model has \(B^{9/8}\). See [the cubic cap](squarepart-cubic-theta-moments.md). The model therefore does not obstruct an argument that also uses that additional source estimate.
