import os
import subprocess

class ADBDeviceManager:
    def __init__(self):
        self.devices = self.get_connected_devices()

    def get_connected_devices(self):
        result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        devices_list = []
        lines = output.split('\n')
        for line in lines[1:]:
            if line:
                device_info = line.split('\t')[0]
                devices_list.append(device_info)
        return devices_list

    def install_app(self, device_id, app_path):
        subprocess.run(['adb', '-s', device_id, 'install', app_path])

    def uninstall_app(self, device_id, package_name):
        subprocess.run(['adb', '-s', device_id, 'uninstall', package_name])

    def take_screenshot(self, device_id, output_path):
        subprocess.run(['adb', '-s', device_id, 'shell', 'screencap', '-p', '/sdcard/screenshot.png'])
        subprocess.run(['adb', '-s', device_id, 'pull', '/sdcard/screenshot.png', output_path])
        subprocess.run(['adb', '-s', device_id, 'shell', 'rm', '/sdcard/screenshot.png'])

# Sample usage
if __name__ == '__main__':
    adb_manager = ADBDeviceManager()
    print('Connected devices:', adb_manager.devices)