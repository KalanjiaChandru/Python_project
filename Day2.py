

def Start_task_manager():
    task_list=[]

    while True:
        name =input('Enter the task Name || EXIT to stop')

        if name.upper() =='EXIT':
            print('Task have stopped')
            print(task_list)
            break

        status_choice=input('Status: 1.Pending | 2.In-Progress | 3.Completed:')
        status_mapping={"1": "Pending", "2": "In-Progress", "3": "Completed"}
        status=status_mapping.get(status_choice,'Unknown')
        task_enter={'name':name,'status':status}
        task_list.append(task_enter)
        print(f"currentList:{task_list}")
Start_task_manager()