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


files = find_files(".c", ".")

for item in files:
	print(item)
