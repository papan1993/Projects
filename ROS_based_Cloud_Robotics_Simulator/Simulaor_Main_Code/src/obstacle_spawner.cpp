#include <ros/ros.h>
#include <ros/package.h>
#include <std_msgs/Int64.h>
#include <fstream>

#define NO_OF_GRIDS 64


using namespace std;

class readCoordinates{

public:
    int small[12] = {9,10,13,14,17,22,41,46,49,50,53,54}, zero[4] = {18,21,42,45};
    readCoordinates();
    ~readCoordinates();
    ifstream grid_coordinateFile;
    vector < vector<double> > grid_coordinates;
    vector <int> small_vect,zero_vect;
    vector <int>::iterator small_it,zero_it;
};

readCoordinates::readCoordinates()
{

    string dataPath= ros::package::getPath("obstacle_spawner").append("/data/gridCoordinates.txt");
    grid_coordinateFile.open(dataPath.c_str());
    if(!grid_coordinateFile.is_open())
    {
        ROS_INFO("Error opening file");
        exit(0);
    }

    grid_coordinates = vector<vector<double> >(int(NO_OF_GRIDS),vector<double>(2,0));

    for(int i=0;i<int(NO_OF_GRIDS);i++)
    {
        for(int j=0;j<2;j++)
        {
            grid_coordinateFile >> grid_coordinates[i][j];
        }
    }

    small_vect.insert(small_vect.end(), small, small+12);
    zero_vect.insert(zero_vect.end(), zero, zero+4);

    return;
}

readCoordinates::~readCoordinates()
{
    return;
}

void spawnerCallback(const std_msgs::Int64::ConstPtr& msg)
{
  readCoordinates *coordinates = new readCoordinates();
  cout<< coordinates->grid_coordinates[msg->data][0] << '\t' <<coordinates->grid_coordinates[msg->data][1] << endl;
  stringstream grid,command;
  grid << msg->data;
  string model_name = "obstacle",grid_no = grid.str(),cmd;
  model_name = model_name.append(grid_no);
  coordinates->small_it = find(coordinates->small_vect.begin(), coordinates->small_vect.end(), msg->data);
  coordinates->zero_it = find(coordinates->zero_vect.begin(), coordinates->zero_vect.end(), msg->data);
  if(coordinates->small_it != coordinates->small_vect.end())
      command << "rosrun gazebo_ros spawn_model -file /home/prasun/simulation_project/simulationVersion_1.0/Gazebo_ModelsWorldsFile/obstacles/model_small.sdf -sdf -x " << coordinates->grid_coordinates[msg->data][0] << " -y " << coordinates->grid_coordinates[msg->data][1] << " -z 0 -model " << model_name;
  else if(coordinates->zero_it != coordinates->zero_vect.end())
      cout<<"Model already exists.";
  else
      command << "rosrun gazebo_ros spawn_model -file /home/prasun/simulation_project/simulationVersion_1.0/Gazebo_ModelsWorldsFile/obstacles/model_big.sdf -sdf -x " << coordinates->grid_coordinates[msg->data][0] << " -y " << coordinates->grid_coordinates[msg->data][1] << " -z 0 -model " << model_name;
  cmd = command.str();
  cout<<cmd<<endl;
  system(cmd.c_str());
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "grid_no");
    ros::NodeHandle n;
    ros::Subscriber sub = n.subscribe("grid_no_publisher", 1000, spawnerCallback);
    ros::spin();
    return 0;
}
