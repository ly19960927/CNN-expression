# -*- coding:utf-8 -*- 

'''
this file reads a csv file which contains [emotion tag, pixels, usage] information
'''

import numpy
import os

class Fer_Parser:

    def parse_all(self):

        print 'Parsing all data...'

	# ----------------------------- init -----------------------------
        f = open('data.csv')
        X_train = []
        Y_train = []  # 
        X_test = []
        Y_test = []
        count = 0
        lines = f.readlines()[1:]
        length = str(len(lines))

	# ------------------------------ for start ---------------------------------
        for line in lines:
            count += 1
            if count % 5000 == 0:
                print str(count) + '/' +length  # print process

            data = line.split(',')  # data is an array (split by ',')

            tag = int(data[0])  # tag is from 0 to 6 (emotion tag)

            pixels = map(int, data[1].split())  # data[1] split and convert to int 
            pixel_holder = numpy.array(pixels)  # numpy create array

            pixels = list(numpy.reshape(pixel_holder, (48,48)))  # convert to 48 * 48 list
            data_set = data[2][:-2]  # usage (-1 removes '/n')

            if data_set == 'Training':
                X_train.append(pixels)
                Y_train.append(tag)

            if data_set == 'PublicTest':
                X_test.append(pixels)
                Y_test.append(tag)
	# ------------------------------ for end -----------------------------------

	print len(X_train)
	print len(Y_train)
	print len(X_test)
	print len(Y_test)

        # ----------------------- convert Y to one hot -----------------------------
        X_train = numpy.array(X_train)
	X_train = X_train - numpy.mean(X_train, axis = 0)  # numpy.mean computes the average value of every row, ???
        X_train = X_train.reshape(numpy.shape(X_train)[0], 48, 48, 1)  # convert to 4D array
        Y_train = numpy.eye(7)[numpy.array(Y_train, dtype = numpy.uint8)]  # eye is a square of 7*7

        X_test = numpy.array(X_test)
	X_test = X_test - numpy.mean(X_test, axis = 0)
        X_test = X_test.reshape(numpy.shape(X_test)[0], 48, 48, 1)
        Y_test = numpy.eye(7)[numpy.array(Y_test, dtype = numpy.uint8)]

        print 'Done parsing data.'
        return X_train, Y_train, X_test, Y_test

#Example
#p = Fer_Parser()
#a,b,c,d = p.parse_all()
#print a
#print b
#print c
#print d
