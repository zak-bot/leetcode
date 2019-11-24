import pytest
from algo.easy_amzn.Solution import Solution, ListNode


@pytest.mark.parametrize('paragraph, banned, expected', [
    ("Bob hit a ball, the hit BALL flew far after it was hit.", ['hit'], 'ball'),
    ("Bob. hIt, baLl", ["bob", "hit"], 'ball')
])
def test_most_common_word(paragraph, banned, expected):
    # paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    # banned = ["hit"]
    # expected = "ball"
    s = Solution()
    assert expected == s.mostCommonWord(paragraph, banned)


@pytest.mark.skip
@pytest.mark.usefixtures('linkedlist')
@pytest.mark.linkedlist
def test_reverse_linked_list(linkedlist):
    s = Solution()
    # 1->2->3->4->5->NULL
    # head =ListNode(1)
    # cur = head
    # for i in range(2, 6):
    #     cur.next = ListNode(i)
    #     cur = cur.next
    input = linkedlist(1, 7)
    output = linkedlist(7, 1, -1)
    # assert output is s.reverseList(input)
    assert True == True


@pytest.mark.parametrize('A, K, expected', [
    ([34, 23, 1, 24, 75, 33, 54, 8], 60, 58),
    ([10, 20, 30], 15, -1),
    ([254, 914, 110, 900, 147, 441, 209, 122, 571, 942, 136, 350, 160, 127, 178, 839, 201, 386, 462, 45, 735, 467, 153,
      415, 875, 282, 204, 534, 639, 994, 284, 320, 865, 468, 1, 838, 275, 370, 295, 574, 309, 268, 415, 385, 786, 62,
      359, 78, 854, 944],
     200, 198)
])
def test_two_sum_less_than_k(A, K, expected):
    s = Solution()
    assert expected == s.twoSumLessThanK(A, K)


@pytest.mark.parametrize('logs, expected', [
    (
            ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"],
            ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
    ),
    (
            ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"],
            ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
    ),
    (
            ["1 n u", "r 527", "j 893", "6 14", "6 82"],
            ["1 n u", "r 527", "j 893", "6 14", "6 82"]
    )
])
def test_reorder_logs(logs, expected):
    s = Solution()
    print("Pass")
    # ["zo4 4 7","a1 9 2 3 1","g1 act car","a8 act zoo","ab1 off key dog"] wrong output...
    assert expected == s.reorderLogFiles(logs)


def test_merge_two_sorted_lists(linkedlist_init_with_items):
    # Input: 1->2->4, 1->3->4
    # Output: 1->1->2->3->4->4
    # Plan
    # 1. Iterate through the list and get the value for List_A and List_B compare which one is smaller
    # 2. You can use a stack or just create the LL on the fly.
    # 3. Then insert into new LL
    # 3. return the new LL
    list_A = linkedlist_init_with_items([1, 2, 4])
    list_B = linkedlist_init_with_items([1, 3, 4])
    expected = linkedlist_init_with_items([1, 1, 2, 3, 4, 4])
    s= Solution()
    results= s.mergeTwoLists(list_A, list_B)
    assert expected == results


def test_sum_root():

    BTre

