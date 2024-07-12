def main():
  string = input("Enter the string: ")
  for i in range(26):
    print(f"Shift {i}: {''.join([chr((ord(c) - 65 + i) % 26 + 65) for c in string])}")

if __name__ == "__main__":
  main()