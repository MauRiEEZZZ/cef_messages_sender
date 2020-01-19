import pysyslogclient, datetime, argparse
from cefevent import CEFEvent 

parser = argparse.ArgumentParser(description='Syslog CEF messages sender')
parser.add_argument('--host', type=str, help='destination host address')
parser.add_argument('--port', type=int, help='destination port')
parser.add_argument('--proto', type=str, help='Syslog protocol; UDP or TCP')
parser.add_argument('--number', type=int, help='Number of Syslog messages to be send')
args = parser.parse_args()

def get_mock_message(index):
    c = CEFEvent()  
    c.set_field('name', 'Mock Event Name') 
    c.set_field('deviceVendor', 'MCPforLife') 
    c.set_field('deviceProduct', 'cefevent') 
    c.set_field('dvchost', 'www.mcpforlife.com') 
    message = "This is a test event (Answer="+ str(index) + ")"
    c.set_field('message', message)  
    c.set_field('sourceAddress', '192.168.67.1') 
    c.set_field('sourcePort', 12345) 
    return c.build_cef() 

client = pysyslogclient.SyslogClientRFC5424(args.host, args.port, proto=args.proto)

for index in range(0, args.number):
    mymessage = get_mock_message(index)
    client.log(message=mymessage, program="")
client.close()
