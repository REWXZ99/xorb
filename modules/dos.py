from core.attack import Attacker

def start_dos(target, port, threads):
    attacker = Attacker(target, port, threads)
    attacker.run()
    return attacker

def stop_dos(attacker):
    if attacker:
        attacker.stop()
