def solution(nums):
    answer = 0
    final = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            answer += 1
            if answer > final:
                final = answer
        else :
            answer = 0
    return final

print(solution([1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]))
print(solution([0, 0, 1, 0, 1, 0, 0]))
print(solution([1, 1, 1, 1, 1]))
print(solution([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]))
