import ms5837 #Pressure Sensor
from adafruit_ina219 import ADCResolution, BusVoltageRange, INA219 #Current Sensor
import board
import time

#Pressure Sensor Setup
sensor = ms5837.MS5837_30BA()

if not sensor.init():
    print("Sensor could not be initialized")
    exit(1)

if not sensor.read():
    print("Sensor read has failed!")
    exit(1)

print(("Pressure: %.2f psi") % (
    sensor.pressure(ms5837.UNITS_psi)
))

print(("Temperature: %.2f C") % (
    sensor.temperature(ms5837.UNITS_Centigrade),
))

sensor.setFluidDensity(ms5837.DENSITY_SALTWATER)
saltwaterDepth = sensor.depth()
print(("Depth: %.3f m") % saltwaterDepth)

print(("MSL Relative Altitude: %.2f m") % sensor.altitude())

#Current Sensor (INA219)
i2c_bus = board.I2C()
ina219 = INA219(i2c_bus)

ina219.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S
ina219.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S
#Change if Battery is not 16V
ina219.bus_voltage_range = BusVoltageRange.RANGE_16V

time.sleep(2)

while True:
    bus_voltage = ina219.bus_voltage
    shunt_voltage = ina219.shunt_voltage
    current = ina219.current
    power = ina219.power

    print("Voltage (VIN+) : {:6.3f}   V".format(bus_voltage + shunt_voltage))
    print("Voltage (VIN-) : {:6.3f}   V".format(bus_voltage))
    print("Shunt Voltage  : {:8.5f} V".format(shunt_voltage))
    print("Shunt Current  : {:7.4f}  A".format(current / 1000))
    print("Power Calc.    : {:8.5f} W".format(bus_voltage * (current / 1000)))
    print("Power Register : {:6.3f}   W".format(power))
    print("")

    if sensor.read():
        print(("P: %0.1f mbar \tT: %0.2f C \tDepth: %0.1f") % (
        sensor.pressure(), # Default is mbar (no arguments)
        sensor.temperature(), # Default is degrees C (no arguments)
	sensor.depth()
        ))
        print("")
    else: 
        print("Sensor read failed (LOOP)!")
        exit(1)
    
    time.sleep(2)
