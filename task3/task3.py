import sys
import os
import re

def parse_log_line(line: str) -> dict:
    """ Парсинг рядка логу і повернення інформації про дату, рівень логування і повідомлення. """
    match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) ([A-Z]+) (.*)', line)
    if match:
        return {
            'timestamp': match.group(1),
            'level': match.group(2),
            'message': match.group(3).strip()
        }
    else:
        return None

def load_logs(file_path: str) -> list:
    """ Завантаження лог-файлу у список записів. """
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                log_entry = parse_log_line(line)
                if log_entry:
                    logs.append(log_entry)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except IOError:
        print(f"Error: Could not read file '{file_path}'.")
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    """ Фільтрація лог-записів за рівнем логування. """
    return [log for log in logs if log['level'] == level.upper()]

def count_logs_by_level(logs: list) -> dict:
    """ Підрахунок кількості записів за рівнем логування. """
    counts = {
        'INFO': 0,
        'DEBUG': 0,
        'ERROR': 0,
        'WARNING': 0
    }
    for log in logs:
        if log['level'] in counts:
            counts[log['level']] += 1
    return counts

def display_log_counts(counts: dict):
    """ Виведення статистики по рівнях логування у форматі таблиці. """
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17} | {count}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_logfile> [log_level]")
        return

    log_file = sys.argv[1]
    log_level = sys.argv[2].upper() if len(sys.argv) > 2 else None

    if not os.path.isfile(log_file):
        print(f"Error: File '{log_file}' not found.")
        return

    logs = load_logs(log_file)

    if logs:
        if log_level:
            filtered_logs = filter_logs_by_level(logs, log_level)
            print(f"Рівень логування | Кількість")
            print("-----------------|----------")
            for log in filtered_logs:
                print(f"{log['level']:<17} | {log['message']}")
        else:
            counts = count_logs_by_level(logs)
            display_log_counts(counts)

if __name__ == "__main__":
    main()

# python3 task3/task3.py task3/logfile.log - for running