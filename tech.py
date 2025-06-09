import streamlit as st
import io
import contextlib
import re

# Page setup
st.set_page_config(page_title="Python Loop Runner", layout="centered")
st.title("Welcome to Aditi's Python🐍 Tech")

# Function to execute Python code and capture output
def run_code_block(code):
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        try:
            exec(code)
        except Exception as e:
            return f"❌ Error: {e}"
    return output.getvalue()

# Topic selection
topic = st.selectbox("🔍 Select a Topic", ["For Loop", "While Loop","LIST","dictonary"])

# ---------------- FOR LOOP ----------------
if topic == "For Loop":
    st.markdown("## 🔁 For Loop Examples")

    # Code Block 1
    st.markdown("### 🔹 Code Block 1: Basic Welcome Loop")
    code1 = """for i in range(3):
    print("Welcome", i)
print("This is outside the loop.")"""
    st.code(code1, language="python")
    if st.button("▶️ Run Code Block 1"):
        result = run_code_block(code1)
        st.text_area("🖨️ Output:", result, height=120)

    # Code Block 2
    st.markdown("### 🔹Code Block 2: Squares of Numbers")
    code2 = """for j in range(1, 4):
    print(j * j)"""
    st.code(code2, language="python")
    if st.button("▶️ Run Code Block 2"):
        result = run_code_block(code2)
        st.text_area("🖨️ Output:", result, height=100)

    # Code Block 3
    st.markdown("### 🔹 Code Block 3: Loop through List")
    code3 = """for k in [10, 20, 30]:
    print("Value of k is", k)"""
    st.code(code3, language="python")
    if st.button("▶️ Run Code Block 3"):
        result = run_code_block(code3)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 4
    st.markdown("### 🔹 Code Block 4:Print numbers from 1 to 10 using a for loop:")
    code4 = """for num in range(1, 11):
    print(num)"""
    st.code(code4, language="python")
    if st.button("▶️ Run Code Block 4"):
        result = run_code_block(code4)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 5
    st.markdown("### 🔹Calculate the sum of numbers from 1 to 10 using a for loop: ")
    code5="""sum_numbers = 0
    for num in range(1, 11):
    sum_numbers += num
    print(sum_numbers)"""
    st.code(code5, language="python")
    if st.button("▶️ Run Code Block 5"):
        result = run_code_block(code5)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 6
    
    st.markdown("### 🔹Calculate the sum of numbers from 1 to 10 using a for loop: ") 
     
    code6="""givennumber=10
sum=0
for i in range(1,givennumber+1): 
    sum+=i
print(sum)"""

    st.code(code6, language="python")
    if st.button("▶️ Run Code Block 6"):
        result = run_code_block(code6)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 7
    st.markdown("### 🔹Print numbers in reverse from 10 to 1 using a for loop :")
    code7="""for num in range(10, 0, -1):
    print(num)"""
    st.code(code7, language="python")
    if st.button("▶️ Run Code Block 7"):
        result = run_code_block(code7)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 8
    st.markdown("### 🔹Print characters of a string using a for loop:")
    code8= """my_string="hello"
for i in my_string:
  print(i)"""
    st.code(code8,  language="python")
    if st.button("▶️ Run Code Block 8"):
        result = run_code_block(code8)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 9
    st.markdown("### 🔹Print all uppercase letters in a string using a for loop:")
    code9="""my_string = "Hello World"
for char in my_string:
  if char.isupper():
    print(char)"""
    st.code(code9,  language="python")
    if st.button("▶️ Run Code Block 9"):
        result = run_code_block(code9)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 10
    st.markdown("### 🔹Count the number of vowels in a string using a for loop:")
    code10="""my_string = "Hello World"
vowels = "aeiou"
count = 0
for i in my_string.lower():
    if i in vowels:
        count += 1
print(count)"""
    st.code(code10,  language="python")
    if st.button("▶️ Run Code Block 10"):
        result = run_code_block(code10)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 11
    st.markdown("## 🔹even number find  if range is given")
    code11="""givenrange=10
for i in range(givenrange):
    if i%2==0:
        print(i)"""
    st.code(code11, language="python")
    if st.button("▶️ Run Code Block 11"):
        result = run_code_block(code11)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 12
    st.markdown("## 🔹if range is give then find out the odd number sum")
    code12="""givennumber=50
    sum=0
    for i in range(givennumber):
        if i%2!=0:
        sum+=i
    print(sum)"""
    st.code(code12,language="python")
    if st.button("▶️ Run Code Block 12"):
        result = run_code_block(code12)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 13
    st.markdown("## 🔹Enter a number and print its reverse")
    code13="""num=123
    reverse=0
    count= len(str(num))
    for i in range(count):
        digit=num % 10
        reverse= reverse * 10 + digit
        num= num // 10
    print( "reversed the number:",reverse)"""
    st.code(code13, language="python")
    if st.button("▶️ Run Code Block 13"):
        result = run_code_block(code13)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 14
    st.markdown("## 🔹sum of first and last digit in a number")
    code14="""num = input("Enter a number: ")
    first_digit = None
    last_digit = None

    for i in range(len(num)):
        if num[i].isdigit():  # Ensure only digits are considered (ignores negative sign)
            if first_digit is None:
                first_digit = int(num[i])
                last_digit = int(num[i])

            if first_digit is not None and last_digit is not None:
                print("Sum of first and last digit:", first_digit + last_digit)
            else:
                print("Invalid input.")"""

    st.code(code14, language="python")
    user_input_val = st.text_input("📥 Enter a number:")
    modified_code14 = re.sub(r'input\((.*?)\)', f'"{user_input_val}"', code14)

    if st.button("▶️ Run Code Block 14"): 
        result = run_code_block(modified_code14)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 15
    st.markdown("## 🔹program to swap first and last digit of a number")
    code15="""number = "1234"
first=number[0]
last=number[-1]
switched=last+number[1:-1]+first
print(switched)"""
    st.code(code15, language="python")
    if st.button("▶️ Run Code Block 15"):
        result = run_code_block(code15)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 16
    st.markdown("### 🔹print star pattern")
    code16="""line=int(input("enter the line"))
for i in range(1,line+1):
    print("*"*i)"""
    st.code(code16, language="python")
    user_input_val = st.text_input("📥 Enter a line:")
    modified_code16 = re.sub(r'input\((.*?)\)', f'"{user_input_val}"', code16)

    if st.button("▶️ Run Code Block 16"):
        result = run_code_block(modified_code16)
        st.text_area("🖨️ Output:", result, height=100)
   #code Block 17
    st.markdown("### 🔹calculate factorial of number")
    code17="""num= int(input("enter the nmber"))
factorial=1
for i in range(1,num+1):
    factorial*=i
print(factorial)"""
    st.code(code17,language="python")
    user_input_val = st.text_input("📥 Enter a number:", key="unique_input_1")

    modified_code17 = re.sub(r'input\((.*?)\)', f'"{user_input_val}"', code17)
    if st.button("▶️ Run Code Block 17"):
        result = run_code_block(modified_code17)
        st.text_area("🖨️ Output:", result, height=100)
        
    



    
    



    







                                                   
        
    
