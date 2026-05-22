name = "Prail @@02-- 00"
new_name = name.replace("@@02","").replace("--","").replace("00","")
print (new_name)
raw_data = ("Prail Üno  Coca lala  tasty")
clean_data = raw_data.split()
final = " ".join(clean_data)
print(final)

unclean = "Prail-Abishek-Kenji"
name1 , name2, name3 = unclean.split("-")
print(name1)
print(name2)
print(name3)