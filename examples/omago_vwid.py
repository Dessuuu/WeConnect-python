import argparse

from weconnect import weconnect

from weconnect.elements.control_operation import ControlOperation


def main():
    
    parser = argparse.ArgumentParser(
        prog='fuelStatus',
        description='Example starting Battery status')
    parser.add_argument('-u', '--username', help='Volkswagen ID:n Käyttäjätunnus', required=True)
    parser.add_argument('-p', '--password', help='Volkswagen ID:n Salasana', required=True)
    parser.add_argument('--vin', help='Halutun auton VIN numero', required=True)

    args = parser.parse_args()

    print('#  Yhdistetään WeConnectiin')
    weConnect = weconnect.WeConnect(username=args.username, password=args.password, updateAfterLogin=False, loginOnInit=False)
    print('#  Kirjaudutaan sisään.')
    weConnect.login()
    print('#  Päivitetään auton tietoja.')
    weConnect.update()

    for vin, vehicle in weConnect.vehicles.items():
        if vin == args.vin:
            if "fuelStatus" in vehicle.domains \
                    and "rangeStatus" in vehicle.domains["fuelStatus"] \
                    and vehicle.domains["fuelStatus"].enabled:
                if vehicle.domains["fuelStatus"]["rangeStatus"]:
                    print('#   Auton tiedot:')
                    print("Kilometrilukema")
                    print(vehicle.domains["measurements"]["odometerStatus"].odometer.value)
                    print("Range")
                    print(vehicle.domains["measurements"]["rangeStatus"].electricRange.value)
                    


    print('  Ole hyvä! :)')


if __name__ == '__main__':
    main()
