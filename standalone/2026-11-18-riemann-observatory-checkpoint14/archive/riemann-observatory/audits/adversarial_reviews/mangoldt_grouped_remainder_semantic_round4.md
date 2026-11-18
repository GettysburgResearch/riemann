# Independent review of von Mangoldt's grouped remainder

Reviewer: semantic_skeptic. Date: 17 November 2026. Reviewed the exact abstract claim in `audits/mangoldt_grouped_remainder_corpus_round4.md` and independently reconstructed its uniform kernel and summation estimates. No numerical calculation or formal build is used.

**Conclusion:** the local O(log²h/h) remainder statement is valid under its stated hypotheses. The growing number of zeros is controlled by the local count; proximity of h to a zero ordinate causes no singularity because the contour remains a fixed positive real distance from all poles. No mathematical counterexample or missing assumption was found in this inspected implication. This does not certify the full historical explicit-formula proof or establish a new source-error finding.

## 1. Exact hypotheses and source scope

Fix x>1, u=logx>0, real r, and a>0 with a+r>1. Let alpha_j=gamma_j+i eta_j, counted with multiplicity, with gamma_j>=gamma0>0, |eta_j|<=1/2, and integer-unit local counts

#{j:m<=gamma_j<m+1}<=C log(2+m), m=0,1,... .

Put c=1/2-r and beta_(j,±)=c±i alpha_j. Their real parts are c∓eta_j in[-r,1-r], their imaginary parts are±gamma_j, and

delta=a+r-1<=a-Re(beta)<=a+r=D,

where delta>0. In particular beta is nonzero, |beta|>=gamma_j, and the contour Re(s)=a never passes through a pole, even when h equals gamma_j. No RH or reality of alpha_j is assumed.

Primary passages actually inspected visually for this review:

- German1894 extract, printed891–892: the exact H-dependent grouped decomposition and the following invocation of equations14–16 and the second theorem of SectionI;
- Laugel's French translation, printed66–68 and72: local count theorem2, kernel inequalities14–16 and the grouped-limit sentence;
- German1895 full article, printed286–287 and290–291: equation49, the bound on a paired coefficient sum independent of H, and the explicit growing tail estimate;
- de la Vallée Poussin's1897 offprint of the1896 memoir, appendix printed70: the footnote alleging a growing-sum error in the1894 extract.

These are targeted source readings, not full-work readings of the14-page original extract,51-page1895 article, or Vallée memoir. The corpus researcher's separate full translation reading is not being counted as this reviewer's reading. Canonical identity/source records are PAPER-H405/H406/H404. Private source images/PDFs remain excluded from the distributed archive.

## 2. Uniform kernel bounds independently derived

Define

P_h(beta)=(1/(2pi i)) integral_(a-ih)^(a+ih) x^s/(s-beta)ds.

For beta=b+i gamma and d=a-b in[delta,D], change variable t=Im(s)-gamma:

P_h(beta)=x^beta/(2pi) integral_(-h-gamma)^(h-gamma)
 exp(u(d+it))/(d+it)dt.                                      (1)

For each d in this fixed positive interval, define the upper oscillatory ray from v>=0. For v>=1, integration by parts gives a bound at most

exp(uD)/u [1/|d+iv|+integral_v^infinity dt/(d²+t²)]
 <=2 exp(uD)/(uv).

For0<=v<=1, use the bounded central interval and the same ray estimate from1; the central denominator is at least delta. Thus both positive and negative ray tails are bounded uniformly by K/(1+v). Reflection gives the negative-ray bound because d,u are real. All constants may depend on the fixed x,a,r; they do not depend on j,h or the distance from h to a zero ordinate.

The full vertical integral in(1), before the factor x^beta, equals1. One elementary verification closes exp(uz)/z along a rectangle with right side Re(z)=d>0 and left side Re(z)=-B. For fixed height, the left side vanishes as B tends to infinity; the horizontal sides have size O(exp(ud)/(u h)). The enclosed residue is1. Letting h tend to infinity proves the value. The preceding ray bounds also establish separate convergence of both improper tails, so shifting unequal endpoints causes no ambiguity.

Because |x^beta| is uniformly bounded for b in[-r,1-r], these facts prove

|P_h(beta)-x^beta|
 <=K[(1+h-|gamma|)^(-1)+(1+h+|gamma|)^(-1)]
 for |gamma|<=h,                                             (2)

and

|P_h(beta)|<=K/(1+|gamma|-h), for |gamma|>h.                  (3)

For(3), the shifted interval is wholly on one side of0 and is a difference of two same-side ray tails. Both estimates remain bounded when |gamma|-h tends to0. Treating beta=0 separately with d=a gives P_h(0)=1+O(1/h).

The constants in the corpus notation C_x should be understood to include the fixed contour parameters a,r as well. This is consistent with the stated final O_(x,a,r,C,gamma0) bound; uniformity as a+r decreases to1 or x decreases to1 is not claimed.

## 3. Pairing and finite-height interchange

The exact identity

J_h(beta)=(P_h(beta)-P_h(0))/beta

