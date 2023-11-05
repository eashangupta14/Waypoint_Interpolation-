import numpy as np
from utils import utility, plot

orig_file = 'C:/Users/eashan/Desktop/Eashan/Masters/coures/csc276c/HW2/waypoints.csv'

# Loading 30 Hz Data
data_30 = np.loadtxt(orig_file,
                 delimiter=",", dtype=float)

# Plot Original Trajectory
plot(data_30[:,0],data_30[:,1])

old_frequency = 30
new_frequency = 0.2
type_inter = 'cubic'

d_rate = old_frequency/new_frequency
print(d_rate)

util_class = utility(int(d_rate))
util_class.downsample(data_30[:,0],data_30[:,1])
util_class.upsample(type_inter = type_inter)
util_class.cal_error()

print('Total error ', util_class.error)
print('Average error', util_class.avg_error)

plot(util_class.arr_x_up,
    util_class.arr_y_up,
    title_name = f'Trajectory plot from {new_frequency} Hz data interpolated using {type_inter} method')