def get_average(func):
    items = func
    activities = []
    for item in items:
        activities.append(item["number_of_activities"])
    avg = sum(activities) / 8
    return avg


def get_max(func):
    items = func
    activities = []
    for item in items:
        activities.append(item["number_of_activities"])
    if len(activities) > 0:
        max_value = max(activities)
    else:
        max_value = 0
    return max_value


def get_sum(func):
    items = func
    activities = []
    for item in items:
        activities.append(item["number_of_activities"])
    sum_value = sum(activities)
    return sum_value