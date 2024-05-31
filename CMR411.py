import pyperclip

# 输入的十六进制数列
vaild = input("是否需要查看运算过程?(y\\n)")
opening = input("输入前导固定指令")

if vaild == 'y':
    while True:
        hex1 = input("输入16进制指令部分")
        hex_list = hex1.split()
        hex_list2 = opening.split()
        hex_list_total = hex_list2 + hex_list
        print(f'你的输入是:{hex_list_total}')
        #求和
        hex_sum_dec = 0
        for num in hex_list_total:
            hex_sum_dec += int(num,16)
            
        print(f'转化为十进制求和{hex_sum_dec}')

        hex_sum = 0
        hex_sum = bin(hex_sum_dec)
        hex_sum = hex_sum[2:]
        print(f'转化为二进制{hex_sum}')
        #补0
        padding_length = 16 - len(hex_sum)
        padded_binary_number = '0' * padding_length + hex_sum
        print(f'补齐16位    {padded_binary_number}')

        #取反 加一
        bitwise_NOT = ''
        for i in padded_binary_number:
            if i == '1':
                bitwise_NOT += '0'
            elif i == '0':
                bitwise_NOT += '1'
        print(f'取反后的结果{bitwise_NOT}')

        result = bin(int(bitwise_NOT, 2) + 1)[2:]
        print(f'加一处理结果{result}')

        #转化为16进制
        decimal_number = int(result, 2)
        # 将整数转换为十六进制字符串
        hex_number = hex(decimal_number)
        hex2 = hex_number.upper()
        print(opening + ' ' + hex1 + ' ' + hex2[2:4] + ' ' +hex2[4:])
        finalstring = opening + ' ' + hex1 + ' ' + hex2[2:4] + ' ' +hex2[4:]
        pyperclip.copy(finalstring)
        print("结果已复制到剪切板")

if vaild == 'n':
    while True:
        hex1 = input("输入16进制指令部分")
        hex_list = hex1.split()
        hex_list2 = opening.split()
        hex_list_total = hex_list2 + hex_list
        print(f'你的输入是:{hex_list_total}')
        #求和
        hex_sum_dec = 0
        for num in hex_list_total:
            hex_sum_dec += int(num,16)
            
        #print(f'转化为十进制求和{hex_sum_dec}')

        hex_sum = 0
        hex_sum = bin(hex_sum_dec)
        hex_sum = hex_sum[2:]
        #print(f'转化为二进制{hex_sum}')
        #补0
        padding_length = 16 - len(hex_sum)
        padded_binary_number = '0' * padding_length + hex_sum
        #print(f'补齐16位    {padded_binary_number}')

        #取反 加一
        bitwise_NOT = ''
        for i in padded_binary_number:
            if i == '1':
                bitwise_NOT += '0'
            elif i == '0':
                bitwise_NOT += '1'
        #print(f'取反后的结果{bitwise_NOT}')

        result = bin(int(bitwise_NOT, 2) + 1)[2:]
        #print(f'加一处理结果{result}')

        #转化为16进制
        decimal_number = int(result, 2)
        # 将整数转换为十六进制字符串
        hex_number = hex(decimal_number)
        hex2 = hex_number.upper()
        print(opening + ' ' + hex1 + ' ' + hex2[2:4] + ' ' + hex2[4:])
        finalstring = opening + ' ' + hex1 + ' ' + hex2[2:4] + ' ' + hex2[4:]
        pyperclip.copy(finalstring)
        print("结果已复制到剪切板")
