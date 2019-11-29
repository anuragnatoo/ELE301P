`include "recursiveDouble.v"

module top;
	reg [15:0] A,B;
	wire [15:0] Sum;
	wire Carry;
	reg iniC;

	CLA cr(A,B,Sum,iniC,Carry);
	initial
		begin
			A[15:0]=16'd10000; B[15:0]=16'd20000; iniC = 1;
			#5 A[15:0]=16'd45000; B[15:0]=16'd4; iniC = 1;
			#5 A[15:0]= 16'd1; B[15:0]=16'd999; iniC = 1;
		end

	initial
		begin
			$monitor($time, ": A=%d B=%d Cin=%d, Sum=%d Carry=%d", A,B,iniC,Sum,Carry);
			$dumpfile("cla.vcd");
			$dumpvars;
		end

endmodule
