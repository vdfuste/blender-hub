from time import ctime
from datetime import datetime, timedelta

def calculateTimeAgo(date):
	# Convert ctime strings to datetime objects
	current = datetime.strptime(ctime(), '%a %b %d %H:%M:%S %Y')
	date = datetime.strptime(date, '%a %b %d %H:%M:%S %Y')
	
	# Calculate the difference
	difference = current - date
	seconds = difference.total_seconds()
	
	# Determine the largest time unit for the difference
	if seconds < 60:
		unit = "second" if seconds == 1 else "seconds"
		value = seconds
	elif seconds < 3600:
		value = seconds // 60
		unit = "minute" if value == 1 else "minutes"
	elif seconds < 86400:
		value = seconds // 3600
		unit = "hour" if value == 1 else "hours"
	elif seconds < 604800:
		value = seconds // 86400
		unit = "day" if value == 1 else "days"
	elif seconds < 2592000:
		value = seconds // 604800
		unit = "week" if value == 1 else "weeks"
	else:
		# For months and years, calculate more accurately
		def months_between(current, date):
			return (current.year - date.year) * 12 + current.month - date.month

		def years_between(current, date):
			return current.year - date.year - ((current.month, current.day) < (date.month, date.day))

		months = months_between(current, date)
		years = years_between(current, date)

		if years >= 1:
			value = years
			unit = "year" if value == 1 else "years"
		else:
			value = months
			unit = "month" if value == 1 else "months"

	# Return the formatted string
	return f"{int(value)} {unit} ago"
