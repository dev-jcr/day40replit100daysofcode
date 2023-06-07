# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python
myUser = {name:"Andy", "age":128, "age" = 129}

print(myUser{"name"})
```

<details> <summary> 👀 Answer </summary>

```python
myUser = {"name":"Andy", "age":128}

myUser["age"] = 129

print(myUser["name"])
```
- The key, `"name"`, needs to be in quotations.
- You can't have two keys with the same value.
- You need `[]` for your `print` statement. `{}` are only used to call the value.
</details>