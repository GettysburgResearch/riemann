# Original Li1997: source reading and central proof audit

2026-11-17, equivalences agent. Work ID PAPER-E008. The complete nine-page original article text was read, not replaced by Lagarias2007. The central positive-coefficient/analytic-continuation argument is independently reconstructed below. No novelty, RH advance, or verified error in the original theorem is claimed.

## Bibliographic grounding and access

Xian-Jin Li, **The Positivity of a Sequence of Numbers and the Riemann Hypothesis**, Journal of Number Theory65(2)(1997),325–333, DOI10.1006/jnth.1997.2137, PII S0022314X97921375, articleNT972137. Crossref confirms author, title, volume, issue, pages and publication month1997-08. The reproduced original header records receipt10September1996 and revision16December1996. Metadata is saved in sources/li_original_round2/crossref.json.

Publisher page and PDF/API requests returned403. Original primary text was accessed as a complete nine-page reproduction at https://paperzz.com/doc/7086946/--science-direct, with page markers325–333 and original article header. Its download link https://paperzz.com/download/7086946 also returned403. Private tool response: sources/li_original_round2/li1997_paperzz_tool_response.json. Mathematical extraction is degraded; source passages are identified by page/equation and the tool line numbers below. No publisher-quality PDF or author manuscript was obtained. This is actual primary-work text, with access-quality limitations, not an abstract or a later summary.

Whole-work status: substantive reading Level1. Scoped Level2: Theorem1's analytic positive-coefficient necessity argument and its local identities reconstructed, with independently verified normal-convergence conditions. Whole-paper Level2 is not claimed: the Dedekind theta integral and its textbook antecedents were not independently audited, and degraded formula extraction prevents an exact typeset comparison of every displayed constant.

Crossref relation/update fields and targeted source searches yielded no verified corrigendum in this run. This is not an exhaustive corrections-history search. Later proof claims by the same author are different works and do not alter the status of the1997 criterion.

## Exact normalization and original statements

Li uses the completion

Xi(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s),

so Xi(0)=Xi(1)=1; this is twice the common modern xi. Define, for every integern>=1,

lambda_n=[1/(n-1)!] D_s^n[s^(n-1)log Xi(s)]_(s=1).       (1.1)

Theorem1,p.325: all nontrivial zeros of the Riemann zeta function lie on Re(s)=1/2 **if and only if lambda_n>=0 for every positive integern**. It is not a finite-prefix criterion. A constant positive rescaling of Xi does not affect these coefficients: its logarithm adds a constant times the polynomial s^(n-1), whose nth derivative vanishes.

Theorem2,p.329: the corresponding statement holds for the Dedekind zeta function of each algebraic number fieldk, with its normalized entire, self-reciprocal completion Xi_k(0)=Xi_k(1)=1 and its own lambda_n(k). This is not stated as an unrestricted theorem about every L-function or every root number. Nontrivial zeros include multiplicity; gamma/trivial zeros are removed by completion.

For the Dedekind normalization, the source defines Z_k(s)=G_1(s)^(r_1)G_2(s)^(r_2)zeta_k(s), with its specified archimedean gamma factors, then Xi_k(s)=c_k^(-1)s(s-1)|d_k|^(s/2)Z_k(s), where c_k>0 is the residue-normalizing constant. Functional equation and endpoint values follow from the quoted standard number-field theory. Those external gamma/measure normalizations are not independently rederived in this audit.

## Branch and zero-product conventions

A logarithm is needed only locally near s=1, where the completion is nonzero. Different local branches differ by a constant2pi i times an integer and therefore give the same lambda_n by the degree argument above. No global logarithm of Xi is assumed before RH is deduced.

Original Eq1.3,p.326 and Eq3.1,p.329 use the genus-zero product with **rho and1-rho paired**. It is not an unordered absolutely convergent product of individual linear factors. A pair satisfies

(1-s/rho)(1-s/(1-rho))=1+s(s-1)/[rho(1-rho)].

For compact s-sets this differs from1 by O(1/|rho|²), apart from finitely many low zeros. The classical order/zero-count input implies summability of these pair bounds. Thus the paired product and its local logarithm converge normally, justifying termwise fixed derivatives. In the Dedekind case the source cites Barner and the classical theory for the product; this audit checks the convergence mechanism assuming that source input.

Likewise the original zero-sum identities Eq1.4,p.326 and Lemma3.1,pp.329–330 are

lambda_n=sum_(paired rho)[1-(1-1/rho)^n],                 (Z)

with multiplicity. The grouped contribution is O_n(1/|rho|²). Individual contributions generally have an O(1/rho) leading term; arbitrary individual reordering is not justified.

