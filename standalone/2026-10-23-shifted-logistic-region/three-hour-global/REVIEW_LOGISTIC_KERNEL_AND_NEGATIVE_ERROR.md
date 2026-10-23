# Independent review of the kernel factorization and negative correction

Reviewer: global-route agent. The reviewer did not author these two
arguments. This is an agent review, not human certification.

## Kernel factorization

Reviewed ../three-hour-root/LOGISTIC_KERNEL_AUTOCORRELATION.md,
SHA256 26dca6795b0fc64f4030f0c271f3f8fdec43c5a796bdae12647e3afdac26ca43.

The integral in K1 checks by the product-to-sum identity over [-d,d-v].
Its two elementary identities S/(2k)=csc(2theta) and
S cos(theta)/k=csc(theta) give precisely the source's w formula,
including its constant -2 term. At v=0 the resulting integral of g^2
equals the displayed w0 normalization. There is no missing factor of
two in Re W(iy)=|ghat(y)|^2/2, because W is the one-sided transform
of the even autocorrelation.

The positivity and w<=w0 conclusions follow directly. The weak first
derivative of compact g is in L2; its correlation is continuous by
continuity of translations in L2. Thus the second derivative of w_e
is continuous. The finite piecewise elementary formula supplies the
piecewise third derivative. Since the globally C2 function vanishes
outside its support, its first two derivatives vanish at the support
endpoints. Evenness gives w'(0)=0. No outstanding issue was found.

## Negative zero-frequency correction

Reviewed ../three-hour-type/LOGISTIC_NEGATIVE_ARCHIMEDEAN.md,
SHA256 88d8dba1316e61aa3cd67e2bb81a2c04d1ac114985593ecde9082aeae766182f,
and its checker verify_logistic_negative_arch.py,
SHA256 5fa012a255a111546c8bd226111d6b422a9e6f85da8e887194b901317babf2a6.

The inequality for f0-f has the correct sign and follows from the
global Taylor estimate and 0<h<=1. The replacement b<=3 is made
while the tanh integrand is nonnegative, before its cubic lower bound
is used. This order is essential and is respected. The inequality
tanh x>=x-x^3/3 follows from the stated nonnegative derivative.

The Laplace moments give the coefficients .49 and -2*.49^3 in the
two reciprocal-power sums. The negative fourth-power tail is bounded
in the unfavorable direction by the integral from 99, whose exact
value is 1/(6*201^3). The positive error integral has precisely the
resource 175 eta^2[2/b^3+1/(2b^2)]. The rational checker implements
these inequalities without floating-point acceptance. Its net lower
bound exceeds .31 and fails the proposed .32 negative control.
No outstanding issue was found.

These are independent analytic components. This review does not assert
that a modified global detector constant has yet been certified, and
does not alter the earlier R=4.84 scalar certificate.
