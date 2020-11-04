# This is a code for SAT Solver Automation for Camouflouge Gate Detection

# In Keys , 0 refer ---> NAND Gate and 1 refer ---> NOR Gate 

# To change the keys for Gates or Gate Type, you can edit the code in "Automation_SAT.py"

# To run the code, follow the steps :-

1) Download the whole folder - "SAT_Solver_Research" in a directory. and also download the benchmark_files
2) Through command line -> $ cd ../SAT_Solver_Research/
3) Go to the executable files -> $ cd ../SAT_solver_research/host15-logic-encryption/bin/ or download host15-logic-encryption/ from github : simulator
4) Then Run --> $ python3 main.py "originalbenchfile.bench"
5) It will ask for %(percentage) of gates to be camaouflouged -- 20 or 30 or 10 (e.g)
6) It will give you the keys and a file will be generated with the keys referred gates in the "bin" folder.
