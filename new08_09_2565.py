import random
monster = 100
hit = 0
CriticalHIT = ["N","H","SH","SSH"]
while monster > 0:
    choice = int(input("จงเลือก! \nAttack:กด1 \nSkill:กด2\n"))
    random1 = random.choice(CriticalHIT)
    if choice == 1:
       
        Attack = int(input("ใส่พลัง!!:"))
        
        if (random1=="N"):
            Attack*=1
            print ("normolHIT")
        if (random1=="H"):
            Attack*=2
            print ("critical!!")
        if (random1=="SH"):
            Attack*=4
            print ("criticalX4!!")
        if (random1=="SSH"):
            Attack*=8
            print ("criticalX8!!")
        monster = monster-Attack
        
        print("เลือดมอนสเตอร์เหลือ",monster)
    else:
        skill = 300
        if (random1=="SH"):
            skill*=4
            print ("criticalX4!!")
        if (random1=="SSH"):
            skill*=8
            print ("criticalX8!!")
        monster = monster-skill
        print("เลือดมอนสเตอร์เหลือ",monster)
    hit+=1
    
print ("มอนสเตอร์ตาย")
print ("จำนวนครั้งที่โจมตี",hit,"ครั้ง")
