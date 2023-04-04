import os

num = os.environ.get("INPUT_NUM")
if num:
    try:
        num = int(num)
    expect Exception:
        exit()
else:
    num = 1
    
print()
