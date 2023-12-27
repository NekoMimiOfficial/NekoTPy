from NekoMimi import tools as nm

_ver = nm.read("./version.txt").split("\n")[0]

_st = nm.read("./setuptemplate.py")
_st = _st.replace("<PLACEHOLDER>", _ver)

nm.write(_st, "./setup.py")

v_line = f"__version__ = '{_ver}'"
description = """
\"\"\"
Version of the NekoTPy module
more info in the telegram sub-module
\"\"\"
"""

contents = f"{v_line}{description}" 

nm.write(contents, "./NekoTPy/__init__.py")
print(f"Built build process files v{_ver}")
