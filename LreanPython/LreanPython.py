from filecmp import dircmp


print("Hello,World!");



Age = 114514;
print(Age);



Age = 114514;
GetType = type(Age);
print(GetType);





#Lrean Convert Area
Age = "1";
print(type(Age));
a = int(Age);
print(type(a));
b = float(Age);
print(type(b));





#Lrean String Area
StringA = "Hello";
StringB = "World";
StringC = StringA+" "+StringB;
print(StringC);
age = 18;
PersonLog = f"[Log]: This Person Input Age Is: {age} Year Old";
print(PersonLog);





#Lrean Array Area
StrArray = ["A","B","C","D"];
print(StrArray[0]);
print(StrArray[1:3]);
print(StrArray[:3]);
print(StrArray[1:]);

Info = f"[INFO]: Array Lenght: {len(StrArray)}";
print(Info);

x = ["a","b"];
y = ["c","d"];
StrArray = x+y;

Info = f"[INFO]: Array Info: {StrArray[:]}";
print(Info);

StrArray = ["a","b"];
StrArray.append("A");
Info = f"[INFO]: Array Info: {StrArray[:]}";
print(Info);

StrArray.remove("A");
Info = f"[INFO]: Array Info: {StrArray[:]}";
print(Info);

IntArray = [3,5,7,11];
Info = f"[INFO]: Array Max Number: {max(IntArray)}";
print(Info);
Info = f"[INFO]: Array Min Number: {min(IntArray)}";
print(Info);

IntArray = [7,3];
Info = f"[INFO]: Array Sum Number: {sum(IntArray)}";
print(Info);

IntArray = [7,3,11,5];
Info = f"[INFO]: Array Sorted Number: {sorted(IntArray,reverse=False)}";
print(Info);

#empty
x = [];
y = list();

#Array 2
Verctor3D = (0,0,0);





#Lrean JSON ?
Json = {
        "Name":"ace",
        "Age":18,
        "UID":114514
    }
Info = f"[INFO]: Json info: {Json.get("Name")}";
print(Info);

Json["Name"] = "awfas";
Info = f"[INFO]: Json info: {Json.get("Name")}";
print(Info);

Info = f"[INFO]: Json info: {Json}";
print(Info);

Info = f"[INFO]: Json Lenght: {len(Json)}";
print(Info);

#JSON TO ARRAY
#you can use x.keys() to get string json
Info = f"[INFO]: Json Key(Name): {Json.keys()}";
Info = f"[INFO]: Json Values: {Json.values()}";

StrArray = list(Json.keys());
Info = f"[INFO]: Array info: {StrArray[:]}";
print(Info);
Array = list(Json.values());
Info = f"[INFO]: Array info: {Array[:]}";
print(Info);

#empty
Json = {};
Json = dict();





#Lrean Set Area (Possessing properties of mathematical "set")
IntSet = {1,2,3};
IntSet.discard(2);
Info = f"[INFO]: Set info: {IntSet}";
print(Info);
IntSet.remove(1);
Info = f"[INFO]: Set info: {IntSet}";
print(Info);
IntSetA = {0,1,2,3};
IntSetB = {4,1,5,3};
IntSet = IntSetA | IntSetB;
Info = f"[INFO]: Set info: {IntSet}";
print(Info);

IntSet = IntSetA - IntSetB;
Info = f"[INFO]: Set info: {IntSet}";
print(Info);

IntSet = IntSetA & IntSetB;
Info = f"[INFO]: Set info: {IntSet}";
print(Info);

#empty
IntSet = set();