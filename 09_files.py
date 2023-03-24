import csv
import string

def get_points ( file_path ):
    points = []
    file = open ( file_path )
    for line in file :
        l = line . split ()
        points . append (l)
    return points
points_list = get_points ('points.txt')
print ( points_list )

########################################################################################################################



def read_csv_file ( file_path ):
    data = []
    file = open ( file_path )
    csv_reader = csv. reader ( file )
    for row in csv_reader :
        data . append (row)
    return data

def list_gps_commands ( data ):
    dictionary = dict ()
    for row in data :
        gps_cmd = row [0]
        if gps_cmd in dictionary :
            dictionary [ gps_cmd ] += 1
        else :
            dictionary [ gps_cmd ] = 1
    return dictionary

gps_list = read_csv_file (r'GPS.csv')
gps_dict = list_gps_commands ( gps_list )
print ( gps_dict )


########################################################################################################################


def word_count ( file_path ):
    file = open ( file_path )
    dictionary = {}

    for line in file:
        line = line.strip(string.whitespace +
                          string.punctuation).lower().split()
        for word in line:
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
    file.close
    return dictionary
word_table = word_count ('snark.txt')
print ( word_table ["and"])

########################################################################################################################


def store_dict ( dictionary , file_path ):
    file = open ( file_path , "w")
    for key in dictionary :
        file . write ("%s: %i\n" %( key , dictionary [key ]))
    file.close ()
store_dict (wordtable, "result32.txt")

########################################################################################################################


word_table = word_count ('snark.txt')

def most_often ( dictionary ):
    count = 0
    word = ''
    for key in dictionary :
        if dictionary [key ] > count :
            count = dictionary [key]
            word = key
    return word , count
print ( most_often ( word_table ))

def most_often_5_chars ( dictionary ):
    count = 0
    word = ''
    for key in dictionary :
        if len(key) == 5:
            if dictionary [key ] > count :
                count = dictionary [key]
                word = key
    return word , count
print ( most_often_5_chars ( word_table ))


def most_often_n_chars ( dictionary , length ):
    count = 0
    word = ''
    for key in dictionary :
        if len(key) == length :
            if dictionary [key ] > count :
                count = dictionary [key]
                word = key
    return word , count
print ( most_often_n_chars ( word_table , 5))

#######################################################################################################################

def begin_with_b ( file_path ):
    word_table = word_count ( file_path )
    count = 0
    for key in word_table :
        if key [0] == 'b':
            count += 1
    return count
print ( begin_with_b ('snark.txt'))


def begin_with_char ( file_path , char ):
    word_table = word_count ( filename )
    count = 0
    for key in word_table :
        if key [0] == char :
            count += 1
    return count
print ( begin_with_char ('snark.txt', 'b'))



















