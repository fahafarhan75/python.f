def count_vowels():
    text = input("enter a text")
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    print(f"The number of vowels in the string is: {count}")

count_vowels()

num = 1
total = 0

while num <= 50:
    total += num
    num += 1

print(f"The sum of numbers from 1 to 50 is: {total}")

