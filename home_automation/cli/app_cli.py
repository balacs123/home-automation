import argparse
import getpass
import os
import signal
from argparse import ArgumentTypeError
from os.path import expanduser, exists

from cli.contants import *
from cli import services
from utils.exceptions import CLIBaseException


parser = argparse.ArgumentParser(description=
                                 '''
                                     A Command Line Interface to interact with Home automation system.
                                 ''')

parser.add_argument('-v', '--version', action='version', version='Home Automation version'.format(HA_CLI_VERSION))
automation_parsers = parser.add_subparsers(title='Home Automation Services', dest='service', help='Home Automation Services; E.g.: "Add_device" "Operate_device"')

# Get device list
get_device_parser = automation_parsers.add_parser('get_device', help='Get smart device list', add_help=False)
get_device_args_grp = get_device_parser.add_argument_group('Get available smart device list')

# Add new device
add_device_parser = automation_parsers.add_parser('add_device', help='Add new smart to application', add_help=False)
add_device_args_grp = add_device_parser.add_argument_group('Add new smart device')
add_device_args = list()
add_device_args.append(add_device_args_grp.add_argument('-id', '--device_id', required=True, type=str, help="Your smart device id"))
add_device_args.append(add_device_args_grp.add_argument('-n', '--device_name', required=True, type=str, help="Your smart device name"))
add_device_args.append(add_device_args_grp.add_argument('-o', '--device_operations', required=True, nargs='+',
                                                        help="Operations can perform by given smart device"))

usage = add_device_parser.format_usage()
add_device_parser.usage=usage
for a in add_device_args:
    a.metavar = ''

# Update a device
update_device_parser = automation_parsers.add_parser('update_device', help='Update a existing smart device', add_help=False)
update_device_args_grp = update_device_parser.add_argument_group('Update existing smart device')
update_device_args = list()
update_device_args.append(update_device_args_grp.add_argument('-id', '--device_id', required=True, type=str, help="Your smart device id"))
update_device_args.append(update_device_args_grp.add_argument('-n', '--device_name', required=True, type=str, help="Your smart device name"))
update_device_args.append(update_device_args_grp.add_argument('-o', '--device_operations', required=True, nargs='+',
                                                        help="Operations can perform by given smart device"))

usage = update_device_parser.format_usage()
update_device_parser.usage=usage
for a in update_device_args:
    a.metavar = ''
    
#Delete a device
delete_device_parser = automation_parsers.add_parser('delete_device', help='Delete a available home smart device', add_help=False)
delete_device_args = list()
delete_device_arg_grp = delete_device_parser.add_argument_group('Annotations Service Required Arguments')
delete_device_args.append(delete_device_arg_grp.add_argument('-id', '--device_id', required=True, type=str, help="device id to be removed"))

usage = delete_device_parser.format_usage()
delete_device_parser.usage=usage
for a in delete_device_args:
    a.metavar = ''

# Update a device status
update_status_parser = automation_parsers.add_parser('update_status', help='Update a existing smart device', add_help=False)
update_status_args_grp = update_status_parser.add_argument_group('Update existing smart device')
update_status_args = list()
update_status_args.append(update_status_args_grp.add_argument('-id', '--device_id', required=True, type=str, help="Your smart device id"))
update_status_args.append(update_status_args_grp.add_argument('-s', '--device_status', required=True, type=str, help="Your new smart device status"))

usage = update_status_parser.format_usage()
update_status_parser.usage=usage
for a in update_status_args:
    a.metavar = ''

args = parser.parse_args()

app_data = dict()
app_data['service'] = args.service

if app_data['service'] == 'add_device' or app_data['service'] =='update_device':
    app_data['device_id'] = args.device_id
    app_data['device_name'] = args.device_name
    app_data['device_operation'] = args.device_operations
    
elif app_data['service'] == 'delete_device':
    app_data['device_id'] = args.device_id

elif app_data['service'] == 'update_status':
    app_data['device_id'] = args.device_id
    app_data['device_status'] = args.device_status

try:
    request_handler = services.AutomationRequestHandler(app_data)
    request_handler.handle_request()
except CLIBaseException as err:
    print('Error : {}'.format(err.message))
except Exception as e:
    print('Error : {}'.format(e))