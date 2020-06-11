'''
SJF:(Shortest Job First) Algorithm by Python
Coder Osman Asgharian
The task is to find the Average Waiting Time and Average Turnaround Time of the given processes with their Burst Time using SJF Scheduling Algorithm.
SJF is a scheduling policy that selects the waiting process with the smallest execution time to execute next.
Priority Scheduling is a Non Pre-emptive and Pre-emptive Algorithm, hence the process which has the Least Burst Time is selected first.
Here we are considering Pre-emptive version of Priority Scheduling, hence the process which has the Least Burst Time will be served first and will be continued to be served till there is any other process with Lower Burst Time priority.
If there is any process with Lower Burst Time, then switch the process.
Start Time: Time at which the execution of the process starts
Completion Time: Time at which the process completes its execution
Turnaround Time: Completion Time - Arrival Time
Waiting Time: Turnaround Time - Burst Time
I have made use of 2 queues in the code:
Ready Queue: It stores all the processes which have already arrived.
Normal Queue: It stores all the processes which have not arrived yet.
'''
class SJF:

    def processData(self, num_p):
        p_data = []
        for i in range(num_p):
            tmp = []
            p_id = int(input("Enter Process ID: "))
            arrival_time = int(input(f"Enter Arrival Time for Process {p_id}: "))
            burst_time = int(input(f"Enter Burst Time for Process {p_id}: "))
            tmp.extend([p_id, arrival_time, burst_time, 0, burst_time])
            '''
            '0' is the state of the process. 0 means not executed and 1 means execution complete
            '''
            p_data.append(tmp)
        SJF.schedulingProcess(self, p_data)

    def schedulingProcess(self, p_data):
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_process = []
        p_data.sort(key=lambda x: x[1])
        '''
        Sort processes according to the Arrival Time
        '''
        while 1:
            ready_queue = []
            normal_queue = []
            temp = []
            for i in range(len(p_data)):
                if p_data[i][1] <= s_time and p_data[i][3] == 0:
                    temp.extend([p_data[i][0], p_data[i][1], p_data[i][2], p_data[i][4]])
                    ready_queue.append(temp)
                    temp = []
                elif p_data[i][3] == 0:
                    temp.extend([p_data[i][0], p_data[i][1], p_data[i][2], p_data[i][4]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[2])
                '''
                Sort processes according to Burst Time
                '''
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(ready_queue[0][0])
                for k in range(len(p_data)):
                    if p_data[k][0] == ready_queue[0][0]:
                        break
                p_data[k][2] = p_data[k][2] - 1
                if p_data[k][2] == 0:        #If Burst Time of a process is 0, it means the process is completed
                    p_data[k][3] = 1
                    p_data[k].append(e_time)
            if len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(normal_queue[0][0])
                for k in range(len(p_data)):
                    if p_data[k][0] == normal_queue[0][0]:
                        break
                p_data[k][2] = p_data[k][2] - 1
                if p_data[k][2] == 0:        #If Burst Time of a process is 0, it means the process is completed
                    p_data[k][3] = 1
                    p_data[k].append(e_time)
        t_time = SJF.calculateTurnaroundTime(self, p_data)
        w_time = SJF.calculateWaitingTime(self, p_data)
        SJF.printData(self, p_data, t_time, w_time, sequence_of_process)

    def calculateTurnaroundTime(self, p_data):
        total_turnaround_time = 0
        for i in range(len(p_data)):
            turnaround_time = p_data[i][5] - p_data[i][1]
            '''
            turnaround_time = completion_time - arrival_time
            '''
            total_turnaround_time = total_turnaround_time + turnaround_time
            p_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(p_data)
        '''
        average_turnaround_time = total_turnaround_time / num_p
        '''
        return average_turnaround_time

    def calculateWaitingTime(self, p_data):
        total_waiting_time = 0
        for i in range(len(p_data)):
            waiting_time = p_data[i][6] - p_data[i][4]
            '''
            waiting_time = turnaround_time - burst_time
            '''
            total_waiting_time = total_waiting_time + waiting_time
            p_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(p_data)
        '''
        average_waiting_time = total_waiting_time / num_p
        '''
        return average_waiting_time

    def printData(self, p_data, average_turnaround_time, average_waiting_time, sequence_of_process):
        p_data.sort(key=lambda x: x[0])
        '''
        Sort processes according to the Process ID
        '''
        print("p_id  Arrival_Time  Rem_Burst_Time      Completed  Orig_Burst_Time Completion_Time  Turnaround_Time  Waiting_Time")
        for i in range(len(p_data)):
            for j in range(len(p_data[i])):
                print(p_data[i][j], end="\t\t\t\t")
            print()
        print(f'Average Turnaround Time: {average_turnaround_time}')
        print(f'Average Waiting Time: {average_waiting_time}')
        print(f'Sequence of Process: {sequence_of_process}')

if __name__ == "__main__":
    num_p = int(input("Enter number of processes: "))
    sjf = SJF()
    sjf.processData(num_p)
