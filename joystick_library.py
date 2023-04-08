import smbus

class joystick0x48(object):

    def __init__(self,pin=0,i2c_ch=1):
        self.address = 0x48
        self.A0 = 0x40
        self.A1 = 0x41
        self.A2 = 0x42
        self.A3 = 0x43
        self.pin = pin
        self.bus = smbus.SMBus(i2c_ch)

    def force_raw(self):
        if self.pin == 0:
            self.bus.write_byte(self.address,self.A0)
        elif self.pin == 1:
            address = 0x48
            A1 = 0x41
            self.bus.write_byte(self.address,self.A1)
        elif self.pin == 2:
            self.bus.write_byte(self.address,self.A2)
        elif self.pin == 3:
            self.bus.write_byte(self.address,self.A3)
        else:
            print("Incorrect value.  Pin defaulted to 0")
            self.bus.write_byte(self.address,self.A0)
        self.value = self.bus.read_byte(self.address)
        return self.value

    def force_scaled(self,scale=5):
        self.force_raw()
        self.scaled = self.force_raw() * scale / 255
        return self.scaled

class joystick0x49(object):

    def __init__(self,pin=0,i2c_ch=1):
        self.address = 0x49
        self.A0 = 0x40
        self.A1 = 0x41
        self.A2 = 0x42
        self.A3 = 0x43
        self.pin = pin
        self.bus = smbus.SMBus(i2c_ch)

    def force_raw(self):
        if self.pin == 0:
            self.bus.write_byte(self.address,self.A0)
        elif self.pin == 1:
            address = 0x48
            A1 = 0x41
            self.bus.write_byte(self.address,self.A1)
        elif self.pin == 2:
            self.bus.write_byte(self.address,self.A2)
        elif self.pin == 3:
            self.bus.write_byte(self.address,self.A3)
        else:
            print("Incorrect value.  Pin defaulted to 0")
            self.bus.write_byte(self.address,self.A0)
        self.value = self.bus.read_byte(self.address)
        return self.value

    def force_scaled(self,scale=5):
        self.force_raw()
        self.scaled = self.force_raw() * scale / 255
        return self.scaled

class joystick0x4B(object):

    def __init__(self,pin=0,i2c_ch=1):
        self.address = 0x4B
        self.A0 = 0x40
        self.A1 = 0x41
        self.A2 = 0x42
        self.A3 = 0x43
        self.pin = pin
        self.bus = smbus.SMBus(i2c_ch)

    def force_raw(self):
        if self.pin == 0:
            self.bus.write_byte(self.address,self.A0)
        elif self.pin == 1:
            address = 0x48
            A1 = 0x41
            self.bus.write_byte(self.address,self.A1)
        elif self.pin == 2:
            self.bus.write_byte(self.address,self.A2)
        elif self.pin == 3:
            self.bus.write_byte(self.address,self.A3)
        else:
            print("Incorrect value.  Pin defaulted to 0")
            self.bus.write_byte(self.address,self.A0)
        self.value = self.bus.read_byte(self.address)
        return self.value

    def force_scaled(self,scale=5):
        self.force_raw()
        self.scaled = self.force_raw() * scale / 255
        return self.scaled

def rolling_average(size, data):
    data = data[len(data)-size:len(data)]
    average = sum(data)/size
    return average

def scale(value, baseline):
    scaled_value = ((value-baseline)/baseline)*2
    return scaled_value

class Joystick:

    def __init__(self, address, pin_x, pin_y):
        self.UD = []
        self.LR = []
        self.SIZE = 8
        if address == "48":
            # I have NO IDEA why the pins are reversed but it works
            self.x = joystick0x48(pin_y)
            self.y = joystick0x48(pin_x)
        elif address == "49":
            self.x = joystick0x49(pin_y)
            self.y = joystick0x49(pin_x)
        elif address == "4B":
            self.x = joystick0x4B(pin_y)
            self.y = joystick0x4B(pin_x)
        else:
            print("Invalid address")
        print("Initiating...")
        for i in range(50):
            self.clear()
            self.UD.append(self.y.force_raw())
            self.LR.append(self.x.force_raw())
        self.BASELINE_Y = self.UD[-1]
        self.BASELINE_X = self.LR[-1]

    def clear(self):
        if len(self.UD) >= self.SIZE*2:
            self.UD = self.UD[-1*(self.SIZE)-1:-1]
        if len(self.LR) >= self.SIZE*2:
            self.LR = self.LR[-1*(self.SIZE)-1:-1]

    def read_y(self):
        self.clear()
        self.UD.append(self.y.force_raw())
        self.average_result_y = rolling_average(self.SIZE,self.UD)
        self.scaled_value_y = scale(self.average_result_y,self.BASELINE_Y)
        return round(self.scaled_value_y, 2)

    def read_x(self):
        self.clear()
        self.LR.append(self.x.force_raw())
        self.average_result_x = rolling_average(self.SIZE,self.LR)
        self.scaled_value_x = scale(self.average_result_x,self.BASELINE_X)
        return round(self.scaled_value_x, 2)
