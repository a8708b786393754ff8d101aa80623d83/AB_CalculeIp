import ipaddress
import argparse 

class CalculatorIP:
    def __init__(self, ip: str): 
        self.ip = ip
    
    def subnet(self): 
        try:
            first = list(ipaddress.ip_network(self.ip).hosts())[0]
            last = list(ipaddress.ip_network(self.ip).hosts()) [-1]
            netmask = ipaddress.IPv4Interface(self.ip).netmask
            hostmask = ipaddress.IPv4Interface(self.ip).hostmask 
            broadcast = ipaddress.IPv4Network(self.ip).broadcast_address
        except ValueError:
            print("Format non accepter")
            exit(0)
        else:
            print(f"first: {first} | last: {last} | netmask: {netmask} | hostmask: {hostmask} | broadcast: {broadcast}")        

    def host(self):
        liste = list(ipaddress.ip_network(self.ip).hosts())
        for i in liste: 
            print(i)

    def binaire(self): 
        try: 
            print("Format Binaire: {:b}".format(ipaddress.IPv4Address(self.ip)))
        except ipaddress.AddressValueError:
            print("Merci d'envlever le '/' est le nombre qui le suit svp")
            


def argument(): 
    args = argparse.ArgumentParser()
    args.add_argument('-i', '--ip', required=True, help='Entrez une adresse ip', type=str)
    return args.parse_args()

if __name__ == '__main__': 
    args = argument()    
    c = CalculatorIP(args.ip)
    c.subnet()    
    c.binaire()
    c.host()