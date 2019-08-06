module FullAdder(A,B,Cin,sum,carry);
input A,B,Cin;
output sum,carry;
assign sum=A^B^Cin;
assign carry=(A&B)|(B&Cin)|(A&Cin);
endmodule

