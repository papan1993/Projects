import java.io.*;
import java.util.*;
import java.net.*;

public class Server
{
    public static ArrayList<Socket> startServer(int port, int higher_neighbours)
    {
        ArrayList<Socket> serverSocketList= new ArrayList<Socket>(higher_neighbours);
        ServerSocket server_obj = null;
        try
        {
            server_obj = new ServerSocket(port);
            System.out.println(" Server Started at Port No. : "+port);

            try
            {
                System.out.println(" Waiting for the connection ");
                for (int i=0; i < higher_neighbours; i++)
                {
                    Socket s_new = server_obj.accept();
                    serverSocketList.add(s_new);
                }
            }
            catch (Exception e)
            {
                e.getStackTrace();
            }

        }
        catch (IOException e)
        {
            //server_obj.close();
            e.printStackTrace();
        }

        return serverSocketList;

    }

}