# Implement a function, that receives changeable number of dictionaries (keys - letters, values - numbers) and
# combines them into one dictionary. Dict values ​​should be summarized in case of identical keys
import InitTask11


def sum_dict(*dict_argument):

    for dic in dict_argument:
        dct = dict.fromkeys(dic)

    return print(dct)


sum_dict(InitTask11.dict1, InitTask11.dict2, InitTask11.dict3)