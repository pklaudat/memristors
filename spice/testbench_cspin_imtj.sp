**********************************************************************************************************
* CSpin - IMTJ
***********************************************************************************************************
* simulator lang=spice
* include "c-spin-imtj/MTJ_model.inc"

* params vmtj=1.0
* **V1 node 0 'vmtj'
* VDD3 vcc 0 vsource type=pwl wave=[0 1u 50n 1u 50.1n vmtj 100n vmtj 100.1n 1u 150n 1u 150.1n -vmtj 200n -vmtj 200.1n 1u]
* XIMTJ vcc 0 MTJ lx=32n ly=96n lz=2.44n Ms0=1210 P0=0.69 alpha=0.0062 Tmp0=358 RA0=5 MA=0 ini=1