# ---------------- WHILE LOOP ----------------
elif topic == "While Loop":
    st.markdown("## 🔁 While Loop Examples")

    # Code Block 1
    st.markdown("### 🔹 Code Block 1: Count to 3")
    code1 = """count = 1
while count <= 3:
    print("Count is", count)
    count += 1"""
    st.code(code1, language="python")
    if st.button("▶️ Run While Loop Block 1"):
        result = run_code_block(code1)
        st.text_area("🖨️ Output:", result, height=100)

    # Code Block 2
    st.markdown("### 🔹 Code Block 2: Even Numbers Less Than 10")
    code2 = """num = 2
while num < 10:
    print(num)
    num += 2"""
    st.code(code2, language="python")
    if st.button("▶️ Run While Loop Block 2"):
        result = run_code_block(code2)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 3
    st.markdown("### A car is at a petrol station. It keeps filling fuel (1 litre at a time) until the fuel tank becomes full (capacity = 40 litres). Simulate the fuel filling process using a while loop, and print the fuel level after each litre is added.")
    code3="""fuel_capacity = 40  # total tank capacity
current_fuel = 0

while current_fuel < fuel_capacity:
    current_fuel += 1
    print(f"Filling fuel... Current fuel level: {current_fuel}L")

print("Tank is full!")"""

    st.code(code3, language="python")
    if st.button("▶️ Run While Loop Block 3"):
        result = run_code_block(code3)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 4
    st.markdown("### 🧼Hand Wash Timer (Hygiene Reminder)🧠 Logic: Decrease timer from 20 to 0.")
    code4="""seconds = 20

while seconds > 0:
    print(f"Keep washing... {seconds} seconds left")
    seconds -= 1
print("Great! You have washed your hands properly.")"""
    st.code(code4,language="python")
    if st.button("▶️ Run While Loop Block 4"):
        result = run_code_block(code4)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 5
    st.markdown("### PIN Verification System")
    code5="""correct_pin = "1234"
    attempts = 3

    while attempts > 0:
    entered_pin = input("Enter your 4-digit PIN: ")
    if entered_pin == correct_pin:
        print("Access granted.")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. {attempts} attempts left.")
    if attempts == 0:
    print("Card blocked. Please contact bank.")"""
    
    st.code(code5,language="python")
    user_input_val = st.text_input("📥 Enter a number:", key="unique_input_1")

    modified_code5= re.sub(r'input\((.*?)\)', f'"{user_input_val}"', code5)
    
    if st.button("▶️ Run While Loop Block 5"):
        result = run_code_block(modified_code5)
        st.text_area("🖨️ Output:", result, height=100)
