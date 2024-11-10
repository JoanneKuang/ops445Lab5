#!/usr/bin/env python3

# Author: Joanne Kuang
# Author ID: 165994187
# Date: 11-07-2024
# Program: Lab5b.py

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

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
	f = open(file_name, 'a')
	f.write(string_of_lines)
	f.close()

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
	f = open(file_name, 'w')
	for item in list_of_lines:
		f.write(item + '\n')
	f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
	f = open(file_name_read, 'r')
	item = f.readlines()
	f.close()

	f = open(file_name_write, 'w')
	itemnum = 1
	for item in item:
		f.write(str(itemnum) + ":" + item)
		itemnum = itemnum + 1
	f.close()


if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
