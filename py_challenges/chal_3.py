# numbers 에서 숫지만 분류
# 숫자끼리 순서대로 더한 후 출력

numbers = [1, "💖", 2, "🔥", 3, "⭐️", 4, "💖", 5, "🔥", 6, "⭐️", 7, "💖", 8, "🔥", 9, "⭐️", 10, "💖", 11, "🔥", 12, "⭐️", 13, "💖", 14, "🔥", 15, "⭐️", 16]

sum = 0

for num in numbers:
    if not num == "💖" and not num == "🔥" and not num == "⭐️":
        sum = sum + num

print(sum)