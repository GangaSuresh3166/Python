# def generate_square(lst):
#     for item in lst:
#         yield item**2
# num_list=list(range(1,5))
# gen=generate_square(num_list)
# for n in gen:
#     print(n)



# def generate_square(lst):
#     for i in lst:
#         yield i**2
# num_list=list(range(1,5))
# gen=generate_square(num_list)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))



def generate_square(lst):
    for item in lst:
        yield item**2
num_list=list(range(1,5))
print(list(generate_square(num_list)))
