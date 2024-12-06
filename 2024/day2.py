def report_is_safe(report):
    diffs = [x - y for x, y in zip(report[:-1], report[1:])]
    return all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs)

def dampened_report_is_safe(report):
    return any(report_is_safe(report[:i] + report[i+1:]) for i in range(len(report)))

with open("day2.in", "r") as f:
    reports = [[int(level) for level in report.split()] for report in f]
    print(sum(1 for report in reports if report_is_safe(report)))
    print(sum(1 for report in reports if dampened_report_is_safe(report)))
