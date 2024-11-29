def check_for_null_byte(filename):
  """
  Opens a file in binary mode and checks for null bytes.

  Args:
      filename: The path to the file.

  Raises:
      ValueError: If a null byte is found in the file.
  """
  with open(filename, 'rb') as f:
    content = f.read()
    if b'\x00' in content:
      raise ValueError("Null byte found in the file")

# Example usage
try:
  check_for_null_byte('C:\\Users\\danmu\\Documents\\Notes academiques Business Information Technology\\BBIT 2.2\\Application Programming for the Intenet\\db_django\\db_django\\classicmodels\\models.py')
  print("No null bytes found")
except ValueError as e:
  print(e)