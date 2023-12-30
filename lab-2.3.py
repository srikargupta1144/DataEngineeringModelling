# write a python program to get a string from a given string where all occurences of its first char have been changed to '$', except the first char itself.
string ="hello world, This is python class"
char=string[0]
new=string.replace(char,'$')
new_str=new[1:]
print(char+new_str)