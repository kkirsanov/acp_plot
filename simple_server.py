import SocketServer
import time


from optparse import OptionParser
import rpyc

import math
parser = OptionParser()

parser.add_option("-a", default="192.168.0.107", dest="ip", help="addres of robot", metavar="IP")
parser.add_option("-p", default=None, dest="port", help="remote port", metavar="PORT")



class RoboServer(SocketServer.BaseRequestHandler):
    def handle(self):
        def snd(st):
            self.request.sendall(str(time.time()) + " " + st + "\n")
        # self.request is the TCP socket connected to the client
        while True:
            cmd=""
            while True:
                cmd += self.request.recv(1)
                if "\n" in cmd:
                    break
                else:
                    time.sleep(0.001)
        
                cmd = cmd.split(" ")
                print cmd
                #snd(str(cmd))
                #return
                try:
                    if cmd[0].lower() == "setspeed":
                        snd('setspeed')
                    if cmd[0].lower() == "setbits":
                        snd('setbits')
                    if cmd[0].lower() == "getodometry":
                        z= [(time.time(), x) for x in range(int(cmd[1]))]
                        snd('getodometry ' + str(z))
                    if cmd[0].lower() == "getadc":
                        z= [(time.time(), x) for x in range(int(cmd[1]))]
                        snd('getadc ' + str(z))
                    if cmd[0].lower() == "help":
                        
                        snd('getodometry x::int, setspeed x::int, setbits X:[Bool], getadc x::int')
                except:
                    snd("FAIL")
if __name__ == "__main__":
    
    options, args = parser.parse_args()

    #ip = options.ip
    #port = options.port
    
    


    HOST, PORT = "192.168.1.13", 10003

    #server = SocketServer.TCPServer((HOST, PORT), RoboServer)

    #server.serve_forever()
    import rpyc.utils.registry as reg
    host = "192.168.1.27"
    registrar = reg.TCPRegistryClient("192.168.1.27")
    print rpyc.discover("ENGINE", host, timeout=10)#, registrar=registrar)/home/kkirsanov/arm/servers/
    
    
#import rpyc.utils.registry as reg
#registrar = reg.TCPRegistryClient(options.server)
#lst = rpyc.discover(service, host, timeout=timeout, registrar=registrar)
#odometry
#o = rpyc.connect(ip, int(port))
#o.root.Get()[0][1]

#engine
#u = rpyc.connect(ip, int(port))
#u.root.SetBSpeed(var1)
#u.root.SetASpeed(var2)
#u.root.SetBits("00000000")