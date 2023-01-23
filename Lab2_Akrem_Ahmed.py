# problem 1

def changeSeconds(seconds):
    day = seconds // (24*3600)
    seconds = seconds - (day * 24*3600)
    hour = seconds // 3600
    reminderSeconds = seconds - (hour* 3600)
    minute = reminderSeconds // 60
    reminderSeconds = reminderSeconds - (minute*60)
    return (hour, minute, reminderSeconds,day)
seconds = int(input("Please Enter Seconds: "))
hour,minute,second,day = changeSeconds(seconds)
print(seconds,"seconds is", hour,"hours,",minute,"minutes,",second,"seconds")

#problem 2

def populationComputer(second):
    initalPopulation  = 334205119
    birth =  second //7
    death = second //13
    immigrant = second //35
    pop = initalPopulation+ birth + immigrant - death
    return pop
second = 0
second += 19* 24* 60 *60
second += 12* 60 * 60
second += 15 * 60
second += 20 
population = populationComputer(second)
print("On january 20, 2022 at 12:15:20 the US population was",population)

# problem 3

second1 = int(input("Enter seconds since beginning of year: "))
hour,minute,second,day= changeSeconds(second1) 
population = populationComputer(second1)
print(day,"days,", hour,"hours,",minute,"minutes,",second,"seconds after the start of 2022, the total population was,",population )

#problem 4

population = 334205119
numerator = (population + 350) ** 2
numerator -= 12
fraction = numerator // 50
whole = fraction ** (1/5)
print(int(whole))

