#ifndef GRAPH_H
#define GRAPH_H
#include <iostream>
#include <vector>
#include <random>
#include <time.h>
#include <stdlib.h>
#include <robot_planning/generic_functions.h>
#include <boost/config.hpp>

#include <boost/graph/graph_traits.hpp>
#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/dijkstra_shortest_paths.hpp>
#include <boost/property_map/property_map.hpp>
#define ROWS    8
#define COLS    5
#define NODES   64
#define NO_OF_GRIDS 64

using namespace std;
using namespace boost;


class Node{

private:
protected:
public:
    int index;

    Node()
    {
        index = 0;
    }

    ~Node()
    {

    }

};

class Edge{

private:
protected:
public:
    int srcIndex,dstIndex;
    double edgeCost;

    Edge(int srcIdx,int dstIdx,double cost)
    {
        srcIndex = srcIdx;
        dstIndex = dstIdx;
        edgeCost = cost;

    }

    ~Edge()
    {

    }

};

class Graph{

private:
protected:
public:
    vector <vector<double> > adj_matrix;
    vector< vector<double> > adj_matrix_unchanged;
    Edge *edgeVector[int(NODES)*int(NODES)];
    vector<double> distanceVector;
    vector<bool> visitedNodes;
    vector<int> pathNodeList;
    vector<int> tempBlockedGrids;



    Graph()
    {
        /* initialize random seed: */
        srand (time(NULL));

        adj_matrix = vector< vector< double> >(int(NODES),vector<double>(int(NODES),0));

        for(int i=0;i<int(NODES);i++)
        {
            for(int j=i;j<int(NODES);j++)
            {
                if(i!=j)
                {
                    edgeVector[i*NODES+j] = new Edge(i,j,1+rand()%10);


                    adj_matrix[i][j] = edgeVector[i*NODES+j]->edgeCost;

                    edgeVector[j*NODES+i] = new Edge(j,i,adj_matrix[i][j]);
                    adj_matrix[j][i] = adj_matrix[i][j];
                }
                else
                {
                    edgeVector[i*NODES+j] = new Edge(i,j,100);
                    adj_matrix[i][j] = edgeVector[i*NODES+j]->edgeCost;
                }
            }
        }

        vector< vector<double> > gridCenters(int(NO_OF_GRIDS),vector<double>(2,0));

        for(int i=0;i<8;i++)
        {
            for(int j=0;j<8;j++)
            {
                gridCenters[i*8+j][0] = 40+j*80;
                gridCenters[i*8+j][1] = 40+i*80;
                //                char temp[200];
                //            cout << i*8+j << "\t" << 40+j*80 << "," << 40+i*80 << endl;
                //                sprintf(temp,"%d",i*8+j);
                //                cv::putText(image,temp,cv::Point(40+j*80,40+i*80),1,2,cv::Scalar(0,0,255),2,8,0);
                //            cv::imshow("im",image);
                //            cv::waitKey(0);
            }
        }

        for(int i=0;i<int(NODES);i++)
        {
            double x= gridCenters[i][0],y=gridCenters[i][1];
            for(int j=0;j<int(NODES);j++)
            {

                double x1 = gridCenters[j][0],y1=gridCenters[j][1];
                double dist = sqrt(pow(x1-x,2)+pow(y1-y,2));
//                cout << i << "\t" << j << "\t" << dist << endl;
                if(dist < 90 && dist > 20)
                {
                    adj_matrix[i][j] = 1;
                    //                    adj_matrix[j][i] = 1;
                }
                else
                {
                    adj_matrix[i][j] = 1000;
                    //                    adj_matrix[j][i] = 1000;

                }

                //                adj_matrix[i][j] = 1;
            }
        }


        // Temporary arrangement for blocking grids
        tempBlockedGrids.push_back(18);
        tempBlockedGrids.push_back(21);
        tempBlockedGrids.push_back(42);
        tempBlockedGrids.push_back(45);
      //tempBlockedGrids.push_back(47);
      //tempBlockedGrids.push_back(55);

        for(int i=0;i<tempBlockedGrids.size();i++)
        {
            for(int j=0;j<NODES;j++)
            {
                adj_matrix[tempBlockedGrids[i]][j] = 1000;
                adj_matrix[j][tempBlockedGrids[i]] = 1000;
            }
        }


        adj_matrix_unchanged.assign(adj_matrix.begin(),adj_matrix.end());

        visitedNodes = vector<bool>(int(NODES),false);

    }

    ~Graph()
    {

    }

    void findShortestPathBetweenTwoNodes(int srcIndex,int dstIndex);
    void findDistanceFromSourceToEachNode(int srcIndex);


};

