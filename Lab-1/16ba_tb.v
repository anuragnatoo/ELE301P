`include "16ba.v"
module top;
reg [15:0] A,B;
wire [15:0] sum;
reg cin;
wire cout;
s16ba s16ba_0(A,B,cin,sum,cout);
initial
begin
A=16'd48;B=16'd36;cin=0;
#5 A=16'd25;
#5 A=16'd33;
#5 cin=1;
#5 B=16'd27;
#5 B=16'd5;
end
initial
begin
$monitor($time,"A=%d,B=%d,Cin=%d,sum=%d,carry=%d",A,B,cin,sum,cout);
$dumpfile("16ba.vcd");
$dumpvars;
end
endmodule

