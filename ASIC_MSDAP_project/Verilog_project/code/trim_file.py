
def main_operation(file_in):
    file1 = open(file_in, 'r')
    input_arr = file1.readlines()
    file1.close()

    final_result_left = []
    final_result_right = []

    ### seperate operations
    for i in range(0, len(input_arr), 1):
        temp_str = input_arr[i]

        if (temp_str[0] != '/'):
            str_1 = temp_str.split(" ")
            str_left = str_1[3]
            str_right = str_1[9]

            final_result_left.append(str_left)
            final_result_right.append(str_right)
            #print("check")


    ### GENERATE result file
    file_strip = file_in.split(".")
    file_new = file_strip[0]
    file_out_L = file_new + str('_Left') + str('.in')
    file_out_R = file_new + str('_Right') + str('.in')

    count = 0
    file2 = open(file_out_L, "w")
    for line in final_result_left:
        if (count == 0):
            temp_line = '// Left Rj values'
            file2.write(temp_line)
            file2.write("\n")

        elif (count == 16):
            temp_line = '// Left Coefficient values'
            file2.write(temp_line)
            file2.write("\n")

        if (count == 528):
            temp_line = '// Left Input values'
            file2.write(temp_line)
            file2.write("\n")

        file2.write(line)
        file2.write("\n")
        count = count + 1

    file2.close()

    count = 0
    file3 = open(file_out_R, "w")
    for line in final_result_right:
        if (count == 0):
            temp_line = '// Right Rj values'
            file3.write(temp_line)
            file3.write("\n")

        elif (count == 16):
            temp_line = '// Right Coefficient values'
            file3.write(temp_line)
            file3.write("\n")

        if (count == 528):
            temp_line = '// Right Input values'
            file3.write(temp_line)
            file3.write("\n")

        file3.write(line)
        file3.write("\n")
        count = count + 1

    file3.close()


if __name__ == '__main__':
    file1 = "data1.in"
    file2 = "data2.in"
    main_operation(file1)
    main_operation(file2)