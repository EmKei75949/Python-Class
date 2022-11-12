#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World")


# In[3]:


money = True

if money == True :
    print("택시를 타자")
else :
    print("걸어가자")


# In[6]:


money = 10000

if money >= 5000 :
    print("택시를 타자")
elif money >= 1000 :
    print("버스를 타자")
else :
    print("걸어가자")


# In[ ]:


# 학생의 성적을 입력 받아서 
# 점수가 90 이상이면 "A학점 입니다."
# 점수가 80 이상이면 "B학점 입니다."
# 점수가 70 이상이면 "C학점 입니다."
# 점수가 60 이상이면 "D학점 입니다."
# 나머지는 모두 "F학점 입니다."


# In[10]:


score = int(input("성적을 입력하세요 : "))

if score >= 90 :
    print("A학점")
elif score >= 80 :
    print("B학점")
elif score >= 70 :
    print("C학점")
elif score >= 60 :
    print("D학점")
else :
    print("F학점")


# In[11]:


# while

no = 10

while no >= 0 :
    print(no)
    no = no - 1


# In[13]:


prompt = "1. 덧셈 / 2. 뺄셈 / 3. 곱셈 / 4. 나눗셈 / 5. 종료"
no = 0

while no <= 4 :
    print(prompt)
    no = int(input())
    


# In[14]:


# while문의 경우에는 반복 횟수가 정확하지 않을 경우가 많기 때문에 조건에서 뿐만 아니라 중간에 반복을 종료시키는 방법도 필요하다.

no = 0

while no <= 10 :
    print(no)
    no = no + 1


# In[16]:


no = 0

while True :
    print(no)
    no = no + 1
    
    if no > 10 :
        break # while문 강종
        


# In[2]:


no = 1
sum = 0

while no < 100 :
    if no % 3 == 0 :
        sum = sum + no
        no = no + 1
    
    else no == 100 :
        break

print(sum)


# In[1]:


no = 1
sum = 0

while no <= 100 :
    if no % 3 == 0 :
        sum = sum + no
    
    no = no + 1  # no += 1
    
print(sum)


# In[4]:


# for 구문

for i in [1,2,3,4,5,6,7,8,9,10] :
    print(i)


# In[8]:


math = [80,90,70,70,100]

j = 1
for i in math : 
    if i >= 90 :
        print(j, "번째 학생은 합격입니다.")
    else :
        print(j, "번째 학생은 불합격입니다.")
    j += 1


# In[9]:


for i in [1,2,3,4,5,6,7,8,9,10] :
    print(i)


# In[10]:


for i in [1,2,3,4,5,6,7,8,9,10] :
    if i % 2 == 0 :
        print(i)


# In[11]:


for i in [1,2,3,4,5,6,7,8,9,10] :
    if i % 2 != 0 :
        continue
        
    print(i)


# In[12]:


# range 함수

# 숫자를 자동으로 생성해준다. for문과 함께 사용되는 경우가 아주 많다.

print(range(1,11))


# In[13]:


for i in range(1,11) : # 두 번째 숫자는 미만
    print(i)


# In[16]:


# for문으로 구구단 출력하기

for i in range(2,10) : # i 는 단을 표현
    for j in range(1,10) :
        print(i*j, end = "\t")
    print()


# In[36]:


for i in range(2,10) :
    for j in range(1,10) :
        print(i*j, end = "\n")
    print()


# In[40]:


# range를 사용하여 100 이하의 수 중 짝수들만의 합계를 구하세요

sum = 0

for i in range(1,101) :
    if i % 2 == 0 :
        sum += i
        
print(sum)        


# In[44]:


# range(start, stop, step)

# start를 생략하면 0에서 시작

# stop을 생략하면 1씩 증가

sum = 0

for i in range(0, 101, 2) :
    sum += i

print(sum)


# In[48]:


# 리스트 축약/내포 List Comprehension

# 리스트를 좀 더 편리하고 직관적으로 만드는 방법이다.

list1 = [1,2,3,4]
print(list1)

list2 = [num for num in list1]
print(list2)

list3 = [num*2 for num in list1]
print(list3)

list4 = [num for num in list1 if num % 2 == 0]
print(list4)


# In[51]:


no = 70

if no >= 70 :
    print("합격입니다")
else :
    print("불합격입니다")
    
"합격입니다"    if no >= 80   else "불합격입니다"    # True , 조건문, False


# In[ ]:




