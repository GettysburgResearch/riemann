# Coupled-flow continuation target after PR #304

The next mathematical object is the explicit aggregate flow

\[
B_X=\sum_{Y=1}^{X-1}\log\frac{Y+1}{Y}[D(p_Y)-D(p)],
\qquad p(n)=n^{-1/2}.
\]

Its carry image is the complete first boundary. The source norm of that image is linear, but this does not estimate the negative capacity of `B_X` after Pascal-cycle optimization.

A valid continuation must:

1. emit the exact central-edge coefficients of `B_X`;
2. truncate or compress its analytic tail without taking source total variation;
3. use the explicit fundamental-cycle basis of PR #272;
4. prove a quantitative upper bound for
   `inf_z N_omega(B_X+C_eta z)`;
5. replay every carry column and the entropy normalization.

Do not reintroduce the refuted isolated atomic-source estimate.
