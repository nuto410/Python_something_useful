import keyboard

def on_key_event(e):
    if e.event_type == keyboard.KEY_DOWN:
        print(f"按下按键: {e.name}")
keyboard.hook(on_key_event)

# 保持程序运行
keyboard.wait()
