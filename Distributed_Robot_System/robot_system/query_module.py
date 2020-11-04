import time
import zmq
from rdflib import Graph
from config import Location_owl


##############----client for robot - 1 ---###############

def client_owl_1(str_query, owl_1):

    product = []

    g = Graph()
    g.parse(owl_1)

    for row in g.query(str_query):

        ##################################################################################

        print ("--------knowledge recieved from location.owl--------------")

        if (row.warehouse != None):
            print ("--location ---- " + str(row.warehouse))
            product.append(str(row.warehouse))

        if (row.aisle_no != None):
            print ("--Inventory aisle number ---- " + str(row.aisle_no))
            product.append(str(row.aisle_no))

        if (row.bin_no != None):
            print ("--Inventory bin number ---- " + str(row.bin_no))
            product.append(str(row.bin_no))

        if (row.rack_no != None):
            print ("--Inventory rack number ---- " + str(row.rack_no))
            product.append(str(row.rack_no))

        print ("\n")

    return product

        ##################################################################################


##############----client for robot - 2 ---###############

def client_owl_2(str_query):

    context = zmq.Context()
    print("Connecting to Robot--2 server")

    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5500")

    for request in range(1):
        print("Sending request- %s" % request)
        socket.send(str_query)
        message = socket.recv()
        time.sleep(1)
        print("Received reply %s [ %s ]" % (request, message))

    new_str = message.split('$')
    final_str = []
    var = ''

    for i in range(0, len(new_str), 1):
        if (i != 0):
            final_str.append(new_str[i])

        if (i == len(new_str)-1):
            var = new_str[i]

    return final_str, var


##############----- client for robot -3 ---################


def client_owl_3(str_query):

    context = zmq.Context()
    print("Connecting to Robot--3 server")

    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:7500")

    for request in range(1):
        print("Sending request %s" % request)
        socket.send(str_query)
        message = socket.recv()
        time.sleep(1)
        print("Received reply %s [ %s ]" % (request, message))

    split_1 = message.split('@')
    final_str_main = []

    for i in range(0, len(split_1), 1):
        if (i != 0):
            split_2 = split_1[i].split('$')
            final_str_temp = []

            for j in range(0, len(split_2), 1):
                if (j != 0):
                    final_str_temp.append(split_2[j])

            final_str_main.append(final_str_temp)

    return final_str_main


#############################

####################################################################

def namepace_cut(val):
    part = val.split("#")
    return part[1]

####################################################################

def Query_search(input_str):

    m = Graph()
    m.parse(Location_owl)

    search_query = """
    PREFIX ns_1: <http://www.semanticweb.org/soumyadeep/ontologies/2017/11/Location#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT ?bag
        WHERE
        {
            ?bag rdf:type ns_1:PersonalItems.
            ?bag ns_1:Product_name \"""" + input_str + """\".
        }
    """

    if (len(m.query(search_query)) == 0):
        print ('---- No---'+ input_str + '----found----')
        return False

    else:
        for row in m.query(search_query):
            found = str(row.bag)
            print ('--object --found ----', found)
            return True

####################################################################

def Bag_related_image():

    p = Graph()
    p.parse(Location_owl)

    str_bag = """
    PREFIX ns_1: <http://www.semanticweb.org/soumyadeep/ontologies/2017/11/Location#>
    SELECT ?img
        WHERE
        {
            ?bag rdf:type ns_1:PersonalItems.
            ?bag ns_1:Product_image ?img.
        }
    """

    for row in p.query(str_bag):
        img_path = str(row.img)
        return img_path


####################################################################

def cup_related_image():

    p = Graph()
    p.parse(Location_owl)

    str_cup = """
    PREFIX ns_1: <http://www.semanticweb.org/soumyadeep/ontologies/2017/11/Location#>
    SELECT ?img
        WHERE
        {
            ?cup rdf:type ns_1:PersonalItems.
            ?cup ns_1:Product_image ?img.
        }
    """

    for row in p.query(str_cup):
        img_path = str(row.img)
        return img_path

####################################################################

def appending(prod_1, prod_2):

    prod = []

    for i in range(0 , len(prod_1), 1):
        prod.append(prod_1[i])

    for j in range(0, len(prod_2), 1):
        prod.append(prod_2[j])


    return prod


####################################################################

def query_main(input_str):

    ###################################----Queries-----#########################################

    recv_owl_1 = []
    recv_owl_2 = []
    recv_owl_3 = []

    str_query_1 = """
     PREFIX ns_1: <http://www.semanticweb.org/soumyadeep/ontologies/2017/11/Location#>

     SELECT ?loc ?warehouse ?aisle_no ?bin_no ?rack_no
     WHERE
        {
            ns_1:""" + input_str + """ ns_1:Available_At ?loc.
            ?loc ns_1:Location_name ?warehouse.
            ns_1:""" + input_str + """ ns_1:Inventory_aisle_no ?aisle_no.
            ns_1:""" + input_str + """ ns_1:Inventory_bin_no ?bin_no.
            ns_1:""" + input_str + """ ns_1:Inventory_rack_no ?rack_no.
        }
     """

    recv_owl_1 = client_owl_1(str_query_1, Location_owl)

    str_query_2 = """
     PREFIX ns_2: <http://www.semanticweb.org/soumyadeep/ontologies/2017/11/Object#>

     SELECT ?mall ?price ?color ?shape ?dim ?grip
     WHERE
        {
            ns_2:""" + input_str + """ ns_2:Item_malleability ?mall.
            ns_2:""" + input_str + """ ns_2:Item_price ?price.
            ns_2:""" + input_str + """ ns_2:Item_color ?color.
            ns_2:""" + input_str + """ ns_2:has_shape ?shape.
            ?shape ns_2:Item_dimension ?dim.
            ns_2:""" + input_str + """ ns_2:can_be_picked_by ?grip.
        }
     """

    recv_owl_2, var = client_owl_2(str_query_2)

    str_query_3 = """
     PREFIX ns_3: <http://www.semanticweb.org/soumyadeep/ontologies/2017/11/Capability#>

     SELECT ?robots ?robo_name ?payload
     WHERE
         {
            ?robots ns_3:Can_Pick ns_3:""" + var + """.
            ?robots ns_3:Machine_name ?robo_name.
            ?robots ns_3:Machine_payload ?payload.

         }
     """

    recv_owl_3 = client_owl_3(str_query_3)


    ##################################################################################################

    product = []

    if (recv_owl_1 != None and recv_owl_2 != None and recv_owl_3 != None):
        product = appending(recv_owl_1, recv_owl_2)
        return product, recv_owl_3

    else:
        return None, None


####################################################################