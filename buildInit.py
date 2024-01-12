from NekoMimi import utils as nm
import os

_ver = nm.read("./version.txt").split("\n")[0].strip()

_st = nm.read("./setuptemplate.py")
_st = _st.replace("<PLACEHOLDER>", _ver)

nm.write(_st, "./setup.py")

contents = nm.read("./NekoTPy/__init__.py").replace("XXXXX", _ver)

os.remove("./NekoTPy/__init__.py")

nm.write(contents, "./NekoTPy/__init__.py")
print(f"Built build process files v{_ver}")
