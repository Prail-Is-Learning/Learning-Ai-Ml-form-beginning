name = "  Prail      "
new_name = name.strip()
print(new_name)

friend = "--Abishek__"
new_friend = friend.lstrip("--").rstrip("__")
print(new_friend)

got = " Pokemon   "
no = got.strip(" ")
print(no)

mess =   "  Hii!! My   name is PRAIL   😎 and I live in Kathmandu,,, Nepal! My phone number is 9876543210 and email is   prail123@@gmail..com  "
clean = mess.replace("ii","i").replace("!!","!").replace(" ", " ").replace("😎"," ").replace(",,, ",",").replace("@@", "@").replace("..",".").strip().replace("  ","")
print(clean)
