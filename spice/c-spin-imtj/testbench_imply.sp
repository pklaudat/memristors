simulator lang=spice

.include "c-spin-imtj/imply/imply.inc"
.include "../cmos/transmission.scs"

.param vcond='0.6'
.param vset='1.2'
.param vlow='0.1u'
.param method=traponly
.param twidth=8n
.param trise=0.01n
* V1 1 0 pwl (0 'vmtj' 'twidth' 'vmtj')
VSET set 0 pwl (0 'vset' 'twidth' 'vset' 'twidth+trise' 0 'twidth*2' 0)
VCOND cond 0 pwl (0 'vcond' 'twidth' 'vcond' 'twidth+trise' 0 'twidth*2' 0)
VDD vdd 0 2.0
* TGATE1 vdd 0 set out_set transmission_gate
* TGATE2 vdd 0 cond out_cond transmission_gate
XIMP cond set IMPLY_IMTJ
* IMP1 out_cond out_set IMPLY_IMTJ

.param pw='20ns' 
.tran STOP='pw' START=1.0e-18 uic relv=100n relvar=100n reltol=100n 