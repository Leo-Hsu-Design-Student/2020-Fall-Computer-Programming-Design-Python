# Problem 3. Competition Ranking - std_ranking() (20 pts)

def std_ranking(rec_file, name):
    # write your answer here
    # complete the function
    fobj=open(rec_file)#read the file
    line=fobj.readline#read the lines
    name_score_dict={}
    score=''
    name_str=''
    scores=[]
    for i in fobj:#make it  a dictionary to store names and scores
        name_str,score=i.split('=')
        name_score_dict[name_str]=int(score)
        scores.append(int(score))
    #make the scores and rank dictionary
    scores_sorted=sorted(scores,reverse=True)#make a new list for sorted scores
    ranks={}
    for i in range(len(scores_sorted)):#store the score and rank in the dictionary
        if i == 0:
            ranks[scores_sorted[i]]=1
        else:
            if scores_sorted[i]==scores_sorted[i-1]:
                ranks[scores_sorted[i]]=ranks[scores_sorted[i-1]]
            else:
                ranks[scores_sorted[i]]=i+1
    for name1,score1 in name_score_dict.items():#take it out the ranks of the names
        if name1==name:
            the_very_rank=ranks[name_score_dict[name]]
            break
        else:
            the_very_rank=-1#if there is no 'name', return -1
    return the_very_rank

if __name__ == '__main__':
    print(std_ranking('scores.txt', 'John'))
    print(std_ranking('scores.txt', 'Helen'))
    print(std_ranking('scores.txt', 'Tom'))
    print(std_ranking('scores.txt', 'Tim'))
