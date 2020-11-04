import java.io.*;
import java.util.*;
import java.net.*;

public class Synchronizer
{
    // Maps and Tables - check once hashmap synchronized or not
    //HashMap<Integer, HashMap<Integer, String>> Message_operation_map = new HashMap<Integer, HashMap<Integer, String>>();
    Map<Integer, HashMap<Integer, HashMap<Integer, ArrayList<Integer>>>> Message_operation_map = Collections.synchronizedMap(new HashMap<Integer, HashMap<Integer, HashMap<Integer, ArrayList<Integer>>>>());
    HashMap<Integer, HashMap<Integer, ArrayList<Integer>>> Msg_support_map = new HashMap<Integer, HashMap<Integer, ArrayList<Integer>>>();
    //ArrayList<Round_Node_Data_Array> Buffer_array = new ArrayList<Round_Node_Data_Array>();
    List<Round_Node_Data_Array> Buffer_array = Collections.synchronizedList(new ArrayList<Round_Node_Data_Array>());
    ArrayList<Integer> Remove_buffer_index_list = new ArrayList<Integer>();

    int number_neighbours = Comm_Channel.my_neighbours.size();
    int counter_no_msg = 0;

    int columns = File_Reader.Number_nodes;
    int rows = File_Reader.Number_nodes;
    String[][] Node_table_ent = new String[columns][rows];

    /// Initialize final K-Hop table with neighbours
    final HashMap<Integer, ArrayList<Integer>> Final_table_map = new HashMap<Integer, ArrayList<Integer>>();
    int eccentricity_neighbours_count = 0;
    int initialise_count = 0;
    //int number_eccentricity_computed = 0;
    ArrayList<Integer> Eccentricity_neighbours_hop_array = new ArrayList<Integer>();

    Comm_Channel com_obj = null;
    public int current_round_number = 1;
    public boolean target_reached = false;

    ////////////// constructor
    public Synchronizer(Comm_Channel com_obj)
    {
        this.com_obj = com_obj;
    }

    // Initialise table function
    public void initialize_table()
    {

        //ArrayList<Integer> Eccentricity_neighbours_hop_array_initial = new ArrayList<Integer>();

        // K-hop : 0
        //System.out.println("check data --> "+Comm_Channel.my_node.node_id);
        Eccentricity_neighbours_hop_array.add(Comm_Channel.my_node.node_id);
        Final_table_map.put(0, new ArrayList<Integer>(Eccentricity_neighbours_hop_array));
        //System.out.println("map --> " + Final_table_map);
        Eccentricity_neighbours_hop_array.clear();
        new ArrayList<Integer>(Eccentricity_neighbours_hop_array);
        //System.out.println("map after clear 1 --> " + Final_table_map);

        // k-hop : 1 (neighbours)
        for (int i=0; i < Comm_Channel.my_neighbours.size(); i++)
        {
            Node temp_node = Comm_Channel.my_neighbours.get(i);
            Eccentricity_neighbours_hop_array.add(temp_node.node_id);
        }
        Final_table_map.put(1, new ArrayList<Integer>(Eccentricity_neighbours_hop_array));
        //System.out.println("map before clear 2 --> " + Final_table_map);
        Eccentricity_neighbours_hop_array.clear();
        new ArrayList<Integer>(Eccentricity_neighbours_hop_array);
        //System.out.println("map after clear 2 --> " + Final_table_map);
    }

    /// Function to check availability of node in the final table in previous hops
    public boolean check_table_data(int node_id)
    {
        boolean ret_flag = false;

        //System.out.println(" received node id -> "+ node_id);

        if (node_id == -1)
        {
            ret_flag = true;
        }
        else
        {
            for (int i = 0; i < Final_table_map.size(); i++)
            {
                ArrayList<Integer> each_row = Final_table_map.get(i);
                //System.out.println(" Each row --> "+each_row);
                for (int j = 0; j < each_row.size(); j++)
                {
                    int each_value = each_row.get(j);
                    //System.out.println("Each value --> "+each_value);
                    if (each_value == node_id)
                    {
                        ret_flag = true;
                        break;
                    }
                }

                if(ret_flag)
                {
                    break;
                }
            }
        }

        return ret_flag;

    }

