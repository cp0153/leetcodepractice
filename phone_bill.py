# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
import time
import operator
def solution(S):
    # write your code in Python 2.7
    # most_called_num = "nnn-nnn-nnnn"
    free_call = {}
    cost = 0
    s = S.split('\n')
    for line in s:
        line = line.split(',')
        duration = time.strptime(line[0], "%H:%M:%S")
        phone_number = line[1]
        free_call.update({phone_number: duration})

        # calculate cost of call before discount
        if duration.tm_min < 5:
            # pay 3 cents per second
            cost += ((int(duration.tm_min) * 60 * 3) + (int(duration.tm_sec) * 3))
        elif duration.tm_min >= 5:
            # pay 150 cents per min started
            cost = (int(duration.tm_min) * 150)
            if duration.tm_sec > 0:
                cost += 150
    # all calls to most called are free
    # most_called_duration = max(free_call.iteritems(), key=operator.itemgetter(1))[0]
    # discount = (int(most_called_duration.tm_min) * 150)
    return cost


print(solution("00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090"))
