# ELE301P
VLSI System Design Practice Lab 

## Contents
* Verilog
  * Adders:
    * Ripple Carry Adders: 4 bit,8 bit,16 bit,32 bit and 64 bit Ripple Carry Adder implemented in Verilog HDL
    * Carry Save Adder: A 16 bit Recursive Doubling Adder implemented in Verilog HDL
* Python
  * Test Bench Generator: A python application which generates a test bench of a given verilog file
    * To RUN the file : `python3 tbgen.py filename.v`
    * The output is stored as `filename_tb.v`
    * Make sure that the verilog file is in the same folder as the tbgen.py
    * ISCAS Benchmark Verilog files are taken as input
    * For convenience the inputs and outputs are placed in different folders. But while compiling they need to be in the same folder.
  * Activity Factor Calculator: A python application which calculates the activity factors of the output elements and lists them down in a text file
    * To RUN the file : `python3 da2.py filename.v`
    * The output is stored as `filename.txt`
    * Make sure that the verilog and the python files are in the same folder
    * ISCAS Benchmark Verilog files are taken as inputs
    * For convenience the inputs and outputs are placed in different folders. But while compiling they need to be in the same folder.
