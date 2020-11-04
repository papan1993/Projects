import cv2
import zmq
from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF
from config import Location_owl, image_path_bag, image_path_cup
from query_module import Bag_related_image, cup_related_image
import time

##################################

def image_process(img1, img2, img_path, img_path_new, robot_input):

    orb = cv2.ORB()
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    # ------- Recievd Parameters----------------------------------

    aisle_no = 3
    bin_no = 4
    rack_no = 7
    obj_x = 5
    obj_y = 4
    obj_z = 7
    dim = str(obj_x) + 'x' + str(obj_y) + 'x' + str(obj_z)
    malleability = 'false'
    location = 'Warehouse_kolkata'

    # -----------------------------------------------------------

    object_data = []

    threshold_keypoints = 120

    if (len(matches) >= threshold_keypoints):
        print "object detected ------", robot_input

        # ----------------------------  Object Parameters ----------------------------------

        object_name = str(robot_input)
        object_grip = "Handle"
        object_dimension = dim
        object_id = 346
        object_image = img_path_new
        object_aisle_no = aisle_no
        object_rack_no = rack_no
        object_bin_no = bin_no
        object_malleable = malleability
        object_price = 340
        object_color = "Blue"
        object_loc = location

        object_data.append(object_name) ### 0
        object_data.append(object_id)   ### 1
        object_data.append(object_image)  ### 2
        object_data.append(object_aisle_no)  ### 3
        object_data.append(object_rack_no)   ### 4
        object_data.append(object_bin_no)  ### 5
        object_data.append(object_malleable)  ### 6
        object_data.append(object_price)  ### 7
        object_data.append(object_loc)  ### 8
        object_data.append(object_grip)  ### 9
        object_data.append(object_dimension)  ### 10
        object_data.append(object_color)  ### 11

    return object_data

######################################################

def ontology_update(object_data):
    print ("---object data ---", object_data)
    g = Graph()
    g.parse(Location_owl)

    ns_1 = "http://www.semanticweb.org/soumyadeep/ontologies/2017/11/Location#"
    object_uri = ns_1 + object_data[0]
    object_war_loc = ns_1 + object_data[8]

    data_nm_1 = Namespace(ns_1)

    g.add((URIRef(object_uri), RDF.type, data_nm_1.PersonalItems))
    g.add((URIRef(object_uri), data_nm_1.Available_At, URIRef(object_war_loc)))
    g.add((URIRef(object_uri), data_nm_1.Product_name, Literal(object_data[0])))
    g.add((URIRef(object_uri), data_nm_1.Product_id, Literal(object_data[1])))
    g.add((URIRef(object_uri), data_nm_1.Product_image, Literal(object_data[2])))
    g.add((URIRef(object_uri), data_nm_1.Inventory_aisle_no, Literal(object_data[3])))
    g.add((URIRef(object_uri), data_nm_1.Inventory_rack_no, Literal(object_data[4])))
    g.add((URIRef(object_uri), data_nm_1.Inventory_bin_no, Literal(object_data[5])))

    file = open(Location_owl, "w")
    file.write(g.serialize(format='application/rdf+xml'))

######################################################

def update_pub_sub(object_data):
    port = "8000"
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:%s" % port)

    num = 0
    while num!= 20:
        topic = 11001
        messagedata = object_data
        print ("--------- sending new explored object to other Robots ------")
        #print ("%d %s" % (topic, messagedata))
        socket.send("%d %s" % (topic, messagedata))
        time.sleep(2)
        num = num+1

    return True

######################################################

def explore(robot_input):
    print ('------------ inside explore module ------------')

    ################################

   # Robot runnibg and detecting object as obstacle

    print ("------- Rover - 1 ----- started exploring -------")
    print ('\n')
    time.sleep(10)
    print ("------- I found an object -----------")

    ################################

    word = robot_input[0:3]

    if (word == 'Bag'):
        img_path = Bag_related_image()
        img1 = cv2.imread(img_path, 0)
        img2 = cv2.imread(image_path_bag, 0)
        object_data = image_process(img1, img2, img_path, image_path_bag, robot_input)

    else:
        img_path = cup_related_image()
        img1 = cv2.imread(img_path, 0)
        img2 = cv2.imread(image_path_cup, 0)
        object_data = image_process(img1, img2, img_path, image_path_cup, robot_input)


    if (object_data == None):
        print ("----- No object detected -----")
        return False

    else:
        print ("---updating owl------")
        ontology_update(object_data)
        res = update_pub_sub(object_data)

        if (res == True):
            return True
        else:
            return False

#######################################################