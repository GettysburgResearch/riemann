# Root review of the posterior diagnostic

Status: **EXACT IDENTITY CHECK; no invariant theorem claimed**. Date: 2026-10-30.  
Reviewed source: `GAUSSIAN_POSTERIOR.md`, SHA256 `299bd693064b37a6910060360aefa25852d10b99d7bf95cc6f5f36112d1051d0`.

Direct differentiation of exp(−x²U) reproduces all four derivatives, the posterior covariance rule and the variance expression for minus log-curvature. Substitution into a²p−p'', a²p'−p''' and a²p''−p'''' gives the displayed A, B, C and 4x²B²−AC. The bracket proposed for posterior reweighting changes sign at large U whenever x is nonzero, so treating it as a positive new mixing law would indeed be invalid.

Integration by parts gives the clock update theta+theta'/a², including the boundary atom theta(0)/a² when it is present. Positivity of that signed update is not inferred from positivity of the bilateral density. The Gamma-clock example has tail |x|^(alpha−1) exp(−sqrt(b)|x|); the differentiated logarithmic curvature is positive at large x for 1/2<alpha<1, as claimed.

These calculations are valid diagnostic identities under the stated differentiability and integrability conditions. They do not show that the moment region is invariant or that a positive one-sided clock survives the near-cutoff removals. The note keeps both missing assertions explicit.
