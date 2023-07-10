s = "III"
#s = "LVIII"
#s = "MCMXCIV"

dict_roman_dig = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

result = 0

if len(s) > 1:
    for i in range(0 , len(s)-1):
        if dict_roman_dig[s[i]] < dict_roman_dig[s[i+1]]:
            result -= dict_roman_dig[s[i]]
        elif dict_roman_dig[s[i]] >= dict_roman_dig[s[i+1]]:
            result += dict_roman_dig[s[i]]
    result += dict_roman_dig[s[i+1]]
elif len(s) == 1:
    result += dict_roman_dig[s[0]]
else:
    result = 0

print(result)

    # if s[i] == "M" and :
    #     dig += dict_roman_dig[]
    # if s[i] == "D":
    #     dig += 500
    # if s[i] == "C":
    #     dig += 100
    # if s[i] == "L":
    #     dig += 50
    # if s[i] == "X":
    #     dig += 10
    # if s[i] == "V":
    #     dig += 5
    # if s[i] == "I":
    #     dig+=1
