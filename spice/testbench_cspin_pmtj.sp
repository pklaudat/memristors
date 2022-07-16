**********************************************************************************************************
* C-Spin - PMTJ
***********************************************************************************************************
simulator lang=spice
.include "c-spin-pmtj/MTJ_model.inc"
.param vmtj='1.0'
V1 1 0 pwl (0 'vmtj' 5n 'vmtj' 6n 0 10n 0 11n '-vmtj' 15n '-vmtj' 16n 0)
PMTJ 1 0 MTJ lx='65n' ly='65n' lz='1.48n' Ms0='1210' P0='0.69' alpha='0.006' Tmp0='358' RA0='5' MA='1' ini='1' tc='1.5n'

.param pw='20ns' 
.tran 1p 'pw' START=1.0e-18  uic $ sweep vmtj 0.4 0.5 0.01