import pyautogui, time, location_handler
pyautogui.click(111,1042)
pyautogui.typewrite('flow decision')
location_handler.locate_image('locations/a4cd913d-34cf-44af-b14c-62e56a3bb0b5.png')
pyautogui.click()
pyautogui.click()
c = location_handler.locate_image_drag('locations/39ee4fa2-79dd-4719-87e7-afa8ffc15692.png')
pyautogui.moveTo(c)
pyautogui.dragTo(914,626,2,pyautogui.easeInQuad)
pyautogui.click(1809,286)
pyautogui.typewrite('flag_setup_complete = True')
pyautogui.click(298,1037)
location_handler.locate_image('locations/317d712a-1cf8-4156-8c0b-886b18785f79.png')
pyautogui.click()
pyautogui.typewrite('flag_setup_complete')
pyautogui.hotkey('tab')
pyautogui.hotkey('up')
pyautogui.hotkey('up')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.typewrite('False')
pyautogui.click(307,1039)
pyautogui.click(79,270)
pyautogui.hotkey('ctrl','a')
pyautogui.typewrite('data table')
location_handler.locate_image('locations/7e92b32c-ae03-4935-8322-26abc39a4313.png')
pyautogui.click()
pyautogui.click()



c = location_handler.locate_image_drag('locations/4a617ea6-e2c3-4d44-af8f-334ef3aea3aa.png')
pyautogui.moveTo(c)
pyautogui.dragTo(1133,613,2,pyautogui.easeInQuad)
pyautogui.moveTo(946,620)
pyautogui.dragTo(1023,621)

pyautogui.click(161,266)
pyautogui.hotkey('ctrl','a')
pyautogui.typewrite('add data row')
location_handler.locate_image('locations/b9924f87-364c-4a55-8945-559534df6418.png')
pyautogui.click()
pyautogui.click()
c=location_handler.locate_image_drag('locations/27bb446a-5521-40ec-8c2d-69ab41a51149.png')
pyautogui.moveTo(c)
pyautogui.dragTo(714,739,2,pyautogui.easeInQuad)
location_handler.locate_image('locations/b9924f87-364c-4a55-8945-559534df6418.png')
pyautogui.click()
pyautogui.click()
c=location_handler.locate_image_drag('locations/27bb446a-5521-40ec-8c2d-69ab41a51149.png')
pyautogui.moveTo(c)
pyautogui.dragTo(1101,787,2,pyautogui.easeInQuad)
pyautogui.click(128,268)
pyautogui.hotkey('ctrl','a')
pyautogui.typewrite('assign')
location_handler.locate_image('locations/175876be-0dd8-4380-9d3e-331cb8cbc87d.png')
pyautogui.click()
pyautogui.click()
c=location_handler.locate_image_drag('locations/cefd3e23-ee68-4ff1-ad21-c1a426333d99.png')
pyautogui.moveTo(c)
pyautogui.dragTo(1065,847,2,pyautogui.easeInQuad)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.typewrite('flag_setup_complete')
time.sleep(0.25)
pyautogui.hotkey('tab')
pyautogui.typewrite('True')
