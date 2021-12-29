# Implement a function, that receives changeable number of dictionaries (keys - letters, values - numbers) and
# combines them into one dictionary. Dict values ​​should be summarized in case of identical keys
import InitTask11


def sum_dict(*dict_argument):
    # Функция обьеден словари в 1 и суммир их значения если ключи одинаковые

    out_dict = dict()
    for dic in dict_argument:
        for key in dic:
            try:
                out_dict[key] += dic[key]
            except KeyError:
                out_dict[key] = dic[key]

    return print(out_dict)


sum_dict(InitTask11.dict1, InitTask11.dict2, InitTask11.dict3,
         InitTask11.dict4, InitTask11.dict5, InitTask11.dict6,
         InitTask11.dict7, InitTask11.dict8, InitTask11.dict9,
         InitTask11.dict10, InitTask11.dict11, InitTask11.dict12,
         InitTask11.dict13, InitTask11.dict14, InitTask11.dict15)

# Данная программа принимает 15 словаоей из InitTask11 и затем последовательно подает их в функция,где обьеденяет их
# в один словарь (в случае одинаковых ключей их значение суммируется)
