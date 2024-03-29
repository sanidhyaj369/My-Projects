# num = {2,4,6,3,7}
# # num.add(9)
# # num.update([13,8])
# # num.add("add")
# # print(num)
# num.pop()
# num.pop()
# print(num)

# SET - un-ordered, un-changeble, doesn't allow duplicate values
# DICTONARY - ordered, changable, unique keys/ doesn't allow duplicate key, allow duplicate value

x = {"model":"splender", "brand":"hero", "cc":100, "hp":11, "color":"yellow"}

#change value
x["model"] = 'passion'

#show vlaues
print(x["brand"], x["color"], x["model"])

#formatting
for key, value in x.items():
    print(f"{key}:{value}")

y = {"roll":1, "name":"rakesh", "class":"python", "location":"indore", "result":"pass"}
print(y.keys())

#------------------------------------------------------------------------------------------------------------------------

