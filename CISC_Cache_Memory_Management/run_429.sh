#!/bin/bash

#429.mcf shell

export GEM5_DIR=/home/soumyadeep/gem5
export M5_DIR=/home/soumyadeep/Project1_SPEC-master/429.mcf/final_project/m5out
export BENCHMARK=./src/benchmark
export ARGUMENT=./data/inp.in

SPACE="_"

for i in 64kB 128kB 256kB #################  L1 size (both data and instruction)
do
	for j in 256kB 512kB 1MB 2MB #################  L2 size 
	do
		for k in 32 64  ########## Cacheline size 
		do
			for m in 1 2 4  ############# L1 associativity
			do
				for n in 1 2 4 ############# L2 associativity
				do
					for cpu in TimingSimpleCPU MinorCPU DerivO3CPU
					do
						time $GEM5_DIR/build/X86/gem5.opt -d $M5_DIR$SPACE$i$SPACE$j$SPACE$k$SPACE$m$SPACE$n$SPACE$cpu 
						$GEM5_DIR/configs/example/se.py -c $BENCHMARK -o $ARGUMENT -I 500000000 --cpu-type=$cpu --caches --l2cache --l1d_size=$i 
						--l1i_size=$i --l2_size=$j --l1d_assoc=$m --l1i_assoc=$m --l2_assoc=$n --cacheline_size=$k
					done
				done
			done
		done
	done
done
