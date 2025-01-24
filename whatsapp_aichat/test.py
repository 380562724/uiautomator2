from time import sleep

import uiautomator2 as u2

d = u2.connect('ff377427')
print(d.info)
d.press('home')
d.app_stop('com.whatsapp')
d.app_start('com.whatsapp', activity='com.whatsapp.HomeActivity')
# get the children or grandchildren
d(className='android.widget.ImageButton', resourceId="com.whatsapp:id/menuitem_search").click()
sleep(1)
d(className='android.widget.EditText', resourceId="com.whatsapp:id/search_input").clear_text()
sleep(1)
d(className='android.widget.EditText', resourceId="com.whatsapp:id/search_input").set_text('贾康')
sleep(1)
d.press('enter')
d(className='android.widget.RelativeLayout', resourceId="com.whatsapp:id/contact_row_container").click()
sleep(1)
d(className='android.widget.EditText', resourceId="com.whatsapp:id/entry").set_text('hello my friend')
sleep(1)
d(className='android.widget.FrameLayout', resourceId="com.whatsapp:id/send_container").click()