    ///// compute eccentricity
    public void eccentricity(HashMap<Integer, ArrayList<Integer>> input_message, int Node_id)
    {
        //// write code here
        // increment count of recv messages
        eccentricity_neighbours_count = eccentricity_neighbours_count + 1;

        /// Main operation checking messages
        int i = current_round_number;
        ArrayList<Integer> k_hop_queue = input_message.get(i);
        //System.out.println(" Neighbour Count for Eccentricity --> "+eccentricity_neighbours_count);
        //System.out.println(" Each K-hop Queue ---> "+k_hop_queue);
        boolean flag = true;

        //System.out.println(" Part - 1");

        for (int j =0; j < k_hop_queue.size(); j++)
        {
            int temp_node_id = k_hop_queue.get(j);
            flag = check_table_data(temp_node_id);
            //System.out.println("flag value --> " + flag);

            if (!flag)
            {
                System.out.println(" Adding data to Main Map ");
                Eccentricity_neighbours_hop_array.add(temp_node_id);
            }
        }

        //System.out.println(" Part - 2 ");

        if (eccentricity_neighbours_count == number_neighbours)
        {
            //System.out.println(" eccentricity_neighbours_count == number_neighbours ");
            int hop_index = current_round_number + 1;

            if (Eccentricity_neighbours_hop_array.size() == 0)
            {
                //System.out.println("I should be here");
                if (Final_table_map.size() != File_Reader.Number_nodes)
                {
                    //System.out.println(" I cannot be here");
                    Eccentricity_neighbours_hop_array.add(-1);
                    Final_table_map.put(hop_index, new ArrayList<Integer>(Eccentricity_neighbours_hop_array));
                }
            }
            else
            {
                //System.out.println(" I am inside else adding data as len is not zero");
                Final_table_map.put(hop_index, new ArrayList<Integer>(Eccentricity_neighbours_hop_array));
            }

            Eccentricity_neighbours_hop_array.clear();
            new ArrayList<Integer>(Eccentricity_neighbours_hop_array);

            //Finish eccentricity
            if (Final_table_map.size() == File_Reader.Number_nodes)
            {
                System.out.println(" Project target reached ");
                target_reached = true;
            }

            eccentricity_neighbours_count = 0; // Reset
        }

    }

    ///// checking buffer data
    public boolean check_buffer()
    {
        boolean temp_flag = false;

        if (Buffer_array.size() == 0)
        {
            temp_flag = false;
        }
        else {

            for (int i = 0; i < Buffer_array.size(); i++)
            {
                Round_Node_Data_Array temp_data = Buffer_array.get(i);

                if (temp_data.Round_number == current_round_number)
                {
                    temp_flag = true;
                    break;
                }

            }
        }

        return temp_flag;
    }

    /////// Remove buffer function
    public void remove_buffer_list()
    {
        for (int i=0; i < Remove_buffer_index_list.size(); i++)
        {
            int temp_index = Remove_buffer_index_list.get(i);
            Buffer_array.remove(temp_index);
        }

        Remove_buffer_index_list.clear();
        new ArrayList<Integer>(Remove_buffer_index_list);
    }

    public synchronized void Buffer_handler()
    {
        boolean check_buffer_before = false;
        ///// Checking buffer data /////

        check_buffer_before = check_buffer();

        System.out.println(" Buffer Data --> "+Buffer_array);
        System.out.println(" Buffer flag -> "+check_buffer_before);

        if (check_buffer_before)
        {
            for (int i = 0; i < Buffer_array.size(); i++)
            {
                Round_Node_Data_Array buffer_temp_data = Buffer_array.get(i);
                if (buffer_temp_data.Round_number == current_round_number)
                {
                    if (Msg_support_map.containsKey(buffer_temp_data.Node_id))
                    {
                        Msg_support_map.replace(buffer_temp_data.Node_id, buffer_temp_data.Message_data);
                    }
                    else {
                        Msg_support_map.put(buffer_temp_data.Node_id, buffer_temp_data.Message_data);
                    }

                    counter_no_msg = counter_no_msg + 1;
                    Remove_buffer_index_list.add(i);
                }
            }
            //remove_buffer_list();
        }

        ////// generating the main operation map /////

        if (number_neighbours == counter_no_msg)
        {
            //System.out.println("Reached here for final operation map, Msg Support Map -> " + Msg_support_map);
            Message_operation_map.put(current_round_number, new HashMap<Integer, HashMap<Integer, ArrayList<Integer>>>(Msg_support_map));
            //System.out.println("Main operation map before -> " + Message_operation_map);
            Msg_support_map.clear();
            new HashMap<Integer, HashMap<Integer, ArrayList<Integer>>>(Msg_support_map);
            counter_no_msg = 0; // Reset to 0
            //System.out.println("Main operation map after all neighbors on receive -> " + Message_operation_map);
        }

        //System.out.println(" End of on receive");
        //System.out.println(Message_operation_map);

    }

