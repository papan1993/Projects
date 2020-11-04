import java.io.*;
import java.util.*;
import java.net.*;

public class Comm_Channel
{
    String File_path;
    int Device_self_id;
    Synchronizer msg_hand = null; // Message handler object
    public static boolean self_identification_status = false;

    public static Node my_node;
    public static ArrayList<Node> my_neighbours = new ArrayList<Node>();
    public static ArrayList<Socket> client_socketArrayList = new ArrayList<Socket>();
    public static ArrayList<Socket> server_socketArrayList = new ArrayList<Socket>();

    public static HashMap<Integer, Socket> socket_node_map = new HashMap<Integer, Socket>();
    public static HashMap<Socket, Integer> socket_node_map_reverse = new HashMap<Socket, Integer>();

    public static HashMap<Socket, Thread> socket_thread_map = new HashMap<Socket, Thread>();
    public static HashMap<Thread, Socket> socket_thread_map_reverse = new HashMap<Thread, Socket>();
    
    // Starting Clients function
    public static ArrayList<Socket> start_clients(ArrayList<Node> client_ngh)
    {
        ArrayList<Socket> client_sockets = new ArrayList<Socket>(client_ngh.size());

        for (Node each_ngh : client_ngh) {
            Socket each_client = null;
            try {
                each_client = Client.startClient(each_ngh.host_name, each_ngh.node_port_number);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            client_sockets.add(each_client);
        }
        return client_sockets;
    }

    // Starting Servers function
    public static ArrayList<Socket> start_servers(int port_number, int num_high_ngh)
    {
        ArrayList<Socket> server_sockets = new ArrayList<Socket>(num_high_ngh);
        server_sockets = Server.startServer(port_number, num_high_ngh);
        return server_sockets;
    }

    // Communication channel constructor and operations
    public Comm_Channel(String File_path, int Device_self_id)
    {
        this.File_path = File_path;
        this.Device_self_id = Device_self_id;

        // File Reader Operations
        try
        {
            File_Reader.read_file(File_path, Device_self_id);
        }
        catch (IOException e) {
            e.printStackTrace();
        }

        my_node = File_Reader.My_node;
        my_neighbours = File_Reader.My_neighbours;

        //// Communication Channel Operations ////

        int my_device_id = my_node.node_id;
        int number_higher_neighbors = 0;
        ArrayList<Node> client_neighbors = new ArrayList<Node>();

        // Compute neighbours
        for (Node each_neighbour : my_neighbours) {
            if (each_neighbour.node_id > my_device_id) {
                number_higher_neighbors = number_higher_neighbors + 1;
            } else {
                client_neighbors.add(each_neighbour);
            }
        }

        // Start Servers and Clients
        server_socketArrayList = start_servers(my_node.node_port_number, number_higher_neighbors);
        client_socketArrayList = start_clients(client_neighbors);

        /////////////////////////////////////////////////////

        // Create socket node map and socket identification
        // for server list
        for (Socket temp_socket : server_socketArrayList) {
            // Send _msg
            // recv _msg
            // put in message : socket node identification

            String message_info = Integer.toString(my_node.node_id);
            int temp_msg_no = 0;
            int socket_node_id = -1;
            Message temp_smsg = new Message(temp_msg_no, message_info);

            Socket_Messaging msg_obj = new Socket_Messaging(temp_socket);
            try {
                msg_obj.Send_Msg(temp_smsg);
            } catch (IOException e) {
                e.printStackTrace();
            }

            try {
                Message temp_rmsg = msg_obj.Recv_Msg();
                socket_node_id = Integer.parseInt(temp_rmsg.Msg_data);
            } catch (IOException | ClassNotFoundException e) {
                e.printStackTrace();
            }

            socket_node_map.put(socket_node_id, temp_socket);
            socket_node_map_reverse.put(temp_socket, socket_node_id);

        }

        // for client list
        for (Socket temp_socket : client_socketArrayList) {
            // Send _msg
            // recv _msg
            // put in message : socket node identification

            String message_info = Integer.toString(my_node.node_id);
            int temp_msg_no = 0;
            int socket_node_id = -1;
            Message temp_smsg = new Message(temp_msg_no, message_info);

            Socket_Messaging msg_obj = new Socket_Messaging(temp_socket);
            try {
                msg_obj.Send_Msg(temp_smsg);
            } catch (IOException e) {
                e.printStackTrace();
            }

            try {
                Message temp_rmsg = msg_obj.Recv_Msg();
                socket_node_id = Integer.parseInt(temp_rmsg.Msg_data);
            } catch (IOException | ClassNotFoundException e) {
                e.printStackTrace();
            }

            socket_node_map.put(socket_node_id, temp_socket);
            socket_node_map_reverse.put(temp_socket, socket_node_id);

        }

        self_identification_status = true;
        /// waiting for others to finish identification
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        ///////////////////////////////////////////////////////////////////////////

    }

    //// Message Handler Setter

    public void setMsg_hand(Synchronizer msg_hand)
    {
        this.msg_hand = msg_hand;

        // Start Listener threads
        for (Socket temp_listen_soc : server_socketArrayList) {

            Thread listen_thread_obj = new Socket_Listener(temp_listen_soc, msg_hand);
            socket_thread_map.put(temp_listen_soc, listen_thread_obj);
            socket_thread_map_reverse.put(listen_thread_obj, temp_listen_soc);
            listen_thread_obj.start();
        }

        for (Socket temp_listen_soc : client_socketArrayList) {
            Thread listen_thread_obj = new Socket_Listener(temp_listen_soc, msg_hand);
            socket_thread_map.put(temp_listen_soc, listen_thread_obj);
            socket_thread_map_reverse.put(listen_thread_obj, temp_listen_soc);
            listen_thread_obj.start();
        }

        /////////////////////////////////////////////////////////////////////////////

    }
}