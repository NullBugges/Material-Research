# Material-Research
Set up on 18/8/16 for Research 
这个程序的主要功能：

1. 读取当前目录下的 input.xlsx 文件
2. 获取第2列的英文内容
3. 调用SiliconCloud API进行翻译
4. 将翻译结果保存在新增的"中文翻译"列中
5. 最后将结果保存到 output.xlsx 文件
使用方法：

1. 将你的Excel文件重命名为 input.xlsx 并放在与程序相同的目录下
2. 安装必要的依赖：
```bash
pip install pandas requests 
 ```

3. 运行程序：
```bash
# 切换目录
cd D:\00python\API2research\test
# 运行程序
python translate_excel++.py
 ```

注意事项：

- 程序会在每次API调用之间添加1秒的延时，以避免请求过于频繁
- 确保Excel文件的第2列包含需要翻译的英文文本
- 如果遇到API错误，程序会打印错误信息并继续处理下一行
- 翻译结果将保存在新的 output.xlsx 文件中，原文件不会被修改
- 提炼结果将保存在新的 output_with_innovations.xlsx 文件中，原文件不会被修改
