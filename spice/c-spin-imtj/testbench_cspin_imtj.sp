**********************************************************************************************************
* CSpin - IMTJ
***********************************************************************************************************
************************************************************************************
** This run file simulates the dynamic motion of  MTJ.
** # Instruction for simulation
** 1. Set the MTJ dimensions and material parameters.
** 2. Select anisotropy(IMA/PMA) and initial state of free layer(P/AP).
** 3. Adjust bias voltage for Read/Write operation.
** ex. APtoP switching: positive voltage @ ini='1'
**     PtoAP switching: negative voltage @ ini='0'  
************************************************************************************
** # Description of parameters
** lx,ly,lz: width, length, and thickness of free layer
** tox: MgO thickness
** Ms0:saturation magnetizaion at 0K
** P0: polarization factor at 0K 
** alpha: damping factor
** temp: temperature
** MA: magnetic anisotropy (MA=0:In-plane,MA=1:Perpendicular)
**     also sets magnetization in pinned layer, MA=0:[0,1,0],MA=1:[0,0,1]
** ini: initial state of free layer (ini=0:Parallel,ini=1:Anti-parallel)
************************************************************************************
simulator lang=spice
.include "model/MTJ_model.inc"
.method=traponly

*** Options ************************************************************************
.option post
.save

*** Voltage biasing to MTJ *********************************************************
.param vmtj='1.0'
.param twidth=10n
.param trise=1n
* V1 1 0 'vmtj'
V1 1 0 pwl (0 'vmtj' 'twidth' 'vmtj' 'twidth+trise' 0 'twidth*2' 0 'twidth*2+trise' '-vmtj' 'twidth*3' '-vmtj' 'twidth*3+trise' 0)
XMTJ1 1 0 MTJ lx='32n' ly='96n' lz='2.44n' Ms0='1210' P0='0.69' alpha='0.0062' Tmp0='358' RA0='5' MA='0' ini='1'

*** Analysis ***********************************************************************
.param pw='10ns' 
.tran 100p 'pw' START=1.0e-18  uic relv=1f relvar=1f $sweep vmtj 0.3 0.7 0.1

.meas tsw0 when v(XMTJ1.XLLG.My)='0'
.meas iwr find i(XMTJ1.ve1) at 1ns
.meas thermal_stability find v(XMTJ1.XLLG.thste) at 1ns

.end



* params vmtj=1.0
* **V1 node 0 'vmtj'
* VDD3 vcc 0 vsource type=pwl wave=[0 1u 50n 1u 50.1n vmtj 100n vmtj 100.1n 1u 150n 1u 150.1n -vmtj 200n -vmtj 200.1n 1u]
* XIMTJ vcc 0 MTJ lx=32n ly=96n lz=2.44n Ms0=1210 P0=0.69 alpha=0.0062 Tmp0=358 RA0=5 MA=0 ini=1