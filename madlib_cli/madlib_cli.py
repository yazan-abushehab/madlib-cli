import re

print("""        *******************
        *******Welcome****** 
***********You are in the Madlib Game ********* 
***********We Hope You'r Ready To play With Us ******
###########################################################
This game is take some words from you like none , verb ,adjective so on ........ 
""")

   # this func take a path for afile and read it then return its content
def read_template(path):
    try:
       test1=open(path)
       return test1.read()
    except FileNotFoundError as err:
        print('file is not found pls change the path !')
        print(err)


def parse_template(text):
    actual_stripped=''
    actual_parts=[]
    x=text.split(' ')
   
    reg=r"^{\w+}"  # made regex to check on the word inside a {}.
    # loop over the x and x is the array have the text after split it 
    for i in x:
        
        if re.match(reg,i)==None :
            
            actual_stripped+=f"{i} " # add what not matches in actual_stripped
            
        else : # other wise have two cases (last word , mid or first words  )
            if i==x[-1]:
                actual_stripped+='{}.' # to add it to the stripped
                actual_parts+=[i[1:-2]] # for last word cuz it has a dot after split
            else:
                actual_parts+=[i[1:-1]]  # for the other words to remove the {} and add it to the actual_parts
                actual_stripped+='{} ' # to add it to the stripped
    # convarert actual_parts from array to tuple then return it and return actual_stripped as a string
    actual_parts=tuple(actual_parts)
    return (actual_stripped,actual_parts)
    
 
def merge(text,tep): # this func take evrey index of a tuple and add it to the txt where he find {}
    return text.format(*tep)

# this write inside my file  that founded assets/output_game.txt
""" this func will over write the file with the new story the user write"""
def create_file(result ,file_to_write_on_it):
    with open(file_to_write_on_it, "w") as f:
        f.write(result)
        

def start_game(file_toRead_game,file_toWrite_game):
    text = read_template(file_toRead_game)
    stripped_text, parts_tuple = parse_template(text)
    user_input = []
    
    for i in range(len(parts_tuple)):
        x = input('enter a {} > '.format(parts_tuple[i]))
        user_input.append(x)
    result = stripped_text.format(*user_input)
    print(f"this is the story you wrote it \n{result}")
    create_file(result,file_toWrite_game)



    
  
if __name__=="__main__":
    start_game("assets/madlib_game_file.txt","assets/output_game.txt")