# L-91370 — First activation-strip domination

Status: **proved exact local lemma; RH unproved**

For `j>=7`, define

\[
R_j(v)=j^{3/2}Q_{jv}(j),
\qquad q(v)=8\sqrt v-7-\frac32\log v.
\]

On `1<=v<1+1/j`, only the `m=j` source is active, so

\[
R_j(v)=\frac{j(j+1)}{j-1}\log v>=0.
\]

Also

\[
q'(v)=4v^{-1/2}-\frac32v^{-1},
\qquad q''(v)<0.
\]

For `j>=7`, the strip is contained in `[1,8/7]`. The exact comparison

\[
\frac78>\left(\frac{297}{320}\right)^2
\]

implies

\[
q'(v)>=q'(8/7)>\frac{12}{5}.
\]

Hence

\[
q(v)>1+\frac{12}{5}(v-1).
\]

Using `log v<=v-1` and `v-1<=1/j`,

\[
\begin{aligned}
q(v)-R_j(v)
&>1-\left[\frac{j(j+1)}{j-1}-\frac{12}{5}\right]\frac1j\\
&=\frac{2(j-6)}{5j(j-1)}>0.
\end{aligned}
\]

Therefore

\[
\boxed{0<=R_j(v)<q(v)}
\]

throughout the first activation strip.

This closes the implicit one-sided step in the large-row proof of `L-91364`: a negative-parity divisor in the first strip is automatically safe when `R_j` is replaced by `q`; only positive-parity divisors require the explicit activation-loss term already certified there.
