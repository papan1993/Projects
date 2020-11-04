///////////////Anmol Gautam -- AXG190014////////Soumyadeep Choudhury -- SXC180056//////////
`timescale 1ns / 1ps

module test;

	reg sclk;
	reg dclk;
	
	reg start, reset, frame;
	reg signed [0:15] inputL, inputR;
	wire inready, outready, wsenL, wsenR;
	wire outputR, outputL;
	wire sl;
	reg [0:39] output_val [1:0];         /// Output little indian to big indian
	reg signed [0:15] dataleft [7527:0];
	reg signed [0:15] dataright [7527:0];
	reg [0:3] state;
	parameter dclkp = 1302.08;//1302.08; 
	parameter sclkp = 37.2023;//37.2023;
	
	integer count1=0, count2=0, outf, bit1=0, countout=0, frame_count = 0;
	integer coeff_cnt = 0, rj_cnt = 0, inputl_cnt = 0, inputr_cnt = 0;
	integer counttemp=0;
	integer resetflag = 0, resetflag2 = 0;
	
	controller_main uut(.sclk(sclk), .dclk(dclk), .start(start), .reset(reset), .inputL(inputL), .inputR(inputR),
								.frame(frame), .state(state), .inready(inready), .outready(outready), 
								.outputL(outputL), .outputR(outputR), .wsenL(wsenL), .wsenR(wsenR), .sl(sl));
	
	////// initial //////
	initial begin
	
		sclk = 0;
		dclk = 0;
		start = 1'b0;
		reset = 1'b0;
		frame = 1'b1;
		inputL = 16'b0;
		inputR = 16'b0;
		$readmemh("./data2_Right.in",dataright);
		$readmemh("./data2_Left.in",dataleft);
		outf = $fopen("data2.out","wb");
		#2604.16; // always double the data clock
		start = 1;
		#2604.16; // always double the data clock
		start = 0;
	
	end
	
	///////////////////////// clock /////////////////////////
	always
	begin 
		#(sclkp)sclk = ~sclk;
	end
	
	always
	begin
		#(dclkp)dclk = ~dclk;
	end
	
	
	always @(posedge dclk)
	begin
		
		if(start == 1)
		begin
				state = 4'b0000;
		end
		
		
		else if (count1 == 0 && start == 0 && state == 4'b0000)
		begin 
			state = 4'b0001;
		end
		
		
		else if (state == 4'b0010 && count1 >= 16)
		begin
			state = 4'b0011;
		end
		
		
		else if (state == 4'b0100 && count1 >= 528)
		begin
			state = 4'b0101;
		end
		
		
		else if(count1 == 4727 && resetflag == 0 && resetflag2 == 0)
		begin
			state = 4'b1111;
			reset = 1'b1;
			resetflag = 1;
		end
		else if (count1 == 6527 && resetflag == 0 && resetflag2 == 0)
		begin
			state = 4'b1111;
			reset = 1'b1;
			resetflag = 1;
		end
		else if(resetflag == 1 && resetflag2 == 0 && count1 == 4727)
		begin
			reset = 1'b0;
			state = 4'b0101;
			reset = 1'b0;
			resetflag2 = 1;
		end
		
		else if(resetflag == 1 && resetflag2 == 0 && count1 == 6527)
		begin
			reset = 1'b0;
			state = 4'b0101;
			reset = 1'b0;
			resetflag2 = 1;
		end
		
		///////////
		else if(inready == 1'b1)
		begin
			
			if (count1 < 16)
			begin
				state = 4'b0010;
			end
			
			
			else if(count1 >= 16 && count1 < 528)
			begin 
				state = 4'b0100;
			end
			
			  
			else if(count1 >= 528 && count1 < 7529 && sl == 1'b0)
			begin 
				state = 4'b0110;
			end
			
			
			else if(count1 >= 528 && count1 < 7529 && sl == 1'b1)
			begin
				state = 4'b1000;
			end
			
			
			if(count1 < 7528)
			begin
				if(bit1==0)
				begin
					frame = 1'b0;
					inputL = dataleft[count1];
					inputR = dataright[count1];			
				end
				
				else if (bit1 == 1)
				begin
					frame = 1'b1;
				end
			end
			
			
			bit1 = bit1 + 1;
			if(bit1 == 16)
			begin
				bit1=0;
				count1 = count1 + 1;
				resetflag = 0;
				resetflag2 = 0;
			end
		
		end
	end
	
	
	////////////////////////// output ///////////////////////////////
	always @(posedge sclk)
	begin
		if(outready && wsenL == 1'b1 && wsenR == 1'b1 && count1 <=7528 )
		begin 
			output_val[0][countout] = outputL;
			output_val[1][countout] = outputR;
			countout = countout + 1;
			if(countout == 40)
			begin 
				$fwrite(outf,"%h\t%h\n",output_val[0], output_val[1]);
				//$display("output -> ","%h\t%h\t\n", output_val[0], output_val[1], counttemp);
				counttemp = counttemp + 1;
				countout = 0;
			end
		end
	end
	//////////////////////////////////////////////////////////   


endmodule

