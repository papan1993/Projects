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

//////////////////////////////////////////  addition subtraction class /////////////////
class bin
{
public:
    char a[40],b[40],c[40];
    string return_data;
    int s1,s2,m;
    char cary;

    bin(char& cary)
    {
        this->cary = cary;
        s1=0;s2=0;m=0;
        int i;
        for(i=0;i<40;i++)
        {
            a[i]='0';
            b[i]='0';
            c[i]='0';
        }
    }

    string feedback()
    {
        string ret_string;
        int i;
        for (i =0; i < 40; i++)
        {
            ret_string = ret_string + c[i];
        }

        return ret_string;
    }

    void getdata(string& m, string& n)
    {
        s1=40;
        s2=40;
        strcpy(a, m.c_str());
        strcpy(b, n.c_str());
    }

    void add();
};

void bin::add()
{
    int i;
    for(i=39;i>=0;i--)
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
}

/////////////////////////////////  utility class /////////////////////////////////
class utils
{
public:

    // variables
    list<list<int>> coeff_sign_bits_list;
    list<list<int>> coeff_pot_bits_list;
    list<list<int>> input_data_bits_list;

    string hex_2_binary(string& hex_value, int& file_type)
    {
        string binary_value;

        if (file_type == 1)
        {
            //number_bits = 32;
            stringstream ss_obj;
            ss_obj << hex << hex_value;
            unsigned temp_n;
            ss_obj >> temp_n;
            bitset<32> b(temp_n);
            binary_value = b.to_string();
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

        return binary_value;
    }

    void file_read(string& file_name, int& file_type)
    {
        ifstream file_op(file_name);
        string str_v;
        string binary_value_str;

        list<int> each_coef_sign_bits_list, each_coef_pot_bits_list, each_input_bits_list;

        while (getline(file_op, str_v)) {
            //cout << " hex value ---> " << str_v << "\n";
            binary_value_str = hex_2_binary(str_v, file_type);
            //cout << " binary ---> " << binary_value_str << endl;

            if (file_type == 1)
            {
                int half_count = 1;
                //char const& each_bit;
                for (char const& each_bit : binary_value_str)
                {
                    int temp_bit;
                    temp_bit = (int) (each_bit);
                    temp_bit = temp_bit - 48;
                    if (half_count > 16) {
                        each_coef_pot_bits_list.push_back(temp_bit);
                    } else if (half_count <= 16) {
                        each_coef_sign_bits_list.push_back(temp_bit);
                    }
                    half_count = half_count + 1;
                }

                coeff_pot_bits_list.push_back(each_coef_pot_bits_list);
                coeff_sign_bits_list.push_back(each_coef_sign_bits_list);

                each_coef_pot_bits_list.clear();
                each_coef_sign_bits_list.clear();
            }
            else if (file_type == 2)
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

/////////////////////////////////////////////////////////////////
bool check_index(list<int>& index_list, int& search_value)
{
    bool ret_flag = false;
    //int const& ind_val;
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
    //int& int_bit;
    for (int& int_bit : binary_value_list)
    {
        return_binary = return_binary + to_string(int_bit);
    }

    return return_binary;
}

///////////////////////////////////////////////////
list<int> right_shift_operation(list<int>& operation_list, int& num_shifts)
{
    list<int> right_shifted_list;
    int length_list = 40;

    list<int> inside;
    inside = operation_list;

    int i;
    for (i = 0; i < num_shifts; i++)
    {
        int iterate_flag = 0;
        //int& each_bit;
        for (int& each_bit : inside)
        {
            if (iterate_flag == length_list)
            {
                break;
            }
            else if (iterate_flag == 0)
            {
                right_shifted_list.push_back(each_bit);
                right_shifted_list.push_back(each_bit);
                iterate_flag = iterate_flag + 2;
            } else{
                right_shifted_list.push_back(each_bit);
                iterate_flag = iterate_flag + 1;
            }

        }

        string sh = list_to_String_Conversion(right_shifted_list);
        string sh_hex = GetHexFromBin(sh);
        inside.clear();
        inside = right_shifted_list;
        right_shifted_list.clear();
    }

    return inside;
}

/////////////////////////////////////////////////////////////////////////////////////
list<int> compute_coeffcient(list<int>& ind_list, list<int>& sign_list)
{
    list<int> final_value;
    auto it1 = ind_list.begin();
    auto it2 = sign_list.begin();

    for (; it1 != ind_list.end() && it2 != sign_list.end(); ++it1, ++it2)
    {
        int temp_copy = *it1;
        if (*it2 == 0)
        {
            temp_copy = (-1)*temp_copy;
        }

        final_value.push_back(temp_copy);
    }

    return final_value;
}

// Function to find two's complement
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
    //list<int>& each_input;
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
        //ifile.close();
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
    string input_file_path_m = argv[2];
    string output_file_path_m = argv[3];

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
    string arg_check_3 = file_path_operation(output_file_path_m, 2);
    if (arg_check_3 == "null")
    {
        cout<< " Wrong path input for : Output File : Please refer to README file inside the Homework_4 folder ";
        exit(0);
    }

    cout << " --- MSDAP Project Task : Started ---- " << endl;

    /// inputs
    //string coeff_file_path = "/home/soumyadeep/Documents/semester_3/ASIC/Mid_term_projoect/hw_4/ASIC_project_MSDAP/coeff.in";
    //string input_file_path = "/home/soumyadeep/Documents/semester_3/ASIC/Mid_term_projoect/hw_4/ASIC_project_MSDAP/data1.in";
    int file_type_coeff = 1; // 1 - coeffcient , 2 - data and 3 - output
    int file_type_input = 2;

    // object class : utils
    utils obj;
    obj.file_read(arg_check_1, file_type_coeff);
    obj.file_read(arg_check_2, file_type_input);


    list<list<int>> coeff_sign_bits_list = obj.coeff_sign_bits_list;
    list<list<int>> coeff_pot_bits_list = obj.coeff_pot_bits_list;
    list<list<int>> input_data_bits_list = obj.input_data_bits_list;

    // compute coefficients //
    list<int> coeff_pot_index;
    list<int> coeff_pot_index_sign;  // assign 1: for +ve and 0 : for -ve
    map<int, list<int>> coefficient_matrix_map;

    int coeff_matrix_index = 0;
    //auto const& each_pot_coeff;
    for (auto const& each_pot_coeff : coeff_pot_bits_list)
    {
        int loc_pot = 1;
        //int pot_bit;
        for (int pot_bit : each_pot_coeff)
        {
            if (pot_bit == 1)
            {
                coeff_pot_index.push_back(loc_pot);
            }
            loc_pot = loc_pot + 1;
        }

        ///////// matching
        int breaker_count = 0;
        //auto const& each_sign_coeff;
        for (auto const& each_sign_coeff : coeff_sign_bits_list)
        {
            if (breaker_count == coeff_matrix_index)
            {
                int loc_sign = 1;
                bool check_flag = false;
                //int const& sign_bit;
                for (int const& sign_bit : each_sign_coeff)
                {
                    check_flag = check_index(coeff_pot_index, loc_sign);
                    if (check_flag)
                    {
                        int temp_sign_bit = sign_bit;
                        int sign;
                        if (temp_sign_bit == 1) {
                            sign = 0;
                            coeff_pot_index_sign.push_back(sign);
                        } else if (temp_sign_bit == 0) {
                            sign = 1;
                            coeff_pot_index_sign.push_back(sign);
                        }
                    }

                    loc_sign = loc_sign + 1;
                }
            }
            breaker_count = breaker_count + 1;
        }

        list<int> each_coeff_value = compute_coeffcient(coeff_pot_index, coeff_pot_index_sign);
        coefficient_matrix_map.insert(pair<int, list<int>>(coeff_matrix_index, each_coeff_value));
        coeff_matrix_index = coeff_matrix_index + 1;

        coeff_pot_index.clear();
        coeff_pot_index_sign.clear();
    }

    /////////////////////////////////////////////////////////////

    ////// Extending input to 40-bit ////////
    list<list<int>> input_data_40bit_final;
    list<int> input_40bit_sub;

    ///list<int> const& each_input_row;
    for (list<int> const& each_input_row : input_data_bits_list)
    {
        int add_counter = 1;
        //int const& each_bit;
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

        /// add 16 bits : 0
        int i;
        for (i = 0; i < 16; i++)
        {
            int temp_bit = 0;
            input_40bit_sub.push_back(temp_bit);
        }

        input_data_40bit_final.push_back(input_40bit_sub);
        input_40bit_sub.clear();
    }
    /////////////////////////////////////////////////////////////

    //// MSDAP operation main ########

    int n = 1; // counter for each x(n)
    list<string> output_file_list;

    ////vectorize the input  for now take input as x
    //list<int> const& each_x;
    for (list<int> const& each_x : input_data_bits_list)
    {
        string sum_final;
        char cary_final = '0';
        map<int, list<int>>::iterator it = coefficient_matrix_map.begin();
        int k = 0; // counter for h(k)

        while (it != coefficient_matrix_map.end())
        {
            // Accessing KEY from element pointed by it.
            //int k = it->first;
            // Accessing VALUE from element pointed by it.
            list<int> each_coeff = it->second;

            if(n-k > 0)
            {
                string sum;
                char cary = '0';

                int retrieve_pos = n-k;
                list<int> input_sum_var = retrieve_x_input(input_data_40bit_final, retrieve_pos);

                //int& each_coeff_s;
                for(int& each_coeff_s : each_coeff)
                {
                    if(each_coeff_s < 0)
                    {
                        int each_coeff_send = each_coeff_s * (-1);
                        string before_shift = list_to_String_Conversion(input_sum_var);
                        string before_hex = GetHexFromBin(before_shift);
                        list<int> right_shift_value = right_shift_operation(input_sum_var, each_coeff_send);
                        string rshift_str = list_to_String_Conversion(right_shift_value);
                        string hex_data_1 = GetHexFromBin(rshift_str);
                        string twos_comp_str = get_Twoscomplement(rshift_str);
                        string hex_data_2 = GetHexFromBin(twos_comp_str);
                        if (sum.empty())
                        {
                            sum = twos_comp_str;
                        }
                        else
                        {
                            bin obj_1(cary);
                            obj_1.getdata(sum, twos_comp_str);
                            obj_1.add();
                            sum = obj_1.feedback();
                            //cary = obj_1.cary;
                        }

                    }
                    else
                    {
                        list<int> right_shift_value = right_shift_operation(input_sum_var, each_coeff_s);
                        string rshift_str = list_to_String_Conversion(right_shift_value);

                        if (sum.empty())
                        {
                            sum = rshift_str;
                        }
                        else
                        {
                            bin obj_1(cary);
                            obj_1.getdata(sum, rshift_str);
                            obj_1.add();
                            sum = obj_1.feedback();
                            //cary = obj_1.cary;
                        }

                    }
                }

                if (sum_final.empty())
                {
                    sum_final = sum;
                }
                else
                {
                    bin obj_2(cary_final);
                    obj_2.getdata(sum_final, sum);
                    obj_2.add();
                    sum_final = obj_2.feedback();
                    //cary_final = obj_2.cary;
                }

                input_sum_var.clear();
            }

            it++;
            k++;
        }

        /// hexa conversion ///
        string sum_hex = GetHexFromBin(sum_final);
        sum_hex = sum_hex.substr(3, 13);
        output_file_list.push_back(sum_hex);
        cout << "output : " << n << " = " << sum_hex << "\n";
        n++;
    }

    /////// Writing to output file ///
    ofstream myfile (arg_check_3);
    if (myfile.is_open())
    {
        //string& each_line;
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
