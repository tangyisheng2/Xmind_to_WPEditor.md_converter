# xmind_to_WPEditor.md_converter

最近因为复习的原因，经常用Xmind做思维导图，然而发现Xmind导出的markdown格式思维导图和WPEditor.md的支援格式并不相同，因此写了这个小工具

## Requirement

Python >= 3.7

## Usage

From XMind Zen App, go to Share - markdown, save your mind app as FFT.md.

![image-20200427130738952](assets/image-20200427130738952.png)

Simply run the command

```
python .\converter.py
```

The script will print convert result and save the result as save.md in the same folder.

![image-20200427131114900](assets/image-20200427131114900.png)

Enjoy

![image-20200427131418453](assets/image-20200427131418453.png)

## Comparison

![image-20200427131302005](assets/image-20200427131302005.png)