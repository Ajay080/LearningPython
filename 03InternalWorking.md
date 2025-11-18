# 📘 Python Memory Model & Data Types

### *Understanding Mutability, Object References & Variable Binding*

---

## 🚀 Overview

Python is a **dynamically typed**, **object-oriented** language where:

* ✔ Everything is an **object**
* ✔ Variables **do not store values**, only **references**
* ✔ Objects in memory **store the actual value and type**
* ✔ Some objects are **mutable**, others are **immutable**

This guide provides a visual and clear explanation of Python’s memory model and how variables, objects, and references work.

---

# 🎭 Mutable vs Immutable Types

## 🔒 Immutable Data Types

These **cannot be modified** after creation.

Examples:

| Type        | Examples           |
| ----------- | ------------------ |
| `int`       | `1`, `10`, `100`   |
| `float`     | `3.14`, `2.5`      |
| `str`       | `"hello"`          |
| `bool`      | `True`, `False`    |
| `tuple`     | `(1,2,3)`          |
| `frozenset` | `frozenset({1,2})` |
| `bytes`     | `b"abc"`           |

### Memory Visualization (Immutable)

```python
a = "hi"
b = a
a = a + "!"
```

```
 a ─────────────┐
                │
 b ─────────────┘──►  "hi"
 
 a ───────────────►  "hi!"
```

✔ New object created
✔ Old object unchanged
✔ `b` remains pointing to original `"hi"`

---

## 🔓 Mutable Data Types

These **can be modified in place**.

Examples:

| Type          | Examples                    |
| ------------- | --------------------------- |
| `list`        | `[1,2,3]`                   |
| `dict`        | `{"a":1}`                   |
| `set`         | `{1,2,3}`                   |
| `bytearray`   | `bytearray(b"abc")`         |
| Class objects | Instances of custom classes |

### Memory Visualization (Mutable)

```python
lst = [1, 2, 3]
x = lst
lst.append(4)
```

```
 lst ───┐
        │
 x ─────┘──►  [1, 2, 3, 4]   (same object modified)
```

✔ Same object
✔ Both references updated

---

# 🧠 Variables Have No Type — Objects Do

In Python:

* Variables are **labels** (names)
* Objects are **actual data containers**
* Variables **point** to objects

```python
x = 10     # x → int object
x = "hi"   # x → str object
x = [1]    # x → list object
```

✔ `x` changes references
✔ Data type is stored **in the object**, not in the variable

---

# 🗂 Python’s Memory Model (Object Reference System)

### 📌 Assignment = Name Binding

```
name ───► object
```

Example:

```python
x = 10
y = x
```

```
 x ───┐
      │
 y ───┘──► 10
```

---

### 📌 Immutable Example (New Object Created)

```python
x = 10
x = x + 5
```

```
 x ─────► 15 (new object)

 y ─────► 10 (old object)
```

---

### 📌 Mutable Example (Same Object Modified)

```python
a = [1,2]
a.append(3)
```

```
 a ───────────► [1,2,3]   (same object, new value)
```

---

# 🔁 Pass-by-Object-Reference

Python is:

* ❌ Not pass-by-value
* ❌ Not pass-by-reference
* ✔ **Pass-by-object-reference**
* ✔ Also called **pass-by-assignment**

Example:

```python
def update(lst):
    lst.append(100)

a = [1,2,3]
update(a)
```

```
 a ─────────► [1,2,3,100]
```

Function modifies the **same object** because lists are mutable.

---

# 🧱 How Python Creates Objects Internally

When you write:

```python
x = 5
```

Python internally:

1. Creates (or reuses) an integer object
2. Stores **value = 5**
3. Stores **type = <class 'int'>**
4. Allocates memory
5. Sets **reference count = 1**
6. Binds name `x` to that object

### Simplified PyObject Structure

```
PyObject {
    reference_count
    type_pointer  → <class 'int'>
    value         → 5
}
```

---

# 🗑 Reference Counting & Garbage Collection

Every object tracks how many references point to it.

```
x = 50
y = x
```

```
refcount(50) = 2
```

When references drop to zero:

```
refcount → 0  ⇒  object deleted
```

Python uses:

* **Reference counting**
* **Garbage collector** (handles cycles)

---

# 📚 Summary

| Concept                | Explanation                                   |
| ---------------------- | --------------------------------------------- |
| Everything is object   | All values are stored as objects              |
| Variables have no type | Only objects do                               |
| Mutable                | list, dict, set, class instances              |
| Immutable              | int, str, tuple, float                        |
| Assignment             | Name bound to object                          |
| Passing args           | Pass-by-object-reference                      |
| Modification           | Mutable → same object, Immutable → new object |

---

# 🎉 Quick Visual Cheat Sheet

```
[variable] → [reference] → [object in memory]
```

### Immutable:

```
x = 5
x = 6   → new object
```

### Mutable:

```
a = [1]
a.append(2)   → same object modified
```