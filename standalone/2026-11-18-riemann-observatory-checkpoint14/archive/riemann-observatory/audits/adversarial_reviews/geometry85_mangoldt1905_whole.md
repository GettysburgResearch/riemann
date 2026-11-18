# Von Mangoldt 1905 | Complete original-source reading

PAPER-GEO82-MANGOLDT1905. Hans von Mangoldt, *Zur Verteilung der Nullstellen der Riemannschen Funktion \(\xi(t)\)*, *Mathematische Annalen* 60 (1905), 1–19, dated Aachen, 6 May 1904 at the close. I read all nineteen original German pages, using OCR to assist with prose and the rendered formulas to check the contour, finite differences, coefficient choices and final bound. The local GDZ article has twenty PDF pages because of the provider cover. Printed p. \(j\) is PDF p. \(j+1\). Source SHA-256 7dd69d353ee6a173cc856131fc1bb07e222e1e2f99b138b4b251d0998d11a5ec, reverified. The original title visibly uses xi, despite the gamma glyph in some index metadata. This earns a complete original-source Level 1 reading. The reconstruction is submitted as a single review, without automatic Level 2 or 3 adjudication. [GDZ original scan](../../sources/geometry81/mangoldt1905_gdz.pdf) · [GDZ article download](https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0060/LOG_0007.pdf) · [Publisher identity](https://doi.org/10.1007/BF01447494)

## Main result and theorem graph

Write \(\Xi(t)=\xi_*(1/2+it)\), where \(\xi_*(s)=s(s-1)\Gamma(s/2)\pi^{-s/2}\zeta(s)/2\). The source's \(\alpha=\beta+i\gamma\) is a zero in the **\(t\)-plane**. In modern \(s\)-plane notation \(\rho=1/2+i\alpha\), so \(\beta=\Im\rho\) and \(\gamma=1/2-\Re\rho\). The \(\beta\) being counted is the ordinate of an arbitrary nontrivial zero. The paper proves the total count, with multiplicities, at heights \(T\) for which the vertical line \(\Re t=T\) contains no zero. The concluding display on p. 19 gives, for \(T>28.558\),
\[
\left|N(T)-\frac{T}{2\pi}\log\frac{T}{2\pi}
                +\frac{T}{2\pi}-\frac78\right|
<0.43200\log T+1.91662\log\log T+12.20373.
\]
The opening constant \(13.07873\) is the bound after absorbing \(7/8\). The paper expressly contrasts the earlier 1895 p. 266 bound \(0.34(\log T)^2+1.35\log T+2.58\) for \(T>12\).

| Printed pages | Proof role and inputs |
|---|---|
| 1 | Riemann's count, the 1895 bound, and the new explicit target. |
| 2–4 | §1. Symmetric contour with an external line \(a>1/2\). Multiplicity, branch continuation, gamma identity (1)–(3), and Stieltjes' bounded Stirling remainder. |
| 5–6 | §1 ends with (4). §2 starts the neighboring-edge subtraction (5) and extracts the second difference of each paired product factor. |
| 7–9 | §2. Separate \(|T-\beta|<2k\) from its complement. Figures 2–3 control near conjugate pairs. Taylor and the cubic distance bound control the far part, giving (6)–(7). |
| 10–11 | Formula (8), then §3 with \(a=3/2\), \(k=\tan1\) and the 1895 p. 265 short-window count. The cubic shell sum (9) is \(O(\log T)\), proving the sharpened order. |
| 11–14 | §4. Move the external line to \(a=1/2+u\). Euler-log estimates (10)–(12), positive argument accumulation and the local bound (13)–(15), then Taylor expansion of the inverse arctangent. |
| 15–17 | (16)–(20) split the local-count main term and remainder and estimate weighted shells. (21) combines the bounds. (22)–(25) choose \(k=0.675\) and \(u=3.2650/\log T\). |
| 18–19 | Small-height context from de la Vallée Poussin and Gram; bounds for the remaining terms, (26)–(29), and the final numerical display. |

## The contour and actual logarithmic improvement

Choose \(a>1/2\). Work in the right half of the \(t\)-plane on the rectangle bounded by \(\Re t=0,T\) and \(\Im t=\pm a\). Symmetry of the real entire \(\Xi\) makes the total variation around the rectangle twice the variation on \(-ia\to T-ia\to T\). The initial logarithm at \(-ia\) is real, and the imaginary axis is free of zeros (the corresponding real \(s\) values give a positive completed function). The horizontal change is \(\Phi_1(a,T)\), and the upward change from \(T-ia\) to \(T\) is \(\Phi_2\). The argument principle gives
\[
N(T)=\frac{\Phi_1(a,T)+\Phi_2}{\pi}.
\]
The \(\zeta\) logarithm on \(\Re s=1/2+a\) is the Euler logarithm. Put \(Z(a,T)=\Im\log\zeta(1/2+a+iT)\). With \(z=1/4+a/2+iT/2\), the source uses \(\Gamma(z+1)(a-1/2+iT)\pi^{-z}\zeta(1/2+a+iT)\). Stieltjes' bounded remainder for \(\log\Gamma(z)\) is at most \(1/[12|z|\cos^2(\arg z/2)]<1/(3T)\), pp. 3–4. Expanding the two elementary logarithms gives (4),
\[
\Phi_1(a,T)=\tfrac T2\log(T/(2\pi))-\tfrac T2+(7/8+a/4)\pi+Z(a,T)+O_a(T^{-1}).
\]
The comparison increment \(\Phi_3\) from \(T-2ia\) to \(T-ia\) equals \(\Phi_1(a,T)-\Phi_1(2a,T)\) by Cauchy's theorem or continuity of the same log on the zero-free strip below the zeros. Thus \(\Phi_3=-a\pi/4+Z(a,T)-Z(2a,T)+O_a(T^{-1})\), giving the \(7/8\) in (8) after adding \(\Phi_1\).

The central technical step is the **difference of two equal-length argument increments**, which suppresses the far zeros more strongly than bounding \(\Phi_2\) alone. The paper uses the paired entire-function factorization, with opposite factors kept adjacent or at bounded separation. The paired product is locally normally convergent and the change of its logarithm along any fixed zero-free path is the sum of the factor changes. For the contribution to \(\Phi_2-\Phi_3\) of a zero \(\beta+i\gamma\), set \(d=T-\beta\ne0\), \(F_d(x)=\arctan(x/d)\) with values in \((-\pi/2,\pi/2)\). Then the contribution is exactly
\[
Q_a(d,\gamma)=2F_d(\gamma+a)-F_d(\gamma)-F_d(\gamma+2a).
\]
Any constant adjustment of an argument on the negative-real side of \(d\) cancels from the increments. The source's Taylor formula on p. 8 gives \(|Q_a|\le a^2(3a+1)|d|^{-3}\), using \(|\gamma|\le1/2\).

A useful direct proof of the sign and decay is
\[
Q_a(d,\gamma)=\int_0^a\int_0^a
  \frac{2d(\gamma+y+z)}{[d^2+(\gamma+y+z)^2]^2}\,dy\,dz.
\]
The induced triangular weight in \(x=\gamma+y+z\) is symmetric around \(a+\gamma>0\) and \(w(x)\ge w(-x)\) for \(x\ge0\). Pairing positive and negative \(x\) therefore shows \(Q_a(d,\gamma)\) has the sign of \(d\), even when \(\gamma<0\) and a pointwise integrand has the opposite sign. It also gives the slightly sharper bound \(|Q_a|\le 2a^2(a+\gamma)|d|^{-3}\): after this pairing replace \((d^2+x^2)^{-2}\) by \(|d|^{-4}\), and integrate the first moment of the triangular weight. This is a reconstruction and a modest coefficient improvement, with no priority or strengthened final numerical bound asserted.

For near zeros, the real-zero contribution has magnitude \(<\pi/2\). For nonreal zeros, group \(\gamma,-\gamma\) at the same \(\beta\), including equal multiplicities. Each pair has aggregate contribution \(<\pi\) in magnitude. Indeed for \(d>0\) the upper increment sum is \(F_d(a+\gamma)+F_d(a-\gamma)\in(0,\pi)\); the lower increment sum is also in \((0,\pi)\), each term a positive difference of arctangents whose arguments have the same positive sign. For \(d<0\) both signs reverse. With cancellation between the two sides of \(T\), the near sum is bounded by \((\pi/2)K\), with \(K\) the **larger** of the multiplicity counts in the two intervals of length \(2k\) abutting \(T\). The far sum is bounded by \(a^2(3a+1)\) times the larger one-sided sum of \(|T-\beta|^{-3}\). This recovers (6), including the one-sided maximum rather than the two-sided total.

In §3 take \(a=3/2\), \(k=\kappa=\tan1\). Both external Euler logs are bounded by \(\log\zeta(2)\). The invoked 1895 p. 265 lemma counts the zeros in an interval of length \(2\kappa\) at large height by \(\kappa\log\) of its center. Bounded low intervals are harmless and reflection gives the lower-height estimates. Splitting the far ranges into shells \(2\nu\kappa\le |T-\beta|<2(\nu+1)\kappa\) produces
\[
\sum\nolimits'|T-\beta|^{-3}
\ll \sum_{\nu\ge1}\nu^{-3}\log(2+T+\nu)
=O(\log T).
\]
The source gives the explicit \(\zeta(3)\) and \(\zeta(2)\) coefficients by \(\log(1+v)\le v\). This supplies \(O(\log T)\) for the actual remaining edge. It uses earlier **local** control, not the older global \(O(\log^2 T)\) bound alone. [1895 original, p. 265 and neighboring count proof](../../sources/history_round4/mangoldt1895_pp255-305.pdf)

## Explicit constants and low-height inputs

In §4 set \(a=1/2+u\). The Euler log satisfies \(|Z(a,T)|<-\log u+u\) from \(\zeta(1+u)<1+1/u\), and \(|Z(2a,T)|\le\log\zeta(3/2)\). A horizontal external segment of length \(2k\) receives nonnegative argument increment from every zero. For projected ordinates in that segment the increment is at least \(\arctan(2k/(1+u))\), by its minimum at an endpoint and the maximal vertical distance \(1+u\). Thus \(\Phi_1(a,T+2k)-\Phi_1(a,T)\) bounds the local count as (13). Stirling and elementary Taylor estimates give (14)–(15),
\[
 K<\frac{k\log(T/(2\pi))-2\log u+2u+6.4759/T}
          {\arctan(2k/(1+u))}
\]
in the stated numerical range \(0.67<k<0.68\), \(0<u<0.97413\), \(T>12\), with reflection and monotonicity as on pp. 13–14 for the other half-interval. The no-zero range \(|\beta|\le12\) is drawn from the earlier count work. The Maclaurin bounds for this reciprocal in p. 14 isolate its leading/linear terms \(M\) and controlled excess \(P\) in (16)–(18). Repeating that estimate outside using the shell location \(T+2\nu k\) gives the extra \(Q\) term multiplying \(\zeta(2)/T\) in (19)–(20). This is how the coefficient is reduced, compared with the fixed \(a\) proof.

The leading coefficient in (21) is
\[
 A(k)=\frac{32\pi k^3+5\zeta(3)}{64\pi k^2\arctan(2k)}.
\]
Equation (22) gives its critical-point condition. Only the value at \(k=0.675\) is required to obtain the claimed upper bound. Independent numerical evaluation of (23)–(25) gives approximately \(0.4319412744,\ 0.5869391418,\ 1.9164457707\), agreeing with the printed upper roundings \(0.43200,0.58704,1.91662\). Minimizing \(0.58704u\log T-1.91662\log u\) gives \(u\simeq3.2650/\log T\), and for \(T>28.558\) this is \(<0.97413\). The choice makes \(u\log T\) bounded and \(-\log u=\log\log T-\log(3.2650)\). That explains the two scales and the shape of the final error. I checked p. 19's numerical bound as a published assertion and checked the displayed leading roundings and choice of \(u\) independently. I did not produce an interval-arithmetic certificate for every decimal in (26)–(29) or the final \(12.20373\). This does not affect the independent \(O(\log T)\) reconstruction.

Pages 17–18 cite de la Vallée Poussin for the small range up to 28.558 and Gram for the approximate ordinates \(14.134725,\ 21.022040,\ 25.010856\). The paper regards these three particular zeros as simple. No simplicity assumption for general zeros enters (6), the shell sums, or the argument principle. The upstream de la Vallée Poussin and Gram numerical/analytic proofs were taken as named source inputs, not independently re-audited here. Stieltjes' remainder used in §1 likewise remains a cited external estimate.

## Modern exact line and limits at an ordinate

Put \(S(T)=\pi^{-1}\arg\zeta(1/2+iT)\) along \(2\to2+iT\to1/2+iT\), with initial real logarithm, and
\[
\vartheta(T)=\Im\log\Gamma(1/4+iT/2)-(T/2)\log\pi
\]
on the branch from \(T=0\). Away from a zero ordinate, deform the rectangle description to \(a=3/2\), i.e. \(\Re s=2\), and read the factors at \(1/2+iT\). The polynomial \(s(s-1)\) contributes continuous argument \(\pi\), since the two factors have upper-half-plane arguments whose sum ends at \(\pi\) on the critical line. The gamma and zeta arguments give
\[
 N(T)=1+\vartheta(T)/\pi+S(T)
 =\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac T{2\pi}+\frac78+S(T)+O(T^{-1}).
\]
This is the exact modern Riemann–von Mangoldt line with its continuous branches. The 1905 derivation reaches the \(7/8\) and \(O(\log T)\) by the different exterior-line subtraction just reconstructed.

The original paragraph on p. 2 selects heights whose vertical line is zero-free, so the literal contour has no endpoint-zero convention. At a zero ordinate \(T_0\), let \(m(T_0)\) denote the total multiplicity of the zeros with that ordinate, on or off the critical line. The right count includes all \(m(T_0)\), the left count none, and the midpoint count includes half. These conventions follow by one-sided limits, and the same \(O(\log T)\) error follows from the continuity of the smooth approximant and the error envelope. The precise strict inequality of the printed no-zero-height numerical statement becomes a weak inequality by this limiting argument. For the midpoint exact line average the corresponding one-sided arguments. A horizontal path through a zero may not be used as a continuous log path without such a convention.

There is a short modern alternative using Jensen, distinct from the proof in this paper. The real-part continuation \(g_T(z)=[\zeta(z+iT)+\zeta(z-iT)]/2\) is positive at \(2\) uniformly (\(g_T(2)\ge2-\zeta(2)\)). On a fixed disk about \(2\) slightly larger than the length \(3/2\) of the horizontal segment, Euler–Maclaurin bounds it by a power of \(T\). Jensen bounds the number of crossings of the imaginary axis by \(O(\log T)\), and between successive crossings the argument changes by at most \(\pi\). On the vertical line \(\Re s=2\) the argument is bounded directly. Thus the modern approach also gives \(S(T)=O(\log T)\). It should not be substituted as a description of von Mangoldt's original proof. [Earlier memoir adjudication and Jensen comparison](geometry81_riemann_adjudication_input.md)

## Reusable lemma and a limitation

For a real entire function with a locally normally convergent paired factorization, all zeros in a fixed horizontal strip, and a multiplicity bound \(O(\log(2+T))\) in each fixed-width window, the equal-edge subtraction above has total error \(O(\log T)\) for each fixed \(a\) wider than the strip half-width. The two vertical evaluations can then be compared to the same exterior asymptotics. This packages the original cubic-decay mechanism without invoking an interior estimate on the argument. It may apply to other paired products with independently available exterior asymptotics, symmetry, and local zero counts. Bounding a single unsymmetrized edge by absolute inverse distances loses the cancellation and supplies no such estimate. The method controls a total count, and gives no critical-line proportion or canonical arithmetic spectral realization.
