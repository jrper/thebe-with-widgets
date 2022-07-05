---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3.8.8
  language: python
  name: python3
---

(launch:thebe)=
# An executable book page with widgets

This page demonstrates a widget-based teaching page leveraging Python to teach material in the theme of "computational thinking. It uses the executable book project and thebe frameworks to 

To see the examples  {fa}`rocket` --> {guilabel}`Live Code` button above on this page, and run the code below.

```{code-cell} ipython3
:tags: [hide-input, thebe-init]

from backend_code.gates import *
from operator import *
from IPython.display import display
```

AND is a logical operation which has two inputs, and one output. The output is FALSE unless both inputs are TRUE. This means that it works just like "and" in compound conditional statements in English
> We'll go to the park if you clean your room and do your homework.

```{code-cell} ipython3
display(gate(and_, 'AND'))
```
