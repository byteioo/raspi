//生成树莓派系统信息图表的js
	function disk_info() {
        var sys_disk_canvers = echarts.init($("#sys_disk_canvers").get(0));
        // 指定图表的配置项和数据
        var disk_option = {
                title: {
                        text: 'DISK'
                },
                tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                                type: 'shadow'
                        }
                },
                //提示框组件
                legend: { //图例组件
                        data: [""] //图例的数据数组。数组项通常为一个字符串，每一项代表一个系列的 name
                },
                xAxis: { //直角坐标系 grid 中的 x 轴
                        data: ['总量( G )', "已使用( G )", "占比( % )"]
                },
                yAxis: {},
                series: [{ //系列列表
                        name: '',
                        //系列名称，用于tooltip的显示，legend 的图例筛选
                        color: ["#FF80AB"],
                        type: 'bar',
                        //类型
                        barWidth: 80,
                        itemStyle: {
                                normal: {
                                        label: {
                                                show: true,
                                                position: 'insideTop'
                                        }
                                }

                        },
                        data: ["{{disk_total}}", "{{disk_used}}", "{{disk_used_percentage}}"] //系列中的数据内容数组。数组项通常为具体的数据项
                }]
        };
        sys_disk_canvers.setOption(disk_option);
        window.onresize = function() {
                sys_disk_canvers.resize(); //屏幕变化时图标自适应
        }
	}

	function ram_info() {
        var sys_ram_canvers = echarts.init($("#sys_ram_canvers").get(0));
        var ram_option = {
                title: {
                        text: 'RAM'
                },
                tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                                type: 'shadow'
                        }
                },
                //提示框组件
                legend: { //图例组件
                        data: [""] //图例的数据数组。数组项通常为一个字符串，每一项代表一个系列的 name
                },
                xAxis: { //直角坐标系 grid 中的 x 轴
                        data: ['总量( M )', "已使用( M )", "剩余( M )"]
                },
                yAxis: {},
                series: [{ //系列列表
                        name: '',
                        //系列名称，用于tooltip的显示，legend 的图例筛选
                        color: ["#80DEEA"],
                        type: 'bar',
                        //类型
                        barWidth: 80,
                        itemStyle: {
                                normal: {
                                        label: {
                                                show: true,
                                                position: 'insideTop'
                                        }
                                }

                        },
                        data: ["{{ram_total}}", "{{ram_used}}", "{{ram_free}}"] //系列中的数据内容数组。数组项通常为具体的数据项
                }]
        };
        sys_ram_canvers.setOption(ram_option);
        window.onresize = function() {
                sys_ram_canvers.resize(); //屏幕变化时图标自适应
        }
	}

	function cpu_info() {
        // 基于准备好的dom，初始化echarts实例
        var sys_cpu_canvers = echarts.init($("#sys_cpu_canvers").get(0));
        // 指定图表的配置项和数据
        var cpu_option = {
                title: {
                        text: 'CPU'
                },
                tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                                type: 'shadow'
                        }
                },
                legend: {
                        data: [""]
                },
                xAxis: {
                        data: ['已使用( % )', "温度( ℃ )"]
                },
                yAxis: {},
                series: [{
                        name: '',
                        color: ["#81D4FA"],
                        type: 'bar',
                        barWidth: 80,
                        itemStyle: {
                                normal: {
                                        label: {
                                                show: true,
                                                position: 'insideTop'
                                        }
                                }

                        },
                        data: ["{{cpu_used}}", "{{cpu_temperature}}"]
                }]
        };
        sys_cpu_canvers.setOption(cpu_option);
        window.onresize = function() {
                sys_cpu_canvers.resize(); //屏幕变化时图标自适应
        }
	}

	function init_pi_info() {
        cpu_info();
        ram_info();
        disk_info();
	}