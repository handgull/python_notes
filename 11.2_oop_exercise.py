# fare una classe che estende list e se viene usato len() non importa quanti elementi abbia deve ritornare 1000
class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(list, object))
