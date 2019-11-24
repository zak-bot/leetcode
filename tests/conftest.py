#import pytest​
import pytest
from algo.easy_amzn.Solution import ListNode

@pytest.fixture(scope='session')
def linkedlist():
    def callback(start, end, step=1):
        head = ListNode(start)
        cur = head
        offset = 0
        if step is 1:
            offset = 1
        else:
            start -= 1
            end -= 1
        for i in range(start+offset, end+offset, step):
            cur.next = ListNode(i)
            cur = cur.next
        return head
    return callback

@pytest.fixture(scope='session')
def linkedlist_init_with_items():
    def callback(items):
        head = ListNode(items[0])
        cur = head
        for i in items[1:]:
            cur.next = ListNode(i)
            cur = cur.next
        return head
    return callback




# @pytest.fixture()
# def ​ tasks_just_a_few():
#        ​"""All summaries and owners are unique."""​
#         ​return​ (
#                       ​            Task(​'Write some code'​, ​'Brian'​, True),
# ​            Task(​"Code review Brian's code"​, ​'Katie'​, False),
# ​            Task(​'Fix what Brian did'​, ​'Michelle'​, False))
# ​
# ​
# ​
#
# @pytest.fixture()
#
# ​    ​
#
# def ​ tasks_mult_per_owner():
#
# ​        ​"""Several owners with several tasks each."""​
# ​        ​return​ (
#                       ​            Task(​'Make a cookie'​, ​'Raphael'​),
# ​            Task(​'Use an emoji'​, ​'Raphael'​),
# ​            Task(​'Move to Berlin'​, ​'Raphael'​),
# ​
# ​            Task(​'Create'​, ​'Michelle'​),
# ​            Task(​'Inspire'​, ​'Michelle'​),
# ​            Task(​'Encourage'​, ​'Michelle'​),
# ​
# ​            Task(​'Do a handstand'​, ​'Daniel'​),
# ​            Task(​'Write some books'​, ​'Daniel'​),
# ​            Task(​'Eat ice cream'​, ​'Daniel'​))
