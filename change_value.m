function [clock] = change_value(x)
    set_param('my_model', 'SimulationCommand', 'pause');
    x = num2str(x);
    set_param('my_model/my_value', 'value', x); % 更改my_value模块的值（只接受字符）
    set_param('my_model', 'SimulationCommand', 'step'); % 运行一步
    clock = evalin('caller', 'times(end,:)');
    %返回系统仿真时间
end

