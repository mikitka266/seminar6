#У вас есть код, который нельзя менять
#Написать лямбда выражение такое, чтобы 
values= [2,3,5,7,11,13,17,19,23,29]
#transformation = [x==values[i] for x in range(len(values)) for i in range(len(values))]
transformation=list.copy(values)
transformed_values=(map(transformation, values))
if values==transformed_values:
    print('ok')
else:
    print('fall')