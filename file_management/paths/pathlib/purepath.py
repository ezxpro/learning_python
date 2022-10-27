from pathlib import PurePath, PurePosixPath, PureWindowsPath

obj = PurePath('foo/bar')
print("pure path = ", obj)

print("posix path = ", PurePosixPath(obj))

# check if path is absolute
print(obj.is_absolute())

# check if path is relative
print(obj.is_)