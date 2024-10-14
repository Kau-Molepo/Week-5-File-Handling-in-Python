def write_to_file(filename, content):
  """Writes content to a new file in write mode."""
  try:
    with open(filename, 'w') as file:
      file.write(content)
      print(f"Successfully wrote to {filename}")
  except PermissionError:
    print("Error: Insufficient permission to write to the file.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

def read_from_file(filename):
  """Reads the contents of a file and displays them on the console."""
  try:
    with open(filename, 'r') as file:
      content = file.read()
      print(f"\nContents of {filename}:\n{content}")
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  except Exception as e:
    print(f"An unexpected error occurred while reading: {e}")

def append_to_file(filename, content):
  """Appends content to an existing file in append mode."""
  try:
    with open(filename, 'a') as file:
      file.write(content)
      print(f"\nSuccessfully appended to {filename}")
  except PermissionError:
    print("Error: Insufficient permission to append to the file.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Create the file
write_to_file("my_file.txt", "This is the first line.\n")
write_to_file("my_file.txt", "Here's the second line with a number: 42\n")
write_to_file("my_file.txt", "Adding another line for good measure.\n")

# Read the contents of the file
read_from_file("my_file.txt")

# Append additional lines
append_to_file("my_file.txt", "\nAppending some more text.\n")
append_to_file("my_file.txt", "This line is appended at the end.\n")
append_to_file("my_file.txt", "The final line - hooray!\n")