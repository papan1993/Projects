//////Anmol Gautam - AXG190014 /// Soumyadeep Choudhury - SXC180056////////
#include <iostream>
#include <map>
#include <list>
#include <string>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <bitset>
#include <sstream>
#include <bits/stdc++.h>

#include <unistd.h>
#define GetCurrentDir getcwd

using namespace std;

/////////////////////////////////  utility class /////////////////////////////////
class utils
{
public:

    // variables
    list<list<int>> input_data_bits_list;

    string hex_2_binary(string& hex_value, int& file_type)
    {
        string binary_value;

        if (file_type == 1)
        {
            //number_bits = 32;
            stringstream ss_obj;
            int x;
            ss_obj << std::hex << hex_value;
            ss_obj >> x;
            cout << x << " " << int(hex_value[0])-48 << "\n";

        }
        else if (file_type == 2)
        {
            //number_bits = 16;
            stringstream ss_obj;
            ss_obj << hex << hex_value;
            unsigned temp_n;
            ss_obj >> temp_n;
            bitset<16> b(temp_n);
            binary_value = b.to_string();
        }
        if(file_type == 3)
        {

        }
        return binary_value;
    }

    void file_read(string& file_name, int& file_type)
    {
        ifstream file_op(file_name);
        string str_v;
        string binary_value_str;

        list<int> each_coef_sign_bits_list, each_coef_pot_bits_list, each_input_bits_list;

        while (getline(file_op, str_v)) {

            binary_value_str = hex_2_binary(str_v, file_type);

            if (file_type == 2)
            {
                //char const& each_bit;
                for (char const& each_bit: binary_value_str)
                {
                    int temp_bit;
                    temp_bit = (int) (each_bit);
                    temp_bit = temp_bit - 48;
                    each_input_bits_list.push_back(temp_bit);
                }

                input_data_bits_list.push_back(each_input_bits_list);
                each_input_bits_list.clear();
            }
        }
    }

};

//////////////////// Addition Function ////////////////////////////////////////
string add_str(string a, string b)
{
    int i;
    char cary = '0';
    string c[a.length()];
    for(i=a.length()-1;i>=0;i--)
    {
        if(cary=='0'&&a[i]=='0'&&b[i]=='0')
        {
            cary='0';
            c[i]='0';
        }
        else if(cary=='0'&&a[i]=='0'&&b[i]=='1')
        {
            cary='0';
            c[i]='1';
        }
        else if(cary=='0'&&a[i]=='1'&&b[i]=='0')
        {
            cary='0';
            c[i]='1';
        }
        else if(cary=='0'&&a[i]=='1'&&b[i]=='1')
        {
            cary='1';
            c[i]='0';
        }
        else if(cary=='1'&&a[i]=='1'&&b[i]=='1')
        {
            cary='1';
            c[i]='1';
        }
        else if(cary=='1'&&a[i]=='0'&&b[i]=='0')
        {
            cary='0';
            c[i]='1';
        }
        else if(cary=='1'&&a[i]=='0'&&b[i]=='1')
        {
            cary='1';
            c[i]='0';
        }
        else if(cary=='1'&&a[i]=='1'&&b[i]=='0')
        {
            cary='1';
            c[i]='0';
        }
        else if(cary=='1'&&a[i]=='1'&&b[i]=='1')
        {
            cary='1';
            c[i]='1';
        }
    }
    string ret_string;
    for (i =0; i < a.length(); i++)
    {
        ret_string = ret_string + c[i];
    }
    return ret_string;
}

/////////////////////////////////////////////////////////////////
bool check_index(list<int>& index_list, int& search_value)
{
    bool ret_flag = false;
    for (int const& ind_val : index_list)
    {
        if (ind_val == search_value)
        {
            ret_flag = true;
            break;
        }
    }

    return ret_flag;
}

//////// bin_string 2 hex ////
string GetHexFromBin(string sBinary)
{
    string rest("0x"),tmp,chr = "0000";
    int len = sBinary.length()/4;
    chr = chr.substr(0,len);
    sBinary = chr+sBinary;
    int i;
    for (i=0;i<sBinary.length();i+=4)
    {
        tmp = sBinary.substr(i,4);
        if (!tmp.compare("0000"))
        {
            rest = rest + "0";
        }
        else if (!tmp.compare("0001"))
        {
            rest = rest + "1";
        }
        else if (!tmp.compare("0010"))
        {
            rest = rest + "2";
        }
        else if (!tmp.compare("0011"))
        {
            rest = rest + "3";
        }
        else if (!tmp.compare("0100"))
        {
            rest = rest + "4";
        }
        else if (!tmp.compare("0101"))
        {
            rest = rest + "5";
        }
        else if (!tmp.compare("0110"))
        {
            rest = rest + "6";
        }
        else if (!tmp.compare("0111"))
        {
            rest = rest + "7";
        }
        else if (!tmp.compare("1000"))
        {
            rest = rest + "8";
        }
        else if (!tmp.compare("1001"))
        {
            rest = rest + "9";
        }
        else if (!tmp.compare("1010"))
        {
            rest = rest + "A";
        }
        else if (!tmp.compare("1011"))
        {
            rest = rest + "B";
        }
        else if (!tmp.compare("1100"))
        {
            rest = rest + "C";
        }
        else if (!tmp.compare("1101"))
        {
            rest = rest + "D";
        }
        else if (!tmp.compare("1110"))
        {
            rest = rest + "E";
        }
        else if (!tmp.compare("1111"))
        {
            rest = rest + "F";
        }
        else
        {
            continue;
        }
    }
    return rest;
}

