import java.net.*;

public class Client
{
    public static Socket startClient(String ipAddress, int port) throws InterruptedException
    {
        Socket client_socket = null;
        //ipAddress = "localhost";   // for testing in local machine

        while(client_socket == null)
        {
            try
            {
                // getting localhost ip
                InetAddress ip = InetAddress.getByName(ipAddress);

                // establish the connection with server port
                client_socket = new Socket(ip, port);

                System.out.println(" Connected to address : " + ipAddress + " at port number : " + port);

            }
            catch(Exception e)
            {
                client_socket = null;
                Thread.sleep(1000);
                //e.printStackTrace();
            }
        }

        return client_socket;
    }
}