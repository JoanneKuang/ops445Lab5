#!/usr/bin/env python3

# Author: Joanne Kuang
# Author ID: 165994187
# Date: 11-07-2024
# Program: Lab5a.py

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
	f = open(file_name, 'r')
	read_data = f.read()
	f.close()
	# this will return the entire content of read_data
	return read_data

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
	f = open(file_name, 'r')
	read_data = f.read()
	f.close()
	# this will return the entire content of read_data
	list_of_lines = read_data.split('\n')
	if list_of_lines[-1] == '':
		list_of_lines = list_of_lines[:-1]
	return list_of_lines

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
