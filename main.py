import heapq
import re
# def solution(name_list):
#     answer = []
#
#     for name in name_list:
#         ascii_int = 65
#         while 1:
#             new_name = name + chr(ascii_int)
#             if new_name in answer:
#                 ascii_int += 1
#             else:
#                 answer.append(new_name)
#                 break
#
#     return answer

# aa = solution(["김비바", "김비바", "이비바", "김토스", "이비바", "김비바"])

# def solution(seconds):
#     menu = {300: 10, 130: 30, 120: 20, 20: 30}
#     sort_menu = {}
#
#     for (key, value) in sorted(menu.items(), reverse=True):
#         sort_menu[key] = value
#
#     answer = 0
#
#     if seconds in sort_menu.keys():
#         return 1
#
#     while 1:
#         for sec in sort_menu.keys():
#             if seconds - sec >= 0 and sort_menu[sec] != 0 and seconds - sec - sort_menu[list(sort_menu.keys())[-1]] >= 0:
#                 answer += 1
#                 seconds = seconds - sec
#                 sort_menu[sec] -= 1
#                 break
#
#         if seconds == 0:
#             break
#
#     return answer

# def solution(scoville, K):
    # heap_scoville = []
    # answer = 0
    # for sco in scoville:
    #     heapq.heappush(heap_scoville, sco)
    #
    # def make_scoville(min, next_min):
    #     return min + (next_min * 2)
    #
    # while True:
    #     if len(heap_scoville) == 1 and heap_scoville[0] < K:
    #         return -1
    #     else:
    #         if heap_scoville[0] >= K:
    #             return answer
    #         else:
    #             mix_scoville = make_scoville(heapq.heappop(heap_scoville), heapq.heappop(heap_scoville))
    #             heapq.heappush(heap_scoville, mix_scoville)
    #             answer += 1

    # sorted_scoville = sorted(scoville, reverse=True)
    # answer = 0
    #
    # def make_scoville(min, next_min):
    #     return min + (next_min * 2)
    #
    # while True:
    #     if sorted_scoville[-1] >= K:
    #         return answer
    #     else:
    #         mix_scoville = make_scoville(sorted_scoville[-1], sorted_scoville[-2])
    #         for i in range(0, 2):
    #             sorted_scoville.pop()
    #         # sorted_scoville = sorted([mix_scoville] + sorted_scoville, reverse=True)
    #         sorted_scoville.append(mix_scoville)
    #         answer += 1


# def solution(jobs):
#     answer = 0
#     start = 0
#     jobs.sort(key=lambda x: x[1])
#     length = len(jobs)
#
#     while len(jobs) != 0:
#         for i in range(len(jobs)):
#             if jobs[i][0] <= start:
#                 start += jobs[i][1]
#                 answer += start - jobs[i][0]
#                 jobs.pop(i)
#                 break
#             if i == len(jobs) - 1:
#                 start += 1
#
#     return answer // length



# def solution(operations):
#     heap_min = []
#     heap_max = []
#     answer = [0, 0]
#
#     for operate in operations:
#         if re.compile(r'I\s*(\S+)').match((operate)):
#             value = int(re.compile(r'I\s*(\S+)').search(operate).group(1))
#             heapq.heappush(heap_min, value)
#             heapq.heappush(heap_max, (-value, value))
#         if re.compile(r'D\s(\S+)').match(operate):
#             if len(heap_min) > 0 and len(heap_max) > 0:
#                 if heap_min[0] == heap_max[0][1]:
#                     heapq.heappop(heap_min)
#                     heapq.heappop(heap_max)[1]
#
#             if len(heap_min) > 0 or len(heap_max) > 0:
#                 if re.compile(r'D\s(\S+)').search(operate).group(1) == '1':
#                     heapq.heappop(heap_max)[1]
#                 else:
#                     heapq.heappop(heap_min)
#
#     if len(heap_max):
#         answer[0] = heapq.heappop(heap_max)[1]
#
#     if len(heap_min):
#         answer[1] = heapq.heappop(heap_min)
#
#     return answer


# def solution(answers):
#     answer = []
#     heap = []
#     collect = {'a': 0, 'b': 0, 'c': 0}
#     a = [1, 2, 3, 4, 5]
#     b = [2, 1, 2, 3, 2, 4, 2, 5]
#     c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
#
#     a_init_idx, b_init_idx, c_init_idx = 0, 0, 0
#
#     for idx in range(len(answers)):
#         if idx % len(a) == 0:
#             a_init_idx = 0
#         if idx % len(b) == 0:
#             b_init_idx = 0
#         if idx % len(c) == 0:
#             c_init_idx = 0
#
#         if answers[idx] == a[a_init_idx]:
#             collect['a'] += 1
#
#         if answers[idx] == b[b_init_idx]:
#             collect['b'] += 1
#
#         if answers[idx] == c[c_init_idx]:
#             collect['c'] += 1
#
#         a_init_idx += 1
#         b_init_idx += 1
#         c_init_idx += 1
#
#     for key, val in collect.items():
#         heapq.heappush(heap, (-val, key))
#
#     while len(heap):
#         tmp_heap = heapq.heappop(heap)
#         answer.append(ord(tmp_heap[1]) - 96)
#         if len(heap) and tmp_heap[0] == heap[0][0]:
#             pass
#         else:
#             break
#
#     return answer


def solution(numbers):
    answer = 0
    arr = numbers.split()
    number_arr = []

    for idx in range(len(arr)):
        pass

    return answer


print(solution("17"))







