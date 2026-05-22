# name = "Prail @@02-- 00"
# new_name = name.replace("@@02","").replace("--","").replace("00","")
# print (new_name)
raw_data = ("Prail Üno  Coca lala  tasty")
clean_data = raw_data.split()
final = " ".join(clean_data)
print(final)