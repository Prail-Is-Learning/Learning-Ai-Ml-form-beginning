name = "Prail @@02-- 00"
new_name = name.replace("@@02","").replace("--","").replace("00","")
print (new_name)

# In this branch i wil use loops to clean the data, i will remove duplicate names in a list 

names = ["Prail", "Abishek", "Prail", "Suman", "Abishek", "Suman", "Prail"]

clean_names = []

for name in names :
    if name not in clean_names:
        clean_names.append(name)

print(clean_names)

# Cleaning messy data given by chatGPT by using loops 

usernames = [
    "  PRAIL_123 ",
    "alex99",
    "BOB__GAMER ",
    "",
    "john doe",
    "alex99",
    "   COOLGUY   "
]

cleaned_names = []

for names in usernames:
    names = ( names.strip()
    .lower()#
    .title()
    .replace("_","")
    .replace("__","")
    .replace("123","")
    .replace("99","")
    )
    if names != "":
        cleaned_names.append(names)

print(cleaned_names)
