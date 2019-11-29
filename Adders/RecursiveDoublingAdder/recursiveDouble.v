`include "FullAdder.v"
module CLA(A, B, Sum, iniC, Carry);
	input [15:0] A,B;
	output [15:0] Sum;
	output Carry;
	input iniC;
	
	reg [1:0] kgp[0:15];//Each location has two bits
	reg [15:0] Cin;//Input carry after final stage
	
	reg [1:0] kgp2[0:15];//Final kpg array
	reg [1:0] kgp_t1[0:15];//Temporary arrays for changing
	reg [1:0] kgp_t2[0:15];
	reg [5:0] i,j,k,m,n,o;//Loop variables
	reg [1:0] access, inaccess1, inaccess2;//Two bit vectors for each location

	//Bit Zero requires different calculations.
	//Using k maps we get equations for bit 0
	always @* begin
	
		//bit0
		//access = kgp[0];
		access[1] = A[0]&B[0] | A[0]&iniC | B[0]&iniC ;
		access[0] = A[0]&B[0] | A[0]&iniC | B[0]&iniC ;
		kgp[0] = access;

		
		o = 6'b000001;//Loop variable---6 bit 16		
		//bit i
		/*
		Kpg calculation takes place here for all the 15 bits
		*/
		while(o<=15)
		begin
			//access = kgp[o];
			access[1] = A[o] & B[o];
			access[0] = A[o] | B[o];
			kgp[o] = access;

			o=o+1;
		end
		$display("%b %b %b %b %b %b %b %b %b %b %b %b %b %b %b %b",kgp[15],kgp[14],kgp[13],kgp[12],kgp[11],kgp[10],kgp[9],kgp[8],kgp[7],kgp[6],kgp[5],kgp[4],kgp[3],kgp[2],kgp[1],kgp[0]);
		
		for(n=0; n<=15; n=n+1)
		begin
			kgp2[n] = kgp[n];//Final array stores the copy of first kpg array initially
			kgp_t2[n] = kgp[n];
			kgp_t1[n] = kgp[n];
		end
		i=6'b000001;//Loop variable for calculation
		//----Calculation takes place as step-i,step-i+2,step-i+4,..step-i+8
		
		while(i<16)//i is number of shifts 
			begin
				j=i;//J is used to calculate along the whole array the prefix sum of j and j-i
				while(j<16)
					begin
						inaccess1 = kgp_t1[j-i];//Each bit calculations
						inaccess2 = kgp_t2[j];
						access[1] = inaccess1[1] & inaccess2[0] | inaccess2[1];
						access[0] = inaccess1[0] & inaccess2[0] | inaccess2[1];
						kgp2[j] = access;

						j=j+1;
					end

				$display(" Step %d:  %b %b %b %b %b %b %b %b %b %b %b %b %b %b %b %b\n",i, kgp2[15],kgp2[14],kgp2[13],kgp2[12],kgp2[11],kgp2[10],kgp2[9],kgp2[8],kgp2[7],kgp2[6],kgp2[5],kgp2[4],kgp2[3],kgp2[2],kgp2[1],kgp2[0]);
				
				for(k=0; k<=15; k=k+1)
				begin
					kgp_t1[k] = kgp2[k];//Temporary arrays for the next stage
					kgp_t2[k] = kgp2[k];
				end

				i=i<<1;

			end
		
		m = 6'b000000;
		while(m<16)
			begin
				access = kgp2[m];
				Cin[m] = access[0]&access[1];
				m=m+1;
			end
		
		$display("%b %b %b %b %b %b %b %b %b %b %b %b %b %b %b %b", kgp2[15],kgp2[14],kgp2[13],kgp2[12],kgp2[11],kgp2[10],kgp2[9],kgp2[8],kgp2[7],kgp2[6],kgp2[5],kgp2[4],kgp2[3],kgp2[2],kgp2[1],kgp2[0]);
	end

	/*
	Sums are calculated below
	*/
	FullAdder f1(A[0],B[0],iniC,Sum[0]);
	FullAdder f2(A[1],B[1],Cin[0],Sum[1]);
	FullAdder f3(A[2],B[2],Cin[1],Sum[2]);
	FullAdder f4(A[3],B[3],Cin[2],Sum[3]);
	FullAdder f5(A[4],B[4],Cin[3],Sum[4]);
	FullAdder f6(A[5],B[5],Cin[4],Sum[5]);
	FullAdder f7(A[6],B[6],Cin[5],Sum[6]);
	FullAdder f8(A[7],B[7],Cin[6],Sum[7]);
	FullAdder f9(A[8],B[8],Cin[7],Sum[8]);
	FullAdder f10(A[9],B[9],Cin[8],Sum[9]);
	FullAdder f11(A[10],B[10],Cin[9],Sum[10]);
	FullAdder f12(A[11],B[11],Cin[10],Sum[11]);
	FullAdder f13(A[12],B[12],Cin[11],Sum[12]);
	FullAdder f14(A[13],B[13],Cin[12],Sum[13]);
	FullAdder f15(A[14],B[14],Cin[13],Sum[14]);
	FullAdder f16(A[15],B[15],Cin[14],Sum[15]);
	
	assign Carry = Cin[15];
		
endmodule
