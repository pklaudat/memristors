**********************************************************************************************************
* C-Spin - PMTJ
***********************************************************************************************************
simulator lang=spice
.include "model/MTJ_model.inc"

.option post
.save

.param vmtj='0.4'
V1 1 0 pwl (0 'vmtj' 5n 'vmtj' 6n 0 10n 0 11n '-vmtj' 15n '-vmtj' 16n 0)
* V1 1 0 pwl (0 'vmtj' 10n 'vmtj' 11n 0 20n 0 21n '-vmtj' 30n '-vmtj' 31n 0)
XMTJ1 1 0 MTJ lx='65n' ly='65n' lz='1.48n' Ms0='1210' P0='0.69' alpha='0.006' Tmp0='358' RA0='5' MA='1' ini='1' tc='1.5n'

.param pw='40ns' 
.tran 1p 'pw' START=1.0e-18  uic sweep vmtj 0.0 1 0.2

.meas tsw0 when v(XMTJ1.XLLG.Mz)='0'
.meas iwr find i(XMTJ1.ve1) at 1ns
.meas thermal_stability find v(XMTJ1.XLLG.thste) at 1ns


.end