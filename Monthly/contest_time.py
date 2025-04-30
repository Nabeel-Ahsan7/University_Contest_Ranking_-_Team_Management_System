from datetime import datetime, timedelta

def get_time(relative_time_seconds):
    time_until_contest_starts = abs(relative_time_seconds)
    need_announce = True
    remaining_days = time_until_contest_starts // 86400  # 86400 seconds in a day
    if remaining_days>0:
        need_announce = False
    remaining_seconds = time_until_contest_starts % 86400
    remaining_hours = remaining_seconds // 3600  # 3600 seconds in an hour
    remaining_minutes = (remaining_seconds % 3600) // 60  # 60 seconds in a minute
    remaining_seconds = remaining_seconds % 60
    remaining_day = remaining_days

    return f"The contest will start in approximately {remaining_days} days, {remaining_hours} hours, {remaining_minutes} minutes, and {remaining_seconds} seconds.",need_announce