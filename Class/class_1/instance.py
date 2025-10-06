from bird import *
print('\nClass instance;\n', Bird.__doc__)
polly = Bird('Squawk, squawk!!!')
print('\nNumber of b',  polly.count)
print("Polly says", polly.talk())
harry  = Bird('Tweeeet!')
print('\n Number of birds', harry.count)
print("Harry says:", harry.talk())