////////  List_to_String Binary Conversion /////
string list_to_String_Conversion(list<int>& binary_value_list)
{
    string return_binary;
    for (int& int_bit : binary_value_list)
    {
        return_binary = return_binary + to_string(int_bit);
    }

    return return_binary;
}

//////////////////////////// Function to find two's complement ///////////////////////////////
string get_Twoscomplement(string str)
{
    int n = str.length();

    int i;
    for (i = n-1 ; i >= 0 ; i--)
        if (str[i] == '1')
            break;

    if (i == -1)
    {
        return '1' + str;
    }

    int k;
    for (k = i-1 ; k >= 0; k--)
    {
        //Just flip the values
        if (str[k] == '1')
            str[k] = '0';
        else
            str[k] = '1';
    }

    return str;;
}

/// Retrieve x[n-k]
list<int> retrieve_x_input(list<list<int>>& input_list, int& loc)
{
    int pos_counter = 1;
    list<int> retrieve_list;
    for (list<int>& each_input : input_list)
    {
        if (loc == pos_counter)
        {
            retrieve_list = each_input;
            break;
        }

        pos_counter++;
    }

    return retrieve_list;
}

/////// get directory ////
string get_current_dir()
{
    char buff[FILENAME_MAX]; //create string buffer to hold path
    GetCurrentDir( buff, FILENAME_MAX );
    string current_working_dir(buff);

    return current_working_dir;
}

/////// file path operation /////
string file_path_operation(string& file_path, int diff_val)
{
    bool path_flag;
    ifstream ifile;
    string final_file_path;

    ifile.open(file_path);
    string curr_dir = get_current_dir();

    if(ifile)
    {
        path_flag = true;
        final_file_path = file_path;
    }
    else
    {
        int total_len = curr_dir.length();
        int end_pos = total_len - 17;
        string new_file_path;

        //curr_dir = curr_dir.substr(0, end_pos);
        if (diff_val == 1)
        {
            new_file_path = curr_dir + '/' + file_path;
        }
        else if (diff_val == 2)
        {
            new_file_path = curr_dir + "/output_files/" + file_path;
	        return new_file_path;
        }

        ifile.open(new_file_path);

        if(ifile)
        {
            path_flag = true;
            final_file_path = new_file_path;
        }
        else
        {
            path_flag = false;
            final_file_path = "null";
        }

    }

    ifile.close();
    return final_file_path;
}

