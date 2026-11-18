# PAPER-C109 — VGPT-RSI for RH-Adjacent Formal Progress: Boundary Certificates, Verified Finite Lagarias Inequalities, and Explicit Failure Localization

Zhixin Hu, Tao Xu, Xiaodian Sun, Li Jin, Momiao Xiong. [Primary source](https://arxiv.org/abs/2606.15096v1), v1,13June2026. Accessed2026-11-17.

**Audit level0; whole-work read: False.**

31-pagePDF accessed. Read title/abstractpp1–3, Lagariasmethodspp12–18, finite-certificate/results/discussionpp20–26 and referencespp27–28. Relevantstatements compared; boundary-curve derivation not fully read; figuresnotindependentlyaudited; formal code/artifactsnotobtainedorreplayed.

Source reports a Coq/CoqInterval finitecertificate forσ(n)≤H_n+exp(H_n)logH_n for1≤n≤10000, assembledfromtenchunks (pp21–23), and a separate finite boundary-curve certificate. It explicitly leavesglobaltail andextremal-integerreductionunresolved (pp17–18,24).

Limits:

* Formal-check claims are source-reported andnotindependentlyreplayed inthistrack.
* Codefilenamesaregiven but no machine-checkableartifactbundle wasobtained.
* No smoothharmonicprofileconcavity or common-εsupportendpoint theorem identifiedininspectedsections.
* Finiteverificationdoesnotproveglobaltail orRH.
* BoundaryB(x,T) isnotourLagariasenvelopeB(x).

See [source comparison](../audits/lagarias_source_comparison_round2.md). No priority claim is made for the independent concavity campaign.
