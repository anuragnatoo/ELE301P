`include "e8ba.v"
module top;
reg [7:0] A,B;
wire [7:0] sum;
reg cin;
wire carry;
e8ba e8ba_0(A,B,cin,sum,carry);
initial
begin
A=8'd24;B=8'd3;cin=0;
#10 A=8'd16;
#10 B=8'd16;
#10 cin=1;
#10 A=8'd30;
end
initial
begin
$monitor($time,"A=%d,B=%d,cin=%d,sum=%d,carry=%d",A,B,cin,sum,carry);
$dumpfile("e8ba.vcd");
$dumpvars;
end
endmodule
