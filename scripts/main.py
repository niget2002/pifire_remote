import requests
import time

DEVICE_IP='10.80.88.134'
data = {}

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

    data['status'] = current_data['status']['status']

    for each in current_data['status']['outpins'].keys():
        data[each] = current_data['status']['outpins'][each]

    units = current_data['status']['units']

    data['hopper'] = hopper_data['hopper_level']


def main():

    while True:

        do_loop()

        for each in data.keys():
            if len(each) <= 6:
                print(f'{each}:\t\t{data[each]}')
            else:
                print(f'{each}:\t{data[each]}')

        print()
        time.sleep(10)



if __name__ == "__main__":
    print("Starting Main")
    main()