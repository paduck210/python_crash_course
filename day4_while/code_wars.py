# def bouncingBall(h, bounce, window):
#     if h > 0 and 1 > bounce > 0 and window < h:
#         count = 1
#         while h > window:
#             h *= bounce
#             count += 2
#         return(count - 2)
#     else:
#         return(-1)
#

def bouncingBall(h, bounce, window):
    if not 0 < bounce < 1: return -1
    count = 0
    while h > window:
        count += 1
        h *= bounce
        if h > window: count += 1
    return count or -1


print(bouncingBall(3, 0.66, 1.5)) # 3
print(bouncingBall(30, 0.66, 1.5)) # 15



