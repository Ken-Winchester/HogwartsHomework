- Decimal翻译一下是十进制的意思
- 1.可以传递给Decimal整型或者字符串参数，但不能是浮点数据，因为浮点数据本身就不准确。
  - 传入浮点数 5.55

        In [74]: Decimal(5.55)*100
        Out[74]: Decimal('554.9999999999999822364316060')
  - 传入字符串 ‘5.55’

        In [75]: Decimal('5.55')*100
        Out[75]: Decimal('555.00')
- 2.要从浮点数据转换为Decimal类型
  - 
      from decimal import *
      Decimal.from_float(22.222)
      结果为Decimal('22.2219999999999995310417943983338773250579833984375')
- 3.通过设定有效数字，限定结果样式：
  - 
      from decimal import *
      getcontext().prec = 6
      Decimal(1)/Decimal(7)
      结果为Decimal('0.142857')，六个有效数字
- 4.四舍五入，保留几位小数
  - 
      from decimal import *
      Decimal('50.5679').quantize(Decimal('0.00'))
      结果为Decimal('50.57')，结果四舍五入保留了两位小数
- 5.Decimal 结果转化为string
  - 
      from decimal import *
      str(Decimal('3.40').quantize(Decimal('0.0')))
      结果为'3.40'，字符串类型

- 特别注意: todo 如果prec的长度比数字小的话，*100得出的数就不对了

      from decimal import *
      print(fetcontext()) #context(prec=28,rounding=ROUND_HALF_EVEN,Emin=-999999,Emax=999999,capitals=1,.....)  
      num,num1 = "12355","123.55"
      getcontext().prec = len(num) + 2
      print(Decimal(num1)*100 == Decimal(num))       true
      如果prec的长度比数字小的话，*100得出的数就不对了
      print(Decimal(num1)*100)                       1.24E+4
      print(Decimal(num1))                           123.55
      print(Decimal(num1)*100 == Decimal(num))       false
      print(Decimal(num))                            12355
