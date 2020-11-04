import java.util.ArrayList;
import java.util.HashMap;

public class Message implements java.io.Serializable
{
    public String Msg_data;
    public int Msg_number;
    public HashMap<Integer, ArrayList<Integer>> Msg_table_data;

    public Message(int Msg_number, String Msg_data, HashMap<Integer, ArrayList<Integer>> Msg_table_data)
    {
        this.Msg_number = Msg_number;
        this.Msg_data = Msg_data;
        this.Msg_table_data = Msg_table_data;
    }

//    public Message(int Msg_number, HashMap<Integer, ArrayList<Integer>> Msg_table_data)
//    {
//        this.Msg_number = Msg_number;
//        this.Msg_data = null;
//        this.Msg_table_data = Msg_table_data;
//    }

    public Message(int Msg_number, String Msg_data)
    {
        this.Msg_number = Msg_number;
        this.Msg_data = Msg_data;
        this.Msg_table_data = null;
    }

}