# Process Creation using `fork()` and `wait()`

This directory contains C programs demonstrating fundamental Linux process management concepts. These examples help understand how processes are created, executed, synchronized, and terminated using system calls.

## Programs

### 1. Multiple `fork()` Example

**File:** `multiple_fork.c`

Demonstrates how multiple calls to `fork()` create multiple processes.

**Concepts Covered**

* Process creation using `fork()`
* Parent and child processes
* Process tree generation
* Non-deterministic execution order

---

### 2. Parent Waiting for Child

**File:** `wait_example.c`

Shows how the parent process waits for the child process before continuing execution.

**Concepts Covered**

* `wait(NULL)`
* Process synchronization
* Ordered execution
* Output buffering with `fflush(stdout)`

---

### 3. Process IDs and `wait()`

**File:** `process_id_wait.c`

Demonstrates retrieving process information and checking the return value of `wait()`.

**Concepts Covered**

* `getpid()`
* `getppid()`
* `wait()`
* Child process termination
* Return value of `wait()`

---

### 4. Waiting for Multiple Child Processes

**File:** `wait_all_children.c`

Creates multiple processes using two `fork()` calls and waits for every child process to finish before exiting.

**Concepts Covered**

* Multiple `fork()` calls
* Process hierarchy
* Waiting for all child processes
* `errno`
* `ECHILD`
* Detecting when no child processes remain

---

## System Calls Used

* `fork()`
* `wait()`
* `getpid()`
* `getppid()`
* `sleep()`
* `fflush()`

---

## Compile

```bash
gcc filename.c -o program
```

Example:

```bash
gcc wait_example.c -o wait_example
```

---

## Run

```bash
./program
```

Example:

```bash
./wait_example
```

---

## Learning Outcomes

After completing these programs, you will understand:

* How Linux creates new processes using `fork()`
* Difference between parent and child processes
* How process IDs (PID and PPID) work
* Why process execution order changes on different runs
* How `wait()` synchronizes parent and child processes
* How to wait for multiple child processes
* How `errno` and `ECHILD` are used to detect that all child processes have terminated
