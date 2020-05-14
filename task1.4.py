sample = {
    'physics' : 88, 'maths' : 75, 'chemistry' : 72, 'Basic electrical' :89
}


    
m = min(sample.values())
n = [key for key in sample if sample[key] == m]
print(f"The key with minimum value {m} is : {n[0]}")