    ////// on receive message handler and buffer zone
    public synchronized void onReceive_handler(Message listen_msg, int Node_id)
    {
        int recv_round_number = listen_msg.Msg_number;
        //int copy_counter_no;

        System.out.println(" Message inside on Receive -- " + recv_round_number + " : " + listen_msg.Msg_table_data);

        if (recv_round_number != 0)
        {
            //////  if code finishes - add if the sent message is same or twice or more - here before

            if (recv_round_number == current_round_number)
            {
                if (Msg_support_map.containsKey(Node_id))
                {
                    Msg_support_map.replace(Node_id, listen_msg.Msg_table_data);
                }
                else {
                    Msg_support_map.put(Node_id, listen_msg.Msg_table_data);
                }

                //copy_counter_no = counter_no_msg;
                counter_no_msg = counter_no_msg + 1;

            }
            else {
                Round_Node_Data_Array temp_buffer = new Round_Node_Data_Array(recv_round_number, Node_id, listen_msg.Msg_table_data);
                Buffer_array.add(temp_buffer);
            }

        }
    }

    public void synchronizer_algorithm()
    {
        /// check identification work
        while (!Comm_Channel.self_identification_status)
        {
            try
            {
                Thread.sleep(100);
            }
            catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        // initialise table
        if (initialise_count == 0)
        {
            initialize_table();
            System.out.println(" Initialize table ---> " + Final_table_map);
        }

        /// Each Round Tasks
        while (!target_reached)
        {

            System.out.println("Round Number ---> " + current_round_number);

            ////// Sending message to neighbours

            String temp_message = "Empty";
            Message send_message = new Message(current_round_number, temp_message, Final_table_map);

            for (int i = 0; i < Comm_Channel.my_neighbours.size(); i++)
            {
                Node neighbour_temp = Comm_Channel.my_neighbours.get(i);
                int neighbour_node_id = neighbour_temp.node_id;
                Socket neighbour_socket = Comm_Channel.socket_node_map.get(neighbour_node_id);

                Socket_Messaging sm_obj = new Socket_Messaging(neighbour_socket);
                try
                {
                    sm_obj.Send_Msg(send_message);
                }
                catch (IOException e) {
                    e.printStackTrace();
                }
            }

            ////// Receiving and processing received messages

            // waiting for all messages to be received in a round
            boolean contain_flag = false;
            while (!contain_flag)
            {
                try
                {
                    Thread.sleep(2000);
                    Buffer_handler();
                    contain_flag = Message_operation_map.containsKey(current_round_number);
                }
                catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }

            /// Do work with received messages : eccentricity call
            HashMap<Integer, HashMap<Integer, ArrayList<Integer>>> message_map = Message_operation_map.get(current_round_number);
            for (int i=0; i < message_map.size(); i++)
            {
                //System.out.println(" I am inside Synchronizer eccentricity for loop ");
                Node neigh_temp = Comm_Channel.my_neighbours.get(i);
                HashMap<Integer, ArrayList<Integer>> neigh_message = message_map.get(neigh_temp.node_id);
                System.out.println(" Message going inside eccentricity --> "+neigh_message);
                System.out.println(" Node id going inside eccentricity --> "+neigh_temp.node_id);
                eccentricity(neigh_message, neigh_temp.node_id);
            }

            // Increment round number
            current_round_number = current_round_number + 1;
            initialise_count = initialise_count + 1;
        }

    }
}