void Graph::findDistanceFromSourceToEachNode(int index)
{
    for(int i=0;i<int(NODES);i++)
    {
        if((visitedNodes[i] == false) && (i!= index))
            distanceVector.push_back(adj_matrix[index][i]);
        else
            distanceVector.push_back(1000);
    }

    return;
}



//void Graph::findShortestPathBetweenTwoNodes(int srcIndex, int dstIndex)
//{

//    double distanceValue = 0.0;
//    int currentNodeIndex = srcIndex;
//    pathNodeList.clear();
//    pathNodeList.push_back(srcIndex);
//    //    visitedNodes.resize(int(NODES),false);
//    visitedNodes.clear();
//    visitedNodes = vector<bool>(int(NODES),false);
//    visitedNodes[srcIndex] = true;
//    int nextIndex = 0;
//    double nextIndexDist = 0.0;


//    while(1)
//    {

//        distanceVector.clear();

//        findDistanceFromSourceToEachNode(currentNodeIndex);

//        nextIndex = 0;
//        nextIndexDist = 0;

//        minOfArray(distanceVector,nextIndexDist,nextIndex);
//        //        cout << currentNodeIndex <<"\t" << nextIndex << "\t" << nextIndexDist << "\t" << visitedNodes[nextIndex] << endl;
//        pathNodeList.push_back(nextIndex);
//        visitedNodes[nextIndex] = true;
//        currentNodeIndex = nextIndex;
//        distanceValue += nextIndexDist;

//        if(currentNodeIndex == dstIndex)
//            break;

//    }

//    //    for(int i=0;i<pathNodeList.size()-1;i++)
//    //    {
//    //        adj_matrix[pathNodeList[i]][pathNodeList[i+1]] = 100;

//    //    }
//    //    cout << "Path node list \t" << endl;
//    for(int i=0;i<pathNodeList.size();i++)
//        cout << pathNodeList[i] << "\t";
//    cout << endl;
//    //    cout << "Total distance from " << srcIndex << " to " << dstIndex << " = " << distanceValue << endl;



//    return;
//}

bool findElementInVector(vector<int> array,int element)
{
    for(int i=0;i<array.size();i++)
    {
        if(array[i] == element)
        {
            return true;
        }
    }

    return false;
}
const int inf = 1 << 1000;

// given adjacency matrix adj, finds shortest path from A to B
void Graph::findShortestPathBetweenTwoNodes(int srcIndex, int dstIndex){
    cout << srcIndex << "\t" << dstIndex << endl;
    pathNodeList.clear();


    // Graph parameters
    typedef adjacency_list< listS, vecS, directedS,no_property, property < edge_weight_t, int > > graph_t;
    typedef graph_traits < graph_t >::vertex_descriptor vertex_descriptor;
    typedef std::pair<int, int> Edge;

//    vector<Edge> edgeArray;
    Edge edge_array[adj_matrix.size()*adj_matrix.size()];
    double weights[adj_matrix.size()*adj_matrix.size()];

    for(int i=0;i<adj_matrix.size();i++)
        for(int j=0;j<adj_matrix.size();j++)
        {
            edge_array[i*adj_matrix.size()+j] = Edge(i,j);
            weights[i*adj_matrix.size()+j] = adj_matrix[i][j];
        }


     const int num_nodes = int(NO_OF_GRIDS);

     int num_arcs = sizeof(edge_array) / sizeof(Edge);
     graph_t g(edge_array, edge_array + num_arcs, weights, num_nodes);
     property_map<graph_t, edge_weight_t>::type weightmap = get(edge_weight, g);
     std::vector<vertex_descriptor> p(num_vertices(g));
     std::vector<int> d(num_vertices(g));
     vertex_descriptor s = vertex(srcIndex, g);


     dijkstra_shortest_paths(g,s,
                             predecessor_map(boost::make_iterator_property_map(p.begin(), get(boost::vertex_index, g))).
                             distance_map(boost::make_iterator_property_map(d.begin(), get(boost::vertex_index, g))));

     int node_index = dstIndex;

     while(1)
     {
         int index = p[node_index];
         if(index == node_index)
         {
             pathNodeList.push_back(node_index);
             break;
         }
         else
         {
             pathNodeList.push_back(node_index);
             node_index = p[node_index];
         }
     }



     cout << "End of dijksrta" << endl;
     for(int i=0;i<pathNodeList.size();i++)
         cout << pathNodeList[i] << "\t";
     cout << endl;

     vector<int> list_temp(pathNodeList.begin(),pathNodeList.end());
     pathNodeList.clear();
     for(int i=list_temp.size()-1;i>=0;i--)
         pathNodeList.push_back(list_temp[i]);


    return;
}

#endif // GRAPH_H
