///////////////Anmol Gautam -- AXG190014////////Soumyadeep Choudhury -- SXC180056//////////
`timescale 1ns / 1ps 

module controller_main(sclk, dclk, start, reset, inputL, inputR, 
							frame, state, inready, outready, outputL, outputR, wsenL, wsenR, sl);

input sclk, dclk, frame, reset, start;
input signed [0:15] inputL, inputR;
input [0:3] state;
output reg inready, outready, outputL, outputR, wsenL, wsenR, sl = 1'b0;

wire inready_get, outready_get, outputL_get, outputR_get;

wire ren, hen, xen;
wire [0:4] rcount;
wire [0:9] hcount;
wire [0:12] xcount1;
wire [0:8] xcount2;

reg [0:4] rcount_upd;
reg [0:9] hcount_upd;
reg [0:12] xcount1_upd;
reg [0:8] xcount2_upd; 

reg signed [0:15] rvaluesL [15:0];
reg signed [0:15] rvaluesR [15:0];
reg signed [0:15] hvaluesL [511:0];
reg signed [0:15] hvaluesR [511:0];
reg signed [0:15] xvaluesL [255:0];
reg signed [0:15] xvaluesR [255:0];
reg [0:8] xindexL [7527:0];  // change from 255 to 7527 :0:8 for storing xcount2 values
reg [0:8] xindexR [7527:0];  // change from 255 to 7527 :0:8 for storing xcount2 values

integer ALU_left_flag = 0, ALU_right_flag = 0, left_x_cnt = 0, right_x_cnt = 0;
reg [0:8] x_cnt_retrieve_left; // for xcount2
reg [0:8] x_cnt_retrieve_right; // for xcount2 

////////////  Left ALU Parameters //////////////

reg [0:39] sum_hex_l;
reg [0:15] retrieve_xn_l;
reg [0:23] un_array_l [15:0];
reg [0:23] un_each_l;
reg [0:15] rj_each_hex_l;
reg [0:7] rj_each_hex_trim_l;
reg [0:23] xn_expand_l;
reg [0:23] xn_expand_comp_l;
reg [0:7] k_l;
reg [0:7] coeff_sign_l;
reg [0:7] coeff_decimal_hex_l;

integer loc_rj_l, m_l, j_l, x_loc_l, rj_count_l;

wire [0:23] w1_l,w2_l,w3_l,w4_l,w5_l,w6_l,w7_l,w8_l,w9_l,w10_l,w11_l,w12_l,w13_l,w14_l,w15_l,w16_l;
wire [0:39] out_wire_l;
reg [0:39] output_final_l [7527:0]; //change

////////////  Right ALU Parameters //////////////

reg [0:39] sum_hex_r;
reg [0:15] retrieve_xn_r;
reg [0:23] un_array_r [15:0];
reg [0:23] un_each_r;
reg [0:15] rj_each_hex_r;
reg [0:7] rj_each_hex_trim_r;
reg [0:23] xn_expand_r;
reg [0:23] xn_expand_comp_r;
reg [0:7] k_r;
reg [0:7] coeff_sign_r;
reg [0:7] coeff_decimal_hex_r;

integer loc_rj_r, m_r, j_r, x_loc_r, rj_count_r;

wire [0:23] w1_r,w2_r,w3_r,w4_r,w5_r,w6_r,w7_r,w8_r,w9_r,w10_r,w11_r,w12_r,w13_r,w14_r,w15_r,w16_r;
wire [0:39] out_wire_r;
reg [0:39] output_final_r [7527:0]; //change
wire clearen;
//////////////////////////////////////////////////


//////// Convolution initiation //////

convolution convolve_left(.clock(sclk),.w1(w1_l),.w2(w2_l),.w3(w3_l),.w4(w4_l),.w5(w5_l),
.w6(w6_l),.w7(w7_l),.w8(w8_l),.w9(w9_l),.w10(w10_l),.w11(w11_l),.w12(w12_l),.w13(w13_l),.w14(w14_l),
.w15(w15_l),.w16(w16_l),.out_wire(out_wire_l));

convolution convolve_right(.clock(sclk),.w1(w1_r),.w2(w2_r),.w3(w3_r),.w4(w4_r),.w5(w5_r),
.w6(w6_r),.w7(w7_r),.w8(w8_r),.w9(w9_r),.w10(w10_r),.w11(w11_r),.w12(w12_r),.w13(w13_r),.w14(w14_r),
.w15(w15_r),.w16(w16_r),.out_wire(out_wire_r));

///////////// Control State Initiation /////////////////

control_state ctrl(.frame(frame), .sclk(sclk), .dclk(dclk), .inready(inready_get),
					.outready(outready_get), .start(start), .reset(reset), .state(state), .ren(ren),
					.hen(hen), .hcount(hcount), .rcount(rcount), .xen(xen), .xcount1(xcount1), 
					.xcount2(xcount2), .clearen(clearen));
					
///////////// Assigning convolution wires ///////////

//// left ////

assign w1_l = un_array_l[0];
assign w2_l = un_array_l[1];
assign w3_l = un_array_l[2];
assign w4_l = un_array_l[3];
assign w5_l = un_array_l[4];
assign w6_l = un_array_l[5];
assign w7_l = un_array_l[6];
assign w8_l = un_array_l[7];
assign w9_l = un_array_l[8];
assign w10_l = un_array_l[9];
assign w11_l = un_array_l[10];
assign w12_l = un_array_l[11];
assign w13_l = un_array_l[12];
assign w14_l = un_array_l[13];
assign w15_l = un_array_l[14];
assign w16_l = un_array_l[15];

//// right ////

assign w1_r = un_array_r[0];
assign w2_r = un_array_r[1];
assign w3_r = un_array_r[2];
assign w4_r = un_array_r[3];
assign w5_r = un_array_r[4];
assign w6_r = un_array_r[5];
assign w7_r = un_array_r[6];
assign w8_r = un_array_r[7];
assign w9_r = un_array_r[8];
assign w10_r = un_array_r[9];
assign w11_r = un_array_r[10];
assign w12_r = un_array_r[11];
assign w13_r = un_array_r[12];
assign w14_r = un_array_r[13];
assign w15_r = un_array_r[14];
assign w16_r = un_array_r[15];

/////////////////////////////////////////

reg [0:39] outvalL, outvalR;
integer wrcountL = 0, wrcountR = 0, wrcL=0, wrcR=0;
integer wrenL, wrenR;
reg [0:39] tempL, tempR;
integer zerocount = 0;
integer counttemp =0;
integer clrj1, clrj2;
integer hard_flag, stop_cnt_1 = 0, stop_cnt_2 = 0; 

/////////////////////////////////////////

/////////////// Outputs connection ////////////

always @(negedge dclk && inready_get)
begin
	inready = inready_get;
end

always @(negedge dclk && outready_get)
begin
	outready = outready_get;
end

always @(negedge sclk)
begin
	if(wrenL == 1 && outready == 1'b1)
	begin
		wsenL = 1'b1;
		
		outputL = outvalL[wrcountL];//output_final_l[wrcL][wrcountL];
		tempL[wrcountL] = outvalL[wrcountL];
		wrcountL = wrcountL + 1;
		if(wrcountL > 40)
		begin
			wsenL = 1'b0;
			//$display("LEFT -> ","%h\t\n", tempL, wrcL);
			wrenL = 0;
			wrcL = wrcL + 1;
			wrcountL = 0;
		end
	end
end

always @(negedge sclk)
begin
	if(wrenR == 1 && outready == 1'b1)
	begin
		wsenR = 1'b1;
		
		outputR = outvalR[wrcountR];//output_final_r[wrcR][wrcountR];
		tempR[wrcountR] = outvalR[wrcountR];
		wrcountR = wrcountR + 1;
		if(wrcountR > 40)
		begin
			wrenR = 1'b0;
			//$display("RIGHT -> ","%h\t\n", tempR, wrcR);
			wrcR = wrcR + 1;
			wrenR = 0;
			wrcountR = 0;
		end
	end
end

////////////R_STORE/////////////////
always @(negedge dclk)
begin
	//#40
	if(ren == 1'b1)
	begin
		rcount_upd = rcount - 5'b00001;
		rvaluesL[rcount_upd] = inputL;
		rvaluesR[rcount_upd] = inputR;
		//$display(" rj_store iter -> %d", rcount_upd);
	end
end

//////////////H_STORE////////////////
always @(negedge dclk)
begin
	//#40
	if(hen == 1'b1)
	begin
		hcount_upd = hcount - 10'b0000000001;
		hvaluesL[hcount_upd] = inputL;
		hvaluesR[hcount_upd] = inputR;
		//$display(" coeff_store iter -> %d", hcount_upd);
	end
end

///////////X_STORE//////////////////
always @(negedge dclk)
begin

	/// Reset : clear data
	if(clearen == 1'b1)
	begin
		stop_cnt_1 = 1;
		stop_cnt_2 = 1;
		//$display("CLEARRRRRRR");
		inready = 1'b0;
		//$display("XEN :::","%b\n" ,xen);
		outready = 1'b0;
		//xcount1_upd = 13'b0000000000000;
		//xcount2_upd = 9'b000000000;
		
		//$display(" delete_count -> %d", left_x_cnt);
		
		for (clrj1=0; clrj1 < 7528; clrj1 = clrj1+1)
		begin
			xindexL[clrj1] <= 9'b000000000;
			xindexR[clrj1] <= 9'b000000000;
		end
		
		for (clrj2=0; clrj2 < 256; clrj2 = clrj2 + 1)
		begin
			xvaluesL[clrj2] <= 16'b0000000000000000;
			xvaluesR[clrj2] <= 16'b0000000000000000;
		end
		
		clrj1 = 0;
		clrj2 = 0;
			
		left_x_cnt = 0;
		right_x_cnt = 0;
		hard_flag = 1;
		
		ALU_left_flag = 0; // flag high for 1st time
		ALU_right_flag = 0;
		
	end
	else 
	begin
		// normal operation
		if(xen == 1'b1)
		begin
			xcount2_upd = xcount2 - 9'b000000001; 
			xcount1_upd = xcount1 - 13'b0000000000001;
			//counttemp = counttemp + 1;
			
			//$display("xcount1 xcount2 xcount1_upd xcount2_upd","%d\t%d\t%d\t%d", xcount1, xcount2, xcount1_upd, xcount2_upd);
			
			if( inputL == 16'b0000000000000000 && inputR == 16'b0000000000000000)
			begin
				zerocount = zerocount + 1;
			end
			else
			begin
				zerocount = 0;
				sl = 1'b0;
				outready = 1'b1;
			end
			
			if (hard_flag == 1) begin
				for (clrj2=0; clrj2 < 256; clrj2 = clrj2 + 1)
				begin
					xvaluesL[clrj2] <= 16'b0000000000000000;
					xvaluesR[clrj2] <= 16'b0000000000000000;
				end
				
				left_x_cnt = 0;
				right_x_cnt = 0;
				clrj2 =0;
				hard_flag = 0;
			end

						
			xvaluesL[xcount2_upd] <= inputL;
			xindexL[xcount1_upd] <= xcount2_upd;   // alternate count
			
			xvaluesR[xcount2_upd] <= inputR;
			xindexR[xcount1_upd] <= xcount2_upd;	// alternate count
			
			if(zerocount >= 800)
			begin
				sl = 1'b1;
				outready = 1'b0;
			end
			
			ALU_left_flag = 1; // flag high for 1st time
			ALU_right_flag = 1;
			
		
		end	
	
	end

end

///////////// ALU ////////////////

/// ALU-Left ///
always @(posedge sclk && ALU_left_flag == 1 && left_x_cnt <= xcount1_upd && clearen == 1'b0 && hard_flag == 0)
begin
	left_x_cnt = left_x_cnt + 9'b000000001; // n for left x (0 to n-1)
	//$display(" left : ALU iter -> %d", left_x_cnt);
	
	if (left_x_cnt == 1 && stop_cnt_1 == 1) 
	begin
		left_x_cnt = 0;
		stop_cnt_1 = 0;
	end
	else begin
	
		rj_count_l = 0;
		for (j_l=0; j_l<16; j_l=j_l+1) begin ///add delay (1 clock period)
		
			rj_each_hex_l = rvaluesL[j_l];            
			rj_each_hex_trim_l = rj_each_hex_l[8:15];
			un_each_l = 24'h000000;
			
			for (k_l=0; k_l < rj_each_hex_trim_l; k_l=k_l+1) 
			begin
			
				coeff_sign_l = hvaluesL[rj_count_l][0:7];          
				coeff_decimal_hex_l = hvaluesL[rj_count_l][8:15];  
			
				x_loc_l = left_x_cnt - coeff_decimal_hex_l - 1;  
				rj_count_l = rj_count_l + 1;
				
				if (x_loc_l >= 0) 
				begin
				
					// expanding
					// retriving x from index
					x_cnt_retrieve_left = xindexL[x_loc_l];
					//$display(" ALU fetch Index Location -> %d", x_cnt_retrieve_left);
					retrieve_xn_l = xvaluesL[x_cnt_retrieve_left]; // get x value 
					
					if (retrieve_xn_l[0] == 1'b0) 
					begin
					
						xn_expand_l = {8'h00,retrieve_xn_l};
					end
					else if (retrieve_xn_l[0] == 1'b1) begin

						xn_expand_l = {8'hff,retrieve_xn_l};
					end
				
					// get sign value			
					if (coeff_sign_l == 8'h00) begin  // change to 8'h00 for latest data
					
						un_each_l = un_each_l + xn_expand_l; 				
					end
					else if (coeff_sign_l == 8'h01) begin // change to 8'h01 for latest data
					
						xn_expand_comp_l = (~xn_expand_l + 1'b1);
						un_each_l = un_each_l + xn_expand_comp_l;				
					end
				end
			end
			
			un_array_l[j_l] = un_each_l;
			/*if (j == 15)
			begin
				$display(" ALU un_array each -> %h", un_array[j]);
			end*/
		end
			
		///add a delay of 1 clock period : sclk = 10
		#32;
		
		// Getting the output from the convolution module
		output_final_l[left_x_cnt - 1] = out_wire_l; // this will send value to testbench
		outvalL = out_wire_l;
		wrenL = 1;
		ALU_left_flag = 0;
		//$display("left : iniside controller -> %h\t%d \n", output_final_l[left_x_cnt - 1], left_x_cnt-1); 
	end
end

/// ALU-Right ///
always @(posedge sclk && ALU_right_flag == 1 && right_x_cnt <= xcount1_upd && clearen == 1'b0 && hard_flag == 0)
begin
	right_x_cnt = right_x_cnt + 9'b000000001; // n for left x (0 to n-1)
	//$display(" right : ALU iter -> %d", right_x_cnt);
	
	if (right_x_cnt == 1 && stop_cnt_2 == 1) 
	begin
		right_x_cnt = 0;
		stop_cnt_2 = 0;
	end
	else begin
	
		rj_count_r = 0;
		for (j_r=0; j_r<16; j_r=j_r+1) begin ///add delay (1 clock period)

			rj_each_hex_r = rvaluesR[j_r];            
			rj_each_hex_trim_r = rj_each_hex_r[8:15];
			un_each_r = 24'h000000;
			
			for (k_r=0; k_r < rj_each_hex_trim_r; k_r=k_r+1) 
			begin
			
				coeff_sign_r = hvaluesR[rj_count_r][0:7];          
				coeff_decimal_hex_r = hvaluesR[rj_count_r][8:15];  
			
				x_loc_r = right_x_cnt - coeff_decimal_hex_r - 1;  
				rj_count_r = rj_count_r + 1;
				
				if (x_loc_r >= 0) 
				begin
				
					// expanding
					// retriving x from index
					x_cnt_retrieve_right = xindexR[x_loc_r];
					//$display(" ALU fetch Index Location -> %d", x_cnt_retrieve_left);
					retrieve_xn_r = xvaluesR[x_cnt_retrieve_right]; // get x value 
					
					if (retrieve_xn_r[0] == 1'b0) 
					begin
					
						xn_expand_r = {8'h00,retrieve_xn_r};
					end
					else if (retrieve_xn_r[0] == 1'b1) begin

						xn_expand_r = {8'hff,retrieve_xn_r};
					end
				
					// get sign value			
					if (coeff_sign_r == 8'h00) begin  // change to 8'h00 for latest data
					
						un_each_r = un_each_r + xn_expand_r; 				
					end
					else if (coeff_sign_r == 8'h01) begin // change to 8'h01 for latest data
					
						xn_expand_comp_r = (~xn_expand_r + 1'b1);
						un_each_r = un_each_r + xn_expand_comp_r;				
					end
				end
			end
			
			un_array_r[j_r] = un_each_r;
		end
			
		///add a delay of 1 clock period : sclk = 10
		#32;

		// Getting the output from the convolution module
		output_final_r[right_x_cnt - 1] = out_wire_r; // this will send value to testbench
		outvalR = out_wire_r;
		wrenR = 1;
		ALU_right_flag = 0;
		//$display("right : iniside controller -> %h\t%d \n", output_final_r[right_x_cnt - 1], right_x_cnt-1); 
	end
end


endmodule 
////////////////////////////////////////////////////////////////

///////////////// control state module /////////////////////////////

module control_state(frame, sclk, dclk, inready, outready, start, reset, state, ren, 
					hen, hcount, rcount, xen, xcount1, xcount2, clearen);
					
input frame, sclk, dclk, reset , start;
output reg outready, inready;
input [0:3] state;
output reg ren, hen, xen, clearen;
output reg [0:9] hcount;
output reg [0:4] rcount;
output reg [0:12] xcount1;
output reg [0:8] xcount2;

always @(negedge dclk)
begin
	//#20
	//state-0
	if(state == 4'b0000)
	begin
		inready = 1'b0;
	end
	
	//state-1
	else if(state == 4'b0001)
	begin
		inready = 1'b1;
		rcount = 5'b00000;
	end
	
	//state-2
	else if(state == 4'b0010)
	begin
		if(frame == 1'b0)
		begin
			ren = 1'b1;
			rcount = rcount + 5'b00001;
		end
		else
		begin
			ren = 1'b0;
		end
	end
	
	//state-3
	else if(state == 4'b0011)
	begin 
		ren = 1'b0;		
		hcount = 10'b0000000000;
	end
	
	//state-4
	else if(state == 4'b0100)
	begin
		if(frame == 1'b0)
		begin
			hen = 1'b1;
			hcount = hcount + 10'b0000000001;
		end
		else
		begin
			hen = 1'b0;
		end
	end
	
	//state-5
	else if(state == 4'b0101)
	begin
		hen = 1'b0;
		inready = 1'b1;
		clearen = 1'b0;
		xcount1 = 13'b0000000000000;
		xcount2 = 9'b000000000;
	end	
	
	// state-6
	else if(state == 4'b0110)
	begin
		if(frame == 1'b0)
		begin
			xen = 1'b1;
			outready = 1'b1;			
			xcount1 = xcount1 + 13'b0000000000001;
			xcount2 = xcount2 + 9'b000000001;
			
			if(xcount2 > 256) //xcount2 starts from 1
			begin
				xcount2 = 9'b000000001;
			end
		end
		else
		begin
			xen = 1'b0;
		end
	end
	
	//state 8
	else if(state == 4'b1000)
	begin
		outready = 1'b0;
		if(frame == 1'b0)
		begin
			xen = 1'b1;
			xcount1 = xcount1 + 13'b0000000000001;
			xcount2 = xcount2 + 9'b000000001;
			
			if(xcount2 > 256) //xcount2 starts from 1
			begin
				xcount2 = 9'b000000001;
			end
		end
		else
		begin
			xen = 1'b0;
		end
	end
	
	//state7
	else if(state == 4'b1111)
	begin
		inready = 1'b0;
		clearen = 1'b1;
		xen = 1'b0;
		xcount1 = 13'b0000000000000;
		xcount2 = 9'b000000000;
	end

end

endmodule

///////////////////////////////////////

///////// Convolution Module /////////
module convolution(clock, w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16, out_wire);
	wire [0:15] temp = 0;
	input clock;
	reg [0:39] sum_final;
	input [0:23] w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16;
	output [0:39] out_wire;
	
	assign out_wire = sum_final;
	always @(*) begin
	sum_final = 0;
	end
	
	always @(negedge clock) begin
	//#0.2
	
	sum_final = {w1,temp[0:15]}; 
	sum_final = $signed(sum_final) >>>1;
	
	sum_final = (sum_final + {w2,temp[0:15]});
	sum_final = $signed(sum_final) >>>1;
	
	sum_final = (sum_final + {w3,temp[0:15]});
	sum_final = $signed(sum_final) >>>1;
	
	sum_final = (sum_final + {w4,temp[0:15]});
	sum_final = $signed(sum_final) >>>1;
	
	sum_final = (sum_final + {w5,temp[0:15]});
	sum_final = $signed(sum_final) >>>1;
	
	sum_final = (sum_final + {w6,temp[0:15]});
	sum_final = $signed(sum_final) >>>1;
	
	sum_final = (sum_final + {w7,temp[0:15]});
	sum_final = $signed(sum_final) >>>1;
	
	sum_final = (sum_final + {w8,temp[0:15]});
	sum_final = $signed(sum_final) >>>1;
	
	sum_final = (sum_final + {w9,temp[0:15]});
	sum_final = $signed(sum_final) >>>1;
	
	sum_final = (sum_final + {w10,temp[0:15]});
	sum_final = $signed(sum_final) >>>1;
	
	sum_final = (sum_final + {w11,temp[0:15]});
	sum_final = $signed(sum_final) >>>1;
	
	sum_final = (sum_final + {w12,temp[0:15]});
	sum_final = $signed(sum_final) >>>1;
	
	sum_final = (sum_final + {w13,temp[0:15]});
	sum_final = $signed(sum_final) >>>1;
	
	sum_final = (sum_final + {w14,temp[0:15]});
	sum_final = $signed(sum_final) >>>1;
	
	sum_final = (sum_final + {w15,temp[0:15]});
	sum_final = $signed(sum_final) >>>1;
	
	sum_final = (sum_final + {w16,temp[0:15]});
	sum_final = $signed(sum_final) >>>1; 
	
	end // end for always

endmodule