////////////////// main function /////////////
int main(int argc, char** argv)
{
    // Main Operation object class

    string coeff_file_path_m = argv[1];
    string input_file_path_m = argv[3];
    string rj_file_path_m = argv[2];
    string output_file_path_m = argv[4];

    ///////////// input and output files /////
    //int diff_file : 1 - input and 2 - output

    string arg_check_1 = file_path_operation(coeff_file_path_m, 1);
    if (arg_check_1 == "null")
    {
        cout<< " Wrong path input for : Coefficient File : Please refer to README file inside the Homework_4 folder ";
        exit(0);
    }
    string arg_check_2 = file_path_operation(input_file_path_m, 1);
    if (arg_check_2 == "null")
    {
        cout<< " Wrong path input for : Input File : Please refer to README file inside the Homework_4 folder ";
        exit(0);
    }
    string arg_check_3 = file_path_operation(rj_file_path_m, 1);
    if (arg_check_3 == "null")
    {
        cout<< " Wrong path input for : Rj File : Please refer to README file inside the Homework_4 folder ";
        exit(0);
    }
    string arg_check_4 = file_path_operation(output_file_path_m, 2);
    if (arg_check_4 == "null")
    {
        cout<< " Wrong path input for : Output File : Please refer to README file inside the Homework_4 folder ";
        exit(0);
    }

    cout << " --- MSDAP Project Task : Started ---- " << endl;

    /// inputs
    //string coeff_file_path = "/home/soumyadeep/Documents/semester_3/ASIC/Mid_term_projoect/hw_5/Homework_5/input_files/Coeff1.in";
    //string input_file_path = "/home/soumyadeep/Documents/semester_3/ASIC/Mid_term_projoect/hw_5/Homework_5/input_files/data1.in";
    //string rj_file_path = "/home/soumyadeep/Documents/semester_3/ASIC/Mid_term_projoect/hw_5/Homework_5/input_files/Rj1.in";

    int file_type_input = 2;

    // object class : utils
    utils obj;
    obj.file_read(arg_check_2, file_type_input);

    list<list<int>> input_data_bits_list = obj.input_data_bits_list;

    // compute coefficients //
    list<int> coeff_pot_index;
    list<int> coeff_pot_index_sign;  // assign 1: for +ve and 0 : for -ve
    map<int, list<int>> coefficient_matrix_map;

    //////////////////////////////// Coefficient Input Operation  ///////////////
    int coeff[200][2];
    ifstream file_op(arg_check_1);
    string temp;
    int index = 0;

    while(!file_op.eof())
    {
        int x;
        file_op >> temp;
        stringstream ss_obj;
        ss_obj << std::hex << temp.substr(1,temp.length());
        ss_obj >> x;
        coeff[index][0] = int(temp[0])-48;
        coeff[index][1] = x;
        index = index + 1;
    }

    int rj[16];
    index = 0;
    ifstream file_op2(arg_check_3);
    while(!file_op2.eof())
    {
        int x;
        file_op2 >> temp;
        stringstream ss_obj;
        ss_obj << std::hex << temp;
        ss_obj >> x;
        rj[index] = x;
        index = index + 1;
    }

    /////////////////////////////////////////////////////////////

    ////// Extending input to 40-bit ////////
    list<list<int>> input_data_40bit_final;
    list<int> input_40bit_sub;

    ///list<int> const& each_input_row;
    for (list<int> const& each_input_row : input_data_bits_list)
    {
        int add_counter = 1;
        for (int const& each_bit : each_input_row)
        {
            if (add_counter == 1)
            {
                int i;
                for(i=1; i < 10; i++)
                {
                    input_40bit_sub.push_back(each_bit);
                    add_counter ++;
                }
            }
            else
            {
                input_40bit_sub.push_back(each_bit);
                add_counter ++;
            }
        }

        input_data_40bit_final.push_back(input_40bit_sub);
        input_40bit_sub.clear();
    }
    /////////////////////////////////////////////////////////////

    //// MSDAP operation main ########

    int n = 1; // counter for each x(n)
    list<string> output_file_list;

    ////vectorize the input  for now take input as x
    for (list<int> const& each_x : input_data_bits_list)
    {
        string sum_final="";
        int k = 0;
        int ucount = 0;

        for(int i=0; i < 16; i++)
        {
            string u = "";
            for(int j = 0;  j<rj[i]; j++)
            {
                if(n - coeff[k][1] > 0)
                {
                    int retrieve_pos = n-coeff[k][1];
                    list<int> input_var = retrieve_x_input(input_data_40bit_final, retrieve_pos);
                    string var = list_to_String_Conversion(input_var);

                    if(u == "")
                    {
                        if(coeff[k][0] == 0)
                        {
                            u = list_to_String_Conversion(input_var);
                        }
                        else if(coeff[k][0] == 1)
                        {
                            u = get_Twoscomplement(var);
                        }
                    }
                    else
                    {
                        if(coeff[k][0] == 0)
                        {
                            u = add_str(u, var);
                        }

                        else
                        {
                            string twos_complement = get_Twoscomplement(var);
                            u = add_str(u, twos_complement);
                        }
                    }
                }

                k= k + 1;

            }
            ucount = ucount + 1;
            if(sum_final == "" && u != "")
            {
                sum_final=u;
                int x ;
                for(x=0; x<ucount-1; x++)
                {
                    sum_final=sum_final + "0";
                }
                ucount = 0;

            }
            else if(sum_final != "" && u != "")
            {
                int x;
                for(x=0; x<ucount; x++)
                {
                    sum_final = sum_final[0] + sum_final;
                }
                string temp = u;
                while (sum_final.length() > temp.length())
                {
                    temp = temp + "0";
                }

                sum_final = add_str(sum_final,temp);
                ucount = 0;

            }

        }

        while(sum_final.length() <40)
        {
            sum_final = sum_final[0] + sum_final;
        }

        string output_str = GetHexFromBin(sum_final);
        if (output_str.length() < 5)
        {
            output_str = "0000000000";
        }
        else
        {
            output_str = output_str.substr(3, 13);
        }
        cout << n << " : " << output_str << "\n";
        output_file_list.push_back(output_str);
        n = n+1;
    }

    /////// Writing to output file ///
    ofstream myfile (arg_check_4);
    if (myfile.is_open())
    {
        for (string& each_line : output_file_list)
        {
            myfile << each_line << "\n";
        }
        myfile.close();
    }
    else
    {
        cout << "Unable to open file";
    }

    ////////////////////////////////////////////////////////////
    cout << " --- MSDAP Project Task : Finished ---- " << endl;
    return 0;
}
