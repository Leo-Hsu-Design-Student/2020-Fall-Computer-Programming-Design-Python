# Problem 5. Build Inventory - build_inventory() (20 pts)

def build_inventory(batches):
    # write your answer here
    # complete the function
    goods_dict={}#construct a dictionary
    for i in range(len(batches)):#construct the keys in the dicitonary
        goods_dict[batches[i][0]]=0
    for i in range(len(batches)):
        for key,quant in goods_dict.items():#see if there is already the same items in the dictionary
            if batches[i][0]==key:
                goods_dict[batches[i][0]]+=batches[i][1]#plus it 
    return goods_dict


if __name__ == '__main__':
    goods = [
        ('guava', 10), ('apple', 20), ('banana', 30),
        ('apple', 10)
    ]
    
    print(build_inventory(goods))
