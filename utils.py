import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

class utility():
	"""Utility class 

	Containes functions like downsampling and all

	"""
	def __init__(self, arg):
		self.downsample_rate = arg
		print(self.downsample_rate)


	def downsample(self,arr_x,arr_y):
		self.arr_x_orig = arr_x
		self.arr_y_orig = arr_y
		self.arr_x_down= arr_x[::self.downsample_rate]
		print(self.arr_x_down.shape)
		self.arr_y_down = arr_y[::self.downsample_rate]
		time = []
		for i in range(arr_x.shape[0]):
			time.append(i)
		self.time_orig = np.array(time)
		#print(self.time_orig)
		self.time_down = self.time_orig[::self.downsample_rate]
		#print(self.time_down)


	def upsample(self,type_inter = 'linear'):
		inter_func_x = interp1d(self.time_down,self.arr_x_down, kind=type_inter)
		inter_func_y = interp1d(self.time_down,self.arr_y_down, kind=type_inter)
		final_time = self.time_orig.shape[0] - (self.time_orig.shape[0]%self.downsample_rate)
		#print(final_time) 
		#print(inter_func_x)
		self.arr_x_up = inter_func_x(self.time_orig[:final_time])
		#print(self.arr_x_up.shape)
		self.arr_y_up = inter_func_y(self.time_orig[:final_time])

	def cal_error(self):
		x_error = self.arr_x_up - self.arr_x_orig[:self.arr_x_up.shape[0]]
		y_error = self.arr_y_up - self.arr_y_orig[:self.arr_y_up.shape[0]]
		total_error = np.vstack((x_error,y_error)).T
		error_l2 = np.linalg.norm(total_error, axis = 1) 
		self.error = np.sum(error_l2)
		self.avg_error = self.error/self.arr_x_up.shape[0]

def plot(x,y, title_name = None):
    # Plotting x and y coordinates 
    # Create a line plot for the trajectory
    plt.plot(x, y, label='Trajectory', color='blue')

    for i in range(1,x.shape[0]-1,20):
        plt.annotate("", xy=(x[i], y[i]), xytext=(x[i-1], y[i-1]),
                     arrowprops=dict(arrowstyle="->", color='red', linewidth=1))

    # Add labels and a title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    if title_name is None:
    	plt.title('Trajectory Plot')
    else:
    	plt.title(title_name)

    # Show a legend
    plt.legend()

    # Show the plot
    plt.show()