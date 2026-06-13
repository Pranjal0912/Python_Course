import statistics as st

# The statistics module in python is used to perform mathematical statistics
# related operations like mean, median, mode, variance, standard deviation, etc.


# ------------------ mean() ------------------
# mean() gives the average value of the given data.

data = [10, 20, 30, 40, 50]

print(st.mean(data))

# Formula of mean:
# mean = sum of all values / total number of values


# ------------------ median() ------------------
# median() gives the middle value of the data after arranging it in sorted order.

data = [10, 40, 20, 50, 30]

print(st.median(data))

# Here python will first arrange the data internally:
# [10, 20, 30, 40, 50]
# So the middle value is 30.


# If total number of values are even then median is calculated by taking
# the average of the two middle values.

data = [10, 20, 30, 40]

print(st.median(data))

# Here middle values are 20 and 30.
# So median = (20 + 30) / 2 = 25


# ------------------ median_low() ------------------
# median_low() gives the lower middle value when the number of values are even.

data = [10, 20, 30, 40]

print(st.median_low(data))

# Here the two middle values are 20 and 30, so median_low() gives 20.


# ------------------ median_high() ------------------
# median_high() gives the higher middle value when the number of values are even.

data = [10, 20, 30, 40]

print(st.median_high(data))

# Here the two middle values are 20 and 30, so median_high() gives 30.


# ------------------ mode() ------------------
# mode() gives the value that occurs most number of times.

data = [10, 20, 20, 30, 40]

print(st.mode(data))

# Here 20 is repeated two times, so mode is 20.


# mode() can also be used with strings.

name = "banana"

print(st.mode(name))

# Here 'a' is repeated most number of times.


# ------------------ multimode() ------------------
# multimode() gives all the values that occur most number of times.

data = [10, 10, 20, 20, 30, 40]

print(st.multimode(data))

# Here 10 and 20 both are repeated two times, so both will be returned.
# multimode() always returns a list.


# ------------------ fmean() ------------------
# fmean() also gives the average value but it always returns the answer in float.

data = [10, 20, 30]

print(st.fmean(data))


# ------------------ geometric_mean() ------------------
# geometric_mean() is used when values are multiplied together or growth rate
# type data is given.

data = [2, 8]

print(st.geometric_mean(data))

# For [2, 8], geometric mean = square root of (2 * 8) = 4.0


# ------------------ harmonic_mean() ------------------
# harmonic_mean() is mostly used for average rate type questions.

speed = [40, 60]

print(st.harmonic_mean(speed))

# Harmonic mean is useful when we have to calculate average speed,
# average rate, etc.


# ------------------ variance() ------------------
# variance() tells how much the data is spread from the mean value.

data = [10, 20, 30, 40, 50]

print(st.variance(data))

# If variance is low, values are close to the mean.
# If variance is high, values are more spread out.


# ------------------ stdev() ------------------
# stdev() means standard deviation.
# It is the square root of variance.

data = [10, 20, 30, 40, 50]

print(st.stdev(data))


# ------------------ pvariance() and pstdev() ------------------
# pvariance() and pstdev() are used when the given data is the full population.
# variance() and stdev() are used when the given data is a sample.

data = [10, 20, 30, 40, 50]

print(st.pvariance(data))
print(st.pstdev(data))


# ------------------ quantiles() ------------------
# quantiles() divides the data into equal parts.

data = [10, 20, 30, 40, 50, 60, 70, 80]

print(st.quantiles(data, n=4))

# n=4 means data will be divided into 4 parts.
# These are called quartiles.


# ------------------ Important point ------------------
# Most functions of statistics module need numeric data.
# But mode() and multimode() can also work with non-numeric data like strings.


# ------------------ Example ------------------

marks = [78, 85, 90, 85, 72, 88, 90, 85]

print("Mean marks:", st.mean(marks))
print("Median marks:", st.median(marks))
print("Mode marks:", st.mode(marks))
print("All modes:", st.multimode(marks))
print("Standard deviation:", st.stdev(marks))
