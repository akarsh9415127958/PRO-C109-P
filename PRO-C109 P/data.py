import pandas as pd
import statistics
import csv

df = pd.read_csv("data.csv")

Wscore_list = df["writing score"].tolist()
Rscore_list = df["reading score"].tolist()
# mean for Rscore and Wscore
Wscore_mean = statistics.mean(Wscore_list)
Rscore_mean = statistics.mean(Rscore_list)
# finding one standard dev the start and the end values, second dev start and the end values
print("mean of the Rscore:-", Wscore_mean)
print("mean of the Wscore:-", Rscore_mean)


Rscore_std_deviation = statistics.stdev(Wscore_list)
Wscore_std_deviation = statistics.stdev(Rscore_list)
# 1,2,3 standard deviation for Rscore
Rscore_first_std_deviation_start, Rscore_first_std_deviation_end = Wscore_mean - \
    Rscore_std_deviation, Wscore_mean+Rscore_std_deviation
Rscore_second_std_deviation_start, Rscore_second_std_deviation_end = Wscore_mean - \
    (2*Rscore_std_deviation), Wscore_mean+(2*Rscore_std_deviation)
Rscore_third_std_deviation_start, Rscore_third_std_deviation_end = Wscore_mean - \
    (3*Rscore_std_deviation), Wscore_mean+(3*Rscore_std_deviation)

# 1,2,3 standard deviation for Wscore
Wscore_first_std_deviation_start, Wscore_first_std_deviation_end = Rscore_mean - \
    Wscore_std_deviation, Rscore_mean+Wscore_std_deviation
Wscore_second_std_deviation_start, Wscore_second_std_deviation_end = Rscore_mean - \
    (2*Wscore_std_deviation), Rscore_mean+(2*Wscore_std_deviation)
Wscore_third_std_deviation_start, Wscore_third_std_deviation_end = Rscore_mean - \
    (3*Wscore_std_deviation), Rscore_mean+(3*Wscore_std_deviation)

# Percentage of data within 1, 2 and 3 Standard Deviations for Wscore
Rscore_list_of_data_within_1_std_deviation = [
    result for result in Rscore_list if result > Wscore_first_std_deviation_start and result < Wscore_first_std_deviation_end]
Rscore_list_of_data_within_2_std_deviation = [result for result in Rscore_list if result >
                                              Wscore_second_std_deviation_start and result < Wscore_second_std_deviation_end]
Rscore_list_of_data_within_3_std_deviation = [
    result for result in Rscore_list if result > Wscore_third_std_deviation_start and result < Wscore_third_std_deviation_end]

# Percentage of data within 1, 2 and 3 Standard Deviations for Rscore
Wscore_list_of_data_within_1_std_deviation = [
    result for result in Wscore_list if result > Rscore_first_std_deviation_start and result < Rscore_first_std_deviation_end]
Wscore_list_of_data_within_2_std_deviation = [result for result in Wscore_list if result >
                                              Rscore_second_std_deviation_start and result < Rscore_second_std_deviation_end]
Wscore_list_of_data_within_3_std_deviation = [
    result for result in Wscore_list if result > Rscore_third_std_deviation_start and result < Rscore_third_std_deviation_end]

print("{}% of data for Rscore lies within 1 standard deviation".format(
    len(Wscore_list_of_data_within_1_std_deviation)*100.0/len(Wscore_list)))
print("{}% of data for Rscore lies within 2 standard deviations".format(
    len(Wscore_list_of_data_within_2_std_deviation)*100.0/len(Wscore_list)))
print("{}% of data for Rscore lies within 3 standard deviations".format(
    len(Wscore_list_of_data_within_3_std_deviation)*100.0/len(Wscore_list)))
