/- Candidate C131 count window; requires patched Formulas and Admission33. -/
import Submissions.arvi_density.Return.CountWindow
import Submissions.arvi_density.Return.Rows.Admission33
set_option autoImplicit false
namespace QRH.ArviDensity.Return
noncomputable section

def returnWindow33 : ReturnCountWindow where
  branch := .C131
  nonold := by decide
  deltaLo := (11 / 25 : ℝ)
  deltaHi := (9 / 20 : ℝ)
  pLo := (49 / 100 : ℝ)
  deltaBounds := by norm_num
  pBounds := by norm_num
  certificate := admission33_all

end
end QRH.ArviDensity.Return
