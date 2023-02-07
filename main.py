import rpa as r

r.init(visual_automation = True)
r.error(True)

try:
    while True:
        r.click('menu.png')
        r.click('remove.png')
        r.wait(1)
except Exception as e:
    print(e)

r.close()
