# Developing

To test the function, navigate to the `test/` directory. However, if importing the `Refinaid` package is unsuccessful, you can resolve this issue by adding the following code at the beginning of your test script. This code snippet allows you to return to the project root directory.

```py
import sys
from os.path import join
from os.path import dirname
from os.path import abspath

project_root = join(
    dirname(abspath(__file__)),
    '..', 
)
sys.path.append(project_root)
```