print("It's alright.")
print("He is called 'Johnny'")
print('He is called "Johnny"')

print("Multiline \n")

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor icididunt"""

print(a)
print("\n")

b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor icididunt'''

print(b)
print("\n")
print("Strings are arrays")

c = "Hello, world"

print(a[1])

print("\n")
print("Looping through a string")
for x in "banana":
    print(x)

print("\n")
print("String Length")
print(len(b))

print("\n")
print("Check string")

txt = "The best things in life are free!"
print("free" in txt)

print("\n")

if "free" in txt:
    print("Yes, 'free' is present.")

print("\n")

print("expensive" not in txt)
