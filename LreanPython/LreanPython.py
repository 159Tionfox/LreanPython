print("Hello,World!");



Age = 114514;
print(Age);



Age = 114514;
GetType = type(Age);
print(GetType);



Age = "1";
print(type(Age));
a = int(Age);
print(type(a));
b = float(Age);
print(type(b));



StringA = "Hello";
StringB = "World";
StringC = StringA+" "+StringB;
print(StringC);
age = 18;
PersonLog = f"[Log]: This Person Input Age Is: {age} Year Old";
print(PersonLog);



StrArray = ["A","B","C","D"];
print(StrArray[0]);
print(StrArray[1:3]);
print(StrArray[:3]);
print(StrArray[1:]);
Info = f"[INFO]: Array Lenght: {len(StrArray)}";
print(Info);
x = [];
y = list();
x = ["a","b"];
y = ["c","d"];
StrArray = x+y;
Info = f"[INFO]: Array Info: {StrArray[:]}";
print(Info);
StrArray = ["a","b"];
StrArray.append("A");
Info = f"[INFO]: Array Info: {StrArray[:]}";
print(Info);