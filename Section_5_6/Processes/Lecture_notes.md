# Lecture Notes 6: Pipes in C

## What is a Pipe?

A **pipe** is an IPC (Inter-Process Communication) mechanism that allows two related processes (usually parent and child) to communicate.

It acts like an **in-memory file** with a buffer:
- `fd[0]` → Read end
- `fd[1]` → Write end

---

## Creating a Pipe

```c
#include <unistd.h>

int fd[2];

if (pipe(fd) == -1) {
    perror("pipe");
    return 1;
}
```

- `pipe()` returns `0` on success and `-1` on failure.

---

## Important Rule

✅ **Always create the pipe before `fork()`.**

```c
pipe(fd);
fork();
```

This allows both parent and child to inherit the same pipe.

---

## Closing Unused Ends

If **Child → Parent** communication:

**Child:**
```c
close(fd[0]);      // Close read end
write(fd[1], &num, sizeof(num));
close(fd[1]);      // Done writing
```

**Parent:**
```c
close(fd[1]);      // Close write end
read(fd[0], &num, sizeof(num));
close(fd[0]);      // Done reading
```

Closing unused ends prevents resource leaks and signals EOF.

---

## Data Transfer

- `write()` → Sends data to the pipe.
- `read()` → Receives data from the pipe.

```c
write(fd[1], &num, sizeof(num));
read(fd[0], &num, sizeof(num));
```

---

## Error Handling

Always check system calls:

```c
pipe(fd);
fork();
read();
write();
```

Return value `-1` indicates an error.

---

## Required Header

```c
#include <unistd.h>
```

---

## Key Points

- Pipe is used for **parent-child communication**.
- `fd[0]` → Read end.
- `fd[1]` → Write end.
- Create the pipe **before** `fork()`.
- Close unused pipe ends.
- Use `read()` and `write()` for communication.
- Check for errors (`-1`).