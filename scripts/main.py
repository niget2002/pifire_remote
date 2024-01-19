import requests
import time

DEVICE_IP='10.80.88.134'
data = {}
targets = { 'Probe1': 165}

def do_loop():
    r = requests.get(f'http://{DEVICE_IP}/api/current')
    current_data = r.json()

    r = requests.get(f'http://{DEVICE_IP}/api/hopper')
    hopper_data = r.json()

    for each in current_data['notify_data']:
        if each['type'] == "probe":
            if each['label'] == "Grill":
                data[each['label']] = current_data['current']['P'][each['label']]
            else:
                data[each['label']] = current_data['current']['F'][each['label']]
            data[f'{each["label"]}_target'] = each['target']

            if each['label'] not in targets:
                targets[each['label']] = each['target']

    data['status'] = current_data['status']['status']

    for each in current_data['status']['outpins'].keys():
        data[each] = current_data['status']['outpins'][each]

    units = current_data['status']['units']

    data['hopper'] = hopper_data['hopper_level']

def update_control():
    payload = { 'updated' : 'true', 'mode': 'Startup' }

    r = requests.post(f'http://{DEVICE_IP}/api/control', json = payload)


def update_target():
    r = requests.get(f'http://{DEVICE_IP}/api/current')
    current_data = r.json()  
    new_notify = current_data['notify_data']
    update_data = False

    for i, each in enumerate(new_notify):
        if each['type'] == 'probe':
            if each['target'] != targets[each['label']]:
                new_notify[i]['target'] = targets[each['label']]
                update_data = True

    this_notify = { 'notify_data': new_notify }

    if update_data:
        print('Temp Changed on a probe')
        r = requests.post(f'http://{DEVICE_IP}/api/control', json = this_notify )


def print_data():
    for each in data.keys():
        if len(each) <= 6:
            print(f'{each}:\t\t{data[each]}')
        else:
            print(f'{each}:\t{data[each]}')
    print()



def main():

#    do_loop()
#    print_data()
#    update_control()
    do_loop()
    print_data()
    update_target()
    do_loop()
    print_data()


    while True:
        do_loop()
        update_target()
        print_data()
        time.sleep(10)



if __name__ == "__main__":
    print("Starting Main")
    main()