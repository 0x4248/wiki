# Hello world in ARM Linux
Hello world in ARM64 [Linux](/Wiki/linux)

## Code
```assembly
.section .data
    msg:
        .ascii "Hello world\n"
        len = . - msg

.section .text
    .globl _start

_start:
    mov x0, 1
    ldr x1, =msg
    ldr x2, =len
    mov x8, 64
    svc 0
    mov x8, 93
    mov x0, 0
    svc 0
```

## Building
To build the program you will need build essential installed before running the commands.
```bash
as -o hello.o hello.s
ld -o hello hello.o
```