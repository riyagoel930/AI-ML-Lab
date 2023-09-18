M1=3
M2=0
C1=3
C2=0
print("Rule of the Game are:-")
print("Rule1: One Missionery is selling boat from bank 1 to bank 2 ")
print("Rule2: Two Missionary are selling boat from Bank 1 to Bank 2 ")
print("Rule3: One Missionary and one Cannibal are selling boat from Bank1 to Bank2")
print("Rule4: One Cannibal boat frone Cannibal is selling boat from Bank 1 to Bank 2")
print("Rule5: Two Cannibal are selling boat from bank1 to Bank2")
print("Rule6: One Missionary is selling boat from bank 2 to bank 1")
print("Rule7: Two Missionary are selling boat from Bank 2 to Bank 1")
print("Rule8: One Missionary and One Cannibal are selling boat from bank 2 to bank 1")
print("Rule9: One Cannibal is selling boat from Bank 2 to Bank 1")
print("Rule10: Two Cannibals are selling boat from Bank2 to Bank 1")
while((M1!=3) or (M2 != 3)):
  r=int(input("Enter Rules: "))
  if(r==1):
    M1 = M1-1
    M2 = M2 + 1
  elif(r==2):
    M1=M1-2
    M2=M2+2
  elif(r==3):  
    M1=M1-1
    M2=M2+1
    C1=C1-1
    C2=C2+1
  elif(r==4):
    C1=C1-1
    C2=C2+1
  elif(r==5):
    C1=C1-2
    C2=C2+2
  elif(r==6):
    M2=M2-1
    M1=M1+1
  elif(r==7):
    M1=M1+2
    M2=M2-2
  elif(r==8):
    M1=M1+1
    M2=M2-1
    C1=C1+1
    C2=C2-1
  elif(r==9):
    C1=C1+1
    C2=C2-1
  elif(r==10):
    C1=C1+2
    C2=C2-2
  print(M1,C1)
  print(M2,C2)
  if((M1>0 and  M1<C1) or (M2>0 and  M2<C2)):
    print("dead")
    break
