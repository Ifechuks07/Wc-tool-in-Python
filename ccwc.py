import argparse
#Read the file into python
# specify encoding Utf-8 not ascii because the document has
# more characters than present in ascii

#Iterating over each line in the file

def count_line(file_obj): #Passing the file content, not the file.

    line_count = 0
 
    for line in file_obj:
            line_count+=1

    return line_count

#Iterating over each word
def count_word(file_obj):
    word_count=0

    
    for line in file_obj:
        for word in line.split():
            word_count+=1

    return word_count

#Iterating over each character
def count_character (file_obj):
    

    char_count = 0

    for line in file_obj:
        char_count+= len(line)
    return char_count


#Counting the number of bytes in a file.
def count_bytes(file_obj):

    b_count= len(file_obj)

    return b_count

    #with  open('test.txt', 'r', encoding = 'utf-8') as reader:
        #for line in reader:
           # print (line)

    

def main():
    #Create a parser or instantiate a parser object
    parser = argparse.ArgumentParser(prog="ccwc") #container for argument specs

    #used to add argument specs to the parser.

    parser.add_argument('filename',nargs ='?',type= argparse.FileType('r', encoding ='utf-8') )
    parser.add_argument("-c", "--bytes", action="store_true", help ="count bytes")
    parser.add_argument("-l", "--lines", action="store_true", help = "count lines")
    parser.add_argument("-w", "--words",action="store_true", help = "count words")
    parser.add_argument("-m", "--characters",action="store_true", help = "count characters")

    args = parser.parse_args()# runs parser and places data in argparse.namespace object

    with args.filename as file:
        file_contents = file.read()
         # read file once
        

        results=[]

        if args.bytes:
           results.append(count_bytes(file)) 
           file.seek(0)
        if args.lines:
            results.append( count_line(file))
            file.seek(0)
        if args.words:
            results.append(count_word(file)) 
            file.seek(0)
        if args.characters:
            results.append(count_character(file))
            file.seek(0)

     #Output formatting        
    print("\t".join(map(str, results)), end=" ")
    if args.filename.name != "<stdin>":  
        print(args.filename.name)


if __name__ == "__main__":
    main()
