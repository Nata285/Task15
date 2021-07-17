
import datetime

from application.db.people import People
from application.salary import calculate_salary

if __name__ == '__main__':
  now = datetime.datetime.now()
  print("Current date and time: ")
  print(str(now))
  calculate_salary()
  People


