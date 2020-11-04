*
*
*
*                       LINUX           Mon Apr 27 23:41:43 2020
*
*
*
*  PROGRAM  advgen
*
*  Name           : advgen - QRC - (64-bit)
*  Version        : 9.1.3-p005
*  Build Date     : Tue Aug  3 12:36:00 PDT 2010
*
*  HSPICE LIBRARY
*
*
*
.GLOBAL gnd! vdd!
*

.SUBCKT microprocessor CLK IN0 IN1 IN2 IN3 INST0 INST1 OUT0 OUT1 OUT2 OUT3
*
*
*  caps2d version: 10
*
*
*       TRANSISTOR CARDS
*
*
MI1/I8/T5	net40	I1/I8/net11	I1/net35	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I9/T5	net41	I1/I9/net11	I1/net19	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I10/T5	net48	I1/I10/net11	I1/net16	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I11/T5	net39	I1/I11/net11	I1/net3	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I8/T3	I1/net13	S0	net40	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I9/T3	I1/net10	S0	net41	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I10/T3	I1/net7	S0	net48	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I11/T3	I1/net14	S0	net39	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I0/T5	net50	I25/I0/net11	OUT0	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I1/T5	net46	I25/I1/net11	OUT1	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I0/T3	gnd!	IN0	net50	gnd!	nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I1/T3	gnd!	I25/net21	net46	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I8/I3/T0	I1/I8/net11	S0	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I9/I3/T0	I1/I9/net11	S0	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I10/I3/T0	I1/I10/net11	S0	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I11/I3/T0	I1/I11/net11	S0	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I5/T0	I25/net21	I25/I5/net11	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I4/T5	I1/net13	I1/I4/net11	I1/net19	gnd!	nfet
+ L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I5/T5	I1/net10	I1/I5/net11	I1/net16	gnd!	nfet
+ L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I6/T5	I1/net7	I1/I6/net11	I1/net3	gnd!	nfet
+ L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I7/T5	I1/net14	I1/I7/net11	I1/net35	gnd!	nfet
+ L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I4/T3	I1/net3	net27	I1/net13	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I5/T3	I1/net35	net27	I1/net10	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I6/T3	I1/net19	net27	I1/net7	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I7/T3	I1/net16	net27	I1/net14	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I0/I3/T0	I25/I0/net11	IN0	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I1/I3/T0	I25/I1/net11	I25/net21	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I5/T7	gnd!	IN1	I25/I5/net11	gnd!	nfet	L=0.24U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I4/I3/T0	I1/I4/net11	net27	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I5/I3/T0	I1/I5/net11	net27	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I6/I3/T0	I1/I6/net11	net27	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I7/I3/T0	I1/I7/net11	net27	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I5/T4	I25/I5/net11	IN0	gnd!	gnd!	nfet	L=0.24U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I0/T5	I1/net35	I1/I0/net11	OUT0	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I1/T5	I1/net19	I1/I1/net11	OUT1	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I2/T5	I1/net16	I1/I2/net11	OUT2	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I3/T5	I1/net3	I1/I3/net11	OUT3	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I0/T3	OUT2	S1	I1/net35	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I1/T3	OUT3	S1	I1/net19	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I2/T3	OUT0	S1	I1/net16	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I3/T3	OUT1	S1	I1/net3	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I0/I3/T0	I1/I0/net11	S1	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I1/I3/T0	I1/I1/net11	S1	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I2/I3/T0	I1/I2/net11	S1	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I3/I3/T0	I1/I3/net11	S1	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI19/I3/T0	I19/net11	net27	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI18/I3/T0	I18/net11	net27	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI39/T0	gnd!	I39/net11	net27	gnd!	nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI39/T4	gnd!	IN2	I39/net11	gnd!	nfet	L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI19/T5	S0	I19/net11	IN1	gnd!	nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI18/T5	S1	I18/net11	IN0	gnd!	nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI39/T7	I39/net11	IN3	gnd!	gnd!	nfet	L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI19/T3	IN2	net27	S0	gnd!	nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI18/T3	IN3	net27	S1	gnd!	nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI10/T7	I10/net023	I10/net14	gnd!	gnd!	nfet	L=0.12U
+ W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI12/T7	I12/net023	I12/net14	gnd!	gnd!	nfet	L=0.12U
+ W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI10/T11	I10/net10	I10/CLKN	I10/net023	gnd!	nfet
+ L=0.48U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI12/T11	I12/net10	I12/CLKN	I12/net023	gnd!	nfet
+ L=0.48U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI10/T8	OUT1	I10/net023	gnd!	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI12/T8	OUT3	I12/net023	gnd!	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI10/T0	I10/net33	net59	gnd!	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI12/T0	I12/net33	net60	gnd!	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI10/T3	I10/net10	CLK	I10/net33	gnd!	nfet	L=0.12U
+ W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI12/T3	I12/net10	CLK	I12/net33	gnd!	nfet	L=0.12U
+ W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI10/T5	I10/net30	I10/net10	gnd!	gnd!	nfet	L=0.12U
+ W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI12/T5	I12/net30	I12/net10	gnd!	gnd!	nfet	L=0.12U
+ W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI10/T12	I10/net14	I10/CLKN	I10/net30	gnd!	nfet
+ L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI12/T12	I12/net14	I12/CLKN	I12/net30	gnd!	nfet
+ L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I2/T5	net45	I25/I2/net11	OUT2	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I3/T5	net44	I25/I3/net11	OUT3	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I2/T3	gnd!	I25/net22	net45	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I3/T3	gnd!	I25/net23	net44	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI10/T4	I10/CLKN	CLK	gnd!	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI12/T4	I12/CLKN	CLK	gnd!	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I6/T4	I25/I6/net11	IN0	gnd!	gnd!	nfet	L=0.24U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I7/T4	I25/I7/net11	IN0	gnd!	gnd!	nfet	L=0.24U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI9/T11	I9/net10	I9/CLKN	I9/net023	gnd!	nfet	L=0.48U
+ W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI31/T11	I31/net10	I31/CLKN	I31/net023	gnd!	nfet
+ L=0.48U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I6/T0	I25/net22	I25/I6/net11	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I7/T0	I25/net23	I25/I7/net11	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI9/T8	OUT0	I9/net023	gnd!	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI31/T8	OUT2	I31/net023	gnd!	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I2/I3/T0	I25/I2/net11	I25/net22	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I3/I3/T0	I25/I3/net11	I25/net23	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI9/T5	I9/net30	I9/net10	gnd!	gnd!	nfet	L=0.12U
+ W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI31/T5	I31/net30	I31/net10	gnd!	gnd!	nfet	L=0.12U
+ W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI9/T12	I9/net14	I9/CLKN	I9/net30	gnd!	nfet	L=0.12U
+ W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI31/T12	I31/net14	I31/CLKN	I31/net30	gnd!	nfet
+ L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI9/T7	I9/net023	I9/net14	gnd!	gnd!	nfet	L=0.12U
+ W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI31/T7	I31/net023	I31/net14	gnd!	gnd!	nfet	L=0.12U
+ W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I6/T7	gnd!	IN2	I25/I6/net11	gnd!	nfet	L=0.24U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I7/T7	gnd!	IN3	I25/I7/net11	gnd!	nfet	L=0.24U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI9/T4	I9/CLKN	CLK	gnd!	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI31/T4	I31/CLKN	CLK	gnd!	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI9/T0	I9/net33	net61	gnd!	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI31/T0	I31/net33	net58	gnd!	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI9/T3	I9/net10	CLK	I9/net33	gnd!	nfet	L=0.12U
+ W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI31/T3	I31/net10	CLK	I31/net33	gnd!	nfet	L=0.12U
+ W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI15/I0/I3/T0	I15/I0/net11	INST0	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI15/I1/I3/T0	I15/I1/net11	INST0	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI15/I2/I3/T0	I15/I2/net11	INST1	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI15/I0/T5	I15/net17	I15/I0/net11	net42	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI15/I1/T5	I15/net16	I15/I1/net11	net39	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI15/I2/T5	net60	I15/I2/net11	I15/net17	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI15/I0/T3	net42	INST0	I15/net17	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI15/I1/T3	net44	INST0	I15/net16	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI15/I2/T3	I15/net16	INST1	net60	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI14/I0/T3	net43	INST0	I14/net17	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI14/I1/T3	net45	INST0	I14/net16	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI14/I2/T3	I14/net16	INST1	net58	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I3/T0	I24/net9	I24/I8/I3/net11	gnd!	gnd!	nfet
+ L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I3/T0	I24/net10	I24/I1/I3/net11	gnd!	gnd!	nfet
+ L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I3/T0	I24/net11	I24/I2/I3/net11	gnd!	gnd!	nfet
+ L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I3/T0	net046	I24/I3/I3/net11	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI14/I0/T5	I14/net17	I14/I0/net11	net43	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI14/I1/T5	I14/net16	I14/I1/net11	net48	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI14/I2/T5	net58	I14/I2/net11	I14/net17	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I3/T7	gnd!	I24/I8/net9	I24/I8/I3/net11	gnd!	nfet
+ L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I3/T7	gnd!	I24/I1/net9	I24/I1/I3/net11	gnd!	nfet
+ L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I3/T7	gnd!	I24/I2/net9	I24/I2/I3/net11	gnd!	nfet
+ L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I3/T7	gnd!	I24/I3/net9	I24/I3/I3/net11	gnd!	nfet
+ L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I3/T4	I24/I8/I3/net11	I24/I8/net7	gnd!	gnd!	nfet
+ L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I3/T4	I24/I1/I3/net11	I24/I1/net7	gnd!	gnd!	nfet
+ L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I3/T4	I24/I2/I3/net11	I24/I2/net7	gnd!	gnd!	nfet
+ L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I3/T4	I24/I3/I3/net11	I24/I3/net7	gnd!	gnd!	nfet
+ L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I5/I3/T5	I24/I8/net10	I24/I8/I5/I3/net09	gnd!	gnd!
+ nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I6/I3/T5	net47	I24/I8/I6/I3/net09	gnd!	gnd!	nfet
+ L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I5/I3/T5	I24/I1/net10	I24/I1/I5/I3/net09	gnd!	gnd!
+ nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I6/I3/T5	net49	I24/I1/I6/I3/net09	gnd!	gnd!	nfet
+ L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I5/I3/T5	I24/I2/net10	I24/I2/I5/I3/net09	gnd!	gnd!
+ nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I6/I3/T5	net43	I24/I2/I6/I3/net09	gnd!	gnd!	nfet
+ L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I5/I3/T5	I24/I3/net10	I24/I3/I5/I3/net09	gnd!	gnd!
+ nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I6/I3/T5	net42	I24/I3/I6/I3/net09	gnd!	gnd!	nfet
+ L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI14/I0/I3/T0	I14/I0/net11	INST0	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI14/I1/I3/T0	I14/I1/net11	INST0	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI14/I2/I3/T0	I14/I2/net11	INST1	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I5/I3/T2	I24/I8/I5/I3/net09	I24/I8/I5/net13
+ I24/I8/I5/I3/net15	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I6/I3/T2	I24/I8/I6/I3/net09	I24/I8/I6/net13
+ I24/I8/I6/I3/net15	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I5/I3/T2	I24/I1/I5/I3/net09	I24/I1/I5/net13
+ I24/I1/I5/I3/net15	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I6/I3/T2	I24/I1/I6/I3/net09	I24/I1/I6/net13
+ I24/I1/I6/I3/net15	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I5/I3/T2	I24/I2/I5/I3/net09	I24/I2/I5/net13
+ I24/I2/I5/I3/net15	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I6/I3/T2	I24/I2/I6/I3/net09	I24/I2/I6/net13
+ I24/I2/I6/I3/net15	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I5/I3/T2	I24/I3/I5/I3/net09	I24/I3/I5/net13
+ I24/I3/I5/I3/net15	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I6/I3/T2	I24/I3/I6/I3/net09	I24/I3/I6/net13
+ I24/I3/I6/I3/net15	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I5/I3/T3	I24/I8/I5/I3/net15	I24/I8/I5/net12	gnd!
+ gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I6/I3/T3	I24/I8/I6/I3/net15	I24/I8/I6/net12	gnd!
+ gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I5/I3/T3	I24/I1/I5/I3/net15	I24/I1/I5/net12	gnd!
+ gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I6/I3/T3	I24/I1/I6/I3/net15	I24/I1/I6/net12	gnd!
+ gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I5/I3/T3	I24/I2/I5/I3/net15	I24/I2/I5/net12	gnd!
+ gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I6/I3/T3	I24/I2/I6/I3/net15	I24/I2/I6/net12	gnd!
+ gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I5/I3/T3	I24/I3/I5/I3/net15	I24/I3/I5/net12	gnd!
+ gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I6/I3/T3	I24/I3/I6/I3/net15	I24/I3/I6/net12	gnd!
+ gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I5/I1/T0	I24/I8/I5/net12	I24/I8/I5/I1/net11	gnd!
+ gnd!	nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I6/I1/T0	I24/I8/I6/net12	I24/I8/I6/I1/net11	gnd!
+ gnd!	nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I5/I1/T0	I24/I1/I5/net12	I24/I1/I5/I1/net11	gnd!
+ gnd!	nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I6/I1/T0	I24/I1/I6/net12	I24/I1/I6/I1/net11	gnd!
+ gnd!	nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I5/I1/T0	I24/I2/I5/net12	I24/I2/I5/I1/net11	gnd!
+ gnd!	nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I6/I1/T0	I24/I2/I6/net12	I24/I2/I6/I1/net11	gnd!
+ gnd!	nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I5/I1/T0	I24/I3/I5/net12	I24/I3/I5/I1/net11	gnd!
+ gnd!	nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I6/I1/T0	I24/I3/I6/net12	I24/I3/I6/I1/net11	gnd!
+ gnd!	nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I5/I1/T4	I24/I8/I5/I1/net11	I24/net12	gnd!	gnd!
+ nfet	L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I6/I1/T4	I24/I8/I6/I1/net11	I24/I8/net10	gnd!	gnd!
+ nfet	L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I5/I1/T4	I24/I1/I5/I1/net11	I24/net16	gnd!	gnd!
+ nfet	L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I6/I1/T4	I24/I1/I6/I1/net11	I24/I1/net10	gnd!	gnd!
+ nfet	L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I5/I1/T4	I24/I2/I5/I1/net11	I24/net15	gnd!	gnd!
+ nfet	L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I6/I1/T4	I24/I2/I6/I1/net11	I24/I2/net10	gnd!	gnd!
+ nfet	L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I5/I1/T4	I24/I3/I5/I1/net11	I24/net13	gnd!	gnd!
+ nfet	L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I6/I1/T4	I24/I3/I6/I1/net11	I24/I3/net10	gnd!	gnd!
+ nfet	L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I5/I1/T7	gnd!	IN0	I24/I8/I5/I1/net11	gnd!	nfet
+ L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I6/I1/T7	gnd!	I24/Y	I24/I8/I6/I1/net11	gnd!	nfet
+ L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I5/I1/T7	gnd!	IN1	I24/I1/I5/I1/net11	gnd!	nfet
+ L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I6/I1/T7	gnd!	I24/net9	I24/I1/I6/I1/net11	gnd!
+ nfet	L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I5/I1/T7	gnd!	IN2	I24/I2/I5/I1/net11	gnd!	nfet
+ L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I6/I1/T7	gnd!	I24/net10	I24/I2/I6/I1/net11	gnd!
+ nfet	L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I5/I1/T7	gnd!	IN3	I24/I3/I5/I1/net11	gnd!	nfet
+ L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I6/I1/T7	gnd!	I24/net11	I24/I3/I6/I1/net11	gnd!
+ nfet	L=0.24U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI13/I0/T3	net49	INST0	I13/net17	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI13/I1/T3	net46	INST0	I13/net16	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI13/I2/T3	I13/net16	INST1	net59	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I5/I2/T0	I24/I8/I5/net13	I24/I8/net7	gnd!	gnd!
+ nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I6/I2/T0	I24/I8/I6/net13	I24/I8/net9	gnd!	gnd!
+ nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I5/I2/T0	I24/I1/I5/net13	I24/I1/net7	gnd!	gnd!
+ nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I6/I2/T0	I24/I1/I6/net13	I24/I1/net9	gnd!	gnd!
+ nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I5/I2/T0	I24/I2/I5/net13	I24/I2/net7	gnd!	gnd!
+ nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I6/I2/T0	I24/I2/I6/net13	I24/I2/net9	gnd!	gnd!
+ nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I5/I2/T0	I24/I3/I5/net13	I24/I3/net7	gnd!	gnd!
+ nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I6/I2/T0	I24/I3/I6/net13	I24/I3/net9	gnd!	gnd!
+ nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI13/I0/T5	I13/net17	I13/I0/net11	net49	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI13/I1/T5	I13/net16	I13/I1/net11	net41	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI13/I2/T5	net59	I13/I2/net11	I13/net17	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I5/I0/T5	I24/I8/net7	I24/I8/I5/I0/net09	gnd!	gnd!
+ nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I6/I0/T5	I24/I8/net9	I24/I8/I6/I0/net09	gnd!	gnd!
+ nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I5/I0/T5	I24/I1/net7	I24/I1/I5/I0/net09	gnd!	gnd!
+ nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I6/I0/T5	I24/I1/net9	I24/I1/I6/I0/net09	gnd!	gnd!
+ nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I5/I0/T5	I24/I2/net7	I24/I2/I5/I0/net09	gnd!	gnd!
+ nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I6/I0/T5	I24/I2/net9	I24/I2/I6/I0/net09	gnd!	gnd!
+ nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I5/I0/T5	I24/I3/net7	I24/I3/I5/I0/net09	gnd!	gnd!
+ nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I6/I0/T5	I24/I3/net9	I24/I3/I6/I0/net09	gnd!	gnd!
+ nfet	L=0.12U	W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I5/I0/T2	I24/I8/I5/I0/net09	I24/net12
+ I24/I8/I5/I0/net15	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I6/I0/T2	I24/I8/I6/I0/net09	I24/I8/net10
+ I24/I8/I6/I0/net15	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I5/I0/T2	I24/I1/I5/I0/net09	I24/net16
+ I24/I1/I5/I0/net15	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I6/I0/T2	I24/I1/I6/I0/net09	I24/I1/net10
+ I24/I1/I6/I0/net15	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I5/I0/T2	I24/I2/I5/I0/net09	I24/net15
+ I24/I2/I5/I0/net15	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I6/I0/T2	I24/I2/I6/I0/net09	I24/I2/net10
+ I24/I2/I6/I0/net15	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I5/I0/T2	I24/I3/I5/I0/net09	I24/net13
+ I24/I3/I5/I0/net15	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I6/I0/T2	I24/I3/I6/I0/net09	I24/I3/net10
+ I24/I3/I6/I0/net15	gnd!	nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI13/I0/I3/T0	I13/I0/net11	INST0	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI13/I1/I3/T0	I13/I1/net11	INST0	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI13/I2/I3/T0	I13/I2/net11	INST1	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I5/I0/T3	I24/I8/I5/I0/net15	IN0	gnd!	gnd!	nfet
+ L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I6/I0/T3	I24/I8/I6/I0/net15	I24/Y	gnd!	gnd!	nfet
+ L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I5/I0/T3	I24/I1/I5/I0/net15	IN1	gnd!	gnd!	nfet
+ L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I6/I0/T3	I24/I1/I6/I0/net15	I24/net9	gnd!	gnd!
+ nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I5/I0/T3	I24/I2/I5/I0/net15	IN2	gnd!	gnd!	nfet
+ L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I6/I0/T3	I24/I2/I6/I0/net15	I24/net10	gnd!	gnd!
+ nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I5/I0/T3	I24/I3/I5/I0/net15	IN3	gnd!	gnd!	nfet
+ L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I6/I0/T3	I24/I3/I6/I0/net15	I24/net11	gnd!	gnd!
+ nfet	L=0.12U	W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I11/I3/T2	I24/net12	I24/I11/net10	I24/I11/I3/net16	gnd!
+ nfet	L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I12/I3/T2	I24/net16	I24/I12/net10	I24/I12/I3/net16	gnd!
+ nfet	L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I13/I3/T2	I24/net15	I24/I13/net10	I24/I13/I3/net16	gnd!
+ nfet	L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I14/I3/T2	I24/net13	I24/I14/net10	I24/I14/I3/net16	gnd!
+ nfet	L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I10/T5	I24/Y	I24/I10/net09	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I11/I0/T3	I24/I11/I0/net16	I24/I11/net7	gnd!	gnd!	nfet
+ L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I12/I0/T3	I24/I12/I0/net16	I24/I12/net7	gnd!	gnd!	nfet
+ L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I13/I0/T3	I24/I13/I0/net16	I24/I13/net7	gnd!	gnd!	nfet
+ L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I11/I0/T2	I24/I11/net10	I24/Y	I24/I11/I0/net16	gnd!	nfet
+ L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I12/I0/T2	I24/I12/net10	I24/Y	I24/I12/I0/net16	gnd!	nfet
+ L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I13/I0/T2	I24/I13/net10	I24/Y	I24/I13/I0/net16	gnd!	nfet
+ L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I10/T3	I24/I10/net15	I24/net14	gnd!	gnd!	nfet	L=0.12U
+ W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I10/T2	I24/I10/net09	INST0	I24/I10/net15	gnd!	nfet	L=0.12U
+ W=0.56U
+ wt=5.6e-07 rf=0 nrs=0.427184 nrd=0.427184 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I11/I3/T3	I24/I11/I3/net16	I24/I11/net9	gnd!	gnd!	nfet
+ L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I12/I3/T3	I24/I12/I3/net16	I24/I12/net9	gnd!	gnd!	nfet
+ L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I13/I3/T3	I24/I13/I3/net16	I24/I13/net9	gnd!	gnd!	nfet
+ L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI16/I0/T3	net47	INST0	I16/net17	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI16/I1/T3	net50	INST0	I16/net16	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI16/I2/T3	I16/net16	INST1	net61	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I14/I0/T3	I24/I14/I0/net16	I24/I14/net7	gnd!	gnd!	nfet
+ L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I14/I0/T2	I24/I14/net10	I24/Y	I24/I14/I0/net16	gnd!	nfet
+ L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I14/I3/T3	I24/I14/I3/net16	I24/I14/net9	gnd!	gnd!	nfet
+ L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI16/I0/T5	I16/net17	I16/I0/net11	net47	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI16/I1/T5	I16/net16	I16/I1/net11	net40	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI16/I2/T5	net61	I16/I2/net11	I16/net17	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I11/I2/T3	I24/I11/I2/net16	OUT0	gnd!	gnd!	nfet	L=0.12U
+ W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I12/I2/T3	I24/I12/I2/net16	OUT1	gnd!	gnd!	nfet	L=0.12U
+ W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I13/I2/T3	I24/I13/I2/net16	OUT2	gnd!	gnd!	nfet	L=0.12U
+ W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I14/I2/T3	I24/I14/I2/net16	OUT3	gnd!	gnd!	nfet	L=0.12U
+ W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I11/I2/T2	I24/I11/net9	I24/I11/net7	I24/I11/I2/net16	gnd!
+ nfet	L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I12/I2/T2	I24/I12/net9	I24/I12/net7	I24/I12/I2/net16	gnd!
+ nfet	L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I13/I2/T2	I24/I13/net9	I24/I13/net7	I24/I13/I2/net16	gnd!
+ nfet	L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I14/I2/T2	I24/I14/net9	I24/I14/net7	I24/I14/I2/net16	gnd!
+ nfet	L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I11/I4/T2	I24/I11/net7	OUT0	I24/I11/I4/net16	gnd!	nfet
+ L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I12/I4/T2	I24/I12/net7	OUT1	I24/I12/I4/net16	gnd!	nfet
+ L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I13/I4/T2	I24/I13/net7	OUT2	I24/I13/I4/net16	gnd!	nfet
+ L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I14/I4/T2	I24/I14/net7	OUT3	I24/I14/I4/net16	gnd!	nfet
+ L=0.12U	W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I9/T0	I24/net14	INST1	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI16/I0/I3/T0	I16/I0/net11	INST0	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI16/I1/I3/T0	I16/I1/net11	INST0	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI16/I2/I3/T0	I16/I2/net11	INST1	gnd!	gnd!	nfet	L=0.12U
+ W=0.28U
+ wt=2.8e-07 rf=0 nrs=0.93617 nrd=0.93617 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I11/I4/T3	I24/I11/I4/net16	I24/Y	gnd!	gnd!	nfet	L=0.12U
+ W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I12/I4/T3	I24/I12/I4/net16	I24/Y	gnd!	gnd!	nfet	L=0.12U
+ W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I13/I4/T3	I24/I13/I4/net16	I24/Y	gnd!	gnd!	nfet	L=0.12U
+ W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I14/I4/T3	I24/I14/I4/net16	I24/Y	gnd!	gnd!	nfet	L=0.12U
+ W=1U
+ wt=1e-06 rf=0 nrs=0.230366 nrd=0.230366 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I8/T2	net40	I1/I8/net11	I1/net13	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I9/T2	net41	I1/I9/net11	I1/net10	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I10/T2	net48	I1/I10/net11	I1/net7	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I11/T2	net39	I1/I11/net11	I1/net14	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I8/T4	I1/net35	S0	net40	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I9/T4	I1/net19	S0	net41	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I10/T4	I1/net16	S0	net48	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I11/T4	I1/net3	S0	net39	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I0/T2	net50	I25/I0/net11	gnd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I1/T2	net46	I25/I1/net11	gnd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I0/T4	OUT0	IN0	net50	vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I1/T4	OUT1	I25/net21	net46	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I8/I3/T1	I1/I8/net11	S0	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I9/I3/T1	I1/I9/net11	S0	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I10/I3/T1	I1/I10/net11	S0	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I11/I3/T1	I1/I11/net11	S0	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I4/T2	I1/net13	I1/I4/net11	I1/net3	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I5/T2	I1/net10	I1/I5/net11	I1/net35	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I6/T2	I1/net7	I1/I6/net11	I1/net19	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I7/T2	I1/net14	I1/I7/net11	I1/net16	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I4/T4	I1/net19	net27	I1/net13	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I5/T4	I1/net16	net27	I1/net10	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I6/T4	I1/net3	net27	I1/net7	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I7/T4	I1/net35	net27	I1/net14	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I0/I3/T1	I25/I0/net11	IN0	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I1/I3/T1	I25/I1/net11	I25/net21	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I5/T5	I25/I5/net20	IN1	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I5/T6	I25/I5/net11	IN0	I25/I5/net20	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I4/I3/T1	I1/I4/net11	net27	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I5/I3/T1	I1/I5/net11	net27	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I6/I3/T1	I1/I6/net11	net27	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I7/I3/T1	I1/I7/net11	net27	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I5/T1	I25/net21	I25/I5/net11	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I0/T2	I1/net35	I1/I0/net11	OUT2	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I1/T2	I1/net19	I1/I1/net11	OUT3	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I2/T2	I1/net16	I1/I2/net11	OUT0	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I3/T2	I1/net3	I1/I3/net11	OUT1	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I0/T4	OUT0	S1	I1/net35	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I1/T4	OUT1	S1	I1/net19	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I2/T4	OUT2	S1	I1/net16	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I3/T4	OUT3	S1	I1/net3	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I0/I3/T1	I1/I0/net11	S1	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I1/I3/T1	I1/I1/net11	S1	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I2/I3/T1	I1/I2/net11	S1	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI1/I3/I3/T1	I1/I3/net11	S1	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI19/I3/T1	I19/net11	net27	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI18/I3/T1	I18/net11	net27	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI39/T1	vdd!	I39/net11	net27	vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI39/T6	I39/net20	IN2	I39/net11	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI19/T2	S0	I19/net11	IN2	vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI18/T2	S1	I18/net11	IN3	vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI39/T5	vdd!	IN3	I39/net20	vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI19/T4	IN1	net27	S0	vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI18/T4	IN0	net27	S1	vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI10/T6	I10/net023	I10/net14	vdd!	vdd!	pfet	L=0.12U
+ W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI12/T6	I12/net023	I12/net14	vdd!	vdd!	pfet	L=0.12U
+ W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI10/T10	I10/net10	CLK	I10/net023	vdd!	pfet	L=0.48U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI12/T10	I12/net10	CLK	I12/net023	vdd!	pfet	L=0.48U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI10/T9	OUT1	I10/net023	vdd!	vdd!	pfet	L=0.12U	W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI12/T9	OUT3	I12/net023	vdd!	vdd!	pfet	L=0.12U	W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI10/T1	I10/net32	net59	vdd!	vdd!	pfet	L=0.12U	W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI12/T1	I12/net32	net60	vdd!	vdd!	pfet	L=0.12U	W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI10/T2	I10/net10	I10/CLKN	I10/net32	vdd!	pfet	L=0.12U
+ W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI12/T2	I12/net10	I12/CLKN	I12/net32	vdd!	pfet	L=0.12U
+ W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI10/T13	I10/net31	I10/net10	vdd!	vdd!	pfet	L=0.12U
+ W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI12/T13	I12/net31	I12/net10	vdd!	vdd!	pfet	L=0.12U
+ W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI10/T14	I10/net14	CLK	I10/net31	vdd!	pfet	L=0.12U
+ W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI12/T14	I12/net14	CLK	I12/net31	vdd!	pfet	L=0.12U
+ W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I2/T2	net45	I25/I2/net11	gnd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I3/T2	net44	I25/I3/net11	gnd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I2/T4	OUT2	I25/net22	net45	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I3/T4	OUT3	I25/net23	net44	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI10/T15	I10/CLKN	CLK	vdd!	vdd!	pfet	L=0.12U
+ W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI12/T15	I12/CLKN	CLK	vdd!	vdd!	pfet	L=0.12U
+ W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI9/T10	I9/net10	CLK	I9/net023	vdd!	pfet	L=0.48U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI31/T10	I31/net10	CLK	I31/net023	vdd!	pfet	L=0.48U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I6/T1	I25/net22	I25/I6/net11	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I7/T1	I25/net23	I25/I7/net11	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI9/T9	OUT0	I9/net023	vdd!	vdd!	pfet	L=0.12U	W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI31/T9	OUT2	I31/net023	vdd!	vdd!	pfet	L=0.12U	W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I2/I3/T1	I25/I2/net11	I25/net22	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I3/I3/T1	I25/I3/net11	I25/net23	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI9/T13	I9/net31	I9/net10	vdd!	vdd!	pfet	L=0.12U
+ W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI31/T13	I31/net31	I31/net10	vdd!	vdd!	pfet	L=0.12U
+ W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI9/T14	I9/net14	CLK	I9/net31	vdd!	pfet	L=0.12U
+ W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI31/T14	I31/net14	CLK	I31/net31	vdd!	pfet	L=0.12U
+ W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI9/T6	I9/net023	I9/net14	vdd!	vdd!	pfet	L=0.12U
+ W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI31/T6	I31/net023	I31/net14	vdd!	vdd!	pfet	L=0.12U
+ W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I6/T5	I25/I6/net20	IN2	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I7/T5	I25/I7/net20	IN3	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I6/T6	I25/I6/net11	IN0	I25/I6/net20	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI25/I7/T6	I25/I7/net11	IN0	I25/I7/net20	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI9/T15	I9/CLKN	CLK	vdd!	vdd!	pfet	L=0.12U	W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI31/T15	I31/CLKN	CLK	vdd!	vdd!	pfet	L=0.12U
+ W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI9/T1	I9/net32	net61	vdd!	vdd!	pfet	L=0.12U	W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI31/T1	I31/net32	net58	vdd!	vdd!	pfet	L=0.12U	W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI9/T2	I9/net10	I9/CLKN	I9/net32	vdd!	pfet	L=0.12U
+ W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI31/T2	I31/net10	I31/CLKN	I31/net32	vdd!	pfet	L=0.12U
+ W=1.72U
+ wt=1.72e-06 rf=0 nrs=0.131343 nrd=0.131343 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI15/I0/I3/T1	I15/I0/net11	INST0	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI15/I1/I3/T1	I15/I1/net11	INST0	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI15/I2/I3/T1	I15/I2/net11	INST1	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI15/I0/T2	I15/net17	I15/I0/net11	net42	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI15/I1/T2	I15/net16	I15/I1/net11	net44	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI15/I2/T2	net60	I15/I2/net11	I15/net16	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI15/I0/T4	net42	INST0	I15/net17	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI15/I1/T4	net39	INST0	I15/net16	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI15/I2/T4	I15/net17	INST1	net60	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI14/I0/T4	net43	INST0	I14/net17	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI14/I1/T4	net48	INST0	I14/net16	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI14/I2/T4	I14/net17	INST1	net58	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I3/T1	I24/net9	I24/I8/I3/net11	vdd!	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I3/T1	I24/net10	I24/I1/I3/net11	vdd!	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I3/T1	I24/net11	I24/I2/I3/net11	vdd!	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I3/T1	net046	I24/I3/I3/net11	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI14/I0/T2	I14/net17	I14/I0/net11	net43	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI14/I1/T2	I14/net16	I14/I1/net11	net45	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI14/I2/T2	net58	I14/I2/net11	I14/net16	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I3/T5	I24/I8/I3/net20	I24/I8/net9	vdd!	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I3/T5	I24/I1/I3/net20	I24/I1/net9	vdd!	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I3/T5	I24/I2/I3/net20	I24/I2/net9	vdd!	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I3/T5	I24/I3/I3/net20	I24/I3/net9	vdd!	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I3/T6	I24/I8/I3/net11	I24/I8/net7	I24/I8/I3/net20
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I3/T6	I24/I1/I3/net11	I24/I1/net7	I24/I1/I3/net20
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I3/T6	I24/I2/I3/net11	I24/I2/net7	I24/I2/I3/net20
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I3/T6	I24/I3/I3/net11	I24/I3/net7	I24/I3/I3/net20
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I5/I3/T4	I24/I8/net10	I24/I8/I5/I3/net09	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I6/I3/T4	net47	I24/I8/I6/I3/net09	vdd!	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I5/I3/T4	I24/I1/net10	I24/I1/I5/I3/net09	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I6/I3/T4	net49	I24/I1/I6/I3/net09	vdd!	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I5/I3/T4	I24/I2/net10	I24/I2/I5/I3/net09	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I6/I3/T4	net43	I24/I2/I6/I3/net09	vdd!	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I5/I3/T4	I24/I3/net10	I24/I3/I5/I3/net09	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I6/I3/T4	net42	I24/I3/I6/I3/net09	vdd!	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI14/I0/I3/T1	I14/I0/net11	INST0	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI14/I1/I3/T1	I14/I1/net11	INST0	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI14/I2/I3/T1	I14/I2/net11	INST1	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I5/I3/T1	vdd!	I24/I8/I5/net13	I24/I8/I5/I3/net09
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I6/I3/T1	vdd!	I24/I8/I6/net13	I24/I8/I6/I3/net09
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I5/I3/T1	vdd!	I24/I1/I5/net13	I24/I1/I5/I3/net09
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I6/I3/T1	vdd!	I24/I1/I6/net13	I24/I1/I6/I3/net09
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I5/I3/T1	vdd!	I24/I2/I5/net13	I24/I2/I5/I3/net09
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I6/I3/T1	vdd!	I24/I2/I6/net13	I24/I2/I6/I3/net09
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I5/I3/T1	vdd!	I24/I3/I5/net13	I24/I3/I5/I3/net09
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I6/I3/T1	vdd!	I24/I3/I6/net13	I24/I3/I6/I3/net09
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I5/I3/T0	I24/I8/I5/I3/net09	I24/I8/I5/net12	vdd!
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I6/I3/T0	I24/I8/I6/I3/net09	I24/I8/I6/net12	vdd!
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I5/I3/T0	I24/I1/I5/I3/net09	I24/I1/I5/net12	vdd!
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I6/I3/T0	I24/I1/I6/I3/net09	I24/I1/I6/net12	vdd!
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I5/I3/T0	I24/I2/I5/I3/net09	I24/I2/I5/net12	vdd!
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I6/I3/T0	I24/I2/I6/I3/net09	I24/I2/I6/net12	vdd!
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I5/I3/T0	I24/I3/I5/I3/net09	I24/I3/I5/net12	vdd!
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I6/I3/T0	I24/I3/I6/I3/net09	I24/I3/I6/net12	vdd!
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I5/I1/T1	I24/I8/I5/net12	I24/I8/I5/I1/net11	vdd!
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I6/I1/T1	I24/I8/I6/net12	I24/I8/I6/I1/net11	vdd!
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I5/I1/T1	I24/I1/I5/net12	I24/I1/I5/I1/net11	vdd!
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I6/I1/T1	I24/I1/I6/net12	I24/I1/I6/I1/net11	vdd!
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I5/I1/T1	I24/I2/I5/net12	I24/I2/I5/I1/net11	vdd!
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I6/I1/T1	I24/I2/I6/net12	I24/I2/I6/I1/net11	vdd!
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I5/I1/T1	I24/I3/I5/net12	I24/I3/I5/I1/net11	vdd!
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I6/I1/T1	I24/I3/I6/net12	I24/I3/I6/I1/net11	vdd!
+ vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I5/I1/T6	I24/I8/I5/I1/net11	I24/net12
+ I24/I8/I5/I1/net20	vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I6/I1/T6	I24/I8/I6/I1/net11	I24/I8/net10
+ I24/I8/I6/I1/net20	vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I5/I1/T6	I24/I1/I5/I1/net11	I24/net16
+ I24/I1/I5/I1/net20	vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I6/I1/T6	I24/I1/I6/I1/net11	I24/I1/net10
+ I24/I1/I6/I1/net20	vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I5/I1/T6	I24/I2/I5/I1/net11	I24/net15
+ I24/I2/I5/I1/net20	vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I6/I1/T6	I24/I2/I6/I1/net11	I24/I2/net10
+ I24/I2/I6/I1/net20	vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I5/I1/T6	I24/I3/I5/I1/net11	I24/net13
+ I24/I3/I5/I1/net20	vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I6/I1/T6	I24/I3/I6/I1/net11	I24/I3/net10
+ I24/I3/I6/I1/net20	vdd!	pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I5/I1/T5	I24/I8/I5/I1/net20	IN0	vdd!	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I6/I1/T5	I24/I8/I6/I1/net20	I24/Y	vdd!	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I5/I1/T5	I24/I1/I5/I1/net20	IN1	vdd!	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I6/I1/T5	I24/I1/I6/I1/net20	I24/net9	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I5/I1/T5	I24/I2/I5/I1/net20	IN2	vdd!	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I6/I1/T5	I24/I2/I6/I1/net20	I24/net10	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I5/I1/T5	I24/I3/I5/I1/net20	IN3	vdd!	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I6/I1/T5	I24/I3/I6/I1/net20	I24/net11	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI13/I0/T4	net49	INST0	I13/net17	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI13/I1/T4	net41	INST0	I13/net16	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI13/I2/T4	I13/net17	INST1	net59	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I5/I2/T1	I24/I8/I5/net13	I24/I8/net7	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I6/I2/T1	I24/I8/I6/net13	I24/I8/net9	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I5/I2/T1	I24/I1/I5/net13	I24/I1/net7	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I6/I2/T1	I24/I1/I6/net13	I24/I1/net9	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I5/I2/T1	I24/I2/I5/net13	I24/I2/net7	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I6/I2/T1	I24/I2/I6/net13	I24/I2/net9	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I5/I2/T1	I24/I3/I5/net13	I24/I3/net7	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I6/I2/T1	I24/I3/I6/net13	I24/I3/net9	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I5/I0/T0	I24/I8/I5/I0/net09	IN0	vdd!	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I6/I0/T0	I24/I8/I6/I0/net09	I24/Y	vdd!	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I5/I0/T0	I24/I1/I5/I0/net09	IN1	vdd!	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I5/I0/T1	vdd!	I24/net12	I24/I8/I5/I0/net09	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I6/I0/T1	vdd!	I24/I8/net10	I24/I8/I6/I0/net09	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I5/I0/T1	vdd!	I24/net16	I24/I1/I5/I0/net09	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I5/I0/T4	I24/I8/net7	I24/I8/I5/I0/net09	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I8/I6/I0/T4	I24/I8/net9	I24/I8/I6/I0/net09	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I5/I0/T4	I24/I1/net7	I24/I1/I5/I0/net09	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I11/I3/T1	vdd!	I24/I11/net10	I24/net12	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I12/I3/T1	vdd!	I24/I12/net10	I24/net16	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I11/I0/T0	I24/I11/net10	I24/I11/net7	vdd!	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I12/I0/T0	I24/I12/net10	I24/I12/net7	vdd!	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I11/I0/T1	vdd!	I24/Y	I24/I11/net10	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I12/I0/T1	vdd!	I24/Y	I24/I12/net10	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I11/I3/T0	I24/net12	I24/I11/net9	vdd!	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I12/I3/T0	I24/net16	I24/I12/net9	vdd!	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I11/I4/T0	I24/I11/net7	I24/Y	vdd!	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I12/I4/T0	I24/I12/net7	I24/Y	vdd!	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I11/I4/T1	vdd!	OUT0	I24/I11/net7	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I12/I4/T1	vdd!	OUT1	I24/I12/net7	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I11/I2/T0	I24/I11/net9	OUT0	vdd!	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I12/I2/T0	I24/I12/net9	OUT1	vdd!	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I11/I2/T1	vdd!	I24/I11/net7	I24/I11/net9	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I12/I2/T1	vdd!	I24/I12/net7	I24/I12/net9	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I6/I0/T0	I24/I1/I6/I0/net09	I24/net9	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I5/I0/T0	I24/I2/I5/I0/net09	IN2	vdd!	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I6/I0/T0	I24/I2/I6/I0/net09	I24/net10	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I6/I0/T1	vdd!	I24/I1/net10	I24/I1/I6/I0/net09	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I5/I0/T1	vdd!	I24/net15	I24/I2/I5/I0/net09	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I6/I0/T1	vdd!	I24/I2/net10	I24/I2/I6/I0/net09	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I1/I6/I0/T4	I24/I1/net9	I24/I1/I6/I0/net09	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I5/I0/T4	I24/I2/net7	I24/I2/I5/I0/net09	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I2/I6/I0/T4	I24/I2/net9	I24/I2/I6/I0/net09	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I10/T4	I24/Y	I24/I10/net09	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I13/I3/T1	vdd!	I24/I13/net10	I24/net15	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I13/I4/T0	I24/I13/net7	I24/Y	vdd!	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I13/I4/T1	vdd!	OUT2	I24/I13/net7	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I9/T1	I24/net14	INST1	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I13/I2/T0	I24/I13/net9	OUT2	vdd!	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I13/I2/T1	vdd!	I24/I13/net7	I24/I13/net9	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I13/I0/T0	I24/I13/net10	I24/I13/net7	vdd!	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I13/I0/T1	vdd!	I24/Y	I24/I13/net10	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I10/T0	I24/I10/net09	I24/net14	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I10/T1	vdd!	INST0	I24/I10/net09	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I13/I3/T0	I24/net15	I24/I13/net9	vdd!	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I14/I4/T0	I24/I14/net7	I24/Y	vdd!	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I14/I4/T1	vdd!	OUT3	I24/I14/net7	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I14/I2/T0	I24/I14/net9	OUT3	vdd!	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I14/I2/T1	vdd!	I24/I14/net7	I24/I14/net9	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I14/I0/T0	I24/I14/net10	I24/I14/net7	vdd!	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I14/I0/T1	vdd!	I24/Y	I24/I14/net10	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I14/I3/T0	I24/net13	I24/I14/net9	vdd!	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I14/I3/T1	vdd!	I24/I14/net10	I24/net13	vdd!	pfet	L=0.12U
+ W=1.6U
+ wt=1.6e-06 rf=0 nrs=0.141479 nrd=0.141479 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I5/I0/T0	I24/I3/I5/I0/net09	IN3	vdd!	vdd!	pfet
+ L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I5/I0/T1	vdd!	I24/net13	I24/I3/I5/I0/net09	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I5/I0/T4	I24/I3/net7	I24/I3/I5/I0/net09	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I6/I0/T0	I24/I3/I6/I0/net09	I24/net11	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I6/I0/T1	vdd!	I24/I3/net10	I24/I3/I6/I0/net09	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI24/I3/I6/I0/T4	I24/I3/net9	I24/I3/I6/I0/net09	vdd!	vdd!
+ pfet	L=0.12U	W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI13/I0/I3/T1	I13/I0/net11	INST0	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI13/I1/I3/T1	I13/I1/net11	INST0	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI13/I2/I3/T1	I13/I2/net11	INST1	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI13/I0/T2	I13/net17	I13/I0/net11	net49	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI13/I1/T2	I13/net16	I13/I1/net11	net46	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI13/I2/T2	net59	I13/I2/net11	I13/net16	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI16/I0/I3/T1	I16/I0/net11	INST0	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI16/I1/I3/T1	I16/I1/net11	INST0	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI16/I2/I3/T1	I16/I2/net11	INST1	vdd!	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI16/I0/T2	I16/net17	I16/I0/net11	net47	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI16/I1/T2	I16/net16	I16/I1/net11	net50	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI16/I2/T2	net61	I16/I2/net11	I16/net16	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI16/I0/T4	net47	INST0	I16/net17	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI16/I1/T4	net40	INST0	I16/net16	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
MI16/I2/T4	I16/net17	INST1	net61	vdd!	pfet	L=0.12U
+ W=0.86U
+ wt=8.6e-07 rf=0 nrs=0.269939 nrd=0.269939 ngcon=1 nf=1 mSwitch=0 m=1 blockParasiticsBetween="PC sub" PWORIENT=1 PLORIENT=1
*
*
*       CAPACITOR CARDS
*
*
C1	CLK	gnd!	1.37513E-14
C2	IN0	gnd!	2.72372E-14
C3	IN1	gnd!	2.75257E-14
C4	IN2	gnd!	3.30154E-14
C5	IN3	gnd!	3.41732E-14
C6	INST0	gnd!	3.29602E-14
C7	INST1	gnd!	2.71781E-14
C8	OUT0	gnd!	3.94837E-14
C9	OUT1	gnd!	4.37655E-14
C10	OUT2	gnd!	5.0646E-14
C11	OUT3	gnd!	4.37433E-14
C12	I24/I3/I6/I3/net09	gnd!	7.49212E-16
C13	I24/I3/I5/I3/net09	gnd!	6.88308E-16
C14	I24/I2/I6/I3/net09	gnd!	7.59073E-16
C15	I24/I2/I5/I3/net09	gnd!	6.88843E-16
C16	I24/I1/I6/I3/net09	gnd!	7.58338E-16
C17	I24/I1/I5/I3/net09	gnd!	6.88843E-16
C18	I24/I8/I6/I3/net09	gnd!	6.96987E-16
C19	I24/I8/I5/I3/net09	gnd!	6.89117E-16
C20	I12/net14	gnd!	8.60111E-16
C21	I10/net14	gnd!	8.59308E-16
C22	I24/I3/I6/net12	gnd!	7.36628E-16
C23	I24/I3/I5/net12	gnd!	6.98655E-16
C24	I24/I2/I6/net12	gnd!	7.31026E-16
C25	I24/I2/I5/net12	gnd!	7.05822E-16
C26	I24/I1/I6/net12	gnd!	7.31516E-16
C27	I24/I1/I5/net12	gnd!	6.98376E-16
C28	I24/I8/I6/net12	gnd!	7.085E-16
C29	I24/I8/I5/net12	gnd!	7.04949E-16
C30	I24/I3/I6/I1/net11	gnd!	1.03334E-15
C31	I24/I3/I5/I1/net11	gnd!	1.01937E-15
C32	I24/I2/I6/I1/net11	gnd!	1.03341E-15
C33	I24/I2/I5/I1/net11	gnd!	1.01836E-15
C34	I24/I1/I6/I1/net11	gnd!	1.0322E-15
C35	I24/I1/I5/I1/net11	gnd!	1.01836E-15
C36	I24/I8/I6/I1/net11	gnd!	1.01809E-15
C37	I24/I8/I5/I1/net11	gnd!	1.01861E-15
C38	I24/I3/I6/I0/net09	gnd!	7.65296E-16
C39	I24/I3/I5/I0/net09	gnd!	7.72922E-16
C40	I24/I2/I6/I0/net09	gnd!	7.64274E-16
C41	I24/I2/I5/I0/net09	gnd!	7.72245E-16
C42	I24/I1/I6/I0/net09	gnd!	7.63242E-16
C43	I24/I1/I5/I0/net09	gnd!	7.72245E-16
C44	I24/I8/I6/I0/net09	gnd!	7.64216E-16
C45	I24/I8/I5/I0/net09	gnd!	7.72926E-16
C46	I25/I7/net11	gnd!	8.18961E-16
C47	I25/I6/net11	gnd!	8.34916E-16
C48	I25/I5/net11	gnd!	8.35953E-16
C49	I31/net14	gnd!	8.60583E-16
C50	I9/net14	gnd!	8.59877E-16
C51	I24/I10/net09	gnd!	6.46617E-16
C52	I39/net11	gnd!	8.90486E-16
C53	I24/net14	gnd!	7.8847E-16
C54	net046	gnd!	3.06311E-16
C55	I24/I3/I3/net11	gnd!	8.41574E-16
C56	I24/I2/I3/net11	gnd!	8.43194E-16
C57	I24/I1/I3/net11	gnd!	8.47023E-16
C58	I24/I8/I3/net11	gnd!	8.49461E-16
C59	I1/I8/net11	gnd!	1.03127E-15
C60	I1/net13	gnd!	2.71277E-15
C61	I1/I9/net11	gnd!	1.03309E-15
C62	I1/I4/net11	gnd!	1.03086E-15
C63	I1/net10	gnd!	2.77944E-15
C64	I1/I10/net11	gnd!	1.03312E-15
C65	I1/I5/net11	gnd!	1.02893E-15
C66	I1/net7	gnd!	2.77308E-15
C67	I1/I0/net11	gnd!	1.03544E-15
C68	I1/I11/net11	gnd!	1.03844E-15
C69	I1/I6/net11	gnd!	1.02878E-15
C70	I1/net14	gnd!	2.82635E-15
C71	I1/net19	gnd!	8.43032E-15
C72	I1/I1/net11	gnd!	1.02978E-15
C73	I1/I7/net11	gnd!	1.03798E-15
C74	I1/I2/net11	gnd!	1.0309E-15
C75	I1/net16	gnd!	8.94015E-15
C76	I1/net35	gnd!	9.08204E-15
C77	I19/net11	gnd!	1.04463E-15
C78	I1/net3	gnd!	1.0808E-14
C79	I25/I0/net11	gnd!	9.786E-16
C80	I1/I3/net11	gnd!	1.02509E-15
C81	I18/net11	gnd!	1.04852E-15
C82	I25/I1/net11	gnd!	9.66521E-16
C83	I25/net21	gnd!	1.49138E-15
C84	S0	gnd!	1.50878E-14
C85	S1	gnd!	1.21653E-14
C86	I25/I2/net11	gnd!	9.66786E-16
C87	I25/net22	gnd!	1.50845E-15
C88	net27	gnd!	1.878E-14
C89	I24/I8/I5/net13	gnd!	1.39932E-15
C90	I24/I8/net7	gnd!	3.03961E-15
C91	I25/I3/net11	gnd!	9.67309E-16
C92	I25/net23	gnd!	1.50082E-15
C93	I24/net12	gnd!	2.87817E-15
C94	I24/I8/I6/net13	gnd!	1.40952E-15
C95	I10/net023	gnd!	1.63733E-15
C96	I24/I8/net9	gnd!	3.22633E-15
C97	I10/net10	gnd!	1.96985E-15
C98	I24/I11/net10	gnd!	9.97498E-16
C99	I24/I8/net10	gnd!	5.15118E-15
C100	I10/CLKN	gnd!	2.21347E-15
C101	I24/I1/I5/net13	gnd!	1.39997E-15
C102	I24/I11/net9	gnd!	1.40569E-15
C103	I24/I1/net7	gnd!	2.98517E-15
C104	I12/net023	gnd!	1.59224E-15
C105	I24/I11/net7	gnd!	1.64242E-15
C106	I12/net10	gnd!	1.94448E-15
C107	I24/net16	gnd!	2.89519E-15
C108	I24/I1/I6/net13	gnd!	1.46523E-15
C109	I24/I1/net9	gnd!	3.22833E-15
C110	I9/net023	gnd!	1.62345E-15
C111	I12/CLKN	gnd!	2.21844E-15
C112	I9/net10	gnd!	1.94332E-15
C113	I24/net9	gnd!	5.39735E-15
C114	I24/I12/net10	gnd!	9.99617E-16
C115	I24/I1/net10	gnd!	5.24187E-15
C116	I9/CLKN	gnd!	2.19058E-15
C117	net60	gnd!	3.60882E-15
C118	I24/I2/I5/net13	gnd!	1.39997E-15
C119	I24/I12/net9	gnd!	1.40711E-15
C120	I24/I2/net7	gnd!	2.99133E-15
C121	I31/net023	gnd!	1.61117E-15
C122	I24/I12/net7	gnd!	1.63391E-15
C123	I31/net10	gnd!	1.91347E-15
C124	I24/net15	gnd!	2.89449E-15
C125	I24/I2/I6/net13	gnd!	1.4666E-15
C126	I24/I2/net9	gnd!	3.22891E-15
C127	I31/CLKN	gnd!	2.22143E-15
C128	I15/I0/net11	gnd!	9.73581E-16
C129	net42	gnd!	5.65985E-15
C130	I24/net10	gnd!	6.22129E-15
C131	I24/I13/net10	gnd!	1.0029E-15
C132	I24/I2/net10	gnd!	5.12309E-15
C133	I24/I3/I5/net13	gnd!	1.39887E-15
C134	I24/I3/net7	gnd!	3.06566E-15
C135	I24/I13/net9	gnd!	1.40816E-15
C136	net39	gnd!	1.34527E-14
C137	I15/I1/net11	gnd!	9.68284E-16
C138	I24/I13/net7	gnd!	1.63287E-15
C139	net44	gnd!	9.1178E-15
C140	I24/net13	gnd!	2.89412E-15
C141	I24/I3/I6/net13	gnd!	1.46735E-15
C142	I24/I3/net9	gnd!	3.23062E-15
C143	I15/net17	gnd!	2.901E-15
C144	I15/I2/net11	gnd!	9.85062E-16
C145	I15/net16	gnd!	2.52266E-15
C146	I14/I0/net11	gnd!	9.70438E-16
C147	I24/net11	gnd!	6.35232E-15
C148	net43	gnd!	7.43491E-15
C149	I24/I14/net10	gnd!	1.00161E-15
C150	I24/I3/net10	gnd!	5.12891E-15
C151	I24/I14/net9	gnd!	1.40671E-15
C152	net58	gnd!	6.98965E-15
C153	I24/I14/net7	gnd!	1.63209E-15
C154	net48	gnd!	1.84479E-14
C155	I14/I1/net11	gnd!	9.66076E-16
C156	net45	gnd!	1.31062E-14
C157	I14/net17	gnd!	2.89946E-15
C158	I14/I2/net11	gnd!	9.82854E-16
C159	I14/net16	gnd!	2.51645E-15
C160	I24/Y	gnd!	2.02548E-14
C161	I13/I0/net11	gnd!	9.72877E-16
C162	net49	gnd!	1.13246E-14
C163	net41	gnd!	2.28985E-14
C164	net59	gnd!	1.10743E-14
C165	I13/I1/net11	gnd!	9.68284E-16
C166	net46	gnd!	1.67839E-14
C167	I13/net17	gnd!	2.93676E-15
C168	I13/I2/net11	gnd!	9.85062E-16
C169	I13/net16	gnd!	2.53001E-15
C170	I16/I0/net11	gnd!	9.7429E-16
C171	net47	gnd!	1.45491E-14
C172	net40	gnd!	2.21902E-14
C173	net61	gnd!	9.3945E-15
C174	I16/I1/net11	gnd!	9.69081E-16
C175	net50	gnd!	1.72539E-14
C176	I16/net17	gnd!	2.90858E-15
C177	vdd!	gnd!	9.56884E-14
C178	I16/I2/net11	gnd!	9.85896E-16
C179	I16/net16	gnd!	2.52776E-15
*
*
.ENDS microprocessor
*
