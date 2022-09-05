# Problem 1. Simple Moving Average - sma() (20 pts)

def sma(data, n):
    # write your answer here
    # complete the function
    average_list=[]#build a list for the averages
    if n>len(data):#n is beyond the length of data, return[]
        return average_list
    else:
        for i in range(len(data)-n+1):#How many averages I have
            sum=0
            for j in range(i,i+n):#plus from different start
                sum+=data[j]
            average=round(sum/n)#calculate the average
            average_list.append(average)
        return average_list

if __name__ == '__main__':
    P = [100, 120, 118, 119, 121, 124, 130, 129, 132, 132]
    Q = [1, 3, 5, 7, 9]
    E = []

    print(sma(P, 3))
    print(sma(P, 7))
    print(sma(Q, 6))
    print(sma(Q, 4))
    print(sma(Q, 2))
    print(sma(Q, 1))
    print(sma(E, 1))
