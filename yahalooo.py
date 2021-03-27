import random

#value=randint(1,10)
#print(value)
#0.2
#print('    colossal cave')
#print('the First Adventure')
#name = input('what is your name?')
#role = input('What is your role?[Wizard,warrior,mage]')
#age =int(input('how old are your?' ))print('Hi','name','Wizard',role)
#if 20 years old and below considered young otherwise  old
#if age > 20:
#   print('You are old man')
#else:
#    print('You are quite young')
#playerHealth=random.randint(50,100)
#monsterHealth=random.randint(50,100)
#if playerHealth < monsterHealth:
#    print('your danger')
#elif monsterHealth == playerHealth:
#    print('you will make')
#else:
#   print('sure win')
"""
array
monstername = ["saad"]
monstername.append("hello")
monstername.append('storm terror')
mostername.remove('hello')
print(monstername)
"""
"""
mosters = ['saad','hello','strom terror']
for moster in mosters:
    print(moster)
mhealth = ['50','60','70']
for x in mHealth:
#moster is bleeding :['50']
#moster is bleeding :['60']
#moster is bleeding :['70']
print("moster is bleeding",str(x)) 
if mosterHealt%age > 5 & playerHealth <65:
    print('you got chances to get gold')
elif mosterHealt%age < 3 & playerHealth < 40:
    print('you got coins instead')
else:
    print('you got coins instead')
"""
print(textlogo+textinfo);

input("Press enter to continue  . . .");
os.system("cls");
print("Colossal Cave");
print("The First Adventure ");
name = input("What is your name ? ");
role = input("What is your role? [ Wizard,Warrior,Monk,Mage ] ? ");
passcheck = False;
if(role=="wizard"):
    passcheck = True;
if(role=="warrior"):
    passcheck = True;
if(role=="monk"):
    passcheck = True;
if(role=="mage"):
    passcheck = True;
if(passcheck):

    age = input("Your Age ? ");
    status = "";
    if(int(age)<=20):
        status = "young";
    else:
        status = "old";
    print("Welcome adventurer "+name+". Your assigned role is "+role+". You are "+status+". ");
    playerHealth = randint(50,100);
    monsterHealth = randint(50,100);

    print("Your Health : "+str(playerHealth) + "\t Monster Health : "+ str(monsterHealth));
    if(playerHealth< monsterHealth):
        print("Your in danger !");
    elif(playerHealth==monsterHealth):
        print("You will make it!");
    else:
        print("Your victory has been assured !");


    monsterHealthPoint = [50,40,20,10];

    for health in monsterHealthPoint:

        print("Monster is bleeding . Monster health is "+str(health));
else:
    print("Wrong role !");






