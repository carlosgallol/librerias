import Rpi_i2c_driver
from time import *
mylcd = Rpi_i2c_driver.lcd()

mylcd.lcd_display_string("RPi I2C test", 1)
mylcd.lcd_display_string(" Custom chars", 2)
sleep(2)
mylcd.lcd_clear()

fontdata1 = [
        # Char 0 - Upper-left
        [ 0x00, 0x00, 0x03, 0x04, 0x08, 0x19, 0x11, 0x10 ],
        # Char 1 - Upper-middle
        [ 0x00, 0x1F, 0x00, 0x00, 0x00, 0x11, 0x11, 0x00 ],
        # Char 2 - Upper-right
        [ 0x00, 0x00, 0x18, 0x04, 0x02, 0x13, 0x11, 0x01 ],
        # Char 3 - Lower-left
        [ 0x12, 0x13, 0x1b, 0x09, 0x04, 0x03, 0x00, 0x00 ],
        # Char 4 - Lower-middle
        [ 0x00, 0x11, 0x1f, 0x1f, 0x0e, 0x00, 0x1F, 0x00 ],
        # Char 5 - Lower-right
        [ 0x09, 0x19, 0x1b, 0x12, 0x04, 0x18, 0x00, 0x00 ],
        # Char 6 - my test
        [ 0x1f,0x0,0x4,0xe,0x0,0x1f,0x1f,0x1f],
]
mylcd.lcd_load_custom_chars(fontdata1)
mylcd.lcd_write(0x80)
mylcd.lcd_write_char(0)
mylcd.lcd_write_char(1)
mylcd.lcd_write_char(2)
mylcd.lcd_write(0xC0)
mylcd.lcd_write_char(3)
mylcd.lcd_write_char(4)
mylcd.lcd_write_char(5)
sleep(2)
mylcd.lcd_clear()

mylcd.lcd_display_string_pos("Testing",1,1) # row 1, column 1
mylcd.lcd_display_string_pos("Testing",2,3) # row 2, column 3
sleep(2)

mylcd.lcd_clear()
sleep(1)
mylcd.backlight(0)

