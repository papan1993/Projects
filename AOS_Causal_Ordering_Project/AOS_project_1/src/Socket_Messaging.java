import java.awt.image.AreaAveragingScaleFilter;
import java.io.*;
import java.util.*;
import java.net.*;

public class Socket_Messaging
{
    public Socket Soc = null;

    public Socket_Messaging(Socket socket_entry)
    {
        this.Soc = socket_entry;
    }

    public void  Send_Msg(Message Msg) throws IOException
    {
        ObjectOutputStream oos = new ObjectOutputStream(Soc.getOutputStream());
        oos.writeObject(Msg);
        System.out.println(" Message Sent to Destination Node ");
        oos.flush();
        //oos.close();
    }

    public Message Recv_Msg() throws IOException, ClassNotFoundException {
        Message m_val = null;
        ObjectInputStream ois = new ObjectInputStream(Soc.getInputStream());
        m_val = (Message)ois.readObject();
        System.out.println(" Message Received From Destination Node ");
        //ois.close();
        return m_val;
    }

}