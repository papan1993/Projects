$Testbench for measuring worstcase delay and average energy for DFF

$ transistor model
.include "/home/cad/kits/IBM_CMRF8SF-LM013/IBM_PDK/cmrf8sf/V1.2.0.0LM/HSPICE/models/model013.lib_inc"
.include microprocessorlvs.sp

.global vdd! 

.option post runlvl=5

$  xi A B out nand2
xi  CLK IN0 IN1 IN2 IN3 INST0 INST1 OUT0 OUT1 OUT2 OUT3 microprocessor

vdd vdd! gnd! 1.2v
     
       vCLK CLK gnd! pulse( 0v 1.2v 0ps 10ps 10ps 610pps 1120ps  )
       vIN0 IN0 gnd! pwl( 0ns 0v 2ns 0v 2.01ns 1.2v 2.9ns 1.2v 2.91ns 0v 7.5ns 0v 7.51ns 1.2v 8.46ns 1.2v 8.47ns 0v 15ns 0v)
       vIN1 IN1 gnd! pwl( 0ns 0v 1ns 0v 1.01ns 1.2v 1.75ns 1.2v 1.76ns 0v 2.9ns 0v 2.91ns 1.2v 5.1ns 1.2v 6.2ns 1.2v 6.21ns 0v 7.5ns 0v 7.51ns 1.2v 9.6ns 1.2v 9.61ns 0v 15ns 0v )
       vIN2 IN2 gnd! pwl( 0ns 0v 4ns 0v 4.01ns 0v 5.1ns 0v 5.11ns 0v 6.2ns 0v 6.21ns 1.2v 7.5ns 1.2v 7.51ns 0v 15ns 0v)
       vIN3 IN3 gnd! pwl( 0ns 0v 0.2ns 0v 0.21ns 1.2v 0.65ns 1.2v 0.66ns 0v 1.5ns 0v 1.51ns 0v 4ns 0v 4.01ns 1.2v 5ns 1.2v 5.01ns 0v 7.5ns 0v 7.51ns 0v 8.46ns 0v 8.47ns 0v 15ns 0v   )
       
       vINST0 INST0 gnd! pwl(0ns 1.2v 2.5ns 1.2v 2.9ns 1.2v 2.91ns 0v 7.5ns 0v 7.51ns 1.2v 9.5ns 1.2v 11.7ns 1.2v 11.71ns 0v 15ns 0v)
       vINST1 INST1 gnd! pwl(0ns 1.2v 2.5ns 1.2v 2.9ns 1.2v 2.91ns 0v 5.31ns 0v 5.32ns 1.2v 7.5ns 1.2v 7.51ns 0v 15ns 0v)



$transient analysis
$.tr 100ps 48ns
.tr 0.1ps 15ns
$$$$$$$$$$$$$$ encoder delay
  .measure tran tphl_encoder trig v(CLK) td=0.4ns val=0.6 fall=1 targ v(OUT3) val=0.6 fall=1
  
$$$$$$$$$$$$$$$$$$$  adder delay 
  .measure tran tplh_adder trig v(CLK) td=5.2ns val=0.6 fall=1 targ v(OUT3) val=0.6 rise=1
  .measure tran tphl_adder trig v(CLK) td=5ns val=0.6 fall=1 targ v(OUT1) val=0.6 fall=1

$$$$$$$$$$$$$$$$$$$$$$$$$shifter delay
  .measure tran tphl_shifter trig v(CLK) td=6.2ns val=0.6 fall=1 targ v(OUT3) val=0.6 fall=1
  .measure tran tplh_shifter trig v(CLK) td=7.3ns val=0.6 fall=1 targ v(OUT3) val=0.6 rise=1

$$$$$$$$$$$$$$$ sub delay
  .measure tran tphl_sub trig v(CLK) td=8.6ns val=0.6 fall=1 targ v(OUT3) val=0.6 fall=1
  .measure tran tplh_sub trig v(CLK) td=8.4ns val=0.6 fall=1 targ v(OUT1) val=0.6 rise=1 

$   &.measure tran tplh_encoder trig v(CLK) td=1ns val=0.6v fall=1 targ v(Q) td=1ns val=0.6v rise=1
$   &.measure tran tphl_encoder trig v(CLK)  val=0.6v fall=1 targ v(Q) val=0.6v fall=1
$   &.measure tran tsetup_f trig v(D) val=0.6  fall=1 targ v(CLK) val=0.6 fall=1
$   &.measure tran tsetup_r trig v(D) td =1ns val=0.6  rise=1 targ v(CLK) td=1ns val=0.6 fall=1
$$  .measure tran i_clk avg i(vin1) from=0 to=15n
$   .measure tran i_D avg i(vin2) from=0 to=15n
$   &.measure t_worse param='max(tplh,tphl)'
$   .measure energy_clk param='1.2*iavg*2n'
$   .measure energy_D param='1.2*iavg*2n'
$   .measure edp param='abs((t_worse+tsetup_f)*energy_avg)'

.measure tran iavg avg i(vdd) from=0 to=10.5n

.measure energy_avg param='1.2*iavg*10.5n'

.end


