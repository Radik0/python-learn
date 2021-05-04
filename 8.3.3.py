def build_person(first_name, last_name, age=''):
    #    返回一个字典
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


while True:
    print('请输入你的个人信息')
    input
