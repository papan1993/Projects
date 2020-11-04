import java.io.*;
import java.net.*;

public class Socket_Listener extends Thread
{
    Socket Soc_obj;
    int Node_id;
    Synchronizer msh_hand_obj = null;

    public Socket_Listener(Socket Soc_obj, Synchronizer msh_hand_obj)
    {
        this.Soc_obj = Soc_obj;
        this.msh_hand_obj = msh_hand_obj;
        this.Node_id = Comm_Channel.socket_node_map_reverse.get(Soc_obj);
    }

    @Override
    public void run()
    {
        Socket_Messaging soc_msg = new Socket_Messaging(Soc_obj);

        while (true)
        {
            try
            {
                Message listener_msg = soc_msg.Recv_Msg();

                // perform message handling operation
                msh_hand_obj.onReceive_handler(listener_msg, Node_id);

            }
            catch (IOException | ClassNotFoundException e) {
                e.printStackTrace();
            }
        }

    }
}