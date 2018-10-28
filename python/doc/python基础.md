![这里随便写文字](https://camo.githubusercontent.com/4dc1d0f95ee0f2dd487a27c595745fb97d9bc262/687474703a2f2f75706c6f61642d696d616765732e6a69616e7368752e696f2f75706c6f61645f696d616765732f373137383639312d336533613863366239633530343066632e706e673f696d6167654d6f6772322f6175746f2d6f7269656e742f7374726970253743696d61676556696577322f322f772f31323430)
* 对同一对象的双重引用

理解Python的引用的含义，数据是何时、如何、为何复制的，是非常重要的。尤其是当你用Python处理大的数据集时。

** 笔记：赋值也被称作绑定，我们是把一个名字绑定给一个对象。变量名有时可能被称为绑定变量。

当你将对象作为参数传递给函数时，新的局域变量创建了对原始对象的引用，而不是复制。如果在函数里绑定一个新对象到一个变量，这个变动不会反映到上一层。因此可以改变可变参数的内容。假设有以下函数：
```python

def append_element(some_list, element):
    some_list.append(element)
```
然后有：
```python

In [27]: data = [1, 2, 3]

In [28]: append_element(data, 4)

In [29]: data
Out[29]: [1, 2, 3, 4]
```

# 动态引用，强类型
与许多编译语言（如JAVA和C++）对比，Python中的对象引用不包含附属的类型。下面的代码是没有问题的：

```python
In [12]: a = 5

In [13]: type(a)
Out[13]: int

In [14]: a = 'foo'

In [15]: type(a)
Out[15]: str
```

变量是在特殊命名空间中的对象的名字，类型信息保存在对象自身中。一些人可能会说Python不是“类型化语言”。这是不正确的，看下面的例子：

```python
In [16]: '5' + 5
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-16-f9dbf5f0b234> in <module>()
----> 1 '5' + 5
TypeError: must be str, not int
```

在某些语言中，例如Visual Basic，字符串‘5’可能被默许转换（或投射）为整数，因此会产生10。但在其它语言中，例如JavaScript，整数5会被投射成字符串，结果是联结字符串‘55’。在这个方面，Python被认为是强类型化语言，意味着每个对象都有明确的类型（或类），默许转换只会发生在特定的情况下，例如：

 ```python
 In [17]: a = 4.5

In [18]: b = 2

# String formatting, to be visited later
In [19]: print('a is {0}, b is {1}'.format(type(a), type(b)))
a is <class 'float'>, b is <class 'int'>

In [20]: a / b
Out[20]: 2.25
```



# 鸭子类型
经常地，你可能不关心对象的类型，只关心对象是否有某些方法或用途。这通常被称为“鸭子类型”，来自“走起来像鸭子、叫起来像鸭子，那么它就是鸭子”的说法。例如，你可以通过验证一个对象是否遵循迭代协议，判断它是可迭代的。对于许多对象，这意味着它有一个__iter__魔术方法，其它更好的判断方法是使用iter函数：
```python

def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError: # not iterable
        return False
 ```
这个函数会返回字符串以及大多数Python集合类型为True：

```python
In [29]: isiterable('a string')
Out[29]: True

In [30]: isiterable([1, 2, 3])
Out[30]: True

In [31]: isiterable(5)
Out[31]: False
```
我总是用这个功能编写可以接受多种输入类型的函数。常见的例子是编写一个函数可以接受任意类型的序列（list、tuple、ndarray）或是迭代器。你可先检验对象是否是列表（或是NUmPy数组），如果不是的话，将其转变成列表：

```python
if not isinstance(x, list) and isiterable(x):
    x = list(x)
```


# 标量类型
Python的标准库中有一些内建的类型，用于处理数值数据、字符串、布尔值，和日期时间。这些单值类型被称为标量类型，本书中称其为标量。表2-4列出了主要的标量。日期和时间处理会另外讨论，因为它们是标准库的datetime模块提供的。


![Python的标量](https://camo.githubusercontent.com/3a5b6e40917f6036df659c7ed27478ce38748cf5/687474703a2f2f75706c6f61642d696d616765732e6a69616e7368752e696f2f75706c6f61645f696d616765732f373137383639312d323761333061633365376432363261312e706e673f696d6167654d6f6772322f6175746f2d6f7269656e742f7374726970253743696d61676556696577322f322f772f31323430)

