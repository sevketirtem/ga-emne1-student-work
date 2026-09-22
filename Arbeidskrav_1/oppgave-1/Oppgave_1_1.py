number_of_studies = int(input("Enter the number of the studies:  "))
length_of_each_study = int(input("Enter the number lenth in minutes:  "))
hour_total_time_used = (number_of_studies * length_of_each_study) // 60
minutes_total_time_used = (number_of_studies * length_of_each_study) % 60
total_time_used = (f"{hour_total_time_used } hours and {minutes_total_time_used} minutes")
print(f"Samlet tidsbrukt : {total_time_used}")