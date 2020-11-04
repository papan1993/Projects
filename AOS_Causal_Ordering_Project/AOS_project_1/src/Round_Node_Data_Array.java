import java.util.ArrayList;
import java.util.HashMap;

public class Round_Node_Data_Array
{
    int Round_number;
    int Node_id;
    HashMap<Integer, ArrayList<Integer>> Message_data;

    public Round_Node_Data_Array(int Round_number, int Node_id, HashMap<Integer, ArrayList<Integer>> Message_data)
    {
        this.Round_number = Round_number;
        this.Node_id = Node_id;
        this.Message_data = Message_data;
    }
}
