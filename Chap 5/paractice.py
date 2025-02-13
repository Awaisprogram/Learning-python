for i in range(2,50):
    print(i)


days = []
for i in range(3):
  day = int(input(f"Enter days {i+1}: "))
  days.append(day)
  days.sort()
  print(f"\nMentioned number of days{days}")

  