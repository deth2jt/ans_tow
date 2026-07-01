#!/usr/bin/python

import ast
import re

class FilterModule(object):
    def filters(self):
        return {
            'disk_select': self.a_filter
        }

    def a_filter(self, disk, disk_list, endStr):
        disk = ast.literal_eval(disk)
        for item in disk_list:
            if  disk['id'] == '' and  len(item.split()) == 2   and re.search(r'sd.*1',item.split()[0]):
                if ( disk.get('size') == item.split()[1].strip()  ):
                    disk['src'] =  re.sub(r"[^a-zA-Z]", "", item.split()[0])
                    return disk
            elif (  len(item.split()) >=4 and disk.get('size') == item.split()[1].strip() and  disk.get('type') == item.split()[2].strip() and disk.get('id') == item.split()[3].strip() ):
                if (re.search(r'nvme1n1p1',item.split()[0]) or re.search(r'nvme0n1p1',item.split()[0]) ):
                    disk['src'] =  re.sub(r"[^a-zA-Z0-9]", "", item.split()[0])
                    return disk
                elif (re.search(r'sd.*1',item.split()[0])):
                    disk['src'] =  re.sub(r"[^a-zA-Z]", "", item.split()[0])
                    return disk
            # else:
        disk['src'] = endStr
        return disk        