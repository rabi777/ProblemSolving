import time

data = []
c = {}
d = {}
speed = 0
min_speed = 0
pre_distance_time_1 = []
pre_distance_speed_1 = []
pre_distance_1 = 0
pre_distance_2 = 0
time_per_speed = []
speed_per_hour = []
j = 0
i = 0
while True:
    try:
        a = input()
        if a != '':
            data.append(a)
        else:
            break
    except:
        break
k = [str(s) for s in data]
for a in k:
    if (' ' in a) == True and a != '':
        j += 1
        time_per_speed.clear()
        speed_per_hour.clear()
        e, f = a.split()
        time_per_speed.append(e)
        speed_per_hour.append(f)
        if i > 0:
            start_speed = int(pre_distance_speed_1[0])
            c_time = time.strptime(time_per_speed[0], '%H:%M:%S')
            s_time = time.strptime(pre_distance_time_1[0], '%H:%M:%S')
            h_m = int(c_time.tm_hour) - int(s_time.tm_hour)
            min = int(c_time.tm_min) - int(s_time.tm_min)
            s_m = int(c_time.tm_sec) - int(s_time.tm_sec)
            if h_m != 0 and h_m > 0 or min != 0 and min > 0:
                hour_to_min = h_m * 60
                sec_to_min = s_m / 60
                total_min = hour_to_min + min + sec_to_min
                pre_distance_1 = (start_speed / 60) * total_min
                pre_distance_speed_1.clear()

        i += 1
    elif a != '':
        if j > 0:
            pre_distance_time_1.clear()
            pre_distance_speed_1.clear()
            pre_distance_time_1.append(a)
            start_time = time_per_speed[0]
            start_speed = int(speed_per_hour[0])
            pre_distance_speed_1.append(start_speed)
            c_time = time.strptime(a, '%H:%M:%S')
            s_time = time.strptime(start_time, '%H:%M:%S')
            h_m = int(c_time.tm_hour) - int(s_time.tm_hour)
            min = int(c_time.tm_min) - int(s_time.tm_min)
            s_m = int(c_time.tm_sec) - int(s_time.tm_sec)
            if h_m != 0 and h_m > 0 or min != 0 and min > 0:
                hour_to_min = h_m * 60
                sec_to_min = s_m / 60
                total_min = hour_to_min + min + sec_to_min
                speed = (start_speed / 60) * total_min
                m_speed = '%.2f' % speed
                if min_speed == start_speed:
                    print(a, m_speed, "km")
                    pre_distance_2 = speed
                else:
                    m_speed = speed + pre_distance_1 + pre_distance_2
                    m_distance = '%.2f' % m_speed
                    print(a, m_distance, "km")
            min_speed = start_speed
        else:
            pass
    #
    #
    # if (' ' in a) == True and a != '':
    #     j += 1
    #     time_per_speed.clear()
    #     speed_per_hour.clear()
    #     e, f = a.split()
    #     time_per_speed.append(e)
    #     speed_per_hour.append(f)
    #     if i > 0:
    #         start_speed = int(pre_distance_speed_1[0])
    #         c_time = time.strptime(time_per_speed[0], '%H:%M:%S')
    #         s_time = time.strptime(pre_distance_time_1[0], '%H:%M:%S')
    #         h_m = int(c_time.tm_hour) - int(s_time.tm_hour)
    #         min = int(c_time.tm_min) - int(s_time.tm_min)
    #         s_m = int(c_time.tm_sec) - int(s_time.tm_sec)
    #         if h_m != 0 and h_m > 0 or min != 0 and min > 0:
    #             hour_to_min = h_m * 60
    #             sec_to_min = s_m / 60
    #             total_min = hour_to_min + min + sec_to_min
    #             pre_distance_1 = (start_speed / 60) * total_min
    #             pre_distance_speed_1.clear()
    #
    #     i += 1
    # else:
    #     if j > 0:
    #         pre_distance_time_1.clear()
    #         pre_distance_speed_1.clear()
    #         pre_distance_time_1.append(a)
    #         start_time = time_per_speed[0]
    #         start_speed = int(speed_per_hour[0])
    #         pre_distance_speed_1.append(start_speed)
    #         c_time = time.strptime(a, '%H:%M:%S')
    #         s_time = time.strptime(start_time, '%H:%M:%S')
    #         h_m = int(c_time.tm_hour) - int(s_time.tm_hour)
    #         min = int(c_time.tm_min) - int(s_time.tm_min)
    #         s_m = int(c_time.tm_sec) - int(s_time.tm_sec)
    #         if h_m > 0 or min > 0 or s_m > 1:
    #             hour_to_min = h_m * 60
    #             sec_to_min = s_m / 60
    #             total_min = hour_to_min + min + sec_to_min
    #             speed = (start_speed / 60) * total_min
    #             m_speed = '%.2f' % speed
    #             if min_speed == start_speed:
    #                 print(a, m_speed, "km")
    #                 pre_distance_2 = speed
    #             else:
    #                 m_speed = speed + pre_distance_1 + pre_distance_2
    #                 m_distance = '%.2f' % m_speed
    #                 print(a, m_distance, "km")
    #         min_speed = start_speed
