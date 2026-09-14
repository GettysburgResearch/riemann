# T-105240 — Lorentz-energy cut for 90% and density one

Claim ID: `T-105240`  
Status: **PROVED CONDITIONAL IMPLICATION; Xi mean-value estimate open**  
Depends on: L-105221; L-105240; L-105241

For each `1<=k<=K`, choose `delta_k>0` and choose `lambda_k>=0` minimizing or
approximately minimizing the line energy of L-105241.  Let
\[
\mathcal Q_k(T)
=
\mathcal E_k(\lambda_k,\delta_k)
+2(\Re O_k(T))_+
+2(-\Re P_k(T))_+.
\]
Then
\[
\boxed{
R_0(T)
\ge
R_K(T)-2\sum_{k=1}^K\mathcal Q_k(T)-K.
}
\tag{1}
\]
If `R_K(T)/N(T)>=p_K-o(1)` and
\[
\limsup_{T\to\infty}
\frac1{N(T)}\sum_{k=1}^K\mathcal Q_k(T)
<\frac{p_K-0.9}{2},
\]
then more than 90% of the zeros lie on the critical line.

If `p_K->1`, the endpoint and multiplicity charges are `o(N)`, and
\[
\sum_{k=1}^{K(T)}\mathcal Q_k(T)=o(N(T)),
\]
then the critical-line proportion tends to one.

The exact remaining input is

```text
LERC105240:
prove a source-qualified bound for the weighted adjacent-derivative
correlations chi_(k,delta), the bottom/side flux, and the negative companion
pole amplitudes in a derivative entry with p_K>0.9.
```

Compared with T-105222, the target now has no arbitrary interpolation field.
Compared with T-105230, its principal bulk term is a positive real integral
and admits the explicit one-parameter regression optimum (L-105241).
`LERC105240` is open; 90%, density one, and RH are not established.
