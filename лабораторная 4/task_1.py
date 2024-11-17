# TODO решите задачу
import json
def task():
    with open('input.json','r') as file:
        data = json.load(file)
        sum=0
        for i in data:
            sum+=i.get('score')*i.get('weight')
        return (round(sum,3))

print(task())
