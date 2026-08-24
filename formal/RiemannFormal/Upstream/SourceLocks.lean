namespace RiemannFormal.Upstream

def bootstrapMergeCommit : String :=
  "573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f"

def mathlibCommit : String :=
  "51e6992efd06126df61a496bebf8f49482a4e129"

def zeta23AuditedCommit : String :=
  "3635e74826a4c1fcece7d1cd2b6fa75e43a00510"

def zeta23SelectedCommit : String :=
  "cec57f919ccf34e5fa5372b4ba332f7c848bbb6e"

def scientificSourceCommit : String :=
  "852d8aa05c701ea7818ce8a50543e68987fef5cc"

def sourceFiveThreeCommit : String :=
  "433fd3662f7b2e4ba384ce64f196380e88624090"

def sourceTwoRowCommit : String :=
  "24ab64551225f2dba9aa53a533eb9b0285c6e363"

def sourceLandauConsumerCommit : String :=
  "e928fd615d753882706bb88c51b717bd8d4a86ba"

def sourceHolomorphicDefectCommit : String :=
  "3f9e80f09fe1f595927ea7dce6fb49ac68c5c21b"

/-- Exact scientific provenance consumed by `scripts/verify_source_locks.py`. -/
structure ScientificClaimLock where
  semanticId : String
  sourcePR : Nat
  sourceSHA : String
  sourcePath : String
  sourceClaimId : String
  leanDeclarations : List String
  deriving Repr

/-- Exact imported declaration provenance consumed by `scripts/verify_source_locks.py`. -/
structure UpstreamDeclarationLock where
  project : String
  commit : String
  sourcePath : String
  declarations : List String
  deriving Repr

def analysisScientificClaimLocks : List ScientificClaimLock :=
  [
    {
      semanticId := "CONSUMER.MELLIN.FIXED_ROW"
      sourcePR := 652
      sourceSHA := sourceTwoRowCommit
      sourcePath := "claims/lemmas/L-99602-exact-two-row-mellin-landau-consumer.md"
      sourceClaimId := "L-99602"
      leanDeclarations := [
        "RiemannFormal.Analysis.FixedDetectorMellinIdentity",
        "RiemannFormal.Analysis.FixedDetectorReciprocalZetaIdentity"
      ]
    },
    {
      semanticId := "CONSUMER.MELLIN.ZERO_SAFE_BOX"
      sourcePR := 653
      sourceSHA := sourceLandauConsumerCommit
      sourcePath := "claims/lemmas/L-99270-zero-free-smoothing-and-negative-mass.md"
      sourceClaimId := "L-99270"
      leanDeclarations := [
        "RiemannFormal.Analysis.logBoxMultiplier",
        "RiemannFormal.Analysis.logBoxMultiplier_nonzero"
      ]
    },
    {
      semanticId := "CONSUMER.MELLIN.SPECIALIZED_LANDAU"
      sourcePR := 653
      sourceSHA := sourceLandauConsumerCommit
      sourcePath := "claims/lemmas/L-99272-specialized-landau-and-scalar-firewall.md"
      sourceClaimId := "L-99272"
      leanDeclarations := [
        "RiemannFormal.Analysis.MellinLandauBoundarySingularity",
        "RiemannFormal.Analysis.nonnegative_landau_boundary"
      ]
    },
    {
      semanticId := "CONSUMER.MELLIN.HOLOMORPHIC_DEFECT"
      sourcePR := 650
      sourceSHA := sourceHolomorphicDefectCommit
      sourcePath := "claims/lemmas/L-99282-holomorphic-perturbation-landau-transfer.md"
      sourceClaimId := "L-99282"
      leanDeclarations := [
        "RiemannFormal.Analysis.fixed_holomorphic_defect_transfer",
        "RiemannFormal.Analysis.fixed_mellin_singularity_transfer"
      ]
    },
    {
      semanticId := "API.MELLIN.SUBPOWER_NEGATIVE_MASS"
      sourcePR := 653
      sourceSHA := sourceLandauConsumerCommit
      sourcePath := "claims/lemmas/L-99270-zero-free-smoothing-and-negative-mass.md"
      sourceClaimId := "L-99270"
      leanDeclarations := [
        "RiemannFormal.Analysis.SubpowerNegativeMassHolomorphy",
        "RiemannFormal.Analysis.fixedDetector_negativeMass_implies_RH"
      ]
    },
    {
      semanticId := "API.MELLIN.SUBPOWER_NEGATIVE_MASS"
      sourcePR := 653
      sourceSHA := sourceLandauConsumerCommit
      sourcePath := "claims/lemmas/L-99272-specialized-landau-and-scalar-firewall.md"
      sourceClaimId := "L-99272"
      leanDeclarations := [
        "RiemannFormal.Analysis.fixedDetector_negativeMass_implies_RH"
      ]
    }
  ]

def analysisUpstreamDeclarationLocks : List UpstreamDeclarationLock :=
  [
    {
      project := "mathlib"
      commit := mathlibCommit
      sourcePath := "Mathlib/NumberTheory/LSeries/RiemannZeta.lean"
      declarations := [
        "RiemannHypothesis",
        "riemannZeta",
        "completedRiemannZeta",
        "completedRiemannZeta₀",
        "differentiableAt_riemannZeta"
      ]
    },
    {
      project := "mathlib"
      commit := mathlibCommit
      sourcePath := "Mathlib/Analysis/MellinTransform.lean"
      declarations := [
        "mellin",
        "MellinConvergent",
        "mellin_comp_mul_left",
        "mellin_differentiableAt_of_isBigO_rpow"
      ]
    },
    {
      project := "mathlib"
      commit := mathlibCommit
      sourcePath := "Mathlib/Analysis/Meromorphic/Order.lean"
      declarations := [
        "meromorphicOrderAt",
        "AnalyticAt.meromorphicOrderAt_eq",
        "meromorphicOrderAt_inv"
      ]
    },
    {
      project := "zeta23"
      commit := zeta23SelectedCommit
      sourcePath := "Zeta23/Statement.lean"
      declarations := [
        "Zeta23.IsNontrivialZero",
        "Zeta23.zeroMult",
        "Zeta23.RH_implies_on_line"
      ]
    },
    {
      project := "zeta23"
      commit := zeta23SelectedCommit
      sourcePath := "Zeta23/ZetaReflect.lean"
      declarations := [
        "Zeta23.zeta_reflect_zero",
        "Zeta23.zeta_mult_reflect"
      ]
    }
  ]

end RiemannFormal.Upstream
