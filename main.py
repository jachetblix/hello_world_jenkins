s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
result = {}
result2 = {}
numbers = [c for c in s.split()]
for num in numbers:
    result[num] = result.get(num, 0) + 1
mx = (max(result.values()))
for key, value in result.items():
    if value == mx:
        result2[key] = result2.get(key, value)
mx2 = (min(result2))
print(mx2)
