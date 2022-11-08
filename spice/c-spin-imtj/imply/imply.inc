simulator lang=spice
.include "../model/MTJ_model.scs"


.subckt IMPLY_IMTJ vcond vset rg='1.8k'
XP vcond bitline MTJ lx='32n' ly='96n' lz='2.44n' Ms0='1210' P0='0.69' alpha='0.0062' Tmp0='358' RA0='5' MA='0' ini='1'
XQ vset bitline MTJ lx='32n' ly='96n' lz='2.44n' Ms0='1210' P0='0.69' alpha='0.0062' Tmp0='358' RA0='5' MA='0' ini='1'
RG bitline 0 resistor r=rg
.ends