There is a subtle convention check. Direct differentiation at s=1 of one linear-factor logarithm yields1-(1-1/rho)^(-n). Reflection rho→1-rho changes w=1-1/rho into w^(-1). Within each fixed pair, plus-n and minus-n grouped sums are identical. Therefore the derivative definition equals(Z) after the legitimate within-pair swap, not by silently asserting equality of a single-zero contribution. The later Bombieri–Lagarias formulation makes this distinction explicit for general multisets.

## Möbius map and generating function

Put phi(z)=Xi(1/(1-z)), analytic on |z|<1 unconditionally, with phi(0)=1. The inverse map is z=1-1/s and

|z|<1 iff Re(s)>1/2.

Using Xi(s)=Xi(1-s) gives phi(z)=Xi(-z/(1-z)). Substituting the paired product yields the source's factors(1-w_rho z)/(1-z), w_rho=1-1/rho. In a sufficiently small disk around0 where phi has no zero,

phi'(z)/phi(z)=sum_(n>=1)lambda_n z^(n-1).               (G)

The source uses a concrete small radius in the zeta case; the argument needs only some positive radius. Normal convergence of grouped terms justifies extracting each fixed coefficient.

Independently, write f(s)=log Xi(s) locally at1, u=z/(1-z), and expand f(1+u). The coefficient of z^n is

sum_(j=1)^n binom(n-1,j-1) f^(j)(1)/j!.

Multiplying byn gives exactly the Leibniz expansion of D^n[s^(n-1)f(s)]/(n-1)!. This verifies the derivative/generating-function normalization without relying on any global zero sum.

The logarithmic derivative is analytic throughout the disk exactly when phi is zero-free there. Any zero of multiplicitym gives a simple pole with residue m; numerator differentiation cannot cancel that logarithmic pole. Disk zero-freeness excludes completed zeros in Re(s)>1/2, and functional symmetry then excludes all off-line zeros.

## Actual original necessity proof: positive Taylor coefficients

**The original proof does not use a finite extremal-root argument.** That is the later Bombieri–Lagarias general-multiset route. Li proves a positive Taylor-coefficient lemma for phi using theta integrals, then a recurrence and coefficient domination.

Write phi(z)=1+sum_(j>=1)a_j z^j. Theorem1's proof shows a_j>0 onpp.326–327, Eqs1.5–1.6 (primary reproduction lines103–212). Here is an independently checked, shorter reconstruction of the same integral mechanism.

