# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## Printing with keys and fStrings
👉 Let's `run` this code and see what happens:

```python
myUser = {"name": "David", "age": 128}

print(f"Your name is {myUser["name"]} and your age is {myUser["age"]}")
```

<details> <summary> 👀 Answer </summary>

  - Note that we have to put the keys in **single quotation marks** `''` inside the fString when using this technique.

- This is because we've already used double quotes to start and end the fString. So, using `""` for the dictionary value would get Python all confuzzled.

```python
myUser = {"name": "David", "age": 128}

print(f"Your name is {myUser['name']} and your age is {myUser['age']}")

# This code outputs 'Your name is David and your age is 128'.
```
</details>

## Syntax error?

👉 Why are you getting a syntax error on the print statement line?


```python
myUser = {"name": "David", "age": 128}

print(myUser{"name"})
```

<details> <summary> 👀 Answer </summary>

- The `print` statement uses **square** brackets. Curly braces `{}` are only used to call the value.

```python
myUser = {"name": "David", "age": 128}

print(myUser["name"])
```

</details>

## Undefined?

👉 What is the problem here?
```python
myUser = {name: "David", "age": 128}

print(myUser["name"])
```

<details> <summary> 👀 Answer </summary>

The key, _name_, in the dictionary should be inside quotes.

```python
myUser = {"name": "David", "age": 128}

print(myUser["name"])
```
</details>

## Spare Key?

👉 What is the problem here?
```python
myUser = {name:"David", "age": 128, "age" = 129}

print(myUser)
```

<details> <summary> 👀 Answer </summary>

A dictionary can't have two keys with the same name. It always overrides the previous one. Therefore, the 129 overrides the age, 128.

```python
myUser = {name:"David", "age": 128}

myUser["age"] = 129

print(myUser)
```
</details>

