def square(x):
 """This is docstring.""" #要用註解的話用docstring比comment好，因為python可以用
 return x ** 2
print(square.__doc__)"""運用這個屬性去印出docstring"""
print(square(7))