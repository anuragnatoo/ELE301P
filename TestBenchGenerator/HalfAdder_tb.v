`include "HalfAdder.v"
module top;
reg a, b;
wire sum, ca;
HalfAdder  m0(a,b,sum, ca);
initial begin
	a=1'b0 ; b=1'b0 ; 
	#5 a=1'b0 ; b=1'b1 ; 
	#5 a=1'b1 ; b=1'b0 ; 
	#5 a=1'b1 ; b=1'b1 ; 
end

initial begin
$monitor ($time, ": a=%b b=%b sum=%b  ca=%b ",a,b,sum, ca);
$dumpfile("HalfAdder.vcd");
$dumpvars;
end

endmodule