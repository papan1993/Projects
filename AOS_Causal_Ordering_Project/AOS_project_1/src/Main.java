import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Map;

public class Main
{
    public static void main(String[] args)
    {
        // Starting Class for project_1 : AOS

        // input
        //System.out.println(args[0]);
        String File_path = args[0];
        int Device_id = Integer.parseInt(args[1]);

        // testing input
        //String File_path = "Config.dat";
        //int Device_id = 1;

        // Call Comm Channel
        Comm_Channel comm_obj = new Comm_Channel(File_path, Device_id);

        // Call Synchronizer
        Synchronizer synch_obj = new Synchronizer(comm_obj);

        // tell this communication channel about synchronizer object
        comm_obj.setMsg_hand(synch_obj);

        // Call algorithm and Eccentricity
        synch_obj.synchronizer_algorithm();

        // Calculate Eccentricity of the Node
        int eccentricity_final_value = 0;
        int nodes_count = 0;

        // Writing To a file
        String dev_id = Integer.toString(Device_id);
        int file_path_len = File_path.length() - 3;
        String file_path_substr = File_path.substring(0, file_path_len-1);
        String output_file_name = file_path_substr + "-" + dev_id + ".dat";

        try
        {
            FileWriter myFile_Obj = new FileWriter(output_file_name);

            // ###################################################

            System.out.print(" ----- Final Eccentricity Table for Node id : " + dev_id + " ------- \n");
            String out_1 = "\n ----- Final Eccentricity Table for Node id : " + dev_id + " ------- \n\n";
            myFile_Obj.write(out_1);
            for (Map.Entry<Integer, ArrayList<Integer>> each_entry : synch_obj.Final_table_map.entrySet())
            {
                int each_round = each_entry.getKey();
                String each_round_str = Integer.toString(each_round);
                System.out.print("K-Hop -> " + each_round_str + " : ");
                String out_2 = "K-Hop -> " + each_round_str + " : ";
                myFile_Obj.write(out_2);

                ArrayList<Integer> each_row = each_entry.getValue();

                for (int i =0; i < each_row.size(); i++)
                {
                    int temp_value = each_row.get(i);
                    String temp_value_str;
                    if (temp_value == -1)
                    {
                        temp_value_str = " ";
                    }
                    else
                    {
                        temp_value_str = Integer.toString(temp_value);
                        nodes_count = nodes_count + 1;

                        if (nodes_count == File_Reader.Number_nodes)
                        {
                            eccentricity_final_value = each_round;
                        }
                    }

                    System.out.print(temp_value_str);
                    myFile_Obj.write(temp_value_str);
                    System.out.print(" ");
                    myFile_Obj.write(" ");

                }

                System.out.print("\n");
                myFile_Obj.write("\n");
            }

            System.out.println(" Eccentricity of this Node : "+eccentricity_final_value);
            String eccentricity_final_value_str = Integer.toString(eccentricity_final_value);
            String eccentricity_last = "\n Eccentricity of this Node : " + eccentricity_final_value_str;
            myFile_Obj.write(eccentricity_last);
            myFile_Obj.close();
            // ############################################

        }
        catch (IOException e)
        {
            System.out.println(" File doesn't exist or output file path is wrong ");
            e.printStackTrace();
        }

        System.out.println(" ---- Output File Generated ----- ");

        // Closing Sockets and threads
        // write code here -- remaining
    }
}
