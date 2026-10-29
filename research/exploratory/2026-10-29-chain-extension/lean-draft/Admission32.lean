/- Generated candidate; uncompiled; requires the count-source overlay. -/
import Submissions.arvi_density.Return.Formulas
set_option autoImplicit false
set_option linter.unnecessarySeqFocus false
namespace QRH.ArviDensity.Return
noncomputable section
def admission32_00_coefficients : Fin 1 → Fin 2 → ℝ := ![![(132/7:ℝ), (125/7:ℝ)]]
theorem admission32_00_identity (δ p : ℝ) : admissionGuard .capC δ p 0 =
 Record12518109.Bernstein.bsum 0 1 (5/4:ℝ) admission32_00_coefficients (39/100:ℝ) (3971/10000:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission32_00_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission32_00_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (39/100:ℝ) (3971/10000:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .capC δ p 0 := by
 rw [admission32_00_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission32_00_coefficients]
def admission32_01_coefficients : Fin 1 → Fin 1 → ℝ := ![![(1:ℝ)]]
theorem admission32_01_identity (δ p : ℝ) : admissionGuard .capC δ p 1 =
 Record12518109.Bernstein.bsum 0 0 (1:ℝ) admission32_01_coefficients (39/100:ℝ) (3971/10000:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission32_01_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission32_01_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (39/100:ℝ) (3971/10000:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .capC δ p 1 := by
 rw [admission32_01_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission32_01_coefficients]
def admission32_02_coefficients : Fin 1 → Fin 2 → ℝ := ![![(116000909/17500000:ℝ), (9000101/1400000:ℝ)]]
theorem admission32_02_identity (δ p : ℝ) : admissionGuard .capC δ p 2 =
 Record12518109.Bernstein.bsum 0 1 (9000101/20000000:ℝ) admission32_02_coefficients (39/100:ℝ) (3971/10000:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission32_02_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission32_02_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (39/100:ℝ) (3971/10000:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .capC δ p 2 := by
 rw [admission32_02_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission32_02_coefficients]
def admission32_03_coefficients : Fin 2 → Fin 2 → ℝ := ![![(840125/497:ℝ), (2263475/1491:ℝ)], ![(829972/497:ℝ), (2231525/1491:ℝ)]]
theorem admission32_03_identity (δ p : ℝ) : admissionGuard .capC δ p 3 =
 Record12518109.Bernstein.bsum 1 1 (89261/120000:ℝ) admission32_03_coefficients (39/100:ℝ) (3971/10000:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission32_03_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission32_03_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (39/100:ℝ) (3971/10000:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .capC δ p 3 := by
 rw [admission32_03_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission32_03_coefficients]
def admission32_04_coefficients : Fin 2 → Fin 3 → ℝ := ![![(577165730739/173950000:ℝ), (405603939/69580:ℝ), (351003939/139160:ℝ)], ![(59566069650021/17395000000:ℝ), (20968904121/3479000:ℝ), (18189204121/6958000:ℝ)]]
theorem admission32_04_identity (δ p : ℝ) : admissionGuard .capC δ p 4 =
 Record12518109.Bernstein.bsum 1 2 (351003939/4000000000:ℝ) admission32_04_coefficients (39/100:ℝ) (3971/10000:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission32_04_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission32_04_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (39/100:ℝ) (3971/10000:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .capC δ p 4 := by
 rw [admission32_04_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission32_04_coefficients]
def admission32_05_coefficients : Fin 2 → Fin 3 → ℝ := ![![(14206097639603/4970000000:ℝ), (14682137125003/2485000000:ℝ), (15103582125003/4970000000:ℝ)], ![(93206455624979/34790000000:ℝ), (96732089170021/17395000000:ℝ), (99868604020021/34790000000:ℝ)]]
theorem admission32_05_identity (δ p : ℝ) : admissionGuard .capC δ p 5 =
 Record12518109.Bernstein.bsum 1 2 (93206455624979/1000000000000000:ℝ) admission32_05_coefficients (39/100:ℝ) (3971/10000:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission32_05_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission32_05_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (39/100:ℝ) (3971/10000:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .capC δ p 5 := by
 rw [admission32_05_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission32_05_coefficients]
def admission32_06_coefficients : Fin 2 → Fin 3 → ℝ := ![![(22913092114597/2758350000:ℝ), (394110118667/27583500:ℝ), (887642999/147112:ℝ)], ![(16416831435603931/1930845000000:ℝ), (17682347494901/1206778125:ℝ), (319408314977/51489200:ℝ)]]
theorem admission32_06_identity (δ p : ℝ) : admissionGuard .capC δ p 6 =
 Record12518109.Bernstein.bsum 1 2 (6213500993/29600000000:ℝ) admission32_06_coefficients (39/100:ℝ) (3971/10000:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission32_06_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission32_06_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (39/100:ℝ) (3971/10000:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .capC δ p 6 := by
 rw [admission32_06_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission32_06_coefficients]
def admission32_07_coefficients : Fin 2 → Fin 3 → ℝ := ![![(16518690672791/1043700000:ℝ), (634159071817/20874000:ℝ), (121618364813/8349600:ℝ)], ![(800917658899387/52185000000:ℝ), (15364284718357/521850000:ℝ), (117784321787/8349600:ℝ)]]
theorem admission32_07_identity (δ p : ℝ) : admissionGuard .capC δ p 7 =
 Record12518109.Bernstein.bsum 1 2 (117784321787/240000000000:ℝ) admission32_07_coefficients (39/100:ℝ) (3971/10000:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission32_07_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission32_07_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (39/100:ℝ) (3971/10000:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .capC δ p 7 := by
 rw [admission32_07_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission32_07_coefficients]
def admission32_08_coefficients : Fin 2 → Fin 4 → ℝ := ![![(25261630800169/3652950000:ℝ), (669464971859/36529500:ℝ), (7971990111/487060:ℝ), (361298650/73059:ℝ)], ![(2926008883088041/365295000000:ℝ), (38984422041913/1826475000:ℝ), (931861363379/48706000:ℝ), (1691199163/292236:ℝ)]]
theorem admission32_08_identity (δ p : ℝ) : admissionGuard .capC δ p 8 =
 Record12518109.Bernstein.bsum 1 3 (7225973/600000000:ℝ) admission32_08_coefficients (39/100:ℝ) (3971/10000:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission32_08_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission32_08_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (39/100:ℝ) (3971/10000:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .capC δ p 8 := by
 rw [admission32_08_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission32_08_coefficients]
def admission32_09_coefficients : Fin 2 → Fin 4 → ℝ := ![![(23746408093603973/19482400000000:ℝ), (292790148042288157/58447200000000:ℝ), (115360863422396119/19482400000000:ℝ), (125173697654016119/58447200000000:ℝ)], ![(782911404494627/19482400000000:ℝ), (101580386628961279/58447200000000:ℝ), (56511794512549319/19482400000000:ℝ), (70957450529841119/58447200000000:ℝ)]]
theorem admission32_09_identity (δ p : ℝ) : admissionGuard .capC δ p 9 =
 Record12518109.Bernstein.bsum 1 3 (782911404494627/8000000000000000000:ℝ) admission32_09_coefficients (39/100:ℝ) (3971/10000:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission32_09_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission32_09_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (39/100:ℝ) (3971/10000:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .capC δ p 9 := by
 rw [admission32_09_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission32_09_coefficients]
def admission32_10_coefficients : Fin 3 → Fin 3 → ℝ := ![![(175900568310119/2964108000:ℝ), (138698408473823/1482054000:ℝ), (101846138473823/2964108000:ℝ)], ![(4307753392170911/37051350000:ℝ), (135380717747423/741027000:ℝ), (32927736649141/494018000:ℝ)], ![(210623763418128577/3705135000000:ℝ), (131864595083177/1482054000:ℝ), (95543339266177/2964108000:ℝ)]]
theorem admission32_10_identity (δ p : ℝ) : admissionGuard .capC δ p 10 =
 Record12518109.Bernstein.bsum 2 2 (95543339266177/12000000000000000:ℝ) admission32_10_coefficients (39/100:ℝ) (3971/10000:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission32_10_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission32_10_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (39/100:ℝ) (3971/10000:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .capC δ p 10 := by
 rw [admission32_10_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission32_10_coefficients]
def admission32_11_coefficients : Fin 2 → Fin 3 → ℝ := ![![(5239839373053/347900000:ℝ), (602172772441/20874000:ℝ), (192334438271/13916000:ℝ)], ![(254923844432871/17395000000:ℝ), (3658623921787/130462500:ℝ), (186796423929/13916000:ℝ)]]
theorem admission32_11_identity (δ p : ℝ) : admissionGuard .capC δ p 11 =
 Record12518109.Bernstein.bsum 1 2 (186796423929/400000000000:ℝ) admission32_11_coefficients (39/100:ℝ) (3971/10000:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission32_11_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission32_11_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (39/100:ℝ) (3971/10000:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .capC δ p 11 := by
 rw [admission32_11_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission32_11_coefficients]
def admission32_12_coefficients : Fin 1 → Fin 1 → ℝ := ![![(74999/20000000:ℝ)]]
theorem admission32_12_identity (δ p : ℝ) : admissionGuard .capC δ p 12 =
 Record12518109.Bernstein.bsum 0 0 (74999/20000000:ℝ) admission32_12_coefficients (39/100:ℝ) (3971/10000:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission32_12_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission32_12_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (39/100:ℝ) (3971/10000:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .capC δ p 12 := by
 rw [admission32_12_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission32_12_coefficients]
def admission32_13_coefficients : Fin 1 → Fin 1 → ℝ := ![![(790659947/40000000000:ℝ)]]
theorem admission32_13_identity (δ p : ℝ) : admissionGuard .capC δ p 13 =
 Record12518109.Bernstein.bsum 0 0 (790659947/40000000000:ℝ) admission32_13_coefficients (39/100:ℝ) (3971/10000:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission32_13_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission32_13_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (39/100:ℝ) (3971/10000:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .capC δ p 13 := by
 rw [admission32_13_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission32_13_coefficients]
def admission32_14_coefficients : Fin 2 → Fin 3 → ℝ := ![![(4642822725809/1043700000:ℝ), (57271603493/6958000:ℝ), (31684032511/8349600:ℝ)], ![(229401748466563/52185000000:ℝ), (88333076733/10871875:ℝ), (31236797689/8349600:ℝ)]]
theorem admission32_14_identity (δ p : ℝ) : admissionGuard .capC δ p 14 =
 Record12518109.Bernstein.bsum 1 2 (31236797689/240000000000:ℝ) admission32_14_coefficients (39/100:ℝ) (3971/10000:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission32_14_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission32_14_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (39/100:ℝ) (3971/10000:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .capC δ p 14 := by
 rw [admission32_14_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission32_14_coefficients]
theorem admission32_all {δ p : ℝ} (hδ : δ ∈ Set.Icc (39/100:ℝ) (3971/10000:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) (j : Fin 15) : 0 < admissionGuard .capC δ p j := by
 fin_cases j
 · exact admission32_00_pos hδ hp
 · exact admission32_01_pos hδ hp
 · exact admission32_02_pos hδ hp
 · exact admission32_03_pos hδ hp
 · exact admission32_04_pos hδ hp
 · exact admission32_05_pos hδ hp
 · exact admission32_06_pos hδ hp
 · exact admission32_07_pos hδ hp
 · exact admission32_08_pos hδ hp
 · exact admission32_09_pos hδ hp
 · exact admission32_10_pos hδ hp
 · exact admission32_11_pos hδ hp
 · exact admission32_12_pos hδ hp
 · exact admission32_13_pos hδ hp
 · exact admission32_14_pos hδ hp
end
end QRH.ArviDensity.Return
