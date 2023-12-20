import re

def is_id_number(id_number):
    if len(id_number) != 18:
        print('身份证号码长度错误')
        return False
    regularExpression = "(^[1-9]\\d{5}(18|19|20)\\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\\d{3}[0-9Xx]$)|"

    if re.match(regularExpression, id_number):
        if len(id_number) == 18:
            n = id_number.upper()
            # 前十七位加权因子
            var = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
            # 这是除以11后，可能产生的11位余数对应的验证码
            var_id = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
            sum = 0
            for i in range(0, 17):
                sum += int(n[i]) * var[i]
            sum %= 11
            if (var_id[sum]) != str(n[17]):
                print("身份证号规则核验失败，校验码应为", var_id[sum], "，当前校验码是：", n[17])
                return False
        return True
    else:
        return False


if __name__ == '__main__':
    result = is_id_number(input())
    print(result)


#  本段代码摘自csdn中，本人对该正则表达式不理解，而且对身份证的校验规则也不甚了解，对此题无法下手

