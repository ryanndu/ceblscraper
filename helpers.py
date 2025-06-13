def normalize_time(time_str):
        hours, minutes = map(int, time_str.split(":"))
        extra_hours, minutes = divmod(minutes, 60)
        hours += extra_hours
        return f"{hours}:{minutes:02d}"