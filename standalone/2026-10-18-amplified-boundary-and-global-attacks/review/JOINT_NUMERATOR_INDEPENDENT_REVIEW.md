# Independent review of the joint-numerator exponent comparison

**Reviewed file:** native/JOINT_NUMERATOR_CLOSURE.md  
**SHA-256:** aa854ac365a480523bd26295c8a1e17359ba51963711fe86f45fbd02e23a12ce  
**Reviewer:** field-audit agent, independently of the author.  
**Result:** PASS for the specified comparison of bounds.

I read the complete proof and independently checked its identities and
inequalities. This was a mathematical component review; the argument
uses no numerical fitting or finite verification as a premise.

The exact difference

$$
J-K=\frac{P_m-R}{4}+\frac q2|z(m)-z(v)|
$$

has the stated nonnegative sign. It correctly uses the detector count
before comparing the two proposed numerator estimates. The stronger
capacity for equal characters is confined to the explicitly stated
case; a principal target does not remove all fixed ray twists from the
buffered detector family.

For the contour comparison, the physical supply transition and the
crossing $v_c$ are correctly located on $[0,1/2]$ under the displayed
range of $\delta,q,R,\kappa,\mathscr L$. In particular the supply
comparison has lower bound

$$
\frac{\delta}{4}
\left[-\frac13+(6\kappa-1)\mathscr L\right]>0.
$$

The three formulas for $M_R(\vartheta)$ follow from the two affine
pieces of $V_R(v)$. Restoring the conductor and outside-scale costs
gives $hM_R(\vartheta)+(h-l_y)\vartheta$ with the correct signs.
Its minimum on the enlarged algebraic contour range occurs at the
old or Xu–Sang endpoint, as claimed.

The original pointwise dyadic lemma includes the stronger exponent
$\delta\min(v,1-v)$; hence the reduction of the block supremum to
$v\leq1/2$ is valid for these bounds. Xu–Sang Appendix B supplies
the profile and mask conventions in its stated contour range. The
reviewed note explicitly treats the larger displacement interval as
a relaxation for an impossibility comparison, not as a newly licensed
analytic contour assertion.

Finally, each bound is nondecreasing in the count exponent $R$.
Taking the block supremum and contour infimum preserves this property,
so retuning the existing detector cannot improve this comparison
merely by postponing that count optimization. At the short balancing
subdivision the equality $v_c=m$ is an exact consequence of $R=P_m$.

The conclusion is appropriately limited: these proposed combinations
of the available marginal moments produce no stronger exponent. It
does not establish that the arithmetic source itself has no further
signed cancellation, and it does not supply a new zero-free theorem.
