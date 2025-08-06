# Learn Python with 5 projects - from beginner to advanced
> By Tech With Tim on YouTube

<h4>5 projects are;</h4>

1. Choose your own Adventure game
2. Text-based calculator
3. Contact Management System
4. Tic Tac Toe (with an AI that can play against us)
5. Automated Quiz Generator and Grader

> Introduction to Python - Free resource by HubSpot

## Python installation and setup

- [Download python](https://www.python.org)
- In a command prompt | type `python`

> Download and install `visual studio code`

<hr>

### Create python file

- Write in a python file, `project.py`
  Use `.py` extension

#### Run Python files

> Extensions allow us execute the python code

- Install extensions
  - Python

- Python code
```python
print("Hello World!")
```

- Press `Ctrl + Shift + P` , this opens a search and search for `Python Select Interpreter`
- or
- Run `python3 name_of_file.py` or  `python name_of_file.py`



#### Write Python code

> - `print` - appends newline on every display.

<hr>

### Datatypes

#### 1. String
- In Python, strings are denoted by `str`
- String is anything surrounded by `""` or `''`

#### 2. Comments
- In In Python, comments are denoted by `#`


#### 3. Integer 
- In Python, integers are denoted by `int`
- Integer is a <u>whole number</u>
- -9, 0, 9, 100000000

#### 4. Float
- Float is a floating point number or any number that has some **decimal place** on it.
- 32.3, -9.03, 0, 

#### 5. Boolean
- True or False (must be written with capitalised first letter)

<hr>

#### Input statement
- Input statement is something that allows us to ask the user for input.
- Use a function called `input()`
- pass `arguments` inside the `()`
- Input() - pass a String which is known as the **`prompt`**
- Input always gives a **string**
```python
input("Hey, Type your name: ")
```

<hr>

### Variable
- Variable name must be either `upper/lower case letters`.
- Can't use any `special characters` other than __underscore__ or __numbers__
- Numbers in the variable name can only be __after the first character__
- Variables are case-sensitive; `Name="Lailah"` is different from `name="Sonia"`

```python
# variable
hello_ = 2
hello2 = "dance"
```
<hr>

#### NB:
> String Concatenation is only valid if all are string.
> ```python
> name = input("Hey type your name: ")
> print("Hello" +name + "Welcome to my game!")
>```
>
> OR
> ```python
> name = input("Hey type your name: ")
> print("Hello", name, "Welcome to my game!")
> ```

<hr>

### Condtitional statements
```python
if(some condition is equal to true): 
  then do this
```

example 1; `if`
```python
should_we_play = input("Do you want to play? ")

play = should_we_play == "yes"
#print(play)

if play:
    print("We are gonna play!")

```

example 2; `if --- else`
```python
if should_we_play == "yes":
    print("We are gonna play!")
else:
    print("We are NOT playing.........")
```

example 3; `if --- elif --- else`
> Only use `elif` after an `if`
```python
if should_we_play == "yes":
    print("We are gonna play!")
elif should_we_play == "YES":
    print("WE ARE GONNA PLAY!")
elif should_we_play == "Yes":
    print("We Are Gonna Play!")
else:
    print("We are NOT playing.........")
```

<h3>Chained Conditionals</h3>

> use the `and`, `or` , `not` operators
> - `and`: if both LHS and RHS is True, then True
> - `or` : if one True and other False, Then False
> - `not` : reverses the condition 
> not True is False

<hr>

### Operators
- 1 < 2 #True
- 1 != 2 #True
- 3 > 5 #False
- 1 == "1" #False
<h5>Assignment operator (=)</h5>

- "=" known as the Assignment operator
- It assigns some value to some variable

<h5>Equivalence operator (==)</h5>

- Checks if values on LHS is equal to those in the RHS

```python
if should_we_play == "yes" or should_we_play == "y":
    print("We are gonna play!")
```

<h5>Arithmetic operators</h5>

> +, -, *, /, %, **
> B E D M A S (Bracket, Exponents, Division, Multiplication, Addition, Subtraction)
>
> Can combine floats and int; `2.2 + 3`
> `5 % 3`

```python
operand = input("Number 1: ")
operand2 = input("Number 2: ")
Sign = input("Sign: ")

print(operand, sign, operand2)

# convert these strings to integers
#result = int(operand) + int(operand)
#print(result)

# Always convert into floats
result = float(operand) + float(operand)
print(result)
```

> `3 / 0` - It's called an **`edge case`**. 
> `edge case` - use case of your program that you weren't expecting
> This gives a `division by zero` error 
>
> - Add an if statement to prevent this `edge case` error


<hr>

<h5>Reserved methods</h5>

- `lower()` - converts strings to lowercase
- `upper()` - converts strings to uppercase

<hr>

### Loops
- While loop
```python
while condition:
  then this happens

# Example 
i=0
while i < 10:
  print(i)
  i = i+1

# Example 
j=0
while i <= 10:
  print(i)
  i = i+1
```

- Infinite loops
```python
# Example 
i=0
while True:
  print(i)
  i = i+1
```
- **break** : exits the loop
```python
# Example 
i=0
while True:
  print(i)
  i = i+1
  break
```
- **continue** : goes to the top of the loop
```python
# Example 
i=0
while True:
  print(i)
  i = i+1
  continue
  print("run")
```

<hr>

### Functions
- Function is a reusable block of code.
- Use `def` to create a function
- `def` stands for `define`
- `return` - give something out for the function. 
  - Return a value which can go back to the user.
- Functions are `callable` .
- **Callable** means they can run as many times as needed by simply writing the function name.
- Function immediately exits as soon as the return statement is reached.

<hr>
<hr>
<hr>
<hr>
<hr>
<hr>


## 1. Adventure game
- Ask user for their input
- Many choices to enter (options for the game)
- Use the following principles
  - input()
  - Conditional statements 
- let **prior choices** influence **future choices**

## 2. Text-based Calculator
- `Parse` an expression; `"5 + 7 - 6"`
- Use the following principles
  - Arithmetic operators
  - convert string to int - int()
  - try and catch, except
  - while loop

<h6>Option 1</h6>

```python
# option 1
#expression = input("Type an expression: ")
operand = input("Number 1: ")
operand2 = input("Number 2: ")
sign = input("Sign: ")

# check if the input is a number
# Use try and Catch
valid = False
try:
    operand = float(operand)
    operand2 = float(operand2)
    valid = True
except:
    print("Invalid input operand")

if valid:
  result = 0
    if sign == "+":
        result = float(operand) + float(operand)
    elif sign == "-":
        result = float(operand) - float(operand)
    elif sign == "/":
        if float(operand2) != 0:
            result = float(operand) / float(operand2)
        else:
            print("Division by Zero.") #type a custom error
    elif sign == "*":
        result = float(operand) * float(operand2)


  print(result)

#print(operand, sign, operand2)
```
<h6>Option 2</h6>

```python 
# Option 2
#expression = input("Type an expression: ")
operand = input("Number 1: ")
operand2 = input("Number 2: ")
sign = input("Sign: ")

# check if the input is a number
# Use try and Catch
try:
    operand = float(operand)
    operand2 = float(operand2)
    result = 0
    if sign == "+":
        result = float(operand) + float(operand)
    elif sign == "-":
        result = float(operand) - float(operand)
    elif sign == "/":
        if float(operand2) != 0:
            result = float(operand) / float(operand2)
        else:
            print("Division by Zero.") #type a custom error
    elif sign == "*":
        result = float(operand) * float(operand2)


    print(result)
except:
    print("Invalid input operand")

#print(operand, sign, operand2)


```

## 3. Contact Management System



## 4. Tic Tac Toe (with an AI that can play against us)



## 5. Automated Quiz Generator and Grader