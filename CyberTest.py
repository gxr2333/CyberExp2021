alphabets = 'abcdefghijklmnopqrstuvwxyz'
def encrypt_caesar(num, text):
 result = ' '
 for k in text.lower():
  try:
    i = (alphabets.index(k) + num) % 26
    results += alphabets[i]
  except ValueError:
   results+= k
 return results.lower()
num =int(input("please input the shift:\t"))
text=input("please input the text: \t")
ciphertext = encrypt_caesar(num, text)
print(“Encoded text:”,ciphertext)

作者：迪鲁宾
链接：https://juejin.cn/post/7068235449529008164
来源：稀土掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
