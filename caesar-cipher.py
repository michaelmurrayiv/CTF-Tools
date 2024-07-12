def main(): # caesar cipher (lowercase only)
  string = input("Enter the string: ").lower()
  for i in range(26):
    shifted_string = ''.join([chr((ord(c) - 97 + i) % 26 + 97) if 'a' <= c <= 'z' else c for c in string])
    print(f"Shift {i}: {shifted_string}")

if __name__ == "__main__":
  main()