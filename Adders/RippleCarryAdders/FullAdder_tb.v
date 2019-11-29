`include "FullAdder.v"
module top;
reg A,B,Cin;
wire sum,carry;
FullAdder FA_O(A,B,Cin,sum,carry);
initial
begin
A=0;B=0;Cin=0;
#5 A=1;
#5 B=1;
#5 Cin=1;
#5 A=0;
end
initial
begin
$monitor($time,"A=%b,B=%b,Cin=%b,sum=%b,carry=%b",A,B,Cin,sum,carry);
$dumpfile("FullAdder.vcd");
$dumpvars;
end
endmodule
