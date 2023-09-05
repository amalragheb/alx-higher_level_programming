#!/usr/bin/python3
for k in range(0, 10):
    for h in range(k + 1, 10):
        if k != h:
            if k != 8 or h != 9:
                print(f"{k}{h}, ", end="")
print(89)
