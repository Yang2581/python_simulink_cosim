import numpy as np
import matlab.engine
from matplotlib import pyplot as plt

my_engine = matlab.engine.start_matlab() # 在python中启动matlab
env_name = 'my_model2' # 文件名
my_engine.load_system(env_name)
my_engine.start_model_using_m(nargout=0) # 运行初始化的m文件

simulation_time = 10 # simulation time (s)
pause_time = 0.1
my_engine.set_param(env_name + '/pause_time', 'value', str(pause_time), nargout=0) # 初始化第一个内部暂停时间为1s
my_engine.set_param(env_name, 'StopTime', str(simulation_time), nargout=0) # 设定仿真截止时间
my_engine.set_param(env_name, 'SimulationCommand', 'start', nargout=0)

y = []

for i in range(simulation_time*10):
    my_engine.set_param(env_name + '/pause_time', 'value', str(pause_time + i*0.1), nargout=0)
    my_engine.set_param(env_name + '/my_value', 'value', str(i*0.01), nargout=0) # 设置需要改变的值
    my_engine.set_param(env_name, 'SimulationCommand', 'continue', nargout=0)
    sig = np.array(my_engine.eval('signal')).reshape(-1)
    sig = sig[-1]
    y.append(sig)

x = []
for i in range(len(y)):
    x.append(i)

plt.plot(x,y)
plt.show()