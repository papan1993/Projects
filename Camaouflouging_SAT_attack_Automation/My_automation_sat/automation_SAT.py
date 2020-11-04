import sys
import pickle
import os

##################################################################################################################
##################################################################################################################

def modify_gatelist(edit_line, satkey):

	camaflouge_gate_main = edit_line[0]
	edit_segment = edit_line[1]
	edit_segment = edit_segment.split(',')
	print(camaflouge_gate_main)

	##################################################################################

	part_1 = edit_segment[0]
	part_1 = part_1.strip(" ")
	part_1 = part_1.split('(')
	gate_main_1 = part_1[1]
	print(gate_main_1)

	##################################################################################

	part_2 = edit_segment[1]
	part_2 = part_2.strip(" ")
	part_2 = part_2.split(')')
	gate_main_2 = part_2[0]
	print(gate_main_2)

	##################################################################################

	update_string_list = []
	change_str_1 = camaflouge_gate_main + str('new1$enc')
	modify_string_1 = change_str_1 + str(' = NAND(') + gate_main_1 + str(', ') + gate_main_2 + str(')')
	update_string_list.append(modify_string_1)
	change_str_2 = camaflouge_gate_main + str('new2$enc')
	modify_string_2 = change_str_2 + str(' = NOR(') + gate_main_1 + str(', ') + gate_main_2 + str(')')
	update_string_list.append(modify_string_2)
	modify_string_3 = camaflouge_gate_main + str(' = MUX(') + satkey + str(', ') + change_str_1 + str(', ') + change_str_2 + str(')')
	update_string_list.append(modify_string_3)

	return update_string_list

##################################################################################################################
##################################################################################################################

def camaflouge_gatelist_edit_function(input_list, logic_list, camaflouge_gate, keyinput):

	final_logic_list = []
	logic_list_break = []

	satkey = 'keyinput' + str(keyinput)
	input_update_string = 'INPUT(' + satkey + str(')')
	input_list.append(input_update_string)

	########################################################

	for i in range(0, len(logic_list), 1):
		temp = logic_list[i]
		break_value = temp.split('=')
		break_value[0] = break_value[0][:-1]
		logic_list_break.append(break_value)

	loc = None

	for i in range(0, len(logic_list_break), 1):
		temp_new = logic_list_break[i]
		check_temp = temp_new[0]
		if (camaflouge_gate == check_temp):
			loc = i
			print("location---", loc)

	###############################################################

	if(loc == 0):
		edit_line = logic_list_break[loc]
		modified_list = modify_gatelist(edit_line, satkey)

		for k in range(0, len(modified_list), 1):
			final_logic_list.append(modified_list[k])

		for i in range(1, len(logic_list), 1):
			final_logic_list.append(logic_list[i])

		print("case 1")

	####################################################################

	elif(loc == len(logic_list_break)-1):
		edit_line = logic_list_break[loc]
		modified_list = modify_gatelist(edit_line, satkey)

		for i in range(0, len(logic_list)-1, 1):
			final_logic_list.append(logic_list[i])

		for k in range(0, len(modified_list), 1):
			final_logic_list.append(modified_list[k])

		print("case 2")

	##################################################################

	else:
		edit_line = logic_list_break[loc]
		modified_list = modify_gatelist(edit_line, satkey)

		for i in range(0, loc, 1):
			final_logic_list.append(logic_list[i])

		for k in range(0, len(modified_list), 1):
			final_logic_list.append(modified_list[k])

		for j in range(loc+1, len(logic_list), 1):
			final_logic_list.append(logic_list[j])

		print("case 3")

	###################################################################

	return final_logic_list, input_list

##################################################################################################################
##################################################################################################################

def stripping_function(main_netlist):

	input_gates_list = []
	output_gates_list = []
	logic_gates_list = []

	for i in range(0, len(main_netlist), 1):

		temp = main_netlist[i]
		set_str = temp.split('(')

		if(set_str[0] == 'INPUT'):
			input_gates_list.append(main_netlist[i])

		elif(set_str[0] == 'OUTPUT'):
			output_gates_list.append(main_netlist[i])

		else:
			logic_gates_list.append(main_netlist[i])

	return input_gates_list, output_gates_list, logic_gates_list

##################################################################################################################
##################################################################################################################

if __name__ == '__main__':
	
	store_netlist = []
	main_netlist = []
	gates_list = []
	camaflouge_gatelist = []

	###############################################

	#with open(sys.argv[1], 'r') as f:
	#	while True:
	#		contents = f.readline()
	#		store_netlist.append(contents)
	#		if not contents:
	#			break

	##################################################

	f = open("test_orginal.bench", 'r')
	while True:
		contents = f.readline()
		store_netlist.append(contents)
		if not contents:
			break
	f.close()

	fh = open("gates_list.txt", 'r')
	while True:
		contents_gate = fh.readline()
		gates_list.append(contents_gate)
		if not contents_gate:
			break
	fh.close()

	##################################################

	store_netlist.pop()
	for i in range(0, len(store_netlist), 1):
		main_netlist.append(store_netlist[i][:-1])

	gates_list.pop()
	for i in range(0, len(gates_list), 1):
		camaflouge_gatelist.append(gates_list[i][:-1])

	##################################################

	input_gates_list, output_gates_list, logic_gates_list = stripping_function(main_netlist)

	##################################################

	for i in range(0, len(camaflouge_gatelist), 1):
		temp = camaflouge_gatelist[i]
		keyinput = i + 1
		logic_gates_list, input_gates_list = camaflouge_gatelist_edit_function(input_gates_list, logic_gates_list, temp, keyinput)

	########################################################

	final_encrypted_netlist = []

	for i in range(0 ,len(input_gates_list), 1):
		final_encrypted_netlist.append(input_gates_list[i])

	for j in range(0, len(output_gates_list), 1):
		final_encrypted_netlist.append(output_gates_list[j])

	for k in range(0, len(logic_gates_list), 1):
		final_encrypted_netlist.append(logic_gates_list[k])

	############################################################

	print("################################")
	for m in range(0, len(final_encrypted_netlist), 1):
		print(final_encrypted_netlist[m])

	############################################################

	with open('sat_automation_encrypted.bench', 'w') as filehandle:
		for listitem in final_encrypted_netlist:
			filehandle.write('%s\n' % listitem)

	############################################################

	os.system('cd /home/soumyadeep/Documents/semester_1/research/SAT_solver_research/host15-logic-encryption/bin/')
	os.system('./sld /home/soumyadeep/Documents/semester_1/research/SAT_solver_research/My_automation_sat/sat_automation_encrypted.bench /home/soumyadeep/Documents/semester_1/research/SAT_solver_research/My_automation_sat/test_orginal.bench > /home/soumyadeep/Documents/semester_1/research/SAT_solver_research/My_automation_sat/output.txt')