def main():
    input = open("./input", "r")

    safe_reports = 0
    dampened_safe_reports = 0

    for line in input:
        report = line.split(" ")
### Part One ###
        if is_report_safe(report):
            safe_reports = safe_reports + 1
### Part Two ###
        if is_report_safe(run_problem_dampener(report)):
            dampened_safe_reports = dampened_safe_reports + 1

    print('Part 1: ' + str(safe_reports))
    print('Part 2: ' + str(dampened_safe_reports))


def is_report_safe(report: list):
    values = [int(i) for i in report]
    previous_value = values[0]
    previous_difference = 0
    for i in range(1, len(values), 1):
        current_value = values[i]
        difference = current_value - previous_value
        if ((abs(difference) > 3) or
            (abs(difference) == 0) or
            (difference > 0 and previous_difference < 0) or
            (difference < 0 and previous_difference > 0)):
            return False
        previous_value = current_value
        previous_difference = difference
    return True


def run_problem_dampener(report_to_be_dampened: list):
    for i in range(0, len(report_to_be_dampened), 1):
        if (is_report_safe(report_to_be_dampened)):
            return report_to_be_dampened
        else:
            dampened_report = report_to_be_dampened.copy()
            del dampened_report[i]
            if (is_report_safe(dampened_report)):
                return dampened_report
    return report_to_be_dampened


main()
