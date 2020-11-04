import java.io.*;
import java.util.*;

public class File_Reader
{
    public static int Number_nodes;
    public static Node My_node;
    public static ArrayList<Node> My_neighbours = new ArrayList<Node>();

    public static void nodes_calculate(ArrayList<String> input_data)
    {
        String temp_str = input_data.get(0);
        Number_nodes = Integer.parseInt(temp_str);
    }

    public static ArrayList<String> cleaned_data(ArrayList<String> input_data)
    {
        ArrayList<String> data_split = new ArrayList<String>();
        for (int i =0; i<input_data.size(); i++)
        {
            String temp_str = input_data.get(i);

            if (temp_str.contains("#"))
            {
                String[] temp_split = temp_str.split("#");
                data_split.add(temp_split[0]);
            }
            else {
                data_split.add(temp_str);
            }
        }

        return data_split;
    }

    public static ArrayList<Node> compute_nodes(ArrayList<String> input_data)
    {
        ArrayList<Node> all_nodes = new ArrayList<Node>();
        int check_counter = 1;

        for (int i =1; i<input_data.size(); i++)
        {
            if (check_counter == Number_nodes+1)
            {
                break;
            }
            else {
                String temp_str = input_data.get(i);
                String[] temp_split = temp_str.split(" ");
                int temp_id = Integer.parseInt(temp_split[0]);
                int temp_port = Integer.parseInt(temp_split[2]);
                Node temp_node = new Node(temp_id, temp_split[1], temp_port);
                all_nodes.add(temp_node);
            }
            check_counter = check_counter + 1;
        }

        return all_nodes;
    }

    public static void self_identify(ArrayList<Node> input_data, int device_id)
    {
        for (int i=0; i<input_data.size(); i++)
        {
            Node temp = input_data.get(i);

            if (device_id == temp.node_id)
            {
                My_node = temp;
            }
        }
    }

    public static void compute_neighbours(ArrayList<String> clean_data, ArrayList<Node> all_nodes)
    {
        int start_loop = Number_nodes + 1;
        int my_node_id = My_node.node_id;
        int comp_index = start_loop + my_node_id;

        String temp_str = clean_data.get(comp_index);
        String[] temp_split = temp_str.split(" ");

        for (int i=0; i<temp_split.length; i++)
        {
            int temp_neigh_id = Integer.parseInt(temp_split[i]);

            for (int j = 0; j < all_nodes.size(); j++)
            {
                Node temp = all_nodes.get(j);
                if (temp_neigh_id == temp.node_id)
                {
                    My_neighbours.add(temp);
                }
            }
        }
    }

    public static void display_nodes(int choice)
    {
        // 1 - Mynode ; // 2 - Neighbours // ; 3 - Number_nodes

        switch (choice){
            case 1:
                System.out.println(" --------------- Displaying Information of My Node ---------------- ");
                System.out.println(" Node ID : " + My_node.node_id);
                System.out.println(" Node HostName : " + My_node.host_name);
                System.out.println(" Node Port Number : " + My_node.node_port_number);
                System.out.println("--------------------------------------------------------------------- \n");
                break;

            case 2:
                System.out.println(" --------------- Displaying Information of Neighbours ---------------- \n");
                for (int i = 0; i < My_neighbours.size(); i++)
                {
                    int temp_prt = i + 1;
                    System.out.println(" Neighbour Number : " + temp_prt);
                    Node each_neighbour = My_neighbours.get(i);
                    System.out.println(" Neighbour Node ID : " + each_neighbour.node_id);
                    System.out.println(" Neighbour Node HostName : " + each_neighbour.host_name);
                    System.out.println(" Neighbour Node Port Number : " + each_neighbour.node_port_number);
                    System.out.println("\n");
                }
                System.out.println("--------------------------------------------------------------------- \n");
                break;

            case 3:
                System.out.println(" --------------- Displaying Information of Number of Nodes ------------------- ");
                System.out.println(" Number_Nodes : " + Number_nodes);
                System.out.println("--------------------------------------------------------------------- \n");
                break;

            default:
                System.out.println(" Wrong Input for Displaying Nodes : // 1 - My_node ; // 2 - Neighbours // ; 3 - Number_nodes \n");
        }
    }

    public static void read_file(String file_path, int device_id) throws IOException
    {

        ArrayList<String> input_data = new ArrayList<String>();
        ArrayList<String> clean_data;
        ArrayList<Node> all_nodes;

        try
        {
            System.out.println("Working Directory : " + System.getProperty("user.dir"));
            File myObj = new File(file_path);
            Scanner myReader = new Scanner(myObj);

            while (myReader.hasNextLine())
            {
                String temp_data = myReader.nextLine();
                String test_str = temp_data;
                if (test_str != null && test_str.trim().length() != 0)
                {
                    if (temp_data.charAt(0) != '#')
                    {
                        input_data.add(temp_data);
                    }
                }
            }

            myReader.close();
            clean_data = cleaned_data(input_data);
            System.out.println("Config File Input : " + clean_data);

            nodes_calculate(clean_data);
            all_nodes = compute_nodes(clean_data);
            self_identify(all_nodes, device_id);
            compute_neighbours(clean_data, all_nodes);

            //display_nodes(3);
            //display_nodes(1);
            //display_nodes(2);

        }
        catch (FileNotFoundException e)
        {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }

}
