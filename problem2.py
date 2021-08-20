import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    if not isinstance(path,str):
      return "Path must be a string"

    elif not os.path.isdir(path):
      return f'{path} is not a valid directory'

    return _find_files(suffix, path, [])

def _find_files(suffix, path, file_list):
  explore_list = os.listdir(path)

  for address in explore_list:
    address = os.path.join(path,address)
    if os.path.isfile(address) and address.endswith(suffix):
      file_list.append(address)
    elif os.path.isdir(address):
      _find_files(suffix, address, file_list)
  
  return file_list


if __name__=='__main__':
  #Test Case 1:
  print("\nTest Case 1:")
  files = find_files(".c", ".")

  for item in files:
    print(item)

  # Returns
  # .\testdir\subdir1\a.c
  # .\testdir\subdir3\subsubdir1\b.c
  # .\testdir\subdir5\a.c
  # .\testdir\t1.c

  # Test Case 2:
  print("\nTest Case 2:")
  files = find_files(".c", 5)
  print(files)

  # Returns
  # Path must be a string

  # Test Case 3:
  print("\nTest Case 3:")
  files = find_files(".c", "Nonexistant_Directory")
  print(files)

  # Returns
  # Nonexistant_Directory is not a valid directory
