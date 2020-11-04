import zmq
import time
from config import Location_owl
from rdflib import Graph
from multiprocessing import Process

################################################################################################

def server_robot_1_2(owl):

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:6500")

    while True:
        #  Wait for next request from client
        message = socket.recv()
        print("Received request: %s" % message)

        #  Do some 'work'
        #time.sleep(1)

        ##################################--Query section --#######################

        store_1 = []

        g = Graph()
        g.parse(owl)

        for row in g.query(message):

            ##################################################################################

            print ("--------knowledge recieved from location.owl--------------")

            if (row.warehouse != None):
                print ("--location ---- " + str(row.warehouse))
                store_1.append(str(row.warehouse))

            if (row.aisle_no != None):
                print ("--Inventory aisle number ---- " + str(row.aisle_no))
                store_1.append(str(row.aisle_no))

            if (row.bin_no != None):
                print ("--Inventory bin number ---- " + str(row.bin_no))
                store_1.append(str(row.bin_no))

            if (row.rack_no != None):
                print ("--Inventory rack number ---- " + str(row.rack_no))
                store_1.append(str(row.rack_no))

            print ("\n")

            ##################################################################################

        ###########################################################################

        #  Send reply back to client
        main_str = ''

        for i in range(0, len(store_1), 1):
            main_str = main_str + '$'
            main_str = main_str + store_1[i]
        socket.send_string(main_str)

###############################################################################################

def server_robot_1_3(owl):

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:6000")

    while True:
        #  Wait for next request from client
        message = socket.recv()
        print("Received request: %s" % message)

        #  Do some 'work'
        #time.sleep(1)

        ##################################--Query section --#######################

        store_2 = []

        g = Graph()
        g.parse(owl)

        for row in g.query(message):

            ##################################################################################

            print ("--------knowledge recieved from location.owl--------------")

            if (row.warehouse != None):
                print ("--location ---- " + str(row.warehouse))
                store_2.append(str(row.warehouse))

            if (row.aisle_no != None):
                print ("--Inventory aisle number ---- " + str(row.aisle_no))
                store_2.append(str(row.aisle_no))

            if (row.bin_no != None):
                print ("--Inventory bin number ---- " + str(row.bin_no))
                store_2.append(str(row.bin_no))

            if (row.rack_no != None):
                print ("--Inventory rack number ---- " + str(row.rack_no))
                store_2.append(str(row.rack_no))

            print ("\n")

            ##################################################################################

        ###########################################################################

        #  Send reply back to client
        main_str = ''

        for i in range(0, len(store_2), 1):
            main_str = main_str + '$'
            main_str = main_str + store_2[i]
        #print store_2
        socket.send_string(main_str)

################################################################################################

def server_robot_2_query(owl):

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:4500")

    while True:
        #  Wait for next request from client
        message = socket.recv()
        print("Received request: %s" % message)

        #  Do some 'work'
        #time.sleep(1)

        ##################################--Query section --#######################

        res = ''

        m = Graph()
        m.parse(owl)

        if (len(m.query(message)) == 0):
            print ('---- No---object----found----')
            res = 'False'

        else:
            for row in m.query(message):
                found = str(row.bag)
                print ('--object --found ----', found)
                res = 'True'

        socket.send_string(res)


################################################################################################

def server_robot_3_query(owl):

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:4000")

    while True:
        #  Wait for next request from client
        message = socket.recv()
        print("Received request: %s" % message)

        #  Do some 'work'
        #time.sleep(1)

        ##################################--Query section --#######################

        res = ''

        m = Graph()
        m.parse(owl)

        if (len(m.query(message)) == 0):
            print ('---- No---object----found----')
            res = 'False'

        else:
            for row in m.query(message):
                found = str(row.bag)
                print ('--object --found ----', found)
                res = 'True'

        socket.send_string(res)


################################################################################################


def main_func():

    owl_copy_1 = Location_owl
    owl_copy_2 = Location_owl
    owl_copy_3 = Location_owl
    owl_copy_4 = Location_owl

    ####################################

    p1 = Process(target=server_robot_1_2, args=(owl_copy_1, ))
    p1.start()
    p2 = Process(target=server_robot_1_3, args=(owl_copy_2, ))
    p2.start()
    p3 = Process(target=server_robot_2_query, args=(owl_copy_3, ))
    p3.start()
    p4 = Process(target=server_robot_3_query, args=(owl_copy_4, ))
    p4.start()
    #p1.join()
    #p2.join()

##################################################################################################

if __name__ == '__main__':
    main_func()
