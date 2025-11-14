import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"

chars = lower + upper + nums
password = "".join(random.sample(chars, 10))
print(password)