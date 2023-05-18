#Dictionary shorly dict is a data type were other data types like list,tupl,set has only value
#but dict has key and a value
val={'number':5,'name':'Naveen'}
print(val)
music={'rock':'Anirudh','melody':'yuvan','classic':'Rahman'}
print(music)
print(music['classic'])#to find a keyword use square brackets to find
#commonly dict support all data types
all={'int':50,'flo':9.9,'str':'code'}
print(all)
#we can able to modify values in dict 'only values'
music={'rock':'Anirudh','melody':'yuvan','classic':'Rahman'}
music['rock']='SPP'#here we can able to modify values of a keyword
music.pop('melody')#normally pop func uses index values here key word uses to remove the element
print(music)
#we can remove a keyword in dict

