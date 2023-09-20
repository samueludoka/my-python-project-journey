age = int(input("Enter your age: "))
heart_rate = 220 - age
resting_heart_rate = 13 * 6
heart_rate_reserve = 170 - resting_heart_rate
reserve_heart_rate = heart_rate_reserve * 0.5
target_heart_rate = resting_heart_rate + reserve_heart_rate
print(resting_heart_rate,"\n",heart_rate_reserve,"\n",reserve_heart_rate,"\n",target_heart_rate)