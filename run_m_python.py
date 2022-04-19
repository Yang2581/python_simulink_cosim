import matlab.engine

my_engine = matlab.engine.start_matlab() # 在python中启动matlab
env_name = 'my_model'
my_engine.load_system(env_name)
my_engine.start_model_using_m(nargout=0) # 运行初始化的m文件

for i in range(5):
    clock = my_engine.change_value(float(2), nargout=1)
    print(clock)