follows from1/[s(s-beta)]=(1/beta)[1/(s-beta)-1/s]. The paired resolvent satisfies

1/(s-beta_+)+1/(s-beta_-)
 =2(s-c)/[(s-c)²+alpha_j²].

For s on a fixed finite contour, this is O_h(gamma_j^(-2)) uniformly for large gamma_j. The local count implies sum gamma_j^(-2)<infinity, so the series of **paired** integrands converges absolutely and uniformly there. Its integral may therefore be interchanged with that paired series. No unpaired absolute convergence is asserted.

There is also the useful exact bound

|1/beta_++1/beta_-|
 =|2c|/|beta_+ beta_-|<=2|c|/gamma_j².                        (4)

This factorization works for complex alpha_j and avoids any unjustified positivity assertion about alpha_j². At c=0 the pair is identically0. An unpaired reciprocal sum need not converge: alpha_j=j gives1/(c+ij) with a harmonic leading part. Pairing is an essential retained hypothesis, not a cosmetic convention.

## 4. Four-piece remainder estimate

Let S_h=sum_(gamma_j<=h) sum_±(x^beta-1)/beta and let I_h be the full sum of paired J integrals. Exact algebra gives

S_h-I_h
 =sum_(gamma<=h,±)(x^beta-P_h(beta))/beta
 +(P_h(0)-1)sum_(gamma<=h,±)1/beta
 -sum_(gamma>h,±)P_h(beta)/beta
 +P_h(0)sum_(gamma>h,±)1/beta.                               (5)

Every sum here is finite or absolutely convergent in the prescribed pairing. This is an identity before taking h to infinity.

The local count gives

sum_(gamma<=h)1/gamma=O(log²(2+h)),

sum_(gamma>h)1/gamma²=O(log(2+h)/h).

Any shifted unit interval is covered by at most two integer-unit bins, so the count bound also applies to intervals measured from a noninteger h.

For the first term of(5), use(2) and |beta|>=gamma. Below h/2 the kernel errors are O(1/h), yielding O(log²h/h). Between h/2 and h, use1/gamma<=2/h; distance bins from h contain O(logh) zeros each, and their1/(1+distance) weights sum to O(logh). This gives the same order. The second ray in(2) is smaller and causes no additional difficulty.

For the second term, pairing and(4) make the partial coefficient sum bounded independently of h. Its Perron multiplier is O(1/h), so this whole term is O(1/h). This slightly sharper treatment matches the source's explicit discussion on1895p287.

For the third term, use(3). In h<gamma<=2h,1/gamma<=1/h and shifted unit distance bins again give O(log²h/h). Above2h the summand is O(1/gamma²), whose tail is O(logh/h).

The final term is O(logh/h), using bounded P_h(0) and the paired tail(4). Thus(5) proves

S_h-I_h=O_(x,a,r,C,gamma0)(log²(2+h)/h).

No individual-summand limit has been summed over an uncontrolled growing set. No separation between h and a zero ordinate is needed. The jump at an exact tie changes a partially included equal-height block by at most O(logh/h), because its multiplicity is O(logh) and each W_j is O(1/gamma_j). This also justifies the stated increasing-height ordering with arbitrary order inside a tie.

The existence/value of lim I_h is a separate input from the logarithmic derivative and pointwise Perron inversion. The local-count lemma does not prove that input by itself.

## 5. Historical reading and limits of the adjudication

The actual German1894p892 says the grouped terms are controlled "unter Benutzung der Formeln(14.) bis(16.) und des zweiten ... Sätze" of SectionI. The corresponding French72 sentence explicitly invokes the same kernel estimates and local-count theorem. Thus the translation did not introduce that reference after the fact.

Taking a fixed admissible k=2 in the local count of French66–67 supplies the unit-height O(logh) bound required above, after harmless treatment of low zeros. I did not independently audit all constants or the proof of that local-count theorem. The source's global O(log²h) counting remainder should not be silently replaced by a later stronger global theorem; it is the separately stated local estimate that is used here.

The German1895p286 identity and pp287,290–291 estimates explicitly keep H and control the complete sums. They predate the1896 criticism. The criticism's printed70 footnote calls the purported mistake irreparable and says growth of H appears forgotten; this review does not accept that allegation as a verified error. The inspected implication can be rigorously justified from exactly the cited types of inputs. That conclusion does not certify every preliminary entire-function argument, the full contour/Perron application, or later parameter-integration/branch choices in either historical work.

Fixed x>1 and the positive contour margin are material. Without a+r>1 a pole may lie on the integration line; a bound uniform in that degenerating margin is false. The integration-by-parts constants involve1/logx, so no uniformity as x tends to1 or across arithmetic jumps is obtained. Pointwise Perron half-values and a discontinuous limit are compatible with the result; arbitrary permutations of the zero series are not licensed.

Classification: **Independently checked with no issue found in the inspected portion.** The result is a scoped reconstruction of the grouped-limit step, not a new RH result, a full-paper audit or a newly verified historical error. Director adjudication remains separate.