#code Block 6
    st.markdown("### 💧 Water Tank Overflow Alert")
    code6="""tank_capacity = 100
current_level = 0

while current_level < tank_capacity:
    current_level += 10
    print(f"Water level: {current_level}L")

if current_level == tank_capacity:
    print("Tank is full.")
else:
    print("Overflow! Turn off the motor.")"""
    st.code(code6,language="python")
    
    if st.button("▶️ Run While Loop Block 6"):
        result = run_code_block(code6)
        st.text_area("🖨️ Output:", result, height=100)
        
        
        
        

#--------------------LIST CODE-------------------
elif topic == "LIST":

    st.markdown("## 🔁 LIST Examples")
    #code Block 1
    st.markdown("### print LIST ")
    code1="""a=[1,2,3,4,5];
for i in a:
    print(i)"""
    st.code(code1,language="python")
    if st.button("▶️ Run  LIST Block 1"):
        result = run_code_block(code1)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 2
    st.markdown("### marge in list")
    code2="""a=[10,20,30,40,50]
b=a[:]
print(b);
    """
    st.code(code2,language="python")
    if st.button("▶️ Run  LIST Block 2"):
        result = run_code_block(code2)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 3
    st.markdown("### find duplicate element in list")
    code3="""a=[1,2,2,3,4,4,5,6,6,7,8,8,9,9]
#duplicates=[]
counted=[]
for i in range(0,len(a)):
    if a[i] is not counted:
        count=1
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            count+=1
        if count>1:
            print(f"{a[i]}: {count}");
        counted.append(a[i])"""
    st.code(code3,language="python")
    if st.button("▶️ Run  LIST Block 3"):
        result = run_code_block(code3)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 4
    st.markdown("### find sum of all list element")
    code4="""n=[1,2,3,4,5]

total=sum(n)
print(total)"""
    st.code(code4,language="python")
    if st.button("▶️ Run  LIST Block 4"):
        result=run_code_block(code4)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 5
    st.markdown("### Find out maximum and minimum and minimum of a list")
    code5="""a=[22,16,17,18,19,20]
maximum=a[0]
minimum=a[0]
for num in a:

    if num>maximum:
        maximum=num
 

    if num<minimum:
        minimum=num 
print(maximum);

print(minimum)"""
    st.code(code5,language="python")
    if st.button("▶️ Run  LIST Block 5"):

        result=run_code_block(code5)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 6
    st.markdown("### find second largest in list")
    code6="""a=[10,20,30,40,50]
secondmaximum= max(a)
maximum=(a)-secondmaximum
print(max)"""
    st.code(code6,language="python")
    if st.button("▶️ Run  LIST Block 6"):
        result=run_code_block(code6)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 7
    st.markdown("### find out the even and odd of a list ")
    code7="""size=int(input("enter the size of list:"))
l=[]
l_e=[]
l_o=[]
count=0
for i in  range (size):
    ele=int(input("enter the element"))
    l.append(ele)
print("my_list=",l)
for i in l:
    if i%2==0:
        count+=1
        l_e.append(i)
    else:
        l_o.append(i)
print("even num list=",l_e)
print("odd num list=",l_o) 
print(count)"""
    st.code(code7,language="python")
    if st.button("▶️ Run  LIST Block 7"):
        result=run_code_block(code7)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 8
    st.markdown("### program to count frequency of each element in an list")
    code8="""a=[10,20,30,40,20]
count={}
for i in a:
    if i  in count:
        count[i]+=1
    else:
        count[i]=1

for key,value in count.items():
        print(key," = " ,value)"""
    st.code(code8,language="python")
    if st.button("▶️ Run  LIST Block 8"):
        result=run_code_block(code8)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 9
    st.markdown("### program  to delete an element from an array at specified position")
    code9="""a=[10,20,30,40]
b=int(input("enetr the position"))
new_a=[]
if 0 <=b<len(a):
    for i in range(len(a)):
        if i!=b:
            new_a.append(a[i])
            print(new_a);
else:
    print("invalid position")"""
    st.code(code9,language="python")
    user_input_val = st.text_input("📥 Enter a position:", key="unique_input_1")
    modified_code9= re.sub(r'input\((.*?)\)', f'"{user_input_val}"', code9)
    if st.button("▶️ Run  LIST Block 9"):
        result=run_code_block(modified_code9)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 10
    st.markdown("### program to find duplicate element in a list")


    code10="""mylist = [1, 2, 3, 2, 4, 5, 1, 6, 7, 5]

duplicates = []
for item in mylist:
    if mylist.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

print("Duplicate elements:", duplicates)"""
    st.code(code10,language="python")
    if st.button("▶️ Run  LIST Block 10"):
        result=run_code_block(code10)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 11
    st.markdown("###two seprate list find even and odd")
    code11="""a=[1,2,3,4,5,6,7,8]
b=[10,11,21,33,66,]
even=[]
odd=[]
for i in a:
    for j in b:
        if i%2==0:
            even.append(a)
            print("even",a)
        
else:
    odd.append(a)
    print("odd",odd)
if j%2==0:
    even.append(b)
    print(even);
else:
    j%2!=0
    odd.append(b)
    print("odd number",odd)"""
    st.code(code11,language="python")
    if st.button("▶️ Run  LIST Block 11"):
        result=run_code_block(code11)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 12
    st.markdown("find out unique element in list")
    code12="""my_list = [1, 2, 2, 3, 4, 4, 5, 1]
unique_elements = list(set(my_list))
print("Unique elements:", unique_elements)"""
    st.code(code12,language="python")
    if st.button("▶️ Run  LIST Block 12"):
        result=run_code_block(code12)
        st.text_area("🖨️ Output:", result, height=100)
        #code Block 13
    st.markdown("### list operation")
    code13="""a=[1,2,3,4,5,6,7,8,9]
#b=[3,4,5,6,7]
#print(a+b)#concation
#repetion
#
# print(a*5)
print(a[2:3:1])"""
    st.code(code13,language="python")
    if st.button("▶️ Run  LIST Block 13"):
        result=run_code_block(code13)
        st.text_area("🖨️ Output:", result, height=100)
