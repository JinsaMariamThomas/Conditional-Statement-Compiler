# Control Flow Graph (CFG)
## Conditional Statement Compiler

### 1. Introduction

A Control Flow Graph (CFG) is a graphical representation of the order in which statements in a program are executed. It consists of nodes and directed edges.

### 2. Example Program

```c
if (a > 10) {
    x = 5;
} else {
    x = 0;
}
```

### 3. Control Flow

1. Start: The program begins.
2. Condition: Check whether `a > 10`.
3. True Branch: If the condition is true, execute `x = 5`.
4. False Branch: If the condition is false, execute `x = 0`.
5. End: Both branches join, and the program finishes.

### 4. Conclusion

The Control Flow Graph shows how an if-else statement chooses between two execution paths depending on whether the condition is true or false.



       START
         |
         v
    [ a > 10 ? ]
      /       \
   True       False
    |           |
    v           v
  [x = 5]    [x = 0]
      \         /
       \       /
         v
        END
