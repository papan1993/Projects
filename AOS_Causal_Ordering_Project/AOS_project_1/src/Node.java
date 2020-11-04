public class Node
{
    public int node_id;
    public String host_name;
    public int node_port_number;

    public Node(int node_id, String host_name, int node_port_number)
    {
        this.node_id = node_id;
        this.host_name = host_name;
        this.node_port_number = node_port_number;
    }
}