# ---------------- dictonary ----------------
if topic == "dictonary":
    st.markdown("## 🔁 dictonary Examples")
    #code block 1
    st.markdown("### find dictonary key")
    code1="""a=[

  { "name":"aditi","age": 21},
  {
      "name":"aditi", "age":28
  }
]
print(a[0]['name'])"""
    st.code(code1,language="python") 
    if st.button("▶️ Run  LIST Block 1"):
        result=run_code_block(code1)
        st.text_area("🖨️ Output:", result, height=100) 
    #code Block 2 
    st.code("### movie program find salman actor and other logic")
    code2="""movies=[
    {
        "name":"race","year":2025,"actor":["salman","kat","saif"]
    },
    {
        "name":"ready","year":2022,"actor":["salman","prem","ashin"]

    },
    {
        "name":"ham sath sath hai ","year":2012,"actor":["salman","kat","srukh"]
    },
    {
        "name":"ham aapke  kon", "year":2016,"actor":["mohnish bahl","madhuri","reema"]
    },
    {
        "name":"animal","year":2025,"actor":["ranbir","rashmika","geetanjali"]
    },
]
#for i in movies:
    #print("movies name=",i["name"]);
#for i in movies:
    #print("movies name=",i["name"])
   # print("movie actors=",i["actor"])
for i in movies:
        if "salman" in i["actor"]:
             print("salaman movie=",i["name"]);
#for i in movies:
    #if i["year"]==2025:
    #if 2012<i["year"]<2019:
       #print("movienamein2025=",i["name"])""" 
    st.code(code2,language="python") 
    if st.button("▶️ Run  LIST Block 2"):
        result=run_code_block(code2)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 3
    st.code("### find the max of a dictonary ")
    code3="""a = {"a": 50, "b": 80, "c": 60, "d": 90}

# Extract values, sort them in descending order
sorted_values = sorted(a.values(), reverse=True)

# Get the second-largest value
second_largest = sorted_values[1]

print("Second largest value:", second_largest)"""

    st.code(code3,language="python") 
    if st.button("▶️ Run  LIST Block 3"):
        result=run_code_block(code3)
        st.text_area("🖨️ Output:", result, height=100)
    #code Block 4
    st.markdown("### sum of dictonary ")
    code4="""dis={"a":10,"b":21,"c":30}
result=1
for value in dis.values():
    #total+=1
     result *=value
#print("sum of dis",total)
print("multi of dis",result)"""
    st.code(code4,language="python") 
    if st.button("▶️ Run  LIST Block 4"):
        result=run_code_block(code4)
        st.text_area("🖨️ Output:", result, height=100)
    

            
       
    
    

       

    
        
   
    
        
    
    

    
    
    




    
        
    

