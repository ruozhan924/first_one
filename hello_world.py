#!/usr/bin/env python3
def hello_world():
  print("Hello, World!")
  print("Welcome to Github!")
  return "Hello World"

if __name__ == "__main__":
  hello_world()
  
new_string = 'about-me-about-you'
print(new_string.replace('-', ' '))
print(new_string.replace('-', ' ', 2))
print(new_string.replace('about', 'with'))
print(new_string.replace('about', 'with', 1))