Let psi(x)=sum_(n>=1)exp(-pi n²x) and W(x)=[x^(3/2)psi'(x)]'. The source's Eq1.2 can be written

Xi(s)=4integral_1^infinity W(x)[x^((s-1)/2)+x^(-s/2)]dx
     =8integral_1^infinity W(x)x^(-1/4)
          cosh((s-1/2)log x/2)dx.

For x>=1,

W(x)=pi x^(1/2)sum_(n>=1)n²(pi n²x-3/2)exp(-pi n²x)>0.

Termwise differentiation is justified by exponential convergence. With s=1/(1-z), s-1/2=1/2+z/(1-z), a power series with positive constant and nonnegative coefficients. For each x>1, the power series of the displayed cosh therefore has nonnegative coefficients, strictly positive in every positive degree. Its squared-power term alone supplies strict positivity. Integration against positive W provesa_j>0.

All coefficient/integral exchanges hold uniformly on compact |z|<=r<1: the Möbius image stays bounded, derivatives introduce only fixed powers of logx, and W decays exponentially inx. Thus this is a legitimate analytic coefficient argument, not an exchange based only on formal positivity.

For Dedekind zeta, Lemma3.2,pp.330–331, proves the analogous positivity from a positive Hecke-theta integral, using intermediate coefficients b_m and Eq3.7. Its conceptual core is also transparent: write s=1+u, u=z/(1-z); then s(s-1)=z/(1-z)² has nonnegative coefficients. For the integral variable q=|x|>=1, the symmetric factor q^(s/2)+q^((1-s)/2)=2q^(1/4)cosh((s-1/2)logq/2) has nonnegative coefficients. Multiplying and integrating preserves positivity. The validity and normalization of the high-dimensional theta representation itself remains an external antecedent here; the conditional coefficient implication is checked.

## Central self-contained analytic lemma and its proof

Let phi be analytic on the unit disk, phi(0)=1, and phi(z)=sum_(n>=0)a_n z^n with a_0=1 and all a_n>=0. Suppose its local logarithmic derivative has real coefficients lambda_n>=0 for **every** n>=1. Then phi has no zero in the unit disk.

Proof. The local identity phi'=phi L gives, for eachn,

n a_n=lambda_n+sum_(j=1)^(n-1)lambda_j a_(n-j).

All terms in the sum are nonnegative, hence0<=lambda_n<=n a_n. For every r<1,

sum_(n>=1)|lambda_n z^(n-1)|
 <=sum_(n>=1)n a_n r^(n-1)=phi'(r)<infinity, |z|<=r.

Thus L extends analytically to the full disk. The identity phi'=phi L extends by the identity theorem from a neighborhood of0 to the disk. A zero of phi would give incompatible orders of vanishing on the two sides; equivalently, the analytic ODE with initial value1 has the nonzero solution exp(integral L). This proves the lemma. Strict a_n>0 is stronger than needed.

This is precisely the necessity mechanism atp.328 and repeated atpp.331–332 for Theorem2. No Pringsheim theorem is required. No uncontrolled limit over a growing finite extremal-root set is present in this original argument.

## Forward implication and reality

If all zeros are critical, eachw_rho has modulus1 and its paired partner is the conjugate/inverse. The paired contribution is2-2cos(n theta_rho)>=0. The sum converges by the O_n(|rho|^-2) tail already checked, hence lambda_n>=0 for everyn. The local derivative of a real normalized completion at real1 also verifies that lambda_n is real independently of RH.

The source states nonnegativity. Stronger strict positivity in the zeta case can be deduced from its infinite zero set, but is not needed to change the exact theorem statement.

## Contrast with Bombieri–Lagarias

PAPER-L002's original Theorem1, author manuscriptp.3, assumes a multisetR excluding1 and satisfying sum(1+|Re rho|)/(1+|rho|)²<infinity. It characterizes Re rho<=1/2 by nonnegativity of the real parts of inverse-power sums for every positive integern, and equivalently by subexponential lower bounds with the quantifier for every fixed epsilon>0. Its proof uses a finitely attained maximal transformed-root modulus, remainder control and simultaneous Diophantine approximation.

Its Corollary1,pp.4–5, adds exclusion of0 and reflection/conjugation symmetry, obtaining the familiar critical-line positive-power criterion. This removes Li's dependence on the specific positive theta coefficients. These are mathematically different proof routes with compatible conclusions. The original general-multiset hypotheses must not be retroactively attributed to Li1997, and Li's arithmetic theta lemma must not be assumed for an arbitrary multiset.

This contrast was checked against the actual Bombieri–Lagarias primary text reproduction and the existing rendered-page audit, not solely against the2007 introduction. No new whole-paper reading count for Bombieri–Lagarias is claimed.

## Prior finite-prefix campaign: assumptions checked against the original

The original proof's infinite quantifier is essential. Nonnegative lambda_n only forn<=N gives0<=lambda_n<=n a_n only throughN; it supplies no majorant for the remaining logarithmic-derivative series. The analytic continuation step therefore cannot follow from the finite prefix.

The existing symmetric entire-function countermodel can even preserve **all** Taylor a_j>0, a feature used by the original proof. Its off-line quartet factor, centered atw=s-1/2, is

Q_T(w)=w^4+2(T²-1/16)w²+(T²+1/16)².

For T>=1/4 it has nonnegative coefficients inw. Substituting w=1/2+z/(1-z), and multiplying by the campaign's cosh factor, preserves positive Taylor coefficients after positive normalization. The independently checked finite-prefix construction still places four zeros off-line while retaining any prescribed finite nonnegative Li prefix by choosingT sufficiently large.

This strengthens the generic negative result: positivity of all a_j, plus a finite Li prefix, still does not imply the infinite positivity premise. It is not a counterexample to Li's theorem and is not a zeta/Dedekind example; the model has no established Euler product or the exact arithmetic theta identity. It isolates the missing infinite quantifier inside the original elementary analytic mechanism.

## Audit findings and continuation

- Theorem1's normalization, local branches, paired product/sums, map of the disk, coefficient recurrence, integral positivity, domination and analytic-continuation argument are consistent in the inspected source and independent reconstruction.
- No material issue found in this central proof. Pairing and the all-n quantifier are indispensable.
- The full article includes Dedekind zeta, not only the classical Riemann zeta function. Its high-dimensional integral and external Lang/Weil/Barner inputs have not received a complete independent audit here.
- Publisher PDF access and exhaustive correction-history verification remain incomplete. Degraded primary text supports substantive reading but not a claim that every typeset formula was audited.

Next source tasks: obtain a publisher-quality or author manuscript copy; inspect the Hecke-theta representation in the cited Lang chapter with the exact measure and normalization; read Barner's product input; continue to the arithmetic explicit formula in Bombieri–Lagarias only with its distinct source hypotheses. Keep manifestations of Li1997 as one work.

## Independent review

The advocate independently read the original pp325–328 primary reproduction and reconstructed the necessity argument before comparing this audit. Its kernel expansion uses a different finite coefficient formula and gives the same positivity, domination, analytic ODE and paired-sum conclusions. See audits/adversarial_reviews/li_original_necessity_round2.md. It also confirms that the finite-prefix model retains all positive Taylor a_j. This is scoped mathematical validation, not an audit of every Dedekind antecedent or an arithmetic counterexample.
