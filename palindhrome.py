def isPalindrome(head):
    palindrome = False
    length = len(head)

    for i in range(length // 2):
        for j in range(-1, -(length//2), -1):
            if head[i] == head[j]:
                print(head[i], head[j])
                palindrome = True

    return palindrome