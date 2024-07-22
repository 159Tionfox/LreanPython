#from filepath import function
from filecmp import dircmp

print("--------------------\t\n");
print("Hello,World!");
print("--------------------\t\n");





#Lrean Variable Area
Age = 114514;
print(Age);
print("--------------------\t\n");




#Show Variable
Age = 114514;
GetType = type(Age);
print(GetType);
print("--------------------\t\n");





#Lrean Convert Area
Age = "1";
print(type(Age));
a = int(Age);
print(type(a));
b = float(Age);
print(type(b));
print("--------------------\t\n");





#Lrean String Area
StringA = "Hello";
StringB = "World";
StringC = StringA+" "+StringB;
print(StringC);
age = 18;
PersonLog = f"[Log]: This Person Input Age Is: {age} Year Old";
print(PersonLog);
print("--------------------\t\n");





#Lrean Array Area
StrArray = ["A","B","C","D"];
print(StrArray[0]);
print(StrArray[1:3]);
print(StrArray[:3]);
print(StrArray[1:]);
print("\t\n");
Info = f"[INFO]: Array Lenght: {len(StrArray)}";
print(Info);
print("\t\n");
x = ["a","b"];
y = ["c","d"];
StrArray = x+y;
print("\t\n");
Info = f"[INFO]: Array Info: {StrArray[:]}";
print(Info);
print("\t\n");
StrArray = ["a","b"];
StrArray.append("A");
Info = f"[INFO]: Array Info: {StrArray[:]}";
print(Info);
print("\t\n");
StrArray.remove("A");
Info = f"[INFO]: Array Info: {StrArray[:]}";
print(Info);
print("\t\n");
IntArray = [3,5,7,11];
Info = f"[INFO]: Array Max Number: {max(IntArray)}";
print(Info);
Info = f"[INFO]: Array Min Number: {min(IntArray)}";
print(Info);
print("\t\n");
IntArray = [7,3];
Info = f"[INFO]: Array Sum Number: {sum(IntArray)}";
print(Info);
print("\t\n");
IntArray = [7,3,11,5];
Info = f"[INFO]: Array Sorted Number: {sorted(IntArray,reverse=False)}";
print(Info);
print("\t\n");
#empty
x = [];
y = list();

#Array 2
Verctor3D = (0,0,0);
print("--------------------\t\n");





#Lrean JSON ?
Json = {
        "Name":"ace",
        "Age":18,
        "UID":114514
    }
Info = f"[INFO]: Json info: {Json.get("Name")}";
print(Info);
print("\t\n");
Json["Name"] = "awfas";
Info = f"[INFO]: Json info: {Json.get("Name")}";
print(Info);
print("\t\n");
Info = f"[INFO]: Json info: {Json}";
print(Info);
print("\t\n");
Info = f"[INFO]: Json Lenght: {len(Json)}";
print(Info);
print("\t\n");
#JSON TO ARRAY
#you can use x.keys() to get string json
Info = f"[INFO]: Json Key(Name): {Json.keys()}";
Info = f"[INFO]: Json Values: {Json.values()}";
print("\t\n");
StrArray = list(Json.keys());
Info = f"[INFO]: Array info: {StrArray[:]}";
print(Info);
Array = list(Json.values());
Info = f"[INFO]: Array info: {Array[:]}";
print(Info);
print("\t\n");
#empty
Json = {};
Json = dict();
print("--------------------\t\n");





#Lrean Set Area (Possessing properties of mathematical "set")
IntSet = {1,2,3};
IntSet.discard(2);
Info = f"[INFO]: Set info: {IntSet}";
print(Info);
print("\t\n");
IntSet.remove(1);
Info = f"[INFO]: Set info: {IntSet}";
print(Info);
print("\t\n");
IntSetA = {0,1,2,3};
IntSetB = {4,1,5,3};
IntSet = IntSetA | IntSetB;
Info = f"[INFO]: Set info: {IntSet}";
print(Info);
print("\t\n");
IntSet = IntSetA - IntSetB;
Info = f"[INFO]: Set info: {IntSet}";
print(Info);
print("\t\n");
IntSet = IntSetA & IntSetB;
Info = f"[INFO]: Set info: {IntSet}";
print(Info);
print("\t\n");
#empty
IntSet = set();
print("--------------------\t\n");





#Lrean Control Area
IntArray = [1,3,5,7,9];
for n in IntArray:
    print(n);
    print("\t\n");
if 1 < 5:
    print("1 < 5");
else:
    print("1 > 5");

'''
>
<
>=
<=
==
!=
in
and
or
not in

'''
print("\t\n");
Json = {
        "Name":"ace",
        "Age":18,
        "UID":114514
    }
for Key,Values in Json.items():
    print(f"{Key} : {Values} \t");
print("\t\n");
for x in range(5,9):
    print(x);

print("\t\n");
    
for x in range(10):
    if x % 2 == 0:
        continue;
    else:
        print(x);
print("--------------------\t\n");





#Lrean Function Area
def Number(a,b):
    return a+b,a-b;

a,b = Number(9,1)
print(a);
print(b);
print("--------------------\t\n");





#Lrean Class Area
class Person:
    def __init__(self,name,location):
        self.name = name;
        self.location = location;
p1 = Person("A",10);
p2 = Person("B",20);
print(p1.name);
print(p2.location);