# ---------------- CUSTOM CODE ----------------
# elif topic == "Custom Code":
#     st.markdown("## 🧪 Try Your Own Python Code")
#     custom_code = st.text_area("✍️ Paste your Python code here:", height=180, placeholder="for i in range(5):\n    print(i)")
#     if st.button("▶️ Run My Code"):
#         result = run_code_block(custom_code)
#         st.text_area("🖨️ Output:", result, height=150)

# st.info("💡 Select a topic to explore different loop examples or run your custom Python code.")













































































































# import  streamlit as st
# import io
# import contextlib
# st.title("welcome to aditi tech")
# st.header("python")
# st.subheader("java")
# st.markdown("i love python")
# st.title("🔁 For Loop Playground (Static Code by Developer)")
# user_code='''
# for i in range(3):
#     print("Welcome", i)

# print("This is outside the loop.")

# for j in range(1, 4):
#     print(j * j)

# for k in [10, 20, 30]:
#     print("Value of k is", k)
# st.markdown("### 🔍 Code Being Analyzed:")
# st.code(user_code, language='python')
# '''
# if st.button("▶️ Run Code"):
#     output_buffer = io.StringIO()
#     try:
#         with contextlib.redirect_stdout(output_buffer):
#             exec(user_code)
#         st.success("✅ Output:")
#         st.text(output_buffer.getvalue())
#     except Exception as e:
#         st.error(f"❌ Error: {e}")
#         if st.button("🔍 Dry Run"):
#             def dry_run(code):
#                 explanation = []
#                 lines = code.strip().split('\n')
#                 for line in lines:
#                  stripped = line.strip()
#                 if stripped.startswith('for') and 'in' in stripped:
#                     explanation.append("Loop detected: repeats over range/list.")
#                 elif stripped.startswith('print'):
#                     explanation.append("Prints something.")
#                 else:
#                     explanation.append(f"Other line: {stripped}")
#                 return '\n'.join(explanation) 
#             st.markdown("### 🧠 Dry Run Explanation:")
#     st.text(dry_run(user_code))
    


#     if st.button("🔁 Show Only For Loops"):
#         lines = user_code.split('\n')
#     loop_blocks = []
#     i = 0
#     while i < len(lines):
#         line = lines[i]
#         if line.strip().startswith("for "):
#             block = [line]
#             i += 1
#             while i < len(lines) and (lines[i].startswith(' ') or lines[i].startswith('\t')):
#                 block.append(lines[i])
#                 i += 1
#             loop_blocks.append('\n'.join(block))
#         else:
#             i += 1
    
#     if loop_blocks:
#         st.success("✅ All for-loops in the code:")
#         for loop in loop_blocks:
#             st.code(loop, language='python')
#     else:
#         st.info("No for loops found in the code.")




    






# # code = '''for i in range (1,5,1):
# #     print("hello")'''
             
# # st.code(code , language='python')
# # def dry_run(code):
# #    explanation=[]
# #    lines=code.strip().split('/n')
# #    for line in lines:
# #         stripped = line.strip()
# #         if stripped.startswith('for') and 'in range' in stripped:
# #             explanation.append("Loop using range: It will repeat from 1 to 4 (excluding 5).")
# #         elif stripped.startswith('print'):
# #             explanation.append("Prints 'hello' in each iteration.")
# #         else:
# #             explanation.append(f"Unknown line: {stripped}")
# #         return '\n'.join(explanation)
# # if st.button("Run code"):
# #     output_buffer = io.StringIO()
# #     try:
# #         with contextlib.redirect_stdout(output_buffer):
# #          exec(code)
# #          output=output_buffer.getvalue()
# #         st.success("output:")
# #         st.text(output)
# #         st.markdown("***Dry RUN")
# #         st.text(dry_run(code))
# #     except Exception as e:
# #         st.error(f"Error: {e}")