# Common examples of dictionary use:
# 1. Translation of words
# 2. Rainfall for a year 
# Examples taken from exlskills.com

print("1st, we're gonna show how a"
+ "dictionary can store translations: \n")

english2spanish = {}
english2spanish['one'] = 'uno'
english2spanish['two'] = 'dos'

print(english2spanish)

print("\n now we're gonna show how it" + 
"can be used to store rainfall percentages"
+ " by year: ")

rain_percent = { 1980 : '17%', 1981 : '15%', 1982 : '10%'}


for i in rain_percent:
    print("Rain percentage in " + str(i) + 
    " was of " + rain_percent[i])


